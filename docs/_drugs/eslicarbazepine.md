---
layout: default
title: Eslicarbazepine
parent: High Evidence (L1-L2)
nav_order: 322
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Eslicarbazepine: predicted new indication Migraine disorder (evidence level L2). Approved use: Not stated in the Indian licence data compiled for this report (eslic…"
monitor_inn: "Eslicarbazepine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "insomnia (disease)", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Eslicarbazepine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **5** 
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

## Eslicarbazepine: From Epilepsy (Antiseizure Therapy) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Eslicarbazepine is an antiseizure medicine that blocks voltage-gated sodium channels and is marketed in India as a tablet.
The TxGNN model predicts it may be effective for **migraine disorder**,
with **1 completed Phase 2 clinical trial (452 participants)** and a small body of literature, mostly general antiseizure drug reviews rather than migraine studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence data compiled for this report (eslicarbazepine is known as an antiseizure drug) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L2 |
| India Market Status | Marketed (valid licences: 9 of 9) |
| Number of Registrations | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, eslicarbazepine (via its active metabolite S-licarbazepine) is a voltage-gated sodium channel blocker. Its efficacy in epilepsy is established, and mechanistically it may be applicable to migraine.

Other antiseizure drugs that modulate neuronal excitability, such as topiramate and valproate, are used for migraine prevention. Reducing neuronal hyperexcitability and cortical spreading depression is therefore a plausible way for eslicarbazepine to work in migraine.

A Phase 2 trial of eslicarbazepine acetate in migraine prevention has been completed. However, the efficacy results are not included in the data compiled for this report, so the strength of the clinical signal cannot be confirmed.

Other predicted indications are weaker. The migraine subtypes (brainstem aura, susceptibility entries) likely reflect closeness to migraine in the disease ontology rather than independent evidence. The insomnia prediction is not supported, and the available literature points to sleep-related adverse signals. The two rare skin conditions (atrophoderma vermiculata, ulerythema ophryogenesis) have no plausible mechanistic link and appear to be model artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01820559](https://clinicaltrials.gov/study/NCT01820559) | Phase 2 | Completed | 452 | Multinational, randomised, double-blind, placebo-controlled study of eslicarbazepine acetate 800 mg/day and 1200 mg/day once daily vs placebo as migraine prophylaxis (2009–2010). Efficacy results are not provided. |

## Literature Evidence

None of the publications below tests eslicarbazepine for migraine outcomes. The first three are the most relevant and the rest are general background.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32217376](https://pubmed.ncbi.nlm.nih.gov/32217376/) | 2020 | Review | J Neurol Sci | Tolerability and safety profile of eslicarbazepine acetate in neurological disorders |
| [32025776](https://pubmed.ncbi.nlm.nih.gov/32025776/) | 2020 | Preclinical study | Psychopharmacology | Eslicarbazepine acetate combined with standard and alternative analgesics reduced trigeminal nociception |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Pharmacotherapy update for trigeminal neuralgia; third-generation anticonvulsants and migraine-targeted agents mentioned as possible options |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network meta-analysis | Cochrane Database Syst Rev | Antiepileptic drug monotherapy for epilepsy (not migraine) |
| [25114785](https://pubmed.ncbi.nlm.nih.gov/25114785/) | 2013 | Review | Ther Adv Drug Saf | Risk of cutaneous adverse reactions in HLA-A*31:01 carriers given carbamazepine, oxcarbazepine or eslicarbazepine |
| [25196459](https://pubmed.ncbi.nlm.nih.gov/25196459/) | 2014 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetic and pharmacodynamic interactions between antiepileptics and antidepressants |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 246993 | Zefretol 400 Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not stated |
| 73750 | Eslizen 800mg Tablet (Intas) | Strip of 10 tablets | Not stated |
| 87442 | Flugesic 800mg Tablet (Lupin) | Strip of 10 tablets | Not stated |
| 81203 | Eslify 200mg Tablet (Torrent) | Strip of 10 tablets | Not stated |
| 80251 | Eslify 800 Tablet (Torrent) | Strip of 10 tablets | Not stated |

There are 9 valid single-ingredient registrations in total, all oral tablets.

## Safety Considerations

- **Drug Interactions**: 125 interactions are recorded. The 20 listed in the data compiled for this report are all of moderate severity. Examples include:
  - Opioids and related agents: morphine (including liposomal), opium, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Other CNS-active agents: ethanol, sibutramine
  - Antiemetics and NK1 antagonists: aprepitant, rolapitant, metoclopramide
  - Statins: rosuvastatin, simvastatin
  - Others: eliglustat, naloxegol, mannitol, nitisinone, folic acid, cobicistat
- **Related literature**: A review notes a risk of cutaneous adverse reactions in HLA-A*31:01 carriers given related drugs (carbamazepine, oxcarbazepine, eslicarbazepine). A pharmacovigilance analysis reports sleep-disturbance signals with antiseizure medications.

Please refer to the package insert for warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence for migraine is one completed Phase 2 trial (n=452) whose results are not available, so it is unclear whether it was positive. The package insert safety information is also missing, which blocks safety screening. Other predicted indications have no supporting evidence.

**To proceed, the following is needed:**
- Retrieve the published or registry results of NCT01820559 (primary endpoint, dose response, tolerability) to see whether the Phase 2 trial showed a benefit
- Obtain the Indian package insert (warnings, contraindications, approved indications)
- Obtain mechanism of action data from DrugBank to support the mechanistic-link analysis
- If the Phase 2 result is positive, plan confirmatory Phase 3 evidence and a review of the drug interaction profile (particularly CNS depressants and opioids)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

