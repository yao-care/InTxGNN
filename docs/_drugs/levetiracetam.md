---
layout: default
title: Levetiracetam
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levetiracetam: predicted new indication Visual epilepsy (evidence level L5). Approved use: Partial epilepsy"
monitor_inn: "Levetiracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Levetiracetam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Levetiracetam: From Partial Epilepsy to Visual Epilepsy
{: .text-alpha }

## One-Sentence Summary

Levetiracetam is an antiseizure medication originally used to treat partial (focal) epilepsy.
The TxGNN model's top-ranked prediction is **Visual Epilepsy**, but the supporting evidence is indirect: **no clinical trials** and **20 general seizure publications** (none specific to visual epilepsy).
The best-supported candidate among the ten predictions is **Status Epilepticus**, with **16 registered clinical trials** (including two completed Phase 3 RCTs) and **20 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy |
| Predicted New Indication | Visual epilepsy (rank 1) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (visual epilepsy); L1 for the best-supported alternative, status epilepticus |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (visual epilepsy); Proceed with Guardrails (status epilepticus) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the literature, levetiracetam is known to bind synaptic vesicle protein 2A (SV2A) and reduce neurotransmitter release, which dampens neuronal hyperexcitability. Its efficacy in focal epilepsy is well established.

Visual (photosensitive) epilepsy is a reflex seizure type. A general antiseizure mechanism could plausibly apply. However, the retrieved literature covers general seizure populations (neonatal seizures, post-stroke seizures, prophylaxis after brain injury) and none of it addresses visual or photosensitive epilepsy. The link is therefore an extrapolation, not demonstrated evidence.

The other top-ranked predictions are mostly reflex seizure types (eating, audiogenic, thinking, micturition-induced, orgasm-induced, startle and reading seizures). They are all scored in the 99.9% range. Their evidence differs a lot:

| Predicted Indication | Score | Evidence Level | Evidence Summary |
|------|------|------|------|
| Visual epilepsy | 99.98% | L4 | Indirect only; general seizure literature |
| Eating seizures | 99.96% | L4 | No levetiracetam efficacy data in this condition |
| Audiogenic seizures | 99.96% | L4 | Rodent kindling model (PMID 18397292) and a veterinary open-label RCT in cats (PMID 26690830); no human trial |
| Thinking seizures | 99.96% | L5 | Non-specific literature; model prediction only |
| Micturition-induced seizures | 99.96% | L5 | Non-specific literature; model prediction only |
| Orgasm-induced seizures | 99.96% | L5 | No literature or trials |
| Startle epilepsy | 99.96% | L3 | Small uncontrolled add-on study (PMID 18486495) and case reports |
| Reading seizures | 99.94% | L4 | Case series (PMID 22386591); related-syndrome studies; a different SV2A ligand (seletracetam) |
| Status epilepticus | 99.91% | L1 | Multiple Phase 3 RCTs |
| Beta-ketothiolase deficiency | 99.90% | L5 | No literature; no known mechanistic link |

Status epilepticus is the most clinically grounded candidate. IV levetiracetam is already used as a second-line agent after benzodiazepines, and the high-quality trial evidence below supports it.

## Clinical Trial Evidence

**Visual epilepsy (rank 1):** Currently no related clinical trials registered.

**Status epilepticus (rank 9, best-supported alternative):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | Completed | 478 | Blinded comparison of fosphenytoin, valproate and levetiracetam in benzodiazepine-refractory status epilepticus (ESETT) |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | Completed | 203 | IV levetiracetam plus clonazepam vs clonazepam alone in prehospital generalized tonic-clonic status epilepticus |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | Completed | 80 | Open-label levetiracetam vs valproate in children with refractory generalized convulsive status epilepticus |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | Completed | 144 | Levetiracetam plus midazolam in pediatric generalized convulsive status epilepticus |
| [NCT00362141](https://clinicaltrials.gov/study/NCT00362141) | Phase 2 | Unknown | 12 | Safety and tolerability of add-on levetiracetam in status epilepticus |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Phase 4 | Completed | 62 | Open-label levetiracetam vs fosphenytoin in convulsive status epilepticus |
| [NCT04176887](https://clinicaltrials.gov/study/NCT04176887) | Phase 4 | Unknown | 60 | Levetiracetam vs phenytoin in pediatric status epilepticus |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | Not applicable | Completed | 138 | Levetiracetam vs valproic acid in pediatric status epilepticus |
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | Not applicable | Completed | 152 | IV brivaracetam vs levetiracetam in pediatric status epilepticus |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | Recruiting | 124 | Ketamine plus levetiracetam vs levetiracetam alone in pediatric convulsive status epilepticus |

## Literature Evidence

**Visual epilepsy (rank 1):** The retrieved publications are all about general seizure populations. The most relevant are listed below; none is specific to visual or photosensitive epilepsy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | Phase 3 RCT | Lancet Neurol | PEACH: prophylactic levetiracetam for seizure prevention in acute intracerebral haemorrhage |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocrit Care | Levetiracetam seizure prophylaxis in neurocritical care |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Network meta-analysis | Neurology | Antiseizure medications in poststroke seizures |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |

**Status epilepticus (rank 9):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | Randomized trial of three anticonvulsants for benzodiazepine-refractory status epilepticus |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT | Lancet | ESETT by age group: levetiracetam, fosphenytoin and valproate in established status epilepticus |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | EcLiPSE: levetiracetam as an alternative to phenytoin in children |
| [38580318](https://pubmed.ncbi.nlm.nih.gov/38580318/) | 2024 | Review | Semin Neurol | Pharmacological management update; phenytoin, valproate and levetiracetam have similar safety and efficacy |
| [37391637](https://pubmed.ncbi.nlm.nih.gov/37391637/) | 2023 | Review | Pediatr Rev | Pediatric status epilepticus; levetiracetam among effective agents |

**Other predicted indications with direct but limited evidence:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18486495](https://pubmed.ncbi.nlm.nih.gov/18486495/) | 2008 | Uncontrolled clinical study | Seizure | Add-on levetiracetam in startle epilepsy |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | Veterinary RCT (open-label) | J Feline Med Surg | Levetiracetam vs phenobarbital in feline audiogenic reflex seizures |
| [22386591](https://pubmed.ncbi.nlm.nih.gov/22386591/) | 2012 | Case series | Epilepsy Behav | Excellent response to levetiracetam in reading epilepsy |

## India Market Information

Levetiracetam has 20 valid single-ingredient registrations and none cancelled. The approved indication text is not available in the data compiled for this report. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 115907 | Keppra 250mg Tablet | Strip of 10 tablets | UCB India Pvt Ltd |
| 128842 | Levitex Injection | Vial of 5 ml injection | Nexokinde Healthcare Pvt Ltd |
| 130181 | Levtam 750mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 119384 | Kuret 1000mg Tablet ER | Strip of 10 extended-release tablets | Molekule India Pvt Ltd |
| 204990 | Seiz-Free 1000mg Tablet | Strip of 10 tablets | USV Ltd |

Oral tablets, extended-release tablets and an injectable form are all available. The injectable matters for status epilepticus, which requires IV administration.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** The knowledge graph flags caution in kidney disease, liver disease, gallbladder disease, anxiety and other mental disorders (including psychotic and schizoaffective disorders), and blood disorders (neutropenia, agranulocytosis, leukopenia, pancytopenia).
- **Drug Interactions:** 155 interactions were recorded. Moderate-level interactions include morphine (including liposomal), dronabinol, nabilone, metoclopramide, opium and sibutramine. Others, such as pantoprazole, omeprazole, metformin and doxycycline, have unclassified severity.
- **Reported adverse effects in the literature:** hyponatremia, gingival hyperplasia and seizure aggravation (case reports and series).

Please refer to the package insert for official warnings and contraindications, as label data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold for visual epilepsy; Proceed with Guardrails for status epilepticus**

**Rationale:**
- Visual epilepsy has no clinical trials and only indirect literature, so it stays at L4. The high TxGNN score alone does not justify advancing it.
- Status epilepticus is supported by two completed Phase 3 RCTs (NCT01960075 and NCT01150331) plus several Phase 2 trials, and meets L1. Startle epilepsy is a smaller signal (L3) and audiogenic seizures remain a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently missing, and blocking formal safety screening)
- Detailed mechanism of action data from DrugBank
- For visual epilepsy: a levetiracetam-specific study in photosensitive epilepsy, such as an intermittent photic stimulation trial
- For status epilepticus: guardrails covering agent choice by age and comorbidity, renal dose adjustment, behavioral adverse effect monitoring, and separate consideration of pediatric vs adult and convulsive vs non-convulsive populations
- For the low-evidence predictions (orgasm-induced seizures, beta-ketothiolase deficiency): deprioritize, as no evidence or mechanistic link was found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

