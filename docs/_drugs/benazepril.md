---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 5
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an angiotensin-converting enzyme (ACE) inhibitor originally used to treat hypertension and chronic kidney disease by blocking the renin-angiotensin system (RAS).
The TxGNN model predicts it may have activity against **Malignant Renovascular Hypertension**, with a prediction score of **99.65%**.
However, **no clinical trials and no targeted publications** currently support this repurposing direction, placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ACE inhibitor class) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Benazepril is a prodrug ACE inhibitor (converted to active benazeprilat) that blocks the conversion of angiotensin I to angiotensin II (Ang II). This reduces systemic vascular resistance, lowers aldosterone secretion, and promotes natriuresis — making it effective in systemic hypertension and renal-protective in chronic kidney disease.

The mechanistic link to malignant renovascular hypertension is biologically plausible but carries significant clinical risk. In renovascular hypertension, the kidneys downstream of a stenotic artery rely heavily on Ang II-mediated efferent arteriolar constriction to maintain glomerular filtration pressure. Blocking ACE in this context can precipitously drop renal perfusion, potentially triggering acute kidney injury — particularly in bilateral renal artery stenosis. The TxGNN model likely detected the shared "hypertension" node in the knowledge graph, but the mechanistic picture is more nuanced than a simple match.

The high TxGNN prediction score (99.65%) reflects a strong computational signal, most likely derived from Benazepril's established antihypertensive activity and its existing connections to renal vascular biology in the knowledge graph. However, this is a case where the model score and the clinical risk are in tension: the same mechanism that makes ACE inhibitors useful for hypertension is precisely the reason they are considered a relative or absolute contraindication in certain forms of renovascular hypertension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benazepril in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available specifically targeting Benazepril in malignant renovascular hypertension.

---

## India Market Information

Benazepril currently has no registered licenses in India. There are no approved products on record.

---

## Safety Considerations

**Drug-Drug Interactions (169 interactions identified):**

The following are notable moderate-level interactions identified from DDInter:

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|-------------------|-------------------|
| Hydrocortisone | Moderate | Corticosteroids may antagonize antihypertensive effect; sodium/water retention risk |
| Insulin human | Moderate | ACE inhibitors may enhance hypoglycaemic effect; monitor blood glucose |
| Insulin glargine | Moderate | Same class risk — enhanced hypoglycaemia with insulin analogues |
| Insulin detemir | Moderate | Enhanced hypoglycaemic risk |
| Insulin aspart | Moderate | Enhanced hypoglycaemic risk |
| Insulin degludec | Moderate | Enhanced hypoglycaemic risk |
| Insulin glulisine | Moderate | Enhanced hypoglycaemic risk |
| Insulin lispro | Moderate | Enhanced hypoglycaemic risk |
| Glimepiride | Moderate | Sulfonylurea + ACE inhibitor: potentiated glucose-lowering effect |
| Glipizide | Moderate | Same risk as glimepiride |
| Glyburide | Moderate | Same risk as glimepiride |
| Alogliptin | Moderate | DPP-4 inhibitor: increased risk of angioedema with concurrent ACE inhibitor use |
| Dapagliflozin | Moderate | SGLT-2 inhibitor: additive blood pressure and renal effects |
| Exenatide | Moderate | GLP-1 agonist: potential pharmacodynamic interaction |
| Acetohexamide | Moderate | First-generation sulfonylurea: enhanced hypoglycaemia risk |
| Chlorpropamide | Moderate | First-generation sulfonylurea: enhanced hypoglycaemia risk |
| Glycerin | Moderate | Osmotic agent: additive renal and blood pressure effects |

> Note: 169 total drug interactions were identified. Listing above represents the most clinically significant categories. For a complete interaction profile, please refer to the full DDInter data and the prescribing information.

> For key warnings and contraindications, please refer to the package insert, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is entirely model-generated (L5 evidence) with no supporting clinical trials or targeted literature. More critically, the predicted indication — malignant renovascular hypertension — carries a well-established mechanistic contraindication risk for ACE inhibitors: Ang II blockade in the setting of renal artery stenosis can precipitate acute renal failure, meaning the drug's known mechanism is a potential hazard rather than a therapeutic advantage for this specific disease subtype.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action from DrugBank (currently marked as Data Gap DG002)
- **Safety label review**: Download and parse the prescribing information to extract key warnings and contraindications (Data Gap DG001 — Blocking severity)
- **Literature search refinement**: Conduct targeted searches combining "benazepril OR ACE inhibitor" with "renovascular hypertension" to assess whether any indirect evidence exists
- **Clinical risk assessment**: Consult a nephrologist or hypertension specialist to formally evaluate whether this indication represents a contraindication rather than a repurposing opportunity
- **Regulatory review**: Assess whether Benazepril is currently contraindicated in bilateral renal artery stenosis per approved labelling in any jurisdiction
- **India registration strategy**: If pursuing this market, a full registration dossier would be required given current zero-licence status in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

