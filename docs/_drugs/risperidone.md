---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). Approved use: Schizophrenia"
---

# Risperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Risperidone: From Schizophrenia and Bipolar Disorder to Familial Horizontal Gaze Palsy with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an atypical antipsychotic originally used for schizophrenia, bipolar disorder (including mania) and autism-spectrum-related conditions.
The TxGNN model's top-ranked prediction is **familial horizontal gaze palsy with progressive scoliosis**, a very rare genetic eye-movement disorder.
This prediction has **no clinical trials and no publications** behind it, so it is most likely a knowledge-graph artifact. Among the other predictions, **major affective disorder** (treatment-resistant depression) has far stronger support, with **2 completed Phase 3 trials** and **several systematic reviews**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; bipolar disorder (including mania); autism spectrum disorder (the Indian registration records contain no indication text, so this comes from the drug's known indications in the knowledge graph) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 (all valid single-ingredient products) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Risperidone is generally understood to act by blocking dopamine D2 and serotonin 5-HT2A receptors. This is why it works in schizophrenia, bipolar mania and irritability linked to autism.

The predicted disease is a rare neurodevelopmental and eye-movement disorder, related to ROBO3 gene changes. It has no known dopaminergic or serotonergic target that risperidone could act on. The high score most likely reflects the way diseases and drugs are linked in the knowledge graph, not a real biological rationale. No mechanistic link could be established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## India Market Information

Risperidone is marketed in India through 20 valid registrations, all single-ingredient oral tablets. The registration records do not include approved indication text. The five listed below are examples.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 186077 | Respidon 3 Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 189472 | Repadone 4mg Tablet | Strip of 10 tablets | Shine Pharmaceuticals Ltd |
| 184310 | Risdone-Plus Tablet | Strip of 10 tablets | Intas Pharmaceuticals Ltd |
| 185469 | Risnia MD 4 Tablet | Strip of 10 mouth-dissolving tablets | Cipla Ltd |
| 249775 | Zisper 2mg Tablet MD | Strip of 10 mouth-dissolving tablets | Torrent Pharmaceuticals Ltd |

---

## Safety Considerations

Package insert warnings and contraindications were not retrieved for this report. Please refer to the package insert for label safety information. The following comes from drug-interaction databases and the knowledge graph.

- **Drug Interactions**: 362 interactions are recorded in total. The two rated Major are:
  - Bupropion
  - Morphine

  Examples rated Moderate include:
  - Metformin and other antidiabetic agents (acarbose, alogliptin, albiglutide, canagliflozin)
  - Epinephrine
  - Hydrocortisone
  - Famotidine
  - Anticholinergic agents (atropine, hyoscyamine, glycopyrronium, clidinium)
  - Loperamide
  - Bisacodyl
  - Amphotericin B
  - Lorcaserin
- **Conditions flagged as contraindications in the knowledge graph** (not taken from label text). The main groups are:
  - Cardiovascular: heart disease, myocardial infarction, stroke, conduction disease, sudden cardiac arrest, orthostatic or low blood pressure
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, obesity
  - Blood: neutropenia, agranulocytosis
  - Liver and gallbladder: liver failure, liver disease, gallbladder disease
  - Other: epilepsy, female breast carcinoma, multiple system atrophy, postural orthostatic tachycardia syndrome

  These should be verified against the official label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a very high model score but no trials, no publications and no plausible mechanism, so it is best treated as a graph-based artifact. Risperidone's safety burden (metabolic, cardiovascular and extrapyramidal effects, and possibly a lowered seizure threshold) is not justified by this prediction.

**Other predictions worth noting from the same analysis:**
- **Major affective disorder (treatment-resistant unipolar depression)** is the strongest signal, rated L1 and "Proceed with Guardrails".
  - Two completed Phase 3 randomised trials of adjunctive risperidone support it: [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) (n=630) and [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) (n=258).
  - Systematic reviews and network meta-analyses also support it, for example [PMID 34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) and [PMID 34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/).
  - The bipolar part of this indication overlaps with an existing one, so the new signal is augmentation in unipolar treatment-resistant depression.
- **Trichotillomania** is rated L4 and a "Research Question". It is supported only by case reports and small case series of risperidone added to SSRIs.
- **Phelan-McDermid syndrome** is rated L4 and a "Research Question". Support is limited to a review and a zebrafish study, and any benefit would be symptomatic only.
- **Asperger syndrome** largely repeats the existing autism-spectrum indication, and **amelocerebrohypohidrotic syndrome** has no support.

**To proceed, the following is needed:**
- A decision to re-prioritise the evaluation toward treatment-resistant depression, which has the strongest evidence
- Verification of the primary outcomes of the two Phase 3 trials
- Package insert warnings and contraindications for the marketed Indian products
- Detailed mechanism of action data from DrugBank
- A safety monitoring plan covering metabolic parameters, prolactin and extrapyramidal symptoms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

