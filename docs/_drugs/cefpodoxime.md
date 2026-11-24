---
layout: default
title: Cefpodoxime
parent: Model Prediction Only (L5)
nav_order: 157
evidence_level: L5
indication_count: 2
monitor_inn: "cefpodoxime"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-11-24
description: "Cefpodoxime: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the licence records compiled for this report"
---

# Cefpodoxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Cefpodoxime: From Bacterial Infections to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Cefpodoxime is a third-generation oral cephalosporin antibiotic, marketed in India in tablet and dry syrup forms. The TxGNN model predicts it may be effective for **osteoarthritis** (with rheumatoid arthritis as a second prediction), but **no clinical trials and no publications** were found to support this direction. The prediction is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9925 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of cefpodoxime as: Bacterial penicillin-binding protein inhibitor ([ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacological knowledge, cefpodoxime is a third-generation oral cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. This is an antibacterial action.

No established mechanistic link to osteoarthritis was identified. Cefpodoxime has no known anti-inflammatory, chondroprotective or analgesic activity relevant to this disease. The very high TxGNN score (0.9925) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The second prediction, rheumatoid arthritis (score 0.9924), is similarly unsupported. Its autoimmune, cytokine-driven synovial inflammation is not addressed by the antibacterial mechanism, and no immunomodulatory activity is documented. The near-identical scores for the two diseases suggest a non-specific signal learned by the TxGNN model (deep learning) rather than a disease-specific rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

At least 20 licences are recorded and all are valid. This list may be partial. The licence records contain no approved-indication text.

<!-- review:begin in-lic-20261124c-cefpodoxime-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 single-ingredient licences are recorded and all are valid." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cefpodoxime-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3764 | Astepod 200mg Tablet | Strip of 10 tablets | Valid |
| 17059 | Apodox 100mg Tablet | Strip of 10 tablets | Valid |
| 32315 | Bellocef 200mg Tablet | Strip of 10 tablets | Valid |
| 33885 | Blepod CV 200mg/125mg Tablet | Strip of 6 tablets | Valid |
| 54801 | Ceforit-O Tablet DT | Strip of 10 tablet dt | Valid |
| 57826 | Cefonox 50mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 71471 | Divojet CV 200mg/125mg Tablet | Strip of 6 tablets | Valid |
| 71574 | Docpod 50mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 82716 | Evaxpod CV Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 101712 | Grandcef 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 102069 | Grampod 100mg Tablet | Strip of 10 tablets | Valid |
| 119398 | Kepdox 200mg Tablet | Strip of 10 tablets | Valid |
| 157642 | Novopod 100mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 202512 | Safepodox Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 204015 | Seytri O 200mg Tablet | Strip of 10 tablets | Valid |
| 208343 | Spinxo 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 212104 | Safydox 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 213897 | Serchpod 200 Tablet DT | Strip of 10 tablet dt | Valid |
| 229113 | Topod CV 200mg/125mg Tablet | Strip of 6 tablets | Valid |
| 247914 | Zerapod 50mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 78 interactions were recorded, and the 20 shown in the data compiled for this report are all rated Moderate. Main groups:
  - Acid-reducing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Antacids: aluminium hydroxide, calcium carbonate, magaldrate, and magnesium carbonate, hydroxide and oxide
  - Aminoglycosides: kanamycin and neomycin
  - Balsalazide

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning). There are no clinical trials or publications for osteoarthritis, and no plausible mechanistic link to an antibacterial drug. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for cefpodoxime
- Package insert warnings, contraindications and approved indications from the India licences
- Preclinical or mechanistic evidence for any effect in osteoarthritis (or rheumatoid arthritis)
- A literature and trial search that directly addresses the predicted disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

