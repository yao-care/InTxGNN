---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pegfilgrastim: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not stated in the available licence records"
monitor_inn: "Pegfilgrastim"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastim: From an Unspecified Original Indication to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegfilgrastim is a PEGylated recombinant G-CSF analogue marketed in India in 13 single-ingredient injectable products. The licence records compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy** (and the broader term **diabetic retinopathy**), but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence records |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (13 of 13) – CDSCO approval status is not included in this data |
| Number of Listed Products | 13 (valid: 13) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pegfilgrastim: "Pegfilgrastim products are colony-stimulating factor that acts on hematopoietic cells by binding to specific cell surface receptors, thereby stimulating proliferation, differentiation, commitment, and end cell functional activation." ([DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83), label version 2026-10-29; accessed 2026-11-19.) Based on known information, pegfilgrastim is a long-acting PEGylated form of granulocyte colony-stimulating factor (G-CSF). It stimulates the growth and mobilisation of neutrophils and haematopoietic progenitor cells. Its mechanistic relationship to diabetic retinopathy has not been established.

Two speculative links can be drawn. First, dysfunction of bone marrow-derived progenitor cells is thought to impair vascular repair in diabetes, and G-CSF might influence this process. Second, neutrophil-mediated inflammation contributes to retinal vascular damage. The second point cuts the other way: G-CSF-induced neutrophilia could worsen retinal inflammation and vascular injury. The direction of effect is therefore unclear.

The two predicted indications (severe nonproliferative diabetic retinopathy and its parent term, diabetic retinopathy) overlap, so they are not independent pieces of evidence. No clinical or preclinical data were available to confirm or refute a therapeutic effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

All 13 licences are valid single-ingredient injectable products. The licence records do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4914 | Adfil 6mg Injection | Prefilled syringe of 0.6 ml Injection | Valid |
| 85747 | Fillif Peg 6mg Injection | Prefilled syringe of 1 Injection | Valid |
| 87425 | Filcad P Injection | Prefilled syringe of 0.6 ml Injection | Valid |
| 109351 | Imupeg 6mg Injection | Vial of 0.6 ml Injection | Valid |
| 123254 | Lupifil P 6mg Injection | Prefilled syringe of 1 ml Injection | Valid |
| 151911 | Neupeg 6mg Injection | Vial of 1 Injection | Valid |
| 173920 | Pegasta Injection | Prefilled syringe of 0.6 ml Injection | Valid |
| 173956 | Pegstim Injection | Prefilled syringe of 0.6 ml Injection | Valid |
| 174423 | Pegex 6mg Injection | Prefilled syringe of 0.6 ml Injection | Valid |
| 174482 | Peg-ReliGrast Injection | Prefilled syringe of 1 Injection | Valid |
| 178035 | Pegheal 6mg Injection | Prefilled syringe of 1 ml Injection | Valid |
| 178417 | Peg Xphil 6mg Injection | Prefilled syringe of 1 Injection | Valid |
| 206706 | Sfil Peg 6mg Injection | Prefilled syringe of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Cytotoxicity

Pegfilgrastim is a supportive-care growth factor, not an antineoplastic drug, so a cytotoxicity assessment does not apply.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening identified 147 potential interacting drugs. The 20 entries retrieved were all rated **Moderate**. They include:
  - Cytotoxic and antineoplastic agents such as paclitaxel, mercaptopurine, azacitidine, arsenic trioxide, trimetrexate, altretamine and asparaginase
  - Targeted agents such as abemaciclib, acalabrutinib and avapritinib
  - Immunotherapies and biologics such as aldesleukin, alemtuzumab and belantamab mafodotin
  - Radiopharmaceuticals and radioimmunotherapy agents such as iobenguane (I-131), tositumomab, ibritumomab tiuxetan and fludeoxyglucose (18F)
  - Others, including levamisole and pegvaliase

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies entirely on a high model score (0.9989). There are no clinical trials, no literature, and no mechanism of action data. The biological direction of effect is also uncertain, because G-CSF-driven neutrophilia could aggravate retinal inflammation.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products, which are required before safety screening can start
- Confirmed mechanism of action data and the approved indications for the marketed products
- Preclinical or mechanistic evidence on G-CSF effects in the diabetic retina, including whether the effect is beneficial or harmful
- A literature and trial search specific to G-CSF or pegfilgrastim and diabetic retinopathy
- An assessment of whether the injectable route and dosing are compatible with a retinal indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

