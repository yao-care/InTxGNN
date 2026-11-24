---
layout: default
title: Doripenem
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 5
monitor_inn: "Doripenem"
predicted_indications: ["hepatoportal sclerosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis"]
last_modified_at: 2026-11-24
description: "Doripenem: predicted new indication Hepatoportal sclerosis (evidence level L5). Approved use: Cholecystitis, low phospholipid associated cholelithiasis…"
---

# Doripenem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Doripenem: From Cholecystitis to Hepatoportal Sclerosis
{: .text-alpha }

## One-Sentence Summary

Doripenem is a carbapenem antibiotic. The TxGNN model (deep learning) predicts it may be effective for **hepatoportal sclerosis**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cholecystitis, low phospholipid associated cholelithiasis, pyelonephritis (relations recorded in the knowledge graph; the licence records contain no approved indication text) |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 0.9900 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Number of Approvals | At least 20 registrations (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of doripenem as: Bacterial penicillin-binding protein inhibitor ([ChEMBL CHEMBL491571 (doripenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL491571), CC BY-SA 3.0; accessed 2026-11-19.) Doripenem is a carbapenem antibiotic, a class that works by inhibiting bacterial cell wall synthesis. Its use in the biliary and urinary tract infections recorded in the knowledge graph fits that antibacterial action.

Hepatoportal sclerosis is a non-infectious vascular disorder of the liver that causes noncirrhotic portal hypertension. Nothing in the data compiled for this report supports a mechanistic link between an antibacterial agent and this disease. The high score (0.9900) comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, such as the hepatobiliary original indications (cholecystitis, cholelithiasis), not biological evidence, and it has not been biologically validated.

The same score of 0.9900 was also given by the TxGNN model to four other liver-related conditions: hepatopulmonary syndrome, idiopathic copper-associated cirrhosis, early-onset familial noncirrhotic portal hypertension and primitive portal vein thrombosis. Each of them has no trials, no literature and no supported mechanistic link. The identical scores may reflect similarities the model learned between related diseases rather than disease-specific signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 single-ingredient injectable registrations are listed, all valid. The list may be partial. No approved indication text is recorded in the licence data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 62869 | Dorilon 500mg Injection | Vial of 1 Injection | Valid |
| 65519 | Doritrum 500mg Injection | Vial of 1 Injection | Valid |
| 65614 | Dori 500mg Injection | Vial of 1 Injection | Valid |
| 65832 | Doripik 500mg Injection | Vial of 1 Injection | Valid |
| 66363 | Denem 500mg Injection | Vial of 1 Injection | Valid |
| 68153 | Dori Nxt 500mg Injection | Vial of 1 Injection | Valid |
| 68471 | Dorbrooks 500mg Injection | Vial of 1 Injection | Valid |
| 69040 | Doriray 500mg Injection | Vial of 1 Injection | Valid |
| 69592 | Doriblast 500mg Injection | Vial of 1 Injection | Valid |
| 69627 | Doriplug 500mg Injection | Vial of 1 Injection | Valid |
| 69842 | Dorap 500mg Injection | Vial of 1 Injection | Valid |
| 70160 | Dpenem 500mg Injection | Vial of 1 Injection | Valid |
| 70530 | Doripem 500mg Injection | Vial of 1 Injection | Valid |
| 71468 | Doreross Injection | Vial of 1 Injection | Valid |
| 80654 | Exeldor 500mg Injection | Vial of 1 Injection | Valid |
| 112816 | Inarem 250mg Injection | Vial of 1 Injection | Valid |
| 144210 | Mydor Injection | Vial of 1 Injection | Valid |
| 158086 | Nozodor 500mg Injection | Vial of 1 ml Injection | Valid |
| 179068 | Penam 500 Injection | Vial of 1 Injection | Valid |
| 207621 | Supernem 500mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: Doripenem is linked to *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and impaired renal function disease as contraindication relations.
- **Drug Interactions**: Four moderate-level interactions are listed: picosulfuric acid, ethinylestradiol, mycophenolic acid and pemetrexed.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, and no plausible mechanism links a carbapenem antibiotic to hepatoportal sclerosis. The evidence level is L5, so it is a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis connecting doripenem to hepatoportal sclerosis
- A systematic literature search for any direct clinical or preclinical studies in this disease
- Package insert warnings and contraindications from Indian regulatory sources
- Evidence that the score reflects more than the similarities the TxGNN model (deep learning) learned between related hepatobiliary diseases

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL491571 (doripenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL491571) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

