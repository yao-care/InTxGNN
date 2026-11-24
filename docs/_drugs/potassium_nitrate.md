---
layout: default
title: Potassium Nitrate
parent: Model Prediction Only (L5)
nav_order: 692
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Potassium Nitrate: predicted new indication Meningococcal infection (evidence level L5). Approved use: Not recorded"
monitor_inn: "Potassium nitrate"
drugbank_id: DB11090
predicted_indications: ["meningococcal infection", "sclerosing cholangitis"]
---

# Potassium Nitrate
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

## Potassium Nitrate: From Dental Hypersensitivity Products to Meningococcal Infection
{: .text-alpha }

## One-Sentence Summary

Potassium nitrate is marketed in India as an ingredient in dental gels and toothpastes. The TxGNN model predicts it may be effective for **meningococcal infection**, but **no clinical trials and no publications** currently support this prediction. It rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the registrations) |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the registrations, potassium nitrate is a single-ingredient component of oral-care products (dental gels and toothpastes) in India. No original indication is recorded for it.

One speculative rationale is that potassium nitrate is an inorganic nitrate salt. It can be reduced to nitrite and then to nitric oxide (NO), and NO and related reactive nitrogen species have general antimicrobial activity. This is not specific to *Neisseria meningitidis* and is not supported by any data compiled for this report.

Meningococcal infection is an acute, life-threatening invasive disease. It is treated with established antibiotics and prevented by vaccines. A high TxGNN score alone does not justify repurposing a nitrate salt for this condition.

A second prediction, **sclerosing cholangitis** (score 0.9921), also has no clinical trials or literature. Its proposed link, nitrate-derived NO signalling affecting vascular tone, inflammation or biliary epithelial function, is equally unsupported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

There are 20 valid registrations, none cancelled. Approved indication text is not recorded for any of them.

<!-- review:begin in-lic-20261124-potassium_nitrate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "There are 20 valid single-ingredient registrations, with no combination products and none cancelled." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-potassium_nitrate-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 24685 | Arident Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 49011 | Crodent Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 61782 | Dent-X Toothpaste (Medicated) | Tube of 100 gm Toothpaste | Valid |
| 64280 | Daxodent-K Dental Gel | Tube of 50 gm Dental Gel | Valid |
| 64878 | Dentop-K Dental Gel | Tube of 50 gm Dental Gel | Valid |
| 65292 | Dentosmith Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 78529 | EV Fresh Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 97830 | Glistodent Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 99770 | Germifresh Dental Gel | Tube of 80 gm Dental Gel | Valid |
| 117360 | Kyodent Dental Gel | Tube of 50 gm Dental Gel | Valid |
| 151674 | Nitra Gel Mint | Tube of 100 gm Dental Gel | Valid |
| 153930 | Nitrodent-KF Tooth Gel | Tube of 50 gm Dental Gel | Valid |
| 164072 | Orasafe Dental Gel | Tube of 50 gm Gel | Valid |
| 177453 | Pyogin-KF Dental Gel | Tube of 75 gm Dental Gel | Valid |
| 192260 | RA Janseal Toothpaste | Tube of 15 gm Toothpaste | Valid |
| 203370 | Siodent Dental Gel | Tube of 50 gm Dental Gel | Valid |
| 204852 | Sensorax Dental Gel | Tube of 100 gm Dental Gel | Valid |
| 206617 | Sisdent Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 206831 | Sensogate Toothpaste | Tube of 50 gm Toothpaste | Valid |
| 207241 | Simodent Toothpaste | Tube of 50 gm Toothpaste | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (PrimeKG) links potassium nitrate to **dental fluorosis** as a contraindication. This comes from graph edges, not from label text.

No package insert warnings, contraindications or drug interaction data were available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score only (Evidence Level L5). There are no clinical trials or publications, and no mechanism data. Established antibiotic treatment and vaccines exist for meningococcal infection. All current products are topical oral-care formulations, and route compatibility with a systemic infection has not been assessed.

**To proceed, the following is needed:**
- Mechanism of action data for potassium nitrate
- Package insert warnings and contraindications for the marketed products
- Independent preclinical evidence of activity against *Neisseria meningitidis*
- Assessment of route and formulation compatibility with the proposed indication
- Clarification of the dental fluorosis contraindication signal

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

