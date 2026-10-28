---
layout: default
title: Levocetirizine
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Levocetirizine: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, idiopathic urticaria"
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Levocetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Levocetirizine: From Allergic Rhinitis to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Levocetirizine is an H1 antihistamine originally used to treat allergic rhinitis, vasomotor rhinitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but **no clinical trials and no publications** currently support this direction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, idiopathic urticaria |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levocetirizine is a selective histamine H1 receptor antagonist. Its efficacy in allergic rhinitis and urticaria is established, and it may mechanistically be applicable to rheumatoid arthritis.

A possible, unvalidated link is that histamine signalling may contribute to synovial inflammation, mast cell activity and vascular permeability in rheumatoid arthritis. This link cannot be verified from the data compiled for this report. Any anti-inflammatory effect would likely be modest compared with established disease-modifying therapies.

The score is high (0.9973, rank 5273), but it reflects a model prediction rather than observed clinical benefit.

Two other predictions, colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9959) and brachydactyly-syndactyly syndrome (0.9952), have no identifiable mechanistic link. They are developmental or genetic disorders that H1 receptor blockade is not expected to correct. Their high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Both are also L5 with a Hold recommendation.

## India Market Information

The 20 registrations are all valid single-ingredient licences, with no cancellations. Approved indication text was not available for any of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 131557 | Lowip-M KID 2.5mg/4mg Tablet | Strip of 10 tablets | Not stated |
| 247737 | Zycet M 5mg/10mg Tablet | Strip of 10 tablets | Not stated |
| 148719 | Monolens-LC Oral Suspension | Bottle of 60 ml oral suspension | Not stated |
| 129038 | Levuxia 5mg Tablet | Strip of 10 tablets | Not stated |
| 165939 | Oviday 5mg Tablet | Strip of 10 tablets | Not stated |

All products are oral (tablets and one oral suspension).

## Safety Considerations

- **Disease associations (knowledge graph, not label text)**: Contraindication links were found for kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure and pyoureter. Renal function should be considered carefully.
- **Drug Interactions**: 241 interactions were recorded. The 20 listed are mostly Moderate, with one Minor (hyaluronidase). Main ones:
  - Central nervous system depressants and opioids: morphine, fentanyl, dihydrocodeine, opium, loperamide, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Other sedating antihistamines: promethazine, chlorpheniramine
  - Other: ethanol, bupropion, metoclopramide, sibutramine, histamine, radioactive iodide (I-123, I-131)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high TxGNN score. There are no clinical trials or publications, and no mechanism data. The proposed histamine link to rheumatoid arthritis is unverified, and any effect would likely be modest compared with established therapies.

**To proceed, the following is needed:**
- Mechanism of action data and a validated mechanistic link between H1 blockade and rheumatoid arthritis
- Preclinical or early clinical evidence in rheumatoid arthritis
- Package insert warnings and contraindications for the India-marketed products (currently missing and blocking safety screening)
- Approved indication text for the India registrations
- Renal safety assessment, given the kidney-related associations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

