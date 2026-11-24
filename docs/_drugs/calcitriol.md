---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 5
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-24
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). In India: at least 19 listed products"
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Calcitriol: active vitamin D hormone → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active form of vitamin D, a hormone that regulates calcium and phosphate balance.
The TxGNN model predicts it may be relevant for **obsolete vitamin D deficiency**, but **no clinical trials and no publications** directly study this disease in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 19) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for calcitriol: "Endogenous synthesis and catabolism of calcitriol, as well as physiological control mechanisms affecting these processes, play a critical role regulating the serum level of calcitriol. Physiological daily production is normally 0.5 to 1.0 mcg and is somewhat higher during periods of increased bone synthesis (eg, growth or pregnancy)." ([DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e), label version 2026-10-15; accessed 2026-11-19.) Calcitriol is the biologically active form of vitamin D (1,25-dihydroxyvitamin D3). It acts on the vitamin D receptor to raise intestinal absorption of calcium and phosphate and to regulate bone mineral metabolism.

Because calcitriol is the active hormone itself, a link to vitamin D deficiency is biologically plausible and likely explains the very high score. However, the disease term is flagged as obsolete, and the prediction largely restates the drug's known physiology rather than offering a novel repurposing signal. In practice, deficiency of the precursor vitamin is usually corrected with native vitamin D, while calcitriol is typically reserved for situations where activation is impaired.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 2394 | Atibon-K27 Softgel Capsule | Strip of 15 soft gelatin capsules | Valid |
| 26559 | Batcium-K2 Capsule | Strip of 10 soft gelatin capsules | Valid |
| 34657 | Cal-Aid Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 35214 | Cal-Aid Soft Gelatin Capsule | Strip of 15 soft gelatin capsules | Valid |
| 36719 | Calcirest Max Tablet | Strip of 10 tablets | Valid |
| 37982 | Calsym-Plus Soft Gel Capsule | Strip of 15 soft gelatin capsules | Valid |
| 38309 | Cecelia Plus Tablet | Strip of 10 tablets | Valid |
| 43426 | Calcijet Injection | Ampoule of 1 ml Injection | Valid |
| 86136 | Fujical-Max Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 95787 | Gemscare Softgel Capsule | Strip of 15 soft gelatin capsules | Valid |
| 122271 | Laretol 1mcg Injection | Ampoule of 1 ml Injection | Valid |
| 126100 | Lifecium Softgel Capsule | Strip of 15 soft gelatin capsules | Valid |
| 134223 | Mancal Forte Softgel Capsule | Strip of 10 soft gelatin capsules | Valid |
| 135921 | Medistrong-K2 Tablet | Strip of 10 tablets | Valid |
| 151400 | Nidcal CL Tablet | Strip of 10 tablets | Valid |
| 188057 | Ritocal CT 0.25mcg Tablet | Strip of 10 tablets | Valid |
| 201065 | Stobo-Cal K27 Softgel Capsule | Strip of 10 soft gelatin capsules | Valid |
| 203281 | Sporecal-Alpha Soft Gelatin Capsule | Strip of 15 soft gelatin capsules | Valid |
| 219110 | Tonecal Softgel Capsule | Strip of 10 soft gelatin capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Calcitriol is marketed in India. The records compiled for this report show no cancelled licences; the list may be partial. The licence records carry no indication text. Available forms:

<!-- review:begin in-lic-20261124c-calcitriol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The records compiled for this report show 20 valid single-ingredient licences and none cancelled;" Revised: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. The product count was also removed: four cholecalciferol (vitamin D3) injections that the data list under calcitriol were excluded from this page; current counts are in the overview table. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-calcitriol-1 -->

| Route | Dosage Forms |
|------|------|
| Oral | Strips of 15 or 10 soft gelatin capsules; strips of 10 tablets |
| Injectable | 1 ml ampoule |

<!-- review:begin in-lic-20261124c-calcitriol-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Injectable / 1 ml ampoule; packet of 6 injections" Revised: the "packet of 6 injections" form came from Calcirol 600000IU Injection (dataset ID 36119), a cholecalciferol (vitamin D3) product that the data list under calcitriol (600000 IU is a vitamin D3 dose; calcitriol is dosed in micrograms). It was excluded from this page; the remaining injectable calcitriol products are 1 ml ampoules. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-calcitriol-2 -->

## Safety Considerations

- **Drug Interactions** (339 interactions recorded; examples):
  - Major: cholecalciferol, calcifediol, burosumab
  - Moderate: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide), enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butalbital, butabarbital), bile-acid binders (cholestyramine, colesevelam, colestipol), aluminium hydroxide, digoxin and digitoxin, topical calcipotriol

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high score but no supporting trials or literature, and the disease term is obsolete. It restates calcitriol's known physiology rather than a new use, so the evidence level is L5.

**To proceed, the following is needed:**
- Clarify which current disease term replaces the obsolete one (e.g., vitamin D deficiency vs. impaired vitamin D activation)
- Studies directly addressing calcitriol in the target condition
- Mechanism-of-action data and package insert warnings and contraindications
- Calcium, phosphate and PTH monitoring plan, given the hypercalcaemia risk and the major interactions with other vitamin D products

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Revised: removed a dosage form from an excluded vitamin D3 product | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

