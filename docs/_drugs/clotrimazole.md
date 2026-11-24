---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 205
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: predicted new indication Acne (disease) (evidence level L5). In India: at least 20 listed products"
---

# Clotrimazole
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

## Clotrimazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is a topical and mucosal azole antifungal that is widely marketed in India.
The TxGNN model predicts it may be effective for **acne (disease)**, but only **1 clinical trial** (a suspended study of a three-drug combination) and **no publications** relate to this prediction, so the prediction is not yet supported by direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for clotrimazole: "Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations." ([DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f), label version 2025-03-27; accessed 2026-11-19.) Clotrimazole is generally known as an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), and it has reported antimicrobial and anti-inflammatory activity on skin.

A possible link to acne is through reducing Malassezia or other microbial burden on the skin and through anti-inflammatory effects. However, acne is driven mainly by sebum production, follicular hyperkeratinization, and *Cutibacterium acnes*. The mechanistic fit is therefore indirect.

The very high TxGNN score (0.9986) is a computational prediction. It does not replace clinical evidence, and no cited study directly shows that clotrimazole alone benefits acne.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a fixed combination of beclomethasone, gentamicin and clotrimazole cream in contaminated dermatosis with bilateral symmetrical lesions. No results available. Because of the combination design, any effect cannot be attributed to clotrimazole alone. |

This trial is registered under an acne-related title, but the study text describes contaminated dermatosis, so it does not directly establish clotrimazole's efficacy in acne.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 35702 | Cloral Lozenges Sugar Free | Strip of 10 lozenges | Valid |
| 36686 | Clocip Tablet VT | Packet of 6 tablet vt | Valid |
| 38953 | Comit 20mg/100mg/500mg Tablet VT | Strip of 6 tablet vt | Valid |
| 41401 | Canazole Mouth Wash | Bottle of 15 ml Mouth Wash | Valid |
| 42289 | Clovag 100mg Tablet | Strip of 6 tablets | Valid |
| 42807 | Can V6 Tablet | Strip of 6 tablets | Valid |
| 45658 | Canditas Dusting Powder | Packet of 75 gm Dusting Powder | Valid |
| 47293 | Curitop Dusting Powder | Bottle of 100 gm Dusting Powder | Valid |
| 48125 | Clozol V 100mg Tablet | Strip of 6 tablets | Valid |
| 50197 | Canfem 100mg Tablet VT | Strip of 6 tablet vt | Valid |
| 51194 | Candicul 100mg Tablet VT | Packet of 6 tablet vt | Valid |
| 67900 | Decand V6 100mg Tablet VT | Strip of 6 tablet vt | Valid |
| 87684 | Fungi Drop | Packet of 10 ml Drop | Valid |
| 95666 | Gynotab Tablet VT | Packet of 6 tablet vt | Valid |
| 109411 | Itchnil Cream | Tube of 20 gm Cream | Valid |
| 110404 | Itchgo Cream | Tube of 15 gm Cream | Valid |
| 137563 | Monil V Vaginal Pessary | Packet of 4 pessaries | Valid |
| 145299 | Mycocid Mouth Wash | Bottle of 15 ml Mouth Wash | Valid |
| 162477 | Oraloz 10mg Lozenges | Strip of 10 lozenges | Valid |
| 163340 | Orecure F Ear Drop | Packet of 10 ml Ear Drop | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 licences listed in the local data are valid products. The list may be partial.

<!-- review:begin in-lic-20261124-clotrimazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 licences listed in the local data are valid single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-clotrimazole-1 -->

---

## Safety Considerations

- **Drug Interactions**: 481 interactions were recorded. Major-level interactions in the sample reviewed include fentanyl, alfentanil, amiodarone and hydrocodone. Moderate-level examples include paclitaxel, abemaciclib, acalabrutinib, nifedipine, amlodipine, apixaban, alprazolam, estradiol and levonorgestrel.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only related trial tested a three-drug combination, is suspended and has no results. No publication directly studies clotrimazole in acne, and the mechanistic link is indirect. The evidence level is therefore L5 despite the high model score.

**To proceed, the following is needed:**
- Controlled clinical studies of single-agent clotrimazole in acne
- Detailed mechanism of action data
- Package insert warnings and contraindications for the relevant formulations
- Confirmation that a suitable topical formulation and route fit acne treatment

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

