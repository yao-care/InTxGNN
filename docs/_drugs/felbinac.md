---
layout: default
title: Felbinac
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Felbinac: predicted new indication Brachyolmia-amelogenesis imperfecta syndrome (evidence level L5). Approved use: Osteoarthritis, arthropathy"
monitor_inn: "Felbinac"
predicted_indications: ["brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "rheumatoid nodulosis", "combined immunodeficiency due to moesin deficiency"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Felbinac: From Osteoarthritis to Brachyolmia-Amelogenesis Imperfecta Syndrome

## One-Sentence Summary

Felbinac is a topical NSAID (non-steroidal anti-inflammatory drug) originally used for osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **brachyolmia-amelogenesis imperfecta syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, arthropathy (the Indian licence lists no approved indication text; these indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Felbinac is known to be a topical NSAID that acts through COX inhibition, and its role in osteoarthritis is symptomatic relief of pain and inflammation.

Brachyolmia-amelogenesis imperfecta syndrome is a rare genetic skeletal and dental disorder, associated with LTBP3 variants that affect TGF-beta signalling. COX inhibition is not expected to act on this pathway, so no mechanistic link has been established. The very high TxGNN score is a graph-based prediction and is likely driven by shared skeletal or joint-related neighbours in the knowledge graph, not by pharmacological rationale.

Other top-ranked predictions show the same pattern. Several are genetic skeletal conditions with no plausible NSAID target (acromesomelic dysplasia Hunter-Thompson type, brachyolmia, myosclerosis, combined immunodeficiency due to moesin deficiency). The more plausible ones are inflammatory joint diseases where NSAIDs give symptomatic relief only: spondyloarthropathy susceptibility, rheumatoid nodulosis, juvenile idiopathic arthritis and its RF-positive polyarticular subtype, and pseudoachondroplasia (where early joint pain and osteoarthritis occur). None has felbinac-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 88988 | Felbimax Gel (Lupin Ltd) | Tube of 30 gm Gel | Not stated |

Felbinac is available in India only as a topical gel.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. There are no clinical trials or publications, and no mechanistic link between COX inhibition and the underlying biology of this genetic syndrome. A topical NSAID is also unlikely to be useful for a skeletal and dental disorder.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking felbinac to this syndrome
- Route-compatibility and disease-similarity assessments, which are still pending
- If a repurposing direction is wanted, consider the more plausible symptomatic candidates (spondyloarthropathy, juvenile idiopathic arthritis) for literature review first, with pediatric safety and dosing established for the JIA subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

