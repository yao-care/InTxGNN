---
layout: default
title: Halometasone
parent: Model Prediction Only (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Halometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L4). Approved use: Not specified in the registration data"
monitor_inn: "Halometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "polyp of vocal cord", "polyp of middle ear", "uterine polyp", "polyp of external auditory canal", "polyp of frontal sinus", "polyp of ureter", "fibroepithelial polyp", "polyp of vulva", "neoplastic polyp"]
---

# Halometasone
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

## Halometasone: From Topical Corticosteroid Therapy to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Halometasone is a potent topical corticosteroid, marketed in India as a cream.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**,
but **no clinical trials and no publications** were found to support this prediction, so it remains a model-based research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the registration data |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Based on known class information, halometasone is a potent topical corticosteroid (a glucocorticoid receptor agonist). It is marketed in India only as a dermatologic cream, and the registration records do not state its approved indications.

Topical corticosteroids are an established skin-directed therapy for early-stage mycosis fungoides, the most common primary cutaneous T-cell lymphoma. In this setting they reduce inflammation and can induce apoptosis of malignant T cells. This is class-level knowledge, not drug-specific evidence for halometasone. The high TxGNN score is a model prediction only, and a topical route fits skin-limited disease.

Nine other predicted indications (various polyps, such as vocal cord, middle ear, uterine, ureter, vulvar, frontal sinus, external auditory canal, fibroepithelial and neoplastic polyps) also scored between 0.9956 and 0.9958. None has any clinical evidence. Most involve sites a dermatologic cream cannot plausibly reach, or conditions treated by surgical removal, so they are not considered credible repurposing directions.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73013 | Execare Cream | Cream (tube of 10 gm) | Not stated |
| 103820 | Halox F Cream | Cream (tube of 10 gm) | Not stated |
| 104383 | Halostrol-F Cream | Cream (tube of 10 gm) | Not stated |
| 72919 | Execare-F Cream | Cream (tube of 10 gm) | Not stated |

All four registrations are valid single-ingredient products.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and class-level reasoning alone, with no clinical trials or literature for halometasone in this indication. Evidence is insufficient to advance, although primary cutaneous T-cell lymphoma is the only predicted indication with a plausible topical-route rationale.

**To proceed, the following is needed:**
- Literature and trial searches specific to halometasone in mycosis fungoides or cutaneous T-cell lymphoma
- Package insert warnings and contraindications from the India registrations, plus approved indication text
- Mechanism of action data from DrugBank
- Comparison with established topical corticosteroids already used in early-stage mycosis fungoides
- Assessment of route compatibility and the suitability of the cream formulation for skin lesions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

