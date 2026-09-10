---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 770
evidence_level: L5
indication_count: 10
---

# Sodium Acetate
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

# Sodium Acetate: From Electrolyte/pH Buffer to Congenital Prothrombin Deficiency (Unsupported Prediction)

## One-Sentence Summary

> Sodium acetate is an electrolyte and pH-buffering agent; no formal original indication or mechanism of action data is currently on file for this candidate.
> TxGNN's top-ranked prediction is **Congenital Prothrombin Deficiency**, but this candidate carries **no supporting clinical trials or literature**, and the model's own rationale flags it as likely knowledge-graph co-occurrence noise rather than a biologically plausible signal.
> Across all 10 predicted indications, only two (dyspepsia, gastroparesis) reach L4 "mechanistic hypothesis" evidence — none reach a level sufficient for a Go decision.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no `original_indications` recorded) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium acetate (DrugBank DB09395). Based on known pharmacology, sodium acetate functions as an electrolyte source and pH-buffering agent (metabolized to bicarbonate); it has no established role in coagulation factor synthesis.

For the top-ranked prediction, the evidence pack's own mechanistic assessment states directly: *"Sodium acetate is an electrolyte/pH buffer, metabolized to bicarbonate, with no known mechanism affecting prothrombin (Factor II) gene expression or synthesis. The high TxGNN score likely reflects knowledge-graph co-occurrence noise rather than biological plausibility."* This is not a case of a plausible-but-unproven hypothesis — it is a prediction the evidence itself flags as unreliable.

The two indications with any mechanistic grounding — **dyspepsia** and **gastroparesis** — rest on acetate's known identity as a short-chain fatty acid (SCFA). Literature shows SCFAs are actively transported in the duodenum and may modulate gastric emptying via receptors such as GPR43/FFAR2, which is mechanistically relevant to both conditions. However, no clinical trial or publication in the evidence pack tests sodium acetate itself against either indication — all supporting studies involve unrelated compounds (nizatidine, rikkunshi-to, maropitant) or use sodium acetate only as a breath-test reagent, not as a therapeutic intervention.

## Clinical Trial Evidence

*(For top-ranked prediction: Congenital Prothrombin Deficiency)*

Currently no related clinical trials registered.

## Literature Evidence

*(For top-ranked prediction: Congenital Prothrombin Deficiency)*

Currently no related literature available.

> **Note:** Two lower-ranked predictions (dyspepsia, gastroparesis) do have supporting literature (6 and 3 references respectively) and a handful of low-relevance clinical trials (Grade C, unrelated study drugs) — but none test sodium acetate as a therapeutic agent for any indication. See "Why is This Prediction Reasonable?" above for details.

## India Market Information

Sodium acetate holds **no marketing authorizations** in the India registry (`total_licenses: 0`, `market_status: 未上市 / Not Marketed`). No license records are available to summarize.

## Safety Considerations

**Key Warnings / Contraindications:** No data currently available (TFDA label warnings and contraindications are flagged as a **Blocking** data gap — DG001 — preventing initial safety review, S1).

**Drug Interactions:** 30 total interactions identified via DDInter. Representative entries:

| Interacting Drug | Severity |
|---|---|
| Doxycycline | Moderate |
| Tetracycline / Minocycline | Moderate |
| Ephedrine / Pseudoephedrine | Moderate |
| Amphetamine / Dextroamphetamine / Benzphetamine | Moderate |
| Acetylsalicylic acid / Choline salicylate | Moderate |
| Methenamine | Moderate |
| Sulfonylureas (Chlorpropamide, Tolazamide, Glipizide, Glyburide, Acetohexamide, Tolbutamide) | Minor |
| Methotrexate, Memantine | Minor |

Most moderate-severity interactions relate to urinary alkalinization effects (reduced tetracycline/methenamine efficacy; increased renal clearance of salicylates and sympathomimetic amines).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (congenital prothrombin deficiency) is explicitly flagged by the evidence pack's own mechanistic review as likely noise with no biological plausibility, and has zero supporting trials or literature. No indication in the full candidate list exceeds L4 evidence, and the two L4 candidates (dyspepsia, gastroparesis) are still at the "Research Question" stage — mechanistically plausible but never directly tested. Combined with a **Blocking** data gap on TFDA label information and zero India market presence, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/DrugBank-sourced mechanism of action and original indication data (currently absent)
- Package insert warnings and contraindications (Blocking gap, DG001)
- If pursuing dyspepsia/gastroparesis: dedicated preclinical or pilot studies testing sodium acetate (not just SCFAs generally) on gastric emptying outcomes
- Re-evaluation of the congenital prothrombin deficiency signal as a likely false positive before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

