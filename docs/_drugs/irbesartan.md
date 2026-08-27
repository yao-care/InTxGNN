---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II type 1 receptor (AT1R) blocker globally approved for hypertension and diabetic nephropathy, but not currently registered in India.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** (prediction score 99.31%), yet **no clinical trials** and **no relevant publications** have been identified for this specific indication.
A significant mechanistic safety concern — acute kidney injury risk in bilateral renal artery stenosis — substantially limits the repurposing feasibility, and the overall evidence remains at the lowest tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Diabetic Nephropathy (globally approved; not registered in India) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Irbesartan selectively blocks the angiotensin II type 1 receptor (AT1R), interrupting the downstream effects of the renin-angiotensin-aldosterone system (RAAS): vasoconstriction, sodium retention, and aldosterone secretion are all suppressed. This mechanism is directly relevant to hypertensive pathophysiology at the kidney level, and irbesartan's renoprotective profile has already been established in the landmark IDNT Phase 3 trial for diabetic nephropathy.

Malignant renovascular hypertension arises when renal artery stenosis severely reduces renal perfusion, triggering a massive surge in renin release and sustained AT1R activation. On paper, AT1R blockade could break this pathological feedback loop — which explains why TxGNN assigns a high prediction score. The mechanistic overlap with irbesartan's approved indications is real.

However, a critical clinical safety concern applies specifically to the *malignant* (bilateral) form: when renal artery stenosis affects both kidneys, the AT1R-mediated efferent arteriolar tone is the primary mechanism sustaining glomerular filtration. Blocking AT1R in this context removes that compensatory mechanism and can precipitate acute kidney injury. This is a well-recognised contraindication for ARBs in bilateral RAS and significantly undermines the repurposing case. No clinical trials or publications have been identified to explore whether any patient subgroup might safely benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications (malignant renovascular hypertension, malignant hypertensive renal disease, or pulmonary hypertension subtypes).

---

## Literature Evidence

Currently no relevant literature available for the top predicted indication (malignant renovascular hypertension).

> **Note on rank-4 indication (pulmonary hypertension owing to lung disease/hypoxia):** 20 PubMed records were retrieved, but on review all are general hypoxia biology papers (HIF-1α signalling, altitude physiology, neurodegeneration under hypoxia, etc.) with no content relating to irbesartan or ARB therapy in pulmonary hypertension. These are keyword false positives and are excluded from the evidence table.

---

## Safety Considerations

**Drug Interactions (216 interactions identified):**

Key interactions to monitor when co-prescribing irbesartan:

| Severity | Interacting Drugs (representative examples) |
|----------|---------------------------------------------|
| **Major** | Potassium citrate, Potassium bicarbonate |
| **Moderate** | Hydrocortisone, Betamethasone, Budesonide, Dexamethasone, Triamcinolone (corticosteroids — antagonise antihypertensive effect); Canagliflozin, Dapagliflozin, Empagliflozin (SGLT2 inhibitors — additive hyperkalaemia / hypotension risk); Insulin aspart, Insulin degludec (enhanced hypoglycaemic effect); Acetylsalicylic acid, Morphine, Bupropion, Aprepitant |

The major interactions with potassium-elevating agents (potassium citrate, potassium bicarbonate) are particularly relevant given irbesartan's class-effect risk of hyperkalaemia through RAAS blockade.

> Please refer to the package insert for full warnings and contraindications — those data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications are at evidence level L5 (model prediction only, zero supporting clinical trials or relevant literature), and the top-ranked indication — malignant renovascular hypertension — carries a specific mechanistic contraindication risk (acute kidney injury in bilateral RAS) that has not been addressed in any clinical study. Proceeding to any clinical development stage without resolving this safety signal would be premature.

**To proceed, the following is needed:**

- **Resolve the bilateral RAS safety question**: Clarify whether a subset of malignant renovascular hypertension patients (unilateral stenosis only) could be identified where AT1R blockade is safe. Imaging-based patient selection criteria must be defined before any clinical work.
- **Obtain irbesartan MOA and full contraindication data**: DrugBank API query and CDSCO/EMA package insert review are required to complete the mechanistic and safety analysis.
- **Design indication-specific literature search**: Current PubMed queries returned only false positives for the pulmonary hypertension indications. A targeted search using irbesartan + ARB + specific PH subtypes (WHO Group 3, Group 5) combined with RAAS/AT1R terms is needed.
- **Explore rank-2 indication separately**: Malignant hypertensive renal disease has a stronger mechanistic rationale (renoprotective evidence from IDNT trial is analogous), and was scored "Research Question" rather than "Hold." This is the most actionable candidate if indication-specific clinical data can be generated.
- **India registration pathway**: Irbesartan has zero CDSCO registrations. If a repurposing candidate is identified, a new drug application or regulatory bridging strategy would be required in parallel with clinical development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

