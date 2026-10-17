---
layout: default
title: Perindopril
parent: Moderate Evidence (L3-L4)
nav_order: 658
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Perindopril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Perindopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials** and only **1 loosely related publication** currently support this direction, so the prediction rests mainly on computational proximity to the approved indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, perindopril is an ACE inhibitor, and its efficacy in hypertension is established. Activation of the renin-angiotensin-aldosterone system (RAAS) is central to malignant hypertension with renal injury, so mechanistically it may be applicable to malignant hypertensive renal disease.

The predicted indication is closely related to the approved one: it is a severe, kidney-damaging form of hypertension. The high TxGNN score most likely reflects this proximity to the hypertension indication rather than independent evidence. The only literature item retrieved concerns a solitary kidney after nephrectomy for renal cancer. It does not address perindopril or malignant hypertensive nephropathy.

Other predictions in the list are weaker:
- **Malignant renovascular hypertension** (score 99.77%, L5): the RAAS rationale is coherent, but ACE inhibitors can cause acute renal function decline in bilateral renal artery stenosis or stenosis of a solitary kidney. No trials or literature are available.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.75%, L4): only indirect rat studies exist (e.g., PMID 10602319 and 11282121). Most other retrieved items are off-topic.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.75%, L5) and **Braddock syndrome** (99.66%, L5): no supporting evidence, and likely graph-based artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Cohort/observational | Urologiia | Functional state of a solitary kidney after nephrectomy for renal cancer. Not about perindopril or malignant hypertensive nephropathy, so it provides only indirect context on renal function loss. |

## India Market Information

The data compiled for this report contain no approved indication text for these licences. A selection of the 20 valid single-ingredient registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34139 | Coversyl 4mg Tablet (Serdia Pharmaceuticals) | Strip of 10 tablets | Not listed |
| 34610 | Coversyl 2mg Tablet (Serdia Pharmaceuticals) | Strip of 10 tablets | Not listed |
| 42129 | Conape 4mg Tablet (Lupin) | Strip of 10 tablets | Not listed |
| 75283 | Eviper 4mg Tablet (Torrent) | Strip of 10 tablets | Not listed |
| 248613 | Zimpril 8mg Tablet (Zim Laboratories) | Strip of 10 tablets | Not listed |

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text):** kidney disease, liver disease, gallbladder disease, angioedema (including acquired, hereditary, and RAAS-blocker-induced forms), neutropenia, agranulocytosis, hypotensive disorder, connective tissue disease, bone disease, cartilage disease, pyoureter, and renal artery obstruction.
- **Drug Interactions:** 213 interactions were identified. Major-level examples are **potassium citrate** and **potassium bicarbonate** (hyperkalaemia risk). Moderate-level examples include metformin, alogliptin, dapagliflozin, empagliflozin, canagliflozin, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, and bupropion.
- **Relevance to the predicted indications:** renal artery obstruction and kidney disease appear among the associated contraindications. This is a significant concern for renal and renovascular hypertension indications. A retrieved case report also documents life-threatening ACE-inhibitor angioedema (PMID 37678466).

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and close to the approved hypertension indication, but there are no clinical trials and no directly relevant literature. The high TxGNN score probably reflects graph proximity rather than independent evidence. Renal-related safety concerns also need clarification.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, which is a blocking gap for safety screening
- Detailed mechanism of action data (e.g., from DrugBank)
- Targeted literature and trial searches specific to perindopril in malignant hypertension with renal involvement
- A renal safety assessment, especially for renal artery stenosis and solitary kidney
- Approved indication text for the Indian licences, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

