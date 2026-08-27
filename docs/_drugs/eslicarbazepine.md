---
layout: default
title: Eslicarbazepine
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 6
---

# Eslicarbazepine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Eslicarbazepine: From Epilepsy (Partial-Onset Seizures) to Migraine Disorder

## One-Sentence Summary

Eslicarbazepine (ESL) is a third-generation antiepileptic drug approved in the US and Europe for partial-onset seizures, acting as a voltage-gated sodium channel (VGSC) blocker.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a score of **99.78%**,
supported by **1 completed Phase 2 clinical trial** (n=452) and **6 publications** in this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Partial-onset seizures (epilepsy) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eslicarbazepine acetate (ESL) is a third-generation antiepileptic drug whose active metabolite eslicarbazepine preferentially blocks the **inactivated state of voltage-gated sodium channels (VGSCs)**, particularly Nav1.1 and Nav1.2 subtypes. This mechanism reduces abnormal neuronal hyperexcitability by stabilising channels in their inactive conformation. Although detailed MOA data is unavailable from this evidence pack, the drug's established role as a VGSCs blocker is well-characterised in the epilepsy literature.

The mechanistic bridge to migraine is well-grounded: **cortical spreading depression (CSD)** — the electrophysiological substrate underlying migraine aura — depends critically on a massive Na⁺ influx through voltage-gated channels, and ESL's inactivated-state blockade is mechanistically capable of suppressing CSD propagation. Furthermore, trigeminal nociceptive transmission during the migraine headache phase involves Nav1.7, Nav1.8, and Nav1.9 subtypes in peripheral pain fibres. This dual-target profile makes ESL theoretically attractive for both aura suppression and headache prevention.

Importantly, this is not a novel hypothesis for this drug class. Approved migraine preventives **topiramate** and **valproate** share VGSCs blockade as part of their polypharmacological profile, establishing the class-level proof of concept. ESL's pharmacokinetic advantages over older congeners (oxcarbazepine, carbamazepine) — including once-daily dosing and a lower drug interaction burden — make it a plausible clinical candidate if efficacy can be confirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01820559](https://clinicaltrials.gov/study/NCT01820559) | Phase 2 | Completed | 452 | Multinational, randomised, double-blind, placebo-controlled, parallel-group study evaluating ESL 800 mg/day and 1200 mg/day (once daily) vs. placebo as prophylactic treatment in subjects with migraine with or without aura. This is the primary direct clinical evidence supporting the migraine prevention indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Discusses pharmacotherapy for trigeminal neuralgia; highlights that third-generation anticonvulsants (including ESL-related agents) and new CGRP blockers may serve as promising options alongside or instead of carbamazepine/oxcarbazepine, linking the drug class to both trigeminal and migraine pain pathways. |
| [32217376](https://pubmed.ncbi.nlm.nih.gov/32217376/) | 2020 | Review | Journal of the Neurological Sciences | Comprehensive assessment of ESL's tolerability and safety profile across neurological disorders — essential reference for characterising the adverse event burden relevant to any new indication pursuit. |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Network meta-analysis of antiepileptic drug monotherapy in epilepsy; contextualises ESL's relative efficacy and tolerability among the broader sodium channel blocker class, informing indirect comparative evidence. |
| [25196459](https://pubmed.ncbi.nlm.nih.gov/25196459/) | 2014 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacokinetic and pharmacodynamic interactions between antiepileptics and antidepressants — relevant given that antidepressants (amitriptyline, venlafaxine) are commonly co-prescribed for migraine prevention. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Advanced Drug Delivery Reviews | Describes chemical and pharmacokinetic properties of ESL among fifteen post-1990 antiepileptics; favourable PK profile (once daily, low DDI) supports feasibility for migraine prophylaxis. |
| [39262552](https://pubmed.ncbi.nlm.nih.gov/39262552/) | 2024 | Case Report | Cureus | Case of MELAS syndrome (mitochondrial disease with stroke-like episodes and seizures); ESL featured as part of seizure management — provides indirect context on ESL use in complex neurological presentations but is not directly relevant to migraine efficacy. |

---

## India Market Information

Eslicarbazepine acetate is currently **not marketed in India**. No registrations or product licences are on record. Regulatory entry would require a full dossier submission to CDSCO (Central Drugs Standard Control Organisation), including clinical data applicable to the Indian patient population.

---

## Safety Considerations

**Drug Interactions (125 interactions on record — key moderate-level interactions listed):**

Eslicarbazepine has a substantial DDI profile (125 recorded interactions). The following moderate-level interactions are clinically relevant in the context of migraine management:

| Interacting Drug | Level | Clinical Relevance for Migraine Use |
|-----------------|-------|--------------------------------------|
| Morphine / Morphine (liposomal) / Opium | Moderate | Opioids occasionally used for refractory migraine; CNS depression additive risk |
| Metoclopramide | Moderate | Commonly used as migraine rescue anti-emetic; interaction warrants monitoring |
| Rosuvastatin / Simvastatin | Moderate | Statins used in cardiovascular comorbidities common in migraine patients |
| Cobicistat | Moderate | CYP3A4 inhibitor; may affect ESL exposure in HIV-positive migraine patients |
| Ethanol | Moderate | Alcohol is a known migraine trigger; combined CNS effects require patient counselling |
| Folic acid | Moderate | Relevant to women of childbearing age on migraine prophylaxis |
| Aprepitant / Rolapitant | Moderate | NK1 antagonists used for nausea management; potential overlap in migraine prophylaxis settings |

> Note: Formal key warnings and contraindications from the package insert are not available in this evidence pack. Please refer to the CDSCO/EMA/FDA-approved labelling for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT01820559, n=452) directly testing ESL as migraine prophylaxis provides L2-level evidence — a meaningful clinical validation signal. The mechanistic rationale (VGSCs blockade → CSD suppression) is coherent and supported by the approved class precedent (topiramate, valproate). However, the trial results have not been confirmed in a Phase 3 study, and the drug is not currently marketed in India, creating both a regulatory and a commercial development gap.

**To proceed, the following is needed:**

- **NCT01820559 full results**: Confirm whether efficacy endpoints (reduction in monthly migraine days, responder rate) were met and whether results were published in peer-reviewed literature — this is the critical gate before any Phase 3 planning
- **Package insert / full prescribing information**: Retrieve official warnings, contraindications, and dose-limiting toxicities from EMA or FDA labelling (identified as a blocking data gap)
- **Detailed MOA documentation**: Formal DrugBank/pharmacology dossier for mechanistic gap analysis
- **India regulatory pathway assessment**: CDSCO new drug application feasibility, including data bridging requirements for Indian patients
- **DDI risk mitigation plan**: Specific interaction review with commonly co-prescribed migraine medications (beta-blockers, tricyclics, triptans) given the 125-interaction DDI profile
- **Phase 3 go/no-go decision framework**: Define primary endpoint, target population (chronic vs. episodic migraine), and sample size based on Phase 2 effect size

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted by qualified medical and pharmaceutical professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

