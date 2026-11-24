---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 459
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Strongyloidiasis, onchocerciasis"
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "candida glabrata", "congenital candidiasis", "neonatal candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
---

# Ivermectin
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

## Ivermectin: From Strongyloidiasis and Onchocerciasis to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Ivermectin is an antiparasitic drug originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**,
but **no clinical trials and no supporting publications** are currently available for this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Strongyloidiasis, onchocerciasis |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ivermectin: "In vitro studies using human liver microsomes and recombinant CYP450 enzymes have shown that ivermectin is primarily metabolized by CYP3A4." ([DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd), label version 2024-09-20; accessed 2026-11-19.) Based on known information, ivermectin is an antiparasitic agent that acts on glutamate-gated chloride channels in invertebrates. Its efficacy in strongyloidiasis and onchocerciasis is established.

Candida is a fungus, not an invertebrate parasite, and the data compiled for this report documents no antifungal mechanism for ivermectin. The high score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Other top predictions (esophageal candidiasis, vulvovaginitis, *Candida glabrata*, neonatal candidiasis and others) show the same pattern: high scores, but no supporting studies.

At this stage the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

Publications linked to other predicted indications were reviewed. They do not support a Candida indication:
- PMID [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) (2022, case report) describes disseminated strongyloidiasis after prolonged corticosteroid use, which is the original antiparasitic indication.
- PMID [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) (1999, case report) describes oral ivermectin for crusted scabies in two immunocompromised children, one of whom had chronic mucocutaneous candidiasis. The drug treated the scabies, not the candidiasis.

## India Market Information

Ivermectin is marketed in India with 20 valid registrations. Approved indication text is not available for these products.

<!-- review:begin in-lic-20261124c-ivermectin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Ivermectin is marketed in India with 20 valid single-ingredient registrations." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-ivermectin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6911 | Albetop-Plus Tablet | Strip of 1 Tablet | Valid |
| 7440 | Albentin Syrup | Bottle of 10 ml Syrup | Valid |
| 12433 | Albez I 12mg/400mg Tablet | Strip of 1 Tablet | Valid |
| 13578 | Albicon I 6mg/400mg Chewable Tablet | Strip of 1 Chewable Tablet | Valid |
| 27333 | Benzole Tablet | Strip of 1 Tablet | Valid |
| 28011 | Bentec Plus 6mg/400mg Tablet | Strip of 1 Tablet | Valid |
| 32279 | Benrod I 6mg/400mg Tablet | Strip of 10 tablets | Valid |
| 33104 | Beniv Oral Suspension | Bottle of 10 ml Oral Suspension | Valid |
| 55687 | Covermect 12mg Tablet | Strip of 10 tablets | Valid |
| 71228 | Denben Plus 6mg/400mg Tablet | Strip of 1 Tablet | Valid |
| 81222 | Evrina A Suspension | Bottle of 10 ml Suspension | Valid |
| 108453 | Ivrix 12 Tablet DT | Strip of 10 tablet dt | Valid |
| 109363 | Iverfine 12 Tablet | Strip of 10 tablets | Valid |
| 112821 | Ivermerc 6mg Tablet | Strip of 10 tablets | Valid |
| 127850 | Lovy Tablet | Strip of 1 Tablet | Valid |
| 210684 | Selmectin 12mg Tablet | Strip of 10 tablets | Valid |
| 229205 | Tadzole 6mg/400mg Tablet | Strip of 10 tablets | Valid |
| 236969 | Verito 12 A Chewable Tablet | Strip of 1 Chewable Tablet | Valid |
| 242771 | Worbend Plus Oral Suspension | Bottle of 10 ml Oral Suspension | Valid |
| 247626 | Zen Mectin 12mg Tablet | Strip of 1 Tablet | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease contraindications (knowledge graph):** loiasis and filariasis are listed as contraindicated conditions. This comes from knowledge graph relationships, not from package insert text.
- **Drug Interactions:** 100 interactions were identified. Moderate-level interactions include:
  - Warfarin
  - Dicoumarol
  - Clarithromycin
  - Aprepitant
  - Cobicistat
  - Deferasirox
  - Ethanol
  - Fostamatinib
  - Iodide I-123 and I-131
  - Abametapir (topical)

  Several others (for example omeprazole, lansoprazole, prednisone, dexamethasone and heparin) are listed with unclassified severity.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score only. There are no clinical trials or relevant publications, and no plausible antifungal mechanism is documented. Effective approved antifungal treatments already exist for candidiasis.

**To proceed, the following is needed:**
- Preclinical data on in vitro activity of ivermectin against *Candida* species
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the India regulator
- Route and formulation compatibility assessment (vaginal or topical versus the currently oral products)
- Safety evaluation for the target population, including women of reproductive age and neonates

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

