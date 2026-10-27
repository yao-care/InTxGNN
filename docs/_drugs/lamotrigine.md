---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Lamotrigine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including partial epilepsy and Lennox-Gastaut syndrome)"
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release. This calms abnormal, hyperexcitable nerve firing, which explains its use in epilepsy and its potential to relieve neuropathic pain.

The link to the predicted indication is weak. The supporting literature is about **trigeminal neuralgia** (a facial nerve pain condition), not tumours of the trigeminal nerve. There is no evidence that lamotrigine has antitumour activity. The high score most likely reflects the drug's network proximity to trigeminal neuralgia in the knowledge graph, rather than a true neoplasm indication.

A closely related prediction, **trigeminal neuralgia** (ranked 2nd by TxGNN, score 99.89%), has far stronger support. It has two completed trials of lamotrigine, one of them a Phase 2/3 comparison against carbamazepine, and European Academy of Neurology guidance lists lamotrigine as an add-on or alternative option. Any development effort would more sensibly focus on that indication.

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

Lamotrigine has 20 valid single-ingredient registrations, with no cancelled licences. The registration records do not list approved indication text. Five of the main registrations:

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| Registration No. 122080 | Lamictal 50mg Tablet DT | Strip of 14 dispersible tablets |
| Registration No. 121198 | Lametec 100 DT Tablet | Strip of 10 dispersible tablets |
| Registration No. 121788 | Lamosyn 100 Tablet | Strip of 10 tablets |
| Registration No. 121707 | Lamitor DT 25 Tablet | Strip of 15 dispersible tablets |
| Registration No. 114357 | JI Lmt OD 200mg Tablet SR | Strip of 10 sustained-release tablets |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

