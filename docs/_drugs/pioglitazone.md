---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (TZD)-class PPAR-γ agonist used as an insulin sensitizer in type 2 diabetes mellitus.
The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this direction currently has **0 clinical trials** and **0 supporting publications**, and the model's own mechanistic annotation flags it as lacking pathophysiological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from literature evidence in this pack; no formal MOA/indication record on file — see Data Gap DG002) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally on file for this drug (Data Gap DG002). Based on the literature captured elsewhere in this evidence pack, pioglitazone is consistently identified as a thiazolidinedione (TZD)-class PPAR-γ agonist that improves insulin sensitivity and pancreatic β-cell function in type 2 diabetes mellitus, with additional pleiotropic effects reported in outcome trials.

Opsismodysplasia is a rare autosomal recessive skeletal dysplasia associated with mutations in genes governing skeletal/cartilage development (e.g., INPPL1/SHIP2 and related pathways). There is no established biological pathway linking PPAR-γ agonism or insulin sensitization to the skeletal growth defects underlying this disease.

The evidence pack's own repurposing rationale for this candidate explicitly states that the high TxGNN score (rank 7,354 by raw score, 99.6th percentile) reflects **graph-topological similarity in the knowledge graph rather than a supported mechanistic link**. In other words, this is a pure model-generated hypothesis with no corroborating pharmacological rationale — it should not be interpreted as a validated repurposing signal. Notably, other lower-ranked candidates in this same prediction set (the lipodystrophy spectrum, ranks 5–8) have a more defensible mechanistic story via PPAR-γ's known role in adipocyte differentiation, and may be worth prioritizing over this top-ranked but mechanistically unsupported candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## India Market Information

Pioglitazone has no marketing authorization currently registered in India in this dataset (Market Status: Not marketed; Total Registrations: 0). No product/license records are available to tabulate.

## Safety Considerations

- **Drug Interactions**: A DDI query returned 603 total documented interactions. Representative systemic (non-topical) interactions of Moderate severity include: Abiraterone, Phenylephrine, Acetazolamide, Formoterol, Pseudoephedrine, Epinephrine, Hydrochlorothiazide, Ethanol, Alpelisib, and Salbutamol. Given the large total count, a full interaction check against the patient's concurrent medication list is recommended before any clinical use.

Detailed prescribing warnings and contraindications are not available in this dataset (Data Gap DG001, Blocking) — please refer to the official India-approved package insert once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Opsismodysplasia) has no clinical trial or literature support, and the evidence pack's own mechanistic assessment concludes the TxGNN score reflects knowledge-graph topology rather than a genuine pharmacological link — this does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Formal MOA documentation for pioglitazone (Data Gap DG002)
- India-specific package insert warnings/contraindications (Data Gap DG001, Blocking — required before any S1 safety screening)
- If pursuing repurposing further, re-evaluate against the mechanistically stronger lipodystrophy-spectrum candidates (ranks 5–8) in this same prediction set rather than this top-ranked but unsupported hypothesis
- Disease-specific literature/trial search for Opsismodysplasia if this direction is still to be explored, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

