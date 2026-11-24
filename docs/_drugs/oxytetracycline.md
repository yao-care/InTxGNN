---
layout: default
title: Oxytetracycline
parent: Model Prediction Only (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Oxytetracycline: predicted new indication Chronic rhinosinusitis (evidence level L5). Approved use: Bacterial infections (e.g., urinary tract infection, bronchitis…"
monitor_inn: "Oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
---

# Oxytetracycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Oxytetracycline: From Bacterial Infections to Chronic Rhinosinusitis
{: .text-alpha }

## One-Sentence Summary

Oxytetracycline is a tetracycline-class antibiotic, originally used for bacterial infections such as urinary tract infection, bronchitis, pneumonia, and conjunctivitis.
The TxGNN model predicts it may be effective for **chronic rhinosinusitis**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g., urinary tract infection, bronchitis, pneumonia, conjunctivitis); the license records compiled do not include indication wording |
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of oxytetracycline as: Bacterial 70S ribosome inhibitor ([ChEMBL CHEMBL1517 (oxytetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1517), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, oxytetracycline belongs to the tetracycline class of broad-spectrum antibiotics. Its efficacy in respiratory, urinary, and eye infections is established, and mechanistically it may be applicable to chronic rhinosinusitis.

Tetracyclines are also known to have anti-inflammatory and matrix metalloproteinase-inhibiting properties. Low-dose doxycycline, a related tetracycline, has been explored in chronic rhinosinusitis with nasal polyps. This offers a plausible bridge between the original infectious indications and the predicted sinus disease.

This link is **hypothetical**. No studies of oxytetracycline itself in chronic rhinosinusitis were found. The high score (0.9961) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a proven therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Oxytetracycline has 20 valid registrations in India and none cancelled. Dosage forms include capsules, tablets, oral solution, syrup, and injectable or infusion products. The license records do not include approved indication text.

<!-- review:begin in-lic-20261124c-oxytetracycline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Oxytetracycline has 20 valid single-ingredient registrations in India and none cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-oxytetracycline-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 15753 | Alpaoxy 50mg Injection | Vial of 30 ml Injection | Valid |
| 78925 | Ecomycin 1gm Injection | Vial of 1 Injection | Valid |
| 161938 | Oxy 500mg Capsule | Strip of 4 capsules | Valid |
| 162862 | Otc Injection | Vial of 30 ml Injection | Valid |
| 163036 | Oxyteracin Injection | Vial of 30 ml Injection | Valid |
| 163153 | Oxytetracycline AF Tablet | Strip of 4 tablets | Valid |
| 163193 | Oxy Dihydrate LA Injection | Vial of 30 ml Injection | Valid |
| 163919 | Oxytetra Injection | Vial of 30 ml Injection | Valid |
| 165916 | Oxytetracin 50mg Infusion | Bottle of 100 ml Infusion | Valid |
| 166510 | Oticycline 250mg Capsule | Strip of 10 capsules | Valid |
| 166778 | Oticycline 500mg Capsule | Strip of 10 capsules | Valid |
| 166988 | Oxy Dihydrate LA Infusion | Bottle of 50 ml Infusion | Valid |
| 167010 | Oxytetracyline Oral Solution | Bottle of 60 ml Oral Solution | Valid |
| 169808 | Oxytetra Wock 50mg Liquid | Bottle of 100 ml Liquid | Valid |
| 216058 | Terramycin MD Injection | Vial of 10 ml Injection | Valid |
| 216151 | Terramycin SF Capsule | Strip of 10 capsules | Valid |
| 219074 | TM 500mg Capsule | Strip of 10 capsules | Valid |
| 220984 | T M SF Capsule | Strip of 10 capsules | Valid |
| 221265 | T M 250mg Capsule | Strip of 4 capsules | Valid |
| 228563 | Tetracon 50mg Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from package insert text): kidney disease, kidney failure, uremia, glomerulonephritis, liver disease, gallbladder disease, *Clostridium difficile* colitis, G6PD deficiency, potassium deficiency, atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome, respiratory failure, perinatal necrotizing enterocolitis, glycogen storage disease, cystinuria, galactosemia, and pyoureter.
- **Drug Interactions**: 144 interactions were recorded. Selected ones:
  - **Major**: Vitamin A.
  - **Moderate**: Amoxicillin, balsalazide, calcium salts (phosphate, acetate), magnesium salts (oxide, sulfate, chloride), zinc salts (sulfate, acetate), potassium citrate, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human).
  - **Minor**: Mannitol.

Please refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The chronic rhinosinusitis prediction is supported only by the model score (L5), with no trials or publications for oxytetracycline in this condition. The mechanistic link, while plausible for the tetracycline class, is unverified for this drug.

**To proceed, the following is needed:**
- A targeted literature search for oxytetracycline, and for tetracyclines more broadly, in chronic rhinosinusitis, to establish whether any direct evidence exists
- Mechanism of action data
- The package insert warnings and contraindications from the Indian regulator, which are needed for safety screening
- Route and formulation compatibility assessment (sinus delivery versus the oral and injectable forms currently registered)
- A comparison against standard chronic rhinosinusitis therapy

**Note on an alternative candidate:** Among the other predictions, **otitis externa** has the most supporting literature. It includes randomized comparisons of topical oxytetracycline, polymyxin B, and hydrocortisone combinations against other treatments (e.g., 1985, 1990, 1993). The studies are mostly old, and several suggest that steroid alone or other antibiotics may perform comparably, so oxytetracycline's own contribution is uncertain. It would be a more tractable research question than chronic rhinosinusitis, but it is not the primary subject of this evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1517 (oxytetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1517) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

