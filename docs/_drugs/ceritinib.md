---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 164
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Ceritinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma"
monitor_inn: "Ceritinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "junctional epidermolysis bullosa"]
---

# Ceritinib
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

## Ceritinib: From Non-Small Cell Lung Cancer to fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Ceritinib is an oral ALK inhibitor originally used to treat non-small cell lung carcinoma and lung cancer.
The TxGNN model's top-ranked prediction is **gingival fibromatosis**, but there are **no clinical trials and no publications** supporting it.
This is a purely computational signal and should be treated as a hypothesis, not as evidence of benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma; lung cancer (the approved indication text is not available in the India registration record) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ceritinib is a kinase inhibitor with activity against ALK, ROS1 and IGF-1R. Its efficacy in ALK-rearranged non-small cell lung cancer is established, but it has no established role in gingival fibromatosis.

The relationship between the original and predicted indications is weak. Gingival fibromatosis is a benign overgrowth of gum tissue. There is no known link between ALK/ROS1 signalling and this condition. The high score (0.9986) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions show the same pattern:
- **Lung-related tumours** (fibroma of lung, hamartoma of lung, lung hilum carcinoma, pulmonary sulcus neoplasm): these are in the same organ as the approved indication. Malignant ALK-positive cases would already fall under the current indication. For benign tumours, there is no evidence that ALK/ROS1 drives them.
- **Lung benign neoplasm** (rank 5): the 20 retrieved publications actually concern ALK/ROS1-rearranged NSCLC, which is malignant and already the approved indication. They do not address benign tumours, so this evidence is indirect at best.
- **Lung germ cell tumour** (rank 6): the literature covers other ALK-altered tumours (neuroblastoma case reports, a glioblastoma Phase 0 trial, an ALK-positive pulmonary carcinoid), not germ cell tumours. It is flagged as a research question only.
- **Genetic disorders** (inclusion body myopathy with Paget disease, junctional epidermolysis bullosa, leukomelanoderma syndrome): no mechanistic link to kinase inhibition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (gingival fibromatosis) or for any of the other nine predictions.

---

## Literature Evidence

Currently no related literature available for the top predicted indication (gingival fibromatosis).

Literature was retrieved for three lower-ranked predictions, but it is indirect. The most informative items are shown below for context. They concern the approved ALK/ROS1 NSCLC use and the ceritinib safety profile, not the predicted new indications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28126333](https://pubmed.ncbi.nlm.nih.gov/28126333/) | 2017 | RCT (Phase 3, ASCEND-4) | Lancet | First-line ceritinib vs platinum-based chemotherapy in advanced ALK-rearranged NSCLC |
| [28520527](https://pubmed.ncbi.nlm.nih.gov/28520527/) | 2017 | Phase 2 | J Clin Oncol | Ceritinib 750 mg daily in 32 patients with ROS1-rearranged NSCLC |
| [37478263](https://pubmed.ncbi.nlm.nih.gov/37478263/) | 2023 | Cohort | Medicine | Retrospective study of ceritinib in crizotinib-resistant ROS1-rearranged NSCLC |
| [32074131](https://pubmed.ncbi.nlm.nih.gov/32074131/) | 2020 | Systematic review/NMA | PLoS One | Relative effects of individual ALK inhibitors in NSCLC |
| [34702773](https://pubmed.ncbi.nlm.nih.gov/34702773/) | 2022 | Phase 0 trial | Clin Cancer Res | Tumour pharmacokinetics and pharmacodynamics of ceritinib in brain metastases and recurrent glioblastoma |
| [33362184](https://pubmed.ncbi.nlm.nih.gov/33362184/) | 2020 | Case report | Recenti Prog Med | Ceritinib in an adult with advanced neuroblastoma carrying ALK F1174L |
| [29907598](https://pubmed.ncbi.nlm.nih.gov/29907598/) | 2018 | Case report | Cold Spring Harb Mol Case Stud | Clinical response of ALK-I1171T neuroblastoma to ceritinib |
| [32671808](https://pubmed.ncbi.nlm.nih.gov/32671808/) | 2020 | Retrospective analysis | Targeted Oncology | Ceritinib-induced organizing pneumonia, which can be confused with disease progression |
| [35435628](https://pubmed.ncbi.nlm.nih.gov/35435628/) | 2022 | Systematic review/meta-analysis | Investigational New Drugs | Toxicity profile of ALK tyrosine kinase inhibitors in NSCLC |
| [29413968](https://pubmed.ncbi.nlm.nih.gov/29413968/) | 2018 | Review/Commentary | Eur J Cancer | QT prolongation with TKIs including ceritinib; ECG screening advised |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 200719 | Spexib Capsule (Novartis India Ltd) | Strip of 10 capsules (oral) | Not available in the registration record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; literature highlights liver function (hepatotoxicity signal in pharmacovigilance data), ECG/QT interval, and pulmonary symptoms (organizing pneumonia) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 629 recorded interactions. Most of those shown are Moderate, and two are Major:
  - **Major**: triamcinolone, budesonide
  - **Moderate (examples)**: acid-reducing agents (famotidine, ranitidine, omeprazole, rabeprazole), other corticosteroids (dexamethasone, hydrocortisone, betamethasone), antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide), aprepitant, loperamide, and bisacodyl
- **Literature-derived safety signals** (not label text): QT prolongation, hepatotoxicity, organizing pneumonia, and a reported hypersensitivity reaction with infiltrative lung disease.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a very high model score but no trials, no literature, and no mechanistic link to ALK/ROS1/IGF-1R inhibition. It is purely computational (L5). None of the ten predicted indications has direct supporting evidence. Lung germ cell tumour is the only one flagged as a research question, and any relevance would depend on demonstrating an ALK alteration in the tumour.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening), obtained from the India registration documents
- Mechanism of action data for ceritinib from DrugBank
- A biological hypothesis linking ceritinib targets to gingival fibromatosis, for example expression of ALK, ROS1 or IGF-1R in affected tissue
- Preclinical or case-level evidence before any clinical consideration
- For lung germ cell tumour, molecular testing for ALK alterations to see whether any cases are actionable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

