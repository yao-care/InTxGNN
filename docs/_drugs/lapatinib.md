---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 1
---

# Lapatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Lapatinib: From HER2-Positive Breast Carcinoma to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib was originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but **no clinical trials or publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Lapatinib is known to be a dual EGFR/HER2 tyrosine kinase inhibitor, and its efficacy in HER2-positive breast carcinoma is established.

DFSP is typically driven by the COL1A1-PDGFB fusion, which causes constitutive PDGFR-beta activation, and it is usually treated with imatinib. A direct link between lapatinib's EGFR/HER2 inhibition and this driver pathway has not been established. A plausible but unverified connection is through downstream signaling shared among receptor tyrosine kinases (such as PI3K/AKT and MAPK), or through EGFR involvement in some sarcomas.

The prediction should therefore be treated as a hypothesis, requiring preclinical validation before any clinical consideration.

## India Market Information

Lapatinib is marketed in India as single-ingredient oral tablets. The approved indication text is not available for these registrations. The first five of the 11 are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 125749 | Lanib 250 Tablet | Bottle of 30 tablets | BDR Pharmaceuticals Internationals Pvt |
| 75607 | Etibo 250mg Tablet | Bottle of 30 tablets | Samarth Life Sciences Pvt Ltd |
| 122886 | Libset Tablet | Bottle of 30 tablets | Intas Pharmaceuticals Ltd |
| 124425 | Lapahope 250mg Tablet | Bottle of 30 tablets | Glenmark Pharmaceuticals Ltd |
| 216089 | Tykerb 250mg Tablet | Bottle of 30 tablets | Glaxo SmithKline Pharmaceuticals Ltd |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, cardiac function (including QT interval), electrolytes (notably potassium), and respiratory symptoms, based on the disease associations listed below |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, drug-induced liver injury, potassium deficiency disease, interstitial lung disease, heart failure.
- **Drug Interactions**: 549 interactions were identified. Major-level interactions include:
  - **Loperamide**
  - **Clarithromycin**

  Moderate-level interactions include acid-suppressing agents (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexlansoprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aprepitant, pioglitazone, saxagliptin, and several laxatives or bowel-preparation agents.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high TxGNN score. There are no clinical trials or publications, and no established mechanistic link between EGFR/HER2 inhibition and the PDGFB-driven biology of DFSP. Imatinib already addresses that driver pathway.

**To proceed, the following is needed:**
- Preclinical validation (for example, lapatinib activity in DFSP cell lines or models, and EGFR/HER2 expression in DFSP tissue)
- Mechanism of action data for lapatinib
- India package insert warnings and contraindications for safety screening
- Route compatibility assessment (oral tablets are marketed)
- A comparison against standard DFSP therapy (imatinib) to define any unmet need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

