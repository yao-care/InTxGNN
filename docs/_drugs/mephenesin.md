---
layout: default
title: Mephenesin
parent: Model Prediction Only (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mephenesin: predicted new indication Metastatic melanoma (evidence level L5). Approved use: Not stated in the India license records"
monitor_inn: "Mephenesin"
predicted_indications: ["metastatic melanoma", "non-cutaneous melanoma", "epithelioid cell melanoma", "choroideremia", "immature cataract", "tetanic cataract", "craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "eyelid melanoma"]
---

# Mephenesin
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

# Mephenesin: From Muscle Spasm (Topical Use) to Metastatic Melanoma

## One-Sentence Summary

Mephenesin is a centrally acting muscle relaxant (a propanediol derivative), marketed in India only as topical gels.
The TxGNN model predicts it may be effective for **metastatic melanoma**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license records (approved indication text is empty for all three licenses) |
| Predicted New Indication | Metastatic melanoma |
| TxGNN Prediction Score | 96.26% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mephenesin is a centrally acting muscle relaxant of the propanediol class, sold in India as a topical gel. No mechanistic link to melanoma has been established.

The high TxGNN score most likely reflects similarity within the knowledge graph rather than a validated biological pathway. The other top predictions support this reading. Several are melanoma subtypes (non-cutaneous, epithelioid cell and eyelid melanoma) that probably share one cluster and are not independent evidence. Several others are cataract subtypes with an identical score of 95.47%, which points to a shared ontology-driven prediction. Choroideremia, a monogenic retinal degeneration, also appears, with no plausible connection to a muscle relaxant.

This prediction should be treated as a hypothesis-generating signal only.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121240 | Lignogesic Gel (Medley Pharmaceuticals) | Tube of 30 gm gel | Not stated |
| 76887 | Ethnorub Gel (Strides Shasun Ltd) | Tube of 30 gm gel | Not stated |
| 8661 | Actofenal Gel 4X (Nexcellence Lifesciences) | Tube of 30 gm gel | Not stated |

All three licenses are valid single-ingredient products, and all are topical gels. No systemic formulation is registered.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, no literature and no mechanistic rationale. Mephenesin is available in India only as a topical gel, and the available data do not show a route that would suit metastatic melanoma.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the India regulator (currently missing and blocking safety screening)
- Mechanism of action data, to test any biological link to melanoma
- A literature and trial search, including preclinical work, for mephenesin or related propanediols in melanoma
- Route compatibility assessment, since only topical gels are marketed and metastatic disease would likely need systemic exposure
- Independent confirmation that the melanoma subtype predictions are not just one duplicated signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

