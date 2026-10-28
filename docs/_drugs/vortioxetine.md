---
layout: default
title: Vortioxetine
parent: Model Prediction Only (L5)
nav_order: 897
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Vortioxetine"
predicted_indications: ["neurotic disorder", "benign paroxysmal torticollis of infancy"]
description: "Vortioxetine: predicted new indication Neurotic disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Vortioxetine
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

## Vortioxetine: Neurotic disorder (rank 1); related predictions: neurotic depression, melancholia, dysthymic disorder (neurotic disorder)
{: .text-alpha }

## One-Sentence Summary

Vortioxetine is an antidepressant originally used for unipolar depression, major depressive disorder and anxiety disorder.
The TxGNN model's top-ranked prediction is **Neurotic Disorder**, but this is largely a relabeling of conditions vortioxetine already treats. The best-supported related prediction is **Melancholia** (a subtype of major depression), backed by **6 clinical trials** (including 3 placebo-controlled Phase 3 efficacy trials) and **over 20 publications**. Evidence for the top-ranked prediction itself is minimal (1 case-report-style paper, no trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Neurotic disorder (rank 1); related predictions: neurotic depression, melancholia, dysthymic disorder (neurotic disorder) |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 for neurotic disorder (L1 for melancholia and neurotic depression, via evidence in general MDD) |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold (neurotic disorder); Proceed with Guardrails (melancholia, neurotic depression) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. From the published literature, vortioxetine is a multimodal antidepressant: it inhibits the serotonin transporter (SERT), acts as a 5-HT1A agonist and 5-HT1B partial agonist, and antagonises 5-HT3, 5-HT7 and 5-HT1D receptors. It also increases serotonergic, noradrenergic, dopaminergic, cholinergic, histaminergic and glutamatergic neurotransmission (PMID 25016186).

"Neurotic disorder" is an outdated umbrella term covering anxiety, depressive and related conditions. Vortioxetine's serotonergic activity is plausibly relevant, but the prediction essentially relabels indications that are already established (depression, anxiety) rather than revealing a new repurposing opportunity.

The same applies to the other high-scoring predictions:
- **Neurotic depression** maps to depressive disorders such as MDD and dysthymia.
- **Melancholia** is the melancholic subtype of major depression, within the MDD indication. The trials enrolled general MDD populations, so efficacy in the melancholic subtype is inferred rather than directly demonstrated.
- **Dysthymic disorder** (persistent depressive disorder) shares monoaminergic pathophysiology with MDD, but there is no controlled evidence specific to it.
- **Benign paroxysmal torticollis of infancy** (rank 4) has no identifiable mechanistic link. It is a self-limiting paediatric episodic disorder, the high score is likely a TxGNN model (deep learning) artefact, and antidepressant use in infants raises serious safety concerns.

---

## Clinical Trial Evidence

No clinical trials are registered for neurotic disorder itself. The table below lists trials linked to the closely related prediction **melancholia**, all conducted in general major depressive disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01163266](https://clinicaltrials.gov/study/NCT01163266) | Phase 3 | Completed | 462 | Randomised, double-blind, placebo-controlled fixed-dose study (10 and 20 mg) in acute MDD |
| [NCT01153009](https://clinicaltrials.gov/study/NCT01153009) | Phase 3 | Completed | 614 | Placebo-controlled, duloxetine-referenced fixed-dose study (15 and 20 mg) in acute MDD |
| [NCT00735709](https://clinicaltrials.gov/study/NCT00735709) | Phase 3 | Completed | 560 | Randomised, double-blind, placebo-controlled study of 3 fixed doses in acute MDD |
| [NCT01255787](https://clinicaltrials.gov/study/NCT01255787) | Phase 2/3 | Completed | 600 | Placebo-controlled, dose-ranging study of efficacy and safety in MDD |
| [NCT01152996](https://clinicaltrials.gov/study/NCT01152996) | Phase 3 | Completed | 1075 | Long-term open-label extension (15 and 20 mg); safety and tolerability |
| [NCT00707980](https://clinicaltrials.gov/study/NCT00707980) | Phase 3 | Completed | 836 | Long-term open-label flexible-dose extension; safety and tolerability (also the only trial linked to dysthymic disorder, with indirect relevance) |

---

## Literature Evidence


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network meta-analysis | Lancet | Comparative efficacy and acceptability of 21 antidepressants in adult MDD |
| [38957929](https://pubmed.ncbi.nlm.nih.gov/38957929/) | 2024 | Meta-analysis of RCTs | Psychiatry Clin Neurosci | Dose-response of vortioxetine in adult depression |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic review / network meta-analysis | Mol Psychiatry | Antidepressants in the maintenance phase of MDD |
| [39891526](https://pubmed.ncbi.nlm.nih.gov/39891526/) | 2025 | Systematic review / meta-analysis | J Psychopharmacol | Efficacy of vortioxetine in acute MDD |
| [25874839](https://pubmed.ncbi.nlm.nih.gov/25874839/) | 2015 | Systematic review / meta-analysis | Syst Rev | Safety and efficacy of vortioxetine in acute MDD |
| [29197738](https://pubmed.ncbi.nlm.nih.gov/29197738/) | 2018 | Network meta-analysis | J Affect Disord | Levomilnacipran, vilazodone and vortioxetine versus other second-generation antidepressants |
| [25016186](https://pubmed.ncbi.nlm.nih.gov/25016186/) | 2015 | Review | Pharmacol Ther | Preclinical and clinical review of vortioxetine's multimodal activity |
| [29189941](https://pubmed.ncbi.nlm.nih.gov/29189941/) | 2018 | Review | Clin Pharmacokinet | Pharmacokinetics (half-life about 66 h, bioavailability 75%) and drug interactions |
| [34029378](https://pubmed.ncbi.nlm.nih.gov/34029378/) | 2021 | Network meta-analysis (paediatric) | Cochrane Database Syst Rev | New-generation antidepressants in children and adolescents; should not be extrapolated to adults |
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review / case report | Zh Nevrol Psikhiatr | Neurotic depression: integrated treatment with antidepressants and psychotherapy (the only paper directly linked to the rank 1 prediction) |

---

## India Market Information

Twenty valid single-ingredient registrations are listed; the first five are shown. No approved indication text is recorded for these licences.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 233722 | Vortiray 10mg Tablet | Strip of 10 tablets | Not recorded |
| 233507 | Voxigain 5 Tablet | Strip of 10 tablets | Not recorded |
| 233746 | Vdep 10mg Tablet | Strip of 10 tablets | Not recorded |
| 215752 | Trivoxetin 10mg Tablet | Strip of 10 tablets | Not recorded |
| 233772 | Vortidif 20mg Tablet | Strip of 10 tablets | Not recorded |

---

## Safety Considerations

**Drug Interactions:** The interaction screen identified 151 interactions. Examples include:
- **Major:** bupropion, lorcaserin, diethylpropion, dolasetron, palonosetron, phentermine
- **Moderate:** morphine, acetylsalicylic acid, dexamethasone, chlorpropamide, glimepiride, several insulins, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)

Literature also notes that vortioxetine is metabolised via CYP2D6, so interaction burden and genotype should be managed (PMID 37032427, PMID 29189941). Reported class-related adverse effects include gastrointestinal effects, hyperhidrosis and sexual dysfunction. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for neurotic disorder (rank 1); Proceed with Guardrails for neurotic depression and melancholia**

**Rationale:**
- The top-ranked prediction, neurotic disorder, has no clinical trials and only one low-tier paper. It is an outdated label that overlaps with already-approved depression and anxiety indications, so it does not represent a distinct repurposing opportunity.
- Neurotic depression and melancholia are supported by multiple Phase 3 placebo-controlled trials and Tier 1 meta-analyses, but that evidence reflects the existing MDD indication rather than a new one.
- Dysthymic disorder remains a research question (L3): the only linked trial is an uncontrolled extension study.
- Benign paroxysmal torticollis of infancy should not be pursued: there is no mechanistic link, no evidence, and paediatric safety concerns.

**To proceed, the following is needed:**
- Map the historical labels (neurotic disorder, neurotic depression, melancholia) to modern diagnostic categories
- Subtype-specific evidence for melancholia, and a dedicated randomised trial in persistent depressive disorder (dysthymia)
- Detailed mechanism of action data from DrugBank
- Package insert warnings and contraindications from the Indian regulator's records (currently missing, and a blocking gap for safety screening)
- A DDI management plan (CYP2D6 metabolism; serotonergic and major interacting drugs)
- Confirmation that paediatric evidence is not extrapolated to adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

