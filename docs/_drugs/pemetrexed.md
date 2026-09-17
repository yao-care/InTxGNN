---
layout: default
title: Pemetrexed
parent: High Evidence (L1-L2)
nav_order: 649
evidence_level: L2
indication_count: 10
---

# Pemetrexed
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Pemetrexed: From Malignant Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate originally established (with cisplatin) as standard chemotherapy for malignant pleural mesothelioma and non-squamous NSCLC. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, a rarer disease arising from the same mesothelial cell lineage, with **11 clinical trials** and **20 publications** currently supporting this direction — though most evidence comes from Phase 1/2 studies rather than confirmatory Phase 3 trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant pleural mesothelioma (with cisplatin); India-specific approved label text not available in this evidence pack |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field in this evidence pack is marked as a data gap, but the mechanistic evidence embedded in the model's rationale is informative: Pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — key enzymes in de novo purine and pyrimidine synthesis. This blocks DNA replication in rapidly dividing cells.

Malignant peritoneal mesothelioma and malignant pleural mesothelioma are histogenetically the same disease — both arise from mesothelial cells, differing only in anatomical site of origin (pleura vs. peritoneum), and share highly overlapping histological and molecular features. Pemetrexed plus cisplatin is already the de facto standard-of-care backbone used off-label for peritoneal mesothelioma in clinical practice, largely extrapolated from its confirmed activity in pleural disease.

Given that TS is highly expressed in mesothelioma cells regardless of anatomical site, the biological rationale for extending pemetrexed's antifolate activity to peritoneal disease is sound. However, the evidence base for peritoneal mesothelioma specifically consists mainly of Phase 1/2 studies (several combined with cytoreductive surgery/HIPEC or investigational agents) rather than an independent large confirmatory Phase 3 RCT — this is best understood as evidence-supported off-label extension of an established combination, not a *de novo* mechanistic prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | ALIMTA (pemetrexed) plus gemcitabine as front-line chemotherapy for pleural or peritoneal mesothelioma; assessed safety, survival, and tumor response |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized trial comparing intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for malignant peritoneal mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Maintenance talazoparib following first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | Methoxyamine (TRC102) combined with cisplatin and pemetrexed in solid tumors/mesothelioma, including cases refractory to pemetrexed-cisplatin |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab combined with pemetrexed and cisplatin for unresectable malignant peritoneal mesothelioma |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Carboplatin/pemetrexed/bevacizumab ± atezolizumab in peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | PIPAC plus systemic chemotherapy (cisplatin+pemetrexed) vs. systemic chemotherapy alone as 1st-line treatment |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 (arginine-degrading enzyme) with pemetrexed and cisplatin in arginine-dependent tumors including peritoneal mesothelioma |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed, and imatinib mesylate in unresectable/metastatic malignant mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | First-line vorinostat with pemetrexed-cisplatin in malignant pleural mesothelioma (trial withdrawn before enrollment) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Comprehensive review of treatment approaches for malignant peritoneal mesothelioma, including systemic chemotherapy role |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management overview of malignant peritoneal mesothelioma |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and Peritoneum | Bidirectional chemotherapy enabling surgery and HIPEC in initially unresectable peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective | Jpn J Clin Oncol | Efficacy and safety of pemetrexed plus cisplatin as first-line chemotherapy in advanced malignant peritoneal mesothelioma — no standard regimen previously established |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective | Expert Rev Anticancer Ther | First-line pemetrexed plus cisplatin chemotherapy specifically evaluated in malignant peritoneal mesothelioma |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Rep | Patient with malignant peritoneal mesothelioma responded to rechallenge with cisplatin and pemetrexed after prior response |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Overview review of malignant peritoneal mesothelioma including treatment landscape |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center study | Ann Surg Oncol | Treatment strategies and outcomes across a multi-center peritoneal mesothelioma cohort |
| [29423664](https://pubmed.ncbi.nlm.nih.gov/29423664/) | 2018 | Review | Ann Surg Oncol | Current management and future opportunities for peritoneal mesothelioma |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | J Immunother | Chemoimmunotherapy in platinum-nonresponsive metastatic peritoneal mesothelioma after prior chemotherapy |

---

## India Market Information

Pemetrexed is currently **not marketed** in India according to this evidence pack (`market_status: Not marketed`, 0 registrations). No license records are available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — multitargeted antifolate (inhibits TS, DHFR, GARFT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: A DDI query identified **367 total interactions**. Among these, several Moderate-level interactions (source: DDInter) are notable, including H2-receptor antagonists (Famotidine, Ranitidine, Cimetidine), NSAIDs (Acetylsalicylic acid), nephrotoxic/renally-cleared agents (Amphotericin B and its lipid/liposomal formulations, Vancomycin, Kanamycin, Neomycin, Polymyxin B, Levofloxacin), 5-ASA compounds (Mesalazine, Balsalazide, Olsalazine), Metformin, and Sapropterin. Given pemetrexed's renal elimination pathway, interactions with nephrotoxic or renally competing agents warrant particular attention.

Key warnings and contraindications data were not available in this evidence pack — please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 1/2 trials and a substantial literature base (including retrospective series specifically evaluating pemetrexed+cisplatin in peritoneal mesothelioma) support biological plausibility and real-world off-label use, but no confirmatory Phase 3 RCT exists for the peritoneal-specific indication — evidence level is L2, warranting guarded rather than unconditional advancement.

**To proceed, the following is needed:**
- Drug label/warning data (currently blocking — DG001)
- Formal, structured mechanism-of-action documentation from DrugBank (DG002)
- India-specific regulatory and market registration data (drug not currently marketed)
- Peritoneal-mesothelioma-specific safety monitoring plan, given the drug's extensive interaction profile (367 identified interactions) and lack of populated toxicity/myelosuppression data in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

