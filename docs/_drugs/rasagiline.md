---
layout: default
title: Rasagiline
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Rasagiline: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease"
monitor_inn: "Rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Rasagiline
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

# Rasagiline: From Parkinson Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Rasagiline is an irreversible MAO-B inhibitor, originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**, but **no clinical trials and no publications** currently support this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (the data compiled for this report also lists related parkinsonian syndromes; no approved indication text is available from Indian licences) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rasagiline is an irreversible MAO-B inhibitor. It raises dopamine availability in the brain and provides symptomatic relief in Parkinson disease.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism (PARK14). A plausible link therefore exists for the parkinsonian features of the late-onset forms.

However, the underlying pathology (defective phospholipid remodelling, iron accumulation, alpha-synuclein pathology) is not addressed by MAO-B inhibition. The very high score likely reflects network proximity to the parkinsonism indications rather than disease-modifying biology. At best, the drug might offer symptomatic benefit in selected patients.

**Other predictions reviewed (all without trials or literature):**

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Paralysis agitans, juvenile, of Hunt | 99.25% | L4 | Within the parkinsonism spectrum. This is closer to an extension of the existing indication than true repurposing, and needs juvenile and paediatric safety and efficacy confirmation. Recommendation: Research Question |
| Rasmussen subacute encephalitis | 99.56% | L5 | No clear mechanistic rationale for a T-cell-mediated disease. Likely a graph artefact |
| Myelitis | 99.32% | L5 | No established anti-inflammatory role. Only indirect preclinical neuroprotection |
| Transaldolase deficiency | 99.19% | L5 | No mechanistic link. Hepatic involvement would need caution given rasagiline's CYP1A2 metabolism |
| Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis | 99.01% | L5 | A structural malformation is not expected to respond to a symptomatic MAO-B inhibitor |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 6734 | Afrelect 0.5mg Tablet (Taj Pharma India Ltd) | Strip of 10 tablets | Not specified |
| 184809 | Relgin 1 Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 184402 | Rasalect 1 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not specified |
| 184676 | Relgin 0.5 Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 189515 | Rasagin 0.5mg Tablet (Natco Pharma Ltd) | Strip of 30 tablets | Not specified |

Nine valid single-ingredient oral registrations exist in total; the five above are shown.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** hypertension and hypertensive disorder; multiple system atrophy; postural orthostatic tachycardia syndrome; orthostatic hypotension; drug-induced dyskinesia; epilepsy; bipolar disorder and major affective disorder; liver disease; gallbladder disease; melanoma; phaeochromocytoma and sympathetic paraganglioma; and several cancers (duodenum, small intestine, heart, adrenal gland).
- **Drug Interactions:** 137 interactions were recorded. Examples:
  - **Major:** bupropion, morphine.
  - **Moderate:** epinephrine, cimetidine, phentermine, diethylpropion, dronabinol, obeticholic acid, chlorpropamide, glimepiride, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, inhaled).

Please refer to the package insert for full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature. The mechanistic link is weak because MAO-B inhibition does not address the core pathology of PLA2G6-associated neurodegeneration. The juvenile parkinsonism prediction is the most coherent but is essentially an extension of the existing indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data
- Case series, natural-history data, or preclinical evidence for MAO-B inhibition in PLA2G6-related dystonia-parkinsonism
- Juvenile and paediatric safety and efficacy data if the juvenile parkinsonism direction is pursued
- Review of hepatic safety, since liver disease appears among the graph-derived contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

