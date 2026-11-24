---
layout: default
title: Reboxetine
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Reboxetine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Reboxetine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "neurotic disorder", "Keppen-Lubinsky syndrome", "ligneous conjunctivitis"]
---

# Reboxetine
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

## Reboxetine: From Depression to Benign Paroxysmal Torticollis of Infancy
{: .text-alpha }

## One-Sentence Summary

Reboxetine is a selective norepinephrine reuptake inhibitor, originally used to treat depressive disorders (unipolar depression, major depressive disorder) and anxiety disorder.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of reboxetine as: Norepinephrine transporter inhibitor ([ChEMBL CHEMBL14370 (reboxetine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL14370), CC BY-SA 3.0; accessed 2026-11-19.) Pharmacology records show that reboxetine targets the norepinephrine transporter (NET, gene SLC6A2). It is a selective norepinephrine reuptake inhibitor used for depressive illness.

**No mechanistic link to the predicted indication was identified.** Benign paroxysmal torticollis of infancy is a childhood disorder related to the migraine spectrum and is often associated with channelopathy genes such as CACNA1A. Blocking norepinephrine reuptake has no established rationale here.

The very high TxGNN score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical evidence. Use in infants would also raise major safety concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Reboxetine is marketed in India as single-ingredient oral tablets. All 6 of 6 licences are valid. The registrations on file do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 156888 | Narebox 2mg Tablet | Strip of 10 tablets | Valid |
| 157026 | Narebox 4mg Tablet | Strip of 10 tablets | Valid |
| 188715 | Rebotin 2mg Tablet | Strip of 10 tablets | Valid |
| 188716 | Rebotin 4mg Tablet | Strip of 10 tablets | Valid |
| 191560 | Reboxxin 4mg Tablet | Strip of 10 tablets | Valid |
| 192463 | Reboxxin 2mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link. The target population is infants, for whom safety concerns would be substantial. This is a TxGNN model (deep learning) prediction only (L5).

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking norepinephrine reuptake inhibition to the pathophysiology of benign paroxysmal torticollis of infancy
- Any preclinical or clinical evidence in this condition
- The package insert warnings and contraindications, and a paediatric safety assessment
- Detailed mechanism of action data

**Note on other predictions for this drug:**
Other predicted indications have more support than this one. Agoraphobia, dysthymic disorder, melancholia and neurotic depression have literature backing (L1–L3), and melancholia and neurotic depression are largely relabelings of an on-label use. These are better candidates for further evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL14370 (reboxetine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL14370) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

