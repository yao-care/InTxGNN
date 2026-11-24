---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 1
monitor_inn: "Diphenhydramine"
predicted_indications: ["rosacea conjunctivitis"]
last_modified_at: 2026-11-24
description: "Diphenhydramine: predicted new indication rosacea conjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Diphenhydramine
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

## Diphenhydramine: First-generation H1 histamine receptor antagonist → rosacea conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine, marketed in India in oral capsule, tablet and syrup forms.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for diphenhydramine: "Diphenhydramine hydrochloride is an antihistamine with anticholinergic (drying) and sedative side effects. Antihistamines appear to compete with histamine for cell receptor sites on effector cells. Diphenhydramine hydrochloride in the injectable form has a rapid onset of action." ([DailyMed: diphenhydramine hydrochloride prescribing information, Henry Schein, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af972e71-62ab-40c6-925a-cbcb4d6720a4), label version 2026-10-28; accessed 2026-11-19.) Based on well-established pharmacology, diphenhydramine blocks H1 histamine receptors and also has mild anticholinergic and local anesthetic effects. In theory this could ease ocular itching and redness.

The link to rosacea conjunctivitis is weak. Rosacea-related eye disease is driven mainly by meibomian gland dysfunction, an unstable tear film, Demodex and bacterial colonization, and neurovascular and innate-immune dysregulation (for example MMPs, IL-1 and TNF). Histamine plays a minor or unproven role in these processes.

The high score (0.9920) most likely reflects the drug's similarity to other conjunctivitis-related uses rather than disease-specific mechanistic evidence. It should be read as a model-ranking signal, not as proof of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 valid single-ingredient licences are recorded, and the list may be partial. None carries approved-indication text in the local data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3090 | Aldryl Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 6446 | A-Rex Syrup | Bottle of 100 ml Syrup | Valid |
| 21615 | Aden-Rex Syrup | Bottle of 100 ml Syrup | Valid |
| 28446 | Bedryl 75mg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 28971 | Benacof 25mg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 78957 | Exylin 125mg Tablet DT | Strip of 10 tablet dt | Valid |
| 115754 | Kuffdryl 25mg Tablet | Strip of 10 tablets | Valid |
| 115882 | Kuffdryl D 25mg Capsule | Strip of 10 capsules | Valid |
| 117573 | Koycal Syrup | Bottle of 100 ml Syrup | Valid |
| 118730 | Kufma CR Syrup | Bottle of 100 ml Syrup | Valid |
| 135486 | Monodryl Syrup | Bottle of 100 ml Syrup | Valid |
| 145847 | Matdryl Syrup | Bottle of 100 ml Syrup | Valid |
| 154621 | Novadryl 25mg Capsule | Strip of 10 capsules | Valid |
| 170101 | Omituss Syrup Delicious Strawberry | Bottle of 100 ml Syrup | Valid |
| 205494 | StayHappi Diphenhydramine+Ammonium Chloride+Sodium Citrate 14.08mg/138mg/57.03m… | Bottle of 100 ml Syrup | Valid |
| 208098 | StayHappi Diphenhydramine 25mg Capsule | Strip of 10 capsules | Valid |
| 224642 | Toslin Expectorant | Bottle of 50 ml Expectorant | Valid |
| 241514 | Weldryl Syrup | Bottle of 100 ml Syrup | Valid |
| 241953 | Windryl Syrup | Bottle of 100 ml Syrup | Valid |
| 247305 | Zendryl 25mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: The interaction database lists 394 interacting drugs. Examples of the two **Major** interactions:
- Potassium citrate
- Eliglustat

Many **Moderate** interactions are also listed, mostly with other anticholinergic or central nervous system–acting drugs, including hyoscyamine, atropine, glycopyrronium, dicyclomine, loperamide, morphine, bupropion, metoclopramide and dronabinol.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trial or publication addresses rosacea conjunctivitis, and its main disease mechanisms are only loosely related to histamine blockade. Evidence level is L5.

**To proceed, the following is needed:**
- Literature and trial searches specific to rosacea-associated ocular disease and antihistamine use
- Preclinical or mechanistic data on histamine's role in rosacea conjunctivitis
- Assessment of whether an ocular formulation or route is feasible, since the marketed forms are oral
- Package insert warnings and contraindications, plus a safety review for the ocular setting and for people taking interacting drugs

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: diphenhydramine hydrochloride prescribing information, Henry Schein, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af972e71-62ab-40c6-925a-cbcb4d6720a4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

