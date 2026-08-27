---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 1
---

# Irinotecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Irinotecan: From Colorectal Cancer to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan (CPT-11) is a topoisomerase I inhibitor prodrug, globally established as a first-line chemotherapy backbone for colorectal cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **22 clinical trials** and **20 publications** currently supporting this direction.
Most notably, its active metabolite SN-38 has already been independently validated in breast cancer through two separate Phase 3 RCTs via the antibody-drug conjugate sacituzumab govitecan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (globally approved; no registration currently held in India) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Irinotecan is a prodrug of the camptothecin class. After administration, hepatic and intestinal carboxylesterases (CES1/CES2) hydrolyze it to SN-38, its pharmacologically active metabolite. SN-38 potently inhibits topoisomerase I (TOP1) by stabilizing the reversible TOP1-DNA cleavage complex into a stable, irreversible covalent adduct. This blocks the progression of the replication fork during the S phase of the cell cycle, causing lethal double-strand DNA breaks and triggering apoptosis. Because rapidly proliferating tumor cells are uniquely vulnerable to this mechanism, irinotecan exerts broad antineoplastic activity across multiple solid tumor types beyond its primary colorectal cancer indication.

Breast cancer shares key biological characteristics with colorectal cancer that make irinotecan mechanistically applicable: high cellular proliferation rates, documented topoisomerase I overexpression in breast tumor tissue relative to normal tissue, and sensitivity to agents that collapse the DNA replication machinery. Direct clinical evidence for free irinotecan in breast cancer includes two Phase 2 trials — NCT00072852 (134 enrolled, completed) evaluating single-agent irinotecan in anthracycline- and taxane-pretreated metastatic disease, and NCT03562390 (124 enrolled) in a Chinese patient population under the same treatment-refractory setting.

Most compellingly, the mechanistic validity of SN-38/TOP1 inhibition in breast cancer has been confirmed at the highest level of clinical evidence through sacituzumab govitecan, an antibody-drug conjugate that delivers SN-38 directly to Trop-2-expressing breast tumor cells. The ASCENT Phase 3 RCT demonstrated a significant overall survival benefit in triple-negative breast cancer, and the TROPiCS-02 Phase 3 RCT demonstrated a progression-free survival benefit in HR+/HER2− metastatic breast cancer. These two independent Phase 3 confirmations establish that SN-38 is effective in breast cancer biology, providing strong mechanistic reinforcement for the TxGNN model's prediction for free irinotecan in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Randomized comparison of two irinotecan oral schedules (5-day vs 14-day) as single-agent in women with metastatic breast cancer after failure of anthracycline, taxane, and capecitabine — the core efficacy trial for free irinotecan in breast cancer |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Open-label single-arm trial of irinotecan as ≥ third-line therapy in Chinese patients with locally recurrent or metastatic breast cancer previously treated with anthracyclines and taxanes (2017–2021) |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 (CHK1 inhibitor) plus irinotecan in refractory solid tumors; Part II enrolled exclusively triple-negative breast cancer patients from 2007, providing safety and tolerability data for irinotecan-based combinations in TNBC |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma; studied irinotecan-mediated sensitisation of breast cancer cells to capecitabine through modulation of thymidine phosphorylase |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | MM-398 (nanoliposomal irinotecan, Nal-IRI) tumor biodistribution study using ferumoxytol MRI in solid tumors including breast cancer; characterised intratumoral irinotecan drug delivery |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Navicixizumab monotherapy or combined with paclitaxel or irinotecan in advanced solid tumors; Cohort C specifically targets triple-negative breast cancer with the irinotecan combination arm |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | Sacituzumab govitecan (anti-Trop-2 antibody conjugated to SN-38, the active metabolite of irinotecan) in epithelial cancers including breast cancer; formed the pivotal basis for FDA approval in TNBC |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Phase 2 | Active, not recruiting | 350 | 9-ING-41 (GSK-3β inhibitor) alone or combined with cytotoxic agents including irinotecan in refractory solid tumors; includes breast cancer cohort in the Actuate 1801 platform study |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, not recruiting | 914 | Cabozantinib alone or combined with atezolizumab across multiple tumor types; includes a dedicated triple-negative breast cancer cohort; irinotecan evaluated as one of the combination partners |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101, a novel SN-38 nanoparticle formulation (the active metabolite of irinotecan), in advanced solid tumors; dose-escalation study providing PK and safety data for next-generation irinotecan delivery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 Study | European Journal of Cancer | PHENOMENAL trial: liposomal irinotecan (nal-IRI) in HER2-negative breast cancer with brain metastases; exploits the blood-brain barrier penetration of nal-IRI to address a critical unmet need in this subgroup |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 1/2 Trial | New England Journal of Medicine | IMMU-132-01 basket trial: sacituzumab govitecan (SN-38 payload) achieved a 33.3% ORR in heavily pretreated mTNBC, directly demonstrating efficacy of irinotecan's active metabolite in breast cancer |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | Phase 3 RCT | Journal of Clinical Oncology | TROPiCS-02: sacituzumab govitecan significantly improved PFS vs physician's choice in HR+/HER2− metastatic breast cancer (median 5.5 vs 4.0 months), validating SN-38/TOP1 inhibition across breast cancer subtypes |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Phase 2 Trial | Journal of Clinical Oncology | Sacituzumab govitecan in heavily pretreated mTNBC: 34% ORR and 7.7-month median response duration; established the first robust clinical proof-of-concept for SN-38 delivery in triple-negative breast cancer |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Phase 3 Protocol | Future Oncology | TROPiCS-02 design publication: articulates the scientific rationale for Trop-2-targeted SN-38 delivery in HR+/HER2− metastatic breast cancer and the endpoint framework that led to approval |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology | Mechanistic rationale for mitomycin plus irinotecan in advanced breast cancer: mitomycin upregulates topoisomerase I, sensitising breast cancer cells to irinotecan — establishes the earliest biological basis for irinotecan use in breast cancer |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology | Broad review of irinotecan's antitumor spectrum across cancer types including breast, ovarian, pancreatic, and small-cell lung cancers; foundational evidence base for irinotecan's multi-indication potential |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Systematic Review | Breast | Systematic review of TROP-2-directed ADCs including sacituzumab govitecan in metastatic breast cancer, synthesising clinical evidence from TNBC, HR+/HER2−, and HER2-low subtypes |
| [31208270](https://pubmed.ncbi.nlm.nih.gov/31208270/) | 2019 | Review | mAbs | Mechanistic review of anti-TROP-2 antibody conjugated to SN-38; explains why the camptothecin/TOP1 inhibitor mechanism is particularly suited to breast cancer biology and discusses the ADC linker strategy |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Phase 1/2 Study | Cancer | Pharmacokinetics and safety of sacituzumab govitecan across multiple cycles in epithelial cancers including breast cancer; characterises SN-38 exposure-response relationships directly relevant to irinotecan dosing strategies |

---

## India Market Information

Irinotecan currently holds **no registered authorisations in India** (0 licenses under CDSCO review). No licensed products are available through standard commercial channels. Clinicians or investigators seeking access would need to pursue importation under the Central Drugs Standard Control Organisation's special import licence framework, compassionate use provisions, or enrolment in an approved clinical trial.

---

## Cytotoxicity

Irinotecan is a conventional cytotoxic agent belonging to the camptothecin alkaloid class (topoisomerase I inhibitor). This section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Camptothecin / Topoisomerase I inhibitor |
| Myelosuppression Risk | High — dose-limiting neutropenia is the most common severe toxicity; UGT1A1\*28 homozygosity (*28/*28) markedly increases risk of grade 3–4 neutropenia and requires mandatory dose reduction |
| Emetogenicity Classification | Moderate (intravenous formulation); low–moderate (oral formulation) |
| Monitoring Items | CBC with differential before each cycle; liver function tests; renal function; UGT1A1 genotyping prior to initiation; electrolytes (especially sodium, potassium, magnesium — at risk from diarrhoea-related losses) |
| Handling Protection | Must follow cytotoxic drug handling regulations: appropriate PPE (gloves, gown, eye protection), closed-system drug transfer devices, dedicated preparation area, and hazardous pharmaceutical waste disposal |

---

## Safety Considerations

**Drug Interactions (435 total interactions identified):**
- **Major interaction — Clarithromycin**: Combined CYP3A4 and P-glycoprotein inhibition significantly increases plasma concentrations of irinotecan and SN-38, substantially elevating the risk of severe toxicity; co-administration should be avoided where possible
- **Moderate interactions (key examples)**:
  - *Aprepitant*: CYP3A4 inhibition may increase SN-38 exposure during the first cycle
  - *Dexamethasone*: CYP3A4 induction may reduce irinotecan efficacy; use with caution when given as antiemetic premedication
  - *Cimetidine*: P-glycoprotein inhibition may alter irinotecan disposition
  - *Miconazole*: Azole antifungal-mediated CYP3A4 inhibition increases toxicity risk
  - *Laxative/cathartic agents* (bisacodyl, castor oil, glycerin, lactitol, lactulose, magnesium citrate, magnesium hydroxide, mannitol, mineral oil, phenolphthalein, picosulfuric acid, eluxadoline): Concurrent use may compound irinotecan-induced early- and late-onset diarrhoea and electrolyte disturbances; use requires careful clinical judgement

For detailed key warnings and contraindications, please refer to the manufacturer's package insert, as CDSCO-specific prescribing information was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for irinotecan in female breast carcinoma is strongly plausible on mechanistic grounds and is backed by a substantial evidence base: two completed Phase 2 trials evaluated free irinotecan directly in anthracycline- and taxane-pretreated metastatic breast cancer, and two independent Phase 3 RCTs (ASCENT and TROPiCS-02) validated the efficacy of its active metabolite SN-38 (via sacituzumab govitecan) in both TNBC and HR+/HER2− subtypes — representing Level 1 mechanistic confirmation that TOP1 inhibition is active in breast cancer biology.

**To proceed, the following is needed:**
- **UGT1A1 genotyping protocol**: Mandatory prior to irinotecan initiation to identify *28/*28 patients requiring dose reduction; this is a patient safety prerequisite
- **CDSCO import authorisation**: Irinotecan is not registered in India; a special import licence or compassionate use pathway must be established before any patient access
- **Package insert review**: Obtain the full manufacturer summary of product characteristics for key warnings, contraindications, and India-specific dosing guidance
- **Subtype and line-of-therapy definition**: Align the development plan with existing Phase 2 data — TNBC (after ≥ 2 prior lines) and HR+/HER2− (after anthracycline/taxane failure) represent the best-characterised populations
- **Formulation strategy decision**: Evaluate whether liposomal irinotecan (Nal-IRI, as in the PHENOMENAL trial) may be preferable to conventional irinotecan for patients with CNS metastases
- **Pharmacovigilance plan**: Address the dual toxicity profile of severe neutropenia and delayed diarrhoea in the Indian patient population, including accessibility of G-CSF support and loperamide protocols at treating centres
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

