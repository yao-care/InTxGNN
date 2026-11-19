---
layout: default
title: Epinastine
parent: Model Prediction Only (L5)
nav_order: 313
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Epinastine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis"
monitor_inn: "Epinastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
---

# Epinastine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Epinastine: From Allergic Conjunctivitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Epinastine is a topical antihistamine originally used to treat allergic conjunctivitis (atopic, papillary and vernal forms).
The TxGNN model predicts it may be effective for **Rosacea Conjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for epinastine: "Epinastine is a topically active, direct H 1 -receptor antagonist and an inhibitor of the release of histamine from the mast cell. Epinastine is selective for the histamine H 1 -receptor and has affinity for the histamine H 2 -receptor." ([DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d), label version 2025-03-22; accessed 2026-11-19.) Based on known information, epinastine is a topical H1 receptor antagonist with mast cell stabilising activity. Its efficacy in allergic conjunctivitis is established, and it may be mechanistically applicable to other inflammatory conditions of the ocular surface.

The link to rosacea conjunctivitis is only a partial fit. Epinastine could relieve itching and surface inflammation. However, ocular disease in rosacea is driven mainly by meibomian gland dysfunction, eyelid inflammation, and microbial or Demodex factors, rather than classic IgE-mediated histamine release. The very high model score (0.9957) therefore cannot be confirmed mechanistically at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

For reference, the second-ranked prediction, allergic urticaria, has indirect literature on epinastine's antihistamine pharmacology (for example, [PMID 10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/), a 1999 double-blind crossover study of histamine-induced wheal and flare suppression in healthy volunteers). This does not support the rosacea conjunctivitis prediction.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 189485 | Relestat Ophthalmic Solution (Allergan India Pvt Ltd) | 5 ml ophthalmic solution | Not specified |
| 74323 | Estina Eye Drop (Entod Pharmaceuticals Ltd) | 5 ml eye drop | Not specified |
| 80560 | Eparto Eye Drop (Neiss Labs Pvt Ltd) | 5 ml eye drop | Not specified |
| 73608 | Epitane Eye Drop (Micro Labs Ltd) | 5 ml eye drop | Not specified |

All four registrations are valid single-ingredient ophthalmic products, so the route of administration is already suited to an ocular indication.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or literature were found, and the antihistamine mechanism fits rosacea-related ocular disease only partly. The drug is already marketed in India as an eye drop, which would ease any future study.

**To proceed, the following is needed:**
- A targeted literature and trial search on antihistamines or mast cell stabilisers in ocular rosacea and meibomian gland dysfunction
- Mechanism of action data to assess the biological link
- Package insert warnings and contraindications for the marketed Indian products, to complete safety screening
- Approved indication text for the Indian registrations
- If the hypothesis still looks credible, a small exploratory study that measures symptoms such as itching and eyelid inflammation

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

