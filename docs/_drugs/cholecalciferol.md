---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 4
monitor_inn: "Cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-11-24
description: "Cholecalciferol: predicted new indication Acromesomelic dysplasia, Campailla Martinelli type (evidence level L5). Approved use: Vitamin D deficiency and bone-mineral disorders (osteoporosis…"
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cholecalciferol: From Vitamin D Deficiency and Bone Disorders to Acromesomelic dysplasia, Campailla Martinelli type
{: .text-alpha }

## One-Sentence Summary

Cholecalciferol (vitamin D3) is a nutritional vitamin D form used for vitamin D deficiency and bone-mineral disorders such as rickets, osteomalacia and osteoporosis. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Campailla-Martinelli type**, an ultra-rare genetic skeletal disorder. This prediction currently has **no supporting clinical trials and no publications**, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency and bone-mineral disorders (osteoporosis, rickets, osteomalacia, hypoparathyroidism). These are relations recorded in the knowledge graph. The local licence records contain no approved-indication text. |
| Predicted New Indication | Acromesomelic dysplasia, Campailla-Martinelli type |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of cholecalciferol as: Vitamin D receptor agonist ([ChEMBL CHEMBL1042 (cholecalciferol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1042), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, cholecalciferol is a pro-hormone that is converted in the liver and kidney to active vitamin D metabolites. These metabolites support calcium and phosphate absorption and bone mineralization. Its use in vitamin D deficiency and bone-mineral disorders is the basis for the model's link to a skeletal disease.

The link to this new indication is weak. Acromesomelic dysplasia, Campailla Martinelli type is an ultra-rare skeletal dysplasia of genetic origin. Vitamin D's general role in bone mineralization is only a loose, nonspecific connection. It does not address the underlying genetic defect, and no specific mechanistic pathway has been established. The very high score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical confirmation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

All 20 listed licences are valid single-ingredient products. Approved-indication text is not stated in the licence records.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 2784 | Aquashine 24 Tablet | Strip of 7 tablets | Valid |
| 5934 | Astesol-D3 60K Chewable Tablet | Strip of 4 Chewable Tablets | Valid |
| 31304 | Borncal D3 Nano Shot (5ml Each) Mango Sugar Free | Box of 4 bottles | Valid |
| 38874 | Cholvac-D3 Softgel Capsule | Strip of 4 soft gelatin capsules | Valid |
| 94298 | Gemsoline-D3 Nano Shot | Bottle of 5 ml Oral Solution | Valid |
| 114570 | Jaivita D3 60K Softgel Capsule | Strip of 4 soft gelatin capsules | Valid |
| 115844 | Kalzin 60K Tablet | Strip of 4 tablets | Valid |
| 134866 | Max-D3 60K Soft Gelatin Capsule | Strip of 8 soft gelatin capsules | Valid |
| 135485 | M 60K Nano Shot Sugar Free | Bottle of 5 ml Oral Solution | Valid |
| 152202 | Nexa-D3 60K Soft Gelatin Capsule | Strip of 4 soft gelatin capsules | Valid |
| 152338 | Nucical D3 Soft Gelatin Capsule | Strip of 4 soft gelatin capsules | Valid |
| 162844 | Optume-D3 60K Softgel Capsule | Strip of 4 soft gelatin capsules | Valid |
| 189174 | Resorce D3 Softgel Capsule | Strip of 8 soft gelatin capsules | Valid |
| 201377 | S-Rise D3 60K Soft Gelatin Capsule | Strip of 4 soft gelatin capsules | Valid |
| 217773 | Tonecal-D3 Softgel Capsule | Strip of 4 soft gelatin capsules | Valid |
| 223864 | Tnt D3 Injection | Vial of 1 ml Injection | Valid |
| 242252 | Werol 600000IU Injection | Vial of 1 ml Injection | Valid |
| 247052 | Zyrol-D3 Nano Shots (Each 5ml) Orange Sugar Free | Box of 4 oral solutions | Valid |
| 247988 | Zymanta D3 Soft Gelatin Capsule | Strip of 4 soft gelatin capsules | Valid |
| 250128 | Zemcy 60K Softgel Capsule | Strip of 4 soft gelatin capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include oral capsules, tablets, chewable tablets, oral solutions and injections.

## Safety Considerations

- **Drug Interactions**: 56 interactions are recorded. The major ones are with other vitamin D-active compounds: calcifediol, calcitriol, dihydrotachysterol and doxercalciferol. Moderate interactions include thiazide diuretics (for example chlorothiazide, chlorthalidone), barbiturates (amobarbital, butabarbital, butalbital), carbamazepine, digoxin and digitoxin, and bile acid sequestrants (cholestyramine, colestipol, colesevelam).
- **Conditions flagged in the knowledge graph** (relations recorded in the knowledge graph, not label text): hypercalcemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, primary hyperoxaluria, and several others. Hypercalcemia and nephrocalcinosis risk is the main practical concern with high-dose use.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials or publications for this disease. Cholecalciferol's nonspecific bone-mineral role does not address the genetic cause of this skeletal dysplasia.

**To proceed, the following is needed:**
- Any disease-specific evidence, such as case series, preclinical work or mechanistic studies, linking vitamin D pathways to this dysplasia
- Mechanism of action data for cholecalciferol
- Package insert warnings and contraindications from Indian labelling
- A review of other predicted indications for the drug. For example, renal osteodystrophy has two related trials and several publications, though its evidence is indirect and overlaps with existing uses.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1042 (cholecalciferol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1042) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

