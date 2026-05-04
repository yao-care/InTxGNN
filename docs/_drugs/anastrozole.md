---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: From HR-Positive Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation non-steroidal aromatase inhibitor, globally established as a standard-of-care endocrine therapy for hormone receptor-positive (HR+) breast cancer in postmenopausal women.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**—confirming and extending its established clinical role—
with **50 clinical trials** and **20 publications** currently supporting this direction, earning an **L1** evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormone receptor-positive (HR+) breast cancer — adjuvant and advanced/metastatic settings (globally recognised; no India licence on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Anastrozole acts as a potent, selective, reversible inhibitor of the aromatase enzyme (CYP19A1), which catalyses the final step of oestrogen biosynthesis—converting androgens (androstenedione, testosterone) to oestrogens (oestrone, oestradiol) in peripheral tissues, adipose, and breast tissue. In postmenopausal women, this peripheral aromatisation is the dominant oestrogen source; anastrozole suppresses circulating oestradiol by approximately 85%, starving oestrogen receptor-positive (ER+) tumour cells of their primary mitogenic signal.

Approximately 70–75% of all breast cancers are hormone receptor-positive, meaning ERα-mediated signalling directly drives tumour proliferation and survival. By blocking oestrogen biosynthesis upstream of the receptor, anastrozole interrupts this driver pathway more completely than tamoxifen, which only competitively blocks ER binding at the receptor level. This mechanistic advantage translated into superior disease-free survival in the landmark ATAC trial (N = 9,358) and is the basis for NCCN/ESMO first-line recommendations.

The TxGNN prediction of anastrozole for "female breast carcinoma" therefore represents a high-confidence model validation rather than a novel repurposing. The knowledge graph correctly captures the deep biological coupling between aromatase inhibition and breast cancer control, corroborated by landmark Phase 3 programmes (ATAC, IBIS-II, FACE, ENDEAVOR). The key operational gap is not scientific plausibility but market authorisation: anastrozole is not currently registered with CDSCO in India despite global approval in over 100 countries.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Completed | 9,358 | ATAC trial: Anastrozole alone vs tamoxifen alone vs combination as 5-year adjuvant treatment in postmenopausal HR+ localised breast cancer; anastrozole significantly prolonged disease-free survival |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | Completed | 7,576 | FACE trial: Exemestane vs anastrozole head-to-head in postmenopausal HR+ primary breast cancer (adjuvant); large-scale direct comparison, core efficacy evidence |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Completed | 4,172 | Letrozole vs anastrozole (each 5 years) as adjuvant therapy in HR+, lymph node-positive postmenopausal breast cancer; 5-year disease and survival follow-up |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Completed | 2,980 | IBIS-II DCIS: Anastrozole vs tamoxifen (5 years) after local excision of HR+ ductal carcinoma in situ in postmenopausal women |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Completed | 1,914 | Randomised comparison of 3-year vs 6-year anastrozole following 2–3 years of tamoxifen in postmenopausal HR+ early breast cancer; evaluates optimal AI duration |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | Completed | 3,420 | Denosumab vs placebo to reduce fracture risk in women with non-metastatic breast cancer receiving non-steroidal AI therapy (including anastrozole); safety support data |
| [NCT00256698](https://clinicaltrials.gov/study/NCT00256698) | Phase 3 | Completed | 514 | FACT trial: Anastrozole monotherapy vs anastrozole + fulvestrant (maximum oestrogen blockade) in HR+ breast cancer at first relapse after primary treatment |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Completed | 298 | Exemestane vs anastrozole as initial hormonal therapy in postmenopausal advanced/recurrent breast cancer; primary endpoint time to tumour progression |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3 | Completed | 301 | 4EVER trial: Everolimus + exemestane in ER+ postmenopausal breast cancer progressing on prior non-steroidal AI (anastrozole/letrozole); real-world safety and efficacy |
| [NCT06311383](https://clinicaltrials.gov/study/NCT06311383) | N/A (Observational) | Completed | 2,610 | Real-world German registry: Ribociclib + aromatase inhibitor/fulvestrant vs endocrine monotherapy vs chemotherapy as first-line in HR+/HER2− advanced breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT (long-term follow-up) | Lancet | IBIS-II: Anastrozole vs placebo for prevention in high-risk postmenopausal women; significant sustained reduction in breast cancer incidence confirmed at long-term follow-up |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT | Lancet | ATAC 5-year results: Anastrozole significantly prolonged disease-free survival vs tamoxifen (HR 0.87); fewer endometrial cancers and thromboembolic events |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS: Anastrozole superior to tamoxifen in preventing locoregional and contralateral breast cancer in postmenopausal women with HR+ DCIS |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis | Oncotarget | Systematic meta-analysis of RCTs comparing anastrozole vs tamoxifen; anastrozole demonstrates superior overall survival benefit and favourable toxicity profile as adjuvant therapy |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Phase 3 analysis | Clinical Pharmacology and Therapeutics | Pharmacogenomic analysis of MA.27 Phase III trial (N = 4,465): SNPs in CSMD1 associated with breast cancer-free interval; anastrozole vs exemestane differential response by genotype |
| [30499075](https://pubmed.ncbi.nlm.nih.gov/30499075/) | 2020 | Meta-analysis | Pathology Oncology Research | Meta-analysis of 7 RCTs evaluating endocrine therapy (tamoxifen/anastrozole) in DCIS after breast-conserving surgery + radiotherapy; anastrozole reduces local recurrence |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | GWAS / Phase 3 analysis | JCI Insight | Pharmacogenomics of AIs in postmenopausal breast cancer (MA.27): CSMD1 SNP identifies patients with fewer distant recurrences on anastrozole; CSMD1 regulates complement pathway |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Monograph | Expert Opinion on Drug Safety | Comprehensive safety and efficacy profile of anastrozole in adjuvant HR+ breast cancer; adjuvant RCT outcomes reviewed and superior benefit vs tamoxifen confirmed |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Comparative Review | Expert Opinion on Pharmacotherapy | Comparative review of anastrozole, letrozole, and exemestane across four adjuvant trial designs in early breast cancer; superiority over tamoxifen consistent across all three AIs |
| [40973715](https://pubmed.ncbi.nlm.nih.gov/40973715/) | 2025 | Review | British Journal of Cancer | 40-year perspective on oestrogen-targeted breast cancer prevention; plasma oestrogen levels shown to interact with anastrozole's preventive efficacy, informing future risk-stratified prevention strategies |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted endocrine therapy — Non-steroidal aromatase inhibitor (NOT conventional cytotoxic; no DNA damage mechanism) |
| Myelosuppression Risk | Low (anastrozole does not cause clinically significant bone marrow suppression) |
| Emetogenicity Classification | Minimal (not classified as emetogenic; nausea incidence < 10% in trials) |
| Monitoring Items | Bone mineral density (DEXA at baseline and annually); liver function tests; lipid profile; musculoskeletal symptom assessment — AI-associated musculoskeletal syndrome (AIMSS) occurs in 35–50% of patients and is a leading cause of treatment discontinuation |
| Handling Protection | Standard oral tablet handling; dedicated cytotoxic handling protocols not required |

---

## Safety Considerations

**Drug Interactions**: Anastrozole has 147 documented interactions recorded in the DDInter database. All listed interactions are currently classified as "Unknown" severity, indicating insufficient characterisation of clinical magnitude. Notable co-medications flagged include:

Bupropion, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Rosiglitazone, Lansoprazole, Prednisone, Simvastatin, Hydrocortisone, Prednisolone, Ondansetron, Famotidine, Acetylsalicylic acid, Glyburide, and Glipizide.

> Formal key warnings and contraindications data were not available in this evidence pack. Please refer to the approved package insert (SmPC / USPI) for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN's prediction of anastrozole for female breast carcinoma is fully supported by an extensive Phase 3 evidence base (L1 level). The science is unambiguous — multiple completed large-scale RCTs (ATAC N = 9,358; FACE N = 7,576; IBIS-II N = 3,864) establish anastrozole as a globally guideline-recommended agent. The primary barrier to use in India is regulatory absence, not scientific uncertainty.

**To proceed, the following is needed:**

- **CDSCO registration**: File an NDA or import licence application with the Central Drugs Standard Control Organisation to obtain marketing authorisation for anastrozole in India; reference global approvals (FDA, EMA) to leverage existing dossiers
- **Safety data gap closure**: Obtain and review the full SmPC / USPI to populate key warnings, contraindications, and risk factors including osteoporosis, cardiovascular effects, and teratogenicity (strictly contraindicated in premenopausal women and pregnancy)
- **Pharmacovigilance plan**: Establish protocols for bone mineral density monitoring, AIMSS surveillance, and lipid tracking tailored to the Indian patient population
- **Local population data assessment**: Evaluate whether South Asian-specific pharmacogenomic data (CYP19A1 polymorphism prevalence) or local HR+ breast cancer epidemiology warrants any label adaptation for CDSCO submission
- **Supply chain and access planning**: Anastrozole is available as a generic globally; assess pricing, procurement pathway, and integration into national cancer treatment guidelines (e.g., ICMR / NCCN India protocols)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

