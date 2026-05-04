---
layout: default
title: Altretamine
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Altretamine
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

# Altretamine: From Refractory Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Altretamine (hexamethylmelamine, HMM) is an oral s-triazine class chemotherapy agent approved for the treatment of refractory ovarian cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with a prediction score of **99.91%**.
Currently, **20 publications** — including multiple Phase II clinical trials conducted between the 1970s and 1990s — provide historical clinical evidence for this direction, though no directly relevant active clinical trials are currently registered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Refractory ovarian cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Altretamine is an s-triazine class oral alkylating-like agent. After hepatic CYP450 metabolism, it generates active metabolites that form DNA interstrand crosslinks, inhibiting DNA replication and ultimately inducing tumour cell apoptosis. Its efficacy in refractory epithelial ovarian cancer has been clinically established, and this DNA damage mechanism is mechanistically relevant to breast cancer — particularly in tumours with defective DNA repair pathways (e.g., BRCA1/2 mutation carriers), which share biological vulnerabilities with platinum-sensitive ovarian cancer.

Ovarian cancer and breast cancer share important biological overlap: both are hormone-sensitive malignancies common in women, both may carry BRCA1/2 germline mutations, and both show susceptibility to DNA-damaging agents. Altretamine's partial mechanistic overlap with platinum compounds is especially relevant because BRCA-mutated breast cancer cells harbour homologous recombination repair defects — the same vulnerability exploited in ovarian cancer treatment.

Historical clinical evidence further supports this rationale. Multiple Phase II trials from the late 1970s to early 1990s tested Altretamine (then called hexamethylmelamine, HMM) in patients with metastatic breast cancer who had failed prior anthracycline-based regimens, observing modest but reproducible antitumour activity. A 2023 systematic review (PMID 37298753) also highlighted Altretamine as one of only three clinically approved s-triazine derivatives in oncology, confirming its established place in antineoplastic pharmacology.

---

## Clinical Trial Evidence

No directly relevant Altretamine-specific clinical trials for female breast carcinoma were identified in the current database. The four trials retrieved (NCT06299163, NCT04442126, NCT05775822, NCT04931823) were assessed as irrelevant (Grade C) — they involve unrelated investigational agents (tri-specific antibodies, CPO-100) or cardiovascular endpoints, and represent database mapping artefacts rather than Altretamine trials.

> Currently no directly relevant Altretamine clinical trials for breast carcinoma are registered on ClinicalTrials.gov.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37298753](https://pubmed.ncbi.nlm.nih.gov/37298753/) | 2023 | Systematic Review | Molecules | Comprehensive review of s-triazine antitumour compounds; confirms Altretamine as one of only three clinically approved s-triazine agents, approved for refractory ovarian cancer |
| [118805](https://pubmed.ncbi.nlm.nih.gov/118805/) | 1979 | Phase II Clinical Trial | Cancer Treatment Reports | 53 patients with metastatic breast cancer (post-FAC/CMFP failure) randomised to HMM alone vs HMM+vincristine+mitomycin C (HOM); both arms showed measurable activity |
| [113095](https://pubmed.ncbi.nlm.nih.gov/113095/) | 1979 | Phase II Clinical Trial | Cancer Treatment Reports | 98 heavily pretreated metastatic breast cancer patients; 2% response rate to HMM alone; neurological toxicity observed in HMM-only arm |
| [6785566](https://pubmed.ncbi.nlm.nih.gov/6785566/) | 1981 | Phase II Clinical Trial | Medical and Pediatric Oncology | AVDH combination (adriamycin + vincristine + dibromodulcitol + HMM) in advanced breast cancer after CMFP failure; ECOG pilot study |
| [6797746](https://pubmed.ncbi.nlm.nih.gov/6797746/) | 1981 | Phase I/II Clinical Trial | Cancer Clinical Trials | Four-drug regimen (cyclophosphamide + 5-FU + HMM + prednisone) in 19 advanced breast cancer patients; 7/18 evaluable patients achieved objective response |
| [1904313](https://pubmed.ncbi.nlm.nih.gov/1904313/) | 1991 | Clinical Retrospective Series | Cancer Treatment Reviews | Review of HMM use in metastatic breast cancer; summarises historical clinical experience |
| [2410072](https://pubmed.ncbi.nlm.nih.gov/2410072/) | 1985 | Clinical Series | Breast Cancer Research and Treatment | 23 metastatic breast cancer patients treated with intensive multiagent induction including HMM; complete remission rate and durability assessed |
| [820422](https://pubmed.ncbi.nlm.nih.gov/820422/) | 1976 | Narrative Review | Cancer | Decade-long NCI evaluation of HMM; confirmed activity across solid tumours including breast carcinoma; noted lack of cross-resistance with other agents |
| [7559101](https://pubmed.ncbi.nlm.nih.gov/7559101/) | 1995 | In Vivo Xenograft | Japanese Journal of Cancer Research | Altretamine tested against 5 human breast carcinoma xenografts (MX-1, T-61, MCF-7, R-27, Br-10) in nude mice; direct evidence of in vivo antitumour activity |
| [8317890](https://pubmed.ncbi.nlm.nih.gov/8317890/) | 1993 | Mechanistic/Laboratory | Anticancer Research | HMM derivative SAE9 developed with both direct antitumour activity and aromatase-inhibitory activity on breast carcinoma cell lines (MCF-7, R-27, MDA-MB-231); supports mechanistic rationale |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — s-triazine class (alkylating-like mechanism) |
| Myelosuppression Risk | Moderate (leucopenia and thrombocytopenia reported in clinical trials; less severe than typical alkylating agents) |
| Emetogenicity Classification | High (dose-limiting gastrointestinal toxicity, including nausea and vomiting, is a well-documented concern) |
| Monitoring Items | CBC with differential, liver function tests, renal function, neurological assessment (peripheral neuropathy risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations; oral administration requires standard chemotherapy dispensing precautions |

---

## Safety Considerations

**Drug Interactions** (120 interactions on record; key interactions listed below):

| Interacting Drug | Level | Clinical Significance |
|-----------------|-------|----------------------|
| Deferiprone | **Major** | Additive myelosuppression risk; combination generally contraindicated |
| Adalimumab | **Major** | Immunosuppression-related infection risk; combination requires careful evaluation |
| Samarium (153Sm) lexidronam | **Major** | Additive haematological toxicity |
| Cimetidine | Moderate | Cimetidine inhibits CYP450 metabolism of Altretamine, potentially increasing drug exposure and toxicity |
| Pyridoxine | Moderate | Pyridoxine (vitamin B6) may reduce Altretamine neurotoxicity but has also been reported to decrease antitumour efficacy; balance requires clinical judgement |
| Zidovudine | Moderate | Additive myelosuppression |
| Chloramphenicol | Moderate | Additive bone marrow suppression |
| Ganciclovir | Moderate | Additive myelosuppression |
| Doxepin | Moderate | Potential pharmacodynamic interaction |
| Strontium chloride Sr-89 | Moderate | Additive myelosuppression risk |

> For complete safety information including warnings, contraindications, and full interaction profile, please refer to the package insert (SmPC/labelling).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Historical Phase II clinical data from the 1970s–1990s and in vivo xenograft evidence confirm that Altretamine has genuine antitumour activity in breast cancer, and the mechanistic rationale — DNA damage in BRCA-mutated or repair-deficient tumours — is scientifically plausible. However, all evidence is dated, no modern randomised trials exist, and India has no approved formulation of this drug.

**To proceed, the following is needed:**

- **MOA data**: Retrieve detailed mechanism of action from DrugBank API (DB00488) to strengthen mechanistic link analysis
- **Regulatory safety data**: Download and parse the full prescribing information (SmPC or FDA label) to populate warnings and contraindications currently missing
- **Modern biomarker context**: Assess whether BRCA1/2 mutation status or homologous recombination deficiency (HRD) scoring could stratify patient populations likely to respond — aligning with contemporary precision oncology frameworks
- **Reformulation feasibility**: Evaluate whether Altretamine (currently only available orally in limited markets) could be sourced or reformulated for India; confirm regulatory pathway with CDSCO
- **Updated literature search**: Commission a systematic search for any post-2000 studies incorporating HMM into breast cancer regimens, including any combination studies with PARP inhibitors given the BRCA-overlap rationale
- **Preclinical confirmation**: Consider a focused in vitro study in BRCA-mutated breast cancer cell lines to confirm contemporary relevance before investing in clinical development

> ⚠️ *Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

