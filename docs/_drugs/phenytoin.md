---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including generalized tonic-clonic seizures…"
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
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

# Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is a sodium channel-blocking antiseizure drug, originally used for epilepsy, including generalized tonic-clonic seizures, partial epilepsy and status epilepticus.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no clinical trials** and **only 2 loosely related publications**, neither of which concerns a neoplasm.
The more credible signal in the list is the related condition **trigeminal neuralgia** (rank 9), which has a body of observational and review literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including generalized tonic-clonic seizures, partial epilepsy, status epilepticus) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, phenytoin blocks voltage-gated sodium channels in a use-dependent manner, which limits repetitive neuronal firing and seizure spread. Its efficacy in epilepsy is well established.

For trigeminal nerve neoplasm, the prediction is **not mechanistically convincing**. The high score most likely reflects graph proximity to trigeminal neuralgia and seizure-related nodes, not any anti-tumour activity. Sodium channel blockade may relieve nerve-related pain, but there is no plausible route by which it would treat a neoplasm itself. The two retrieved papers concern trigeminal neuralgia treatment and Sturge-Weber syndrome, not neoplasms.

The data compiled for this report show a more meaningful picture among the other predictions:
- **Trigeminal neuralgia (rank 9, evidence level L3):** Ectopic, hyperexcitable firing of trigeminal afferents is the same sodium channel mechanism targeted by carbamazepine and phenytoin. Phenytoin appears to be a second-line or rescue option, with carbamazepine and oxcarbazepine as first-line.
- **Reflex seizure types (ranks 2-4, 6-8):** These include orgasm-, micturition-, thinking-, audiogenic, startle and reading seizures. They are sub-phenotypes of the already approved epilepsy indication rather than true repurposing, and direct evidence is sparse.
- **Beta-ketothiolase deficiency (rank 10):** No known mechanistic link and no evidence. The score is likely a graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, trigeminal nerve neoplasm. No registered trials were retrieved for any of the other nine predicted indications either.

## Literature Evidence

**Top-ranked prediction (trigeminal nerve neoplasm)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; concerns neuralgia, not neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 Sturge-Weber syndrome cases, reviewing clinical characteristics and therapeutic response |

**Most relevant related prediction (trigeminal neuralgia)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology recommendations for trigeminal neuralgia management |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Res | Appraises phenytoin and carbamazepine in trigeminal neuralgia: marketing-based versus evidence-based treatment |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Clinical study | Cephalalgia | Retrospective analysis of 144 cases of IV lacosamide and phenytoin for acute trigeminal neuralgia exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Retrospective cohort | Headache | Responses to IV phenytoin as rescue treatment in trigeminal neuralgia crisis |
| [22592741](https://pubmed.ncbi.nlm.nih.gov/22592741/) | 2012 | Cochrane review | Cochrane Database Syst Rev | Phenytoin for neuropathic pain and fibromyalgia in adults; notes occasional use in intractable trigeminal neuralgia |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Overview of trigeminal neuralgia from pathophysiology to pharmacological treatment |
| [11803299](https://pubmed.ncbi.nlm.nih.gov/11803299/) | 2002 | Review | Clin J Pain | Carbamazepine is supported by controlled trials; other agents have only small trials or uncontrolled observations |

## India Market Information

A total of 20 valid single-ingredient registrations were found, with no cancelled licences. The approved indication text is not available in the compiled data. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 182325 | Phalin 300mg Tablet | Strip of 10 tablets | Not available |
| 74300 | Epsotal Tablet | Bottle of 100 tablets | Not available |
| 72821 | Epsolin ER 300 Tablet | Bottle of 30 extended-release tablets | Not available |
| 212388 | Stoin 50mg Suspension | Bottle of 200 ml suspension | Not available |
| 79626 | Epsod Injection | Vial of 2 ml injection | Not available |

Available forms include oral tablets, extended-release tablets, an oral suspension and injectables.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

Additional information that was available:

- **Conditions flagged as contraindicated in the knowledge graph (not label text):** long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, porphyria, thrombocytopenia, neutropenia and agranulocytosis, hyperglycaemia, diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus, hypotensive disorder, hepatic coma and encephalopathy, sleep apnoea syndromes, anxiety and neurotic disorders, and substance abuse or dependence.
- **Drug interactions:** 390 interactions were recorded. Examples at Moderate level include acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, metformin, pioglitazone, bupropion, aprepitant, morphine, omeprazole, metronidazole, cholecalciferol and calcifediol. Acetylsalicylic acid is Minor.
- **Adverse events seen in the retrieved literature (case-level):** thrombocytopenia, hyperglycaemia and diabetic ketoacidosis, ophthalmoplegia at high serum levels, peripheral neuropathy, gingival hyperplasia, and EMPACT syndrome (erythema multiforme with cranial radiation).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (trigeminal nerve neoplasm) has no trials, no relevant literature and no plausible anti-tumour mechanism, so it is a model score without support (L5). The nearest credible signal is trigeminal neuralgia, where phenytoin is a second-line or rescue option supported by limited observational evidence (L3). Even there, it is best treated as a research question rather than a Go.

**To proceed, the following is needed:**
- Do not pursue trigeminal nerve neoplasm unless independent biological evidence emerges. Consider redirecting the programme to trigeminal neuralgia.
- For trigeminal neuralgia, confirm the study design of PMID 35469475 and the guideline position on phenytoin, and compare against first-line carbamazepine and oxcarbazepine.
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening).
- Mechanism of action data from DrugBank.
- Approved indication text for the Indian registrations.
- Route compatibility assessment, since oral and injectable forms are marketed but required routes for any new indication are not yet defined.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

