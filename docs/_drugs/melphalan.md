---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 522
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Melphalan"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
description: "Melphalan: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Melphalan
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

## Melphalan: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug, originally used to treat ovarian cancer.
with **7 clinical trials** and **1 publication** currently listed for this direction. Most of the trials test melphalan as one part of high-dose multi-drug regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (13 of 13) – CDSCO approval status is not included in this data |
| Number of Registrations | 13 (valid: 13) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, melphalan is a bifunctional alkylating agent that cross-links DNA. Its efficacy in ovarian cancer is established, and mechanistically it may be applicable to gonadal germ cell tumor.

Germ cell tumors are highly sensitive to DNA-damaging chemotherapy. This supports the use of high-dose melphalan with autologous stem cell rescue in relapsed or poor-prognosis disease. Ovarian cancer and gonadal germ cell tumor are related, since ovarian germ cell tumors appear among the original ovarian indications.

An important limitation is that melphalan is given inside multi-agent regimens in the supporting studies. Its individual contribution cannot be separated out.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) in relapsed poor-prognosis germ-cell tumors |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with stem cell support and amifostine in solid tumors, including germ cell tumors |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant in hematologic malignancies and selected solid tumors; germ cell results not isolated |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced and recurrent tumors |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | Completed | 174 | High-dose chemotherapy with or without total-body irradiation before autologous transplant; heterogeneous population |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for neoplastic meningitis; different route and setting |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as a chemoprotectant with transplant in pediatric solid tumors; supportive care focus |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Other | Acta - Unio Internationalis Contra Cancrum | Early report on the effects of hormonal and alkylating drugs on pituitary follicle-stimulating function; no abstract and limited relevance to efficacy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 138154 | Megval 50mg Injection | Vial of 1 injection | Not listed |
| 4057 | Alkeran 2mg Tablet | Strip of 25 tablets | Not listed |
| 5060 | Alphalan 5mg Tablet | Strip of 25 tablets | Not listed |
| 5301 | Alkacel 50 Injection | Vial of 1 powder for injection | Not listed |
| 9297 | Alphalan 50mg Injection | Vial of 1 injection | Not listed |

All 13 registrations are valid single-ingredient products. They include both oral tablets and injectable forms.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The graph links melphalan to blood-count disorders (thrombocytopenia, anemia, leukopenia, neutropenia, agranulocytosis, hemolytic anemia), kidney disease, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury and vasculitis.
- **Drug Interactions**: 234 interactions are recorded. Moderate-level interactions include amphotericin B and its lipid, cholesteryl sulfate and liposomal formulations. Minor-level interactions include cimetidine, levofloxacin, and zinc sulfate and gluconate.
- **Other safety concerns from the literature**: Alkylating agents such as melphalan carry a risk of second malignancies, mostly acute leukaemia. High-dose regimens with stem cell rescue add substantial toxicity.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (n=64) directly addresses relapsed germ-cell tumors, and several smaller transplant studies support high-dose melphalan. However, melphalan is only one component of the regimens, the other studies are early-phase or mixed-population, and published literature specific to this indication is nearly absent. Evidence therefore supports a research question rather than a clinical recommendation.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products (currently a blocking gap for safety screening)
- Approved indication text for the Indian registrations
- Detailed mechanism of action data
- Published results from the completed Phase 2 trial (NCT00936936) and analysis separating melphalan's contribution from the rest of the regimen
- A safety monitoring plan covering myelosuppression, renal and pulmonary function, and second malignancy risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

