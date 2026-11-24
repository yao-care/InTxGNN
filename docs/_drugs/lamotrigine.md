---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Lamotrigine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including partial epilepsy and Lennox-Gastaut syndrome)"
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Lamotrigine
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

## Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Lamotrigine is an antiepileptic drug, originally used for epilepsy, including partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **2 publications** for this prediction. Both publications concern trigeminal neuralgia, not tumour treatment, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including partial epilepsy and Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lamotrigine: "The precise mechanism(s) by which lamotrigine exerts its anticonvulsant action are unknown. In animal models designed to detect anticonvulsant activity, lamotrigine was effective in preventing seizure spread in the maximum electroshock (MES) and pentylenetetrazol (scMet) tests, and prevented seizures in the visually and electrically evoked after-discharge (EEAD) tests for antiepileptic activity." ([DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4), label version 2026-10-12; accessed 2026-11-19.) Based on known pharmacology, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release. This calms abnormal, hyperexcitable nerve firing, which explains its use in epilepsy and its potential to relieve neuropathic pain.

The link to the predicted indication is weak. The supporting literature is about **trigeminal neuralgia** (a facial nerve pain condition), not tumours of the trigeminal nerve. There is no evidence that lamotrigine has antitumour activity. The high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, such as trigeminal neuralgia, rather than biological evidence of a true neoplasm indication.

A closely related prediction, **trigeminal neuralgia** (ranked 2nd by TxGNN, score 0.9989), has far stronger support. It has two completed trials of lamotrigine, one of them a Phase 2/3 comparison against carbamazepine, and European Academy of Neurology guidance lists lamotrigine as an add-on or alternative option. Any development effort would more sensibly focus on that indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; concerns the pain condition, not neoplasm |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a cavernous malformation; no lamotrigine treatment of a tumour |

---

## India Market Information

Lamotrigine has 20 valid single-ingredient registrations, with no cancelled licences. The registration records do not list approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 75191 | Epilam 50mg Tablet DT | Strip of 10 tablet dt | Valid |
| 91720 | Flylep-OD 50 Tablet | Strip of 10 tablet dt | Valid |
| 114357 | JI Lmt OD 200mg Tablet SR | Strip of 10 tablet sr | Valid |
| 121198 | Lametec 100 DT Tablet | Strip of 10 tablet dt | Valid |
| 121707 | Lamitor DT 25 Tablet | Strip of 15 tablet dt | Valid |
| 121709 | Lamosyn 50 Tablet | Strip of 10 tablets | Valid |
| 121788 | Lamosyn 100 Tablet | Strip of 10 tablets | Valid |
| 122080 | Lamictal 50mg Tablet DT | Strip of 14 tablet dt | Valid |
| 125132 | Lamictin 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 125424 | Lemit 25 Tablet | Strip of 10 tablets | Valid |
| 127605 | Lemogin 25mg Tablet DT | Strip of 10 tablet dt | Valid |
| 127636 | Lamorig 50mg Tablet | Strip of 10 tablets | Valid |
| 128382 | Lemogen 25mg Tablet | Strip of 10 tablets | Valid |
| 128689 | Laogine 25mg Tablet | Strip of 10 tablets | Valid |
| 129014 | Lamight 100mg Tablet | Strip of 10 tablets | Valid |
| 129937 | Laogine 50mg Tablet | Strip of 10 tablets | Valid |
| 130001 | Lemogin 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 131100 | Lamiace 100mg Tablet DT | Strip of 10 tablet dt | Valid |
| 159293 | Nombre OD 100mg Tablet | Strip of 10 tablets | Valid |
| 225048 | Tablodep 100mg Tablet DT | Strip of 10 tablet dt | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral formulations.

---

## Safety Considerations

- **Contraindications and warnings from the knowledge graph** (not label text): anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic and aplastic anaemia), pancytopenia, and non-infectious meningitis. These are drug-disease links and should be checked against the official package insert.
- **Drug Interactions**: 149 interactions were recorded. Moderate-level ones include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide, and orlistat. Metformin is rated minor. Several others, such as proton pump inhibitors, doxycycline, and vancomycin, have an unknown severity level.

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials and no publications showing lamotrigine treats a trigeminal nerve tumour. The available literature describes trigeminal neuralgia, which is a different condition, so the evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Evidence of antitumour activity, such as preclinical studies in relevant tumour models
- Clarification of whether the prediction reflects trigeminal neuralgia rather than a true neoplasm indication
- Consideration of trigeminal neuralgia as the more supportable repurposing target (Evidence Level L2, with completed trials)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the India regulatory source

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

