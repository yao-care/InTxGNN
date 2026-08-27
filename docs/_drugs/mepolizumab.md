---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mepolizumab: From Severe Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody originally approved for severe eosinophilic asthma and hypereosinophilic syndrome (HES), reducing eosinophil counts by blocking the IL-5 cytokine.
The TxGNN model predicts it may be effective for **Thrombocytopenia Due to Immune Destruction**,
with **0 clinical trials** and **1 publication** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma, hypereosinophilic syndrome (HES) |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Mepolizumab is an anti-IL-5 monoclonal antibody whose efficacy in severe eosinophilic asthma and hypereosinophilic syndrome (HES) has been established. Mechanistically, it may be indirectly relevant to immune-mediated thrombocytopenia through the eosinophil-platelet axis.

The proposed link works as follows: excessive IL-5 signalling drives eosinophil tissue infiltration, causing release of major basic protein (MBP) and eosinophilic cationic protein (ECP). These granule mediators can activate complement and trigger immune-mediated platelet destruction. By suppressing eosinophil counts, Mepolizumab could indirectly relieve HES-associated immune thrombocytopenia. The single available case report documents a patient with steroid-resistant hypereosinophilic immune diathesis who showed simultaneous resolution of a mixed thrombotic microangiopathy following Mepolizumab treatment, providing anecdotal but not controlled support for this hypothesis.

It is important to emphasise that this mechanistic link is **secondary and indirect** — not an independent, direct therapeutic pathway. The prediction likely reflects the biological proximity between eosinophilic disorders and certain platelet destruction syndromes in the knowledge graph, rather than a stand-alone repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | A patient with steroid-resistant hypereosinophilic immune diathesis treated with Mepolizumab showed full resolution of symptoms; concomitant amelioration of mixed thrombotic microangiopathy was observed, suggesting that IL-5-driven eosinophilia may contribute to platelet-related immune injury and that its suppression could have secondary haematological benefit |

---

## India Market Information

Mepolizumab currently has **no registered products in India** (0 authorisations on record). The drug is not marketed locally and would require full regulatory filing before any clinical use.

---

## Additional Predicted Indications (TxGNN Top 5)

For reference, all five top-ranked predictions share a common theme of platelet disorders, suggesting that the model is capturing an eosinophil–platelet biology cluster rather than distinct individual targets.

| Rank | Disease | TxGNN Score | Evidence Level | Mechanistic Confidence | Decision |
|------|---------|------------|---------------|----------------------|---------|
| 1 | Thrombocytopenia due to immune destruction | 99.66% | L4 | Moderate (indirect via HES/MBP pathway) | Hold |
| 2 | Primary release disorder of platelets | 99.61% | L4 | Low (eosinophil–platelet aggregates, basic research only) | Hold |
| 3 | Pseudo-von Willebrand disease | 99.44% | L5 | Very low (GPIbα mutation, no IL-5 connection) | Hold |
| 4 | Autoimmune thrombocytopenic | 99.33% | L5 | Low (Th2/eosinophil involvement possible, not mainstream ITP pathway) | Hold |
| 5 | Glanzmann thrombasthenia | 99.29% | L5 | None (structural GPIIb/IIIa deficiency, unrelated to IL-5) | Hold |

> ⚠️ The clustering of platelet disorders in positions 1–5 is a known knowledge-graph topology effect. High TxGNN scores within a disease cluster do not independently validate each indication; biological plausibility must be assessed individually.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single anecdotal case report with an indirect mechanistic link; no clinical trials exist for this indication, detailed MOA and safety data are unavailable, and Mepolizumab is not currently registered in India.

**To proceed, the following is needed:**

- Obtain the full prescribing information (FDA/EMA label) to fill critical safety gaps: warnings, contraindications, and DDI profile
- Characterise the mechanism of action more precisely — particularly whether eosinophil suppression independently reduces immune platelet destruction versus being a co-phenomenon in HES
- Search for retrospective data or post-hoc analyses in HES cohorts for thrombocytopenia as a secondary endpoint
- Design a pilot prospective study in HES patients with concurrent immune thrombocytopenia before committing to a standalone repurposing programme
- Initiate India regulatory pathway assessment (new drug registration) since the drug has zero local approvals
- Commission a formal systematic review to determine whether the platelet-disorder clustering in TxGNN reflects a true biological signal or a graph topology artefact

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

