---
layout: default
title: Pinaverium
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 1
---

# Pinaverium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Pinaverium: From Irritable Bowel Syndrome to Benign Prostatic Hyperplasia

## One-Sentence Summary

Pinaverium is a gut-selective calcium channel blocker best known for relieving intestinal spasm in irritable bowel syndrome (IBS); formal TFDA-approved indication data is not available since the drug is not currently marketed in Taiwan. The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on knowledge-graph embedding similarity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in TFDA data (drug not marketed in Taiwan); pharmacologically known for IBS-related intestinal spasm |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pinaverium is a musculotropic calcium antagonist that acts selectively on L-type calcium channels in gastrointestinal smooth muscle, reducing intestinal wall tension. This gut-selective mechanism is why it has been used clinically to relieve spasm associated with IBS.

The proposed link to BPH is a cross-organ pharmacological extrapolation: lower urinary tract symptoms (LUTS) in BPH are partly driven by excessive smooth muscle tone in the bladder neck and prostate, and calcium channel blockade could theoretically relax this tissue as well. However, this is not a mechanism the drug was designed or previously documented for — it is inferred purely from structural/functional similarity in the TxGNN knowledge graph.

A key pharmacological concern is that Pinaverium has very low systemic bioavailability, with its therapeutic action concentrated locally in the gut. Whether clinically meaningful drug concentrations could be achieved at the bladder neck or prostate is unconfirmed, and there is currently no direct molecular, preclinical, or clinical evidence supporting this cross-indication extrapolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Pinaverium is not currently marketed in Taiwan (0 licenses on record), so no product registration details are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction is supported only by TxGNN embedding similarity (L5 evidence) with zero clinical trials or literature, and the underlying mechanistic rationale is a cross-organ extrapolation not yet confirmed pharmacologically. Combined with the drug's absence from the Taiwan market, there is insufficient basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank or primary literature (currently a High-severity data gap)
- Preclinical or pharmacokinetic data demonstrating whether Pinaverium reaches effective concentrations in prostate/bladder neck tissue given its low systemic bioavailability
- At minimum, preclinical or early-phase clinical evidence directly linking Pinaverium to LUTS/BPH before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

