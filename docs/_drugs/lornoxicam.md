---
layout: default
title: Lornoxicam
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 8
monitor_inn: "Lornoxicam"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "tendinitis", "myositis fibrosa"]
last_modified_at: 2026-11-24
description: "Lornoxicam: predicted new indication Migraine disorder (evidence level L5). In India: at least 20 listed products"
---

# Lornoxicam
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

## Lornoxicam: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Lornoxicam is a nonsteroidal anti-inflammatory drug (NSAID) of the oxicam class that is marketed in India.
The TxGNN model predicts it may be effective for **migraine disorder**.
The evidence is thin: **1 completed Phase 2 trial** has no published or posted results, and the **2 publications** are reviews, so the evidence level is **L5**.

<!-- review:begin in-lic-20261124c-lornoxicam-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Lornoxicam is a nonsteroidal anti-inflammatory drug (NSAID) of the oxicam class that is marketed in India as single-ingredient products." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-lornoxicam-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lornoxicam inhibits both COX-1 and COX-2, which reduces prostaglandin synthesis. Detailed mechanism of action data is not available in the data compiled for this report, so this description reflects the general pharmacology of the drug class.

Prostaglandins contribute to neurogenic inflammation and trigeminovascular sensitization, which are central to migraine attacks. NSAIDs as a class are an established acute migraine therapy, so the mechanism is biologically plausible for lornoxicam.

This is a class-level rationale only. No published study tests lornoxicam itself in migraine, which is why the evidence level stays at L5 despite the high model score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00293657](https://clinicaltrials.gov/study/NCT00293657) | Phase 2 | Completed | 150 | Randomized, double-blind, placebo-controlled single-dose study of intravenous lornoxicam (8 mg or 16 mg) versus placebo for moderate or severe headache during an acute migraine attack. Completed in 2006 with no published or posted results. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1495823](https://pubmed.ncbi.nlm.nih.gov/1495823/) | 1992 | Review | Pathologie-biologie | Reviews controlled studies of NSAIDs for acute and preventive migraine treatment. Lornoxicam is among the many NSAIDs listed. |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Review | Drugs | Reviews the pharmacology and therapeutic potential of lornoxicam in painful and inflammatory conditions. It is not a migraine-specific study. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 71073 | D Carnox P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 71611 | Durnox P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 85223 | Flexilor P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 125263 | Lorni Plus Tablet | Strip of 10 tablets | Valid |
| 125630 | Lornigesic P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 126265 | Lornem P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 126438 | Lodol 4mg Tablet | Strip of 10 tablets | Valid |
| 127600 | Lorbax P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 127730 | Lorelax P 4mg/325mg Tablet | Strip of 10 tablets | Valid |
| 129953 | Loxica XP 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 130013 | Lorniflex Plus 8 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 130030 | Lonexi P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 130140 | Lorchek-P Tablet | Strip of 10 tablets | Valid |
| 131425 | Lornoviz-P Tablet | Strip of 10 tablets | Valid |
| 131888 | Lornok 8mg Tablet | Strip of 10 tablets | Valid |
| 132637 | Lormyp 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 133076 | Loristar P 8mg/325mg Tablet | Strip of 10 tablets | Valid |
| 222411 | Trois CX Tablet | Strip of 10 tablets | Valid |
| 232371 | Univer 4mg Tablet | Strip of 10 tablets | Valid |
| 250889 | Zoloxy 8mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

At least 20 valid licences are on record, and the list may be partial.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high. However, the only trial in migraine (NCT00293657) has no published or posted results, and the available publications are reviews. No published study therefore tests lornoxicam in migraine, and the evidence level is L5.

**To proceed, the following is needed:**
- Results of NCT00293657, or a new controlled trial of lornoxicam in migraine
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian licences
- Confirmation of the approved indication text on the local licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

