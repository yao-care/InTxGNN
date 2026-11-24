---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). In India: 2 listed products (2 not discontinued)"
---

# Entacapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Entacapone: PLA2G6-associated neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor originally used for Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this direction, so it remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for entacapone: "Entacapone is a selective and reversible inhibitor of COMT. In mammals, COMT is distributed throughout various organs with the highest activities in the liver and kidney. COMT also occurs in the heart, lung, smooth and skeletal muscles, intestinal tract, reproductive organs, various glands, adipose tissue, skin, blood cells, and neuronal tissues, especially in glial cells." ([DailyMed: entacapone prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ee02a04a-4b42-4cfa-8d9d-b1459c0ee9fd), label version 2026-02-16; accessed 2026-11-19.) Based on known pharmacology, entacapone is a catechol-O-methyltransferase (COMT) inhibitor. It prolongs the action of levodopa by reducing its peripheral breakdown, and its benefit in Parkinson disease is established.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. The parkinsonian features of the latter overlap with the original indication, so a symptomatic benefit from levodopa augmentation is conceivable. This is a hypothesis, not evidence.

Entacapone would at best treat symptoms. It would not modify the underlying phospholipid metabolism defect. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1690 | Adcapone Tablet | Strip of 10 tablets | Valid |
| 72837 | Entacom Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: The knowledge graph links entacapone with contraindications in the following areas. These should be checked against the official label.
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, postural orthostatic tachycardia syndrome
  - Psychiatric: psychotic disorder, schizoaffective disorder, schizophreniform disorder, anxiety disorder, dysthymic disorder, neurotic disorder, mental disorder
  - Hepatic, renal and gastrointestinal: liver disease, gallbladder disease, kidney disease, peptic or gastric ulcer, diarrheal disease
  - Neurological: epilepsy, multiple system atrophy, drug-induced dyskinesia
  - Metabolic: diabetes mellitus, diabetic ketoacidosis
  - Other: melanoma, hemoglobinopathy, open-angle and angle-closure glaucoma, pyoureter
- **Drug Interactions**: 82 interactions were recorded. Those graded Moderate include epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide and iron. Others are of unknown severity, for example pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin and potassium chloride.
- **Additional concern**: Hepatotoxicity warnings apply to the related drug tolcapone. This matters especially for any mitochondrial or metabolic disorder.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications for PLA2G6-associated neurodegeneration, and the expected benefit would be symptomatic at best.

**To proceed, the following is needed:**
- The package insert warnings and contraindications for the Indian products. This data is currently missing and blocks safety screening.
- Detailed mechanism of action data.
- Case series or preclinical data on COMT inhibition in PLA2G6-related dystonia-parkinsonism.
- Assessment of the knowledge-graph contraindication signals against the official label.

---

### Other Predicted Indications Reviewed (Reference)

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 4 | Paralysis agitans, juvenile, of Hunt | 0.9960 | L5 | Historical term for juvenile parkinsonism. This largely overlaps with the existing Parkinson indication and is not a true new indication. Research Question. |
| 7 | Lewy body dementia | 0.9925 | L5 | Shares alpha-synuclein pathology with Parkinson disease. Support is limited to an in vitro study (PMID 23913715) and an unrelated imaging trial. Dopaminergic agents may worsen psychosis and hallucinations. Research Question. |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 0.9904 | L5 | These conditions respond poorly to levodopa. The only trial is an observational gait study. Research Question. |

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: entacapone prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ee02a04a-4b42-4cfa-8d9d-b1459c0ee9fd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

