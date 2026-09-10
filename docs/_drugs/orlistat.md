---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 616
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a pancreatic/gastric lipase inhibitor whose established use is weight management in obesity, though this evidence pack does not carry TFDA-confirmed indication text (the drug is not currently marketed in Taiwan). The TxGNN model predicts a possible application in **Hypervitaminosis** (excess of fat-soluble vitamins), but this is a **pure model-derived hypothesis** — currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (lipase inhibitor) — not marketed in Taiwan, so no TFDA-approved indication text is on file |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa: [Data Gap]). Based on publicly known pharmacology, Orlistat is a pancreatic and gastric lipase inhibitor that blocks hydrolysis of dietary triglycerides in the gut, reducing fat absorption — the mechanism underlying its established use in weight management.

Because fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat, a well-known clinical consequence of Orlistat therapy is *reduced* absorption of these vitamins — a recognized adverse effect, not a treatment effect. TxGNN's high score for "hypervitaminosis" appears to be a mechanistic extrapolation in the *opposite* direction: reasoning that a drug which lowers fat-soluble vitamin absorption could, in principle, be repurposed to treat states of fat-soluble vitamin *excess*.

This is a logically coherent mechanistic hypothesis, but it inverts a known side effect into a putative indication without any confirmatory human data. No clinical trials, registry trials, or published literature currently exist to support efficacy, dosing, or safety of Orlistat specifically for hypervitaminosis. It should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Orlistat is currently **not marketed in Taiwan** (0 registered licenses on file), so no product registration, dosage form, or approved-indication records are available for this evidence pack.

---

## Safety Considerations

TFDA label warnings and contraindications are not currently available for this drug (data collection pending — see Next Steps).

**Drug Interactions**: 314 total documented interactions on file (DDInter). A sample of Moderate-level interactions includes: Metformin, Acarbose, Alogliptin, Canagliflozin, Albiglutide, Chlorpropamide (antidiabetics — relevant to glycemic monitoring), Amiodarone, Atazanavir, Emtricitabine, Abacavir, Lamivudine (antiretrovirals), and Brentuximab vedotin, Clofarabine, Calaspargase pegol, Asparaginase (Escherichia coli / Erwinia chrysanthemi) (oncology agents). Minor-level interactions include Cholecalciferol, Calcifediol, and Calcitriol — notable given Orlistat's known effect on fat-soluble vitamin absorption, which is directly relevant to the proposed hypervitaminosis indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, S0) with zero supporting clinical trials or literature, and a critical safety data gap (TFDA label/warnings, marked Blocking) prevents even an initial safety screen. There is not yet a basis to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank (DG002, High priority)
- Confirmation of Orlistat's original approved indication(s), since no structured record exists in this pack
- Preclinical or observational evidence connecting Orlistat to fat-soluble vitamin excess/hypervitaminosis specifically (not just the inverse deficiency effect)
- Clarification of clinical rationale — e.g., whether "hypervitaminosis" here refers to a specific fat-soluble vitamin (A, D, E, or K) toxicity, since dosing and risk/benefit would differ substantially by vitamin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

