---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "Flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In India: at least 20 listed products"
---

# Flurbiprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Flurbiprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID) that is marketed in India in oral tablet and ophthalmic forms.
The TxGNN model predicts it may be related to **acromesomelic dysplasia, Hunter-Thompson type**, but the prediction is supported by **0 clinical trials** and **0 publications**, so it remains a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for flurbiprofen: "Flurbiprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of flurbiprofen, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763), label version 2026-10-05; accessed 2026-11-19.) Flurbiprofen belongs to the NSAID class, which acts mainly by inhibiting cyclooxygenase (COX) enzymes and reducing inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway. No plausible mechanism is known by which COX inhibition would modify this disease. The high TxGNN score (0.9999) is a computational prediction based on network proximity to other skeletal phenotypes, not on clinical or laboratory findings.

At most, an NSAID might relieve secondary joint pain, which would be symptomatic relief rather than treatment of the underlying disorder. No data compiled for this report support even that use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 licences are recorded, all valid, and this list may be partial. None of the records carries approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4457 | Aflur Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 8562 | Aroflur Eye Drop | Bottle of 5 ml Ophthalmic Solution | Valid |
| 29833 | Bellflur Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 77341 | Eyeflur Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 84289 | Flur Ophthalmic Solution | Packet of 10 ml Ophthalmic Solution | Valid |
| 84393 | Flubigat Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 88294 | Flufen Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 89879 | Flugati Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 91149 | Flurac Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 97440 | Gatifax F Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 97660 | Gatidrops FP Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 97695 | Gaticon-F Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 124151 | Lufen Eye Drop | Packet of 5 ml Ophthalmic Solution | Valid |
| 127186 | Lumat Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 136158 | Migrid 10mg Tablet | Strip of 10 tablets | Valid |
| 139138 | Migrid 5mg Tablet | Strip of 10 tablets | Valid |
| 164804 | Ocuflur Eye Ointment | Tube of 5 gm Eye Ointment | Valid |
| 166621 | Ocupen 0.03% Eye Drop | Bottle of 5 ml Ophthalmic Solution | Valid |
| 178957 | Proflur Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 227070 | Tofler Eye Drop | Packet of 5 ml Eye Drop | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 352 interactions are recorded. Examples rated Moderate include acetylsalicylic acid, hydrocortisone, dexamethasone, metformin, glimepiride, and mesalazine. Examples rated Minor include famotidine, cimetidine, and linaclotide.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for this disease, and no plausible mechanism links COX inhibition to the underlying genetic defect.

**To proceed, the following is needed:**
- Any preclinical or clinical study directly addressing this disease
- Mechanism of action data and a credible biological rationale
- Package insert warnings and contraindications for the relevant formulations
- Assessment of whether the available oral and ophthalmic routes suit any proposed use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

