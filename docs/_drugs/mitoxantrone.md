---
layout: default
title: Mitoxantrone
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 8
---

# Mitoxantrone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mitoxantrone: From Leukemia & Lymphoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Mitoxantrone is a synthetic anthraquinone antineoplastic agent internationally established for the treatment of acute leukemias, non-Hodgkin's lymphoma, and multiple sclerosis.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leukemia, Non-Hodgkin's Lymphoma, Multiple Sclerosis (international; not registered in India) |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Mitoxantrone is a synthetic anthraquinone compound structurally related to doxorubicin. Its primary mechanism of action involves **inhibition of Topoisomerase II (Topo II)** and direct intercalation into DNA double strands, blocking DNA replication and repair and ultimately triggering apoptosis in rapidly dividing cells. This mechanism is not tumor-type specific — any cancer with high DNA replication activity and Topo II expression is potentially susceptible. The drug has a long terminal half-life (approximately 40–71 hours) and is primarily eliminated via hepatic metabolism, supporting sustained systemic exposure following intravenous administration.

Upper aerodigestive tract neoplasms encompass cancers of the nasopharynx, oral cavity, pharynx, larynx, hypopharynx, and salivary glands. Like leukemias and lymphomas where Mitoxantrone has established efficacy, these tumors are characterized by rapid cell proliferation and active DNA synthesis, providing a clear pharmacological basis for Topo II inhibitor sensitivity. This mechanistic overlap directly explains the TxGNN model's high-confidence prediction.

Clinical evidence has been accumulating since the early 1980s. Multiple Phase II trials have demonstrated measurable antitumor activity of Mitoxantrone in nasopharyngeal carcinoma (with full PK/PD profiling published in 1992), squamous cell carcinoma of the head and neck (HNSCC), salivary gland malignancies, and adenoid cystic carcinoma. Crucially, a next-generation liposomal formulation (PLM60 / Mitoxantrone Hydrochloride Liposome), already approved in China for peripheral T-cell lymphoma, completed a multicenter Phase 1b study in recurrent/metastatic HNSCC in 2025 (PMID 39952083), and a Phase 3 randomized controlled trial targeting nasopharyngeal carcinoma (NCT05717764, n=500) is planned — setting the stage for potential L1 evidence in the near term.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Phase 3 | Not Yet Recruiting | 60 | P-GEMD vs P-Gemox regimens in untreated early-stage non-upper aerodigestive tract or advanced-stage extranodal NK/T-cell lymphoma; anatomically related disease but targets lymphoma rather than solid epithelial tumors of the upper aerodigestive tract (Grade B relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Phase 1b Clinical Study | Oral Oncology | PLM60 (liposomal Mitoxantrone) evaluated for safety and efficacy in recurrent/metastatic HNSCC; PLM60 already China-approved for relapsed/refractory PTCL |
| [1735075](https://pubmed.ncbi.nlm.nih.gov/1735075/) | 1992 | Phase II PK/PD Study | Cancer | Mitoxantrone pharmacokinetics established in 15 advanced nasopharyngeal carcinoma patients; three-compartment model with terminal half-life ~71h; provides PK rationale for NPC use |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II Trial | Anti-Cancer Drugs | Mitoxantrone + cisplatin in 14 patients with recurrent/metastatic salivary gland malignancies; assessed safety and antitumor efficacy |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II Trial | Anti-Cancer Drugs | Ifosfamide + Mitoxantrone in recurrent/metastatic squamous cell carcinoma of the head and neck (n=22); 4-weekly cycles up to 6 courses |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II Trial (EORTC) | Annals of Oncology | EORTC multicenter Phase II of Mitoxantrone in adenoid cystic carcinoma of the head and neck; initiated based on prior case report activity |
| [36070368](https://pubmed.ncbi.nlm.nih.gov/36070368/) | 2022 | Pharmacogenomic Analysis | Science Translational Medicine | Established pharmacogenomic atlas of 56 HNSCC patient-derived cells; Mitoxantrone identified as a precision oncology candidate in specific molecular subtypes |
| [11269736](https://pubmed.ncbi.nlm.nih.gov/11269736/) | 2001 | Phase I Study | Cancer Chemotherapy and Pharmacology | Mitoxantrone + raltitrexed + levofolinic acid + 5-FU in advanced H&N and colorectal solid tumors; well-tolerated with clinical activity noted |
| [37776708](https://pubmed.ncbi.nlm.nih.gov/37776708/) | 2023 | Preclinical Screen | Redox Biology | Small molecule screen in NRF2-activated esophageal SCC (ESCC) identified actionable targets; contextual evidence for upper GI aerodigestive tract chemosensitivity |
| [3512224](https://pubmed.ncbi.nlm.nih.gov/3512224/) | 1986 | Review | Drug Intelligence & Clinical Pharmacy | Foundational review of Mitoxantrone; explicitly notes activity in head and neck cancer alongside breast cancer and leukemia/lymphoma |
| [32183950](https://pubmed.ncbi.nlm.nih.gov/32183950/) | 2020 | Basic Science | Cancer Cell | ADORA1 inhibition upregulates PD-L1 via ATF3; PD-1 blockade synergizes with ADORA1 antagonism — provides immunotherapy combination rationale relevant to Mitoxantrone's immunogenic cell death properties |

---

## India Market Information

Mitoxantrone currently has **no registered products in India**. There are no approved licenses, authorized product names, or dosage forms on record in the Indian regulatory database. Any future use would require a full regulatory submission and approval pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthraquinone/Anthracenedione class (Topo II inhibitor + DNA intercalator) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are primary dose-limiting toxicities; nadir typically at days 10–14 post-infusion |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (at least weekly during active treatment), liver function tests (LFTs), renal function, **cardiac function (LVEF by echocardiogram or MUGA scan)** — cumulative cardiomyopathy is a class-defining risk requiring mandatory dose tracking |
| Handling Protection | Must follow cytotoxic drug handling regulations; blue-green urine and scleral discoloration are expected and non-harmful but should be disclosed to patients |

---

## Safety Considerations

**Drug Interactions** (355 total interactions identified; key interactions listed below):

| Interacting Drug | Severity | Clinical Consideration |
|------|------|------|
| Dolasetron | Major | Additive QTc prolongation risk; avoid concurrent use if possible |
| Clarithromycin | Moderate | CYP3A4 inhibition may increase Mitoxantrone exposure |
| Eliglustat | Moderate | Metabolic interaction; requires close monitoring |
| Rolapitant | Moderate | CYP2D6 inhibition; potential pharmacokinetic interaction |
| Levofloxacin | Minor | Mild additive QT risk; clinical monitoring advisable |

Full prescribing warnings and contraindications are not available in the current evidence pack. Please refer to the official package insert / prescribing information for complete safety guidance before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Over 40 years of Phase II clinical evidence across multiple upper aerodigestive tract tumor types (NPC, HNSCC, adenoid cystic carcinoma, salivary gland malignancies) provides a well-established biological and clinical basis for this prediction. The modern liposomal formulation (PLM60) has already completed Phase 1b in HNSCC with published results (2025), and a Phase 3 RCT (NCT05717764, n=500) in nasopharyngeal carcinoma is advancing — making near-term L1 evidence realistic.

**To proceed, the following is needed:**
- Obtain the full package insert / SmPC to document contraindications and key warnings (currently a blocking data gap)
- Confirm detailed mechanism of action from DrugBank or primary pharmacology literature
- Establish baseline and periodic LVEF monitoring protocol to manage cumulative cardiotoxicity risk
- Assess ABCG2/BCRP expression as a potential biomarker for resistance selection in HNSCC patients
- Track recruitment and interim results of NCT05717764 (Phase 3, n=500, nasopharyngeal carcinoma) — this trial alone could upgrade evidence to L1
- Initiate India regulatory pathway assessment for market entry, as Mitoxantrone is currently unregistered in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

