---
layout: default
title: Lobeglitazone
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 4
---

# Lobeglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lobeglitazone: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Lobeglitazone is a thiazolidinedione (TZD)-class PPAR-γ agonist known for type 2 diabetes management; detailed original-indication and MOA fields are not populated in this evidence pack.
The TxGNN model predicts it may be relevant to **Focal Stiff Limb Syndrome**, but this is a **pure knowledge-graph prediction (L5)** with **zero clinical trials and zero publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (known TZD/PPAR-γ agonist class; not captured in structured Taiwan license data) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Lobeglitazone is part of the thiazolidinedione (TZD) class of PPAR-γ agonists, and its efficacy in type 2 diabetes has been proven; mechanistically it is being proposed as possibly applicable to focal stiff limb syndrome.

Focal stiff limb syndrome is considered a localized variant of stiff person syndrome, an autoimmune neuromuscular disorder. The proposed mechanistic link relies on PPAR-γ activation's known partial anti-inflammatory/immunomodulatory effects, which could theoretically intersect with the autoimmune component of this disease.

However, this connection is explicitly flagged in the source evidence as **indirect and unvalidated** — there is no established evidence that TZD-class drugs affect GABAergic neurotransmission or autoimmune neuromuscular excitability pathways. The high TxGNN score (99.17%) reflects proximity within the knowledge graph rather than a mechanistically or clinically validated relationship, and is unsupported by any clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Lobeglitazone currently has no marketing authorization on file in Taiwan (0 registrations, status: 未上市/Not Marketed). No product, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are currently unavailable/pending TFDA label acquisition — this is flagged as a **Blocking** data gap [DG001] for safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on a knowledge-graph score (L5) with no supporting clinical trials or literature, and the proposed mechanistic link between PPAR-γ agonism and an autoimmune neuromuscular disorder is explicitly characterized as indirect and unvalidated. The drug is also not marketed in Taiwan, and other top-ranked predictions for this molecule (classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia) show the same L5/Hold pattern with equally tenuous mechanistic rationale — suggesting these high scores may largely reflect knowledge-graph co-occurrence rather than genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) to clear the blocking safety data gap (DG001)
- Confirmed mechanism of action (DG001/DG002) to properly evaluate mechanistic plausibility
- Preclinical or case-level evidence linking PPAR-γ agonism to autoimmune/neuromuscular excitability disorders
- Any real-world DDI data, since the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

