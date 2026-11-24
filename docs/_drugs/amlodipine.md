---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 9
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-24
description: "Amlodipine: predicted new indication brain stem infarction (evidence level L5). In India: at least 20 listed products"
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amlodipine: Dihydropyridine calcium channel blocker → brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is a dihydropyridine calcium channel blocker used mainly for blood pressure control.
The TxGNN model predicts it may be effective for **brain stem infarction**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | brain stem infarction |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for amlodipine: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), label version 2026-09-28; accessed 2026-11-19.) Based on known pharmacology, amlodipine is a dihydropyridine calcium channel blocker that relaxes vascular smooth muscle and lowers blood pressure.

Blood pressure control is a cornerstone of preventing stroke, so a link to a brain stem infarction is plausible. However, it is probably a secondary-prevention extension of blood pressure management in cerebrovascular disease rather than a genuinely new mechanism. No trials or publications were found for brain stem infarction itself, so this remains a model-based hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

## Literature Evidence

Currently no related literature available for brain stem infarction.

## India Market Information

The data compiled for this report list 20 valid licences, with no cancelled licences. The list may be partial. No approved indication text is recorded for these licences.

<!-- review:begin in-lic-20261124c-amlodipine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report list 20 valid single-ingredient licences, with no cancelled licences." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-amlodipine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 262 | Amlong 2.5 Tablet | Strip of 15 tablets | Valid |
| 1017 | Amlopin 2.5 Tablet | Strip of 10 tablets | Valid |
| 1242 | Angicam-M Tablet PR | Strip of 15 Tablet pr | Valid |
| 5577 | Amlan 10mg Tablet | Strip of 10 tablets | Valid |
| 9458 | Anol-Ad 50 Tablet | Strip of 10 tablets | Valid |
| 17823 | Amlovib 10mg Tablet | Strip of 10 tablets | Valid |
| 18841 | Amlovate 5mg Tablet | Strip of 10 tablets | Valid |
| 19664 | AMZEL-EL 5MG/2.5MG TABLET | Strip of 15 tablets | Valid |
| 39186 | Caduet 5 mg/10 mg Tablet | Strip of 10 tablets | Valid |
| 65587 | D P Lol 5mg Tablet | Strip of 10 tablets | Valid |
| 73116 | Exforge 10 mg/160 mg Tablet | Strip of 14 tablets | Valid |
| 106919 | Hydipin 5mg Tablet | Strip of 10 tablets | Valid |
| 122755 | Lipril AM Tablet | Strip of 10 tablets | Valid |
| 123743 | Listril AM Tablet | Strip of 10 tablets | Valid |
| 135787 | Metapol AM 5mg/50mg Tablet | Strip of 10 tablets | Valid |
| 144669 | Metomend-AM 50/5 Tablet ER | Strip of 10 tablet er | Valid |
| 193130 | Renace AM 5 mg/50 mg Tablet | Strip of 10 tablets | Valid |
| 212766 | StayHappi Amlodipine+Metoprolol Succinate 5mg/50mg Tablet | Strip of 10 tablets | Valid |
| 234726 | Vintol Plus 5mg/50mg Tablet | Strip of 10 tablets | Valid |
| 235328 | Valzaar SM Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 292 interactions are recorded. Examples at Moderate level include hydrocortisone, aprepitant, acetylsalicylic acid, betamethasone, budesonide, bupropion, clarithromycin, canagliflozin, dapagliflozin and dexamethasone, as well as several calcium salts.

Package insert warnings and contraindications were not available; please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9994), but there are no clinical trials or publications on brain stem infarction, so the evidence is at the model-prediction level (L5). The likely benefit overlaps with existing blood pressure control in cerebrovascular disease.

**To proceed, the following is needed:**
- Studies or trials that directly address brain stem infarction
- Mechanism of action data
- Package insert warnings and contraindications
- Assessment of whether any benefit goes beyond blood pressure lowering

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

