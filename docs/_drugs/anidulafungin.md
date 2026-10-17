---
layout: default
title: Anidulafungin
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Anidulafungin: predicted new indication Impetigo (evidence level L5). Approved use: Esophageal candidiasis, candidemia"
monitor_inn: "Anidulafungin"
predicted_indications: ["impetigo", "malignant pleural mesothelioma", "staphylococcal scalded skin syndrome", "pleural empyema (disease)", "malignant visceral pleura tumor", "bullous impetigo", "malignant epithelioid mesothelioma", "sarcomatoid mesothelioma", "hordeolum", "Clostridium infectious disease"]
---

# Anidulafungin
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

# Anidulafungin: From Esophageal Candidiasis and Candidemia to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal, originally used to treat esophageal candidiasis and candidemia.
The TxGNN model predicts it may be effective for **impetigo**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.
The mechanistic review found no plausible biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, anidulafungin belongs to the echinocandin class. It inhibits 1,3-beta-D-glucan synthase, an enzyme in the fungal cell wall, which explains its proven efficacy in invasive Candida infections.

The link to impetigo is weak. Impetigo is a bacterial skin infection, mainly caused by *Staphylococcus aureus* and *Streptococcus pyogenes*. Bacteria do not have the enzyme that anidulafungin targets, so the drug has no expected antibacterial activity. The high TxGNN score most likely reflects the model grouping anti-infective drugs together in its knowledge graph rather than a real biological relationship.

The other top-ranked predictions have the same problem. Mesothelioma and other pleural tumours have no known glucan synthase target. Staphylococcal scalded skin syndrome, bullous impetigo, hordeolum and Clostridium infection are bacterial conditions. Pleural empyema is the only one with indirect support: a pharmacokinetic study showed the drug reaches pleural fluid. That supports feasibility for a fungal pleural infection, not efficacy in empyema, which is mostly bacterial.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 3077 | Anidulan Injection (Mylan Pharmaceuticals) | Vial of 1 Injection | Indication text not listed |
| 39084 | Canidula Injection (Gufic Bioscience) | Vial of 1 Injection | Indication text not listed |
| 62776 | Dulaedge 100mg Injection (Abbott) | Vial of 1 Injection | Indication text not listed |
| 72925 | Eraxis 100mg Injection (Pfizer) | Vial of 1 Injection | Indication text not listed |
| 75267 | Endfung 100mg Injection (Glenmark) | Vial of 1 Injection | Indication text not listed |

Twelve single-ingredient injectable registrations are valid, and none are cancelled. Only the five main ones are shown here.

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver disease and gallbladder disease.
- **Drug Interactions**: One interaction was found, with cyclosporine, rated Minor.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for impetigo has no clinical trials or publications behind it. The drug has no antibacterial activity and the target enzyme is absent in bacteria, so the high score is probably a graph artifact. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- A credible mechanistic rationale for activity against impetigo, or a switch to a better-supported indication
- Package insert warnings and contraindications from the Indian manufacturers, which are currently missing and block safety screening
- Detailed mechanism of action data
- In vitro or preclinical data showing activity against the relevant pathogens
- Route compatibility assessment, since only injectable forms are marketed and impetigo is usually treated topically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

