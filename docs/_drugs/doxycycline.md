---
layout: default
title: Doxycycline
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Doxycycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bronchitis, acne, bacterial pneumonia, anthrax…"
monitor_inn: "Doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
---

# Doxycycline
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

## Doxycycline: From Bacterial Infections (Bronchitis, Acne, Pneumonia) to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Doxycycline is a tetracycline-class antibiotic. It is used for bronchitis, bacterial pneumonia, acne, anthrax, gonorrhoea and a range of other bacterial infections.
The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**.
Evidence is thin: **no clinical trials** and **1 publication** (a 1992 case report) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, acne, bacterial pneumonia, anthrax, gonorrhoea and other bacterial infections (from the knowledge-graph indication list; no approved-indication text is recorded for the Indian licences) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxycycline: "Doxycycline inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit. Doxycycline has bacteriostatic activity against a broad range of Gram-positive and Gram-negative bacteria." ([DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8), label version 2026-07-09; accessed 2026-11-19.) Based on known information, doxycycline is a broad-spectrum tetracycline antibiotic. Its efficacy in bacterial infections, including those caused by *Chlamydia trachomatis*, is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

Persistent superficial punctate keratitis can follow chlamydial follicular conjunctivitis, an infection doxycycline treats. Doxycycline is also known for anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects that could help the ocular surface. This benefit is inferred, not demonstrated.

The only supporting report describes keratitis that appeared *after* the infection was treated with oral tetracycline or doxycycline. That is indirect evidence, and it does not show that doxycycline treats the keratitis itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and the follicles resolved. Both then developed recurrent, bilateral punctate epithelial keratitis, and one had anterior stromal edema. |

## India Market Information

Twenty doxycycline licences are valid, and none are cancelled. Oral tablets and capsules and injectable vials are all available. The licence records do not include approved-indication text.

<!-- review:begin in-lic-20261124c-doxycycline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty single-ingredient doxycycline licences are valid, and none are cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-doxycycline-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6971 | Andoxy 100mg Injection | Vial of 1 Injection | Valid |
| 11519 | Avidox 100mg/100mg Tablet | Strip of 10 tablets | Valid |
| 13789 | Amdoxy Capsule | Strip of 10 capsules | Valid |
| 40898 | Codo Capsule | Strip of 10 capsules | Valid |
| 58835 | Doxicip LB Capsule | Strip of 10 capsules | Valid |
| 59114 | Doxivent LB 100mg Capsule | Strip of 10 capsules | Valid |
| 59833 | Doxytab 100mg Tablet | Strip of 8 tablets | Valid |
| 59902 | Doxymiz SL 100mg Capsule | Strip of 10 capsules | Valid |
| 60395 | Doxyguard 100mg Injection | Vial of 1 Injection | Valid |
| 60571 | Doxypro LB 100mg Capsule | Strip of 10 capsules | Valid |
| 62309 | Doxiheal 100 Capsule | Strip of 10 capsules | Valid |
| 67415 | Doxberry 100mg Tablet | Strip of 8 tablets | Valid |
| 68326 | Dcyline 100mg Injection | Vial of 1 Injection | Valid |
| 69735 | Doxsom 100mg Injection | Vial of 1 Injection | Valid |
| 74161 | Emdox 100mg Capsule | Strip of 10 capsules | Valid |
| 116739 | Kivodox LB 100mg Capsule | Strip of 10 capsules | Valid |
| 150457 | Nixidox Capsule | Strip of 10 capsules | Valid |
| 178608 | Pydox 100mg Tablet | Strip of 10 tablets | Valid |
| 201246 | Skidox-LB Capsule | Strip of 10 capsules | Valid |
| 238283 | Vdoux Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (knowledge-graph disease associations, not label text)**: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and dyskinesia of the esophagus.
- **Drug Interactions**: 471 interactions are recorded. Major-level examples include **isotretinoin**, **acitretin** and **aminolevulinic acid**. Moderate-level examples include aluminum hydroxide, aminophylline, amoxicillin, ampicillin and bedaquiline.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only evidence is a single 1992 case report that describes keratitis after an infection, not a response to doxycycline. No trials exist, and the mechanistic link is inferred.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications for Indian-market products, which are required for safety screening
- Controlled clinical evidence (trials or well-designed studies) of doxycycline in punctate epithelial keratoconjunctivitis
- A clear route and formulation rationale for ocular use, since the Indian products are oral and injectable

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

