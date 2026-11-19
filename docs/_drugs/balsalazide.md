---
layout: default
title: Balsalazide
parent: Model Prediction Only (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Balsalazide: predicted new indication Gout (evidence level L5). Approved use: Ulcerative colitis, inflammatory bowel disease"
monitor_inn: "Balsalazide"
predicted_indications: ["gout", "congenital hypotrichosis with juvenile macular dystrophy", "ankylosing spondylitis", "rheumatoid arthritis", "rheumatoid vasculitis", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis", "anus disease"]
---

# Balsalazide
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

## Balsalazide: From Ulcerative Colitis to Gout
{: .text-alpha }

## One-Sentence Summary

Balsalazide was originally used to treat ulcerative colitis and inflammatory bowel disease.
The TxGNN model predicts it may be effective for **gout**, but this is a model prediction only,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for balsalazide: "Balsalazide disodium is delivered intact to the colon where it is cleaved by bacterial azoreduction to release equimolar quantities of mesalamine, which is the therapeutically active portion of the molecule, and the 4-aminobenzoyl-β-alanine carrier moiety. The carrier moiety released when balsalazide disodium is cleaved is only minimally absorbed and is largely inert." ([DailyMed: balsalazide disodium prescribing information, Zydus Pharmaceuticals (USA) Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed73067-e2ca-4184-a93a-5a2141bb4898), label version 2026-11-03; accessed 2026-11-19.) Based on known information, balsalazide is a prodrug of mesalamine (5-ASA), an anti-inflammatory agent. Its efficacy in ulcerative colitis is established, and mechanistically it may be applicable to inflammatory conditions such as gout.

The known anti-inflammatory activity of 5-ASA includes inhibition of prostaglandin and leukotriene synthesis, modulation of NF-kB, and radical scavenging. These pathways could plausibly overlap with the inflammation seen in gout. This link is speculative: no direct mechanistic connection is established in the data compiled for this report, and the high score is a model output only.

Other top-ranked predictions are mostly inflammatory joint or spine conditions (ankylosing spondylitis, rheumatoid arthritis, inflammatory spondylopathy, polyarticular juvenile rheumatoid arthritis). Several others (congenital hypotrichosis with juvenile macular dystrophy, hypermobility of coccyx, Kummell disease) have no plausible biological link and are likely TxGNN model (deep learning) artifacts. For the rheumatoid conditions, the benefit of the related drug sulfasalazine is generally attributed to its sulfapyridine component rather than 5-ASA, which weakens extrapolation to balsalazide.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 38806 | Cozabal 750mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 32753 | Balsacol 750mg Capsule (Gufic Bioscience Ltd) | Strip of 10 capsules | Not stated |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, pyloric stenosis
- **Drug Interactions**: 196 interacting drugs were identified. One is rated Major: intravenous human immunoglobulin G. Moderate interactions include:
  - NSAIDs: ketorolac, ibuprofen, celecoxib
  - Aminoglycosides and other nephrotoxic agents: amikacin, amphotericin B (including lipid formulations), foscarnet, gallium nitrate
  - Antibiotics: doxycycline, amoxicillin, ampicillin, azithromycin, bacitracin, fosfomycin
  - Others: acyclovir, azathioprine, acetohexamide

  Many of these are nephrotoxic agents, which is notable given the kidney disease contraindication signal. Of note, NSAIDs are commonly used in gout, so co-prescription is a practical concern.

Please also refer to the package insert for full warnings, as label-based warnings were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests only on a high model score. No clinical trials or literature support it, the mechanistic link is speculative, and label-based safety data are missing. Possible renal concerns and frequent NSAID co-use in gout add caution.

**To proceed, the following is needed:**
- Retrieve the India package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism of action data
- Run a systematic literature and trial search for 5-ASA or balsalazide in gout and in inflammatory arthritis
- Evaluate route compatibility and similarity to the original indication (both still pending)
- Consider the more biologically plausible inflammatory candidates (e.g., ankylosing spondylitis, inflammatory spondylopathy) for comparison

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: balsalazide disodium prescribing information, Zydus Pharmaceuticals (USA) Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed73067-e2ca-4184-a93a-5a2141bb4898) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

