---
layout: default
title: Pemetrexed
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Pemetrexed"
predicted_indications: ["pleural adenomatoid tumor", "pericardium cancer", "iminoglycinuria"]
description: "Pemetrexed: predicted new indication Pleural adenomatoid tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Pemetrexed
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

## Pemetrexed: Pleural adenomatoid tumor
{: .text-alpha }

## One-Sentence Summary

Pemetrexed is an antifolate chemotherapy drug originally used to treat non-small cell lung cancer and malignant pleural mesothelioma.
This direction currently has **7 clinical trials** and **20 publications** behind it. They are mostly Phase 2 trials, retrospective series and reviews, with no randomized trial specific to the peritoneal disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pleural adenomatoid tumor |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pemetrexed is a multi-targeted antifolate. It inhibits thymidylate synthase, dihydrofolate reductase (DHFR) and glycinamide ribonucleotide formyltransferase (GARFT). This blocks purine and pyrimidine synthesis in rapidly dividing tumour cells. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects the established pharmacology of the drug.

Peritoneal and pleural mesothelioma are the same disease in different locations. They share histology and chemosensitivity, and the mechanism is expected to carry over. Pemetrexed plus platinum is already the standard first-line chemotherapy for pleural mesothelioma. It is also used as systemic therapy for peritoneal disease, mostly by extrapolation. The current NCCN review notes that peritoneal mesothelioma is rare, that disease-specific prospective trials are scarce, and that systemic therapy recommendations are mostly borrowed from pleural trials.

The evidence is therefore consistent but indirect. Peritoneal data come from small Phase 2 studies and retrospective series, and the strongest randomized evidence (pemetrexed plus cisplatin versus cisplatin alone) was generated in pleural disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed (ALIMTA) plus gemcitabine as front-line therapy in pleural or peritoneal mesothelioma. Directly tests pemetrexed in the peritoneal population. |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of carboplatin-pemetrexed-bevacizumab with or without atezolizumab in peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | Randomized trial of PIPAC plus cisplatin-pemetrexed versus systemic chemotherapy alone as first-line treatment (MESOTIP) |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm study of sintilimab and bevacizumab with pemetrexed and cisplatin in unresectable peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 with cisplatin and pemetrexed in advanced solid tumours and mesothelioma. Mainly dose-finding and safety. |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed and imatinib in metastatic malignant mesothelioma. Early-phase safety study. |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Intraperitoneal versus intravenous chemotherapy after cytoreductive surgery and HIPEC (ICARuS II). Pemetrexed is not clearly the studied agent. |

---

## Literature Evidence

No randomized controlled trials specific to peritoneal mesothelioma were found. The list below covers the most relevant reviews and clinical series.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Review | J Natl Compr Canc Netw | Systemic therapy options for peritoneal mesothelioma. Recommendations are largely extrapolated from pleural trials, and first-line options include chemotherapy with pemetrexed and platinum. |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Clinical series | Jpn J Clin Oncol | Efficacy and safety of pemetrexed plus cisplatin as first-line chemotherapy in advanced peritoneal mesothelioma |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Rev Anticancer Ther | Retrospective evaluation of first-line pemetrexed-cisplatin in peritoneal mesothelioma |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Single-institution study | Tumori | Efficacy and safety of pemetrexed-cisplatin in chemo-naïve peritoneal mesothelioma patients |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparative study | Clin Med Insights Oncol | First-line pemetrexed-platinum versus gemcitabine-platinum regimens in peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-centre study | Ann Surg Oncol | Treatment strategies and outcomes in peritoneal mesothelioma |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | Diagnostic and therapeutic pathway. 5-year survival is about 20%, and cytoreductive surgery plus HIPEC gives the best outcomes in selected patients. |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment of peritoneal mesothelioma. Surgical cytoreduction plus HIPEC is the preferred initial treatment in selected patients. |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Review of the disease: rare, poor prognosis, weaker asbestos link than pleural disease |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management of peritoneal mesothelioma |

---

## India Market Information

Pemetrexed has 20 valid single-ingredient injectable registrations in India and none cancelled. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 4159 | Alimta 500mg Injection (Eli Lilly India) | Vial of 1, injection | Not listed in the data compiled |
| Registration No. 176971 | Pemgem 500mg Injection (Dr Reddy's) | Vial of 1, injection | Not listed in the data compiled |
| Registration No. 227660 | Temeran 500mg Injection (Sun Pharma) | Vial of 1, injection | Not listed in the data compiled |
| Registration No. 118127 | Kabipem 500mg Injection (Fresenius Kabi India) | Vial of 1, injection | Not listed in the data compiled |
| Registration No. 175406 | Pemnat 500mg Injection (Natco) | Vial of 1, injection | Not listed in the data compiled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate, antimetabolite class) |
| Myelosuppression Risk | High. Neutropenia, thrombocytopenia, anaemia and agranulocytosis are all recorded as concerns for this drug. |
| Emetogenicity Classification | Medium (general category-based estimate; confirm against the package insert) |
| Monitoring Items | CBC with differential, renal function (creatinine clearance), liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for dosing rules, including vitamin supplementation and renal dose considerations.

---

## Safety Considerations

- **Conditions of concern:** Pemetrexed is flagged as problematic in kidney disease and impaired renal function, and in blood-count disorders: thrombocytopenia, neutropenia, agranulocytosis, anaemia and macrocytic anaemia. These come from drug-disease relationship data, not from package insert text.
- **Drug interactions:** 367 interactions were identified. All of those listed below are rated Moderate:
  - Acid suppressants: famotidine, ranitidine, cimetidine.
  - Metformin and aspirin.
  - Aminosalicylates: mesalazine, balsalazide, olsalazine.
  - Amphotericin B, including its lipid and liposomal forms.
  - Antibiotics: vancomycin, kanamycin, neomycin, polymyxin B, levofloxacin, amoxicillin.
  - Sapropterin.

  A full interaction review is advised before use, especially for drugs that are cleared by the kidney or are nephrotoxic.

For label warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pemetrexed plus platinum is already an accepted systemic option in peritoneal mesothelioma. It is supported by a completed Phase 2 trial, several retrospective series, and several ongoing randomized and single-arm Phase 2 trials. It is also marketed widely in India. However, there are no completed randomized trials specific to the peritoneal disease, so the evidence rests mostly on extrapolation from pleural mesothelioma. The drug's high myelosuppression and renal risks require tight controls.

**To proceed, the following is needed:**
- Review of the India package insert for warnings, contraindications and approved indications, which were not available for this report
- Detailed mechanism-of-action data from a drug database
- Results of the ongoing randomized Phase 2 trials in peritoneal mesothelioma (NCT05001880, NCT03875144)
- A safety monitoring plan covering blood counts, renal function, vitamin supplementation and interaction screening
- Clarification of how systemic chemotherapy fits alongside cytoreductive surgery with HIPEC and immunotherapy options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

