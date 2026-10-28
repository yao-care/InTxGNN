---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rifaximin: Oral candidiasis
{: .text-alpha }

## One-Sentence Summary

Rifaximin is a non-absorbed oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **oral candidiasis**, but the only supporting item is **1 publication**, and it points toward a possible harm signal rather than a benefit. There are **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is a non-absorbed oral antibacterial that acts mainly in the gut and alters gut microbiota. Its efficacy in hepatic encephalopathy is the basis of its original use, but its link to oral candidiasis is hard to justify mechanistically.

The one linked publication (2021) reports that rifaximin use **favoured micafungin-resistant Candida infections** in patients receiving allogeneic hematopoietic cell transplants. This suggests that altering gut microbiota may promote fungal overgrowth, which is opposite to the predicted therapeutic direction. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a treatment effect.

The other top-ranked predictions (commissural lip fistula, osteoradionecrosis of the mandible, burning mouth syndrome, oral leukoedema) have no trials or literature and no plausible mechanism. Candidiasis (rank 6, score 0.9915) has two observational publications, both indicating increased infection risk rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients given rifaximin prophylaxis, use of rifaximin favoured micafungin-resistant Candida infections. This is a harm signal, not a benefit. |

## India Market Information

The registrations below are 5 of 20 valid single-ingredient products. All are oral tablets. The data compiled for this report contains no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 192547 | Rifanid 400mg Tablet (Nidus Pharma Pvt Ltd) | Strip of 10 tablets | Not available |
| 185439 | Rifarex 400mg Tablet (Tas Med India Pvt Ltd) | Strip of 10 tablets | Not available |
| 185961 | Rifaset 550 Tablet (Macleods Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not available |
| 184595 | Rifakem 550 Tablet (Alkem Laboratories Ltd) | Strip of 10 tablets | Not available |
| 184191 | Rcifax 400 Tablet (Lupin Ltd) | Strip of 10 tablets | Not available |

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease graph edges, not label text): *Clostridium difficile* colitis; perinatal necrotizing enterocolitis.
- **Drug Interactions**: 69 interactions were identified. Examples include:
  - **Major**: live cholera vaccine (*Vibrio cholerae* CVD 103-HgR strain).
  - **Moderate**: warfarin, cyclosporine, tolvaptan, daclatasvir, ledipasvir, and several oncology agents (alpelisib, apalutamide, brigatinib, cabozantinib, capmatinib, darolutamide, encorafenib, enasidenib).
- **Fungal infection signal**: Observational literature links rifaximin use to Candida infections, including micafungin-resistant strains, in transplant recipients. This should be treated as a safety concern.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score, but the only supporting literature suggests rifaximin may promote Candida infection rather than treat it. There are no clinical trials, and a non-absorbed gut antibiotic has no clear mechanism against oral candidiasis. Evidence is insufficient to proceed.

**To proceed, the following is needed:**
- Mechanism of action data to assess any plausible link to oral candidiasis
- Package insert warnings and contraindications for the India products (currently missing and blocking safety screening)
- Approved indication text for the India registrations
- Prospective or controlled studies showing a therapeutic benefit, not just a risk association
- Consideration of reframing the hypothesis as a safety question (fungal overgrowth risk with rifaximin use)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

