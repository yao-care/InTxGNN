---
layout: default
title: Polyethylene Glycol
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Polyethylene Glycol: predicted new indication Congenital ichthyosiform erythroderma (evidence level L5). Approved use: Constipation disorder, dry eye syndrome, xerophthalmia"
monitor_inn: "Polyethylene glycol"
predicted_indications: ["congenital ichthyosiform erythroderma"]
---

# Polyethylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Polyethylene glycol: From Constipation and Dry Eye to Congenital Ichthyosiform Erythroderma
{: .text-alpha }

## One-Sentence Summary

Polyethylene glycol is an osmotic agent used as a laxative for constipation and as a lubricant in dry eye products.
The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder, dry eye syndrome, xerophthalmia (the India license records contain no approved indication text) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, polyethylene glycol is an osmotic agent and a hydrating or lubricating ingredient. Its efficacy in constipation (as an osmotic laxative) and in dry eye (as a lubricant) is established, and it may mechanistically be applicable to dry, scaly skin conditions.

The only rationale available is speculative. Because polyethylene glycol attracts and holds water, it could help hydrate a dry, scaly stratum corneum, as seen in congenital ichthyosiform erythroderma. This is a hypothesis, not a demonstrated link.

Ichthyosis is a genetic keratinization disorder (for example, TGM1 and ALOX12B/ALOXE3 variants) with a defective skin barrier. Moisturizing the skin eases symptoms but does not modify the disease. The high TxGNN score is a model-based prediction, and the data compiled for this report contain no clinical or literature support for it. The prediction's similarity to the original indications and its route compatibility have not been assessed. All registered products are oral, other (powder/liquid), or ophthalmic, and none is a dermatological product.

## India Market Information

All 20 registrations are valid products. The license records contain no approved indication text.

<!-- review:begin in-lic-20261124-polyethylene_glycol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-polyethylene_glycol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34887 | Cellwet Eye Drop | Packet of 10 ml Eye Drop | Valid |
| 35230 | CCS Ultra Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 39940 | C-Well Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 50992 | Curemoist Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 51015 | Comc Ultra Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 60232 | Devomoist Eye Drop | Packet of 10 ml Eye Drop | Valid |
| 75925 | Eyeaqua Ultra Eye Drop | Bottle of 10 ml Ophthalmic Solution | Valid |
| 109375 | Imoist-Ultra Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 113911 | Junior Cipeg Powder for Oral Solution | Bottle of 121.1 gm Powder for Oral Solution | Valid |
| 120935 | Laxolite Oral Laxative Liquid Sugar Free | Bottle of 200 ml Liquid | Valid |
| 121044 | Looz Peg Oral Solution Orange | Bottle of 200 ml Oral Solution | Valid |
| 121797 | Laxolite 10gm Oral Laxative Liquid Sugar Free | Bottle of 100 ml Liquid | Valid |
| 139403 | Medmoist Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 175323 | Pegsure Sachet Orange | Sachet of 17 gm Powder | Valid |
| 175828 | Popro Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 177324 | PG Wet Eye Drop | Bottle of 10 ml Ophthalmic Solution | Valid |
| 201028 | Syslube Eye Drop | Bottle of 10 ml Ophthalmic Solution | Valid |
| 201412 | Scilax Powder Strawberry | Sachet of 23 gm Powder | Valid |
| 203824 | Sherwyn Ultra Eye Drop | Bottle of 10 ml Eye Drop | Valid |
| 230442 | Ultralife Eye Drop | Bottle of 10 ml Ophthalmic Solution | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The registrations held in the data are mostly eye drops in 10 ml presentations, plus oral laxative powders and solutions.

<!-- review:begin in-lic-20261124b-polyethylene_glycol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The other 15 registrations include one further laxative powder (Scilax) and 14 additional eye drops, all in 10 ml presentations." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-polyethylene_glycol-1 -->

## Safety Considerations

**Contraindications (from drug-disease associations in the knowledge graph, not from label text):**
The following conditions are linked to polyethylene glycol as contraindications in the knowledge graph:
- **Gastrointestinal:** ileus, paralytic ileus, intestinal obstruction, toxic megacolon, pyloric stenosis, familial visceral myopathy, appendicitis
- **Cardiovascular:** hypertension, hypertensive disorder, congestive heart failure, cardiovascular disease, heart disease
- **Renal and metabolic:** kidney disease, anuria, pyoureter, nephrocalcinosis, hypercalcemia, phosphorus metabolism disease, potassium deficiency disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis
- **Endocrine:** hyperthyroidism, Graves disease, thyrotoxicosis
- **Neurological:** epilepsy
- **Ocular:** angle-closure (closed-angle) glaucoma, eye infectious disease, conjunctivitis

These associations come from a model knowledge graph and may reflect other products or components. They should be verified against the official package insert.

No drug interaction records were found. Please refer to the package insert for warnings and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials or publications, the mechanistic link is speculative, and the benefit would at most be symptomatic moisturization of a genetic barrier disorder. No registered product has a dermatological route.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for polyethylene glycol or PEG-based topical products in ichthyosis
- An assessment of route compatibility (a topical formulation would be needed) and similarity to the original indications
- Preclinical or small exploratory data showing a benefit beyond ordinary emollients

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Revised: wording about the earlier partial table and hard-coded counts | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

