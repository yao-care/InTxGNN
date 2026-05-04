---
layout: default
title: Nefopam
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: From Acute/Chronic Pain to Craniostenosis Cataract

## One-Sentence Summary

Nefopam is a non-opioid central analgesic (benzoxazocine class), clinically established for moderate-to-severe pain management via monoamine reuptake inhibition and NMDA receptor modulation.
The TxGNN model's highest-scoring prediction points to **Craniostenosis Cataract** (score: 99.98%); however, 9 of the top 10 predictions are cataract subtypes with near-identical scores — a pattern strongly consistent with a knowledge graph clustering artifact rather than genuine biological signal.
**No clinical trials or publications** were found to support Nefopam for any of the 10 predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute and chronic pain (non-opioid analgesic) |
| Predicted New Indication | Craniostenosis Cataract (Rank 1) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Nefopam acts primarily through monoamine reuptake inhibition (serotonin, norepinephrine, dopamine) and NMDA receptor modulation, giving it a central analgesic profile without opioid receptor activity. It also exhibits sodium and calcium channel blocking properties at higher concentrations — a breadth of CNS targets that may create indirect connectivity to many disease nodes in the TxGNN knowledge graph.

Craniostenosis cataract is a rare developmental condition in which premature fusion of cranial sutures is associated with lens opacification. There is no established biological pathway linking Nefopam's analgesic mechanisms to lens metabolism or craniosynostosis pathophysiology. The same assessment applies to the eight other cataract subtypes (Ranks 2–9): mature cataract, DM type 2 associated cataract, tetanic cataract, immature cataract, cortical cataract, nuclear senile cataract, senile cataract, and diabetic cataract. All nine share near-identical TxGNN scores (0.9997–0.9998), which is a diagnostic hallmark of **knowledge graph node clustering artifacts** — the model is picking up structural proximity between the Nefopam node and a dense ophthalmic disease cluster in the graph, not a genuine biological relationship.

The sole exception is **Lumbar Spinal Stenosis (Rank 10)**, where Nefopam's analgesic mechanism directly maps to the primary symptom burden of neurogenic claudication and chronic compressive pain. This is the only prediction in this list with conceptual coherence to Nefopam's established clinical role. Even so, no specific clinical trials or literature evidence currently support this application, and the appropriate framing would be **symptom management** (pain relief), not disease modification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## India Market Information

Nefopam is **not currently marketed in India**. No CDSCO-registered licenses were identified.

> **Note:** Nefopam is approved and widely used in several European countries (France, Belgium, UK, South Africa) for acute and postoperative pain. The absence of an India registration means both supply chain and regulatory pathway assessments would be required before any clinical evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information. Full prescribing information (including warnings and contraindications) was not retrievable from the current data inputs — this is classified as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top 9 predictions (all cataract subtypes) share near-identical TxGNN scores across unrelated disease subtypes, are mechanistically unsupported, and carry zero clinical or literature evidence — collectively indicating a knowledge graph clustering artifact that should be excluded from further evaluation. The one mechanistically coherent candidate (lumbar spinal stenosis) is also unsupported by evidence and cannot be assessed safely without resolving the blocking safety data gap.

**To proceed, the following is needed:**

- **Artifact verification (immediate):** Examine TxGNN graph topology to confirm adjacency between the Nefopam node and the cataract disease cluster; if confirmed as artifact, remove these 9 indications from the candidate list
- **MOA data retrieval (DG002 — High priority):** Query DrugBank API for Nefopam's full mechanism of action, targets, and pharmacology profile
- **Safety baseline (DG001 — Blocking):** Retrieve and parse the Nefopam package insert (available from EMA, MHRA, or French ANSM) to extract warnings, contraindications, and key drug interactions; the DDI database path error must also be resolved
- **Lumbar Spinal Stenosis — targeted literature review:** If proceeding beyond artifact cleanup, commission a focused search on Nefopam use in neuropathic and compressive pain conditions (not restricted to LSS) to establish whether a symptom-management claim is supportable
- **India regulatory feasibility:** Assess CDSCO registration pathway and import supply chain before committing research investment, given the drug's complete absence from the India market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

