---
layout: default
title: Rofecoxib
parent: 僅模型預測 (L5)
nav_order: 744
evidence_level: L5
indication_count: 10
---

# Rofecoxib
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

# Rofecoxib: From COX-2-Mediated Analgesia to Heparin Cofactor II Deficiency

## One-Sentence Summary

> Rofecoxib is a selective COX-2 inhibitor historically used for analgesic and anti-inflammatory purposes (marketed as Vioxx until its global withdrawal in 2004 due to cardiovascular thrombotic risk); no original indication data is recorded in the current evidence pack.
> The TxGNN model's top prediction is **Heparin Cofactor II Deficiency**, a rare hereditary thrombophilic disorder,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the underlying evidence pack itself flags it as a likely embedding-space false positive with a mechanistically opposite safety direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap). Based on mechanistic notes within the evidence pack, rofecoxib is described as a selective COX-2 inhibitor for analgesic/anti-inflammatory use; historically marketed as Vioxx, withdrawn worldwide in 2004 for cardiovascular thrombotic risk |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no verified mechanism-of-action record exists in the structured drug fields (`original_moa` = data gap). However, the evidence pack's own repurposing-rationale notes describe rofecoxib as a selective COX-2 inhibitor whose primary pharmacology is suppression of prostaglandin synthesis for analgesic and anti-inflammatory effect.

Heparin cofactor II deficiency is a hereditary defect in a thrombin-inhibiting plasma protein that produces a **thrombophilic (pro-clotting)** phenotype. There is no established pharmacological pathway connecting COX-2/prostaglandin inhibition to coagulation-factor gene regulation, and the evidence pack explicitly notes that this prediction runs in the **opposite safety direction**: rofecoxib is independently associated with an *increased* risk of cardiovascular thrombotic events (myocardial infarction, stroke) — the very reason it was withdrawn from global markets in 2004. Applying it to a population already predisposed to spontaneous thrombosis would be mechanistically incongruent and potentially harmful rather than beneficial.

Notably, this pattern extends across the full top-10 prediction list: 9 of 10 candidates are rare monogenic disorders (coagulation-factor diseases or skeletal/developmental dysplasias) with very high TxGNN scores (>99.6%) but **zero** supporting trials or literature. Only rank 5 (spondyloarthropathy susceptibility) has any literature hit, and that single reference (PMID 17913549) discusses cardiovascular risk *in* spondyloarthropathy patients rather than providing efficacy or safety evidence *for* rofecoxib in that indication. The overall pattern is consistent with a knowledge-graph embedding artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Rofecoxib currently has **no marketing authorizations registered in Taiwan** (market status: 未上市 / Not marketed; total licenses: 0). No product listings are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: DDI database query completed with **246 total interactions** identified (source: DDInter). Representative moderate-severity interactions include: Acetylsalicylic acid, Metformin, Glimepiride, Chlorpropamide, Nateglinide (glycemic/antiplatelet-relevant agents), corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide), Vancomycin, Kanamycin, Levofloxacin, Mesalazine, Balsalazide, Alosetron, Naltrexone, and bowel-prep agents (Polyethylene glycol with electrolytes, Sodium sulfate, Picosulfuric acid).
- **Known Class-Level Risk (from evidence pack rationale, not a formal label warning)**: Rofecoxib was withdrawn from global markets in 2004 due to an established increase in cardiovascular thrombotic events (myocardial infarction, stroke). This is directly relevant context for any repurposing evaluation, particularly given that several top predicted indications are thrombophilic/coagulation disorders where this risk would be especially concerning.

Formal TFDA-equivalent label warnings and contraindications are not yet available (see Data Gap DG001 below); please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (and 9 of the top 10) carry Evidence Level L5 with no clinical trial or literature support, and the leading candidate is mechanistically and safety-wise contradictory to rofecoxib's known prothrombotic cardiovascular risk profile — the same risk that led to its 2004 global withdrawal. The drug is also not currently marketed in Taiwan (0 registrations), and blocking data gaps remain on official label warnings/contraindications and confirmed MOA.

**To proceed, the following is needed:**
- TFDA (or equivalent) official label with warnings, contraindications, and cardiovascular risk labeling (DG001 — Blocking)
- Confirmed mechanism-of-action documentation via DrugBank API (DG002 — High)
- Any real-world or preclinical evidence directly linking COX-2 inhibition to the predicted coagulation/skeletal disorders, if such evidence exists
- A dedicated cardiovascular risk-benefit reassessment before considering any of the top-10 predicted indications for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

