---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 257
evidence_level: L5
indication_count: 5
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
last_modified_at: 2026-11-24
description: "Dextromethorphan: predicted new indication nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dextromethorphan: Sigma-1 agonist and NMDA antagonist antitussive → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Dextromethorphan is a centrally acting antitussive (cough suppressant) that acts as a sigma-1 agonist and NMDA receptor antagonist.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials and no publications** were found to support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dextromethorphan hydrobromide, bupropion hydrochloride (a combination product containing dextromethorphan): "Dextromethorphan is an uncompetitive antagonist of the NMDA receptor (an ionotropic glutamate receptor) and a sigma-1 receptor agonist. The mechanism of dextromethorphan in the treatment of MDD and agitation associated with dementia due to Alzheimer’s disease is unclear." ([DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79), label version 2026-08-17; accessed 2026-11-19.) Dextromethorphan is generally understood as a centrally acting cough suppressant working through sigma-1 agonism and NMDA receptor antagonism. It has no established direct effect on the nasal mucosa.

The prediction most likely reflects closeness to upper respiratory conditions that dextromethorphan is associated with, such as rhinitis and nasopharyngitis. "Nasal cavity disease" is a broad category that overlaps with these terms. The link appears to come from shared parent terms in the model rather than from a distinct pharmacological mechanism. Any benefit would at most be symptomatic (for example cough relief), not treatment of the nasal disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26256 | Bro Cofdex Plus Syrup | Bottle of 100 ml Syrup | Valid |
| 40361 | Corituss Syrup | Bottle of 100 ml Syrup | Valid |
| 46599 | Cozia Tablet | Strip of 10 tablets | Valid |
| 58356 | DMR 30mg Tablet | Strip of 10 tablets | Valid |
| 59260 | Deroxy P Syrup | Bottle of 100 ml Syrup | Valid |
| 59937 | DMR 10mg Tablet | Strip of 10 tablets | Valid |
| 63178 | Dexpro Syrup | Bottle of 100 ml Syrup | Valid |
| 65055 | Dezex 5mg Tablet | Strip of 10 tablets | Valid |
| 73684 | Endkuf SF Syrup | Bottle of 100 ml Syrup | Valid |
| 94831 | Glycodin Syrup | Bottle of 100 ml Syrup | Valid |
| 116047 | Kofrid D Syrup | Bottle of 100 ml Syrup | Valid |
| 146035 | Medkuff 15mg/5mg Tablet | Strip of 10 tablets | Valid |
| 156721 | Novamine P Syrup | Bottle of 60 ml Syrup | Valid |
| 200456 | Sudin D Syrup | Bottle of 100 ml Syrup | Valid |
| 203717 | Stopper SF Syrup | Bottle of 100 ml Syrup | Valid |
| 219856 | Terp D Syrup | Bottle of 100 ml Syrup | Valid |
| 225580 | Tixy Soft 10 mg/100 mg Capsule | Strip of 4 capsules | Valid |
| 225601 | Trigenic-CS Syrup | Bottle of 60 ml Syrup | Valid |
| 244962 | Xing Cuf Syrup | Bottle of 100 ml Syrup | Valid |
| 252722 | Zealtus Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 306 interactions are recorded. Major-level interactions include dexfenfluramine, dolasetron, fenfluramine, granisetron, lorcaserin, ondansetron, palonosetron and sibutramine (mainly serotonergic agents). Moderate-level interactions include bupropion, morphine, cimetidine, dronabinol, eliglustat, metoclopramide, opium and phentermine.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9998) but no supporting clinical trials or publications, and no plausible direct mechanism on nasal tissue. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data to assess biological plausibility
- A targeted literature review for dextromethorphan in nasal and upper airway disease
- Package insert warnings and contraindications for the Indian products
- A review of the major serotonergic and CYP2D6-related interactions before any new-use consideration

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

