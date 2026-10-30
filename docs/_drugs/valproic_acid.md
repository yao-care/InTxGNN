---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Valproic Acid: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Valproic Acid
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

## Valproic Acid: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Valproic acid is a broad-spectrum antiseizure drug, originally used for epilepsy, manic episodes of bipolar disorder and absence epilepsy.
This is essentially an extension of its established use to a seizure subtype, rather than a new therapeutic area.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

The first-ranked prediction, trigeminal nerve neoplasm (score 0.9997), was not selected. It has only a single unrelated case series (Sturge-Weber syndrome) and is rated L5 with a Hold recommendation. Visual epilepsy was chosen as the lead indication because it has the strongest supporting evidence among the predictions. Other predictions are summarised below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, valproic acid enhances GABAergic over glutamatergic transmission, blocks sodium channels and modulates T-type calcium channels, which raises the seizure threshold. It also inhibits histone deacetylase, which is of theoretical interest in oncology but not relevant to this indication.

Visual (photosensitive) epilepsy is a reflex seizure type within the generalized epilepsy spectrum, where valproate is already a standard treatment. The prediction therefore fits the drug's known pharmacology well. Support comes from reviews and from a randomized comparison of ethosuximide, valproic acid and lamotrigine in childhood absence epilepsy. That trial concerns a related but different syndrome.

**Other predicted indications (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Trigeminal nerve neoplasm | 0.9997 | L5 | Hold. No clear mechanistic link; the only paper is an unrelated case series |
| 3 | Trigeminal neuralgia | 0.9983 | L4 | Research question. Class-level reviews only; no valproate-specific trials, and not better supported than first-line carbamazepine or oxcarbazepine |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20200383](https://pubmed.ncbi.nlm.nih.gov/20200383/) | 2010 | RCT | N Engl J Med | Compared ethosuximide, valproic acid and lamotrigine as initial treatment in childhood absence epilepsy (a related syndrome, not visual epilepsy) |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Curr Neuropharmacol | Valproic acid remains one of the most efficient antiepileptic drugs; broad actions on ion currents and GABAergic transmission |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Cohort | Future Oncol | Levetiracetam and valproic acid in glioma: antiseizure use and possible antineoplastic effects |
| [37037506](https://pubmed.ncbi.nlm.nih.gov/37037506/) | 2023 | Review | Brain Nerve | Medical treatment of epilepsy, based on recent clinical practice guidelines |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arq Neuropsiquiatr | Diagnosis, monitoring and treatment of status epilepticus |
| [39899098](https://pubmed.ncbi.nlm.nih.gov/39899098/) | 2025 | Review | Continuum | Treatment of first seizures, acute repetitive seizures and status epilepticus |
| [32768086](https://pubmed.ncbi.nlm.nih.gov/32768086/) | 2020 | Review | Handb Clin Neurol | Epilepsy management in pregnancy, including antiseizure medication choice and counseling |
| [26478444](https://pubmed.ncbi.nlm.nih.gov/26478444/) | 2015 | Review | CNS Oncol | Seizures in oligodendroglial tumors |
| [1808081](https://pubmed.ncbi.nlm.nih.gov/1808081/) | 1991 | Review | Indian Pediatr | General review of valproic acid |
| [36994516](https://pubmed.ncbi.nlm.nih.gov/36994516/) | 2023 | Preclinical | J Tradit Chin Med | Dingxian pill combined with valproic acid in a rat chronic epilepsy model |

No publication directly studies visual epilepsy; the evidence is indirect.

## India Market Information

The data compiled for this report list 20 valid single-ingredient registrations. No approved indication text is recorded for any of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 188649 | Raival 500mg Tablet ER | Extended-release tablet | Not recorded |
| 38619 | Convulex 500mg Tablet ER | Extended-release tablet | Not recorded |
| 109837 | Ivalp 750mg Tablet XR | Extended-release tablet | Not recorded |
| 205534 | Soval 500mg Tablet | Tablet | Not recorded |
| 235102 | Valcot 500mg Tablet CR | Controlled-release tablet | Not recorded |

All available forms are oral tablets (standard, ER, XR and CR).

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver disease, pancreatitis, kidney disease, hematologic disease, thrombocytopenia, gallbladder disease, porphyria and other porphyrin metabolism diseases, urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia), cognitive disorder, anxiety disorder, neurotic disorder and dysthymic disorder.
- **Drug interactions:** 248 interactions are recorded. The most serious listed is **glycerol phenylbutyrate (Major)**. Moderate interactions include bupropion, morphine, acetylsalicylic acid, clarithromycin, metoclopramide, diphenoxylate and difenoxin, dronabinol, nabilone and activated charcoal. Minor interactions include cimetidine, esomeprazole and several antacids (magnesium, aluminum and calcium salts).
- **Other concerns from the literature:** teratogenicity in women of reproductive age, hepatotoxicity, and interaction with carbapenem antibiotics.

Package insert warnings and contraindications for the Indian products were not available; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct evidence is lacking, however: there are no trials, and support comes from reviews and a randomized trial in a related syndrome. The guardrails are teratogenicity, hepatotoxicity and the large number of drug interactions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products, which are currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Approved indication text for the Indian registrations, to confirm whether this use is already covered
- Studies directly addressing photosensitive or visually triggered seizures
- A pregnancy and reproductive-age risk management plan
- Review of the 248 recorded drug interactions, prioritising the Major interaction with glycerol phenylbutyrate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

