---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Primidone: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (generalized tonic-clonic seizures, partial epilepsy…"
monitor_inn: "Primidone"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Primidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Primidone: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Primidone is an anticonvulsant originally used to treat epilepsy, including generalized tonic-clonic and partial seizures.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primidone is an anticonvulsant (partly metabolized to phenobarbital), its efficacy in epilepsy is well established, but there is no known anti-neoplastic mechanism that would make it applicable to a nerve tumour.

The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between primidone's related neurological diseases, such as trigeminal neuralgia, not biological evidence of a therapeutic link. Seizure control might matter in patients with tumours of the nervous system, but that would be symptom management, not treatment of the tumour.

Other predictions in the list are more mechanistically plausible. They are mostly reflex epilepsy subtypes (startle epilepsy, thinking seizures, eating seizures, reading seizures, audiogenic seizures, micturition-induced seizures), which sit close to primidone's original indication. Trigeminal neuralgia is also plausible as a class effect of sodium-channel-blocking anticonvulsants, although carbamazepine remains the standard and no primidone-specific evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For context, the literature linked to the other top predictions is indirect and mostly old:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs used outside epilepsy; evidence mostly from case series and small trials (linked to trigeminal neuralgia) |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case report | Zhonghua Yi Xue Za Zhi | Startle epilepsy presenting as drop attacks; not clearly tied to a primidone effect |
| [19054416](https://pubmed.ncbi.nlm.nih.gov/19054416/) | 2009 | Cohort | Epilepsia | Antiepileptic drug choice in older veterans with new-onset epilepsy; indirect |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Animal study | Neurol Psychiatr | Antiepileptic drug effects (including primidone) on brain enzymes in audiogenic epilepsy mice |
| [14249886](https://pubmed.ncbi.nlm.nih.gov/14249886/) | 1964 | Animal study | Biull Eksp Biol Med | Audiogenic convulsions after preliminary pyramidone administration in animals |
| [116632](https://pubmed.ncbi.nlm.nih.gov/116632/) | 1979 | Case report | Arch Neurol | Drawing-induced seizures, a reflex epilepsy case |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clin Neurosci | Myoclonus therapy; primidone listed among useful drugs (500–1,000 mg/day) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 133919 | Mysoline 250 Tablet (Abbott) | Strip of 10 tablets | Not specified |
| 215161 | Tremidon Tablet (Intas) | Strip of 10 tablets | Not specified |
| 176322 | Prolet SR 100 Tablet (Alteus Biogenics) | Strip of 15 tablets (SR) | Not specified |
| 75151 | Epiad 50mg Tablet (Tas Med India) | Strip of 10 tablets | Not specified |
| 217528 | Tremfree 25 Tablet (Avallac) | Strip of 10 tablets | Not specified |

All 20 registrations are valid single-ingredient oral tablet products; none are cancelled.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: anxiety and neurotic disorders, dysthymic disorder, porphyria (inherited porphyria and porphyrin metabolism disease), kidney disease, liver disease, gallbladder disease, substance abuse/dependence, sleep apnea syndromes, and blood disorders (thrombocytopenia, neutropenia, agranulocytosis, leukopenia, pancytopenia, anemia, including macrocytic anemia and congenital neutropenia syndromes).
- **Drug Interactions**: 273 interactions were recorded. Major-level examples include **morphine** and **eliglustat**. Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), doxycycline, metronidazole, bupropion, aprepitant, pioglitazone, canagliflozin, saxagliptin, vitamin D analogues (cholecalciferol, calcifediol, calcitriol), diphenoxylate, difenoxin and dronabinol. Cimetidine is a minor interaction.

The graph-derived contraindications should be verified against the package insert, which was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trigeminal nerve neoplasm rests only on a very high model score, with no trials, no literature, and no known anti-neoplastic mechanism for primidone (Evidence Level L5). The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related neurological diseases, not biological evidence.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to assess any biological link to nerve tumours
- Package insert warnings and contraindications from the Indian regulator (approved indication text is currently empty for all registrations)
- Evidence of a plausible mechanism or preclinical data in trigeminal nerve tumours before any further evaluation
- Consider redirecting effort to better-supported candidates, such as reflex epilepsy subtypes (startle epilepsy, thinking seizures) or trigeminal neuralgia, where an anticonvulsant rationale exists, though primidone-specific clinical evidence is still lacking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

