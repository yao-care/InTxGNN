#!/usr/bin/env python3
"""市場段落的許可證表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 CaTxGNN／DETxGNN／UkTxGNN 同名檔）。

為什麼：「## India Market Information」段落原本是 AI 寫的自由格式表（多數表頭「Authorization Number | Product Name | Dosage Form |
Approved Indication」，Approved Indication 全是「Not recorded」；known_use_pages 的頁是「Licence | Product | Dosage form | Status」），
只列前幾筆，表上下另有「The main five are shown below.」之類的說明句。資料集每週變（Is_discontinued），AI 表不會跟著改，
跟事實矛盾時 checker 擋整頁。改成程式依證據包（data/bundles/<藥>/drug_bundle.json 的 tfda.records）產生，每週排程
（license_adapter.sync_tables）自動同步。

本站的資料不是主管機關許可證：是第三方整理的印度藥品價格資料集（junioralive/Indian-Medicine-Dataset；id、name、
pack_size_label、Is_discontinued），CDSCO 核准狀態不在資料裡（同概覽表狀態列的口徑）。
表的內容（全程不用 AI；品名、包裝照資料集原文，不翻譯）：
  | Dataset ID | Product Name | Pack Size | Status |
  - 列＝證據包存的全部紀錄（收集器最多存 20 筆），排序：未停產（Valid）在前、Discontinued 在後，同狀態依 ID 數字。
  - 狀態欄：資料集 Is_discontinued＝TRUE（license_adapter 寫成 status「Discontinued」、license_status cancelled）→「Discontinued」，
    其餘→「Valid」（本站概覽表與 known_use_pages 表既有的寫法，.claude/license_labels/InTxGNN.json）。
  - 不放成分欄：證據包 ingredients 只收了資料集的 short_composition1（複方的第二成分 short_composition2 沒收），照抄會誤導。
  - 不放廠商欄：廠商名照抄會被 checker 誤判（2026-11-24 實測 itraconazole「GRAF Laboratories」被 P5 當成知識圖譜字樣），
    廠商名也不是概覽表、正文張數用到的事實。
  - 表後一句來源（SOURCE）；證據包只收到部分紀錄（total_matches 大於紀錄數，或事實層 partial）時另加 PART_NOTE
    （本站 known_use_pages 既有的句子）。證據包沒有任何紀錄時不放表，改一句 NONE_LINE。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、刪句工具與 gate 用來分辨程式寫的字）。
放在哪：「## India Market Information」段落的第一張許可證表（表頭含 Authorization／Licen／Product）；段落裡沒有表時放在段落開頭；
  沒有這個段落的公開頁（證據包有紀錄）在 Safety Considerations 之前補段落（2026-11-24 第三輪 add_section；noindex 頁不補）。表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照改寫）；
  段落裡舊的 PART_NOTE 行一律拿掉（程式區塊自己會寫）。

第一次換表（--migrate）時另做兩件事（之後頁面上已是程式區塊，不會再發生）：
  - 市場段落裡只講「舊表列了幾筆／前 5 筆／以下為例」的整句（is_caption）與句尾子句拿掉；判斷用字詞白名單（CAP_WORDS），
    句子裡有白名單以外的字（品名、劑型…）就不動；查核紀錄的更正文字／錨點所在的句子不動。
  - 錨在被取代的表或說明上的查核紀錄標 status: superseded＋superseded_by（紀錄保留、頁面不顯示框，同 Tw 慣例）。
資料來源：預設讀快照 snapshots/in_licenses.json.gz 的 rows／show（scripts/build_license_snapshot.py 依證據包用 program_rows 算好）；
  --bundles 改讀 data/bundles（每週排程用）。gate（src/intxgnn/regulatory/licenses.py）檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程 license_adapter.sync_tables（--bundles）。
  sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.py，所以也會重新產生（取代 notes 裡模型寫的表）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [--migrate] [--dry-run] [--verbose] [頁 ...]
"""
import datetime as dt
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "in_licenses.json.gz"
SEC = "## India Market Information"
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = "| Dataset ID | Product Name | Pack Size | Status |"
SEP = "|------|------|------|------|"
# 來源句不寫 marketed／valid／discontinued 等狀態字：checker M3 會把它當成正文的上市說法（CaTxGNN 2026-11-24 實測）
SOURCE = ("Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian "
          "medicine prices; dataset ID, product name and pack size as recorded in the dataset. "
          "CDSCO approval status is not included in this data.")
PART_NOTE = "Only part of the licence list is held in the data; the list may be incomplete."
NONE_LINE = "No product containing this ingredient is recorded in the Indian medicine dataset used for this report."
SUPERSEDED_BY = "programmatic product table (scripts/sync_license_tables.py, 2026-11-24, from the Indian Medicine Dataset)"
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
# 2026-11-24 第三輪：補段落時新增的標題行（SEC）也放行
PAGE_NOTE = r"^(" + "|".join(re.escape(x) for x in (BEGIN, END, SOURCE, PART_NOTE, NONE_LINE, SEC)) + r")$"


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def _disc(r):
    return str(r.get("license_status") or "").lower() == "cancelled" or str(r.get("status") or "").strip().lower() == "discontinued"


def _cap(x):
    x = cell(x, 60)
    return x[:1].upper() + x[1:]


def table_rows(recs):
    seen, rows = set(), []
    for r in recs:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        d = _disc(r)
        num = int(k) if k.isdigit() else 10 ** 9
        rows.append((1 if d else 0, num, k, f"| {k} | {cell(r.get('brand_name_en') or r.get('brand_name_zh'), 80)} | "
                                         f"{_cap(r.get('dosage_form'))} | "
                                         f"{'Discontinued' if d else 'Valid'} |"))
    return [x[3] for x in sorted(rows)]


def program_rows(tf, fc=None):
    """證據包 tfda → (表格列, 表下的程式文字列)。build_license_snapshot.py 存進快照，gate 依它比對。"""
    recs = (tf or {}).get("records") or []
    rows = table_rows(recs)
    if not rows:
        return [], [NONE_LINE]
    partial = int((tf or {}).get("total_matches") or 0) > len(recs) or bool((fc or {}).get("partial"))
    return rows, [SOURCE] + ([PART_NOTE] if partial else [])


def program_block(rows, show):
    if not rows:
        return list(show)
    out = [HEAD, SEP] + list(rows)
    for x in show:  # 每句各一段（Markdown 不會把來源句與部分紀錄說明接成一段）
        out += ["", x]
    return out


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


# ---- 舊表說明句（--migrate） ----
NUMW = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)"
CAP_WORDS = set("""listed shown shows show lists list listing showing below above here table selection representative examples example
main first only the of them these those ones one a an are is be may partial and as in total all valid single-ingredient single-entity
licences licence licenses license authorizations authorization authorisations authorisation dins din products product entries entry
records record registrations registration data local up to shown selected sample following displayed is are main
one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
sixth seventh eighth ninth tenth fifth at least full found india single-entry""".split())
DISPLAY_KEY = re.compile(r"^\s*these are\b|\b(shown|shows|showing|lists|table|examples?|selection|representative|selected|sample|displayed|below|above|here)\b|:\s*$", re.I)
SPLIT = re.compile(r"(?<=[.!?:])\s+(?=[A-Z*\[(])")


def _words(s):
    s = re.sub(r"[*_()\[\]]", " ", s)
    return [w.lower() for w in re.findall(r"[A-Za-z][\w-]*|\d+", s)]


def is_caption(s):
    """整句只講表上列了幾筆（字都在白名單、且有顯示用字）"""
    x = s.strip()
    if not x or not DISPLAY_KEY.search(x):
        return False
    if re.match(r"\W*the (?:data|local data|records?) (?:lists?|shows?|contains?)\b", x, re.I):
        return False  # 「The data lists 20 valid single-ingredient licences.」講資料裡的張數，不是表的說明
    w = _words(x)
    return bool(w) and all(t in CAP_WORDS or t.isdigit() for t in w)


CLAUSE = re.compile(r"(\s*;\s*|,\s+so\s+|,\s+and\s+(?=the (?:table|list)\b)|\s+\()([^;()]+?)(\)?)(?=[.]\*?\)?\*?$)")


def _trim_sentence(x):
    """回傳 (新句子或 None＝整句拿掉, 拿掉的文字)"""
    core = x.strip()
    m = CLAUSE.search(core)
    if m and (m.group(1).strip() != "(" or m.group(3)) and is_caption(m.group(2) + ".") and core[:m.start()].strip():
        rest = core[:m.start()] + core[m.end(3) if m.group(3) else m.end(2):]
        if not is_caption(rest):  # 句子前半講張數（「Eight valid licences are on record」）：只拿掉講表的子句
            return rest, m.group(0).strip()
    m = re.match(r"(.+?)(?:;|,\s+and)\s+((?:the (?:others|remaining|rest|remainder)|none)\b.*)$", core, re.I)
    if m and is_caption(m.group(1) + "."):
        return m.group(2)[:1].upper() + m.group(2)[1:], m.group(1) + ";"
    if is_caption(core):
        return None, core
    return x, ""


def _caption_trim(line, protect=()):
    if not line.strip() or line.startswith(("|", "#", "<!--", "---", ">", "{:")):
        return line, []
    lead = line[:len(line) - len(line.lstrip())]
    sents = SPLIT.split(line.strip())
    out, gone = [], []
    for x in sents:
        if any(p and (x.strip() in p or p in x) for p in protect):
            out.append(x)
            continue
        nx, g = _trim_sentence(x)
        if g:
            gone.append(g)
        if nx is not None:
            out.append(nx)
    if not gone:
        return line, []
    return (lead + " ".join(out)) if out else "", gone


def _section(lines):
    if SEC not in lines:
        return None, None
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _is_license_head(lines, k):
    return lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|")) and re.search(r"Authori[sz]ation|Licen|Product", lines[k]) \
        and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])


def _splice(lines, x, y, blk):
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def process(text, rows, show, migrate=False, protect=()):
    """回傳 (新內容, 拿掉的文字列)。沒有市場段落時原樣。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    a, b = _section(lines)
    if a is None:
        return add_section(text, rows, show), []
    blk = wrap(program_block(rows, show))
    removed = []
    sec = lines[a:b]
    if BEGIN in sec and END in sec:
        x = lines.index(BEGIN, a)
        lines = _splice(lines, x, lines.index(END, x) + 1, blk)
    else:
        tb = [k for k in range(a, b) if _is_license_head(lines, k)]
        if tb:
            y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            removed += lines[tb[0]:y + 1]
            lines = _splice(lines, tb[0], y + 1, blk)
        else:
            lines = _splice(lines, a, a, blk)
    # 段落裡舊的「Only part of the licence list …」行（known_use_pages 寫在舊表後）拿掉：程式區塊依證據包自己寫 PART_NOTE
    a, b = _section(lines)
    i0, i1 = lines.index(BEGIN, a), lines.index(END, a)
    for k in range(b - 1, a - 1, -1):
        if not (i0 <= k <= i1) and lines[k].strip() == PART_NOTE:
            removed.append(lines[k].strip())
            del lines[k]
    if migrate:
        a, b = _section(lines)
        i0, i1 = lines.index(BEGIN, a), lines.index(END, a)
        for k in range(a, b):
            if i0 <= k <= i1:
                continue
            nl, g = _caption_trim(lines[k], protect)
            if g:
                lines[k] = nl
                removed += g
    t = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t, removed


# 2026-11-24 第三輪（用戶決定，照 JpTxGNN 第二輪 add_section）：公開頁整頁沒有「## India Market Information」段落、證據包卻有紀錄的，
# 補一個段落放程式表。位置：「## Safety Considerations」之前（預測頁固定順序）；沒有就「## Conclusion and Next Steps」之前；再沒有就「## Disclaimer」之前。
# noindex 頁與證據包沒有紀錄的頁不補。
ADD_BEFORE = ("Safety Considerations", "Conclusion and Next Steps", "Disclaimer")


def is_noindex(text):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    return bool(re.search(r"^noindex:\s*true", fm, re.M))


def add_section(text, rows, show):
    if is_noindex(text) or not rows:
        return text
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return text
    head = lines[:at]
    while head and not head[-1].strip():
        head.pop()
    sec = ["", SEC, ""] + wrap(program_block(rows, show)) + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(head + sec + lines[at:]))


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def bundle_for(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def _protect():
    out = {}
    f = ROOT / "docs/_data/drug_reviews.json"
    if f.exists():
        for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
            if r.get("status"):
                continue
            out.setdefault(r["file"][:-3], []).extend(x.strip() for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def run(from_bundles=False, check=False, only=None, migrate=False, removed_out=None):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    prot = _protect() if migrate else {}
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = bundle_for(p.stem)
            if b is None:
                continue
            rows, show = program_rows(b.get("tfda") or {})
            e = snap.get(p.stem)
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, show = e["rows"], e["show"]
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new, gone = process(t0, rows, show, migrate, prot.get(p.stem, ()))
        if gone and removed_out is not None:
            removed_out[p.stem] = gone
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def supersede(removed_by_page, today=None):
    """--migrate：錨在拿掉的文字上、新頁面上也找不到的查核紀錄標 superseded（紀錄保留）。回傳標記的 id"""
    data = ROOT / "docs/_data/drug_reviews.json"
    doc = json.loads(data.read_text(encoding="utf-8"))
    today = today or dt.date.today().isoformat()
    marked = []
    for r in doc["records"]:
        gone = removed_by_page.get(r["file"][:-3])
        if not gone or r.get("status") or r.get("action") not in ("correct", "annotate", "rereview"):
            continue
        page = (ROOT / "docs/_drugs" / r["file"]).read_text(encoding="utf-8")
        page = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", page, flags=re.S)
        page = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", page, flags=re.S)
        loc = r.get("anchor") or (r.get("replacement") if r["action"] == "correct" else r.get("claim")) or r.get("claim")
        if loc and loc.strip() and loc in page:
            continue
        keys = [x for x in (r.get("anchor"), r.get("replacement"), r.get("claim")) if x and x.strip()]
        if any(any(k.strip() in g or (g.strip() and g.strip() in k) for g in gone) for k in keys):
            r["status"] = "superseded"
            r["superseded_by"] = SUPERSEDED_BY
            r["superseded_on"] = today
            marked.append(r["id"])
    if marked:
        data.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return marked


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    migrate = "--migrate" in a
    check = "--check" in a or "--dry-run" in a
    rm = {}
    ch = run(from_bundles="--bundles" in a, check=check, only=only, migrate=migrate, removed_out=rm)
    print(f"程式許可證表：{'待改' if check else '改'} {len(ch)} 頁" + (f"；拿掉舊表說明 {sum(1 for v in rm.values() for x in v if not x.startswith('|'))} 處（{len(rm)} 頁）" if migrate else ""))
    if migrate and "--verbose" in a:
        for k, v in rm.items():
            for x in v:
                if not x.startswith("|"):
                    print(f"  {k}\t{x}")
    if migrate and not check:
        ids = supersede(rm)
        print(f"錨在被取代的表或說明上的查核紀錄標 superseded：{len(ids)} 筆")
        for i in ids:
            print("  ", i)
    if "--check" in a:
        sys.exit(1 if ch else 0)
