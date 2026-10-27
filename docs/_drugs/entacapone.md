---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease"
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
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

## Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor originally used for Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this direction, so it remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (the licence records compiled for this report contain no approved indication text; the original indication comes from the knowledge graph) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entacapone is a catechol-O-methyltransferase (COMT) inhibitor. It prolongs the action of levodopa by reducing its peripheral breakdown, and its benefit in Parkinson disease is established.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. The parkinsonian features of the latter overlap with the original indication, so a symptomatic benefit from levodopa augmentation is conceivable. This is a hypothesis, not evidence.

Entacapone would at best treat symptoms. It would not modify the underlying phospholipid metabolism defect. The very high score may also partly reflect the proximity of these diseases to Parkinson disease in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1690 | Adcapone Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the data compiled for this report |
| 72837 | Entacom Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the data compiled for this report |

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
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L4 | Historical term for juvenile parkinsonism. This largely overlaps with the existing Parkinson indication and is not a true new indication. Research Question. |
| 7 | Lewy body dementia | 99.25% | L4 | Shares alpha-synuclein pathology with Parkinson disease. Support is limited to an in vitro study (PMID 23913715) and an unrelated imaging trial. Dopaminergic agents may worsen psychosis and hallucinations. Research Question. |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L4 | These conditions respond poorly to levodopa. The only trial is an observational gait study. Research Question. |
| 2, 3, 5, 6, 8, 9 | Rasmussen encephalitis, myelitis, transaldolase deficiency, lethal infantile mitochondrial myopathy, fructose-1,6-bisphosphatase deficiency, perisylvian polymicrogyria syndrome | 99.1–99.7% | L5 | No plausible mechanistic link and no evidence. Hold. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

