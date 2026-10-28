---
layout: default
title: Pertuzumab
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Pertuzumab"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab: predicted new indication Ectomesenchymoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Pertuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## One-Sentence Summary

Pertuzumab is a HER2-directed monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
Currently **1 clinical trial** and **20 publications** are linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ectomesenchymoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, pertuzumab binds the extracellular dimerization domain of HER2 and blocks HER2/HER3 heterodimerization. This inhibits downstream PI3K/AKT and MAPK signalling.

A share of HER2-positive tumours also express the progesterone receptor (HR+/HER2+ disease). In these tumours the HER2-directed mechanism still applies. This prediction is therefore mainly an extension of the approved HER2-positive breast cancer indication into a hormone-receptor-defined subgroup, not a truly novel indication.

Evidence applies only to HER2-positive disease. It should not be extended to HER2-negative, PR-positive cancers.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 vs reference pertuzumab, each with trastuzumab and docetaxel, in neoadjuvant HER2-positive, ER/PR-negative breast cancer. Direct support for pertuzumab in HER2-positive disease, but it is a biosimilar equivalence design and does not enrol PR-positive patients. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: neoadjuvant endocrine therapy plus trastuzumab and pertuzumab vs de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | J Clin Oncol | Survival analysis of WSG TP-II in HR+/HER2+ early breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 weeks of dual blockade with or without paclitaxel |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | Br J Cancer | Phase 3 equivalence of biosimilar QL1209 vs reference pertuzumab in HER2-positive, ER/PR-negative disease |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort / 5-year follow-up of a phase 2 RCT | Lancet Oncol | NeoSphere 5-year analysis of neoadjuvant pertuzumab plus trastuzumab |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | HR+/HER2+ breast cancer: cross-talk between hormone receptor and HER2 pathways |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | Cohort | Breast | Adjuvant ovarian function suppression and aromatase inhibitors in premenopausal HR+/HER2+ patients |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer | Signalling interactions and clinical translation in HR+/HER2+ breast cancer |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Review | South Med J | Overview of neoadjuvant and adjuvant breast cancer therapies |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 175277 | Perjeta 420mg Injection (Roche Products India Pvt Ltd) | Vial of 14 ml injection | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (myelosuppression is mainly associated with the combined chemotherapy, e.g., docetaxel) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; cardiac function monitoring is commonly used with anti-HER2 combinations, and cardiac safety was a focus of the TRYPHAENA and BERENICE studies |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**:
  - Idelalisib: Moderate interaction (DDInter).
  - Pertuzumab's pharmacological target is ERBB2 (HER2); this is a target relationship, not a drug interaction.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pertuzumab with trastuzumab is already established for HER2-positive breast cancer. Randomised evidence (WSG-TP-II) exists in HR+/HER2+ disease, and a completed Phase 3 trial supports the regimen in HER2-positive disease overall. The one registered trial linked to this prediction enrolled ER/PR-negative patients, so direct Phase 3 evidence in PR-positive disease is lacking.

**To proceed, the following is needed:**
- Confirmation of HER2-positive status; the prediction must not be applied to HER2-negative, PR-positive cancers
- Package insert warnings and contraindications for the India-marketed product
- Detailed mechanism of action data from DrugBank
- Clarification of the approved indication wording on the India licence (currently blank)
- A cardiac safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

