---
layout: default
title: Oxaceprol
parent: Model Prediction Only (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oxaceprol: predicted new indication Spondyloarthropathy, susceptibility to (evidence level L5). Approved use: Osteoarthritis, osteoarthritis susceptibility, arthropathy"
monitor_inn: "Oxaceprol"
predicted_indications: ["spondyloarthropathy, susceptibility to", "ankylosing spondylitis", "brachyolmia-amelogenesis imperfecta syndrome", "juvenile idiopathic arthritis", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid vasculitis", "pseudoachondroplasia"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Oxaceprol: From Osteoarthritis to Spondyloarthropathy (Susceptibility)
{: .text-alpha }

## One-Sentence Summary

Oxaceprol is an oral agent used for osteoarthritis and related joint disorders (arthropathy).
The TxGNN model predicts it may be effective for **spondyloarthropathy, susceptibility to**,
but **no clinical trials and no publications** currently support this prediction, so it is a model-based hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, osteoarthritis susceptibility, arthropathy (the approved-indication text is empty in the India licence records; these come from the knowledge-graph indication data) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxaceprol is a proline-derivative joint agent used in osteoarthritis. It is reported to be cartilage-protective and anti-inflammatory, possibly by inhibiting leukocyte migration into joints. This has not been verified in the data compiled for this report.

The predicted indication is a genetic susceptibility phenotype for spondyloarthropathy. It is related to the original joint indications only indirectly. The prediction most likely reflects the closeness of these diseases to the existing arthropathy and osteoarthritis indications in the knowledge graph, not a demonstrated therapeutic effect.

Other predicted indications are also supported only by model scores. The more biologically plausible ones are inflammatory joint diseases such as **juvenile idiopathic arthritis** (score 99.95%) and **ankylosing spondylitis** (score 99.95%). Ankylosing spondylitis is driven by axial, immune pathways (HLA-B27, IL-17/TNF), and no data show that oxaceprol acts on them. Juvenile idiopathic arthritis has no paediatric safety or efficacy data. Rare genetic skeletal disorders in the list (for example brachyolmia-amelogenesis imperfecta syndrome, acromesomelic dysplasia, pseudoachondroplasia and myosclerosis) have very low plausibility and likely reflect network artefacts. Rheumatoid vasculitis needs immunosuppression, and relying on this prediction could be clinically risky.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty valid single-ingredient registrations were found. The approved-indication text is not recorded for any of them. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 171698 | Oxasoft 200mg Capsule | Strip of 10 capsules | Not recorded |
| 116504 | Kneerol OD Tablet SR | Strip of 10 SR tablets | Not recorded |
| 215745 | Trueceprol OD Tablet SR | Strip of 10 SR tablets | Not recorded |
| 249155 | Zextra Capsule | Strip of 10 capsules | Not recorded |
| 40609 | Ceprol Tablet SR | Strip of 10 SR tablets | Not recorded |

All products are oral (capsules, tablets, sustained- or extended-release tablets).

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a knowledge-graph score (L5), with no trials, no literature and no verified mechanism. The link between oxaceprol and a genetic susceptibility phenotype is speculative. The drug is widely marketed in India, but its approved indications and safety text are not available in the data compiled for this report.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- A literature and trial search for oxaceprol in spondyloarthritis and juvenile idiopathic arthritis, the more plausible candidates
- A paediatric safety review before considering juvenile idiopathic arthritis
- Reassessment of the candidate list, prioritising inflammatory arthropathies over rare genetic skeletal disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

