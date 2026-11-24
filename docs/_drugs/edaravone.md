---
layout: default
title: Edaravone
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Edaravone: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Ischemic stroke, stroke disorder, amyotrophic lateral sclerosis"
monitor_inn: "Edaravone"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis"]
---

# Edaravone
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

## Edaravone: From Ischemic Stroke and ALS to Heparin Cofactor 2 Deficiency
{: .text-alpha }

## One-Sentence Summary

Edaravone is a free radical scavenger originally used to treat ischemic stroke and amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but this rests on a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ischemic stroke, stroke disorder, amyotrophic lateral sclerosis (approved indication text is not available in the India registrations) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for edaravone: "The mechanism by which edaravone injection exert its therapeutic effect in patients with ALS is unknown." ([DailyMed: edaravone prescribing information, Piramal Critical Care Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=19862ae9-d6e1-70e6-e063-6394a90ae749), label version 2025-10-07; accessed 2026-11-19.) Based on known information, edaravone is a free radical scavenger with established use in ischemic stroke and ALS. A speculative link is that it may reduce oxidative endothelial injury, which could in theory lower thrombotic risk in a prothrombotic condition.

This link is weak. Heparin cofactor 2 deficiency is a defect in dermatan sulfate-dependent thrombin inhibition, and a radical scavenger would not correct it. The prediction is therefore hypothetical and unvalidated.

A second prediction, **factor 5 excess with spontaneous thrombosis** (score 0.9906), has the same limitations. Edaravone does not target the coagulation cascade, and no trials or publications support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Edaravone has 20 valid single-ingredient registrations in India and none are cancelled. The registrations include no approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 494 | Aravon Injection | Vial of 20 ml Injection | Valid |
| 53927 | Convaron Injection | Ampoule of 20 ml Injection | Valid |
| 67526 | Dravon 1500mg Injection | Vial of 1 Injection | Valid |
| 72868 | Edastar Injection | Vial of 20 ml Injection | Valid |
| 73931 | Edanox 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 74902 | Edastar 1.5mg Tablet | Strip of 10 tablets | Valid |
| 77525 | Edivone 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 78146 | Edcross 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 78993 | Edasure 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 79377 | Edosat 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 79749 | Ezycut 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 79876 | Evaspey Injection | Ampoule of 20 ml Injection | Valid |
| 80558 | Edax 1.5mg Injection | Ampoule of 20 ml Injection | Valid |
| 80814 | ED 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 81598 | Edavone 1500mg Injection | Vial of 1 Injection | Valid |
| 82552 | Erivon Injection | Ampoule of 20 ml Injection | Valid |
| 88289 | Fesuvor Injection | Ampoule of 20 ml Injection | Valid |
| 88647 | Fraseda 1.5mg Injection | Vial of 20 ml Injection | Valid |
| 154137 | Neurovon 30mg Injection | Ampoule of 1 Injection | Valid |
| 192197 | Ridostro Injection | Ampoule of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Most products are injectables, and one oral tablet is registered.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature. The proposed mechanism does not fit the underlying defect in thrombin inhibition, so there is no basis to advance it.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to the predicted conditions
- Package insert warnings and contraindications for the India-registered products
- Preclinical or mechanistic studies showing edaravone affects thrombin inhibition or coagulation
- Route compatibility assessment and similarity analysis against the original indications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: edaravone prescribing information, Piramal Critical Care Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=19862ae9-d6e1-70e6-e063-6394a90ae749) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

