---
layout: default
title: Imidapril
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 4
monitor_inn: "Imidapril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-28
description: "Imidapril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertension (hypertensive disorder)…"
---

# Imidapril
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

## Imidapril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia
{: .text-alpha }

## One-Sentence Summary

Imidapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but **no clinical trials and no publications** were found in the data compiled for this report, so this remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder), as recorded in the knowledge graph; the licence records contain no indication text |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, imidapril is an ACE inhibitor prodrug that is converted to its active form, imidaprilat. It reduces angiotensin II formation and may lower vascular tone and vascular remodeling. Its target is the angiotensin-converting enzyme (ACE).

Hypertension is a relation recorded in the knowledge graph for this drug. In theory, lowering vascular tone and remodeling could be relevant to pulmonary vascular resistance, which is the basis of the prediction.

This link is weak. ACE inhibitors are not generally used for pulmonary hypertension caused by lung disease or hypoxia, and systemic vasodilators may worsen ventilation-perfusion matching. The prediction rests only on the high model score and is not backed by clinical evidence.

Other predicted indications from the same model, all at evidence level L5 with a Hold recommendation:

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Pulmonary hypertension with unclear multifactorial mechanism | 0.9978 | The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| Malignant hypertensive renal disease | 0.9976 | The most biologically coherent, since the RAAS is central to malignant hypertension and its renal injury; however, it is an acute emergency usually managed with IV agents, and ACE inhibitors carry risks such as acute kidney injury and renal artery stenosis |
| Braddock syndrome | 0.9970 | The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; no clear mechanistic link, needs verification |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 224165 | Tanatril 10mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| Registration No. 220107 | Tanatril 5mg Tablet | Strip of 10 tablets | Not stated in the licence record |

Both are single-ingredient products from Elder Pharmaceuticals Ltd, currently valid, for oral use.

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacological target relationship with angiotensin-converting enzyme (ACE), which is the drug's intended target rather than a drug-drug interaction.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No clinical trials or publications address pulmonary hypertension, and the mechanistic rationale is doubtful in lung-disease or hypoxia-related settings.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the manufacturer, which are currently missing and block safety screening
- Confirmed mechanism of action data from DrugBank
- A literature and trial search specific to ACE inhibitors in pulmonary hypertension
- Preclinical or physiological evidence on the effect on ventilation-perfusion matching and pulmonary vascular resistance
- If any indication is pursued, malignant hypertensive renal disease is the most plausible candidate, but it would require dedicated safety assessment (renal function, renal artery stenosis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

