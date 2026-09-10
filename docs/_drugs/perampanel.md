---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Perampanel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Perampanel: From Epilepsy (Focal/Generalized Seizures) to Visual Epilepsy

## One-Sentence Summary

Perampanel is a selective, non-competitive AMPA-receptor antagonist originally developed and marketed internationally (in 35+ countries) as adjunctive therapy for focal-onset and primary generalized tonic-clonic seizures in epilepsy; it is **not currently registered in Taiwan**. The TxGNN model predicts it may be effective for **Visual Epilepsy** (a photosensitive/visually-induced reflex epilepsy subtype), with **3 clinical trials** and **20 publications** returned by the evidence search — though none of them are designed specifically for this seizure subtype, so the direct evidence is currently indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in structured regulatory/DrugBank data (Data Gap). Per published literature, perampanel is internationally approved as adjunctive treatment for focal (partial-onset) seizures with/without secondary generalization and primary generalized tonic-clonic seizures in epilepsy. |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (mechanistic/general-population trial and literature support; no study specific to visual epilepsy) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is flagged as a data gap in this evidence pack. Based on information consistently reported across the retrieved literature, perampanel is a selective, non-competitive antagonist of AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) glutamate receptors, reducing glutamate-mediated postsynaptic neuronal excitation — a mechanism distinct from GABAergic or sodium-channel-based antiseizure drugs. This mechanism underlies its established efficacy in focal-onset and generalized tonic-clonic seizures.

Visual (photosensitive) epilepsy is characterized by photoparoxysmal responses driven by excessive glutamatergic excitation in the occipital cortex when triggered by visual stimuli (e.g., flickering light patterns). Because AMPA-receptor-mediated excitation is a plausible contributor to this cortical hyperexcitability, an AMPA antagonist such as perampanel has a coherent mechanistic rationale for suppressing photoparoxysmal/visually-triggered seizure activity — essentially an extension of its established broad-spectrum antiseizure action to a specific seizure trigger rather than a new therapeutic mechanism.

That said, all three retrieved clinical trials and all 20 literature items concern general epilepsy populations (tolerability/PK, EEG/cognition, neurophysiology testing) rather than a photosensitive/visual-epilepsy-specific cohort — the reviewers grading these trials scored the two most relevant items only "B"/"C" relevance precisely because the visually-induced seizure subtype was not a designed endpoint. The prediction should therefore be read as mechanistically plausible but clinically unconfirmed for this specific reflex-epilepsy subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Randomized, double-blind, placebo-controlled study of tolerability, safety, and PK of perampanel (E2007) in epileptic patients with partial and generalized seizures on concomitant AEDs; general safety/PK design, not visual-epilepsy-specific. |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated perampanel's effects on cognition and EEG in general epilepsy patients; assesses adverse effects during AED introduction, not a photosensitive-epilepsy cohort. |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Assessed perampanel's effects on EEG, somatosensory evoked potentials, brainstem auditory evoked potentials, and visual evoked potentials (VEP) in healthy volunteers; relevant to visual neurophysiology testing but not a visual-epilepsy treatment trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Review (Practice Guideline) | Neurology | AAN/AES guideline update on efficacy/tolerability of newer AEDs (including perampanel) for new-onset epilepsy. |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review/Meta-analysis of RCTs | Seizure | Pooled efficacy and safety of perampanel across randomized controlled trials in focal and generalized-onset seizures. |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review/Meta-analysis | Brain & Development | Efficacy, tolerability, and safety of perampanel in children and adolescents with epilepsy. |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy & Behavior | Perampanel monotherapy for focal-onset and generalized tonic-clonic seizures: clinical trial and real-world evidence. |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Post-hoc analysis of 3 Phase III RCTs | Neurology | Impact of concomitant enzyme-inducing AEDs on perampanel efficacy/safety across the pivotal Phase III trials. |
| [31912315](https://pubmed.ncbi.nlm.nih.gov/31912315/) | 2020 | Cohort | Clinical Pharmacokinetics | Therapeutic drug monitoring of AEDs (including perampanel) in women with epilepsy before, during, and after pregnancy. |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Cohort | The Medical Journal of Malaysia | Real-world efficacy and safety of adjunctive perampanel in epilepsy patients. |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Cohort | Annals of Clinical and Translational Neurology | Efficacy of perampanel in pediatric epilepsy with known/presumed genetic etiology. |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Cohort | Frontiers in Neurology | Real-life effectiveness/tolerability of perampanel in childhood absence epilepsy. |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opinion on Drug Discovery | Discovery and development history of perampanel as an AMPA-receptor antagonist antiepileptic. |

**Note:** None of the above trials or publications are designed specifically around visually-induced/photosensitive seizures — all are general epilepsy populations. This is consistent with the "L4" evidence level assigned.

---

## Taiwan Market Information

Perampanel currently holds **no marketing authorization in Taiwan** (0 registrations; market status: 未上市). No license records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: A DDI query returned 56 total interactions (source: DDInter). Notable **Moderate**-level interactions include CNS depressants and opioids (morphine, codeine, hydrocodone, opium, difenoxin, diphenoxylate, dextromethorphan), sedating antihistamines (promethazine, chlorpheniramine, azelastine nasal), cannabinoids (dronabinol, nabilone), ethanol, dexamethasone, metoclopramide, sibutramine, and chloroquine/hydroxychloroquine — consistent with perampanel's known CNS-depressant and dizziness/somnolence potentiation profile. One **Minor**-level interaction was noted with clarithromycin.

Package-insert-level warnings and contraindications are not available in this evidence pack (flagged as a Blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (AMPA-receptor antagonism suppressing cortical hyperexcitability) is sound, but no clinical trial or publication in the evidence pack specifically targets visual/photosensitive epilepsy — all supporting evidence is drawn from general epilepsy populations. Combined with the absence of Taiwan regulatory registration and a **Blocking** data gap on TFDA label warnings/contraindications, this candidate is not yet ready to advance past a research question.

**To proceed, the following is needed:**
- TFDA (or equivalent) package-insert warnings and contraindications (currently a Blocking gap, DG001)
- Confirmed DrugBank mechanism-of-action record (currently a High-severity gap, DG002)
- Preclinical or clinical evidence specifically in a photosensitive/visually-induced seizure population (e.g., photoparoxysmal response suppression studies)
- A Taiwan market-access/registration pathway assessment, given the drug is not currently marketed locally

**Additional note:** Among the 10 TxGNN-predicted indications in this evidence pack, **status epilepticus** (rank 10, score 99.77%) shows materially stronger direct evidence — an L3 evidence level, multiple targeted Phase 2–4 trials (including an actively recruiting post-cardiac-arrest prophylaxis trial, NCT06401707), a 81-patient cohort study, and two tier-1 systematic reviews — and is already scored "Proceed with Guardrails." Since status epilepticus therapy is a natural extension of perampanel's core antiseizure mechanism rather than a cross-disease application, it may warrant separate, higher-priority evaluation alongside this visual-epilepsy candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

