---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 7
monitor_inn: "Sertraline"
predicted_indications: ["histrionic personality disorder (disease)", "schizoid personality disorder", "paranoid personality disorder", "schizotypal personality disorder", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
last_modified_at: 2026-11-24
description: "Sertraline: predicted new indication Histrionic personality disorder (disease) (evidence level L5). In India: at least 20 listed products"
---

# Sertraline
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

## Sertraline: Histrionic personality disorder (disease)
{: .text-alpha }

## One-Sentence Summary

Sertraline is an antidepressant of the selective serotonin reuptake inhibitor (SSRI) class. The TxGNN model predicts it may be effective for **histrionic personality disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Histrionic personality disorder (disease) |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for sertraline: "Sertraline potentiates serotonergic activity in the central nervous system through inhibition of neuronal reuptake of serotonin (5-HT)." ([DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7), label version 2023-08-08; accessed 2026-11-19.) Based on general knowledge, sertraline belongs to the SSRI class, which increases serotonin signalling in the brain. Its use in anxiety-related conditions is well established. Mechanistically, it may influence mood, anxiety and impulsivity, which are features that overlap with some personality disorders.

The model most likely assigns the high score because of closeness in the network of related personality and anxiety disorders, not because of disease-specific biology. Several neighbouring personality disorders (schizoid, paranoid, schizotypal) received an identical score of 0.9993, which supports this reading. No study in the compiled data tests sertraline in histrionic personality disorder, so the link remains a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

At least 20 single-ingredient sertraline registrations were found, and the list may be partial. The records do not include approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 39363 | Cnsert 25mg Tablet | Strip of 10 tablets | Valid |
| 58529 | Daxid 25mg Tablet | Strip of 15 tablets | Valid |
| 65442 | Dazline 50mg Tablet | Strip of 10 tablets | Valid |
| 73952 | Elesert 12.5 Tablet | Strip of 10 tablets | Valid |
| 74165 | Elesert 25 Tablet | Strip of 10 tablets | Valid |
| 125561 | Linta 50mg Tablet | Strip of 10 tablets | Valid |
| 186793 | Rollosert 100 Tablet | Strip of 10 tablets | Valid |
| 200878 | Serlin 50mg Tablet | Strip of 10 tablets | Valid |
| 201032 | Sermind 100 Tablet | Strip of 10 tablets | Valid |
| 201671 | Setmax 100 Tablet | Strip of 10 tablets | Valid |
| 202048 | Serocare 50 Tablet | Strip of 10 tablets | Valid |
| 202180 | Setral 25mg Tablet | Strip of 10 tablets | Valid |
| 203515 | Sertanex 50mg Tablet | Strip of 10 tablets | Valid |
| 203578 | Senta 25mg Tablet | Strip of 10 tablets | Valid |
| 205342 | Serdos 50 Tablet | Strip of 10 tablets | Valid |
| 205564 | Setradox 50mg Tablet | Strip of 10 tablets | Valid |
| 206513 | Sertane 100mg Tablet | Strip of 10 tablets | Valid |
| 210377 | Sertapox 100mg Tablet | Strip of 10 tablets | Valid |
| 226204 | Tras 50mg Tablet | Strip of 10 tablets | Valid |
| 249466 | Zedtraline 50mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindication-type relations in the knowledge graph** (not label text): epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, serotonin syndrome.
- **Drug Interactions**: 396 interactions were recorded. Those rated **Major** among the first 20 listed include bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and phentermine. Moderate interactions include famotidine, loperamide, morphine, acetylsalicylic acid, clarithromycin and glimepiride.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications for histrionic personality disorder. The high score appears to reflect network proximity to other personality and anxiety disorders. The evidence level is therefore L5.

However, it largely overlaps with anxiety indications already linked to sertraline, so it is not a distinct repurposing opportunity.

**To proceed, the following is needed:**
- Any clinical or observational study of sertraline specifically in histrionic personality disorder
- Mechanism of action data and a mechanistic rationale specific to this condition
- Package insert warnings and contraindications from the Indian regulatory records
- A drug interaction review for the likely co-medications in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

