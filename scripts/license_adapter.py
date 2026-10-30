"""IN（Indian Medicine Dataset，GitHub 公開資料集）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

IN 站的本地資料原本就是這份公開資料集（config/fields.yaml：「Indian Medicine Dataset (GitHub/Kaggle)」），不是 CDSCO 許可證；
印度沒有全國性的產品許可證資料庫，CDSCO 網站在印度境外解析不到網域。用戶 2026-10-30 選「沿用現有來源排程」。
來源：https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/DATA/indian_medicine_data.csv（與站上 data/raw 同一檔，
2026-10-30 比對大小一致；資料集持續更新，最近一次 2026-06-27）。欄位 id（＝證據包 license_id）、Is_discontinued（TRUE／FALSE）。
寫回：TRUE → status「Discontinued」、license_status cancelled；FALSE → 維持原值（空白，reviewer 視為有效）。新檔沒有的 id 保留原狀態。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/in_medicine_discontinued.json"
URL = "https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/DATA/indian_medicine_data.csv"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    rows = csv.DictReader(io.StringIO(r.content.decode("utf-8-sig")))
    if "id" not in (rows.fieldnames or []) or "Is_discontinued" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    return [{"id": (x["id"] or "").strip(), "disc": (x["Is_discontinued"] or "").strip().upper()} for x in rows if x.get("id")]


def validate(new, old):
    p = []
    if len(new) < 100000:
        p.append(f"只解析出 {len(new)} 筆（約 25 萬），疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["id"]: r["disc"] == "TRUE" for r in new if r["disc"] in ("TRUE", "FALSE")}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if new:
        if rec.get("status") == "Discontinued" and rec.get("license_status") == "cancelled":
            return False
        rec["status"], rec["license_status"] = "Discontinued", "cancelled"
        return True
    if rec.get("license_status") == "cancelled" and rec.get("status") == "Discontinued":
        rec["status"], rec["license_status"] = "", "valid"  # 資料集改回未停產
        return True
    return False
