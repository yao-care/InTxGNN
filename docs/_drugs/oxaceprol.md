---
layout: default
title: Oxaceprol
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
---

# Oxaceprol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Oxaceprol: From Undocumented Original Indication to Spondyloarthropathy Susceptibility

## One-Sentence Summary

Oxaceprol's original approved indication and mechanism of action are not documented in the available data (the drug is not currently marketed in India). The TxGNN model's top prediction is **Spondyloarthropathy, susceptibility to**, but this is a genetic susceptibility trait rather than a treatable disease, and there are **zero clinical trials** and **zero publications** supporting any of the model's top 10 predicted indications for this drug.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no approved indication or license on file) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Oxaceprol is not available, and no original approved indication is documented — the drug has zero registered licenses in India. Externally, oxaceprol is known in some markets as a proline derivative used as an anti-inflammatory agent (e.g., for osteoarthritis), but this is not confirmed within the current evidence pack.

Because both the original indication and MOA are undocumented, no mechanistic bridge can be constructed between Oxaceprol and the predicted new indication. More importantly, the top-ranked prediction itself — "spondyloarthropathy, susceptibility to" — describes a genetic susceptibility trait, not a drug-treatable disease state. The model's own rationale for this candidate explicitly flags that the high score likely reflects proximity between gene–disease–drug nodes in the knowledge graph rather than a real pharmacological relationship, and assesses this as a probable graph-based false positive.

This pattern repeats across the full top-10 list: several candidates (brachyolmia-amelogenesis imperfecta syndrome, acromesomelic dysplasia, pseudoachondroplasia) are structural/genetic disorders with no plausible anti-inflammatory mechanism, while the more biologically plausible inflammatory-arthritis candidates (ankylosing spondylitis, juvenile idiopathic arthritis, rheumatoid vasculitis, etc.) have no corroborating trial or literature evidence at all. Given the missing MOA/indication data and the non-actionable nature of the top hit, this prediction should currently be treated as an unverified model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN predictions for Oxaceprol rest solely on model score (Evidence Level L5), with no supporting clinical trials or literature. The top-ranked candidate is a genetic susceptibility trait rather than a treatable indication, and the model's own rationale flags it as a likely knowledge-graph false positive. The drug also lacks basic documentation (original indication, MOA, safety label) needed to build any supporting case.

**To proceed, the following is needed:**
- Original approved indication and mechanism of action (e.g., via DrugBank API or a market where Oxaceprol is licensed)
- Local safety label data — key warnings, contraindications, and a working DDI database (current DDI query failed due to a missing local data file)
- Targeted literature/trial search focused on the more biologically plausible candidates (ankylosing spondylitis, juvenile idiopathic arthritis) rather than the genetic-disorder candidates, which should likely be deprioritized or excluded as non-actionable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

