---
layout: default
title: Sparfloxacin
parent: Model Prediction Only (L5)
nav_order: 786
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Sparfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Pneumonia (streptococcal, Mycoplasma pneumoniae, chlamydial)"
monitor_inn: "Sparfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Sparfloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Sparfloxacin: From Pneumonia to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Sparfloxacin is a fluoroquinolone antibiotic, originally used to treat pneumonia (including streptococcal, Mycoplasma pneumoniae and chlamydial pneumonia).
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** currently support this prediction.
It is a computational signal only and should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pneumonia (streptococcal, Mycoplasma pneumoniae, chlamydial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, sparfloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. This action explains its efficacy against respiratory pathogens.

No mechanistic link to hyperamylasemia could be identified. Elevated amylase is not an established therapeutic target for this drug class, and no known pathway connects the antibacterial action to amylase regulation. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and there are no supporting clinical or literature data.

Other top-ranked predictions show the same pattern. These include polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy and several haematological conditions. None has a plausible mechanistic rationale, and none has trials or publications. One exception is **septicemic plague** (rank 8, score 0.9931). A class-level rationale exists because fluoroquinolones are active against *Yersinia pestis*. However, no sparfloxacin-specific data were found, and the one retrieved publication concerns uropathogenic *E. coli*, not plague.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For reference, the only publication retrieved across the predicted indications relates to the lower-ranked prediction of septicemic plague:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20231390](https://pubmed.ncbi.nlm.nih.gov/20231390/) | 2010 | Preclinical (in vitro) | Antimicrob Agents Chemother | Persistence of uropathogenic *E. coli* in the face of multiple antibiotics. Not specific to plague or hyperamylasemia. |

---

## India Market Information

Sparfloxacin is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. Approved indication text was not available for these products. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 201912 | Spin 200mg Tablet | Strip of 10 tablets | Lancer Health Care Pvt Ltd |
| 213300 | Sparflin 400mg Tablet | Strip of 6 tablets | Lupin Ltd |
| 208042 | Sparcure 200mg Tablet | Strip of 10 tablets | Radicura Pharma Pvt Ltd |
| 202418 | Spiro 200mg Tablet | Strip of 10 tablets | Adoc Pharma |
| 210716 | Spearl 200mg Tablet | Strip of 6 tablets | Pax Healthcare |

---

## Safety Considerations

Drug-interaction screening identified **239 interacting drugs**. Examples of those rated **Major**:

- Hydrocortisone
- Dexamethasone
- Betamethasone
- Triamcinolone
- Bupropion
- Chlorpropamide

Examples of **Moderate** interactions include acarbose, famotidine, metformin, pioglitazone, canagliflozin, loperamide, acetylsalicylic acid and calcium or potassium salts.

Other considerations noted in the data compiled for this report:
- Fluoroquinolones are associated with peripheral neuropathy as an adverse effect.
- Sparfloxacin carries phototoxicity and QT-prolongation risks, and has limited current availability.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There is no mechanistic link, no clinical trials and no literature for hyperamylasemia. Sparfloxacin's safety profile (phototoxicity, QT prolongation, neuropathy, many major interactions) further argues against pursuing this indication.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a plausible biological rationale linking sparfloxacin to amylase regulation
- Package insert warnings and contraindications from the India market, which are required for safety screening
- Any preclinical or clinical evidence for the predicted indication
- A risk-benefit assessment for QT prolongation, phototoxicity and drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

