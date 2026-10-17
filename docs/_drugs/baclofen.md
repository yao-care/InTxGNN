---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Baclofen: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Not stated in the licence records (baclofen is generally known as a s…"
monitor_inn: "Baclofen"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence"]
---

# Baclofen
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is an oral muscle relaxant that acts on GABA-B receptors. It is generally used for spasticity, although the licence records compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **0 clinical trials** and only **9 loosely related publications** (reviews and animal studies), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (baclofen is generally known as a spasticity treatment) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only, no direct studies) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Baclofen is a GABA-B receptor agonist. GABA-B signalling can modulate dopamine and other monoamine activity in circuits that control impulsivity and attention. This is plausible but unproven.

The data compiled for this report show no paper in which baclofen itself improves ADHD symptoms. The retrieved literature concerns Tourette syndrome and tic management, where ADHD is a common comorbidity. It also includes alpha-2 agonist research and rodent studies of impulsivity, hippocampal EEG, social play and effort-based decision-making. The high score most likely reflects network proximity to related neuropsychiatric conditions (tics, impulsivity) rather than clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging treatments for Tourette syndrome, where ADHD is a common comorbidity; no direct baclofen-ADHD data |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Clinical features and management of Tourette syndrome, including its psychiatric comorbidities |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review | Cureus | Behavioural, antipsychotic and alpha-agonist treatments for tics in Tourette syndrome |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurol | Reports on 450 patients with tics/Tourette syndrome treated with baclofen/botulinum toxin A; not an ADHD study |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Other | L'Encephale | Supervised off-label methylphenidate prescribing in adult ADHD; not about baclofen |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical (animal) | Brain Res | EEG responses to neurotransmitter agonists in an ADHD rat model and a kainate epilepsy model |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical (animal) | Psychopharmacology | Alpha-2A stimulation (guanfacine) in the ventral hippocampus reduces impulsive decision-making |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Preclinical (animal) | Eur J Neurosci | Habenula integrity is needed for social play behaviour in rats |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Preclinical (animal) | Neuropsychopharmacology | Roles of the anterior cingulate cortex and basolateral amygdala in effort-based decision-making |

## India Market Information

Baclofen has 20 valid single-ingredient registrations, all oral (tablets, extended-release tablets and capsules). The records list no approved indication text. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31310 | Batlin 10mg Tablet | Tablet (strip of 10) | Not stated in the licence record |
| 149617 | Mesifen 20mg Tablet XL | Extended-release tablet (strip of 10) | Not stated in the licence record |
| 122003 | Liofen 40mg Capsule XL | Extended-release capsule (strip of 10) | Not stated in the licence record |
| 30634 | Baclonip 10mg Tablet | Tablet (strip of 10) | Not stated in the licence record |
| 44208 | Chinofen 10mg Tablet | Tablet (strip of 3) | Not stated in the licence record |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not label text): epilepsy, kidney disease, psychotic and schizophrenia-spectrum disorders (including schizoaffective and schizophreniform disorder), mental disorder, stroke and cerebrovascular disorders, cerebral infarction, autonomic nervous system disease (including autonomic dysreflexia and Horner syndrome), pyoureter, and disease of the neck of the urinary bladder.
- **Drug Interactions**: 120 interactions are recorded. The most important are:
  - **Major**: morphine, liposomal morphine.
  - **Moderate**: dronabinol, nabilone, metoclopramide, opium, sibutramine, difenoxin, diphenoxylate.
  - These involve additive central nervous system effects, so caution is needed with opioids, cannabinoids and other CNS-active drugs.

Please refer to the package insert for label-based warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.32%), but no clinical trials exist and no retrieved paper shows that baclofen improves ADHD symptoms. The evidence is model prediction only (L5). The safety signals in the knowledge graph (epilepsy, psychotic disorders) are also relevant to a neuropsychiatric population.

**To proceed, the following is needed:**
- Direct evidence, such as case series or a pilot trial of baclofen in ADHD
- Mechanism of action data and a specific hypothesis for GABA-B involvement in ADHD
- Package insert warnings and contraindications for Indian-marketed products
- A safety assessment for seizure risk, psychiatric comorbidity and use in children and adolescents

**Note:** The second predicted indication, **nicotine dependence** (score 99.19%), has stronger support at evidence level L2. It has three Phase 2 baclofen trials in smokers (one completed with 44 participants, two terminated early) and consistent preclinical data. It deserves a separate evaluation as a research question, although no Phase 3 evidence is available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

