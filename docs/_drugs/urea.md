---
layout: default
title: Urea
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 0
---

# Urea
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Urea (DB03904): Repurposing Evaluation — Awaiting TxGNN Predictions

## One-Sentence Summary

Urea (DrugBank ID: DB03904) is a small-molecule compound with well-known osmotic and keratolytic properties, though no original registered indications are recorded in this Evidence Pack.
The TxGNN pipeline has **not yet generated any predicted indications** for this candidate, and mechanism of action data is currently unavailable.
This report summarises the available regulatory and safety information to support a future full evaluation once predictions are ready.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication on file |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (prediction pending) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The TxGNN model has not produced any repurposing predictions for Urea (DB03904) in this Evidence Pack run. Without a target disease, a mechanistic rationale cannot be constructed at this stage.

Detailed mechanism of action data is also unavailable (Data Gap DG002). Urea is a naturally occurring small molecule central to the urea cycle. In clinical practice it is best known for osmotic diuretic effects and topical keratolytic activity, but without a formal TxGNN prediction, no target indication can be evaluated here.

This section will be updated once TxGNN predictions are generated and a mechanistic bridge between Urea's pharmacology and the predicted indication can be established.

---

## Safety Considerations

**Drug Interactions** — 54 total interactions identified; top 20 shown below, all rated Moderate severity (Source: DDInter):

| Interacting Drug | Level | Interaction Class |
|-----------------|-------|-------------------|
| Canagliflozin | Moderate | SGLT2 inhibitor — volume depletion risk |
| Dapagliflozin | Moderate | SGLT2 inhibitor — volume depletion risk |
| Empagliflozin | Moderate | SGLT2 inhibitor — volume depletion risk |
| Ertugliflozin | Moderate | SGLT2 inhibitor — volume depletion risk |
| Exenatide | Moderate | GLP-1 agonist — fluid balance interaction |
| Sibutramine | Moderate | Appetite suppressant |
| Bisacodyl | Moderate | Stimulant laxative — electrolyte effect |
| Picosulfuric acid | Moderate | Osmotic laxative — electrolyte effect |
| Polyethylene glycol (3350 with electrolytes) | Moderate | Osmotic laxative |
| Polyethylene glycol (3350) | Moderate | Osmotic laxative |
| Lactulose | Moderate | Osmotic laxative |
| Lactitol | Moderate | Osmotic laxative |
| Sodium sulfate | Moderate | Osmotic laxative |
| Magnesium hydroxide | Moderate | Laxative — electrolyte interaction |
| Magnesium citrate | Moderate | Osmotic laxative |
| Glycerin | Moderate | Osmotic agent |
| Castor oil | Moderate | Laxative |
| Mineral oil | Moderate | Lubricant laxative |
| Phenolphthalein | Moderate | Stimulant laxative |
| Iothalamic acid | Moderate | Contrast agent — renal function consideration |

The interaction profile is dominated by osmotic laxatives/cathartics and SGLT2 inhibitors, consistent with Urea's osmotic mechanism: concurrent use with agents that also alter fluid and electrolyte balance warrants clinical monitoring.

Please refer to the package insert for full key warnings and contraindications, which are not available in this Evidence Pack (Data Gap DG001 — Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions exist for Urea at this time, and two blocking data gaps (MOA and TFDA/CDSCO package insert warnings) prevent completion of even the preliminary safety screen. There is no actionable repurposing candidate to evaluate.

**To proceed, the following is needed:**

- **[Blocking]** Resolve Data Gap DG001: Download TFDA/CDSCO package insert PDF and extract key warnings and contraindications
- **[High]** Resolve Data Gap DG002: Query DrugBank API for Urea's mechanism of action
- Re-run the TxGNN pipeline to generate repurposing predictions for DB03904
- Once a target indication is identified, collect supporting clinical trials and literature evidence
- Reassess Evidence Level and Decision recommendation after gaps are resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

