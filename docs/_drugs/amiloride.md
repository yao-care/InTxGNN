---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 5
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Amiloride: predicted new indication malignant hypertensive renal disease (evidence level L5). In India: 4 listed products (4 not discontinued)"
---

# Amiloride
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

## Amiloride: Potassium-sparing diuretic → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Amiloride is an oral potassium-sparing diuretic that is currently marketed in India.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
The prediction is supported by **0 clinical trials** and **0 publications**, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for amiloride: "Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies." ([DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68), label version 2026-11-11; accessed 2026-11-19.) Amiloride belongs to the potassium-sparing diuretic class, which reduces sodium reabsorption in the kidney while retaining potassium.

The link to malignant hypertensive renal disease is plausible only by extension, through amiloride's sodium-handling and blood-pressure-lowering effects. No trial or publication was found that tests amiloride in this kidney condition. The high score therefore reflects a computational prediction, not independent clinical or experimental evidence.

Safety is a particular concern in this setting. Amiloride can cause hyperkalaemia, and the risk rises when kidney function is impaired. Patients with malignant hypertensive renal disease would be expected to have impaired kidney function.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

All recorded licences are valid. The approved indication text is not recorded in the local data.

<!-- review:begin in-lic-20261106-amiloride-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Four valid single-ingredient licences are recorded." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-amiloride-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3897 | Amiur 5mg Tablet | Strip of 10 tablets | Valid |
| 4158 | Amiur H 2.5mg/25mg Tablet | Strip of 10 tablets | Valid |
| 11714 | Amiur H Forte 5mg/50mg Tablet | Strip of 10 tablets | Valid |
| 26232 | Biduret -L Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Hyperkalaemia risk**: Amiloride retains potassium, so there is a safety concern in patients with impaired kidney function.
- **Drug Interactions**: 136 interactions are recorded. Examples at Moderate level include:
  - Corticosteroids: hydrocortisone, betamethasone, budesonide and dexamethasone.
  - Glucose-lowering drugs: metformin, the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin, and exenatide.
  - Laxatives: bisacodyl, castor oil, glycerin, lactitol and lactulose.
  - Others: bupropion and dronabinol.
- Minor-level examples are doxycycline, amoxicillin and cimetidine.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications (Evidence Level L5). Amiloride's hyperkalaemia risk in kidney impairment adds a safety concern for this population.

**To proceed, the following is needed:**
- Studies that directly examine amiloride in malignant hypertensive renal disease, whether preclinical, observational or clinical.
- Detailed mechanism-of-action data.
- Package insert warnings and contraindications from the India licences.
- A potassium and kidney-function monitoring plan, and a review of the interaction burden in this population.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

