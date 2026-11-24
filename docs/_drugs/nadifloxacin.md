---
layout: default
title: Nadifloxacin
parent: Model Prediction Only (L5)
nav_order: 575
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Nadifloxacin: predicted new indication Malaria (evidence level L5). Approved use: Acne"
monitor_inn: "Nadifloxacin"
predicted_indications: ["malaria"]
---

# Nadifloxacin
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

## Nadifloxacin: From Acne to Malaria
{: .text-alpha }

## One-Sentence Summary

Nadifloxacin is a topical fluoroquinolone antibacterial originally used to treat acne.
The TxGNN model predicts it may be effective for **malaria**, but **no clinical trials and no publications** currently support this prediction.
It is a model-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne |
| Predicted New Indication | Malaria |
| TxGNN Prediction Score | 0.9916 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, nadifloxacin is a topical fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in acne is attributed to its antibacterial action.

A theoretical link to malaria exists: *Plasmodium* has a gyrase located in its apicoplast, which could in principle be a target for quinolones. However, this is a hypothesis with no supporting activity data. The very high TxGNN score (0.9916) reflects a model prediction only.

A major unresolved concern is route of administration. Nadifloxacin is marketed only as topical products (cream, gel, ointment, dusting powder), and achieving systemic antimalarial exposure with these forms is doubtful. Malaria is a bloodstream infection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

All 20 registrations are valid products. Approved indication text is not available in the data compiled for this report.

<!-- review:begin in-lic-20261124-nadifloxacin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-nadifloxacin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 5186 | Acnevent Forte Cream | Tube of 10 gm Cream | Valid |
| 150606 | Nadibact Gel | Tube of 10 gm Gel | Valid |
| 150775 | Nadoxin-A Gel | Tube of 15 gm Gel | Valid |
| 150776 | Nadoxin Ointment | Tube of 5 gm Ointment | Valid |
| 150943 | Nadifa Cream | Tube of 10 gm Cream | Valid |
| 151528 | Nadimax Cream | Tube of 15 gm Cream | Valid |
| 152494 | Ncp Cream | Tube of 15 gm Cream | Valid |
| 152518 | Nadix 1% Cream | Tube of 15 gm Cream | Valid |
| 152547 | Nodix 1% Gel | Tube of 10 gm Gel | Valid |
| 152717 | Nadimin Ointment | Tube of 10 gm Ointment | Valid |
| 152987 | Nadiwin 1% Cream | Tube of 15 gm Cream | Valid |
| 152994 | Nadimin Plus Cream | Tube of 10 gm Cream | Valid |
| 153155 | Nadicin C 10mg/500mcg Cream | Tube of 15 gm Cream | Valid |
| 154284 | Nadix C Cream | Tube of 15 gm Cream | Valid |
| 154548 | Nadivin Gel | Tube of 15 gm Gel | Valid |
| 154906 | Nadiskin Cream | Tube of 10 gm Cream | Valid |
| 155357 | Nadikem Cream | Tube of 20 gm Cream | Valid |
| 156062 | Nadoxin 1% Dusting Powder | Packet of 10 gm Dusting Powder | Valid |
| 215775 | Triclear N Gel | Tube of 20 gm Gel | Valid |
| 247027 | Zinderm-AN Gel | Tube of 15 gm Gel | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction rests only on a model score, with no clinical trials or literature. The available products are topical, which makes systemic antimalarial exposure unlikely.

**To proceed, the following is needed:**
- Mechanism of action data for nadifloxacin
- In vitro activity data against *Plasmodium* (and, as secondary candidates, *Leishmania* and *Borrelia*)
- Pharmacokinetic evidence on whether therapeutic systemic exposure is achievable, or a feasibility assessment for a non-topical formulation
- Package insert warnings and contraindications from the Indian regulatory source
- A systematic literature and trial search for malaria and the other top-ranked predicted indications

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

