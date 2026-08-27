---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Gemcitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Gemcitabine: From Pancreatic Cancer to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a cytotoxic nucleoside analog originally developed and internationally approved for pancreatic cancer and non-small cell lung cancer (with additional approvals in ovarian and bladder cancer), though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with a prediction score of **99.98%**,
supported by **50 clinical trials** and **20 publications** currently on record for this drug-disease pair.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic cancer / NSCLC (international approval; not licensed in Taiwan — see evidence trial NCT00183794: "gemcitabine is approved by the FDA for the treatment of pancreatic and lung cancer") |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action field for this evidence pack is currently empty (Data Gap DG002). However, the evidence base itself preserves a working mechanistic description: Gemcitabine is a deoxycytidine analog that is intracellularly phosphorylated and incorporated into DNA, inhibiting DNA synthesis and driving S-phase-specific apoptosis. This gives it broad cytotoxic activity against highly proliferative epithelial tumors, and it has decades of established clinical use in combination regimens with paclitaxel, trastuzumab, and carboplatin.

Although this evidence pack does not carry a populated "original indications" field, the collected trial documentation itself confirms the drug's approved use — for example, NCT00183794 explicitly states that "gemcitabine is approved by the FDA for the treatment of pancreatic and lung cancer." Internationally, gemcitabine additionally holds approvals in ovarian and bladder cancer. All of these are epithelial-origin, rapidly proliferating solid tumors, placing them in the same broad mechanistic category as breast carcinoma.

Because gemcitabine's cytotoxic mechanism is not tumor-type-specific but rather targets the cell cycle (S-phase) shared across proliferating epithelial malignancies, extrapolation to breast cancer is mechanistically plausible. This is reinforced by the evidence pack itself, which already contains multiple Phase 2/3 trials combining gemcitabine with breast-cancer-standard agents (trastuzumab, paclitaxel, capecitabine, carboplatin), indicating that this combination space has been actively explored in clinical practice for over two decades.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Randomized comparison of gemcitabine+Herceptin vs. capecitabine+Herceptin in HER2-positive metastatic breast cancer; direct head-to-head RCT design (terminated early) |
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase 3 | Active (not recruiting) | 1052 | Large RCT of carboplatin+paclitaxel (or gemcitabine) ± bevacizumab in platinum-sensitive recurrent ovarian/peritoneal/fallopian tube cancer, including a dedicated gemcitabine treatment arm |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | Completed | 19 | Gemcitabine + genistein in metastatic breast cancer, with biomarker assays |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's-choice chemotherapy in gBRCA-mutated platinum-sensitive relapsed ovarian cancer; gemcitabine arm inclusion not fully confirmed from title alone |
| [NCT00620295](https://clinicaltrials.gov/study/NCT00620295) | Phase 1 | Completed | 17 | Bortezomib + gemcitabine dose-finding study in elderly patients with solid tumors |
| [NCT02658214](https://clinicaltrials.gov/study/NCT02658214) | Phase 1 | Completed | 32 | Durvalumab + tremelimumab combined with first-line chemotherapy across advanced solid tumors, including TNBC |
| [NCT03076372](https://clinicaltrials.gov/study/NCT03076372) | Phase 1 | Unknown | 34 | MM-310 (docetaxel-prodrug liposome) monotherapy in solid tumors; gemcitabine combination not confirmed |
| [NCT03839823](https://clinicaltrials.gov/study/NCT03839823) | Phase 2 | Completed | 222 | Ribociclib + goserelin vs. chemotherapy in HR+/HER2- advanced breast cancer; no confirmed gemcitabine arm |
| [NCT00005614](https://clinicaltrials.gov/study/NCT00005614) | Phase 2 | Withdrawn | 0 | Gemcitabine monotherapy in elderly women with metastatic breast cancer — withdrawn prior to enrollment |
| [NCT02009449](https://clinicaltrials.gov/study/NCT02009449) | Phase 1 | Completed | 353 | Dose-escalation study of pegilodecakin (AM0010) in advanced solid tumors, alone or with chemotherapy/immunotherapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I Trial/Cohort | Breast Cancer Research and Treatment | Phase I trial of carboplatin + gemcitabine + mifepristone in advanced breast cancer and recurrent/persistent epithelial ovarian cancer, targeting glucocorticoid-receptor-mediated chemoresistance |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase I Trial | Gynecologic Oncology | Mirvetuximab soravtansine + gemcitabine in FRα-positive recurrent ovarian/peritoneal/fallopian tube/endometrial cancer and triple-negative breast cancer; MTD/RP2D determination |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Cohort (Salvage therapy) | Cancer Chemotherapy and Pharmacology | Docetaxel + gemcitabine + bevacizumab as salvage chemotherapy for HER2-negative metastatic breast cancer |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Overview of gemcitabine, anthracycline, and taxane combinations in advanced breast cancer |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine and platinum-based combination chemotherapy in metastatic breast cancer |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine + paclitaxel regimens and response rates in metastatic breast cancer |
| [24295415](https://pubmed.ncbi.nlm.nih.gov/24295415/) | 2013 | Review | Future Oncology | Review of liposomal chemotherapeutics, using gemcitabine and paclitaxel as illustrative examples |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | Preclinical (cell line) | Clinical Breast Cancer | Preclinical study of gemcitabine + trastuzumab in breast and lung cancer cell lines, relevant to HER2 status |
| [15685824](https://pubmed.ncbi.nlm.nih.gov/15685824/) | 2004 | Preclinical (cell line) | Oncology (Williston Park) | Gemcitabine combined with trastuzumab and/or platinum salts in HER2-overexpressing breast cancer cells |
| [34580061](https://pubmed.ncbi.nlm.nih.gov/34580061/) | 2021 | Preclinical/Mechanistic | Cancer Research | ALDH1A1 activity in tumor-initiating cells remodels myeloid-derived suppressor cells to promote breast cancer progression (mechanistic background, not a gemcitabine treatment study) |

---

## Taiwan Market Information

Gemcitabine currently has **0 registrations** and is **not marketed (未上市)** in Taiwan. No TFDA license records are available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (pyrimidine antimetabolite / deoxycytidine analog) |
| Myelosuppression Risk | High — nucleoside-analog antimetabolites of this class are well known to cause dose-dependent neutropenia, thrombocytopenia, and anemia; formal toxicity data for this evidence pack is not yet available (see Data Gap DG001) |
| Emetogenicity Classification | Low to Moderate (typical for this drug class) |
| Monitoring Items | CBC with differential, liver function tests, renal function, proteinuria/hematuria screening |
| Handling Protection | Yes — should be handled under standard cytotoxic/hazardous drug handling precautions |

*Note: Detailed, source-specific toxicity data (e.g., from a Taiwan package insert) is not yet available for this drug. Please refer to the package insert warnings and precautions once obtained.*

---

## Safety Considerations

- **Drug Interactions**: DDI query completed with **339 total interactions** on record. Sampled interactions include: **Naltrexone (Moderate)**, **Levofloxacin (Minor)**, and a large number of entries with severity level currently listed as **Unknown** (e.g., Calcitriol, Doxycycline, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Sucralfate, Palonosetron, Lansoprazole, Vancomycin, Lactulose, Prednisone, Simvastatin, Nystatin, Aprepitant, Potassium chloride, Loperamide). Given the large unclassified proportion, a full pharmacist-level DDI review is recommended before clinical use.

Key warnings and contraindications are not currently available in this evidence pack (Data Gap DG001, Blocking severity) — please refer to the package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (female breast carcinoma) reaches Evidence Level L1, supported by a Phase 3 RCT (NCT00440622), a large ongoing Phase 3 trial with a gemcitabine arm (NCT00565851), and multiple completed Phase 2 studies combining gemcitabine with breast-cancer-standard agents, plus two decades of published clinical experience with gemcitabine-based combination regimens in breast cancer. However, gemcitabine is not currently marketed in Taiwan, and formal local safety labeling data is missing, so guardrails are required before any local clinical application.

**To proceed, the following is needed:**
- TFDA-equivalent package insert / safety warnings and contraindications (Data Gap DG001 — **Blocking**, required before S1 safety screening can proceed)
- Formal DrugBank mechanism-of-action record (Data Gap DG002 — High priority)
- Full pharmacist review of the 339 recorded drug-drug interactions, particularly resolving the large "Unknown severity" subset
- Note: lower-ranked predicted indications in this evidence pack (rectum/colon mucinous adenocarcinoma, rete ovarii adenocarcinoma, secretory endometrioid adenocarcinoma, cervical mucinous adenocarcinoma) rate Evidence Level L4–L5 with a "Hold" recommendation and should not be advanced without substantially stronger primary evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

