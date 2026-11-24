---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
monitor_inn: "colistin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
last_modified_at: 2026-11-24
description: "Colistin: predicted new indication postinfectious vasculitis (evidence level L5). In India: at least 20 listed products"
---

# Colistin
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

## Colistin: Polymyxin antibiotic that disrupts the Gram-negative outer membrane → postinfectious vasculitis
{: .text-alpha }

## One-Sentence Summary

Colistin is a polymyxin antibiotic that acts on the outer membrane of Gram-negative bacteria.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but the data compiled for this report contain **no clinical trials and no publications** on this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | postinfectious vasculitis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Colistin belongs to the polymyxin class, which is known to disrupt the outer membrane of Gram-negative bacteria and kill them.

Postinfectious vasculitis is an immune-mediated inflammatory condition that develops after an infection. Antibacterial activity would not be expected to treat it, because the problem is the immune response rather than a live pathogen. No plausible mechanistic link has been identified, so the high score reflects a statistical pattern in the model, not a biological rationale. Colistin's known risks to the kidneys and nervous system add further concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 19505 | Acostin 4.5Million iu Injection | Vial of 1 ml Injection | Valid |
| 37190 | Coly Monas 2 Injection | Vial of 1 Injection | Valid |
| 37755 | Coly Monas 3 Injection | Vial of 1 Injection | Valid |
| 41100 | Colgit DS 25mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 44467 | Colizin Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 53427 | Colifate Suspension | Bottle of 30 ml Suspension | Valid |
| 53957 | Colicease 2Million IU Injection | Vial of 1 ml Injection | Valid |
| 95523 | GD Safe 12.5mg Syrup | Bottle of 30 ml Syrup | Valid |
| 104503 | Hopstin 1Million IU Injection | Vial of 1 ml Injection | Valid |
| 112018 | Iystin 12.5mg Suspension | Bottle of 30 ml Suspension | Valid |
| 117887 | Kallistro 2Million IU Powder for Injection | Vial of 1 Powder for Injection | Valid |
| 160029 | Nonumycin 12.5mg Syrup | Bottle of 30 ml Syrup | Valid |
| 160401 | Nelomycin 12.5mg Syrup | Bottle of 30 ml Syrup | Valid |
| 181015 | Pmx 1Million IU Injection | Vial of 1 Injection | Valid |
| 183900 | Quickstin 12.5mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 229116 | Tifmycine 12.5mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 241471 | Walamycin DS 25mg Suspension | Bottle of 30 ml Suspension | Valid |
| 242576 | Walapride 12.5mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 244243 | Xylomonas 3Million IU Injection | Vial of 1 Injection | Valid |
| 244352 | Xylomonas 4.5 MIU Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Colistin is marketed in India. The local data list at least 20 valid single-ingredient registrations, and this list may be partial. Products come as injections (vials of 1, 2, 3 and 4.5 million IU), syrups, dry syrups, suspensions and an oral suspension. Approved indication text is not recorded in the local data.

## Safety Considerations

- **Disease-level cautions (relation records, not label text):** Colistin has recorded contraindication relations with kidney disease, myasthenia gravis and other neuromuscular junction diseases, Clostridium difficile colitis, perinatal necrotizing enterocolitis, herpes simplex infection, and several other conditions. For infection-related hemolytic uremic syndrome, a related prediction in this analysis, colistin's nephrotoxicity is a particular concern.
- No drug interaction data were found.

Please refer to the package insert for further safety information, as label warnings and contraindications are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there is no clinical, literature or mechanistic support for colistin in postinfectious vasculitis. The condition is immune-mediated, and colistin's nephrotoxicity and neurotoxicity make speculative use unattractive.

**To proceed, the following is needed:**
- A plausible biological rationale linking colistin to post-infectious immune vasculitis
- Any preclinical or clinical studies that directly address this disease
- Mechanism of action data and package insert warnings and contraindications
- A nephrotoxicity and neurotoxicity risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

