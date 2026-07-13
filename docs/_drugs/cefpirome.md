---
layout: default
title: Cefpirome
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Cefpirome
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

以下是根據 Evidence Pack 產生的藥師評估報告：

---

# Cefpirome: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Cefpirome is a fourth-generation cephalosporin antibiotic developed to treat serious bacterial infections caused by both gram-positive and gram-negative organisms, including those resistant to earlier-generation cephalosporins.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (score: 98.31%),
however there are currently **0 clinical trials** and **0 publications** supporting this direction — making this a purely model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fourth-generation cephalosporin antibiotic for serious bacterial infections (no India-registered indication on record) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.31% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological class, Cefpirome is a fourth-generation cephalosporin that exerts its antibacterial effect by binding to penicillin-binding proteins (PBPs) on bacterial cell walls, inhibiting cell wall synthesis. Its fourth-generation classification confers broad-spectrum activity and resistance to many beta-lactamases.

The mechanistic bridge to rheumatoid arthritis is speculative but not entirely without precedent. Some cephalosporins — notably cefoperazone — have demonstrated anti-inflammatory properties in preclinical settings, including inhibition of matrix metalloproteinases (MMPs) such as MMP-1, MMP-3, and MMP-13, which are key enzymes driving joint destruction in RA. TxGNN may be drawing an inference through PBP-adjacent protein nodes that share structural homology with arthritis-related targets in the knowledge graph.

A second proposed pathway involves the gut microbiome: antibiotic exposure alters intestinal microbial composition, and dysbiosis has been increasingly linked to immune dysregulation relevant to RA pathogenesis. However, this connection is indirect, highly context-dependent, and remains entirely speculative for Cefpirome specifically. No published preclinical or clinical data supports Cefpirome as an anti-arthritic agent. The TxGNN signal here most plausibly reflects shared graph neighbourhood rather than a validated pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Cefpirome has no registered drug licenses in India. The drug is not currently marketed and has no approved indications on record with CDSCO.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for Cefpirome sit at Evidence Level L5 — the lowest tier — with zero supporting clinical trials or published literature across any of the predicted diseases. The top prediction (rheumatoid arthritis, 98.31%) appears to reflect indirect knowledge graph pathways rather than a validated pharmacological connection. Crucially, Cefpirome itself has no approved indication or market presence in India, and foundational safety data (package insert warnings, contraindications) is unavailable for review.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve Cefpirome's full mechanism of action from DrugBank API (DB13682) to evaluate whether any known targets overlap with RA or musculoskeletal disease pathways
- **Safety dossier**: Download and parse the originating regulatory package insert (EMA or CDSCO equivalent) to establish key warnings and contraindications before any repurposing evaluation can advance to Stage 1
- **Preclinical evidence search**: Conduct a broader literature search using MeSH terms combining cephalosporins + inflammation + MMP + rheumatoid to determine if any class-level evidence exists that could support a Cefpirome hypothesis
- **KG artifact review**: Evaluate whether the clustering of musculoskeletal predictions (ranks 1–5: RA, osteoarthritis, osteoarthritis susceptibility, gout, pseudoachondroplasia) represents a genuine signal or systematic false positives due to shared ECM/cartilage protein nodes in the TxGNN knowledge graph
- **India market pathway**: If evidence eventually supports advancement, a full CDSCO new drug application pathway would be required given zero existing market presence

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

