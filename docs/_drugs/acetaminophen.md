---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acetaminophen: From Pain & Fever to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol, DB00316) is one of the world's most widely used analgesic and antipyretic agents, primarily indicated for the relief of pain and reduction of fever.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar migraine), with **no specific registered clinical trials** but **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain relief and fever reduction (analgesic/antipyretic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed (data gap likely) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on known pharmacology, Acetaminophen exerts its analgesic effects primarily through **central inhibition of COX enzymes** (reducing prostaglandin synthesis in the CNS), **modulation of the endocannabinoid system** via TRPV1 desensitization, and **enhancement of descending serotonin inhibitory pathways**. These central mechanisms—distinct from the peripheral COX inhibition of NSAIDs—are directly relevant to central pain sensitization, a key feature of migraine.

For **migraine with brainstem aura** (formerly basilar migraine), the treatment landscape is uniquely constrained. Triptans—the standard first-line acute migraine therapy—carry potential vasoconstrictive concerns that have led several guidelines to restrict or caution their use in this specific subtype. Acetaminophen has no vasoconstrictive mechanism whatsoever, positioning it as a clinically safer alternative, particularly for pregnant patients, individuals with cardiovascular risk factors, and those in whom triptans are contraindicated. Clinical guidelines, including those from the American Headache Society, already recognize acetaminophen as an evidence-based option for acute migraine treatment broadly.

It is important to note that while acetaminophen can effectively address the **pain phase** of migraine, it does not directly target the neurophysiological mechanism underlying brainstem aura—specifically cortical spreading depression (CSD). The existing evidence base, though substantial for general migraine, is not yet specific to the brainstem aura subtype, which limits the strength of this prediction and warrants guardrails before clinical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for acetaminophen in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Guideline | *Headache* | American Headache Society evidence assessment: acetaminophen and combination analgesics are evidence-based options for acute migraine; provides updated efficacy grading |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (×3) | *Archives of Neurology* | Three double-blind, randomized, placebo-controlled trials demonstrating efficacy and safety of acetaminophen + aspirin + caffeine combination for alleviating migraine headache pain |
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | *Archives of Internal Medicine* | Population-based randomized double-blind placebo-controlled trial: acetaminophen monotherapy is safe and effective for acute migraine treatment |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT (×3) | *Clinical Therapeutics* | Three randomized placebo-controlled trials: OTC acetaminophen + aspirin + caffeine combination effective for menstruation-associated migraine vs. non-menstrual migraine |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Study | *Headache* | Isometheptene/dichloralphenazone/acetaminophen vs. sumatriptan for mild-to-moderate migraine (with or without aura): comparable efficacy and safety at first sign of attack |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | *Neurologic Clinics* | Acetaminophen identified as first-line symptomatic treatment for headache during pregnancy, including migraine; supports use in populations where vasoconstrictive agents are restricted |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | *Cureus* | Acetaminophen recommended as an abortive therapy for migraine in pregnancy; notes particular relevance for migraine with aura subgroups, including those with neurological features |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | *Handbook of Clinical Neurology* | Status migrainosus management reviewed; highlights role of non-vasoconstrictive analgesics including acetaminophen for complicated or refractory migraine presentations |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | *Neurology International* | Acetaminophen cited as appropriate treatment for mild-to-moderate migraine and as a standard comparator in evaluating newer agents such as ubrogepant |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | *Cureus* | Comprehensive review of migraine treatment during pregnancy and breastfeeding; acetaminophen consistently identified as the preferred analgesic across all trimesters |

---

## India Market Information

No regulatory registrations are currently recorded in this dataset for Acetaminophen (0 licenses). This is highly inconsistent with the drug's global status as one of the most widely available OTC analgesics and likely reflects a **data gap** in the current regulatory data feed rather than actual market absence. Independent verification via CDSCO is recommended before drawing any conclusions about availability.

---

## Safety Considerations

**Drug Interactions (277 interactions documented in total; selected key interactions shown below):**

| Interacting Drug | Severity | Clinical Note |
|----------------|----------|--------------|
| Activated charcoal | Moderate | Significantly reduces acetaminophen absorption; primarily relevant in overdose management scenarios |
| Glycerol phenylbutyrate | Moderate | Potential pharmacokinetic interaction affecting drug exposure |
| Naltrexone | Moderate | May reduce analgesic efficacy of acetaminophen; exercise caution when co-administering in pain management |
| Metoclopramide | Minor | May enhance rate of acetaminophen absorption via accelerated gastric emptying |
| Cimetidine / Ranitidine | Minor | Minor effects on acetaminophen hepatic metabolism; generally not clinically significant at standard doses |
| Atropine / Anticholinergics | Minor | Reduced GI motility may slow acetaminophen absorption rate |

Please refer to the official prescribing information for complete warnings and contraindications. Warning and contraindication data were not available in the current dataset.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized controlled trials and systematic guidelines establish acetaminophen as an evidence-based acute migraine treatment, and its lack of vasoconstrictive activity makes it a mechanistically well-justified option for the brainstem aura subtype where triptans are often restricted. However, no clinical trial data exist specifically for the *migraine with brainstem aura* subpopulation, leaving a critical evidence gap that must be addressed before formal repurposing claims can be made.

**To proceed, the following is needed:**
- **[Blocking]** Obtain CDSCO/TFDA package insert safety data (key warnings and contraindications): download and parse the official prescribing information PDF
- **[High Priority]** Retrieve detailed mechanism of action data via DrugBank API (DB00316) to strengthen mechanistic justification
- Conduct a dedicated literature search and, if feasible, a prospective observational study specifically enrolling patients diagnosed with *migraine with brainstem aura* (ICD: G43.1)
- Verify India market registration status independently via CDSCO — 0 registrations is almost certainly a data artifact for a drug of this ubiquity
- Assess appropriate dosage forms and administration routes for the target indication in the relevant patient population (e.g., oral vs. rectal for patients experiencing severe nausea during migraine attacks)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

