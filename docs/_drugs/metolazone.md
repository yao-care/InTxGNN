---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Metolazone"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Metolazone: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: at least 20 listed products"
---

# Metolazone
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

## Metolazone: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Metolazone is a thiazide-like diuretic, originally used to treat hypertension.
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of metolazone as: Thiazide-sensitive sodium-chloride cotransporter inhibitor ([ChEMBL CHEMBL878 (metolazone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL878), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, metolazone is a thiazide-like diuretic, its use in hypertension is established, and mechanistically it may lower blood pressure through sodium and volume reduction.

Malignant renovascular hypertension is a severe form of hypertension. It is driven largely by activation of the renin-angiotensin system due to renal artery stenosis. This makes the link to the original indication only partial. Thiazide-like diuretics can further stimulate renin, which could work against the intended effect in this setting. The high score most likely reflects the model's similarity to the parent hypertension indication rather than a specific mechanistic fit.

Other predictions show the same pattern. Malignant hypertensive renal disease (0.9984) has a plausible link, since metolazone stays effective when kidney function is reduced. However, malignant hypertension usually needs rapid, titratable intravenous agents, and an oral diuretic is not a primary therapy. Pulmonary hypertension (0.9983) has only a symptom-level rationale: relieving fluid congestion and right-heart volume load, not treating the pulmonary vessels. Braddock syndrome (0.9978) has no identifiable mechanistic connection and appears to be a TxGNN model (deep learning) artifact.

## Literature Evidence

For the top prediction, no related literature is currently available.

The only article retrieved across the top five predictions was linked to a lower-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Preclinical | Am J Physiol | In rats, thiazide diuretic receptors (labelled with metolazone) fell by about 90% after acute renal ischemia and recovered afterwards. It does not address pulmonary hypertension. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 64284 | Diurem 2.5mg Tablet | Strip of 10 tablets | Valid |
| 122416 | Lazon 5mg Tablet | Strip of 10 tablets | Valid |
| 122484 | Lazon 2.5mg Tablet | Strip of 10 tablets | Valid |
| 133687 | Metoz 5 Tablet | Strip of 10 tablets | Valid |
| 133748 | Metoz 2.5 Tablet | Strip of 10 tablets | Valid |
| 135905 | Mela 5mg Tablet | Strip of 10 tablets | Valid |
| 136988 | Metozide 5mg Tablet | Strip of 10 tablets | Valid |
| 138153 | Metolaz 5mg Tablet | Strip of 10 tablets | Valid |
| 138457 | Metadure 2.5mg Tablet | Strip of 10 tablets | Valid |
| 138638 | Metolaz 2.5mg Tablet | Strip of 10 tablets | Valid |
| 139662 | Metadure 5mg Tablet | Strip of 10 tablets | Valid |
| 143479 | Metolactone 2.5 mg/50 mg Tablet | Strip of 10 tablets | Valid |
| 143978 | Metoz 1.25mg Tablet | Strip of 10 tablets | Valid |
| 196598 | Rpmel 2.5mg Tablet | Strip of 10 tablets | Valid |
| 246435 | Zytanix 5 Tablet | Strip of 10 tablets | Valid |
| 246439 | Zytanix 2.5 Tablet | Strip of 10 tablets | Valid |
| 246882 | Zytanix 2.5 Tablet | Strip of 15 tablets | Valid |
| 246982 | Zytanix 5 Tablet | Strip of 15 tablets | Valid |
| 247839 | Zalat 5mg Tablet | Strip of 10 tablets | Valid |
| 248353 | Zalat 2.5mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All are oral tablets.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: orthostatic hypotension, multiple system atrophy, postural orthostatic tachycardia syndrome, liver failure, hepatic coma and encephalopathy, pancreatitis, systemic lupus erythematosus (including pediatric), potassium deficiency, diabetes mellitus, diabetic ketoacidosis, anuria, gout, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, and HELLP syndrome.
- **Drug Interactions**: 249 interactions were recorded. Examples at moderate level include acarbose, alogliptin, albiglutide, bupropion, morphine, omeprazole, rabeprazole, cholecalciferol, calcium phosphate, bisacodyl, amphotericin B, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone). Minor examples include doxycycline, atropine, and hyoscyamine.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or relevant literature, and the mechanism may even conflict with the disease biology (renin-driven hypertension). Standard management of malignant hypertension also relies on parenteral agents rather than an oral diuretic.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data for metolazone
- Clinical or mechanistic studies of thiazide-like diuretics in renovascular or malignant hypertension
- Assessment of similarity to the original indication and of route compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL878 (metolazone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL878) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

