---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Decitabine
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

# Decitabine: From Myelodysplastic Syndrome to Refractory Cytopenia of Childhood

## One-Sentence Summary

Decitabine is a DNA hypomethylating agent (DNMT inhibitor) approved internationally for adult Myelodysplastic Syndrome (MDS) treatment.
The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood (RCC)**,
with **0 registered clinical trials** and **1 observational study** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adult Myelodysplastic Syndrome (MDS) |
| Predicted New Indication | Refractory Cytopenia of Childhood (RCC) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Decitabine is a nucleoside analog that acts as a DNA methyltransferase (DNMT) inhibitor — a class known as hypomethylating agents (HMAs). It incorporates into DNA and irreversibly inhibits DNMT, causing global DNA hypomethylation that reactivates silenced tumour suppressor genes and promotes differentiation of abnormal haematopoietic progenitor cells.

Refractory Cytopenia of Childhood (RCC) is the most common subtype of paediatric MDS, characterized by peripheral blood cytopenias with a hypocellular or normocellular bone marrow. Critically, RCC and adult MDS share the same core pathological mechanism: aberrant DNA hypermethylation silencing haematopoietic differentiation genes. Because Decitabine's mechanism directly targets this shared pathology, its therapeutic rationale for RCC is mechanistically coherent — not merely analogical.

From a clinical strategy perspective, Decitabine is proposed as a bridge-to-transplant therapy in paediatric MDS/RCC: reducing disease burden prior to allogeneic haematopoietic stem cell transplantation (allo-HSCT) to improve transplant outcomes. The TxGNN score of 0.9903 reflects a strong knowledge-graph structural association between Decitabine and RCC, consistent with this mechanistic reasoning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(ClinicalTrials.gov and ICTRP searches returned 0 results for Decitabine + Refractory Cytopenia of Childhood, as of 2026-03-27.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Retrospective Cohort / Case Series | BMC Pediatrics | Single-centre 10-year experience using Decitabine + minimally myelosuppressive regimen (DAC + MMR) as bridge to allo-HSCT in paediatric MDS; reports transplant outcomes for children receiving this HMA-based bridging strategy |

---

## India Market Information

Decitabine currently has **no registered products** in India. There are no marketing authorisations on record.

---

## Cytotoxicity

Decitabine is an antineoplastic agent (nucleoside analog / DNA hypomethylating agent used for haematologic malignancy). The following cytotoxicity profile applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Hypomethylating agent (nucleoside analog class) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anaemia are the most common dose-limiting toxicities |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (prior to each cycle and as clinically indicated), liver function tests, serum creatinine, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed system transfer, PPE required) |

---

## Safety Considerations

Detailed package insert warnings and contraindications are not available in this Evidence Pack. Please refer to the originator package insert (e.g., Dacogen® SmPC/USPI) for complete safety information.

**Key Drug Interactions** (from DDI database, 120 interactions total — major interactions listed below):

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Deferiprone | **Major** | Additive myelosuppression risk (bone marrow toxicity) |
| Adalimumab | **Major** | Immunosuppression potentiation; increased infection risk |
| Baricitinib | **Major** | Additive immunosuppression; risk of serious infection |
| Samarium (¹⁵³Sm) lexidronam | **Major** | Additive bone marrow suppression |
| Mercaptopurine | Moderate | Additive haematological toxicity |
| Gemcitabine | Moderate | Additive myelosuppression |
| Azathioprine | Moderate | Additive immunosuppression |
| Zidovudine | Moderate | Additive bone marrow suppression |
| Ganciclovir | Moderate | Additive myelosuppression |
| Palifermin | Moderate | Timing considerations with chemotherapy administration |

> ⚠️ Note: 4 Major interactions involve agents that are also frequently used in paediatric haematology (e.g., immunosuppressants, radioimmunotherapy). Careful medication reconciliation is essential if Decitabine is used as bridging therapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to a single retrospective single-centre case series (L3), with no registered prospective clinical trials for this specific indication. While the mechanistic rationale is compelling and TxGNN confidence is very high (99.03%), the paediatric-specific safety and efficacy data are insufficient to move forward without additional investigation.

**To proceed, the following is needed:**

- **Prospective clinical trial data**: Identify or initiate a Phase 1/2 trial of Decitabine in paediatric RCC/MDS as a bridge-to-HSCT strategy
- **Full MOA data**: Retrieve complete pharmacology and mechanism-of-action data from DrugBank (DG002)
- **Safety package insert**: Download and parse TFDA/EMA/FDA SmPC for Decitabine to obtain official warnings, contraindications, and paediatric dosing (DG001)
- **Paediatric PK/PD data**: Confirm appropriate dosing for children (weight-based, age-stratified)
- **Expanded literature search**: Search for additional paediatric MDS HMA studies beyond the current single publication
- **Regulatory landscape assessment**: Evaluate whether orphan drug designation or paediatric investigation plan (PIP) has been filed in any jurisdiction for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

