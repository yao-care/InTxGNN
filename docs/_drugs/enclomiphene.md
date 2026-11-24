---
layout: default
title: Enclomiphene
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Enclomiphene: predicted new indication Acute intermittent porphyria (evidence level L5). Approved use: Not stated in the compiled licence data"
monitor_inn: "Enclomiphene"
drugbank_id: DB06735
predicted_indications: ["acute intermittent porphyria", "psychogenic movement disorders", "chronic tic disorder", "benign shuddering attacks", "extrapyramidal and movement disease", "primary orthostatic tremor", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "carbamoyl phosphate synthetase I deficiency disease"]
---

# Enclomiphene
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

## Enclomiphene: From an Unspecified Approved Indication to Acute Intermittent Porphyria
{: .text-alpha }

## One-Sentence Summary

Enclomiphene is a selective estrogen receptor modulator (the trans-isomer of clomiphene) that is marketed in India, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**, but this is a model output only.
**No clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled licence data |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (17 of 17) – CDSCO approval status is not included in this data |
| Number of Listed Products | 17 (valid: 17) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, enclomiphene is a selective estrogen receptor modulator. It blocks estrogen feedback at the hypothalamus, which raises LH and FSH secretion. It is mainly associated with male hypogonadism and fertility-related use.

Acute intermittent porphyria is a heme biosynthesis disorder caused by HMBS deficiency. Hormonal changes can influence the frequency of porphyria attacks, so a link through endocrine modulation is conceivable. However, no data support a role for enclomiphene in this disease, and no mechanistic link has been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and should be treated as a hypothesis only.

Other top-ranked predictions are also unsupported by evidence (see the table below).

| Rank | Predicted Disease | TxGNN Score |
|------|------|------|
| 2 | Psychogenic movement disorders | 0.9965 |
| 3 | Chronic tic disorder | 0.9964 |
| 4 | Benign shuddering attacks | 0.9964 |
| 5 | Extrapyramidal and movement disease | 0.9964 |
| 6 | Primary orthostatic tremor | 0.9963 |
| 7 | Tremor-nystagmus-duodenal ulcer syndrome | 0.9962 |
| 8 | Lingual-facial-buccal dyskinesia | 0.9962 |
| 9 | Benign paroxysmal tonic upgaze of childhood with ataxia | 0.9961 |
| 10 | Carbamoyl phosphate synthetase I deficiency disease | 0.9948 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Enclomiphene has 17 valid single-ingredient registrations in India and none cancelled. The approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 73311 | EN-Clofert 50 Tablet | Strip of 5 tablets | Valid |
| 77774 | Enclopure 100mg Tablet | Strip of 5 tablets | Valid |
| 78420 | Engamet 25mg Tablet | Strip of 5 tablets | Valid |
| 78506 | Enos 50mg Tablet | Strip of 10 tablets | Valid |
| 78822 | Enos 25mg Tablet | Strip of 5 tablets | Valid |
| 79245 | Enclowin 100mg Capsule | Strip of 5 capsules | Valid |
| 79843 | Engamet 50mg Tablet | Strip of 5 tablets | Valid |
| 79900 | Enclowin 50mg Capsule | Strip of 5 capsules | Valid |
| 81940 | Enclowin 25mg Capsule | Strip of 5 capsules | Valid |
| 156853 | N Clomi 50mg Tablet | Strip of 5 tablets | Valid |
| 157975 | N Clomi 100mg Tablet | Strip of 5 tablets | Valid |
| 158042 | N Clomi 25mg Tablet | Strip of 5 tablets | Valid |
| 161875 | Ova Plus 100mg Tablet | Strip of 10 tablets | Valid |
| 162576 | Oviduct NC Tablet | Strip of 30 tablets | Valid |
| 166622 | Ovafree 50mg Soft Gelatin Capsule | Strip of 5 soft gelatin capsules | Valid |
| 181723 | Primeova 100mg Capsule | Strip of 5 capsules | Valid |
| 205764 | Smartova Pure 50 Capsule | Strip of 5 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All products are oral forms (tablets, capsules and soft gelatin capsules).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or publications, and no plausible mechanistic link to acute intermittent porphyria has been established. The approved indication and mechanism of action are also missing from the compiled data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source, which are required before any safety screening
- Mechanism of action data and the approved indication from DrugBank or the package insert
- A mechanistic and preclinical rationale linking selective estrogen receptor modulation to heme biosynthesis or porphyria attacks
- A literature and trial search to confirm that no relevant studies exist
- A route-of-administration and formulation compatibility assessment for the target disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

