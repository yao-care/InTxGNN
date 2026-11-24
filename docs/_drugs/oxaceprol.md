---
layout: default
title: Oxaceprol
parent: Model Prediction Only (L5)
nav_order: 624
evidence_level: L5
indication_count: 9
monitor_inn: "Oxaceprol"
predicted_indications: ["ankylosing spondylitis", "brachyolmia-amelogenesis imperfecta syndrome", "juvenile idiopathic arthritis", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid vasculitis", "pseudoachondroplasia"]
last_modified_at: 2026-11-24
description: "Oxaceprol: predicted new indication Ankylosing spondylitis (evidence level L5). Approved use: Osteoarthritis and arthropathy"
---

# Oxaceprol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Oxaceprol: From Osteoarthritis to Ankylosing Spondylitis
{: .text-alpha }

## One-Sentence Summary

Oxaceprol is a proline derivative (N-acetyl-hydroxyproline) used for joint conditions such as osteoarthritis. The TxGNN model predicts it may be effective for **ankylosing spondylitis**, but **no clinical trials and no publications** were found to support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis and arthropathy (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Ankylosing spondylitis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Oxaceprol is generally described as a proline derivative with a proposed effect on cartilage metabolism and reduced leukocyte infiltration into joints. These points come from general knowledge rather than from the data compiled for this report, and they should be verified.

The score for ankylosing spondylitis (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

However, ankylosing spondylitis is an axial, HLA-B27-associated spondyloarthritis driven mainly by IL-17 and TNF pathways. Its biology differs substantially from degenerative joint disease, so the mechanistic connection is weak. The high score (0.9995) is a model prediction only and has not been validated.

Other top predictions are mostly rare skeletal dysplasias or autoimmune arthritis variants (for example juvenile idiopathic arthritis, rheumatoid vasculitis and pseudoachondroplasia). None has any supporting trial or publication in the compiled data.

---

## India Market Information

Oxaceprol is marketed in India. At least 20 single-ingredient registrations are on record, and the list may be partial. No approved indication text is recorded in these licences.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 11421 | Aksiprol Tablet | Strip of 10 tablets | Valid |
| 13368 | Aksiprol OD 600mg Tablet | Strip of 10 tablets | Valid |
| 19506 | Arthoprol 200mg Capsule | Strip of 10 capsules | Valid |
| 40609 | Ceprol Tablet SR | Strip of 10 tablet sr | Valid |
| 79019 | Ezrol Capsule | Strip of 10 capsules | Valid |
| 109878 | Iboxa Capsule | Strip of 10 capsules | Valid |
| 111942 | Iboxa OD Tablet | Strip of 10 tablets | Valid |
| 116504 | Kneerol OD Tablet SR | Strip of 10 tablet sr | Valid |
| 116566 | Kneox Tablet | Strip of 15 tablets | Valid |
| 155634 | Neoxacep Capsule | Strip of 10 capsules | Valid |
| 162490 | Oxuba Capsule | Strip of 10 capsules | Valid |
| 166231 | Oxcp 200 Capsule | Strip of 10 capsules | Valid |
| 167858 | Oxafirst 200mg Capsule | Strip of 10 capsules | Valid |
| 168095 | Oxapol 200mg Capsule | Strip of 10 capsules | Valid |
| 171698 | Oxasoft 200mg Capsule | Strip of 10 capsules | Valid |
| 186944 | Roxupol-OD Tablet ER | Strip of 10 tablet er | Valid |
| 201008 | Steoxa 200mg Capsule | Strip of 10 capsules | Valid |
| 202139 | StayHappi Oxaceprol 200mg Capsule | Strip of 10 capsules | Valid |
| 215745 | Trueceprol OD Tablet SR | Strip of 10 tablet sr | Valid |
| 249155 | Zextra Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All listed products are oral forms (capsules, tablets, sustained-release and extended-release tablets).

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were available in the data compiled for this report, and no drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications for ankylosing spondylitis, and the mechanistic link is weak. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for oxaceprol, to test relevance to IL-17/TNF-driven axial inflammation
- Package insert warnings, contraindications and indication text from Indian licences
- Preclinical or early clinical evidence directly studying oxaceprol in ankylosing spondylitis
- A review of whether other candidates, such as rheumatoid or juvenile arthritis variants, have better supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

