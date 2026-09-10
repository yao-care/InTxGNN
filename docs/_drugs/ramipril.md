---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Ramipril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ramipril: From Unspecified Original Indication to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

> Ramipril is an ACE inhibitor; its original approved indication is not recorded in this evidence pack.
> The TxGNN model's top prediction suggests possible relevance to **Pulmonary Hypertension with Unclear Multifactorial Mechanism**,
> but this direction currently has **0 clinical trials** and **0 supporting publications** — the prediction score is high, but the evidence base is empty.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no `original_indications` data recorded) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.93% (rank 1659) |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for ramipril in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacological class, ramipril is an **ACE inhibitor (ACEI)**. Mechanistically, ACE inhibitors reduce angiotensin II production, which in theory could lower pulmonary vascular resistance and reduce pulmonary vasoconstriction — a plausible, if indirect, biological rationale for a role in pulmonary hypertension.

However, the target indication here is specifically defined as pulmonary hypertension **"with unclear multifactorial mechanism"** — meaning the disease's own pathophysiology is not well characterized. This makes it inherently difficult to construct a strong biological argument connecting ACE inhibition to this particular PH subtype, and no clinical or preclinical evidence currently exists to support the link.

Because `original_indications` is empty in this evidence pack, no direct comparison can be made between ramipril's original approved use and this predicted indication. Resolving this data gap (see Conclusion) is necessary before the mechanistic rationale can be properly evaluated.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## India Market Information

No registration records available — Ramipril currently holds **0 licenses** and is **not marketed** in India per this evidence pack.

## Safety Considerations

**Drug Interactions**: 283 documented interactions are recorded for ramipril in the DDI database. Notable interactions include:

- **Major severity**: Potassium citrate, Potassium bicarbonate — combined use with an ACE inhibitor raises hyperkalemia risk.
- **Moderate severity**: SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), sulfonylureas (chlorpropamide, glimepiride), metformin, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel-prep agents (picosulfuric acid, polyethylene glycol with electrolytes).

Key warnings and contraindications are not available in this evidence pack (flagged as Blocking data gap DG001 — TFDA package insert not yet retrieved).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction carries a high TxGNN score but zero supporting clinical trials or literature (Evidence Level L5), and the target disease's own mechanism is described as "unclear," making biological plausibility hard to establish. Critical drug-level data (original indication, detailed MOA, regulatory warnings/contraindications) are also missing, blocking a full safety assessment (S1).

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: retrieve TFDA/regulatory package insert (warnings & contraindications)
- Resolve High-priority data gap DG002: retrieve detailed MOA via DrugBank API
- Recover original approved indication(s) for ramipril to enable indication-relationship analysis
- Consider re-evaluating lower-ranked but better-evidenced candidates in this same evidence pack — e.g., **rank 10 (cerebral artery occlusion)**, which has Evidence Level L3 with a completed Phase 2 trial (NCT00005928) and 5 supporting mechanistic/clinical studies, may represent a more actionable next step than the current top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

