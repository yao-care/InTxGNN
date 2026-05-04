---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 3
---

# Alprazolam
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

# Alprazolam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a triazolo-benzodiazepine primarily used to treat anxiety disorders and panic disorder. The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently supporting this direction. Evidence is assessed at Level L3 — real-world observational data and comparative studies provide meaningful support, though dedicated Phase 3 RCTs specifically targeting insomnia as a primary endpoint are still lacking.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders / Panic disorder |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank source. Based on established pharmacological knowledge, Alprazolam is a positive allosteric modulator of the GABA-A receptor complex. It binds to the benzodiazepine site on GABA-A receptors (particularly α1 and α2 subunits), increasing the frequency of chloride ion channel opening in response to GABA, thereby enhancing inhibitory neurotransmission throughout the CNS.

This mechanism directly produces sedative-hypnotic effects: Alprazolam shortens sleep onset latency and prolongs total sleep time (predominantly N2/N3 slow-wave stages), which explains its established off-label utility in clinical insomnia management. However, it concurrently suppresses REM sleep and carries well-documented risks of pharmacodynamic tolerance, physical dependence, and rebound insomnia with prolonged use — characteristics that differentiate it from more sleep-selective Z-drugs (zolpidem, eszopiclone).

The mechanistic bridge from anxiety to insomnia is biologically sound. Insomnia and anxiety disorders share overlapping neurobiological substrates — including dysregulated GABAergic tone in the amygdala and hypothalamic-pituitary-adrenal (HPA) axis hyperactivity — meaning the same GABA-A enhancement that blunts anxiety responses simultaneously promotes sleep induction. Real-world prescribing patterns confirm that benzodiazepines including alprazolam are widely used for insomnia in clinical practice globally, often co-prescribed in patients with comorbid anxiety and sleep disturbance.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Large prospective cohort in Taiwan assessing risk-benefit profiles of hypnotics (including BZDs) in elderly patients with sleep disorders; evaluates efficacy, safety, pharmacokinetics, and pharmacogenetics — most relevant real-world evidence for alprazolam in insomnia |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | 8-week open-label RCT comparing Niravam (alprazolam orally disintegrating tablet) + SSRI/SNRI vs. SSRI/SNRI alone in GAD/Panic Disorder; documents alprazolam's short-term symptom relief including sleep disturbance components |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Placebo-controlled study of AVP-923 for agitation in Alzheimer's disease; GABA-A modulation as mechanism for sedation/sleep in neuropsychiatric context, mechanistically relevant |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Self-management intervention to promote BZD (including Xanax/alprazolam) cessation in Veterans using sleeping pills; captures real-world insomnia-related prescribing and long-term dependence risk |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Hypnosis vs. alprazolam premedication for perioperative anxiety in gynaecological surgery; documents acute sedative-hypnotic dose and tolerability in a controlled setting |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for hypersomnia; alprazolam used as a pharmacological comparator for CNS sedation, providing indirect mechanistic context |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for BZD dependence — terminated after enrolling only 2 subjects; limited informational value but highlights clinical challenge of BZD discontinuation in insomnia patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative RCT | *Cureus* | Head-to-head comparison of alprazolam vs. melatonin for sleep disturbances in end-stage renal disease (ESRD) hemodialysis patients; directly assesses alprazolam efficacy and safety in a sleep disorder population |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (integrative) | *Medicine* | Alprazolam serves as active control in 116-patient study of coronary heart disease with comorbid insomnia (2021–2023); confirms alprazolam as standard-of-care comparator for insomnia treatment in real-world clinical settings |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis / Cohort | *Acta Pharmaceutica* | Systematic review and meta-analysis of tranquilizers (including alprazolam) in elderly patients with chronic non-communicable diseases; evaluates dose, efficacy outcomes, and adverse event profiles |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical (Proteomic) | *Aging* | Repeated alprazolam administration in mice causes mitochondrial dysfunction and hippocampal memory impairment; elucidates molecular mechanism underlying adverse cognitive effects relevant to long-term insomnia management risk assessment |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | *Expert Opin Drug Metab Toxicol* | Comprehensive pharmacokinetics of anxiolytics including alprazolam; provides PK context (half-life, CYP3A4 metabolism, active metabolites) essential for insomnia dosing strategy |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive Model | *Value in Health Regional Issues* | 10-year BZD utilization trend analysis (Croatia); demonstrates benzodiazepines including alprazolam are widely prescribed for insomnia in real-world practice, quantifying economic burden and long-term risks |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observational | *Sleep Medicine* | Hypnotic prescription pattern analysis in large managed-care population; documents alprazolam among the non-hypnotic agents frequently prescribed off-label for insomnia |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world Analysis | *China Journal of Chinese Materia Medica* | Analysis of 1,067 insomnia patient records from 20 hospitals; characterizes concurrent diseases and medicine use including western agents (BZDs) in insomnia management |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | *Medicine* | Insomnia prevalence study among COVID-19 survivors; contextualizes current disease burden and treatment landscape where benzodiazepines remain among the most commonly deployed pharmacological options |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Review | *American Family Physician* | Narrative review of panic disorder including alprazolam treatment; describes the anxiety-insomnia symptom overlap (palpitations, hyperarousal, sleep difficulty) that underpins the mechanistic rationale for this repurposing prediction |

---

## India Market Information

Alprazolam is currently **not registered** under any drug license in this dataset for the Indian market. No authorization records are available.

> Alprazolam is classified as a Schedule H1 prescription drug (psychotropic substance) in India under the Narcotic Drugs and Psychotropic Substances (NDPS) Act. Any regulatory filing for a new insomnia indication would require CDSCO review and must comply with controlled substance prescribing and dispensing regulations.

---

## Safety Considerations

**Drug Interactions** (273 total interactions identified; key interactions listed below):

| Severity | Interacting Drug | Clinical Implication |
|----------|-----------------|----------------------|
| **Major** | Morphine | Additive CNS and respiratory depression; co-administration may be life-threatening, particularly in opioid-naïve patients |
| **Major** | Morphine (liposomal) | Same mechanism as above; risk of fatal respiratory depression |
| **Moderate** | Clarithromycin | CYP3A4 inhibition increases alprazolam plasma concentrations; monitor for excess sedation and consider dose reduction |
| **Moderate** | Miconazole | CYP3A4 inhibition; elevated alprazolam exposure |
| **Moderate** | Clotrimazole | CYP3A4 inhibition; elevated alprazolam exposure |
| **Moderate** | Cimetidine | Reduced hepatic clearance; prolonged and enhanced sedation |
| **Moderate** | Bupropion | CNS interaction; potential lowering of seizure threshold |
| **Moderate** | Aprepitant | CYP3A4 modulation; alters alprazolam pharmacokinetics unpredictably |
| **Moderate** | Metoclopramide | Additive CNS depression; increased sedation risk |
| **Moderate** | Dronabinol | Additive CNS depression; enhanced sedation and psychomotor impairment |

> The complete package insert (warnings, contraindications) was not available in this evidence pack. Please obtain and review the full prescribing information from the official regulatory source before clinical deployment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprazolam's GABA-A receptor mechanism directly and plausibly supports its activity as a sedative-hypnotic for insomnia. The TxGNN model's 99.81% prediction score is consistent with this strong mechanistic alignment. Comparative RCTs (e.g., alprazolam vs. melatonin in ESRD patients) and large-scale observational studies confirm that alprazolam is already employed for insomnia in clinical practice globally. However, the absence of registered Phase 3 RCTs with insomnia as the primary endpoint, the well-documented risks of dependence, REM suppression, and cognitive adverse effects, and the lack of India regulatory approval for this indication collectively warrant a guarded approach with rigorous patient selection and monitoring protocols.

**To proceed, the following is needed:**

- **Address data gaps DG001 & DG002**: Retrieve the full package insert (warnings, contraindications, MOA) from the official regulatory source to complete the safety and mechanism analysis before any S1 decision gate
- **Clarify CDSCO regulatory pathway**: Determine whether a new indication filing is required under India's Schedule H1 / NDPS framework for alprazolam in insomnia, and confirm feasibility
- **Establish a dedicated clinical protocol**: Design a prospective controlled study comparing alprazolam to Z-drugs (zolpidem, eszopiclone) for short-term insomnia using standardized sleep outcome measures (Insomnia Severity Index, Pittsburgh Sleep Quality Index, polysomnography)
- **Implement a risk management plan**: Define maximum treatment duration, mandatory dependence screening, and a structured tapering/discontinuation protocol to mitigate rebound insomnia and withdrawal
- **Special population assessment**: Evaluate safety data in the elderly (fall risk, cognitive decline), patients with hepatic impairment (reduced CYP3A4 clearance), and those with comorbid respiratory conditions (COPD, OSA) before broader deployment
- **Pharmacovigilance integration**: Establish post-marketing surveillance for off-label insomnia prescriptions, including monitoring for misuse, dependence, and drug-drug interactions in real-world polypharmacy settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

