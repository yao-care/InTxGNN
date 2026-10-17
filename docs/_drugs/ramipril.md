---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ramipril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertensive disorder / hypertension…"
monitor_inn: "Ramipril"
predicted_indications: ["malignant hypertensive renal disease", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis"]
---

# Ramipril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ramipril: From Hypertension to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Ramipril is an ACE inhibitor originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials and no publications** currently support this specific prediction; it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension, stroke and cerebrovascular disorder (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ramipril is an ACE inhibitor: it lowers angiotensin II, which reduces vasoconstriction and may influence vascular remodeling. Its efficacy in systemic hypertension and cerebrovascular risk reduction is established.

Pulmonary vascular tone and remodeling are also influenced by the renin-angiotensin system, so a mechanistic link is plausible. However, systemic hypertension does not establish efficacy in pulmonary hypertension, and no trial or publication was found for this exact predicted condition. The very high TxGNN score should be read as a network-based signal, not as evidence of efficacy.

A related predicted condition, **pulmonary hypertension owing to lung disease and/or hypoxia** (same score, 99.93%), has some indirect support. A rat study (PMID 9200213) found that ramipril attenuated the effects of chronic hypoxia on pulmonary blood vessels. This is preclinical only, and no human trials were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction. The closest related papers, retrieved for the hypoxia-related pulmonary hypertension prediction, are listed below. Most of the other papers retrieved for that condition were off-topic.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (animal) | Physiological Research | In rats exposed to chronic hypoxia, ramipril lowered baseline pulmonary perfusion pressure and attenuated hypoxic pulmonary vascular changes |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclinical (animal) | Am J Physiol Regul Integr Comp Physiol | Renin-angiotensinogen transgenic rats showed decreased susceptibility of cardiac function to hypoxia-reoxygenation, supporting a role for the renin-angiotensin system in hypoxic injury |

## India Market Information

Ramipril has 20 valid single-ingredient registrations in India (none cancelled). Approved indication text is not available in the licence records. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 179098 | Preventopril 5 Tablet | Strip of 10 tablets | Not specified |
| 186679 | Ramisave 10 Capsule | Strip of 10 capsules | Not specified |
| 44093 | Conram 5mg Tablet | Strip of 10 tablets | Not specified |
| 195861 | Ramey 1.25mg Capsule | Strip of 10 capsules | Not specified |
| 43915 | Cardika 2.5mg Capsule | Strip of 6 capsules | Not specified |

All products are oral tablets or capsules.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, renal artery obstruction, hypotensive disorder, hereditary angioedema, neutropenia and agranulocytosis, systemic lupus erythematosus, scleroderma and systemic sclerosis, connective tissue disease, bone and cartilage disease.
- **Drug Interactions**: 283 interactions were recorded. Major-level interactions include **potassium citrate** and **potassium bicarbonate** (hyperkalaemia risk). Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, glimepiride, chlorpropamide, alogliptin, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin), acetylsalicylic acid, morphine, bupropion, and dronabinol.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or publications for this exact condition. Indirect preclinical evidence exists only for the hypoxia-related form of pulmonary hypertension. No human data support efficacy, and the safety profile in this setting has not been assessed.

**To proceed, the following is needed:**
- Human clinical data (trials or observational studies) for ramipril in pulmonary hypertension, ideally by subtype
- Mechanism of action data and a clearer mechanistic-link analysis
- Package insert warnings and contraindications from the India regulatory source
- Safety assessment for pulmonary hypertension populations, including blood pressure, renal function, and potassium monitoring
- Comparison with established pulmonary hypertension therapies to define any added value

**Other predictions of note (all Hold or Research Question):**
- Most other top predictions are either close to existing indications (malignant renovascular hypertension, malignant hypertensive renal disease, brain stem infarction) or have no supporting data (Braddock syndrome, ABri amyloidosis, Prinzmetal angina).
- Intracerebral hemorrhage (L4) has only preclinical support, and safety in acute hemorrhage would need dedicated assessment.
- Cerebral artery occlusion (L4, "Research Question") is the most developed lead, with one small clinical study of cerebral blood flow (PMID 8797135) plus animal data. The animal data are mixed, and candesartan outperformed ramipril in one study (PMID 18300867).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

