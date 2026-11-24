---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
monitor_inn: "Cyproheptadine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-24
description: "Cyproheptadine: predicted new indication nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Cyproheptadine
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

## Cyproheptadine: H1 antagonist and anticholinergic antihistamine → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Cyproheptadine is an antihistamine with anticholinergic activity, marketed in India as syrups, tablets and drops.
The TxGNN model predicts it may be relevant for **nasal cavity disease**, but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

<!-- review:begin in-lic-20261124c-cyproheptadine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Cyproheptadine is an antihistamine with anticholinergic activity, marketed in India as single-ingredient syrups, tablets and drops." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cyproheptadine-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for cyproheptadine: "Cyproheptadine is a serotonin and histamine antagonist with anticholinergic and sedative effects. Antiserotonin and antihistamine drugs appear to compete with serotonin and histamine, respectively, for receptor sites." ([DailyMed: Cyproheptadine Hydrochloride Solution (cyproheptadine hydrochloride) prescribing information, Method Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1acfd050-6c07-a269-e063-6394a90a77e8), label version 2025-10-21; accessed 2026-11-19.) Based on general pharmacology, cyproheptadine blocks histamine H1 receptors and has anticholinergic effects. Both actions are relevant to nasal symptoms such as congestion, sneezing and watery discharge.

"Nasal cavity disease" is a broad, non-specific category. The high model score most likely reflects the drug's pharmacological relevance to allergic and vasomotor nasal conditions rather than a specific, testable disease. No specific literature or trial evidence exists for a defined nasal cavity condition, so this is a prediction only. A specific disease entity (for example allergic rhinitis, or chronic rhinosinusitis) should be defined before any evaluation.

Similarity to existing uses and route compatibility have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

The drug is marketed in India. The data compiled for this report show 20 valid licences and no cancelled ones; this list may be partial. No approved-indication text is recorded for these licences. Dosage forms include syrup, tablets, drops and oral suspension.

<!-- review:begin in-lic-20261124c-cyproheptadine-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report show 20 valid single-ingredient licences and no cancelled ones;" Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cyproheptadine-2 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3192 | Apicare Syrup | Bottle of 200 ml Syrup | Valid |
| 16814 | Apiked Syrup | Bottle of 200 ml Syrup | Valid |
| 34969 | Colactin Syrup | Bottle of 200 ml Syrup | Valid |
| 41129 | Cymed Syrup | Bottle of 200 ml Syrup | Valid |
| 41285 | Ceron Syrup | Bottle of 200 ml Syrup | Valid |
| 44998 | Cypfed Syrup | Bottle of 200 ml Syrup | Valid |
| 49208 | C-Tiss Syrup | Bottle of 200 ml Syrup | Valid |
| 49294 | Cyptogood Syrup | Bottle of 200 ml Syrup | Valid |
| 50425 | Cypjem Syrup | Bottle of 200 ml Syrup | Valid |
| 57056 | Cyprigen Tablet | Strip of 10 tablets | Valid |
| 57658 | Cypnid 4mg Tablet | Strip of 10 tablets | Valid |
| 105795 | Hysin 1.5 mg/55 mg Drop | Packet of 30 ml Drop | Valid |
| 106367 | Heptazoom T Syrup | Bottle of 200 ml Syrup | Valid |
| 118282 | Kardine Syrup | Bottle of 200 ml Syrup | Valid |
| 164497 | Osoliv Syrup | Bottle of 200 ml Syrup | Valid |
| 167594 | Ocypo T Syrup | Bottle of 200 ml Syrup | Valid |
| 202906 | Siocyp Syrup | Bottle of 200 ml Syrup | Valid |
| 223986 | Tsecyp Syrup | Bottle of 200 ml Syrup | Valid |
| 225110 | Triko Cyp Oral Suspension | Bottle of 200 ml Oral Suspension | Valid |
| 251226 | Zatrotoz Syrup | Bottle of 200 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 308 interactions were identified in total. Major-level interactions include **potassium chloride** and **potassium citrate**. Moderate-level interactions are mainly with other anticholinergic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium) and with central nervous system or gut-motility agents (morphine, opium, loperamide, dronabinol, nabilone, metoclopramide, eluxadoline, fenfluramine).

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9921) but no supporting trials or publications, and the predicted term is too broad to evaluate. The evidence level is L5.

**To proceed, the following is needed:**
- Define a specific nasal cavity disease entity for evaluation
- Mechanism of action data
- Package insert warnings and contraindications from the Indian regulator
- A literature and trial search for the defined condition
- Assessment of route compatibility (for example oral versus nasal use)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyproheptadine Hydrochloride Solution (cyproheptadine hydrochloride) prescribing information, Method Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1acfd050-6c07-a269-e063-6394a90a77e8) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

