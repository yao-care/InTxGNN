#!/usr/bin/env python3
"""
Generate news monitoring keyword list

Extract keywords from:
- DrugBank vocabulary (drug names)
- Disease vocabulary (disease names)
- Synonyms mapping

Output: data/news/keywords.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_json(path: Path) -> dict | list:
    """Load JSON file"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_synonyms(path: Path) -> dict:
    """Load synonyms mapping"""
    if not path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_drugbank_vocab() -> list[dict]:
    """Load DrugBank vocabulary"""
    vocab_path = DATA_DIR / "external" / "drugbank_vocab.csv"
    if not vocab_path.exists():
        print(f"Warning: {vocab_path} not found")
        return []

    import pandas as pd
    df = pd.read_csv(vocab_path)

    drugs = []
    for _, row in df.iterrows():
        drug_id = row.get("drugbank_id", "")
        drug_name = row.get("drug_name", "")
        if drug_id and drug_name:
            drugs.append({
                "drugbank_id": drug_id,
                "name": drug_name
            })
    return drugs


def load_disease_vocab() -> list[dict]:
    """Load disease vocabulary"""
    vocab_path = DATA_DIR / "external" / "disease_vocab.csv"
    if not vocab_path.exists():
        print(f"Warning: {vocab_path} not found")
        return []

    import pandas as pd
    df = pd.read_csv(vocab_path)

    diseases = []
    for _, row in df.iterrows():
        disease_id = row.get("disease_id", "")
        disease_name = row.get("disease_name", "")
        if disease_id and disease_name:
            diseases.append({
                "disease_id": disease_id,
                "name": disease_name
            })
    return diseases


# Generic keyword patterns for common disease categories
GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma"
    ],
    "_cardiovascular": [
        "cardiovascular", "atherosclerosis", "arteriosclerosis",
        "coronary", "vascular disease"
    ],
    "_heart_disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy"
    ],
    "stroke": ["stroke", "ischemic stroke", "cerebrovascular"],
    "herpes zoster": ["herpes", "zoster", "varicella"],
    "dementia": ["dementia", "alzheimer", "cognitive impairment"],
    "diabetes": ["diabetes", "diabetic", "hyperglycemia", "insulin resistance"],
    "hypertension": ["hypertension", "high blood pressure", "hypertensive"],
}


def main():
    print("Loading data files...")

    # Load vocabularies
    drugbank_vocab = load_drugbank_vocab()
    disease_vocab = load_disease_vocab()
    synonyms = load_synonyms(DATA_DIR / "news" / "synonyms.json")

    print(f"  - DrugBank vocabulary: {len(drugbank_vocab)} drugs")
    print(f"  - Disease vocabulary: {len(disease_vocab)} diseases")
    print(f"  - Synonyms: {len(synonyms.get('indication_synonyms', {}))} indication synonyms")

    # Build drug keywords list
    drugs_keywords = []
    drug_synonyms = synonyms.get("drug_synonyms", {})

    for drug in drugbank_vocab:
        drug_name = drug["name"]
        drug_id = drug["drugbank_id"]

        # English keywords
        keywords_en = [drug_name.lower()]

        # Add synonyms if available
        if drug_name in drug_synonyms:
            for syn in drug_synonyms[drug_name]:
                if syn.lower() not in keywords_en:
                    keywords_en.append(syn.lower())

        # Hindi/local language keywords (if available in synonyms)
        keywords_local = drug_synonyms.get(drug_name, [])

        drugs_keywords.append({
            "drugbank_id": drug_id,
            "name": drug_name,
            "keywords": {
                "en": keywords_en,
                "local": keywords_local
            }
        })

    print(f"\nProcessed drug keywords: {len(drugs_keywords)} drugs")

    # Build indication keywords list
    indications_keywords = []
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # Track unique diseases to avoid duplicates
    seen_diseases = set()

    for disease in disease_vocab:
        disease_name = disease["name"]
        disease_id = disease["disease_id"]

        if disease_name.lower() in seen_diseases:
            continue
        seen_diseases.add(disease_name.lower())

        # English keywords
        keywords_en = [disease_name.lower()]

        # Local language synonyms
        keywords_local = indication_synonyms.get(disease_name, [])

        # Also check lowercase version
        if not keywords_local:
            keywords_local = indication_synonyms.get(disease_name.lower(), [])

        indications_keywords.append({
            "disease_id": disease_id,
            "name": disease_name,
            "keywords": {
                "en": keywords_en,
                "local": keywords_local
            }
        })

    # Add generic keyword patterns
    for pattern_name, patterns in GENERIC_KEYWORD_PATTERNS.items():
        if pattern_name.lower() not in seen_diseases:
            keywords_local = indication_synonyms.get(pattern_name, [])
            indications_keywords.append({
                "disease_id": f"generic_{pattern_name}",
                "name": pattern_name.lstrip("_"),
                "keywords": {
                    "en": patterns,
                    "local": keywords_local
                }
            })

    print(f"Processed indication keywords: {len(indications_keywords)} indications")

    # Output
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "drug_count": len(drugs_keywords),
        "indication_count": len(indications_keywords),
        "drugs": drugs_keywords,
        "indications": indications_keywords
    }

    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - Drug keywords: {len(drugs_keywords)}")
    print(f"  - Indication keywords: {len(indications_keywords)}")


if __name__ == "__main__":
    main()
