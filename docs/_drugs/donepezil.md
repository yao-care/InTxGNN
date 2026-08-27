---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a well-established acetylcholinesterase (AChE) inhibitor, widely used for the symptomatic treatment of Alzheimer's disease.
The TxGNN model ranks **Psychogenic Movement Disorders** as the top predicted new indication (score 99.23%), but with **no clinical trials** and **no supporting publications**, this specific prediction lacks empirical backing.
Notably, lower-ranked predictions — particularly **Lingual-Facial-Buccal Dyskinesia** (rank 8, L3 evidence) and **Chronic Tic Disorder** (rank 2, L4 evidence) — carry substantially stronger mechanistic and literature support and may be more actionable repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease (symptomatic treatment of mild to severe dementia) |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack (flagged as a High-severity data gap). Based on established clinical and pharmacological knowledge, Donepezil is a reversible, selective inhibitor of acetylcholinesterase (AChE) — the enzyme responsible for hydrolysing acetylcholine (ACh) in the synaptic cleft. By preventing ACh breakdown, Donepezil elevates synaptic ACh concentrations and enhances cholinergic neurotransmission throughout the central nervous system, primarily targeting the basal forebrain–cortical cholinergic projections implicated in cognitive function.

Psychogenic (functional) movement disorders are driven primarily by psychological and functional mechanisms — not by a structural cholinergic deficit — making them an implausible direct target for AChE inhibition. The TxGNN model's high score (0.992) most likely reflects the knowledge graph's structural proximity between "movement disorder" node clusters rather than any disease-specific mechanistic connection. No biological hypothesis currently supports Donepezil for this indication, and no clinical or preclinical literature was retrieved.

It is worth contextualising across the full ranked list: several lower-ranked TxGNN predictions carry far more defensible mechanistic rationale. **Lingual-Facial-Buccal Dyskinesia** (tardive dyskinesia subtype) is supported by a well-articulated cholinergic deficiency hypothesis in the striatum — AChE inhibition may help restore the dopamine-acetylcholine balance disrupted by long-term antipsychotic exposure — and is backed by two Cochrane systematic reviews. **Extrapyramidal and Movement Disease** similarly rests on established cholinergic-dopaminergic circuit biology in the basal ganglia, albeit with an important safety caveat: a 2025 systematic review (PMID 40224553) documents that AChEIs can themselves induce movement disorders in Alzheimer's patients, requiring careful patient-subtype stratification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Donepezil in Psychogenic Movement Disorders.

---

## Literature Evidence

Currently no related literature available for Donepezil in Psychogenic Movement Disorders.

---

## India Market Information

Donepezil currently has **no registered authorisations** in India (market status: Not marketed, 0 licences on record). No regulatory authorization table is available.

---

## Safety Considerations

**Drug Interactions** (257 total interactions identified; representative sample below)

| Severity | Interacting Drug | Clinical Note |
|----------|-----------------|--------------|
| **Major** | Bupropion | Avoid combination or monitor closely |
| **Moderate** | Atropine | Pharmacodynamic antagonism (anticholinergic vs. pro-cholinergic) |
| **Moderate** | Hyoscyamine | Antagonises Donepezil's cholinergic effect |
| **Moderate** | Glycopyrronium | Antagonises Donepezil's cholinergic effect |
| **Moderate** | Clidinium | Antagonises Donepezil's cholinergic effect |
| **Moderate** | Dicyclomine | Antagonises Donepezil's cholinergic effect |
| **Moderate** | Famotidine | Monitor |
| **Moderate** | Ranitidine | Monitor |
| **Moderate** | Cimetidine | Monitor |
| **Moderate** | Dexamethasone | Monitor |
| **Moderate** | Metronidazole | Monitor |
| **Moderate** | Dolasetron | Monitor |
| **Moderate** | Loperamide | Monitor |
| **Minor** | Clarithromycin | Low risk; note CYP3A4 inhibition |
| **Minor** | Acetylsalicylic acid | Low risk |

A key pharmacodynamic pattern across the moderate interactions: all anticholinergic agents (Atropine, Hyoscyamine, Glycopyrronium, Clidinium, Dicyclomine) directly oppose Donepezil's mechanism and can negate therapeutic benefit. Co-administration should be avoided wherever possible.

Please refer to the package insert for complete warnings and contraindications (currently a Blocking data gap — full label text not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication — Psychogenic Movement Disorders — has no clinical trials, no supporting literature, and no credible mechanistic hypothesis linking cholinergic enhancement to functional/psychogenic movement pathology. The model's high score (99.23%) most likely reflects knowledge graph structural proximity to movement disorder categories rather than true biological relevance. Without any foundational evidence, advancing this specific indication is not justified at this stage.

**To proceed, the following is needed:**

- **Reprioritise the candidate pipeline**: Evaluate **Lingual-Facial-Buccal Dyskinesia** (rank 8, L3 evidence — supported by two Cochrane reviews on cholinergic treatment of tardive dyskinesia) and **Chronic Tic Disorder** (rank 2, L4 evidence — open-label study and animal models) as the primary repurposing leads
- **Retrieve MOA data**: Complete DrugBank API query for full mechanism of action (currently a High-severity data gap)
- **Obtain full safety label**: Download and parse the package insert from the appropriate regulatory authority to resolve the Blocking data gap for warnings and contraindications
- **Conduct a formal S1 safety evaluation**: Before any clinical investigation, assess risk-benefit in the target population (including the safety paradox documented in PMID 40224553 — AChEIs can themselves induce movement disorders)
- **Assess India registration pathway**: Donepezil is not currently marketed in India; confirm regulatory strategy before any repurposing trial design

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

