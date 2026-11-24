---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 521
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis (also osteoarthritis…"
monitor_inn: "Meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Meloxicam: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID, originally used to treat rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis and spondyloarthropathy.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this prediction. It is a TxGNN model (deep learning) prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (also osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for meloxicam: "Meloxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Zybic™, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec), label version 2026-09-25; accessed 2026-11-19.) Based on known information, meloxicam is an NSAID that inhibits COX-2, and its efficacy in inflammatory joint disease has been established.

The predicted disease is a skeletal dysplasia caused by loss-of-function variants in CDMP1/GDF5. This is a genetic developmental defect, and COX-2 inhibition does not address it. No mechanistic link has been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same pattern appears in the other top-ranked predictions. Several are rare skeletal or developmental syndromes (brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) or unrelated conditions (WHIM syndrome). Meloxicam might offer symptomatic relief of secondary joint pain in some of them, such as pseudoachondroplasia, but it would not modify the disease. The only prediction with any supporting literature is rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (rank 8, evidence level L4). It is largely an extension of an existing indication, not a novel repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only publication in the compiled data relates to the rank 8 prediction (polyarticular JIA):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Safety registry (Phase 4) | Pediatr Rheumatol Online J | Long-term safety and developmental data for celecoxib vs. nonselective NSAIDs in JIA |

## India Market Information

The 20 valid registrations are all products with valid status. The compiled data does not include approved indication text.

<!-- review:begin in-lic-20261124-meloxicam-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The 20 valid registrations are all single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-meloxicam-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4758 | Artaz 15mg Tablet | Strip of 10 tablets | Valid |
| 10347 | Artaz 7.5mg Tablet | Strip of 10 tablets | Valid |
| 78458 | Ecwin 7.5mg Tablet | Strip of 10 tablets | Valid |
| 133640 | Melonex Tablet | Strip of 10 tablets | Valid |
| 135030 | M-Cam 15mg Tablet | Strip of 10 tablets | Valid |
| 135516 | M-Cam 7.5mg Tablet | Strip of 10 tablets | Valid |
| 136556 | Mel OD 15mg Tablet | Strip of 10 tablets | Valid |
| 136620 | Melodol Tablet | Strip of 10 tablets | Valid |
| 138452 | Movac 15mg Tablet | Strip of 10 tablets | Valid |
| 138674 | Melotross 5mg Infusion | Bottle of 100 ml Infusion | Valid |
| 139390 | Melflam 7.5mg Tablet | Strip of 10 tablets | Valid |
| 139415 | Melwin 15mg Tablet | Strip of 10 tablets | Valid |
| 140136 | Muvik 7.5mg Tablet | Strip of 10 tablets | Valid |
| 144942 | Muvik 15mg Tablet | Strip of 10 tablets | Valid |
| 146196 | Movac 7.5mg Tablet | Strip of 10 tablets | Valid |
| 146476 | Melwin 7.5mg Tablet | Strip of 10 tablets | Valid |
| 146643 | Movel 7.5mg Tablet | Strip of 10 tablets | Valid |
| 146996 | Movacam 15mg Tablet | Strip of 10 tablets | Valid |
| 194233 | Rafree 7.5mg Tablet | Strip of 10 tablets | Valid |
| 218620 | Tmel Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms: oral tablets and an intravenous infusion.

## Safety Considerations

- **Contraindications / risk conditions (not label text)**: hypertension, congestive heart failure, heart disease and cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, kidney disease and impaired renal function, active peptic ulcer disease, gastritis, blood coagulation disease, anemia, diabetes mellitus and diabetic ketoacidosis, hyperlipidemia, and substance abuse/dependence.
- **Drug Interactions**: 273 interactions were identified. Those listed are mainly moderate:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Acetylsalicylic acid
  - Antidiabetic agents (metformin, glimepiride, chlorpropamide)
  - Aminosalicylates (mesalazine, balsalazide)
  - Aminoglycosides and vancomycin (kanamycin)
  - Aprepitant
  - Bowel-preparation and potassium products
  - Linaclotide (minor)

Please also refer to the package insert for label warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications, and no plausible mechanistic link between COX-2 inhibition and a GDF5-related genetic skeletal dysplasia. The cardiovascular, renal and gastrointestinal risk profile of meloxicam also offers no advantage for a non-inflammatory genetic condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian-market products
- Detailed mechanism of action data
- Preclinical or mechanistic evidence linking COX-2/prostaglandin signalling to GDF5-related skeletal pathology
- If a practical direction is wanted, evaluate rank 8 (polyarticular JIA) or symptomatic joint-pain use in pseudoachondroplasia instead, as these are better grounded

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

