---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 765
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Silodosin is a selective α1A-adrenergic receptor antagonist clinically used for benign prostatic hyperplasia (BPH) symptom relief.
> The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth syndrome,
> but **no clinical trials and no literature** currently support this direction — the prediction is not corroborated by any external evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — known clinical use, inferred from evidence rationale text; not present in structured regulatory data (`original_indications` is empty) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record (`original_moa: [Data Gap]`). Based on known pharmacology, Silodosin is a highly selective α1A-adrenergic receptor antagonist used clinically to relieve lower urinary tract symptoms associated with BPH by relaxing smooth muscle in the prostate and bladder neck. It has low CNS penetration and no established activity outside the adrenergic signaling pathway.

Ambras syndrome is a rare congenital form of generalized hypertrichosis caused by chromosomal rearrangement near 8q24.3, affecting genes involved in hair follicle developmental patterning. There is no known biological pathway connecting α1A-adrenergic receptor blockade to hair follicle growth regulation, which is driven primarily by androgen and growth-factor signaling.

Despite the very high TxGNN embedding score (99.99%, rank 386 of the full candidate space), the complete absence of supporting clinical trials or literature — combined with the lack of a plausible mechanistic pathway — indicates this prediction most likely reflects knowledge-graph embedding similarity noise rather than a genuine pharmacological signal. This assessment is consistent with the evidence pack's own repurposing rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## India Market Information

Silodosin is not currently registered or marketed in India (`total_licenses: 0`). No product authorization records are available for review.

## Safety Considerations

**Drug Interactions**: 99 total interactions identified. Notable findings include:

| Interacting Drug | Level |
|---|---|
| Clarithromycin | Major |
| Bupropion, Aprepitant, Morphine, Dexamethasone, Canagliflozin, Cimetidine, Dapagliflozin, Dronabinol, Eliglustat, Empagliflozin, Nabilone, Metreleptin, Miconazole, Rolapitant, Clotrimazole, Ertugliflozin, Glycerol phenylbutyrate, Morphine (liposomal), Opium | Moderate |

Key warnings and contraindications are not available in the current data (blocking gap, see below); please refer to the official package insert once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis) has no clinical trial or literature support and no biologically plausible mechanistic link to Silodosin's known pharmacology — the high TxGNN score appears to be an embedding artifact rather than a true signal. Combined with the absence of India market registration and missing core safety data, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolve blocking gap DG001: obtain official label warnings/contraindications (required before any S1 safety screening)
- Resolve high-priority gap DG002: confirm mechanism of action via DrugBank API
- Independently verify whether rank-3 prediction ("malformation syndrome with odontal/periodontal component") reflects a genuine signal or a keyword-matching false positive — the 20 associated publications are generic periodontology literature with no mention of Silodosin or α1-adrenergic antagonism
- If pursuing repurposing further, prioritize re-screening TxGNN output against indications with plausible adrenergic/urological mechanistic overlap rather than the current top-ranked rare genetic syndromes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

