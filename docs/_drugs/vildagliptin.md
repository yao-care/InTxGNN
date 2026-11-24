---
layout: default
title: Vildagliptin
parent: Model Prediction Only (L5)
nav_order: 889
evidence_level: L5
indication_count: 9
monitor_inn: "Vildagliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-24
description: "Vildagliptin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Vildagliptin
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

## Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Vildagliptin is an oral DPP-4 inhibitor used to manage type 2 diabetes mellitus.
The TxGNN model (deep learning) predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly studying this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of vildagliptin as: Dipeptidyl peptidase IV inhibitor ([ChEMBL CHEMBL142703 (vildagliptin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL142703), CC BY-SA 3.0; accessed 2026-11-19.) Vildagliptin is known as a selective inhibitor of dipeptidyl peptidase-4 (DPP-4), which raises active incretin hormones (GLP-1, GIP) and enhances glucose-dependent insulin secretion. Pharmacology records also list DPP-4, DPP-8, DPP-9 and TRPV4 as targets.

The link to stiff person syndrome is weak. Stiff person syndrome is an autoimmune neurological disorder involving anti-GAD65 antibodies and impaired GABAergic signalling. DPP-4 inhibition might theoretically modulate immune or incretin pathways, but no supporting data exist. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the overlap of anti-GAD autoimmunity with autoimmune diabetes, not biological evidence or a true therapeutic effect.

The same applies to other top-ranked predictions (focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and several lipodystrophy conditions). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; they have no trial or literature support. Pancreatic agenesis (rank 9) is biologically implausible, since there is no functional pancreatic tissue for the drug to act on.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

(For reference, the only publications retrieved in the compiled data relate to a lower-ranked prediction, pancreatic agenesis, and none supports a benefit: two general reviews of DPP-4 inhibitors in type 2 diabetes, one animal study of a different drug, and one case report of probable vildagliptin-associated acute pancreatitis.)

## India Market Information

At least 20 valid single-ingredient licences are recorded (the list may be partial). The licence records contain no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 60979 | Debiglip 100 SR Tablet | Strip of 15 tablet sr | Valid |
| 78373 | Euvilda 50mg Tablet | Strip of 10 tablets | Valid |
| 163646 | O Vildalog 100 Tablet SR | Strip of 10 tablet sr | Valid |
| 167372 | Oldglip 50mg Tablet | Strip of 10 tablets | Valid |
| 233613 | Vilnip Tablet | Strip of 15 tablets | Valid |
| 233738 | Vidaglo Tablet | Strip of 10 tablets | Valid |
| 233750 | Vildanex 50mg Tablet | Strip of 15 tablets | Valid |
| 233805 | Vildazem 50mg Tablet | Strip of 10 tablets | Valid |
| 233910 | Vil-G Tablet | Strip of 15 tablets | Valid |
| 234048 | Vildanex 100mg Tablet SR | Strip of 10 tablet sr | Valid |
| 234186 | Vicemic Tablet | Strip of 15 tablets | Valid |
| 234217 | Vildaprime 50mg Tablet | Strip of 15 tablets | Valid |
| 235163 | Vildalor 50mg Tablet | Strip of 10 tablets | Valid |
| 235359 | Vildact 50mg Tablet | Strip of 15 tablets | Valid |
| 236338 | Vildapure 50mg Tablet | Strip of 10 tablets | Valid |
| 236907 | Venna 100mg Tablet SR | Strip of 10 tablet sr | Valid |
| 237335 | Vild Well 50mg Tablet | Strip of 15 tablets | Valid |
| 238614 | Vildamence 50mg Tablet | Strip of 15 tablets | Valid |
| 239661 | Vildock 50mg Tablet | Strip of 15 tablets | Valid |
| 250300 | Ziglip 50 Tablet | Strip of 15 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Pharmacology records list interactions at the target level (DPP-4, DPP-8, DPP-9, TRPV4), with no graded drug-drug interactions.
- **Related literature signal**: A 2026 case report describes probable vildagliptin-associated acute pancreatitis in a patient with type 2 diabetes. The link between DPP-4 inhibitors and pancreatitis remains controversial.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. No clinical trials or publications address classic stiff person syndrome, and no mechanistic link is supported, so the evidence level is L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the licence holders
- Preclinical or mechanistic studies testing DPP-4 inhibition in stiff person syndrome models or anti-GAD65 autoimmunity
- Review of whether the TxGNN model (deep learning) score simply reflects similarities the model learned between related diseases, such as anti-GAD overlap with autoimmune diabetes

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL142703 (vildagliptin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL142703) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

