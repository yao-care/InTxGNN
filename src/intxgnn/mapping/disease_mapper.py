"""Disease mapping module - India indication mapping to TxGNN disease ontology

Since India uses English in medical documentation, this mapper handles:
1. English medical term variations and abbreviations
2. Common Hindi medical terms (transliterated)
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# English medical term variations and Hindi terms -> standard English
DISEASE_DICT = {
    # === Cardiovascular System ===
    "hypertension": "hypertension",
    "high blood pressure": "hypertension",
    "HTN": "hypertension",
    "hypotension": "hypotension",
    "low blood pressure": "hypotension",
    "heart disease": "heart disease",
    "cardiac disease": "heart disease",
    "myocardial infarction": "myocardial infarction",
    "MI": "myocardial infarction",
    "heart attack": "myocardial infarction",
    "angina": "angina",
    "angina pectoris": "angina",
    "chest pain": "angina",
    "arrhythmia": "arrhythmia",
    "irregular heartbeat": "arrhythmia",
    "atrial fibrillation": "atrial fibrillation",
    "AF": "atrial fibrillation",
    "heart failure": "heart failure",
    "CHF": "heart failure",
    "congestive heart failure": "heart failure",
    "atherosclerosis": "atherosclerosis",
    "hardening of arteries": "atherosclerosis",
    "DVT": "deep vein thrombosis",
    "deep vein thrombosis": "deep vein thrombosis",
    "stroke": "stroke",
    "CVA": "stroke",
    "cerebrovascular accident": "stroke",
    # Hindi terms
    "dil ki bimari": "heart disease",
    "uchh raktchap": "hypertension",

    # === Respiratory System ===
    "asthma": "asthma",
    "bronchial asthma": "asthma",
    "wheezing": "asthma",
    "bronchitis": "bronchitis",
    "chronic bronchitis": "bronchitis",
    "pneumonia": "pneumonia",
    "lung infection": "pneumonia",
    "tuberculosis": "tuberculosis",
    "TB": "tuberculosis",
    "pulmonary TB": "tuberculosis",
    "COPD": "chronic obstructive pulmonary disease",
    "chronic obstructive pulmonary disease": "chronic obstructive pulmonary disease",
    "cough": "cough",
    "cold": "common cold",
    "common cold": "common cold",
    "influenza": "influenza",
    "flu": "influenza",
    "rhinitis": "rhinitis",
    "allergic rhinitis": "allergic rhinitis",
    "hay fever": "allergic rhinitis",
    "sinusitis": "sinusitis",
    "sinus infection": "sinusitis",
    "dyspnea": "dyspnea",
    "shortness of breath": "dyspnea",
    "emphysema": "emphysema",
    # Hindi terms
    "dama": "asthma",
    "khansi": "cough",
    "sardi": "common cold",

    # === Digestive System ===
    "gastritis": "gastritis",
    "stomach inflammation": "gastritis",
    "gastric ulcer": "gastric ulcer",
    "peptic ulcer": "peptic ulcer",
    "stomach ulcer": "gastric ulcer",
    "duodenal ulcer": "duodenal ulcer",
    "dyspepsia": "dyspepsia",
    "indigestion": "dyspepsia",
    "diarrhea": "diarrhea",
    "loose motion": "diarrhea",
    "constipation": "constipation",
    "enteritis": "enteritis",
    "colitis": "colitis",
    "ulcerative colitis": "ulcerative colitis",
    "IBS": "irritable bowel syndrome",
    "irritable bowel syndrome": "irritable bowel syndrome",
    "dysentery": "dysentery",
    "hepatitis": "hepatitis",
    "liver disease": "hepatitis",
    "hepatitis B": "hepatitis B",
    "hepatitis C": "hepatitis C",
    "cirrhosis": "cirrhosis",
    "liver cirrhosis": "cirrhosis",
    "gallstone": "gallstone",
    "cholelithiasis": "gallstone",
    "cholecystitis": "cholecystitis",
    "pancreatitis": "pancreatitis",
    "nausea": "nausea",
    "vomiting": "vomiting",
    "GERD": "gastroesophageal reflux disease",
    "gastroesophageal reflux": "gastroesophageal reflux disease",
    "acid reflux": "gastroesophageal reflux disease",
    "acidity": "gastroesophageal reflux disease",
    # Hindi terms
    "pet dard": "abdominal pain",
    "kabz": "constipation",
    "dast": "diarrhea",

    # === Nervous System ===
    "epilepsy": "epilepsy",
    "seizure": "epilepsy",
    "fits": "epilepsy",
    "headache": "headache",
    "migraine": "migraine",
    "vertigo": "vertigo",
    "dizziness": "dizziness",
    "insomnia": "insomnia",
    "sleep disorder": "insomnia",
    "neuralgia": "neuralgia",
    "nerve pain": "neuralgia",
    "sciatica": "sciatica",
    "parkinson disease": "parkinson disease",
    "parkinsonism": "parkinson disease",
    "alzheimer disease": "alzheimer disease",
    "dementia": "dementia",
    "multiple sclerosis": "multiple sclerosis",
    "MS": "multiple sclerosis",
    "meningitis": "meningitis",
    "neuropathy": "neuropathy",
    "peripheral neuropathy": "neuropathy",
    # Hindi terms
    "sir dard": "headache",
    "mirgi": "epilepsy",

    # === Mental Health ===
    "depression": "depression",
    "major depression": "depression",
    "MDD": "depression",
    "anxiety": "anxiety disorder",
    "anxiety disorder": "anxiety disorder",
    "GAD": "anxiety disorder",
    "bipolar disorder": "bipolar disorder",
    "manic depression": "bipolar disorder",
    "schizophrenia": "schizophrenia",
    "panic disorder": "panic disorder",
    "panic attack": "panic disorder",
    "OCD": "obsessive-compulsive disorder",
    "obsessive-compulsive disorder": "obsessive-compulsive disorder",
    "PTSD": "post-traumatic stress disorder",
    "post-traumatic stress disorder": "post-traumatic stress disorder",
    "ADHD": "attention deficit hyperactivity disorder",

    # === Endocrine System ===
    "diabetes": "diabetes",
    "diabetes mellitus": "diabetes",
    "DM": "diabetes",
    "type 2 diabetes": "type 2 diabetes",
    "type 1 diabetes": "type 1 diabetes",
    "hyperthyroidism": "hyperthyroidism",
    "thyrotoxicosis": "hyperthyroidism",
    "hypothyroidism": "hypothyroidism",
    "thyroid disorder": "thyroid disease",
    "obesity": "obesity",
    "overweight": "obesity",
    "gout": "gout",
    "hyperuricemia": "gout",
    "hyperlipidemia": "hyperlipidemia",
    "dyslipidemia": "hyperlipidemia",
    "high cholesterol": "hypercholesterolemia",
    "hypercholesterolemia": "hypercholesterolemia",
    # Hindi terms
    "madhumeh": "diabetes",
    "sugar": "diabetes",
    "motapa": "obesity",

    # === Musculoskeletal System ===
    "arthritis": "arthritis",
    "joint pain": "arthritis",
    "rheumatoid arthritis": "rheumatoid arthritis",
    "RA": "rheumatoid arthritis",
    "osteoarthritis": "osteoarthritis",
    "OA": "osteoarthritis",
    "osteoporosis": "osteoporosis",
    "bone loss": "osteoporosis",
    "fracture": "fracture",
    "bone fracture": "fracture",
    "myalgia": "myalgia",
    "muscle pain": "myalgia",
    "back pain": "back pain",
    "low back pain": "back pain",
    "lumbago": "back pain",
    "neck pain": "neck pain",
    "cervical pain": "neck pain",
    "sprain": "sprain",
    "tendinitis": "tendinitis",
    "fibromyalgia": "fibromyalgia",
    # Hindi terms
    "gathiya": "arthritis",
    "kamar dard": "back pain",

    # === Skin Diseases ===
    "eczema": "eczema",
    "atopic dermatitis": "eczema",
    "urticaria": "urticaria",
    "hives": "urticaria",
    "psoriasis": "psoriasis",
    "dermatitis": "dermatitis",
    "skin rash": "dermatitis",
    "tinea": "tinea",
    "fungal infection": "fungal infection",
    "ringworm": "tinea",
    "onychomycosis": "onychomycosis",
    "nail fungus": "onychomycosis",
    "acne": "acne",
    "pimples": "acne",
    "scabies": "scabies",
    "herpes zoster": "herpes zoster",
    "shingles": "herpes zoster",
    "pruritus": "pruritus",
    "itching": "pruritus",
    "burn": "burn",
    "wound": "wound",
    # Hindi terms
    "khujli": "pruritus",
    "daad": "tinea",

    # === Urinary System ===
    "UTI": "urinary tract infection",
    "urinary tract infection": "urinary tract infection",
    "urethritis": "urethritis",
    "cystitis": "cystitis",
    "bladder infection": "cystitis",
    "nephritis": "nephritis",
    "kidney disease": "kidney disease",
    "CKD": "chronic kidney disease",
    "chronic kidney disease": "chronic kidney disease",
    "kidney stone": "kidney stone",
    "renal calculi": "kidney stone",
    "nephrolithiasis": "kidney stone",
    "BPH": "benign prostatic hyperplasia",
    "benign prostatic hyperplasia": "benign prostatic hyperplasia",
    "prostate enlargement": "benign prostatic hyperplasia",
    "urinary incontinence": "urinary incontinence",
    "erectile dysfunction": "erectile dysfunction",
    "ED": "erectile dysfunction",
    # Hindi terms
    "peshab ki taklif": "urinary tract infection",

    # === Ophthalmology ===
    "conjunctivitis": "conjunctivitis",
    "pink eye": "conjunctivitis",
    "eye infection": "conjunctivitis",
    "glaucoma": "glaucoma",
    "cataract": "cataract",
    "dry eye": "dry eye syndrome",
    "dry eye syndrome": "dry eye syndrome",
    "myopia": "myopia",
    "near-sightedness": "myopia",
    "hyperopia": "hyperopia",
    "macular degeneration": "macular degeneration",
    "AMD": "macular degeneration",
    "diabetic retinopathy": "diabetic retinopathy",

    # === ENT ===
    "otitis media": "otitis media",
    "ear infection": "otitis media",
    "otitis externa": "otitis externa",
    "tinnitus": "tinnitus",
    "ringing in ears": "tinnitus",
    "pharyngitis": "pharyngitis",
    "sore throat": "pharyngitis",
    "tonsillitis": "tonsillitis",
    "laryngitis": "laryngitis",
    "hearing loss": "hearing loss",
    "deafness": "hearing loss",

    # === Infectious Diseases ===
    "bacterial infection": "bacterial infection",
    "viral infection": "viral infection",
    "fungal infection": "fungal infection",
    "parasitic infection": "parasitic infection",
    "sepsis": "sepsis",
    "septicemia": "sepsis",
    "cellulitis": "cellulitis",
    "malaria": "malaria",
    "dengue": "dengue",
    "typhoid": "typhoid fever",
    "typhoid fever": "typhoid fever",
    "cholera": "cholera",
    "HIV": "HIV infection",
    "AIDS": "HIV infection",
    "COVID-19": "COVID-19",
    "coronavirus": "COVID-19",
    # Hindi terms
    "bukhar": "fever",

    # === Allergies ===
    "allergy": "allergy",
    "allergic reaction": "allergic reaction",
    "anaphylaxis": "anaphylaxis",
    "food allergy": "food allergy",
    "drug allergy": "drug allergy",

    # === Gynecology ===
    "menstrual disorder": "menstrual disorder",
    "irregular periods": "menstrual disorder",
    "dysmenorrhea": "dysmenorrhea",
    "menstrual cramps": "dysmenorrhea",
    "menopause": "menopause",
    "menopausal symptoms": "menopause",
    "endometriosis": "endometriosis",
    "vaginitis": "vaginitis",
    "vaginal infection": "vaginitis",
    "uterine fibroid": "uterine fibroid",
    "PCOS": "polycystic ovary syndrome",
    "polycystic ovary syndrome": "polycystic ovary syndrome",
    "infertility": "infertility",

    # === Oncology/Cancer ===
    "cancer": "cancer",
    "carcinoma": "cancer",
    "tumor": "tumor",
    "neoplasm": "tumor",
    "malignancy": "malignant tumor",
    "leukemia": "leukemia",
    "blood cancer": "leukemia",
    "lymphoma": "lymphoma",
    "breast cancer": "breast cancer",
    "lung cancer": "lung cancer",
    "prostate cancer": "prostate cancer",
    "colon cancer": "colorectal cancer",
    "colorectal cancer": "colorectal cancer",

    # === General Symptoms ===
    "fever": "fever",
    "pyrexia": "fever",
    "pain": "pain",
    "inflammation": "inflammation",
    "edema": "edema",
    "swelling": "edema",
    "fatigue": "fatigue",
    "tiredness": "fatigue",
    "anemia": "anemia",
    "anaemia": "anemia",
    "bleeding": "bleeding",
    "hemorrhage": "bleeding",
    "spasm": "spasm",
    "muscle cramp": "cramp",
    "cramp": "cramp",
    "weakness": "weakness",
    "malaise": "malaise",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load TxGNN disease vocabulary"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """Build disease name index (keyword -> (disease_id, disease_name))"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # Full name
        index[name_upper] = (disease_id, disease_name)

        # Extract keywords (split by space and comma)
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """Extract individual indications from indication text

    Uses common English separators
    """
    if not indication_str:
        return []

    # Normalize
    text = indication_str.strip()

    # Split by common separators
    parts = re.split(r"[;.]", text)

    indications = []
    for part in parts:
        # Further split by comma and 'and'
        sub_parts = re.split(r"[,]|\band\b", part)
        for sub in sub_parts:
            sub = sub.strip()
            # Remove common prefixes
            sub = re.sub(r"^(used for|treatment of|indicated for|for the treatment of)", "", sub, flags=re.IGNORECASE)
            sub = re.sub(r"^(management of|relief of|prevention of)", "", sub, flags=re.IGNORECASE)
            sub = sub.strip()
            if sub and len(sub) >= 3:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """Translate indication to standard English keywords"""
    keywords = []
    indication_lower = indication.lower()

    for term, standard in DISEASE_DICT.items():
        if term.lower() in indication_lower:
            keywords.append(standard.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """Map a single indication to TxGNN disease

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # Translate to standard keywords
    keywords = translate_indication(indication)

    for kw in keywords:
        # Exact match
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # Partial match
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # Deduplicate and sort by confidence
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "therapeutic_use",
    license_field: str = "approval_number",
    brand_field: str = "brand_name",
) -> pd.DataFrame:
    """Map India CDSCO drug indications to TxGNN diseases"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str or pd.isna(indication_str):
            continue

        # Extract individual indications
        indications = extract_indications(str(indication_str))

        for ind in indications:
            # Translate and map
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """Calculate indication mapping statistics"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
