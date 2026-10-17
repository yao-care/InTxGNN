---
layout: default
title: Treosulfan
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Treosulfan: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not stated in the India license data (the approved indication text is…"
monitor_inn: "Treosulfan"
predicted_indications: ["diabetic cataract", "cortical cataract", "nuclear senile cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "craniostenosis cataract", "mature cataract", "diabetic retinopathy", "senile cataract"]
---

# Treosulfan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Treosulfan: From Hematopoietic Stem Cell Transplant Conditioning to Diabetic Cataract

## One-Sentence Summary

Treosulfan is an alkylating agent marketed in India as an injectable. The TxGNN model predicts it may be effective for **diabetic cataract**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the approved indication text is blank) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Treosulfan is a bifunctional alkylating agent: a prodrug that converts to epoxide intermediates which cross-link DNA. It is generally used in conditioning regimens before hematopoietic stem cell transplantation. This general description comes from background knowledge, not from the data compiled for this report.

A plausible mechanistic link to diabetic cataract cannot be established. Diabetic cataract is driven by polyol pathway activation, glycation and oxidative stress in the lens. DNA alkylation does not address these processes. The high score (0.990) reflects a graph-based signal only. Nine other predictions on the list are also eye conditions (eight cataract types plus diabetic retinopathy), with scores between 0.989 and 0.990. This suggests the signal may come from shared connectivity among cataract terms in the knowledge graph rather than a drug-specific effect.

There is also a safety concern. Cataract is a known risk after conditioning regimens and with related alkylators such as busulfan, so lens toxicity could work against any benefit.

Other top-ranked predictions are:
- Cortical cataract (98.96%)
- Nuclear senile cataract (98.96%)
- Immature cataract (98.95%)
- Diabetes mellitus type 2 associated cataract (98.95%)
- Tetanic cataract (98.95%)
- Craniostenosis cataract (98.95%)
- Mature cataract (98.95%)
- Diabetic retinopathy (98.93%)
- Senile cataract (98.92%)

None has trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 74934 | Emtreo Injection (Emcure Pharmaceuticals Ltd) | Vial of 1 injection | Not stated in the license data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (profound myelosuppression is expected at conditioning doses; please confirm against the package insert) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found. Lens toxicity is a theoretical concern for alkylating agents and should be assessed before any ophthalmic repurposing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature and no supported mechanism. A systemic cytotoxic agent also has an unfavorable benefit-risk balance for cataract and diabetic eye disease, which are managed with surgery, anti-VEGF therapy and laser.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to test any biological link to lens or retinal disease
- Preclinical evidence of benefit, and a review of lens toxicity
- A feasibility assessment of a local ocular route, since only an injectable form is registered in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

