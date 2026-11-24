---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 95
evidence_level: L5
indication_count: 4
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Benazepril: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: 4 listed products (4 not discontinued)"
---

# Benazepril
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

## Benazepril: Angiotensin-converting enzyme (ACE) inhibitor → Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Benazepril is an oral ACE inhibitor that blocks the renin-angiotensin system.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
The data compiled for this report contain **0 clinical trials** and **0 publications** on this disease, so the prediction currently rests on the model score and class-level reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for benazepril: "Benazepril and benazeprilat inhibit angiotensin-converting enzyme (ACE) in human subjects and animals. Benazeprilat has much greater ACE inhibitory activity than does benazepril. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e), label version 2025-09-30; accessed 2026-11-19.) Benazepril belongs to the ACE inhibitor class. These drugs block the renin-angiotensin system, which lowers blood pressure and reduces pressure inside the kidney's filtering units (glomeruli), as well as protein loss in the urine. ACE inhibitors have an established kidney-protective role in chronic kidney disease. That gives indirect plausibility for a condition in which severe high blood pressure damages the kidney.

There are important caveats. Malignant hypertension with kidney involvement is an acute, severe condition. In this setting, an ACE inhibitor can cause excessive blood pressure drops or acute kidney injury if it is not carefully monitored. No trials or literature were found for benazepril in this disease. The support is therefore indirect, from the drug class and the model prediction.

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
| 4630 | Apriace 5mg Tablet | Strip of 10 tablets | Valid |
| 10337 | Apriace 10mg Tablet | Strip of 10 tablets | Valid |
| 26609 | Benzil 5 Tablet | Strip of 10 tablets | Valid |
| 30004 | Bampril 5 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

Benazepril is currently marketed in India. All locally recorded licences are valid, and they are single-ingredient oral tablet products. Approved indication text is not recorded in the local data.

---

## Safety Considerations

- **Conditions that call for caution** (from drug-disease relationship data, not label text): liver failure and other liver disease, kidney disease, anuria, angioedema (including hereditary and acquired forms and angioedema induced by renin-angiotensin blockers), pancreatitis, gallbladder disease, systemic lupus erythematosus and other connective tissue disease, diabetes and diabetic ketoacidosis, potassium deficiency, neutropenia and agranulocytosis, low blood pressure, hyperparathyroidism, hepatic encephalopathy, and neonatal jaundice.
- **Drug Interactions**: 169 interactions are recorded. The ones listed here are all rated Moderate.
  - Glucose-lowering agents: insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro), sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), alogliptin, dapagliflozin and exenatide.
  - Other: hydrocortisone and glycerin.

Package insert warnings and contraindications were not available, so please refer to the package insert for the complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or publications directly study benazepril in malignant hypertensive renal disease. The model score of 0.9965 and the class-level kidney-protective effects of ACE inhibitors are not enough to support progression. The acute, severe nature of the condition adds a risk of hypotension and acute kidney injury.

**To proceed, the following is needed:**
- Direct clinical or observational evidence of ACE inhibitor use in malignant hypertensive renal disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India regulator
- A safety and monitoring plan covering blood pressure, kidney function and potassium in this acute setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data for benazepril is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

