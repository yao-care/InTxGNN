---
layout: default
title: Leflunomide
parent: Model Prediction Only (L5)
nav_order: 475
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Leflunomide: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Leflunomide
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

## Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome
{: .text-alpha }

## One-Sentence Summary

Leflunomide is an oral immunomodulatory drug originally used to treat rheumatoid arthritis and psoriatic arthritis.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
However, there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; psoriatic arthritis (from the knowledge graph, as no approved indication text is available in the India licence records) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on generally known pharmacology, leflunomide inhibits dihydroorotate dehydrogenase (DHODH). This blocks de novo pyrimidine synthesis and limits the proliferation of activated lymphocytes, which explains its benefit in rheumatoid and psoriatic arthritis.

A mechanistic link between these autoimmune joint diseases and a congenital limb malformation is not evident. A speculative route could run through shared developmental pathways, such as pyrimidine metabolism, cell proliferation, or limb-bud signalling. Nothing in the available data supports this. The very high score may reflect proximity in the knowledge graph (shared genes or pathways) rather than true therapeutic relevance.

There is also a safety concern. DHODH inhibition is associated with teratogenicity, and leflunomide is contraindicated in pregnancy. This makes use in a developmental disorder counterintuitive. The prediction should be treated as a hypothesis-generating signal only.

A second prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 99.93%), is in the same position. It has no trials or literature and no clear mechanistic rationale, and the same teratogenicity caution applies.

## India Market Information

Leflunomide is widely marketed in India as a single-ingredient oral tablet. There are 20 valid registrations and none cancelled. Approved indication text is not available for any of them. The main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 124048 | Lefnol 20mg Tablet (Cista Medicorp) | Strip of 10 tablets | Not available |
| 36008 | Cleft 20 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not available |
| 131085 | Leflodol 100mg Tablet (TNT Lifesciences) | Strip of 10 tablets | Not available |
| 125008 | Lefnol 10mg Tablet (Cista Medicorp) | Strip of 10 tablets | Not available |
| 125771 | Lefno 5mg Tablet (Ipca Laboratories Ltd) | Strip of 10 tablets | Not available |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The drug-disease contraindication links in the knowledge graph include:
  - Liver: liver failure, liver disease, gallbladder disease, chronic hepatitis B and C virus infection.
  - Kidney: kidney disease.
  - Blood: neutropenia (including congenital forms), agranulocytosis, thrombocytopenia, anaemia, pancytopenia.
  - Lung: interstitial lung disease.
  - Nerves: peripheral neuropathy.
  - Infection: pneumocystosis, aspergillosis.
- **Pregnancy**: Leflunomide is known to be teratogenic and contraindicated in pregnancy. This is especially relevant for the predicted developmental-disorder indications.
- **Drug Interactions**: 677 interactions were recorded. Major-level examples include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide.
  - Antidiabetics: pioglitazone, acarbose.
  - Antibiotics: clarithromycin, minocycline.
  - Others: acetylsalicylic acid, bupropion, naltrexone, oxandrolone, oxymetholone, chenodeoxycholic acid.

  Moderate-level examples include metronidazole, chlorpropamide and acetohexamide.

Package insert warnings were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (L5). No clinical trials or literature support it, and the mechanistic link to a congenital limb malformation is unclear. The drug's teratogenic risk adds a serious safety concern for a developmental-disorder indication.

**To proceed, the following is needed:**
- Independent mechanistic validation, such as the knowledge-graph genes or pathways behind the prediction and any preclinical model evidence
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India licence documents
- A literature and trial search specific to the predicted rare syndromes
- A teratogenicity risk assessment for any developmental-disorder indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

