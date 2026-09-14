---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 802
evidence_level: L5
indication_count: 10
---

# Tegafur
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

Using no additional skill — this is a direct report-writing task with a fully specified template; I'll follow the prompt exactly.

# Tegafur: From Gastrointestinal Cancer to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral prodrug of 5-fluorouracil (5-FU) and a core component of combination regimens (UFT, S-1) historically developed for gastric and other gastrointestinal cancers. The TxGNN model predicts it may also be effective for **Colonic Neoplasm**, with **30 clinical trials** and **20 publications** currently supporting this direction — largely reflecting real-world use of tegafur-containing regimens (UFT, S-1) that are already established therapies in colorectal cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in India regulatory data (drug not marketed); per associated literature, tegafur-based combinations (UFT, S-1) are used for gastric, colorectal, lung and breast cancer chemotherapy |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for tegafur is not available in this evidence pack. Based on known pharmacology, tegafur is a prodrug of 5-fluorouracil (5-FU), metabolized in vivo (via CYP2A6/DPD) to release 5-FU, which inhibits thymidylate synthase and disrupts DNA synthesis in rapidly dividing cells. Tegafur is the core cytotoxic component of two widely used combination regimens: UFT (tegafur + uracil, where uracil competitively inhibits DPD to increase 5-FU exposure) and S-1 (tegafur + gimeracil + oteracil, which further inhibits DPD and reduces GI toxicity).

Gastric cancer and colonic neoplasm are both gastrointestinal-tract adenocarcinomas that share fluoropyrimidine sensitivity as a class effect. Since tegafur's therapeutic activity depends on systemic 5-FU exposure rather than tumor-site-specific mechanisms, its applicability is not restricted to a single GI organ.

This mechanistic rationale is strongly reinforced by real-world clinical practice: tegafur-containing regimens (UFT, S-1) are already established, guideline-supported adjuvant and first-line therapies for colon and colorectal cancer in multiple countries (notably Japan), as reflected by the large number of completed Phase 3 RCTs in the evidence base below. The TxGNN prediction therefore aligns with existing clinical use rather than representing a novel, untested hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs capecitabine (± bevacizumab) as first-line therapy for metastatic colorectal cancer |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant UFT vs observation in curatively resected Stage II colon cancer |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | Completed | 89 | Cross-over comparison of Xeloda vs UFT+leucovorin in advanced/metastatic colorectal cancer, patient preference and safety |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | NSAS-CC: adjuvant UFT vs surgery alone in Dukes C colorectal cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs S-1 as adjuvant treatment for Stage III colon cancer, with gene-expression predictive factor analysis |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | Oral UFT+LV vs IV 5-FU+LV in resected Stage II/III colon cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1+oxaliplatin) vs XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Postoperative UFT+LV vs UFT+LV+PSK regimens for Stage III colorectal cancer |
| [NCT00497107](https://clinicaltrials.gov/study/NCT00497107) | Phase 3 | Unknown | 300 | UFT/LV vs UFT/LV+PSK as postoperative adjuvant therapy for Stage IIIa/IIIb colorectal cancer |
| [NCT02836977](https://clinicaltrials.gov/study/NCT02836977) | N/A | Unknown | 400 | Maintenance tegafur-uracil vs observation following adjuvant oxaliplatin-based regimen in Stage III colon cancer |

*(30 total clinical trials identified; 10 most relevant shown above.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (Phase 3) | Clinical Colorectal Cancer | ACTS-CC 02 trial: S-1+oxaliplatin (SOX) vs UFT/LV as adjuvant chemotherapy in high-risk Stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (updated survival) | ESMO Open | ACTS-CC 02 updated 5-year overall survival and subgroup analysis |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | Journal of Clinical Oncology | NSABP C-06: oral UFT+LV vs IV 5-FU+LV in Stage II/III colon carcinoma, comparable efficacy |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT (Phase 3) | Annals of Oncology | JFMC33-0502: optimal treatment duration for UFT/LV adjuvant therapy in Stage IIB/III colon cancer |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective observational | BMC Cancer | JFMC46-1201: UFT/LV efficacy in high-risk Stage II colon cancer using propensity score matching |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective controlled (final analysis) | International Journal of Clinical Oncology | JFMC46-1201 final results, updated 5-year OS and risk factor analysis |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohort study + meta-analysis | Medicine | Nationwide cohort: UFT vs 5-FU as postoperative adjuvant chemotherapy in Stage II/III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clinical Colorectal Cancer | Asian consensus guidelines adapting international metastatic colorectal cancer treatment recommendations |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT (tegafur+uracil) as adjuvant chemotherapy for solid tumors incl. colon/rectum: clinical evidence and mechanism |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | International Journal of Clinical Oncology | Adjuvant immunochemotherapy with OK-432 and oral pyrimidines (incl. UFT) for colorectal cancer |

*(20 total publications identified; 10 most relevant shown above, prioritizing RCTs and reviews.)*

---

## Cytotoxicity

Tegafur is a conventional cytotoxic antineoplastic agent (fluoropyrimidine class, prodrug of 5-FU); this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (5-FU prodrug) |
| Myelosuppression Risk | Moderate — class-level risk of neutropenia and leukopenia; a dedicated pharmacokinetic study (NCT05266300) highlights DPYD genotype as a key determinant of fluoropyrimidine toxicity risk |
| Emetogenicity Classification | Low to moderate (typical of oral fluoropyrimidine regimens) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; consider DPYD genotyping/phenotyping prior to initiation given known DPD-deficiency toxicity risk |
| Handling Protection | Must follow standard cytotoxic drug handling regulations (preparation, dispensing, and disposal per institutional hazardous drug protocols) |

No India/TFDA-specific toxicity label data is currently available; the above reflects general fluoropyrimidine-class knowledge and should be confirmed against the official package insert once obtained.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical efficacy evidence for tegafur-containing regimens in colorectal/colon cancer is strong (Evidence Level L1, ≥2 completed Phase 3 RCTs), but a **Blocking** data gap exists: no India/TFDA label warnings or contraindications are available, which prevents completion of the S1 safety initial screening. The drug is also currently not marketed in India (0 registrations), so the regulatory pathway is undefined.

**To proceed, the following is needed:**
- Official package insert / label data (warnings, contraindications) — required before S1 safety screening can proceed
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Drug-drug interaction (DDI) data (currently not found)
- Assessment of India regulatory pathway/feasibility given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

