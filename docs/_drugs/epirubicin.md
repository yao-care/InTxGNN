---
layout: default
title: Epirubicin
parent: Moderate Evidence (L3-L4)
nav_order: 315
evidence_level: L4
indication_count: 7
---

# Epirubicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Epirubicin: From Breast Carcinoma to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy drug, originally used to treat breast cancer.
The TxGNN model predicts it may be effective for **primary pulmonary lymphoma**, but there are **no registered clinical trials** and only **6 loosely related publications**, none of which directly tests epirubicin in this disease. The prediction rests mainly on the model score and the general activity of anthracyclines in lymphoid cancers.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast carcinoma / breast neoplasm (the approved indication text on Indian registrations is blank) |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, epirubicin is an anthracycline (a topoisomerase II inhibitor and DNA intercalator). Its efficacy in breast cancer is established, and mechanistically it may be applicable to lymphoid cancers.

Anthracyclines are part of well-known lymphoma regimens, such as CEOP/FEC-type and VEBEP. Cytotoxic activity against lymphoid malignancies is therefore biologically plausible.

However, the retrieved literature does not show that epirubicin works in primary pulmonary lymphoma. It consists of:
- a general epirubicin pharmacology review;
- a DLBCL regimen (Pola-R-CHP) that contains doxorubicin, not epirubicin;
- case reports and retrospective series.

Doxorubicin-based R-CHOP is already the standard of care, so there is little reason to substitute epirubicin. The prediction is mechanistically plausible but not clinically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Epirubicin pharmacology and clinical use. Response rates and survival were similar to doxorubicin regimens in breast and other cancers. Not specific to pulmonary lymphoma. |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Subgroup analysis (retrospective) | Annals of Hematology | Real-world Pola-R-CHP in 117 first-line DLBCL patients, including trial-ineligible and low-IPI patients. Regimen contains doxorubicin, not epirubicin. |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Clinical features and prognostic factors of primary extranodal DLBCL in the rituximab era. |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort (pilot) | The Cancer Journal from Scientific American | VEBEP regimen plus involved-field radiotherapy in advanced Hodgkin's disease. Evaluated efficacy and toxicity of an intensive regimen. |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report with review | Translational Cancer Research | Misdiagnosed primary MALT lymphoma of the pleura. Rare site, atypical presentation. |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report/series | Revista de Investigación Clínica | Primary non-Hodgkin lymphoma of the lung with pleural effusion. |

---

## India Market Information

Epirubicin is marketed in India, with 20 valid single-ingredient registrations, all injectable. The approved indication text is blank in the registration records. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 89381 | Farmorubicin RD 10mg Injection | Vial of 5 ml, injection | Pfizer Ltd |
| 82628 | Episar 10mg Injection | Vial of 1, injection | Sarabhai Chemicals Ltd |
| 11863 | Alrubicin 150mg Injection | Vial of 1, injection | Alkem Laboratories Ltd |
| 79984 | Epitero 10 Injection | Vial of 1, powder for injection | Hetero Drugs Ltd |
| 77804 | Epitaz 10mg Injection | Vial of 1, injection | Intas Pharmaceuticals Ltd |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are expected) |
| Emetogenicity Classification | Moderate to high, depending on dose |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (e.g., LVEF) and cumulative anthracycline dose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are based on the anthracycline drug class. Please refer to the package insert warnings and precautions for product-specific details.

---

## Safety Considerations

- **Conditions linked to contraindications** (drug-disease associations from a knowledge graph, not label text): liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, hemoglobinopathy, myocardial infarction, coronary thrombosis, sudden cardiac arrest, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, myocardial disorder, heart conduction disease, stomatitis, and pyoureter.
- **Drug interactions**: 487 interactions are recorded. In the 20-entry sample reviewed, the two **Major** interactions are **cimetidine** and **dolasetron**. Most others are Moderate (e.g., clarithromycin, levofloxacin, bupropion, famotidine, palonosetron, loperamide), and metronidazole is Minor.
- **Literature-noted risks**: The retrieved literature, from reports in other indications, describes anthracycline cardiotoxicity and secondary AML/MDS after epirubicin-based therapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score (99.71%) is not backed by any clinical trial or by direct literature on epirubicin in primary pulmonary lymphoma. Doxorubicin-based R-CHOP is already standard care, so epirubicin has no clear added value here.

**To proceed, the following is needed:**
- Direct clinical evidence of epirubicin in primary pulmonary lymphoma, or a clear rationale for choosing it over doxorubicin.
- Mechanism of action data (MOA).
- Package insert warnings and contraindications for Indian-marketed products.
- A cardiac and haematological safety monitoring plan.

Other predicted indications for epirubicin have stronger support and may be better candidates:
- **Gastroesophageal adenocarcinoma** (predicted as "upper aerodigestive tract neoplasm"): supported by Phase 3 evidence (the MAGIC trial of perioperative ECF), evidence level L1, recommendation Proceed with Guardrails.
- **Small cell lung carcinoma**: has Phase 3 trials and L1 evidence, but epirubicin is not part of current standard care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

