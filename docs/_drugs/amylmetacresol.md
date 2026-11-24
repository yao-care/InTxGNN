---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Amylmetacresol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data (marketed as throat/cough lozenge…"
monitor_inn: "Amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
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

## Amylmetacresol: From Throat Lozenge Antiseptic to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Amylmetacresol is a local antiseptic used in throat lozenges, marketed in India in several cough and sore-throat lozenge products.
The TxGNN model predicts it may be relevant for **cauda equina syndrome**, but this is a purely computational prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (marketed as throat/cough lozenges) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amylmetacresol is a single-ingredient topical antiseptic used in oropharyngeal lozenges, with minimal systemic exposure expected from lozenge use.

The predicted indication, cauda equina syndrome, is a compressive neurological emergency that requires surgical decompression. There is no plausible pharmacological route from a local throat antiseptic to this condition. The high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions are also unsupported. They include an obsolete neurogenic bladder entry (likely a TxGNN model (deep learning) artifact), irritable bowel syndrome, and several eye conditions (uveitis, panuveitis, iris and ciliary body diseases and neoplasms). None has clinical, literature, or mechanistic backing. The only weak, speculative link is infectious anterior uveitis, based on the drug's in-vitro antibacterial and antiviral activity in the throat. There is no evidence of intraocular penetration or ocular safety.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 37682 | Cof Q Lozenges | Strip of 6 lozenges | Valid |
| 214969 | Tusq-D Cough Lozenges Sugar Free | Strip of 6 lozenges | Valid |
| 214990 | Tusq-D Cough Lozenges Orange | Strip of 6 lozenges | Valid |
| 215973 | Tusq-D Cough Lozenges Honey lemon | Strip of 6 lozenges | Valid |
| 219813 | Tusq-D Lozenges Ginger | Strip of 6 lozenges | Valid |
| 248366 | Zedex Lozenges | Strip of 10 lozenges | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are products with valid status.

<!-- review:begin in-lic-20261106-amylmetacresol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 6 registrations are single-ingredient products with valid status." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-amylmetacresol-1 -->

<!-- review:begin in-lic-20261124b-amylmetacresol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "One further registration (214990, Tusq-D Cough Lozenges Orange) is also valid." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-amylmetacresol-1 -->

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found, and no contraindication edges were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. No clinical trials, publications, or plausible mechanism support using a local throat antiseptic for cauda equina syndrome. The same holds for the other nine predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's product information (currently blocking for safety screening)
- Mechanism of action data for amylmetacresol
- A credible biological rationale linking the drug to the predicted condition, plus evidence that the drug can reach the target tissue (the current lozenge route is local and oropharyngeal)
- Any preclinical or clinical evidence for the predicted indication, or review of whether a different candidate indication is more plausible

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Revised: wording about the earlier partial table and hard-coded counts | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

