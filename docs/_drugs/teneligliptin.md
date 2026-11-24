---
layout: default
title: Teneligliptin
parent: Model Prediction Only (L5)
nav_order: 816
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Teneligliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Teneligliptin"
predicted_indications: ["opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Teneligliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Teneligliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Teneligliptin is a DPP-4 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on computation only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of teneligliptin as: Dipeptidyl peptidase IV inhibitor ([ChEMBL CHEMBL2147777 (teneligliptin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2147777), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, teneligliptin targets dipeptidyl peptidase 4 (DPP4) and also acts on the related enzymes DPP8 and DPP9. Its efficacy in type 2 diabetes is established, and it is approved for that use in Japan and South Korea.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 (SHIP2) mutations, which affect PI3K/AKT signaling and endochondral ossification. No direct mechanistic link between DPP-4 inhibition and this pathway has been established. The high TxGNN score (0.994) is a computational association only, and the missing mechanism-of-action data further limits mechanistic reasoning.

Other predictions for this drug follow a similar pattern. They include thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome and several localized lipodystrophies (drug-induced, centrifugal, pressure-induced and idiopathic). Most appear to be driven by links to diabetes, such as comorbidity or insulin injection context, rather than by evidence of therapeutic benefit. None has any supporting clinical trial or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Teneligliptin is marketed in India as oral single-ingredient tablets. The data compiled for this report show 20 valid registrations and no cancelled ones. The approved indication text is not available for these entries.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 49487 | Coniark 20mg Tablet | Strip of 10 tablets | Valid |
| 73019 | Eliptin 20mg Tablet | Strip of 10 tablets | Valid |
| 99158 | Glimform 20mg Tablet | Strip of 10 tablets | Valid |
| 99180 | Gliptinita 20mg Tablet | Strip of 10 tablets | Valid |
| 124044 | Lariten 20mg Tablet | Strip of 10 tablets | Valid |
| 131987 | Lavitenglip 20mg Tablet | Strip of 10 tablets | Valid |
| 204429 | Supraglip Tablet | Strip of 10 tablets | Valid |
| 215017 | Tendia Tablet | Strip of 15 tablets | Valid |
| 218059 | Tenipack 20mg Tablet | Strip of 10 tablets | Valid |
| 219352 | Tenark 20mg Tablet | Strip of 10 tablets | Valid |
| 219919 | Tenrite Tablet | Strip of 10 tablets | Valid |
| 219927 | T-Gliptin Tablet | Strip of 10 tablets | Valid |
| 220836 | Tenepace Tablet | Strip of 10 tablets | Valid |
| 220907 | Tenlifine 20mg Tablet | Strip of 10 tablets | Valid |
| 221924 | Teniglip 20mg Tablet | Strip of 10 tablets | Valid |
| 222223 | Tenevir Tablet | Strip of 10 tablets | Valid |
| 222504 | Tenecare 20mg Tablet | Strip of 10 tablets | Valid |
| 225293 | Tenebliz 20mg Tablet | Strip of 10 tablets | Valid |
| 228261 | Tenreen 20mg Tablet | Strip of 10 tablets | Valid |
| 246699 | Zita-Pio Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: No drug-drug interactions are recorded. The three entries retrieved are pharmacological targets of teneligliptin (DPP4, DPP8 and DPP9), not interacting drugs.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link between DPP-4 inhibition and opsismodysplasia (Evidence Level L5). The same is true for all other predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, to support mechanistic analysis
- Package insert warnings and contraindications from the India regulatory source, which are needed for safety screening
- Preclinical or mechanistic studies testing whether DPP-4 inhibition affects INPPL1/SHIP2-related PI3K/AKT signaling or endochondral ossification
- Assessment of route compatibility and similarity to the original indication, both still pending

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL2147777 (teneligliptin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2147777) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

