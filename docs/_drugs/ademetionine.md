---
layout: default
title: Ademetionine
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ademetionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Ademetionine"
predicted_indications: ["acne (disease)", "colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "colonic lymphangioma", "cecum neuroendocrine tumor G1", "cecal disease", "benign neoplasm of cecum", "colon leiomyoma"]
---

# Ademetionine
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

## Ademetionine: From an Unspecified Original Indication to acne (disease)
{: .text-alpha }

## One-Sentence Summary

Ademetionine (S-adenosylmethionine, SAMe) is marketed in India as an oral tablet, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **acne**, with a very high score of **0.9990**.
However, there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 14 of 14) |
| Number of Registrations | 14 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Based on general pharmacological knowledge, ademetionine is a methyl donor involved in transmethylation, transsulfuration and polyamine synthesis, and it supports glutathione production.

A plausible but unvalidated link to acne runs through modulation of inflammation, oxidative stress and sebaceous lipid metabolism. The original indication could not be determined from the registration data, so the relationship between the original and new indications cannot be assessed.

The very high TxGNN score is a computational result only. No trials or publications were found to support it.

Other top-ranked predictions are mostly colonic conditions: colonic neoplasm (0.9937), cecum villous adenoma (0.9917), lipoma of colon (0.9917), rectosigmoid junction neoplasm (0.9917), colonic lymphangioma (0.9917), cecum neuroendocrine tumor G1 (0.9915), cecal disease (0.9914), benign neoplasm of cecum (0.9913) and colon leiomyoma (0.9913). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related colonic diseases, not biological evidence. The one exception with a biologically plausible rationale is colonic neoplasm, where DNA and histone methylation are relevant to colorectal carcinogenesis. Even there, the direction of effect (protective or tumour-promoting) is uncertain.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 216212 | Triosam 400 Tablet | Strip of 10 tablets | Not stated |
| 3638 | Admetral 400mg Tablet | Strip of 10 tablets | Not stated |
| 200560 | S-Methiwave 400 Tablet | Strip of 10 tablets | Not stated |
| 150657 | New Adesam 400 Tablet | Strip of 10 tablets | Not stated |
| 103671 | Heptral 400mg Tablet | Strip of 10 tablets | Not stated |

There are 14 valid single-ingredient registrations in total, all oral tablets (200 mg and 400 mg strengths).

## Safety Considerations

- **Knowledge-graph contraindication signals** (model-derived, not from label text): hypertensive disorder, hypertension, diabetes mellitus, diabetic ketoacidosis, hyperlipidemia, familial hyperlipidemia.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acne (and for every other ranked disease) is supported only by the TxGNN score, with no clinical trials or literature (Evidence Level L5). The original indication and mechanism data are also missing, and the package insert safety data are unavailable.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data for ademetionine
- A literature and trial search for ademetionine/SAMe in acne, and in colonic neoplasia if that direction is pursued
- Review of the knowledge-graph contraindication signals (hypertension, diabetes, hyperlipidemia) against the target population
- Drug interaction data (none were found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

