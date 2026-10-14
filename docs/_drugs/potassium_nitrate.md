---
layout: default
title: Potassium Nitrate
parent: Model Prediction Only (L5)
nav_order: 692
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Potassium Nitrate: From Dental Hypersensitivity Products to Meningococcal Infection

## One-Sentence Summary

Potassium nitrate is marketed in India as an ingredient in dental gels and toothpastes. The TxGNN model predicts it may be effective for **meningococcal infection**, but **no clinical trials and no publications** currently support this prediction. It rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the registrations) |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the registrations, potassium nitrate is a single-ingredient component of oral-care products (dental gels and toothpastes) in India. No original indication is recorded for it.

One speculative rationale is that potassium nitrate is an inorganic nitrate salt. It can be reduced to nitrite and then to nitric oxide (NO), and NO and related reactive nitrogen species have general antimicrobial activity. This is not specific to *Neisseria meningitidis* and is not supported by any data compiled for this report.

Meningococcal infection is an acute, life-threatening invasive disease. It is treated with established antibiotics and prevented by vaccines. A high TxGNN score alone does not justify repurposing a nitrate salt for this condition.

A second prediction, **sclerosing cholangitis** (score 99.21%), also has no clinical trials or literature. Its proposed link, nitrate-derived NO signalling affecting vascular tone, inflammation or biliary epithelial function, is equally unsupported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

There are 20 valid single-ingredient registrations, with no combination products and none cancelled. The five main ones are listed below. Approved indication text is not recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 151674 | Nitra Gel Mint | Dental gel, 100 g tube | Micro Labs Ltd |
| 117360 | Kyodent Dental Gel | Dental gel, 50 g tube | Lifekyor Pharmaceuticals |
| 61782 | Dent-X Toothpaste (Medicated) | Toothpaste, 100 g tube | Cascade India Pharmaceuticals |
| 65292 | Dentosmith Toothpaste | Toothpaste, 50 g tube | Nusmith Pharma Pvt. Ltd |
| 164072 | Orasafe Dental Gel | Gel, 50 g tube | Age Biotech |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

