---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 1
monitor_inn: "Ammonium chloride"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-24
description: "Ammonium Chloride: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
---

# Ammonium Chloride
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

## Ammonium Chloride: From Pharyngitis and Common Cold to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Ammonium chloride is a long-established ingredient in cough and cold preparations, with recorded uses in the knowledge graph for pharyngitis, common cold and nasopharyngitis.
The TxGNN model predicts it may be useful for **nasal cavity disease**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (relations recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is used in cough and cold syrups, mainly as an expectorant that increases airway secretions. Its recorded uses in upper respiratory conditions (pharyngitis, common cold, nasopharyngitis) are relations from the knowledge graph rather than approved indications.

The upper airway conditions it is linked to sit close to the nasal cavity anatomically and share symptoms such as congestion and mucus. This makes it plausible that the model is picking up on this overlap. However, this is only a hypothesis. "Nasal cavity disease" is also a broad, non-specific category, so it is hard to translate into a defined clinical question. The very high TxGNN score is a computational prediction, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

At least 20 licences are valid. The licence records contain no approved indication text.

<!-- review:begin in-lic-20261124c-ammonium_chloride-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 single-ingredient licences are valid." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-ammonium_chloride-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 7659 | Ambitus Syrup | Bottle of 100 ml Syrup | Valid |
| 12881 | Adyl Expectorant | Bottle of 110 ml Expectorant | Valid |
| 14380 | Azadryl Syrup | Bottle of 100 ml Syrup | Valid |
| 29960 | Becodryl Syrup | Bottle of 60 ml Syrup | Valid |
| 35576 | Cofdex Plus Syrup Sweet Orange | Bottle of 100 ml Syrup | Valid |
| 36696 | Cofrest Syrup | Bottle of 100 ml Syrup | Valid |
| 38677 | Coupress N Syrup | Bottle of 50 ml Syrup | Valid |
| 105768 | Histanil BM Syrup | Bottle of 100 ml Syrup | Valid |
| 105897 | HL Dex Syrup | Bottle of 100 ml Syrup | Valid |
| 106938 | Henadryl Syrup | Bottle of 100 ml Syrup | Valid |
| 117683 | Kospin Syrup | Bottle of 100 ml Syrup | Valid |
| 152200 | Nocof Syrup | Bottle of 100 ml Syrup | Valid |
| 186868 | Resporex Syrup | Bottle of 60 ml Syrup | Valid |
| 193386 | Redax Syrup | Bottle of 100 ml Syrup | Valid |
| 194726 | Respigil DM Syrup | Bottle of 100 ml Syrup | Valid |
| 207868 | Seekof Syrup | Bottle of 100 ml Syrup | Valid |
| 210394 | Sardex Syrup | Bottle of 100 ml Syrup | Valid |
| 212407 | Sonidril DMR Syrup | Bottle of 100 ml Syrup | Valid |
| 241241 | Vizcof-Lite Syrup | Bottle of 100 ml Syrup | Valid |
| 249589 | Zumcof DX Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications (relations recorded in the knowledge graph, not label text):** hypertension and hypertensive disorder, liver failure, impaired renal function, anuria, epilepsy, adrenocortical insufficiency and Addison disease, peptic ulcer disease, hyperthyroidism (Graves disease, thyrotoxicosis), angle-closure glaucoma, ocular hypertension, benign prostatic hyperplasia, bladder neck obstruction, pulmonary edema, myocardial ischemia and coronary artery disease, sudden cardiac arrest, heart conduction disease, anxiety disorder, obsessive-compulsive disorder, insomnia, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, necrotizing enterocolitis, and others.
- **Drug Interactions:** 21 interactions are recorded.
  - Moderate: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine.
  - Minor: ephedrine, pseudoephedrine, tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin, imipramine, nortriptyline, protriptyline, trimipramine), methadone, mexiletine, flecainide.

Package insert warnings were not available; please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a computational score. No trials or publications study nasal cavity disease directly, and the mechanism of action is unavailable, so the evidence level is L5. The condition is also too broad to define a clear clinical question.

**To proceed, the following is needed:**
- Mechanism of action data for ammonium chloride
- Package insert warnings and contraindications from the Indian licences
- A specific nasal condition (for example, rhinitis or nasal congestion) in place of the broad category, with a targeted literature and trial search
- Review of the 21 recorded drug interactions and the knowledge-graph contraindications
- Assessment of route and formulation compatibility; all current products are oral syrups or expectorants

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

