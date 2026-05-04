---
layout: default
title: Methocarbamol
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol: From Musculoskeletal Spasm to Cauda Equina Syndrome

## One-Sentence Summary

Methocarbamol is a centrally-acting skeletal muscle relaxant, widely used internationally for musculoskeletal pain and spasm, but currently not marketed in India.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome** with a prediction score of **99.98%**.
However, there are currently **no clinical trials** and **no supporting publications** for this specific indication — the evidence level is L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Skeletal muscle spasm and musculoskeletal pain (international labelling; no India registration data available) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Methocarbamol is a centrally-acting skeletal muscle relaxant that works primarily via CNS depression, reducing nerve impulse transmission to skeletal muscle. It does not act directly on the neuromuscular junction or on smooth muscle.

Cauda equina syndrome is a neurosurgical emergency caused by compression of the cauda equina nerve roots at the lumbar spine, resulting in lower limb weakness, sensory deficits, and loss of bladder/bowel control. The definitive treatment is surgical decompression. While Methocarbamol could theoretically relieve the secondary skeletal muscle spasm that accompanies nerve root irritation, it has no direct effect on the underlying mechanical compression or the neurological damage itself.

The high TxGNN score most likely reflects an indirect connection in the knowledge graph between "spinal/neuromuscular" nodes rather than a true therapeutic mechanistic link. The prediction may be a structural artefact rather than a genuine repurposing signal, and this interpretation is supported by the complete absence of any clinical or preclinical evidence for this combination.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

---

## India Market Information

Methocarbamol has no registered products in India. No authorization records are available.

---

## Safety Considerations

**Drug Interactions** (126 total interactions identified; notable examples listed below):

| Interacting Drug | Severity | Notes |
|-----------------|----------|-------|
| Morphine | **Major** | Enhanced CNS/respiratory depression; combination requires close monitoring |
| Morphine (liposomal) | **Major** | Same risk profile as morphine |
| Dronabinol | Moderate | Additive CNS depression |
| Nabilone | Moderate | Additive CNS depression |
| Opium | Moderate | Additive CNS/respiratory depression |
| Metoclopramide | Moderate | Potential pharmacodynamic interaction |
| Sibutramine | Moderate | CNS-related interaction |

> For full warnings, contraindications, and precautions, please refer to the official prescribing information (package insert). These data were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Methocarbamol carry an L5 evidence rating — meaning there is no clinical trial or published literature support for any of the predicted new uses. Several predicted targets (uveitis, iris disease, panuveitis, conjunctivitis) appear to be knowledge graph clustering artefacts rather than true biological signals. The top prediction (cauda equina syndrome) lacks a plausible direct mechanism, as Methocarbamol cannot address the structural nerve compression that defines this condition. Additionally, Methocarbamol is not currently marketed in India, meaning even its established muscle relaxant indication has no local regulatory foothold.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank API (DG002 — High severity gap) to enable proper mechanistic analysis
- **Safety data**: Download and parse India prescribing information or international SmPC/FDA label to obtain warnings and contraindications (DG001 — Blocking gap; prevents S1 safety evaluation)
- **Broader evidence search**: Expand PubMed and clinical trial searches beyond top-1 indication to check whether any predicted indication has even preclinical support
- **KG artefact review**: Conduct a systematic review of whether the eye-disease cluster (uveitis, panuveitis, iris disease, conjunctivitis) represents a structural knowledge graph bias, and filter accordingly before escalating any indication
- **Regulatory feasibility**: Assess whether Methocarbamol can be registered in India and under what pathway, given zero current market presence

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

