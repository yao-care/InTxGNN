---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Pioglitazone"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitizing drug originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pioglitazone: "ACTOS is a thiazolidinedione that depends on the presence of insulin for its mechanism of action. ACTOS decreases insulin resistance in the periphery and in the liver resulting in increased insulin-dependent glucose disposal and decreased hepatic glucose output. […] Pioglitazone is not an insulin secretagogue." ([DailyMed: Actos (pioglitazone) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d2ddc491-88a9-4063-9150-443b4fa4330c), label version 2025-03-28; accessed 2026-11-19.) Based on known pharmacology, pioglitazone is a PPAR-gamma agonist (thiazolidinedione class). Its efficacy in type 2 diabetes is established, where it improves insulin sensitivity.

Opsismodysplasia is caused by INPPL1 mutations (loss of SHIP2 function), which affect PI3K/insulin signaling and chondrocyte maturation. Both conditions touch insulin-related signaling, which may explain the prediction. However, no direct mechanistic link is established, and any connection is speculative. The high score (0.9959) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions show the same pattern: stiff person syndrome and its focal variant (possible immunomodulation), localized lipodystrophies (PPAR-gamma-driven adipogenesis), thiamine-responsive dysfunction syndrome and pancreatic agenesis (both diabetes-related). All are L5 with no supporting trials or literature specific to the indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly addresses opsismodysplasia. The seven publications retrieved belong to the rank 9 prediction (pancreatic agenesis). They concern type 2 diabetes and PPAR agonists in general, so they are indirect at best and are not evidence for the top prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16644631](https://pubmed.ncbi.nlm.nih.gov/16644631/) | 2006 | RCT | Diabetes Care | Muraglitazar vs pioglitazone added to metformin in type 2 diabetes; improved glycaemic control and lipids |
| [20859539](https://pubmed.ncbi.nlm.nih.gov/20859539/) | 2010 | Review | Vasc Health Risk Manag | Pioglitazone plus alogliptin as pathophysiologically sound therapy in type 2 diabetes |
| [23680744](https://pubmed.ncbi.nlm.nih.gov/23680744/) | 2013 | Review | Hosp Pract | Pleiotropic effects of thiazolidinediones, including beta-cell protection |
| [22068250](https://pubmed.ncbi.nlm.nih.gov/22068250/) | 2012 | Review | Endocr Pract | Targeting insulin resistance and beta-cell dysfunction in prediabetes |
| [15892654](https://pubmed.ncbi.nlm.nih.gov/15892654/) | 2005 | Review | Curr Mol Med | Clinical significance of PPAR-gamma agonism |
| [12149047](https://pubmed.ncbi.nlm.nih.gov/12149047/) | 2002 | Review | Drugs | Rosiglitazone use in type 2 diabetes (related thiazolidinedione) |
| [15832493](https://pubmed.ncbi.nlm.nih.gov/15832493/) | 2002 | Review | Treat Endocrinol | Rosiglitazone profile in type 2 diabetes (related thiazolidinedione) |

## India Market Information

Pioglitazone has valid registrations in India (the compiled data hold only part of the list; see the Quick Overview and the table below), including fixed-dose combinations with metformin or glimepiride-type partners. All are oral tablets. Approved indication text is not available in the registration records.

<!-- review:begin in-lic-20261124b-pioglitazone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Pioglitazone has 20 valid registrations in India, all single-ingredient entries according to the data compiled for this report, including combinations with metformin or glimepiride-type partners in product names." Revised: the sentence said the data classify these products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for several of them (they are fixed-dose combinations). Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-pioglitazone-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26819 | Biodib 15 Tablet | Strip of 10 tablets | Valid |
| 32319 | Betapride 30mg Tablet | Strip of 10 tablets | Valid |
| 32934 | Bioglita M 30 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 48336 | Carbophage P 30mg/500mg Tablet | Strip of 10 tablets | Valid |
| 97537 | Glitaz 30mg Tablet | Strip of 10 tablets | Valid |
| 99480 | G Tase 30mg Tablet | Strip of 10 tablets | Valid |
| 100065 | Glitanel Plus 15mg/500mg Tablet | Strip of 10 tablets | Valid |
| 100286 | Glyciphage P 7.5 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 101571 | Glizone 30mg Tablet | Strip of 10 tablets | Valid |
| 102012 | Glita M 15 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 136884 | Mysensi M Forte 15mg/1000mg Tablet ER | Strip of 10 tablet er | Valid |
| 140470 | Mysensi M 15mg/500mg Tablet ER | Strip of 10 tablet er | Valid |
| 175035 | Pionorm-M 15 Tablet SR | Strip of 10 tablet sr | Valid |
| 176353 | Piorun 7.5mg Tablet | Strip of 10 tablets | Valid |
| 176905 | Path 15 Tablet | Strip of 15 tablets | Valid |
| 177054 | Pozitiv 15mg Tablet | Strip of 10 tablets | Valid |
| 177190 | Piolee 7.5mg Tablet | Strip of 10 tablets | Valid |
| 182814 | Piotrust 15mg Tablet | Strip of 10 tablets | Valid |
| 239711 | Vedapride-P 7.5mg/1mg Tablet | Strip of 10 tablets | Valid |
| 241866 | Wonglita Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, congestive heart failure, adrenocortical insufficiency/Addison disease, thymus gland disease, infectious disease, and a large group of pituitary deficiency and hypogonadotropic hypogonadism conditions (including Kallmann syndrome and Sheehan syndrome).
- **Drug Interactions:** 603 interactions were identified in total. Examples at the moderate level include abiraterone, acetazolamide, hydrochlorothiazide, epinephrine, salbutamol, formoterol, pseudoephedrine, phenylephrine, hydrocortisone, ethanol and alpelisib. Examples at the minor level include nifedipine, ethinylestradiol and lipoic acid.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for opsismodysplasia rests solely on a model score, with no clinical trials, no literature, and no established mechanistic link. The knowledge-graph contraindication signals (heart failure, liver and kidney disease) also need review in a rare pediatric skeletal disorder.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data for pioglitazone (e.g., from DrugBank)
- Preclinical or mechanistic studies testing PPAR-gamma modulation in INPPL1/SHIP2-deficient models
- A targeted literature search specific to opsismodysplasia
- Review of lower-ranked predictions (e.g., lipodystrophy forms) as possibly more biologically plausible alternatives, each also requiring supporting evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Actos (pioglitazone) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d2ddc491-88a9-4063-9150-443b4fa4330c) |
| 2026-11-24 | Revised: the single-ingredient classification | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

