---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 141
evidence_level: L5
indication_count: 3
monitor_inn: "Captopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
last_modified_at: 2026-11-20
description: "Captopril: predicted new indication malignant hypertensive renal disease (evidence level L5). In India: 7 listed products (7 not discontinued)"
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Captopril: ACE inhibitor → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an angiotensin-converting enzyme (ACE) inhibitor sold in India as single-ingredient tablets.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but the data compiled for this report contain **no clinical trials** and only **1 publication**, a diagnostic case report that does not show therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for captopril: "The mechanism of action of captopril tablets have not yet been fully elucidated. Its beneficial effects in hypertension and heart failure appear to result primarily from suppression of the renin-angiotensin-aldosterone system." ([DailyMed: captopril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ccbffd30-4b21-4522-bdb8-abba8d592017), label version 2026-11-11; accessed 2026-11-19.) Captopril belongs to the ACE inhibitor class, which lowers activity of the renin-angiotensin system (RAS) by blocking the conversion of angiotensin I to angiotensin II.

Malignant hypertensive renal disease (malignant nephrosclerosis) involves RAS activation. Blocking this system with an ACE inhibitor therefore offers a plausible mechanistic basis, and captopril is also linked to kidney-protective effects in diabetic nephropathy. This is a theoretical link only.

The one retrieved publication is a case report on captopril renography, a diagnostic test. It describes a renal cell carcinoma that produced a false-positive result, and it does not show that captopril treats this disease. The prediction is therefore essentially model-based.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | Positive captopril renography in a patient with a large chromophobe renal cell carcinoma and intact renal arteries; hypertension resolved after nephrectomy. Diagnostic use only, not therapeutic evidence. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 4601 | Aceten 25mg Tablet | Strip of 10 tablets | Not recorded |
| 5570 | Angiopril 25mg Tablet | Strip of 10 tablets | Not recorded |
| 38749 | Capotril 12.5mg Tablet | Strip of 10 tablets | Not recorded |
| 36749 | Capotril 25mg Tablet | Strip of 10 tablets | Not recorded |
| 10076 | Aceten 12.5mg Tablet | Strip of 10 tablets | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 245 interactions were found in total. The main ones listed are of moderate level, for example with hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide (corticosteroids), metformin, alogliptin, canagliflozin, dapagliflozin and empagliflozin (diabetes drugs), and acetylsalicylic acid, morphine and bupropion. Aluminum hydroxide and calcium carbonate have minor interactions.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9928), but no clinical trial studies this disease and the only publication is a diagnostic case report. Evidence is limited to a model prediction (L5).

**To proceed, the following is needed:**
- Clinical or well-designed preclinical studies of captopril in malignant hypertensive renal disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian regulator
- A review of how captopril compares with standard treatment for severe hypertension with kidney involvement, including safety in patients with kidney disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: captopril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ccbffd30-4b21-4522-bdb8-abba8d592017) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

