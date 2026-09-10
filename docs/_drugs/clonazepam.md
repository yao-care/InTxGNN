---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the drug-repurposing evaluation report template directly (no additional skill needed — this is straightforward document generation per the provided v5 prompt).

# Clonazepam: From Seizure Disorders to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a benzodiazepine classically used for seizure disorders and panic disorder. The TxGNN model predicts it may also be effective for **Restless Legs Syndrome (RLS)**, with **20 supporting publications** (including randomized, placebo-controlled studies) — though currently no dedicated registered clinical trials — backing this direction. A closely related prediction, **Insomnia**, is supported by **12 clinical trials and 18 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in India (CDSCO) regulatory data — drug is not currently marketed there. Per general pharmacological references, clonazepam is classically indicated for seizure disorders (e.g., Lennox-Gastaut, akinetic, myoclonic seizures) and panic disorder. |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in the current evidence pack (data gap DG002). Based on known pharmacology, clonazepam is a benzodiazepine, and its established efficacy in seizure disorders and panic disorder derives from potentiation of GABAergic inhibitory neurotransmission in the central nervous system.

This same mechanism plausibly extends to RLS: clonazepam is a positive allosteric modulator of the GABA-A receptor. By enhancing GABAergic inhibitory transmission, it reduces excessive excitability at the sensorimotor cortex and spinal cord level, which may alleviate the abnormal sensations and involuntary limb movements characteristic of RLS, while its sedative properties improve the associated sleep disruption.

Importantly, clonazepam does **not** act on the dopaminergic pathway, which is considered the core pathophysiological driver of RLS. This means its benefit is likely symptomatic (sedation/anxiolysis-mediated) rather than disease-modifying — consistent with its real-world positioning as a second-line/adjunctive agent behind dopamine agonists, and reflected in the L2 evidence tier rather than a stronger classification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | RCT (open-label) | Journal of Mid-Life Health | Prospective randomized study comparing clonazepam vs. nortriptyline on rate, frequency, and severity of RLS in women over 40 |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | RCT | Acta Neurologica Scandinavica | Randomized, double-blind, placebo-controlled crossover trial showing clonazepam significantly improved subjective sleep quality and leg dysesthesia in 6 RLS patients |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | RCT (sleep lab) | European Neuropsychopharmacology | Acute placebo-controlled sleep laboratory study measuring effects of 1 mg clonazepam on objective/subjective sleep and awakening quality in RLS/PLMD |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Cochrane review of benzodiazepines, particularly clonazepam, for RLS symptom control |
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Review (Guideline) | Journal of Clinical Sleep Medicine | AASM clinical practice guideline for treatment of RLS and periodic limb movement disorder |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review / Meta-analysis | Journal of Clinical Sleep Medicine | Meta-analysis of pharmacological responsiveness of periodic limb movements in RLS patients across drug categories |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Review | Neurotherapeutics | Overview of RLS treatment classes including benzodiazepines |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review | Movement Disorders | Movement Disorder Society task force evidence-based review of RLS treatment modalities |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Review | Tremor and Other Hyperkinetic Movements | Historical overview of benzodiazepines, including clonazepam, in adult RLS/PLMS treatment (17 articles reviewed) |
| [12531130](https://pubmed.ncbi.nlm.nih.gov/12531130/) | 2002 | Review | Sleep Medicine Reviews | Global therapeutic considerations for RLS and periodic limb movements of sleep |

---

## Safety Considerations

**Drug Interactions** (278 total interactions on record in DDI database; key examples below):

- **Major interactions**: Morphine, Morphine (liposomal) — combined CNS and respiratory depression risk with opioids
- **Moderate interactions**: Bupropion, Aprepitant, Omeprazole, Cimetidine, Clarithromycin, Dronabinol, Metoclopramide, Nabilone, Opium, Sibutramine, Teduglutide
- **Minor interactions**: Magnesium oxide, Aluminum hydroxide, Calcium carbonate, Magaldrate, Magnesium carbonate, Magnesium hydroxide

Formal TFDA/CDSCO label warnings and contraindications are not yet available in this evidence pack (data gap DG001, Blocking severity) — package insert safety information should be consulted directly before clinical use.

---

## Additional Predicted Indications (Lower Priority)

The evidence pack also flags two other candidate indications for clonazepam, included here for completeness:

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|-----------|-------------|-----------------|----------|------|
| 2 | Insomnia | 99.32% | L2 | Proceed with Guardrails | 12 clinical trials (mostly indirect, e.g., REM sleep behavior disorder) and 18 publications, including a 2024 RCT comparing high- vs. low-dose clonazepam with CBT-I in older adults ([PMID 37940498](https://pubmed.ncbi.nlm.nih.gov/37940498/)) |
| 3 | Trigeminal Nerve Neoplasm | 99.30% | L4 | Hold | Only 2 case-report-level publications with no direct mechanistic link to tumor pathophysiology; not recommended for further pursuit |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical randomized, placebo-controlled studies and current clinical practice guidelines (AASM 2025, Cochrane 2017) support clonazepam's symptomatic benefit in RLS, consistent with its established real-world use as a second-line/adjunctive agent. However, the drug is not currently marketed in India, and safety documentation (warnings/contraindications) is not yet available, so guardrails are required before any clinical application.

**To proceed, the following is needed:**
- TFDA/CDSCO package insert warnings and contraindications (data gap DG001, Blocking — required before safety review)
- Formal, sourced mechanism-of-action documentation (data gap DG002)
- Assessment of the high DDI burden (278 interactions, including opioids) in the target RLS population, which skews toward older adults on polypharmacy
- Registration pathway assessment given current "Not Marketed" status in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

