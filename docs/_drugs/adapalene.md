---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Adapalene: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
monitor_inn: "Adapalene"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Adapalene: From Acne to Zinc, Elevated Plasma
{: .text-alpha }

## One-Sentence Summary

Adapalene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for adapalene: "Adapalene binds to specific retinoic acid nuclear receptors but does not bind to cytosolic receptor protein. Biochemical and pharmacological profile studies have demonstrated that adapalene is a modulator of cellular differentiation, keratinization, and inflammatory processes." ([DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec), label version 2023-12-27; accessed 2026-11-19.) Based on known information, adapalene is a topical retinoid that acts as a selective retinoic acid receptor (RAR-beta/gamma) agonist. Its efficacy in acne is established, but a mechanistic link to elevated plasma zinc has not been found.

Elevated plasma zinc is a laboratory finding or biochemical state rather than a conventional treatable disease. No known pathway connects retinoid receptor signalling to zinc homeostasis in a way that would lower plasma zinc. Topical adapalene also has low systemic exposure, which makes a systemic effect on plasma zinc even less likely.

The very high TxGNN score (0.9951) is a model output only. It may reflect a TxGNN model (deep learning) artifact, such as general retinoid–zinc associations in skin biology or shared gene-network neighbours. It should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty valid registrations are listed. All are topical gels, and no approved indication text is available in the data compiled for this report.

<!-- review:begin in-lic-20261124c-adapalene-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty valid single-ingredient registrations are listed." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-adapalene-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4386 | Adorg B Gel | Tube of 15 gm Gel | Valid |
| 5953 | Aclene 0.10% Gel | Tube of 15 gm Gel | Valid |
| 9358 | Aditop Gel | Tube of 15 gm Gel | Valid |
| 12911 | Achilles 0.10% Gel | Tube of 15 gm Gel | Valid |
| 13815 | Alin Gel | Tube of 15 gm Gel | Valid |
| 13865 | Acgel Nano Gel | Tube of 15 gm Gel | Valid |
| 14480 | Adene 0.1% Gel | Tube of 15 gm Gel | Valid |
| 17264 | Adhibit Gel | Tube of 15 gm Gel | Valid |
| 21942 | Akend Gel | Tube of 10 gm Gel | Valid |
| 34053 | Cleargel AP Gel | Tube of 15 gm Gel | Valid |
| 34449 | Clindakem A Gel | Tube of 20 gm Gel | Valid |
| 35817 | Clindex Gel | Tube of 10 gm Gel | Valid |
| 40090 | Clinmi Skin A Gel | Tube of 15 gm Gel | Valid |
| 40729 | Capgel Plus Gel | Tube of 15 gm Gel | Valid |
| 61250 | Dee-C Gel | Tube of 15 gm Gel | Valid |
| 74120 | Epiclin-A Gel | Tube of 15 gm Gel | Valid |
| 116972 | Klincin-A Gel | Tube of 15 gm Gel | Valid |
| 140565 | Maviclin-A Gel | Tube of 15 gm Gel | Valid |
| 174496 | Persol Plus Gel | Tube of 15 gm Gel | Valid |
| 217787 | Ticin Plus Gel | Tube of 20 gm Gel | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not taken from label text): photoparoxysmal response, photosensitivity disease, exfoliative dermatitis, and dermatitis.
- **Drug Interactions:** 58 potential interactions were identified, but none has a severity level assigned. Examples include doxycycline, minocycline, tetracycline, metronidazole, prednisone, triamcinolone, budesonide, omeprazole, pantoprazole, ibuprofen, fluconazole, clopidogrel, and bupropion.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). No trials or publications exist, and no plausible mechanism links a topical retinoid to lowering plasma zinc. The target is also a laboratory finding rather than a disease, and topical dosing gives low systemic exposure.

**To proceed, the following is needed:**
- Confirmation that elevated plasma zinc is a clinically meaningful therapeutic target
- Detailed mechanism of action data and any evidence linking retinoid signalling to zinc homeostasis
- Preclinical or exploratory studies showing an effect on plasma zinc
- Package insert warnings and contraindications from the India Pharma source, which are currently missing and block safety screening
- An assessment of route compatibility, since the topical gel formulations may not achieve relevant systemic exposure

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

