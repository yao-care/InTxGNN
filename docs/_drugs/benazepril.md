---
layout: default
title: Benazepril
parent: Moderate Evidence (L3-L4)
nav_order: 95
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Benazepril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, benazepril is an ACE inhibitor, its efficacy in hypertension is established, and mechanistically it may be applicable to renovascular hypertension, which is strongly driven by activation of the renin-angiotensin system (RAS).

However, the predicted indication is closely related to the approved hypertension indication, so it is not a true repurposing opportunity. ACE inhibitors also carry a well-known risk of acute decline in kidney function in bilateral renal artery stenosis or stenosis in a solitary kidney, which is a significant safety concern.

The other predictions are weaker:
- **Malignant hypertensive renal disease** (score 99.65%): RAS blockade reduces intraglomerular pressure and proteinuria, so there is indirect plausibility. This is an acute, severe condition in which ACE inhibitors may cause hypotension or acute kidney injury without careful monitoring.
- **Pulmonary hypertension (hypoxia-related and unclear multifactorial)** (both 99.60%): The link is theoretical. ACE inhibitors have not shown established benefit here. The identical scores suggest a shared graph neighbourhood rather than independent evidence.
- **Braddock syndrome** (99.44%): No clear mechanistic connection can be established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction, currently no related literature is available.

Three publications were retrieved for the pulmonary hypertension (hypoxia) prediction, but none concerns benazepril or pulmonary hypertension. They are preclinical studies of traditional Chinese medicine formulations in renal fibrosis, chronic renal failure and myocardial fibrosis, matched only by the keyword "hypoxia", so they are not counted as supporting evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38803876](https://pubmed.ncbi.nlm.nih.gov/38803876/) | 2024 | Preclinical | Heliyon | Modified Zhenwu Tang slowed chronic renal failure progression via oxidative stress and hypoxic responses (not about benazepril) |
| [31007700](https://pubmed.ncbi.nlm.nih.gov/31007700/) | 2019 | Preclinical | Evid Based Complement Alternat Med | Danggui Shaoyao San reduced renal fibrosis in rats via hypoxia and autophagy regulation (not about benazepril) |
| [31317035](https://pubmed.ncbi.nlm.nih.gov/31317035/) | 2019 | Preclinical | Biomed Res Int | Tongxinluo reduced myocardial fibrosis after myocardial infarction in rats (not about benazepril) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 30004 | Bampril 5 Tablet | Strip of 10 tablets | Not specified |
| 10337 | Apriace 10mg Tablet | Strip of 10 tablets | Not specified |
| 4630 | Apriace 5mg Tablet | Strip of 10 tablets | Not specified |
| 26609 | Benzil 5 Tablet | Strip of 10 tablets | Not specified |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Liver failure, liver disease, hepatic coma/encephalopathy, kidney disease, anuria, angioedema (including hereditary, acquired and RAAS-blocker-induced forms), pancreatitis, gallbladder disease, systemic lupus erythematosus, connective tissue disease, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, neutropenia, agranulocytosis, hypotensive disorder, hyperparathyroidism, bone and cartilage disease, and neonatal jaundice, among others.
- **Drug Interactions**: 169 interactions are recorded. The main ones listed are of moderate severity and include:
  - Glucose-lowering agents: insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), alogliptin, dapagliflozin and exenatide
  - Others: hydrocortisone and glycerin
- **Class-level concern**: Risk of acute renal function decline in bilateral renal artery stenosis or stenosis in a solitary kidney, and of hypotension or acute kidney injury in malignant hypertension with renal involvement.

Please also refer to the package insert for label warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has a plausible RAS-based rationale, but it overlaps with the approved hypertension indication and has no supporting trials or literature. The ACE-inhibitor renal risk in renovascular disease is also a significant safety issue. The high TxGNN score is a model prediction only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian-marketed products (currently a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clinical trial or literature evidence on benazepril or ACE inhibitors in renovascular and malignant hypertension
- A renal safety and monitoring plan for patients with renal artery stenosis
- Clarification of whether the indication is distinct enough from approved hypertension use to count as repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

