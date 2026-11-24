---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-24
description: "Amoxicillin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Relations recorded in the knowledge graph: urinary tract infection…"
---

# Amoxicillin
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

## Amoxicillin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic used in infections such as urinary tract infection, otitis media, pneumonia and pharyngitis.
The TxGNN model predicts it may be useful for **hyperamylasemia**, but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph: urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, pharyngitis (no approved indication text is available in the local licence records) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for amoxicillin: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), label version 2026-11-13; accessed 2026-11-19.) Amoxicillin is known as a beta-lactam antibiotic that blocks bacterial cell wall synthesis, and its use in bacterial infections is recorded in the knowledge graph.

Based on the data compiled for this report, no plausible mechanistic link to hyperamylasemia could be identified. Amoxicillin has no known action on amylase regulation or on pancreatic or salivary enzyme release. The high score (rank 6778 in the model) is a network-based prediction and should be treated as a hypothesis only, not as a reasoned repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

The local records list 20 valid licences (the total is at least 20, so the list may be partial). No approved indication text is recorded for any of them.

<!-- review:begin in-lic-20261124c-amoxicillin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The local records list 20 valid licences for single-ingredient products (the total is at least 20, so the list may be partial)." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-amoxicillin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1386 | Almox DT 125 Tablet | Strip of 10 tablet dt | Valid |
| 28756 | Beniclav 625 Tablet | Strip of 6 tablets | Valid |
| 43337 | Clas Capsule | Strip of 10 capsules | Valid |
| 50892 | Cureclav Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 51119 | Caprimox DT 250mg Tablet | Strip of 10 tablet dt | Valid |
| 77966 | Emcillin CV 500mg/125mg Tablet | Strip of 6 tablets | Valid |
| 83683 | EEshmox DX 250mg/250mg Capsule | Strip of 10 capsules | Valid |
| 99169 | Grandmox 375mg Tablet | Strip of 10 tablets | Valid |
| 100537 | Gesclav 500mg/125mg Tablet | Strip of 10 tablets | Valid |
| 107460 | HB Clav DX 250mg/250mg Capsule | Strip of 10 capsules | Valid |
| 131138 | Lenoxy 1000mg/200mg Injection | Vial of 20 ml Injection | Valid |
| 139442 | Monoclav 500 mg/125 mg Tablet | Strip of 10 tablets | Valid |
| 147011 | Moxpil 250mg Tablet DT | Strip of 10 tablet dt | Valid |
| 147390 | Moxiket CV 500mg/125mg Tablet | Strip of 6 tablets | Valid |
| 148810 | Moxydak-CV Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 156737 | Nimclav 625mg Tablet | Strip of 6 tablets | Valid |
| 196459 | Raziclav 500 mg/125 mg Tablet | Strip of 10 tablets | Valid |
| 198322 | Rotfic Capsule | Strip of 10 capsules | Valid |
| 208211 | Stamclav LB 500mg/125mg Tablet | Strip of 10 tablets | Valid |
| 240479 | Voxiclav 500mg/125mg Tablet | Strip of 6 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Other available forms include an injection (vial of 20 ml), an oral suspension and a dry syrup.

## Safety Considerations

- **Drug Interactions**: 271 interactions were recorded. Major-level examples include methotrexate and the live cholera vaccine (Vibrio cholerae CVD 103-HgR strain). Moderate-level examples include doxycycline, minocycline, ethinylestradiol, estradiol, mycophenolate mofetil, entecavir and anticoagulants such as dicoumarol and anisindione.
- **Relations recorded in the knowledge graph as contraindications** (not label text): long QT syndrome, torsades de pointes, liver failure and liver disease, kidney disease, porphyria, cholestasis, myasthenia gravis, Clostridium difficile colitis, ventricular tachycardia, osteoporosis, bone fracture, and infectious mononucleosis. These should be checked against the package insert.

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or publications address hyperamylasemia, and no plausible mechanism links amoxicillin to this condition. The evidence level is therefore L5.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for amylase elevation, and mechanism-of-action data for amoxicillin
- Any clinical or preclinical study that directly examines hyperamylasemia
- Package insert warnings and contraindications for the marketed products
- Review of the other predicted indications. Septicemic plague is biologically plausible for an antibacterial, but its evidence is limited to preclinical, in vitro and case-level data, and beta-lactams are not first-line agents for plague.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

