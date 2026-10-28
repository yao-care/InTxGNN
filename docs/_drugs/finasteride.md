---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Finasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Finasteride: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride is a 5-alpha-reductase inhibitor originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 registered clinical trials** and only **4 publications**, all of which are narrative reviews or a methods paper rather than direct efficacy evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

*Note: The top-ranked prediction by TxGNN score is Ambras type hypertrichosis universalis congenita (0.9999), but it has no trials or literature (L5). Hypertrichosis is presented here because it is the highest-ranked prediction with any supporting literature.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, finasteride inhibits type II (and III) 5-alpha-reductase, which blocks the conversion of testosterone to dihydrotestosterone (DHT). This is the basis for its use in BPH, and it is also widely used for male pattern hair loss.

The mechanistic fit with hypertrichosis is only partial. Hypertrichosis is, by definition, excess hair growth in non-androgen-dependent areas, whereas finasteride acts on androgen-dependent tissue. Any prediction signal may partly reflect overlap with hirsutism (androgen-dependent excess hair growth), which is a different condition. The relationship between the original and new indication is therefore thematic (hair biology and androgen signalling) rather than directly mechanistic.

Other predictions are even weaker. For Ambras syndrome (a congenital condition linked to TRPS1 regulation), dental/periodontal malformation syndromes, Dandy-Walker-related syndromes, isolated hair shaft abnormalities and familial trichomegaly, no plausible DHT-mediated mechanism was identified. For Dandy-Walker-related syndromes, finasteride's concern for male fetal development also makes use unattractive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | Hypertrichosis occurs in non-androgen-dependent areas, unlike hirsutism; adult causes are mostly drug-induced, metabolic, nutritional or paraneoplastic |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Overview of new treatments for androgenetic alopecia and hirsutism, including oral therapy for male pattern hair loss |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods/Instrument | Der Hautarzt | TrichoScan digital hair analysis tool for measuring hair density, diameter and growth |

None of these publications directly demonstrates finasteride efficacy in hypertrichosis.

## India Market Information

Finasteride has 20 valid single-ingredient registrations in India, all oral tablets. Approved indication text is not available for these registrations. The main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84119 | Finast Tablet (Dr Reddy's Laboratories Ltd) | Strip of 30 tablets | Not specified |
| 85730 | Finabald 5mg Tablet (East West Pharma) | Strip of 10 tablets | Not specified |
| 87493 | Fistide 5mg Tablet (Samarth Life Sciences Pvt Ltd) | Strip of 10 tablets | Not specified |
| 86672 | Feelal 1mg Tablet (Synnove Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not specified |
| 88910 | Findil 1mg Tablet (Daksh Pharma Pvt Ltd) | Strip of 10 tablets | Not specified |

## Safety Considerations

- **Contraindications (knowledge-graph based, not label text)**: Liver disease and gallbladder disease.
- **Drug Interactions**: 321 potential interactions were identified, but the severity level is unclassified for all of those retrieved. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin and morphine.
- **Other considerations**: Finasteride raises a teratogenicity concern for male fetal development.

Please refer to the package insert for full warnings, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, and the only literature consists of narrative reviews and a methods paper. Hypertrichosis is by definition androgen-independent, so the mechanistic fit is weak. Evidence is indirect (L4 at best, L5 for all other predictions).

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Direct clinical evidence of finasteride in hypertrichosis, separate from hirsutism, such as case series or controlled studies
- Severity classification for the drug interactions
- Evaluation of whether hirsutism would be a more suitable target indication than hypertrichosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

