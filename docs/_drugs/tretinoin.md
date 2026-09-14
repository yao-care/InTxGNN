---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 853
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Unspecified Original Indication to Rheumatoid Nodulosis

## One-Sentence Summary

> Tretinoin (all-trans retinoic acid, DB00755) is not currently marketed in India, and no original indication data is available in this dataset.
> The TxGNN model predicts it may be effective for **Rheumatoid Nodulosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only prediction with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licenses or original indication data in current dataset |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| India Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tretinoin is not available in this dataset (flagged as a High-severity data gap, DG002). Based on the accompanying repurposing rationale, Tretinoin (ATRA) is known to act as a **retinoic acid receptor (RAR) agonist**. The theoretical link to rheumatoid nodulosis rests on the general premise that RAR agonism can modulate Th17/Treg balance and influence autoimmune inflammation.

This is explicitly described in the evidence pack as an **inferential mechanistic link only** — there is no direct clinical, preclinical, or case-based data connecting Tretinoin to rheumatoid nodulosis specifically. The same caveat applies to the next four ranked predictions (rheumatoid factor-positive polyarticular JIA, juvenile idiopathic arthritis, juvenile chronic polyarthritis, and spondyloarthropathy susceptibility), all of which are L5/S0 with no supporting evidence.

Notably, one lower-ranked prediction in this pack (osteoarthritis, rank 7, L4) does have substantial literature (20 publications), but several of those publications suggest the opposite therapeutic direction — retinoic acid signaling may *promote* cartilage degradation and OA pathogenesis (e.g., PMID 40564983 directly uses ATRA to induce OA in animal models; PMID 37418291 proposes *blocking* retinoic acid metabolism as the therapeutic strategy). This raises a mechanistic red flag rather than reinforcing the repurposing hypothesis, and is a signal that TxGNN score alone should not be relied upon without directionality review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

No registration records are available. Tretinoin is currently listed as **not marketed (未上市)** in this dataset, with 0 total licenses on file.

---

## Safety Considerations

- **Drug Interactions**: 323 documented interactions on file. Notable **Major**-level interactions include Doxycycline, Tetracycline, Minocycline, and Vitamin A (additive retinoid toxicity risk). **Moderate**-level interactions include Aprepitant, Clarithromycin, and Naltrexone. A **Minor** interaction is noted with Levofloxacin. Several additional interactions (e.g., with Metformin, PPIs, corticosteroids) are on file but currently classified as "Unknown" severity and require further review.

Key warnings and contraindications are not yet available in this dataset (flagged as a **Blocking** data gap, DG001 — TFDA-equivalent label warnings/contraindications). This gap must be resolved before any safety assessment (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid nodulosis) has no supporting clinical trials or literature — it is a pure model output at evidence level L5/S0. Combined with a blocking data gap on label warnings/contraindications and the drug's non-marketed status in India, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA-equivalent/Indian regulatory label data (warnings, contraindications) to resolve the blocking data gap (DG001)
- DrugBank-sourced mechanism of action data to properly evaluate mechanistic plausibility (DG002)
- Independent preclinical or case-level evidence specifically linking Tretinoin to rheumatoid nodulosis (or related juvenile arthritis phenotypes) before this candidate can move past S0
- If osteoarthritis is considered as an alternative candidate, a directionality review is required given literature suggesting retinoic acid agonism may worsen rather than improve cartilage degradation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

