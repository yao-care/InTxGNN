---
layout: default
title: Rofecoxib
parent: Model Prediction Only (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rofecoxib: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, migraine…"
monitor_inn: "Rofecoxib"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia"]
---

# Rofecoxib
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

# Rofecoxib: From Rheumatoid Arthritis and Osteoarthritis to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Rofecoxib is a selective COX-2 inhibitor (an NSAID) originally used for arthritic and inflammatory conditions such as rheumatoid arthritis, osteoarthritis and migraine.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.
The drug's known prothrombotic safety signal also runs against this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, migraine, juvenile idiopathic arthritis, spondyloarthropathy (the product labels in India list no indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed (should be verified, see below) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, rofecoxib is a selective COX-2 inhibitor. Its efficacy in inflammatory joint disease and pain is well established.

Heparin cofactor 2 deficiency is an inherited thrombophilic disorder involving a serine protease inhibitor (SERPIND1). No credible mechanistic link exists between COX-2 inhibition and this condition. The high score most likely reflects proximity between nodes in the knowledge graph, not a biological rationale.

Rofecoxib was withdrawn from many markets because of increased cardiovascular thrombotic risk. Using it in a prothrombotic condition would therefore raise a significant safety concern, so the prediction points in the wrong direction.

The other top-ranked predictions show the same pattern:
- **Other thrombophilic disorders** (factor 5 excess with spontaneous thrombosis, antithrombin deficiency type 2): no plausible mechanism, and the same safety concern applies.
- **Congenital skeletal or developmental syndromes** (for example brachydactyly-syndactyly syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia): an NSAID would not be expected to correct a genetic structural malformation.
- **Spondyloarthropathy, susceptibility to** (rank 5): biologically plausible, since COX-2 inhibitors are used for symptom relief in spondyloarthritis. However, it overlaps with an existing indication and is not a new repurposing finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 92030 | Flexib 100mg Tablet | Strip of 15 tablets | Not specified |
| Registration No. 197698 | Rofejet Gel | Tube of 20 gm gel | Not specified |
| Registration No. 164793 | Oslol 20mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 171767 | Okabax 12.5mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 197904 | Roflam 50mg Tablet | Strip of 10 tablets | Not specified |

There are 20 valid single-ingredient registrations in total, including oral tablets and capsules and topical gels. The database lists the product as marketed, but rofecoxib has been withdrawn in most markets, so the actual market status should be verified.

## Safety Considerations

- **Drug Interactions**: 246 interacting drugs were found. The 20 shown in the data compiled for this report are all Moderate level. They include:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - Other anti-inflammatory drugs: acetylsalicylic acid, mesalazine, balsalazide
  - Antidiabetic drugs: metformin, glimepiride, chlorpropamide, nateglinide
  - Antibiotics: vancomycin, kanamycin, levofloxacin
  - Bowel preparations: picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate
  - Others: alosetron, naltrexone
- **Class-level concern**: Rofecoxib is associated with increased thrombotic cardiovascular events, which was the reason for its market withdrawal. This matters especially for any thrombophilic indication.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score, with no clinical trials, no literature and no plausible mechanism. Rofecoxib's prothrombotic signal makes it a safety concern, not a therapeutic opportunity, for thrombophilic conditions such as heparin cofactor 2 deficiency.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India's regulatory sources (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking COX-2 inhibition to the predicted condition
- Verification of the current market and withdrawal status of rofecoxib in India
- Thrombotic and cardiovascular risk assessment before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

