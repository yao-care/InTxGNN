---
layout: default
title: Dasatinib
parent: Model Prediction Only (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dasatinib: predicted new indication Ewing sarcoma (evidence level L5). Approved use: Chronic myelogenous leukemia…"
---

# Dasatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dasatinib: From BCR-ABL1-Positive Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral tyrosine kinase inhibitor originally used to treat BCR-ABL1-positive chronic myeloid leukemia (CML), including blast phase.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **2 clinical trials** and **about 8 relevant publications** on this direction.
The support is mostly preclinical, and the one reported clinical result, from a review of the advanced-sarcoma Phase 2 study, was negative for single-agent use in this tumor type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive (including blast phase). Approved-indication text is blank on the Indian licenses, so this comes from the drug's indication records. |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 as assigned, with a caveat (see below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

**Evidence level caveat:** The only completed Phase 2 trial (NCT00464620) is a single-arm study in mixed advanced sarcomas, not a randomized trial. A 2022 review reports that single-agent dasatinib failed in Ewing sarcoma and rhabdomyosarcoma. The practical strength is closer to L4 (preclinical and mechanistic support).

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. From the literature, dasatinib is a multi-targeted kinase inhibitor. It potently blocks BCR-ABL, which drives CML, and also blocks SRC-family kinases, c-KIT and PDGFR.

Ewing sarcoma is a very different disease from CML, so the link is through SRC signaling rather than BCR-ABL. Preclinical studies show that SRC activation drives invadopodia formation, migration and invasion in Ewing sarcoma cells, especially under microenvironmental stress. Dasatinib reduced proliferation and migration in Ewing sarcoma and neuroblastoma cell lines. It also induced apoptosis in bone sarcoma cells that depend on SRC. The FAK-Src axis has been proposed as a treatment target in Ewing sarcoma and related sarcomas.

The clinical picture is less encouraging. A review notes that dasatinib alone did not work in Ewing sarcoma in a Phase 2 sarcoma study. A more plausible route is combination therapy, such as the RIST regimen (rapamycin, irinotecan, dasatinib, temozolomide) used in relapsed disease. That evidence is so far only a small descriptive case series.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Single-agent dasatinib in advanced sarcomas, measuring response rate and 6-month progression-free survival. Ewing-specific results are not shown in the trial record. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib with ifosfamide, carboplatin and etoposide. Stopped early with very few patients, so it gives little safety or efficacy information. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Targeting the FAK-Src complex in DSRCT, Ewing sarcoma and rhabdomyosarcoma. Notes that single-agent dasatinib failed in a Phase 2 sarcoma study. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Src signaling in sarcoma and its feasibility as a drug target. |
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | Case series | J Pediatr Hematol Oncol | Single-center descriptive experience with the RIST regimen (including dasatinib) in relapsed Ewing sarcoma. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical | Cancer Research | Dasatinib inhibited migration and invasion in sarcoma cell lines and induced apoptosis in SRC-dependent bone sarcoma cells. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical | Oncology Reports | Antiproliferative and antimigratory activity of dasatinib in neuroblastoma and Ewing sarcoma cell lines. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress activates Src-dependent invadopodia and migration in Ewing sarcoma. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to promote invadopodia formation in Ewing sarcoma. |

---

## India Market Information

There are 20 valid single-ingredient registrations (no combination products and none cancelled), all oral tablets. The approved-indication text is blank on every license, so that column is omitted. Five main registrations are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 200644 | Sprycel 50mg Tablet | Bottle of 60 tablets | BMS India Pvt Ltd |
| 205671 | Sprycel 20mg Tablet | Bottle of 60 tablets | BMS India Pvt Ltd |
| 67898 | Dasamed 20mg Tablet | Bottle of 60 tablets | Medicamen Biotech Ltd |
| 66154 | Dyronib 20mg Tablet | Bottle of 60 tablets | Hetero Healthcare Limited |
| 65360 | Dasania 20mg Tablet | Bottle of 60 tablets | Lupin Ltd |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: BCR-ABL, SRC family, c-KIT, PDGFR) |
| Myelosuppression Risk | Medium to high. Neutropenia and thrombocytopenia are among the knowledge-graph contraindication flags, and anemia and agranulocytosis are also flagged. |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, signs of fluid retention such as pleural effusion, and cardiac status including QT interval |
| Handling Protection | Please refer to the package insert warnings and precautions. Follow institutional hazardous-drug handling practice. |

---

## Safety Considerations

- **Contraindication-related conditions (from the drug-disease knowledge graph, not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anemia, congestive heart failure and heart failure, myocardial infarction, coronary thrombosis, pericardial effusion, hemopericardium, intracerebral hemorrhage, active peptic ulcer disease, and hemoglobinopathy.
- **Drug interactions:** 691 interactions are recorded. Major-level examples include:
  - acid-reducing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole)
  - dexamethasone
  - acetylsalicylic acid
  - clarithromycin
  
  Moderate-level examples include hydrocortisone, loperamide, aprepitant, budesonide, antacids (aluminum hydroxide, calcium carbonate, magnesium oxide) and saxagliptin.
- Package insert warnings and contraindications for the Indian market were not available, so please refer to the package insert for the authoritative label information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Ewing sarcoma prediction is biologically plausible through SRC inhibition and has consistent preclinical support. However, the one relevant clinical signal, single-agent dasatinib in advanced sarcomas, is reported as unsuccessful in Ewing sarcoma. The Ewing-specific trial is too small (7 patients) to inform efficacy. This is best treated as a research question rather than a candidate for clinical development.

**To proceed, the following is needed:**
- Ewing-specific outcome data from NCT00464620
- Prospective clinical data on dasatinib-containing combinations such as RIST, beyond the single-center case series
- Detailed mechanism-of-action data
- Indian package insert warnings and contraindications
- A safety and monitoring plan for pediatric and young-adult patients, covering myelosuppression, fluid retention and QT risk, plus review of acid-reducer and CYP3A4-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

