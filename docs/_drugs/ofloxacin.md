---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-24
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). In India: at least 20 listed products"
---

# Ofloxacin
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

## Ofloxacin: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic. The TxGNN model (deep learning) predicts it may be effective for **hyperamylasemia** (score 0.9991); this score may reflect similarities the model learned between related diseases, not biological evidence. **No clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ofloxacin: "Ofloxacin exerts its antibacterial activity by inhibiting DNA gyrase, a bacterial topoisomerase. DNA gyrase is an essential enzyme which controls DNA topology and assists in DNA replication, repair, deactivation, and transcription." ([DailyMed: Ofloxacin Otic (ofloxacin) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=42366170-e536-46a1-9735-d76e5820a9de), label version 2026-10-23; accessed 2026-11-19.) Based on general pharmacology, ofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its antibacterial activity is well established, but it is only recorded as a treatment for infections in the knowledge graph.

Hyperamylasemia is a biochemical finding. Its causes are pancreatic, salivary or renal, and it has no known antibacterial target. No plausible mechanistic link to ofloxacin could be identified. The very high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not supported by any trial or literature, so the prediction should be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indication Worth Noting: Septicemic Plague

Among the other predictions, **septicemic plague** (TxGNN score 0.9979) is the only one with a biologically plausible link. It was assessed at L4, preclinical evidence only. No human trials or registered clinical trials were found.

- In vitro studies show ofloxacin is highly active against *Yersinia pestis* ([8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/), [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/)).
- Mouse and primate models of plague suggest benefit for treatment or prophylaxis ([8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/), [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/), [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/)).
- This is largely class-level fluoroquinolone evidence and is not specific to ofloxacin. Several other retrieved papers concern resistance mechanisms or other organisms.

## India Market Information

At least 20 valid licences are recorded. The list may be partial. No approved-indication text is present in the licence records, so no approved indication can be stated from them. Five representative single-strength ofloxacin products are shown below.

<!-- review:begin in-lic-20261124-ofloxacin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 valid licences are recorded, all classified as single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-ofloxacin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3728 | Aliox 200mg Tablet | Strip of 10 tablets | Valid |
| 70355 | Dflox 100 Tablet | Strip of 10 tablets | Valid |
| 86208 | Flavospas D 200 mg/200 mg Tablet | Strip of 10 tablets | Valid |
| 86858 | Flozoross Tablet | Strip of 10 tablets | Valid |
| 87245 | Fixit OF Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 87739 | Flozox 200mg Tablet | Strip of 10 tablets | Valid |
| 98285 | Geflox 200mg Tablet | Strip of 10 tablets | Valid |
| 102690 | Glofty 100mg Tablet | Strip of 10 tablets | Valid |
| 163774 | Ofka OZ Tablet | Strip of 10 tablets | Valid |
| 164041 | Ole 200mg Tablet | Strip of 10 tablets | Valid |
| 167906 | OPD-OZ 200mg/500mg Tablet | Strip of 10 tablets | Valid |
| 168014 | Ofrut OZ 200mg/500mg Tablet | Strip of 10 tablets | Valid |
| 169715 | Ofo 200mg Tablet | Strip of 10 tablets | Valid |
| 170722 | Oflomus 200mg Tablet | Strip of 10 tablets | Valid |
| 171335 | Oflatoz 50mg Oral Suspension | Bottle of 60 ml Oral Suspension | Valid |
| 171439 | Oflozec OZ Oral Suspension | Bottle of 60 ml Oral Suspension | Valid |
| 172894 | Oflavid-TZ 200mg/600mg Tablet | Strip of 10 tablets | Valid |
| 173567 | Ospol OZ 200mg/500mg Tablet | Strip of 10 tablets | Valid |
| 214574 | Sehflo 200mg Tablet | Strip of 10 tablets | Valid |
| 247177 | ZO 100mg Tablet DT | Strip of 10 tablet dt | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Some other listed product names (for example those with "OZ" or two strengths) suggest possible combination products. These should be verified before using their licences to describe single-ingredient ofloxacin.

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not label text): long QT syndrome, torsades de pointes, liver failure or disease, kidney disease and impaired renal function, epilepsy, myasthenia gravis, peripheral neuropathy, tendinitis, rhabdomyolysis, diabetes and diabetic ketoacidosis, thrombocytopenia, leukopenia, anemia, *Clostridium difficile* colitis, and drug-induced liver injury.
- **Drug interactions**: 383 interactions are recorded. Those rated Major among the first 20 listed are hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion and chlorpropamide. Moderate ones include metformin, pioglitazone, acetylsalicylic acid, famotidine and calcium or potassium salts.
- Fluoroquinolones carry a peripheral neuropathy warning. This is a particular concern for the predicted indication "hematological disease associated with an acquired peripheral neuropathy".

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperamylasemia prediction has a high model score but no trials, no literature and no plausible mechanism, so the evidence level is L5. The only biologically credible lead among the predictions is septicemic plague, which has preclinical support only.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic hypothesis linking ofloxacin to hyperamylasemia
- The package insert warnings and contraindications from the India licence holders
- Any direct clinical or observational study of ofloxacin in the predicted disease
- If plague is pursued instead, a review of guideline-level fluoroquinolone evidence and human data specific to ofloxacin

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ofloxacin Otic (ofloxacin) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=42366170-e536-46a1-9735-d76e5820a9de) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

