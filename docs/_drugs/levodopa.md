---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease (and related parkinsonian syndromes)"
monitor_inn: "Levodopa"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
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

## Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **no clinical trials** and **no publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian syndromes) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levodopa is a dopamine precursor that is converted to dopamine in the brain. Its efficacy in Parkinson disease and related movement disorders is well established.

Rasmussen encephalitis is a chronic, usually unilateral, immune-mediated inflammatory brain disease. It involves T-cell-driven neuronal injury, intractable focal seizures (often epilepsia partialis continua), progressive hemispheric atrophy, and neurological decline. A possible link is overlap in neurological symptoms with movement disorders. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This is speculation only.

Dopamine replacement has no known effect on the autoimmune or inflammatory process, or on seizure control, in this disease. Dopaminergic agents could in principle lower the seizure threshold. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Levodopa is marketed in India with 20 valid single-ingredient registrations. Approved indication text was not available for any of them. Main registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 123290 | LCD 275 Tablet | Strip of 10 tablets | Intas Pharmaceuticals Ltd |
| 216100 | Tidomet Forte Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 201468 | Syndopa Forte Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 32492 | Benspar 100mg/28.5mg Capsule | Strip of 10 capsules | Zydus Cadila |
| 201135 | Sinemet 250mg/25mg Tablet | Strip of 10 tablets | Chandra Bhagat Pharma Pvt Ltd |

All listed forms are oral (tablets and capsules).

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Disease-level contraindications (knowledge graph, not label text)**: The knowledge graph lists contraindication links with several conditions. Examples:
  - Neurological and psychiatric: epilepsy, psychotic disorder, schizoaffective disorder, mental disorder, anxiety disorder, drug-induced dyskinesia
  - Cardiovascular: myocardial infarction, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, multiple system atrophy
  - Eye: open-angle glaucoma, angle-closure glaucoma
  - Gastrointestinal, hepatic and renal: peptic ulcer disease, liver disease, kidney disease
  - Metabolic and other: diabetes mellitus, diabetic ketoacidosis, melanoma

  The epilepsy link is especially relevant, because Rasmussen encephalitis presents with intractable seizures.
- **Drug Interactions**: 104 interactions were recorded. Those shown are mostly Moderate or Minor.
  - Moderate: epinephrine, ephedrine, bupropion, metronidazole, pyridoxine, metoclopramide, iron, and several anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, methscopolamine, clidinium, mepenzolate)
  - Minor: antacids (aluminium hydroxide, calcium carbonate, magnesium salts, magaldrate)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (0.9906). There are no clinical trials or publications, and no mechanistic data. Dopamine replacement has no known effect on the immune-mediated pathology of Rasmussen encephalitis, and the seizure-related contraindication signal adds concern.

**To proceed, the following is needed:**
- Mechanism of action data for levodopa, and a clear biological rationale linking dopaminergic signalling to Rasmussen encephalitis
- Preclinical or clinical evidence (case reports, animal models, or early-phase studies) in this disease
- Package insert warnings and contraindications from the India regulator, especially regarding seizure risk
- Route and formulation compatibility assessment for this population
- Review of the similarity between the original and predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

