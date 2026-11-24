---
layout: default
title: Doxylamine
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
monitor_inn: "Doxylamine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-24
description: "Doxylamine: predicted new indication nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Doxylamine
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

## Doxylamine: Antihistamine with anticholinergic activity → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Doxylamine is an antihistamine with anticholinergic properties that is marketed in India as tablets.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but no clinical trials or publications were found in the compiled data to support this direction. The prediction rests on model output alone.

<!-- review:begin in-lic-20261124c-doxylamine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Doxylamine is an antihistamine with anticholinergic properties that is marketed in India as single-ingredient tablets." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-doxylamine-1 -->

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg (a combination product containing doxylamine): "The mechanism of action of doxylamine succinate and pyridoxine hydrochloride is unknown." ([DailyMed: Doxylamine Succinate And Pyridoxine Hydrochloride (doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de265fd1-bc22-4da1-aab5-b5fedd649c8b), label version 2026-08-24; accessed 2026-11-19.) Doxylamine is, however, a first-generation antihistamine. Drugs of this class block H1 histamine receptors and also have anticholinergic effects, which can reduce nasal secretions and congestion.

"Nasal cavity disease" is a broad category that covers many conditions, such as rhinitis and cold-related nasal symptoms. Symptom relief of this kind is plausible for an H1-blocking, anticholinergic drug. Because the term is non-specific, the prediction cannot be tied to one defined disease. No trial or publication directly studies this predicted disease, so the mechanistic link remains a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

At least 20 valid licences are recorded, and the list may be partial. None of them carries approved indication text in the local data.

<!-- review:begin in-lic-20261124c-doxylamine-2 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 valid single-ingredient licences are recorded, and the list may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-doxylamine-2 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 63164 | Doxytuff Tablet | Strip of 10 tablets | Valid |
| 64184 | Doxibert-Plus Tablet | Strip of 10 tablets | Valid |
| 64225 | Doxyfresh F Tablet | Strip of 10 tablets | Valid |
| 67048 | Doxipy Tablet | Strip of 10 tablets | Valid |
| 71001 | Doxixor 10mg/10mg/2.5mg Tablet | Strip of 10 tablets | Valid |
| 71620 | Doxqueen 10mg/10mg/2.5mg Tablet | Strip of 10 tablets | Valid |
| 83669 | Emewin 10mg/10mg Tablet | Strip of 10 tablets | Valid |
| 88908 | Folmine P Tablet | Strip of 10 tablets | Valid |
| 96198 | Gud M Tablet | Strip of 10 tablets | Valid |
| 98621 | Gravidox 10 mg/10 mg Tablet | Strip of 10 tablets | Valid |
| 118454 | Kan-Fresh Tablet | Strip of 10 tablets | Valid |
| 145517 | Mosick 10mg/10mg Tablet | Strip of 10 tablets | Valid |
| 151388 | NV Tablet | Strip of 30 tablets | Valid |
| 152298 | Nomosic Tablet | Strip of 10 tablets | Valid |
| 155903 | Nms D Tablet | Strip of 10 tablets | Valid |
| 159279 | Nnv Tablet | Strip of 10 tablets | Valid |
| 176184 | Prezen Tablet | Strip of 10 tablets | Valid |
| 180264 | Pregmesis F Tablet | Strip of 10 tablets | Valid |
| 201100 | Sinate Tablet | Strip of 30 tablets | Valid |
| 237257 | Vemsaid Plus 10mg/10mg/2.5mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 289 interactions are recorded. Two are rated Major: potassium citrate and potassium chloride. Many others are rated Moderate, mainly with other anticholinergic drugs (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine) and with opioids or other central nervous system depressants (morphine, loperamide, opium, dronabinol, nabilone).

Label warnings and contraindications are not available in the compiled data. Please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9936), but no clinical trial or publication directly studies nasal cavity disease. The target is also a broad, non-specific category, so evidence is limited to model output (L5).

**To proceed, the following is needed:**
- A more specific predicted disease (for example, a defined type of rhinitis) so that studies can be searched
- Clinical trial or literature evidence directly addressing the predicted disease
- Mechanism of action data
- Package insert warnings and contraindications for the India-marketed products

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Doxylamine Succinate And Pyridoxine Hydrochloride (doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de265fd1-bc22-4da1-aab5-b5fedd649c8b) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

