---
layout: default
title: Procyclidine
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Procyclidine"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "transaldolase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "paralysis agitans, juvenile, of Hunt", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "fructose-1,6-bisphosphatase deficiency"]
description: "Procyclidine: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Procyclidine
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

## Procyclidine: Rasmussen subacute encephalitis
{: .text-alpha }

## One-Sentence Summary

Procyclidine is an anticholinergic (muscarinic antagonist) originally used to treat Parkinson disease and related movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, procyclidine is a muscarinic antagonist (anticholinergic) whose efficacy in parkinsonian disorders and dystonia is established. It reduces the relative excess of cholinergic activity in the basal ganglia.

Rasmussen encephalitis is an immune-mediated, T-cell-driven chronic encephalitis that causes focal epilepsy. No established link exists between muscarinic blockade and this pathology. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For context, other predictions in the top 10 are also unsupported by clinical data. The most plausible symptomatic links are **PLA2G6-associated neurodegeneration** (parkinsonism and dystonia overlap) and **progressive supranuclear palsy-corticobasal syndrome** (anticholinergics are generally poorly effective there and may worsen cognition). The entry "paralysis agitans, juvenile, of Hunt" is a historical term for juvenile parkinsonism and largely overlaps with existing indications, so it is not a true repurposing finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Procyclidine has 20 valid single-ingredient registrations in India, all oral tablets. No approved-indication text is available in the records. The 5 main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 177924 | Prolidine 2.5mg Tablet (Oxford Pharmaceuticals) | Strip of 10 tablets | Not specified |
| 154622 | Nopadin 2.5mg Tablet (Kivi Labs) | Strip of 10 tablets | Not specified |
| 176998 | Procydin 2.5 Tablet (D D Pharmaceuticals) | Strip of 10 tablets | Not specified |
| 116277 | Kemdin 5mg Tablet (Vrddhi Life Sciences) | Strip of 10 tablets | Not specified |
| 204191 | Sycline 5mg Tablet MD (Pifer Pharmaceuticals) | Strip of 10 orally disintegrating tablets | Not specified |

## Safety Considerations

- **Disease-level contraindications (knowledge graph, not label text)**: Procyclidine is associated with contraindications in the following disease groups:
  - Eye: angle-closure (closed-angle) glaucoma
  - Gastrointestinal: gastric ulcer, pyloric stenosis, achalasia/megaesophagus, hiatus hernia, paralytic ileus, intestinal obstruction, toxic megacolon, ulcerative colitis/inflammatory bowel disease
  - Urinary: benign prostatic hyperplasia, bladder neck obstruction
  - Neuromuscular: myasthenia gravis and other neuromuscular junction diseases
  - Cardiovascular and endocrine: hypertension, coronary artery disease, hyperthyroidism/Graves disease/thyrotoxicosis
  - Organ disease: kidney, liver and gallbladder disease
- **Drug Interactions**: 70 interactions were identified. The two **Major** interactions shown are with potassium citrate and potassium chloride. Most others are Moderate and involve additive anticholinergic effects (e.g., atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium) or additive central nervous system and gut-motility effects (e.g., morphine, loperamide, opium, metoclopramide, dronabinol, nabilone, eluxadoline).
- **Paediatric and cognitive note**: Anticholinergics may impair cognition and attention, which is relevant for conditions such as ADHD and PSP/CBS.

Please also refer to the package insert for full warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (0.9974), with no clinical trials or literature and no plausible mechanistic link between muscarinic blockade and Rasmussen encephalitis. Evidence is at level L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence linking cholinergic modulation to Rasmussen encephalitis
- If a symptomatic-use strategy is pursued, consider re-prioritising candidates such as PLA2G6-associated neurodegeneration, which has the most plausible overlap with the labelled parkinsonism and dystonia domains, and gather supporting evidence for it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

