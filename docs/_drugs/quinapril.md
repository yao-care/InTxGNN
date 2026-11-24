---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 716
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Quinapril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Quinapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: 7 listed products (7 not discontinued)"
---

# Quinapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Quinapril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Quinapril is an ACE inhibitor originally used to treat hypertension.
but **no clinical trials and no publications** currently support this specific prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for quinapril: "Quinapril is deesterified to the principal metabolite, quinaprilat, which is an inhibitor of ACE activity in human subjects and animals. ACE is apeptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor, angiotensin II." ([DailyMed: quinapril prescribing information, Proficient Rx LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f33dbbb1-1a4a-42b0-a5c5-3ac905823206), label version 2021-01-01; accessed 2026-11-19.) Based on known information, quinapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension.

Malignant renovascular hypertension is strongly driven by activation of the renin-angiotensin-aldosterone system (RAAS), which is the pathway ACE inhibitors block. This makes the mechanistic rationale plausible.

However, the high TxGNN score most likely reflects similarity to the already-approved hypertension indication rather than a new therapeutic signal. ACE inhibitors are also known to risk acute decline in kidney function in patients with bilateral renal artery stenosis, which is a significant safety concern for this specific condition.

**Other predicted indications (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 0.9986 | L5 | RAAS blockade is relevant to hypertensive kidney damage, but this largely extends the approved use. No studies provided. |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9985 | L5 | Two animal studies from 1996 only. This is the best-supported of the five predictions, though still preclinical. |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 0.9985 | L5 | Only an indirect link through hypoxic pulmonary hypertension work. |

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For the rank 3 prediction (pulmonary hypertension owing to lung disease and/or hypoxia), the following preclinical publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Preclinical (animal) | Circulation | Inhibiting tissue ACE with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodeling. |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Preclinical (animal) | Journal of Cardiovascular Pharmacology | Quinapril preserved left ventricular function and energy metabolism in rats after myocardial infarction. Cardiac model with weak relevance to pulmonary hypertension. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4846 | Artisol 10mg Tablet | Strip of 10 tablets | Valid |
| 183304 | Q Press 10mg Tablet | Strip of 10 tablets | Valid |
| 183338 | Q Press H 20 mg/12.5 mg Tablet | Strip of 10 tablets | Valid |
| 183424 | Q Pril 5mg Tablet | Strip of 10 tablets | Valid |
| 183513 | Q Pril 20mg Tablet | Strip of 10 tablets | Valid |
| 183540 | Q Press 5mg Tablet | Strip of 10 tablets | Valid |
| 183608 | Q Press H 10 mg/12.5 mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are valid, and all are oral tablets.

<!-- review:begin in-lic-20261106-quinapril-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Seven valid single-ingredient registrations are listed in total; all are oral tablets." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-quinapril-1 -->

## Safety Considerations

  - Kidney disease and anuria
  - Liver disease, hepatic coma and hepatic encephalopathy
  - Angioedema, including hereditary, acquired and RAAS-blocker-induced forms
  - Hypotensive disorder
  - Pancreatitis and gallbladder disease
  - Neutropenia and agranulocytosis
  - Systemic lupus erythematosus and connective tissue disease
  - Potassium deficiency, diabetes mellitus and diabetic ketoacidosis
  - Hyperparathyroidism, osteitis fibrosa, bone and cartilage disease
  - Gout and hyperuricemia
  - Neonatal jaundice
- **Drug Interactions:** 246 interactions were identified. The one major interaction listed is **potassium citrate**, because of hyperkalaemia risk. Moderate interactions include metformin, canagliflozin, dapagliflozin, chlorpropamide, acetylsalicylic acid, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone).
- **Specific concern for this indication:** ACE inhibitors may cause acute renal function decline in bilateral renal artery stenosis, which is directly relevant to renovascular hypertension.

Please refer to the package insert for full warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score likely reflects overlap with the approved hypertension indication, and the renal safety risk in renovascular disease is significant.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Clinical studies or systematic literature review of ACE inhibitors in malignant or renovascular hypertension
- A renal safety assessment for patients with renal artery stenosis
- If pursuing pulmonary hypertension instead, human data to follow up the 1996 animal studies, which is currently a research question only

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: quinapril prescribing information, Proficient Rx LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f33dbbb1-1a4a-42b0-a5c5-3ac905823206) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

