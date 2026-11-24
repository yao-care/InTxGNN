---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Risperidone"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania"]
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). In India: at least 20 listed products"
---

# Risperidone
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

## Risperidone: Gaze palsy, familial horizontal, with progressive scoliosis
{: .text-alpha }

## One-Sentence Summary

Risperidone is an atypical antipsychotic marketed in India as oral tablets.
The TxGNN model predicts it may be effective for **gaze palsy, familial horizontal, with progressive scoliosis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for risperidone: "The mechanism of action of risperidone in schizophrenia is unclear. The drug's therapeutic activity in schizophrenia could be mediated through a combination of dopamine Type 2 (D 2 ) and serotonin Type 2 (5HT 2 ) receptor antagonism." ([DailyMed: Risperdal (risperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e117c7e-02fc-4343-92a1-230061dfc5e0), label version 2026-10-23; accessed 2026-11-19.) Risperidone is generally understood to act through dopamine D2 and serotonin 5-HT2A receptor antagonism.

The predicted disease is a rare inherited disorder of horizontal eye movement with progressive scoliosis, linked to the ROBO3 gene. It has no plausible dopaminergic or serotonergic target that risperidone would act on, and no mechanistic link has been established. The high score is therefore best treated as a statistical output of the model rather than a biologically grounded signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Risperidone is currently marketed in India. All 20 records in the compiled data are valid licences, and the list may be partial. The licence records carry no indication text.

<!-- review:begin in-lic-20261124-risperidone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 records in the compiled data are valid single-ingredient licences, and the list may be partial." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-risperidone-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 80656 | Eauris 3mg Tablet | Strip of 10 tablets | Valid |
| 182102 | Psydon 4mg Tablet | Strip of 10 tablets | Valid |
| 184310 | Risdone-Plus Tablet | Strip of 10 tablets | Valid |
| 185469 | Risnia MD 4 Tablet | Strip of 10 tablet md | Valid |
| 185725 | Restek H 2 mg/2 mg Tablet | Strip of 10 tablets | Valid |
| 186077 | Respidon 3 Tablet | Strip of 10 tablets | Valid |
| 187022 | Rize 2mg Tablet | Strip of 10 tablets | Valid |
| 187430 | Riswave Plus Tablet MD | Strip of 10 tablet md | Valid |
| 188192 | Rasin Forte 4mg/2mg Tablet | Strip of 10 tablets | Valid |
| 189472 | Repadone 4mg Tablet | Strip of 10 tablets | Valid |
| 189531 | Restonorm 1mg Tablet | Strip of 15 tablets | Valid |
| 194815 | Rion 4mg Tablet | Strip of 10 tablets | Valid |
| 195547 | Repadone 3mg Tablet | Strip of 10 tablets | Valid |
| 195578 | Respijet 1mg Tablet | Strip of 10 tablets | Valid |
| 196349 | Risbris 2 Tablet | Strip of 10 tablets | Valid |
| 198284 | Ripsy 2mg Tablet | Strip of 10 tablets | Valid |
| 211982 | StayHappi Risperidone 3mg Tablet | Strip of 10 tablets | Valid |
| 248965 | Zisper Forte 4 mg/2 mg Tablet MD | Strip of 10 tablet md | Valid |
| 249775 | Zisper 2mg Tablet MD | Strip of 10 tablet md | Valid |
| 251845 | Zepid Plus 3 mg/2 mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 362 interactions are recorded. Major-level interactions include **bupropion** and **morphine**. Many moderate-level interactions are also listed, including acarbose, metformin, famotidine, epinephrine, hydrocortisone, amphotericin B, atropine and loperamide.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no publications and no plausible mechanistic link. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Any biological rationale linking risperidone's receptor pharmacology to ROBO3-related horizontal gaze palsy
- Mechanism of action data and package insert safety information
- Preclinical or clinical studies directly addressing this disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Risperdal (risperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e117c7e-02fc-4343-92a1-230061dfc5e0) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

