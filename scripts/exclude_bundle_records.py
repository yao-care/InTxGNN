#!/usr/bin/env python3
"""依 config/license_exclusions.json 把成分欄錯植的資料集品項從證據包排除（2026-11-24，用戶決定第三輪 A）。

為什麼：證據包（data/bundles/<藥>/drug_bundle.json）的 tfda.records 是 src/intxgnn/collectors/infda.py 依 drug_mapping.csv
（資料集成分欄→DrugBank ID）收的；資料集把幾個 cholecalciferol（維生素 D3，劑量以 IU 計）注射劑的成分寫成「Calcitriol (600000IU)」，
所以收進 calcitriol。這支把表內品項移到 tfda.excluded_records（附 reason／basis／excluded），total_matches 扣掉
（資料集原本算進本藥的品項，每號只扣一次；已扣過的號記在 tfda.excluded_ids）。只動表內的號碼、可重複執行。
收集器 infda.py 也照同一張表排除，重新收集不會再收進來。

用法（repo 根目錄，先還原 data/）：python3 scripts/exclude_bundle_records.py [--check]
  --check：只列要改的，有要改的就 exit 1
每週許可證排程（.github/workflows/license-refresh.yml）在 license_refresh 前先跑。
"""
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "license_exclusions.json"


def load():
    return json.loads(CFG.read_text(encoding="utf-8")).get("exclusions") or []


def _mapped():
    """data/processed/drug_mapping.csv 的 (license_id, DrugBank ID) 配對；沒有檔回 None"""
    import csv
    f = ROOT / "data" / "processed" / "drug_mapping.csv"
    if not f.exists():
        return None
    with f.open(encoding="utf-8") as fh:
        return {(str(r.get("license_id") or "").strip(), str(r.get("drugbank_id") or "").strip().upper()) for r in csv.DictReader(fh)}


def main(check=False):
    today = dt.date.today().isoformat()
    by_bundle = {}
    for e in load():
        by_bundle.setdefault(e["bundle"], []).append(e)
    changed, missing = [], []
    mapped = _mapped()
    for bundle, items in sorted(by_bundle.items()):
        f = ROOT / "data" / "bundles" / bundle / "drug_bundle.json"
        if not f.exists():
            missing.append(bundle)
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        tf = b.get("tfda") or {}
        recs = tf.get("records") or []
        done = set(tf.get("excluded_ids") or [])
        exc = tf.get("excluded_records") or []
        moved = []
        for e in items:
            lid = str(e["license_id"]).strip()
            hit = [r for r in recs if str(r.get("license_id") or "").strip() == lid]
            if hit:
                recs = [r for r in recs if str(r.get("license_id") or "").strip() != lid]
                for r in hit:
                    exc.append({**r, "excluded": today, "reason": e["reason"], "basis": e["basis"]})
                moved.append(lid)
            if lid not in done:
                # 2026-11-24 追加：只有收集器確實算進本藥的號才扣 total_matches（drug_mapping.csv 把該號對到本藥 DrugBank ID；
                # drug_mapping 只對成分欄第一個成分，第二成分才寫 Calcitriol 的鈣劑複方本來就不在總數裡）。
                # 沒有 drug_mapping 時不扣、也不記進 excluded_ids（下次有 drug_mapping 時再判斷）。
                if not hit and (mapped is None or (lid, str(e.get("drugbank_id") or "").upper()) not in mapped):
                    continue
                done.add(lid)
                if isinstance(tf.get("total_matches"), int) and tf["total_matches"] > 0:
                    tf["total_matches"] -= 1
                if lid not in moved:
                    moved.append(lid)
        if moved:
            changed.append((bundle, sorted(set(moved))))
            if not check:
                tf["records"], tf["excluded_records"], tf["excluded_ids"] = recs, exc, sorted(done)
                b["tfda"] = tf
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    for bundle, ids in changed:
        print(f"{'要排除' if check else '排除'} {bundle}：{', '.join(ids)}")
    if missing:
        print(f"✗ 找不到證據包：{', '.join(missing)}", file=sys.stderr)
        return 2
    print(f"證據包排除：{len(changed)} 個證據包{'要改' if check else '已改'}（表內 {sum(len(v) for v in by_bundle.values())} 筆）")
    return 1 if (check and changed) else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
