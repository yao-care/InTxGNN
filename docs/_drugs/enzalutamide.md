---
layout: default
title: Enzalutamide
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Enzalutamide: predicted new indication Top-ranked: prostate cancer/brain cancer susceptibility . Best-suppor… (evidence level L5). Approved use: Prostate cancer (including familial prostate carcinoma)"
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate cancer/brain cancer susceptibility", "prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "male reproductive organ cancer", "benign prostate phyllodes tumor", "benign neoplasm of prostate", "prostate neoplasm", "prostate phyllodes tumor"]
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Male Reproductive Organ Cancer (Prostate Neoplasm)

## One-Sentence Summary

Enzalutamide is an androgen receptor inhibitor originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is "prostate cancer/brain cancer susceptibility", a germline susceptibility term with no evidence behind it. The best-supported candidates are **male reproductive organ cancer** (**35 clinical trials** and **20 publications**) and **prostate neoplasm** (**35 clinical trials** and **20 publications**). Both are essentially the already-approved prostate cancer indication rather than a genuinely new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (including familial prostate carcinoma) |
| Predicted New Indication | Top-ranked: prostate cancer/brain cancer susceptibility (no evidence). Best-supported: male reproductive organ cancer / prostate neoplasm |
| TxGNN Prediction Score | 99.71% (top-ranked); 99.51% (male reproductive organ cancer); 98.37% (prostate neoplasm) |
| Evidence Level | L1 for male reproductive organ cancer and prostate neoplasm (on-label evidence); L5 for the top-ranked prediction |
| India Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Proceed with Guardrails (restricted to prostate cancer); Hold for the other predictions |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on known pharmacology, enzalutamide is a second-generation androgen receptor (AR) signaling inhibitor. It blocks androgen binding, nuclear translocation of the AR, and AR binding to DNA.

The high-scoring predictions are mostly different labels for prostate disease or closely related ontology terms. "Male reproductive organ cancer" and "prostate neoplasm" are parent terms that contain prostate cancer, so the supporting trial and literature evidence is almost entirely on-label prostate cancer work. This is confirmation of the existing indication, not novel repurposing. No evidence was found for other male reproductive cancers such as testicular or penile cancer.

Other predictions are rare or benign prostate lesions (prostate leiomyoma, fibroma of prostate, benign prostate phyllodes tumor, prostate phyllodes tumor, benign neoplasm of prostate). They may be biologically conceivable through AR biology, but no trials or supporting literature exist. Brenner tumor has no known AR-driven biology, and its high score is likely a graph artifact. The top-ranked "prostate cancer/brain cancer susceptibility" is a germline susceptibility term, not a treatable disease state.

---

## Clinical Trial Evidence

The table below covers the best-supported prediction groups (male reproductive organ cancer and prostate neoplasm), selecting the most relevant trials. The other predictions have no registered trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Phase 3 | Active, not recruiting | 1125 | ENZAMET: enzalutamide vs conventional non-steroidal antiandrogen with first-line ADT in metastatic prostate cancer |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | Active, not recruiting | 600 | MEVPRO-1: mevrometostat plus enzalutamide vs enzalutamide or docetaxel in mCRPC after abiraterone |
| [NCT02987543](https://clinicaltrials.gov/study/NCT02987543) | Phase 3 | Completed | 387 | PROfound: olaparib vs enzalutamide or abiraterone in mCRPC with HRR gene mutations |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Phase 3 | Terminated | 1244 | KEYNOTE-641: pembrolizumab plus enzalutamide vs placebo plus enzalutamide in mCRPC |
| [NCT06136624](https://clinicaltrials.gov/study/NCT06136624) | Phase 3 | Recruiting | 1310 | OMAHA-003: opevesostat vs abiraterone or enzalutamide in heavily pretreated mCRPC |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) | Phase 3 | Recruiting | 500 | Standard of care ± 177Lu-PSMA-617 in poor-responding de novo mHSPC; enzalutamide likely in the backbone |
| [NCT03641560](https://clinicaltrials.gov/study/NCT03641560) | Phase 4 | Completed | 52 | Single-arm safety and efficacy study of enzalutamide in Indian patients with docetaxel-pretreated mCRPC |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | Not yet recruiting | 26 | Dose optimization of enzalutamide in elderly patients with advanced prostate cancer |
| [NCT04332744](https://clinicaltrials.gov/study/NCT04332744) | Phase 2 | Completed | 54 | Talazoparib plus enzalutamide in metastatic hormone-naïve prostate cancer |
| [NCT01547299](https://clinicaltrials.gov/study/NCT01547299) | Phase 2 | Completed | 52 | Neoadjuvant enzalutamide before prostatectomy in localized prostate cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22894553](https://pubmed.ncbi.nlm.nih.gov/22894553/) | 2012 | RCT (AFFIRM) | N Engl J Med | Enzalutamide increased survival in prostate cancer after chemotherapy |
| [29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/) | 2018 | RCT (PROSPER) | N Engl J Med | Enzalutamide in nonmetastatic castration-resistant prostate cancer with rapidly rising PSA |
| [31329516](https://pubmed.ncbi.nlm.nih.gov/31329516/) | 2019 | RCT (ARCHES) | J Clin Oncol | Enzalutamide plus ADT in metastatic hormone-sensitive prostate cancer |
| [41633900](https://pubmed.ncbi.nlm.nih.gov/41633900/) | 2026 | Post hoc analysis | Eur Urol | ARCHES 5-year efficacy and safety of enzalutamide plus ADT in mHSPC |
| [41124201](https://pubmed.ncbi.nlm.nih.gov/41124201/) | 2026 | RCT (EMBARK) | N Engl J Med | Improved overall survival with enzalutamide in biochemically recurrent prostate cancer |
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | RCT | N Engl J Med | PARP inhibitor plus androgen-signaling inhibition plus ADT in metastatic prostate cancer |
| [27477525](https://pubmed.ncbi.nlm.nih.gov/27477525/) | 2017 | Extended RCT analysis (PREVAIL) | Eur Urol | Longer-term efficacy and safety in chemotherapy-naïve mCRPC |
| [40439959](https://pubmed.ncbi.nlm.nih.gov/40439959/) | 2025 | Cohort | Adv Ther | Overall survival with apalutamide vs enzalutamide in mCSPC |
| [39275993](https://pubmed.ncbi.nlm.nih.gov/39275993/) | 2024 | Review | Expert Rev Anticancer Ther | Current uses and resistance mechanisms of enzalutamide |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends Cancer | Treatment advances in advanced prostate cancer |

---

## India Market Information

Enzalutamide has 17 valid registrations in India, all single-ingredient products. The approved indication text is not available for any of them. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 243972 | Xtandi 40mg Soft Capsule | Bottle of 112 capsules | Astellas Pharma Inc |
| 72884 | Enzamide 40mg Tablet | Strip of 28 tablets | Intas Pharmaceuticals Ltd |
| 1970 | Azel 40mg Capsule | Strip of 28 capsules | Dr Reddy's Laboratories Ltd |
| 72886 | Enzyl Capsule | Strip of 28 capsules | Sun Pharmaceutical Industries Ltd |
| 243863 | Xylutide Capsule | Strip of 28 capsules | Cipla Ltd |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; blood pressure, seizure risk, falls and fatigue are key clinical concerns |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 571 interactions were identified in total. Major-level interactions include bupropion, dolasetron and eliglustat. Moderate-level interactions include famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, clarithromycin, aprepitant, loperamide, saxagliptin, empagliflozin and linagliptin, among others.
- **Clinical risks to monitor** (from the assessment of the prostate neoplasm group): seizure, falls, fatigue, hypertension, and CYP-mediated drug interactions.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (restricted to prostate cancer); Hold for all other predicted indications**

**Rationale:**
- The strongest evidence (multiple completed Phase 3 RCTs such as AFFIRM, PROSPER, ARCHES and EMBARK, plus the ENZAMET trial) supports enzalutamide in prostate cancer, which is the already-approved use. It should be labeled as on-label confirmation rather than new repurposing, and not extended to other organ sites.
- The top-ranked prediction and the rare or benign prostate lesions, as well as Brenner tumor, have no trials or supporting literature (L5), so no clinical inference can be made.
- The "benign neoplasm of prostate" and "benign reproductive system neoplasm" predictions rely only on prostate cancer data and indirect preclinical work (L4), and the benefit-risk balance is unfavorable without dedicated studies.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Indian regulatory sources (currently missing and blocking safety screening)
- Detailed mechanism-of-action data from DrugBank
- Approved indication text for the Indian registrations
- Dedicated studies before any consideration of benign or rare prostatic or non-prostatic indications
- A drug-interaction management plan covering the major-level interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

