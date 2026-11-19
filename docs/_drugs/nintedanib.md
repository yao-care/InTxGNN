---
layout: default
title: Nintedanib
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Nintedanib"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
description: "Nintedanib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). In India: at least 20 listed products"
---

# Nintedanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nintedanib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Nintedanib was originally used for non-small cell lung carcinoma and fibrosing interstitial lung diseases such as idiopathic pulmonary fibrosis.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
but at present only **1 review article** supports this direction, and **no clinical trials** are registered.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9915 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nintedanib: "Nintedanib is a small molecule that inhibits multiple receptor tyrosine kinases (RTKs) and non-receptor tyrosine kinases (nRTKs). Nintedanib inhibits the following RTKs: platelet-derived growth factor receptor (PDGFR) α and β, fibroblast growth factor receptor (FGFR) 1-3, vascular endothelial growth factor receptor (VEGFR) 1-3, colony stimulating factor 1 receptor (CSF1R), and Fms-like tyrosine kinase-3 (FLT-3)." ([DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa), label version 2026-04-21; accessed 2026-11-19.) Based on known pharmacology, nintedanib is a small-molecule tyrosine kinase inhibitor that targets PDGFR-alpha/beta, FGFR1-3 and VEGFR1-3. Its efficacy in idiopathic pulmonary fibrosis and non-small cell lung carcinoma is established, and mechanistically it may be applicable to DFSP.

DFSP is driven by the COL1A1-PDGFB fusion, which causes constitutive activation of PDGFR-beta. Because nintedanib inhibits PDGFR-beta, there is a plausible biological link between the drug and this tumour. Its antifibrotic and antiproliferative effects on fibroblasts add a general supporting rationale.

This link is indirect, however. Imatinib is the established PDGFR-targeted agent for DFSP, and no nintedanib-specific clinical data are available. The prediction should therefore be treated as a research question rather than a treatment recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders; indirect support for targeting PDGFR in PDGF-driven tumours |

## India Market Information

Twenty valid single-ingredient registrations are on record, all oral capsules. The licence records do not include approved indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 41026 | Cyendiv 100mg Soft Gelatin Capsule (Boehringer Ingelheim) | Bottle of 10 soft gelatin capsules | Not stated in the records |
| 150549 | Nintib 150 Soft Gelatin Capsule (Cipla Ltd) | Strip of 10 soft gelatin capsules | Not stated in the records |
| 151861 | Nindev 100mg Soft Gelatin Capsule (Zydus Cadila) | Strip of 10 soft gelatin capsules | Not stated in the records |
| 140002 | Mantedanib Capsule 150mg (Mankind Pharma Ltd) | Strip of 10 capsules | Not stated in the records |
| 150364 | Nintena 150mg Soft Gelatin Capsule (Sun Pharmaceutical Industries Ltd) | Strip of 10 soft gelatin capsules | Not stated in the records |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The first 20 returned include one Major interaction and 19 Moderate ones.
  - **Major**: Dexamethasone.
  - **Moderate, bleeding-risk related**: Acetylsalicylic acid, clopidogrel, apixaban, dalteparin, cilostazol, dipyridamole, alteplase, abciximab, bivalirudin, betrixaban, cangrelor, caplacizumab, defibrotide, desirudin, antithrombin III human. Anticoagulants, antiplatelets and thrombolytics warrant particular caution.
  - **Moderate, other**: Clarithromycin, cobicistat, naltrexone, rolapitant.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9915), and the PDGFR-beta mechanism is plausible for DFSP. However, the only supporting evidence is one indirect review, there are no clinical trials, and an established PDGFR-targeted therapy (imatinib) already exists. Safety review also cannot proceed until the package insert data are obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking data gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical data (for example DFSP cell-line or xenograft studies) or case reports of nintedanib in DFSP
- A comparison against imatinib to define a possible role, such as in imatinib-resistant disease
- A bleeding-risk management plan for patients taking anticoagulants or antiplatelet agents

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

