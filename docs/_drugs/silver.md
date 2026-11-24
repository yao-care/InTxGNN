---
layout: default
title: Silver
parent: Model Prediction Only (L5)
nav_order: 773
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Silver"
predicted_indications: ["bone Paget disease"]
description: "Silver: predicted new indication Bone Paget disease (evidence level L5). In India: 9 listed products (9 not discontinued)"
---

# Silver
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Silver: Bone Paget disease
{: .text-alpha }

## One-Sentence Summary

Silver is marketed in India as a topical antimicrobial in wound and burn products (gels, creams, sprays and liquids).
The TxGNN model predicts it may be effective for **bone Paget disease**, but there are **no registered clinical trials** and the **5 publications** retrieved use silver only as a laboratory staining reagent, not as a treatment.
This prediction is a model output without therapeutic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bone Paget disease |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, silver is used topically in India as an antimicrobial agent in wound and burn products.

The high TxGNN score (0.9967) is not backed by pharmacological evidence. The five retrieved papers mention silver only as a histological stain, for example silver impregnation of bone tissue and staining of nucleolar organizer regions in osteoclasts. None evaluates silver as a therapy. The link appears to be a text-mining artefact of the word "silver" rather than a real treatment relationship.

Other top predictions show the same pattern. Silver appears as a stain, as a toxicant (argyria), as part of the eponym "Silver-Russell syndrome", or as a metaphor ("silver bullets", "silver lining"). Antimicrobial wound-care use is also topical, which makes systemic bone disease an unlikely target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9836854](https://pubmed.ncbi.nlm.nih.gov/9836854/) | 1998 | Histopathology study | Bone | Silver staining (AgNOR) shows increased nucleolar organizer regions in osteoclast nuclei in Paget's disease; silver is used as a stain only |
| [3163726](https://pubmed.ncbi.nlm.nih.gov/3163726/) | 1988 | Imaging study | J Nucl Med | Gallium-67 citrate localizes in osteoclast nuclei of Paget lesions; unrelated to silver therapy |
| [4111887](https://pubmed.ncbi.nlm.nih.gov/4111887/) | 1972 | Histological method | Stain Technology | Silver staining of bone before decalcification to quantify osteoid |
| [2420233](https://pubmed.ncbi.nlm.nih.gov/2420233/) | 1985 | Histological method | Anatomischer Anzeiger | Silver impregnation method for bone tissue |
| [9227338](https://pubmed.ncbi.nlm.nih.gov/9227338/) | 1997 | Laboratory method | J Pathol | Quantification of vitamin D receptor mRNA in tissue sections; limitations of in situ RT-PCR |

None of these studies tests silver as a treatment.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26669 | Burnosept Plus Cream | Tube of 15 gm Cream | Valid |
| 199930 | Silvacure Plus Cream | Tube of 15 gm Cream | Valid |
| 200609 | Silverstream Liquid | Bottle of 100 ml Liquid | Valid |
| 202657 | Silverstream Liquid | Bottle of 250 ml Liquid | Valid |
| 230608 | Unosil 550 Antimicrobial Wound and Burn Gel | Tube of 15 gm Gel | Valid |
| 230841 | Unosil Antimicrobial Wound and Burn Spray | Bottle of 100 ml Solution | Valid |
| 231089 | Unosil 550 Antimicrobial Wound and Burn Gel | Tube of 50 gm Gel | Valid |
| 231127 | Unosil Antimicrobial Wound and Burn Spray | Pump bottle of 50 ml Solution | Valid |
| 231323 | Unosil 550 Antimicrobial Wound and Burn Gel | Jar of 200 gm Gel | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are valid.

<!-- review:begin in-lic-20261106-silver-1 -->

> **Review correction (2026-11-24)**: Originally stated: "There are 9 valid single-ingredient registrations in total; the table lists the first 5." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-silver-1 -->

---

## Safety Considerations

Please refer to the package insert for safety information.

One note from the literature: a case report of systemic argyria (PMID 8063942) describes silver pigment deposition in multiple organs after chronic ingestion of silver compounds. This is a toxicity finding relevant to any systemic use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no therapeutic literature; the papers match only on the word "silver" as a stain.

**To proceed, the following is needed:**
- Mechanism of action data for silver
- Package insert warnings and contraindications from the India regulatory source
- Preclinical evidence that silver has any effect on osteoclast biology or bone remodelling
- Route compatibility assessment (current products are topical or non-systemic; Paget disease needs systemic or bone-targeted exposure)
- Consolidation of the duplicate "bone Paget disease" and "Paget disease of bone" predictions
- Review of other top predictions with the same silver-as-stain artefact before any further evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

