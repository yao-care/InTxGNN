---
layout: default
title: Racecadotril
parent: 僅模型預測 (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
---

# Racecadotril
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

# Racecadotril: From Acute Diarrhea to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Racecadotril is an enkephalinase (NEP/CD10) inhibitor established as an antidiarrheal agent for acute diarrhea, reducing intestinal hypersecretion without affecting gut motility. The TxGNN model predicts potential efficacy for **Polyclonal Hyperviscosity Syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment flags the link as a likely knowledge-graph topological artifact rather than a substantiated pharmacological relationship.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute diarrhea (antidiarrheal, antisecretory) — inferred from background context in the prediction rationale, not from an India regulatory filing, since the drug is not marketed in India |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 97.72% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Racecadotril is flagged as a data gap (DG002) and could not be independently verified. However, the evidence pack's own prediction rationale identifies Racecadotril as an inhibitor of neutral endopeptidase (NEP/CD10/enkephalinase), an enzyme also expressed on lymphoid and plasma cell lineages and involved in the metabolism of various peptides.

The proposed link to Polyclonal Hyperviscosity Syndrome rests on this shared NEP/CD10 node rather than on any demonstrated pharmacodynamic effect on immunoglobulin production or blood viscosity. The evidence pack explicitly characterizes this as a speculative association: the TxGNN high score likely reflects topological proximity between NEP-related nodes and hematologic disease nodes in the knowledge graph, not a validated mechanistic pathway. No preclinical, clinical, or case-based evidence currently connects enkephalinase inhibition to plasma viscosity or immunoglobulin regulation.

Given this, the mechanistic rationale should be read as a hypothesis-generating signal only, not as pharmacological support strong enough to justify clinical action without further validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Racecadotril currently has no registered products in India (market status: Not marketed, 0 registrations), so no authorization details are available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/India-equivalent label warnings and contraindications are a **Blocking** data gap — DG001 — preventing a formal S1 safety pre-assessment.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5, model prediction only), and the evidence pack's own mechanistic review characterizes the drug-disease link as a likely graph-embedding artifact rather than a plausible pharmacological relationship. Combined with a blocking safety data gap and no India market presence, there is insufficient basis to advance.

**To proceed, the following is needed:**
- TFDA/India label warnings and contraindications (resolves DG001, required before any S1 safety pre-assessment)
- Confirmed mechanism-of-action data from DrugBank or primary literature (resolves DG002)
- Preclinical or mechanistic studies directly testing NEP/CD10 inhibition in the context of immunoglobulin production or plasma viscosity
- Any case reports, observational data, or pharmacovigilance signals linking Racecadotril to hematologic/viscosity-related outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

