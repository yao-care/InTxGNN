---
layout: default
title: Dexibuprofen
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 8
monitor_inn: "Dexibuprofen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome"]
last_modified_at: 2026-11-24
description: "Dexibuprofen: predicted new indication brachydactyly-syndactyly syndrome (evidence level L5). In India: 5 listed products (5 not discontinued)"
---

# Dexibuprofen
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

## Dexibuprofen: NSAID (COX inhibitor) → brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Dexibuprofen is a nonsteroidal anti-inflammatory drug (NSAID), the S-enantiomer of ibuprofen, which inhibits cyclooxygenase (COX). The TxGNN model predicts it may be relevant to **brachydactyly-syndactyly syndrome**, but this is a computational prediction only: **no clinical trials and no publications** were found to support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of dexibuprofen as: Cyclooxygenase inhibitor ([ChEMBL CHEMBL175 (dexibuprofen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL175), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, dexibuprofen is the active S-enantiomer of ibuprofen and works by inhibiting COX enzymes, which reduces prostaglandin-mediated inflammation and pain.

Brachydactyly-syndactyly syndrome is a congenital malformation of the digits. Its cause is developmental and genetic, not inflammatory. There is no recognized mechanism by which COX inhibition would change the course of a congenital skeletal malformation. The high score appears to reflect model-based proximity to musculoskeletal terms rather than a demonstrated biological link. This prediction should be treated as a hypothesis with a weak mechanistic basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 63789 | Debura 300 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 109579 | Ibusoft 400mg Tablet | Strip of 10 tablets | Valid |
| 153180 | Nuprin Plus Tablet | Strip of 10 tablets | Valid |
| 153219 | Nuprin 300mg Tablet | Strip of 10 tablets | Valid |
| 155424 | Nuprin 200 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for this disease, and COX inhibition has no plausible effect on the underlying congenital malformation.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence linking dexibuprofen to this condition
- Detailed mechanism of action data and a plausible biological rationale
- Package insert warnings and contraindications for safety screening

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL175 (dexibuprofen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL175) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

