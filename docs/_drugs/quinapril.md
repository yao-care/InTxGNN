---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 5
---

# Quinapril
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

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Quinapril is an ACE inhibitor whose established use is treating essential hypertension (and, more broadly, heart failure). TxGNN predicts it may be effective for **Malignant Renovascular Hypertension**, but this specific indication currently has **zero clinical trials** and **zero supporting publications** — the prediction rests entirely on the model's network-similarity score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor class; no detailed indication text available in this evidence pack) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Quinapril is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Quinapril is an ACE inhibitor: it blocks conversion of angiotensin I to angiotensin II, lowering blood pressure — a mechanism directly relevant to any hypertensive disorder, including malignant hypertension.

However, the "renovascular" qualifier matters. Malignant renovascular hypertension typically arises from renal artery stenosis. In that setting, ACE inhibitors dilate the efferent arteriole and can sharply reduce glomerular perfusion pressure in the stenotic kidney — a well-recognized mechanism for precipitating acute kidney injury, particularly with bilateral renal artery stenosis or a solitary functioning kidney. The mechanistic link is therefore double-edged: blood-pressure lowering is favorable, but renal hemodynamics may be harmed, and no clinical evidence in this pack addresses that risk-benefit balance for this specific subgroup.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Quinapril is not currently marketed in India (0 registrations on file), so no product/authorization details are available.

---

## Other Candidates Identified in This Batch

TxGNN also surfaced four additional high-score predictions for Quinapril, all similarly at evidence level L5 with a **Hold** recommendation:

- **Malignant hypertensive renal disease** (score 99.86%) — same ACEI-in-renovascular-disease caveat as above; no trials or literature.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.85%) — 20 PubMed hits retrieved, but all concern general hypoxia biology (neurodegeneration, tumor metabolism, aging) with no mention of Quinapril or RAAS-targeted therapy for this WHO Group 3 condition. This is very likely keyword co-occurrence noise rather than genuine supporting evidence, and current clinical guidance does not favor ACE inhibitors for hypoxia-driven pulmonary hypertension.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.85%) — no trials or literature; disease category (WHO Group 5) has no established RAAS-linked pathophysiology.
- **Braddock syndrome** (score 99.79%) — a rare congenital developmental disorder with no known mechanistic connection to ACE inhibition; almost certainly an embedding-similarity false positive.

None of these candidates should be treated as actionable without independent mechanistic or clinical validation.

---

## Safety Considerations

- **Drug Interactions**: The DDI database lists 246 total documented interactions for Quinapril. Notable examples include:
  - **Major**: Potassium citrate (combined RAAS inhibition and potassium loading — hyperkalemia risk)
  - **Moderate**: Doxycycline, Tetracycline, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Metformin, Canagliflozin, Dapagliflozin, Chlorpropamide, Bupropion, Morphine, Acetylsalicylic acid, Atropine, Bisacodyl, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Pancrelipase

Detailed label-level warnings and contraindications are not available in this evidence pack (flagged as a **Blocking** data gap — this data must be obtained before any formal safety review can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's model score (L5) — there are no clinical trials or literature specific to Quinapril in malignant renovascular hypertension, and the mechanistic rationale carries a plausible harm signal (risk of AKI in renal artery stenosis) that is not offset by any outcome data. A Blocking-severity gap in label warnings/contraindications also prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert warnings and contraindications (Blocking gap, DG001)
- Full mechanism-of-action documentation from DrugBank (High-severity gap, DG002)
- Confirmation of renal artery anatomy (unilateral vs. bilateral stenosis) as an inclusion/exclusion criterion for any future exploratory use
- Dedicated clinical or case-series evidence specific to malignant renovascular hypertension before this indication is reconsidered beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

