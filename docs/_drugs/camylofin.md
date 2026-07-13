---
layout: default
title: Camylofin
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 1
---

# Camylofin
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

# Camylofin: From Antispasmodic to Insomnia

## One-Sentence Summary

Camylofin is an anticholinergic/antispasmodic agent known primarily for peripheral smooth muscle relaxation.
The TxGNN model predicts it may be effective for **Insomnia**,
with a high prediction score of **99.39%**, however **no clinical trials and no published literature** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antispasmodic / smooth muscle relaxation (no formal registration on record) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Camylofin is classified as an anticholinergic and antispasmodic drug, acting primarily by blocking muscarinic receptors in peripheral smooth muscle to reduce spasms. Its established use in gastrointestinal and genitourinary conditions is well within this peripheral mechanism.

The mechanistic link to insomnia is indirect: central M1 muscarinic receptors play a role in regulating sleep architecture, particularly REM sleep suppression. In theory, drugs with anticholinergic properties could influence sleep-wake cycles via central pathways. However, Camylofin's CNS penetration has not been documented in available literature, and its primary pharmacological profile is peripheral rather than central.

The TxGNN high score (0.9939) likely reflects the presence of an "anticholinergic ↔ sleep regulation" indirect edge in the knowledge graph, representing an algorithmic inference rather than direct pharmacological evidence. With the MOA field currently unavailable ([Data Gap]), mechanistic confirmation is not possible at this stage. This prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Camylofin is currently **not marketed in India**. No drug licenses or registrations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.39%), but this is model prediction only (Evidence Level L5) with zero supporting clinical trials or published literature. Critical data on MOA, safety warnings, and contraindications are missing, making it impossible to assess feasibility or risk at this stage.

**To proceed, the following is needed:**

- **MOA clarification**: Query DrugBank API (DB13738) to confirm Camylofin's mechanism of action and CNS penetration profile
- **Safety data**: Retrieve prescribing information / package insert to obtain key warnings and contraindications
- **Literature search expansion**: Broaden PubMed search to include Camylofin + sleep, sedation, or CNS effects (not limited to insomnia)
- **Mechanistic plausibility review**: Assess blood-brain barrier permeability and central M1 receptor binding data before any clinical hypothesis is formed
- **Regulatory pathway check**: Determine whether Camylofin holds any marketing authorization in any jurisdiction (EU, US, Japan) to establish a safety baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

