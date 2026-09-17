---
layout: default
title: Felbinac
parent: Model Prediction Only (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Felbinac
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

# Felbinac: From Topical Anti-inflammatory Use to Brachyolmia-Amelogenesis Imperfecta Syndrome

## One-Sentence Summary

Felbinac (DrugBank DB07477) has no confirmed original indication on record in this evidence pack, but is described in the underlying data as a topical NSAID (COX inhibition, local anti-inflammatory/analgesic action). The TxGNN model's top prediction is **Brachyolmia-Amelogenesis Imperfecta Syndrome**, a rare genetic skeletal/dental dysplasia, but this pairing has **zero clinical trials, zero literature, and no known mechanistic link** — the model's own rationale text flags a lack of biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (no approved indication text available; drug reportedly classified as a topical NSAID) |
| Predicted New Indication | Brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the information embedded in the model's own rationale text across candidates, Felbinac is a **topical NSAID** acting through COX inhibition to produce local anti-inflammatory and analgesic effects.

Brachyolmia-amelogenesis imperfecta syndrome, however, is a hereditary skeletal and dental developmental disorder caused by structural genetic defects — it is not an inflammatory condition. The evidence pack's own mechanistic_link assessment for this top-ranked candidate explicitly states there is **no known mechanistic relationship** between COX-mediated anti-inflammatory action and this genetic syndrome, and that the model's high confidence score "lacks biological plausibility support."

Notably, several lower-ranked candidates in this pack (e.g., rank 6 spondyloarthropathy, rank 7 rheumatoid nodulosis, ranks 9–10 juvenile idiopathic arthritis) are inflammatory joint conditions where NSAID pharmacology has directional plausibility — these may be more scientifically defensible follow-up targets than the top-ranked prediction, even though none currently have Felbinac-specific trial or literature support either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Felbinac has no marketing authorizations on record in Taiwan (0 registrations; market status: Not marketed / Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications for Felbinac are currently a **Blocking** data gap (DG001) — this must be resolved before any safety-stage (S1) evaluation can proceed, and no drug interaction data could be located (DDI query: not found).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on an L5 model score with no supporting trials or literature, and the pack's own mechanistic assessment finds no biological plausibility for the top-ranked indication (brachyolmia-amelogenesis imperfecta syndrome). Combined with the blocking gap on TFDA safety labeling and the drug's unmarketed status in Taiwan, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) to close the blocking gap (DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- If pursuing repurposing, redirect evaluation toward mechanistically plausible candidates lower in the ranking (e.g., spondyloarthropathy, JIA) and search for Felbinac-specific evidence there
- Dedicated literature/trial search for Felbinac in inflammatory joint disease before any further staging
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

