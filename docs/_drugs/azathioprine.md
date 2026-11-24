---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Azathioprine: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Azathioprine"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Azathioprine is an immunosuppressant (a purine antimetabolite) originally used for rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome,
but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of azathioprine as: Amidophosphoribosyltransferase inhibitor; DNA inhibitor ([ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, azathioprine is a thiopurine immunosuppressant, and its efficacy in rheumatoid arthritis and other immune-mediated conditions is established.

For this specific prediction, however, no plausible mechanistic link could be identified. The predicted condition is a rare developmental malformation syndrome. Azathioprine's immunosuppressive, purine-antimetabolite action has no known relevance to its underlying biology. The very high score from the TxGNN model (deep learning) (1.0000) may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Azathioprine is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. The registrations listed in the compiled data carry no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 279 | AZR Tablet | Strip of 10 tablets | Valid |
| 1325 | ATZ 50 Tablet | Strip of 10 tablets | Valid |
| 2607 | Azaprin Tablet | Strip of 10 tablets | Valid |
| 3093 | Aprin 50mg Tablet | Strip of 10 tablets | Valid |
| 7004 | Azawan Tablet | Strip of 10 tablets | Valid |
| 7576 | Azathiol 50mg Tablet | Strip of 10 tablets | Valid |
| 7807 | Autorin 50mg Tablet | Strip of 10 tablets | Valid |
| 7920 | Aparin 50mg Tablet | Strip of 10 tablets | Valid |
| 8835 | Azoth 50 Tablet | Strip of 10 tablets | Valid |
| 10265 | A Pin 50mg Tablet | Strip of 10 tablets | Valid |
| 11651 | Azatoz 50mg Tablet | Strip of 10 tablets | Valid |
| 11695 | Azoalfa 50 Tablet | Strip of 10 tablets | Valid |
| 108077 | Imoprine Tablet | Strip of 10 tablets | Valid |
| 109067 | Immugo Tablet | Strip of 10 tablets | Valid |
| 130224 | Lazorin 50mg Tablet | Strip of 10 tablets | Valid |
| 155572 | Neoprine 50mg Tablet | Strip of 10 tablets | Valid |
| 180576 | Priorg 50mg Tablet | Strip of 10 tablets | Valid |
| 217432 | Thiopress Tablet | Strip of 10 tablets | Valid |
| 220374 | Transimune 50mg Tablet | Strip of 10 tablets | Valid |
| 234855 | Vaprin Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Conditions flagged as contraindication-related in the knowledge graph** (not drawn from label text): pancreatitis, thrombocytopenia, anaemia (including macrocytic anaemia), impaired renal function, infectious disease (including fungal infection and dermatophytosis), lymphoma (including primary CNS lymphoma, lymphosarcoma and hepatosplenic T-cell lymphoma), hepatic vein thrombosis and Budd-Chiari syndrome.
- **Drug Interactions:** 447 interactions were recorded. The main moderate-level ones are the aminosalicylates **mesalazine, balsalazide, olsalazine and sulfasalazine**. Minor interactions include zinc salts (acetate, gluconate, sulfate).
- **Considerations for the predicted indication:** Azathioprine's myelosuppressive effects and infection risk have no offsetting mechanistic benefit in this condition.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5) and no plausible mechanistic link to azathioprine's action. The high score from the TxGNN model (deep learning) may reflect similarities the model learned between related diseases, not biological evidence, and the safety profile offers no compensating benefit.

**To proceed, the following is needed:**
- Any mechanistic or preclinical rationale connecting purine antimetabolite immunosuppression to this syndrome's pathophysiology
- Detailed mechanism of action data for azathioprine
- Package insert warnings and contraindications for the India-marketed products
- Consideration of TPMT/NUDT15 genotyping and blood count and liver monitoring as guardrails

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

