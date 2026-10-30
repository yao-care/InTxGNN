---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Bleomycin: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Hodgkin lymphoma, non-Hodgkin lymphoma, head and neck cancer"
monitor_inn: "Bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Bleomycin
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

## Bleomycin: From Lymphoma and Head and Neck Cancer to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Bleomycin is a cytotoxic anticancer antibiotic, originally used for Hodgkin and non-Hodgkin lymphomas and head and neck cancer.
The TxGNN model's top-ranked prediction is **cauda equina neoplasm** (score 0.9930), but only **0 clinical trials** and **1 publication** support it. The best-supported candidate among the top six predictions is **reticulum cell sarcoma** (an obsolete term for aggressive B-cell lymphoma), with **11 clinical trials** and **20 publications**. That candidate largely overlaps with bleomycin's already-approved lymphoma use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, non-Hodgkin lymphoma, head and neck cancer (the India licence records contain no indication text) |
| Predicted New Indication | Cauda equina neoplasm (top-ranked prediction) |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 (model prediction only) |
| India Market Status | Listed in a compiled Indian medicine price dataset (18 of 18) – CDSCO approval status is not included in this data |
| Number of Registrations | 18 (valid: 18) |
| Recommended Decision | Hold |

**Other predictions reviewed:**

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Cauda equina neoplasm | 0.9930 | L5 | Hold |
| 2 | Adult astrocytic tumour | 0.9928 | L5 | Research Question |
| 3 | Reticulum cell sarcoma | 0.9914 | L5 | Proceed with Guardrails |
| 4 | Primary pulmonary lymphoma | 0.9910 | L4 | Research Question |
| 5 | Pulmonary blastoma | 0.9904 | L4 | Hold |
| 6 | Well-differentiated fetal adenocarcinoma of the lung | 0.9903 | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Bleomycin is a cytotoxic agent that causes DNA strand breaks, and it is already used in lymphoma regimens. Germ cell tumours are also known to be sensitive to it.

**Cauda equina neoplasm (rank 1):** No direct mechanistic link has been established. The only retrieved paper describes radiation therapy for relapsed CNS germinoma after a carboplatin, etoposide and bleomycin regimen. That is a weak, indirect connection, and it does not address cauda equina tumours. The high score is a model prediction without clinical support.

**Reticulum cell sarcoma (rank 3):** This is an old name for diffuse large B-cell or aggressive non-Hodgkin lymphoma. Bleomycin is already used in lymphoma regimens such as VACOP-B, ProMACE-CytaBOM and PMitCEBO. This is therefore closer to an existing indication than a true repurposing. Modern regimens (R-CHOP, DA-EPOCH-R) have largely replaced bleomycin-based ones for aggressive B-cell lymphoma.

**Adult astrocytic tumour (rank 2):** In principle, bleomycin's DNA damage could act on high-grade glioma cells, but the blood-brain barrier limits systemic delivery. A Phase I trial of continuous intratumoral infusion in recurrent glioblastoma suggests local delivery is feasible. A randomized trial found no survival benefit from adding bleomycin to radiotherapy.

---

## Clinical Trial Evidence

Clinical trials were found only for reticulum cell sarcoma (rank 3). No registered trials were found for the other five predictions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | Completed | 61 | Alternating triple therapy vs CHOP in intermediate-grade and immunoblastic lymphoma |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | Completed | 116 | Early intensification vs alternating triple therapy in poor-prognosis lymphoma |
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | Completed | 310 | CHOP vs PMitCEBO in good-risk aggressive non-Hodgkin lymphoma |
| [NCT00003815](https://clinicaltrials.gov/study/NCT00003815) | Phase 3 | Unknown | Not reported | High-dose chemotherapy/radiotherapy with autologous transplant in high-grade non-Hodgkin lymphoma |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | Completed | 5 | 72-hour continuous infusion bleomycin as salvage in AIDS-related and immunocompetent non-Hodgkin lymphoma |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | Completed | 52 | ProMACE-CytaBOM with antiviral therapy and G-CSF in AIDS-related lymphoma |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | Completed | 46 | Combination chemotherapy pilot in AIDS-related lymphoma |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | Completed | 20 | ProMACE-CytaBOM with immunosuppression modification in post-cardiac-transplant lymphoproliferation |
| [NCT00032149](https://clinicaltrials.gov/study/NCT00032149) | Phase 1/2 | Unknown | 30 | PMitCEBO plus G-CSF in good-prognosis HIV-related lymphoma |
| [NCT00031902](https://clinicaltrials.gov/study/NCT00031902) | Phase 1 | Unknown | Not reported | Rituximab plus PVB chemotherapy in HIV-related non-Hodgkin lymphoma |

Bleomycin is only one component of most of these regimens, so the trials do not isolate its individual contribution. A further trial, NCT00983944 (DA-EPOCH-R vs R-VACOP-B in primary mediastinal lymphoma), was withdrawn with no enrollment.

---

## Literature Evidence

Selected publications across the predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | Randomized trials (pooled analysis) | Eur J Cancer | Long-term efficacy of CHVmP/BV in 936 patients with aggressive non-Hodgkin lymphoma across three EORTC trials (reticulum cell sarcoma) |
| [6164465](https://pubmed.ncbi.nlm.nih.gov/6164465/) | 1981 | RCT | Cancer | In 118 patients with grade III-IV astrocytoma, bleomycin added to radiotherapy did not improve survival (adult astrocytic tumour) |
| [12416544](https://pubmed.ncbi.nlm.nih.gov/12416544/) | 2002 | Phase I trial | J Neurooncol | Continuous intratumoral bleomycin infusion in recurrent glioblastoma was feasible (adult astrocytic tumour) |
| [1698540](https://pubmed.ncbi.nlm.nih.gov/1698540/) | 1990 | Phase II trial | Cancer Res | Calmodulin inhibitor plus bleomycin in high-grade glioma (adult astrocytic tumour) |
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | Cohort | Br Med J | Single-agent bleomycin gave remissions in Hodgkin disease and other reticuloses, including reticulum cell sarcoma |
| [15202521](https://pubmed.ncbi.nlm.nih.gov/15202521/) | 2003 | Review | Leuk Lymphoma | MACOP-B followed by radiotherapy may be a better induction strategy in primary mediastinal B-cell lymphoma (reticulum cell sarcoma) |
| [2437659](https://pubmed.ncbi.nlm.nih.gov/2437659/) | 1987 | Case report | South Med J | Fatal pulmonary fibrosis after a low total bleomycin dose (20 units) in BACOP therapy |
| [31668826](https://pubmed.ncbi.nlm.nih.gov/31668826/) | 2020 | Cohort | J Geriatr Oncol | Association of advancing age with bleomycin pulmonary toxicity in Hodgkin lymphoma (primary pulmonary lymphoma) |
| [18827617](https://pubmed.ncbi.nlm.nih.gov/18827617/) | 2008 | Case report | J Thorac Oncol | Pulmonary blastoma with germ cell elements; markers responded to bleomycin, etoposide and cisplatin, but the tumour did not regress |
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort | J Clin Oncol | Radiation salvage for relapsed CNS germinoma after carboplatin, etoposide and bleomycin (cauda equina neoplasm) |

No literature was found for well-differentiated fetal adenocarcinoma of the lung. Several retrieved papers are off-topic (for example, radiotracer imaging and pulmonary fibrosis models).

---

## India Market Information

Bleomycin has 18 valid single-ingredient registrations in India. The records contain no approved indication text. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26306 | Bleomycin Sulphate Injection (Dabur India Ltd) | Vial of 1 ml injection | Not stated |
| 167240 | Oncobleo 15IU Injection (Sun Pharmaceutical Industries Ltd) | Vial of 1 injection | Not stated |
| 32205 | Bledmax 15mg Injection (Max India Ltd) | Vial of 1 powder for injection | Not stated |
| 29038 | Bleotex 15IU Injection (Alkem Laboratories Ltd) | Vial of 1 injection | Not stated |
| 219746 | Tumocin 15IU Injection (Neon Laboratories Ltd) | Vial of 1 ml injection | Not stated |

All are injectable forms.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-strand-scission antibiotic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. One report notes bleomycin has marrow-sparing properties. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Pulmonary function and symptoms (cough, dyspnoea) are essential, since fatal pulmonary fibrosis has been reported even at low total doses. Routine tests cannot reliably detect early, reversible lung toxicity. Also consider CBC and liver and renal function. |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Pulmonary toxicity:** Bleomycin can cause interstitial pneumonitis and fatal pulmonary fibrosis, including at low doses. Older age is being studied as a risk factor. Prior bleomycin lung toxicity may also bear on radiation pneumonitis risk. This matters especially for lung-based indications.
- **Hyperpyrexia:** A fatal hyperpyrexic reaction has been reported, so a test dose is recommended before therapy.
- **Drug Interactions:** 205 interactions are recorded. Only one is graded (levofloxacin, Minor). The rest have no severity grade, including pantoprazole, omeprazole, prednisone, morphine, vancomycin, clarithromycin and several antiemetics (palonosetron, aprepitant, granisetron, ondansetron).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (cauda equina neoplasm). **Proceed with Guardrails** applies only to reticulum cell sarcoma (aggressive B-cell lymphoma).

**Rationale:**
- Cauda equina neoplasm has a high model score but no registered trials and only one indirect publication, so it is a model prediction without clinical support.
- Reticulum cell sarcoma has the strongest evidence (L1, including several completed Phase 3 trials). However, it is essentially bleomycin's existing lymphoma use rather than new repurposing, and modern regimens have largely displaced bleomycin there.
- Adult astrocytic tumour remains a research question (L3). Older randomized data showed no survival benefit, and only a Phase I trial supports intratumoral delivery.
- The lung-related predictions (primary pulmonary lymphoma, pulmonary blastoma, fetal adenocarcinoma of the lung) are poor fits given bleomycin's pulmonary toxicity.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- Package insert warnings and contraindications from the India product labels, which are required before safety screening
- For cauda equina neoplasm, any direct clinical evidence beyond the single indirect germinoma paper
- For glioma, a pulmonary and neurological safety plan and further trials of local delivery
- For reticulum cell sarcoma, comparison against current standard regimens, plus a pulmonary toxicity monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

