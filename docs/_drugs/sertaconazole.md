---
layout: default
title: Sertaconazole
parent: Model Prediction Only (L5)
nav_order: 769
evidence_level: L5
indication_count: 3
monitor_inn: "Sertaconazole"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease", "pityriasis versicolor"]
last_modified_at: 2026-10-23
description: "Sertaconazole: predicted new indication Ectothrix infectious disease (evidence level L5). Approved use: Tinea pedis"
---

# Sertaconazole
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

## Sertaconazole: From Tinea Pedis to Ectothrix Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Sertaconazole is a topical imidazole antifungal whose recorded original use is tinea pedis (a relation in the knowledge graph).
The TxGNN model predicts it may be effective for **ectothrix infectious disease**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model score and mechanistic plausibility alone.
Two related predictions were also generated: endothrix infectious disease (no direct evidence) and pityriasis versicolor (1 small 1992 clinical study plus several reviews).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis (relation recorded in the knowledge graph; the licence records provide no approved indication text) |
| Predicted New Indication | Ectothrix infectious disease |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | at least 20 |
| Number of Approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for the original record is not available. Sertaconazole is, however, a known imidazole antifungal. This class inhibits fungal ergosterol synthesis (lanosterol 14-alpha-demethylase), and sertaconazole's benzothiophene ring may add direct membrane-disrupting effects.

Ectothrix infection is a dermatophyte infection of the hair (tinea capitis, typically *Microsporum* or *Trichophyton* species), in which spores form on the outside of the hair shaft. Tinea pedis is caused by the same broad group of fungi, so activity against these organisms is biologically plausible.

The main limitation is delivery. Hair-shaft and follicular infections are poorly reached by topical products, and treatment guidelines generally favour systemic therapy. The high TxGNN score is a computational prediction only. Closely related is endothrix infection (score 0.9956), with the same mechanistic reasoning and the same penetration limitation.

The third prediction, **pityriasis versicolor** (score 0.9945), is better supported. It is caused by *Malassezia* yeasts in the stratum corneum, a superficial and topically accessible target. One caution is that the literature describes sertaconazole as already used for this condition in some regions, so the repurposing novelty is limited. Because the evidence for it sits in a different disease from the headline prediction, it is described separately below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ectothrix infectious disease (and none for endothrix infectious disease or pityriasis versicolor).

---

## Literature Evidence

There is currently no related literature for ectothrix or endothrix infectious disease. The publications below concern the third prediction, pityriasis versicolor, and related superficial mycoses.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1627203](https://pubmed.ncbi.nlm.nih.gov/1627203/) | 1992 | Clinical study (randomized, parallel, double-blind per abstract; 21 patients) | Arzneimittel-Forschung | Sertaconazole 1% cream compared with a second treatment in 21 patients with pityriasis versicolor; efficacy and safety assessed |
| [19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) | 2009 | Review | Drugs | Sertaconazole use in superficial mycoses in dermatology and gynaecology; indicated in the EU for several dermatophytoses, pityriasis versicolor and others, and in the US for tinea pedis only |
| [15954850](https://pubmed.ncbi.nlm.nih.gov/15954850/) | 2005 | Review | Expert Rev Anti Infect Ther | Updated review of topical sertaconazole; in vitro activity and clinical experience in dermatophytosis and tinea versicolor |
| [25968082](https://pubmed.ncbi.nlm.nih.gov/25968082/) | 2015 | Review | Der Hautarzt | Update on cutaneous *Malassezia* infections, including pityriasis versicolor (general background) |
| [23546772](https://pubmed.ncbi.nlm.nih.gov/23546772/) | 2013 | Clinical study | Mycopathologia | Sertaconazole 2% cream in diaper dermatitis candidiasis (indirect evidence, different condition) |
| [26135513](https://pubmed.ncbi.nlm.nih.gov/26135513/) | 2015 | Formulation/preclinical study | Nanomedicine (London) | Nanovesicle antifungal formulation with penetration enhancer in skin fungal disease (indirect evidence) |

---

## India Market Information

At least 20 licences are on record, all valid single-ingredient products (the list may be partial). No approved indication text is recorded in these licence entries. The five main entries are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 207184 | Sernaz V1 Tablet VT | Strip of 1 Tablet VT | Not recorded |
| 204300 | Sertalin Cream | Tube of 30 gm Cream | Not recorded |
| 202939 | Seriva 2% Lotion | Bottle of 30 ml Lotion | Not recorded |
| 74534 | Episert Cream | Tube of 20 gm Cream | Not recorded |
| 136020 | Mycoclin Lotion | Bottle of 20 ml Lotion | Not recorded |

Most products are topical creams or lotions, which matters for hair-shaft infections that usually need systemic treatment.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications are recorded.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ectothrix prediction has no supporting trials or publications, so its evidence level is L5. Topical sertaconazole is also unlikely to reach infected hair shafts adequately. The pityriasis versicolor prediction has more support but is a different disease and is possibly already covered by existing practice in some regions.

**To proceed, the following is needed:**
- Direct clinical or in vitro data of sertaconazole against ectothrix and endothrix dermatophytes (e.g. *Microsporum*, *Trichophyton*)
- Evidence that a topical or other formulation can adequately penetrate the hair follicle and shaft
- Mechanism of action data and package insert warnings and contraindications for the Indian products
- Confirmation of the design and results of the 1992 pityriasis versicolor study, if that indication is pursued separately
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

