---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is a selective CDK4/6 inhibitor primarily used for the treatment of hormone receptor-positive (HR+), HER2-negative breast cancer, with multiple Phase 3 approvals supporting its efficacy in this setting.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- Breast Cancer |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided dataset. Based on known information, Abemaciclib is a selective oral inhibitor of cyclin-dependent kinases 4 and 6 (CDK4/6), which are master regulators of the G1-to-S phase transition in the cell cycle. Its efficacy in HR+/HER2- breast cancer is well-established across multiple pivotal Phase 3 trials (MONARCH series), and the molecular target — CDK4/6 — has biological relevance that extends beyond oncology.

CDK4/6 play central roles in T lymphocyte proliferation and activation. In rheumatoid arthritis (RA), autoreactive T cells and synovial fibroblasts undergo aberrant, unchecked proliferation that drives progressive joint inflammation and destruction. By inhibiting CDK4/6, Abemaciclib could theoretically suppress the clonal expansion of pathogenic T cells and downregulate NF-κB-mediated pro-inflammatory cytokine signaling — both key mechanisms in RA pathogenesis. This immunomodulatory rationale represents a biologically coherent, if unproven, mechanistic hypothesis.

However, the only available supporting evidence (PMID 40504547, 2025) is a pharmacovigilance observational study examining the incidence of immune-mediated diseases in breast cancer patients receiving CDK4/6 inhibitors. This study was not designed as a therapeutic evaluation of Abemaciclib in RA, and its findings are limited to safety surveillance. There is an important caveat: CDK4/6 inhibitors may paradoxically trigger autoimmune reactions, which means the relationship between this drug class and inflammatory disease requires careful bidirectional evaluation before any therapeutic application can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Observational / Pharmacovigilance | The Oncologist | Investigates prevalence of autoimmune diseases in HR+/HER2- breast cancer patients receiving CDK4/6 inhibitors with endocrine therapy; finds CDK4/6 inhibitors may enhance antitumor immunity but also trigger autoimmune reactions — provides an indirect, non-therapeutic signal regarding CDK4/6 inhibition and immune-mediated conditions such as RA |

---

## India Market Information

Abemaciclib is **not currently marketed in India**. No product registrations were found (0 licenses on record).

---

## Cytotoxicity

Abemaciclib is an antineoplastic targeted therapy approved for breast cancer treatment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Selective CDK4/6 inhibitor (small molecule kinase inhibitor) |
| Myelosuppression Risk | Moderate — neutropenia is a well-documented class effect of CDK4/6 inhibitors; dose reductions or interruptions are commonly required |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (neutrophil count at baseline, then periodically), liver function tests (ALT/AST), renal function, ECG for QTc interval |
| Handling Protection | Follow cytotoxic drug handling regulations applicable to oral targeted antineoplastic agents; avoid crushing tablets |

---

## Safety Considerations

**Drug Interactions**: 210 interactions identified in total (source: DDInter). Major interactions requiring clinical attention:

| Interacting Drug | Severity | Clinical Relevance |
|------|---------|------|
| Clarithromycin | Major | Strong CYP3A4 inhibitor — may significantly increase Abemaciclib plasma levels |
| Cobicistat | Major | Strong CYP3A4 inhibitor — pharmacokinetic interaction risk |
| Deferiprone | Major | Additive myelosuppression risk |
| Lumacaftor | Major | Strong CYP3A4 inducer — may reduce Abemaciclib efficacy |
| Samarium (153Sm) lexidronam | Major | Additive bone marrow suppression risk |
| Aprepitant | Moderate | Moderate CYP3A4 inhibitor |
| Dexamethasone | Moderate | CYP3A4 inducer — may reduce exposure |
| Erythromycin | Moderate | Moderate CYP3A4 inhibitor |
| Fluconazole | Moderate | CYP3A4 inhibitor |
| Ticagrelor | Moderate | Pharmacokinetic interaction |

Please refer to the package insert for complete warnings and contraindications (currently a data gap — TFDA package insert review pending).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score of 97.32% for Abemaciclib in rheumatoid arthritis, and a plausible mechanistic hypothesis exists (CDK4/6-mediated suppression of pathogenic T cell proliferation), the evidence base consists of only a single indirect pharmacovigilance study with no clinical trials in RA. Furthermore, emerging safety signals suggest CDK4/6 inhibitors may trigger rather than treat autoimmune conditions, warranting careful evaluation before committing resources to this indication.

**To proceed, the following is needed:**
- Retrieve detailed MOA data from DrugBank (DB12001) to formally document CDK4/6 inhibition mechanisms relevant to inflammation
- Commission preclinical RA model studies (e.g., collagen-induced arthritis mouse model) to validate CDK4/6 inhibition as a viable therapeutic strategy
- Conduct a systematic safety review specific to RA patient populations, with particular attention to whether CDK4/6 inhibitors exacerbate or ameliorate autoimmune inflammation (see PMID 40504547 paradox)
- Obtain and parse TFDA/FDA package insert to document warnings and contraindications, especially regarding immunosuppression, infections, and QTc prolongation
- Design a cardiac safety monitoring plan given documented QTc prolongation signals (from "heart disease" indication evidence in this same evidence pack)
- If preclinical data is supportive, conduct a focused literature review for any RA-adjacent inflammatory arthritis models where CDK4/6 inhibition has been tested

> ⚠️ **Note for reviewers**: The "heart disease" indication (rank 6) in this evidence pack contains high-quality safety evidence (systematic reviews and meta-analyses) documenting QTc prolongation and cardiotoxicity risk with CDK4/6 inhibitors, including Abemaciclib specifically. Any future clinical evaluation in RA must mandate cardiac safety monitoring as a primary safety endpoint.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation prior to any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

