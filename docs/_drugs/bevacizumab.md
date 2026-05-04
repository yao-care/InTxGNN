---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Colorectal Cancer to Cystic Neoplasm

## One-Sentence Summary

Bevacizumab is a recombinant humanized monoclonal antibody that blocks VEGF-A to inhibit tumour angiogenesis, first approved for metastatic colorectal cancer and subsequently extended to multiple solid tumours including NSCLC, glioblastoma, renal cell carcinoma, and ovarian cancer.

The TxGNN model predicts it may be effective for **Cystic Neoplasm** — principally ovarian serous/mucinous cystic carcinoma and pseudomyxoma peritonei — with **8 clinical trials** and **20 publications** currently supporting this direction.

Among 10 predicted indications evaluated in this multi-indication pack, cystic neoplasm is the only actionable candidate, achieving **Evidence Level L1** with a landmark Phase III RCT (N = 1,052) as core support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic colorectal cancer (first approval, 2004); also NSCLC, glioblastoma, RCC, cervical cancer, and ovarian/fallopian tube/primary peritoneal cancer |
| Predicted New Indication | Cystic Neoplasm (ovarian serous/mucinous carcinoma; low-grade serous carcinoma; pseudomyxoma peritonei) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Market Status | ✗ Not Registered in Current Database |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Multi-Indication Overview

This evidence pack covers 10 TxGNN-predicted indications. Prediction scores are closely clustered (99.89–99.90%), reflecting a broad anti-angiogenic signal rather than indication-specific discrimination. The table below summarises all 10 candidates:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|------------|----------------|---------|
| 1 | Epiglottis neoplasm | 99.90% | L5 | Hold |
| 2 | Benign neoplasm of tongue | 99.90% | L4 | Hold |
| 3 | Tumour of testis and paratestis | 99.90% | L5 | Hold |
| 4 | Benign neoplasm of hypopharynx | 99.90% | L5 | Hold |
| 5 | Benign neoplasm of floor of mouth | 99.90% | L4 | Hold |
| 6 | Cervical neuroblastoma | 99.89% | L4 | Research Question |
| **7** | **Cystic neoplasm** | **99.89%** | **L1** | **Proceed with Guardrails** |
| 8 | Nasal cavity inverting papilloma | 99.89% | L4 | Hold |
| 9 | Mesenchymoma | 99.89% | L5 | Hold |
| 10 | Schwannoma of jugular foramen | 99.89% | L5 | Hold |

**Hold indications (Ranks 1–5, 8–10):** Most are benign tumours or rare mesenchymal/neural conditions without documented VEGF dependency. Anti-VEGF therapy has no established biological rationale in benign lesions (epiglottic cysts, tongue papillomas, hypopharyngeal polyps) where new blood vessel formation is not a pathological driver. The high TxGNN scores likely reflect training bias toward anatomical proximity in the head-and-neck tumour cluster, not indication-specific signal.

**Cervical neuroblastoma (Rank 6 — Research Question):** Assigned above Hold due to a case report of olfactory neuroblastoma (an analogous head-neck neural tumour) achieving durable palliation with bevacizumab-based anti-angiogenic therapy (PMID 22826790). VEGF is upregulated in the neuroblastoma microenvironment, and bevacizumab has been explored in abdominal neuroblastoma. This constitutes a weak but mechanistically coherent hypothesis warranting dedicated literature surveillance.

The remainder of this report focuses on **cystic neoplasm** as the primary actionable finding.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Bevacizumab is a recombinant humanized IgG1 monoclonal antibody that selectively binds and neutralises all biologically active isoforms of VEGF-A, preventing its interaction with VEGFR-1 and VEGFR-2 on vascular endothelial cells. This blockade suppresses tumour-driven angiogenesis — the formation of new blood vessels essential for solid tumour growth, invasion, and metastatic spread.

Cystic neoplasms of the ovary (serous, mucinous, and borderline/low-grade subtypes) as well as pseudomyxoma peritonei are among the most angiogenesis-dependent malignancies in gynaecologic oncology. VEGF-A drives not only tumour neovascularisation in these cancers but also the secretion of malignant ascites — a defining and debilitating complication of advanced ovarian disease. By blocking VEGF-A, bevacizumab simultaneously suppresses tumour vasculature and ascites formation, a dual mechanism particularly relevant to cystic tumour pathobiology.

The TxGNN prediction is strongly grounded in established evidence. Bevacizumab has already obtained FDA/EMA regulatory approval for platinum-sensitive and platinum-resistant recurrent epithelial ovarian carcinoma. The cystic neoplasm category extends this rationale to understudied subtypes — specifically low-grade serous carcinoma (LGSOC), mucinous cystic carcinoma, and pseudomyxoma peritonei — where emerging clinical data (PMID 38328890, PMID 37657955, PMID 37754507) demonstrate clinically meaningful responses even in the setting of conventional chemotherapy resistance.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase III | Active, Not Recruiting | 1,052 | ⭐ Core evidence: carboplatin/paclitaxel (or gemcitabine) ± bevacizumab followed by bevacizumab maintenance ± secondary cytoreductive surgery in platinum-sensitive recurrent ovarian, primary peritoneal, and fallopian tube cancer. Largest and highest-grade trial in this evidence pack. |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Phase II | Active, Not Recruiting | 133 | Atezolizumab + bevacizumab in rare solid tumours; immune-checkpoint plus anti-VEGF combination strategy potentially applicable to rare cystic subtypes such as pseudomyxoma peritonei |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Phase II | Completed | 97 | Bevacizumab + irinotecan in paediatric recurrent/progressive gliomas and low-grade gliomas, including tumours with prominent cystic components; provides additional safety reference |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase I/II | Completed | 66 | Erlotinib + cetuximab ± bevacizumab in metastatic RCC, colorectal, head and neck, pancreatic, and NSCLC; broad bevacizumab tolerability reference across solid tumour histologies |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Phase I | Completed | 39 | Bevacizumab + 5-FU/hydroxyurea with concurrent radiotherapy in poor-prognosis head and neck cancer; early characterisation of bevacizumab safety in combination regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Prospective Clinical Study | Future Oncology | N = 51 recurrent LGSOC; objective response rate 54.1% (CR 10.4%, PR 43.7%); median PFS 15 months with bevacizumab ± chemotherapy — strongest direct evidence for bevacizumab in chemo-resistant cystic ovarian subtype |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | Clinical Trial | Clinical Colorectal Cancer | Mitomycin-C + metronomic capecitabine + bevacizumab in unresectable/relapsed pseudomyxoma peritonei of appendiceal origin; demonstrates efficacy in a traditionally chemoresistant cystic mucinous tumour |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | RCT Ancillary Study | European Journal of Cancer | Ancillary analysis of PAOLA-1 Phase III RCT; BRCA1/RAD51C methylation as predictive biomarker for bevacizumab/olaparib maintenance in HGSOC — supports biomarker-guided patient selection |
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Systematic Review | Current Oncology | Systematic review of bevacizumab in LGSOC; evidence supports clinically meaningful activity in this chemo-resistant, rare ovarian cystic subtype with limited standard options |
| [24978709](https://pubmed.ncbi.nlm.nih.gov/24978709/) | 2014 | Clinical Study | Int J Gynecol Cancer | Bevacizumab shows significant clinical activity in low-grade serous ovarian and primary peritoneal cancer; establishes proof-of-concept in this VEGF-dependent cystic malignancy |
| [27154293](https://pubmed.ncbi.nlm.nih.gov/27154293/) | 2016 | Clinical/Translational | J Translational Medicine | GNAS mutations as prognostic biomarker in relapsed pseudomyxoma peritonei treated with metronomic capecitabine + bevacizumab; identifies a molecularly defined subgroup for targeted therapy |
| [27141073](https://pubmed.ncbi.nlm.nih.gov/27141073/) | 2016 | Review | Annals of Oncology | Comprehensive review of mucinous epithelial ovarian carcinoma; discusses diagnostic challenges, chemoresistance mechanisms, and systemic therapy options including anti-VEGF approaches |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Review / Guidelines | Current Oncology Reports | First-line management of advanced HGSOC; bevacizumab (with or without PARP inhibitor maintenance) is positioned as a standard-of-care component in eligible patients |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | Clinical Series | Clin Transl Oncol | Oral metronomic cyclophosphamide + bevacizumab in heavily pre-treated recurrent ovarian cancer; demonstrates activity in later-line cystic malignancies with an oral convenience regimen |
| [29752717](https://pubmed.ncbi.nlm.nih.gov/29752717/) | 2018 | Preclinical/Translational | Int J Cancer | Dose-dense vs conventional paclitaxel + cisplatin ± bevacizumab in preclinical ovarian cancer models; investigates scheduling optimisation for bevacizumab combination regimens |

---

## Market Information

Bevacizumab is **not registered** in the current regulatory database (0 active licences).

> **Context:** Bevacizumab (Avastin®, Roche/Genentech) holds regulatory approval in the USA (FDA), EU (EMA), Japan (PMDA), and numerous other major markets for ovarian cancer and additional solid tumours. Multiple biosimilars are also approved internationally (Mvasi®, Zirabev®, and others). The absence of registration in this local database likely reflects a local market gap rather than global non-availability. A formal registration or biosimilar bridging pathway should be evaluated before clinical use.

---

## Cytotoxicity

Bevacizumab is an antineoplastic biologic agent used exclusively for malignant tumours. Its original indication involves cancer treatment, and it belongs to the anti-angiogenic targeted therapy class.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Anti-VEGF monoclonal antibody (humanized IgG1 biologic; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Low (bevacizumab itself does not suppress bone marrow; haematological toxicity in clinical practice arises from concurrent cytotoxic chemotherapy partners, not bevacizumab) |
| Emetogenicity Classification | Low (as monotherapy; overall emetogenicity of the regimen is determined by the accompanying chemotherapy) |
| Monitoring Items | Blood pressure at each visit (hypertension occurs in ~25–35% of patients; most common bevacizumab AE); urine dipstick / protein-to-creatinine ratio (proteinuria, nephrotic syndrome); coagulation parameters and platelet count (arterial/venous thromboembolic events); wound inspection before each cycle (impaired wound healing / dehiscence); CBC if combined with cytotoxics; neurological assessment (posterior reversible encephalopathy syndrome, rare but serious) |
| Handling Protection | Standard biological agent aseptic preparation in a clean/ISO Class 5 environment; personal protective equipment per institutional biologic handling guidelines; cytotoxic-specific closed-system transfer devices are not mandatory for bevacizumab alone but may be required by institutional policy when co-prepared with cytotoxic agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For the cystic neoplasm indication, bevacizumab is supported by a Phase III RCT (N = 1,052) as core evidence alongside over 20 publications including prospective clinical studies, a systematic review, and translational biomarker studies in ovarian serous/mucinous carcinoma and pseudomyxoma peritonei subtypes. The anti-VEGF mechanism is well-validated in VEGF-dependent cystic tumours, and bevacizumab holds established regulatory approval for related ovarian cancer indications in major global markets. However, cystic neoplasm is histologically heterogeneous — efficacy and evidence strength differ substantially by subtype (HGSOC > LGSOC > mucinous > pseudomyxoma peritonei) — and the drug is not currently registered in this local database.

**To proceed, the following is needed:**
- Download and review the full prescribing information / package insert to resolve the blocking safety data gap (DG001 — warnings and contraindications)
- Confirm mechanism of action details from DrugBank to complete mechanistic link analysis (DG002)
- Define the specific cystic neoplasm subtype of interest (HGSOC, LGSOC, mucinous carcinoma, or pseudomyxoma peritonei) since evidence quality and recommended combination partners differ by histology
- Determine local regulatory registration pathway: assess whether originator Avastin® or an approved biosimilar can be registered or accessed under compassionate use or named-patient programmes
- Resolve the DDInter database file path error (query log ID 1) to enable drug-drug interaction profiling before clinical planning
- Establish a patient safety monitoring protocol addressing hypertension, proteinuria, thromboembolic events, and wound healing risk — particularly important for any perioperative use in ovarian cancer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

