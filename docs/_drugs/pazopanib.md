---
layout: default
title: Pazopanib
parent: Model Prediction Only (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib: predicted new indication Unclassified renal cell carcinoma (evidence level L5). Approved use: Not stated in the Indian licence records (approved indication text is…"
monitor_inn: "Pazopanib"
predicted_indications: ["fibroblastic neoplasm"]
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma and Soft Tissue Sarcoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Pazopanib is an oral multi-targeted tyrosine kinase inhibitor (VEGFR/PDGFR/c-KIT), originally used for renal cell carcinoma and soft tissue sarcoma.
The TxGNN model predicts it may be effective for **unclassified renal cell carcinoma**, supported by **6 publications** (no registered clinical trials).
Of the top 10 predictions, **liposarcoma** has the strongest trial evidence (**6 clinical trials**, **20 publications**), and it is discussed alongside the lead prediction below.

## Quick Overview

The lead indication is the highest-ranked prediction that has any supporting evidence. The three higher-ranked predictions (renal cell carcinoma associated with neuroblastoma, renal cell carcinoma with Xp11.2/TFE3 fusions) have no trials or literature.

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records (approved indication text is blank). The knowledge graph lists renal cell carcinoma (including clear cell) and soft tissue sarcoma. |
| Predicted New Indication | Unclassified renal cell carcinoma (rank 3; ranks 1 and 2 have no supporting evidence) |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L3 (retrospective series, real-world data and one single-arm Phase 2 study; no randomized or registered trials) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold (research question; see below) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, pazopanib is a multi-targeted inhibitor of VEGFR, PDGFR and c-KIT. This anti-angiogenic activity underlies its established use in clear cell renal cell carcinoma and soft tissue sarcoma.

Non-clear-cell and unclassified renal cell carcinomas depend on angiogenic signalling to a variable degree. This is why VEGF-pathway inhibitors are commonly extrapolated from clear cell disease to these tumours. These tumours are under-represented in trials, so such extrapolation is common in practice, but the strength of benefit is uncertain.

The sarcoma-related predictions follow a similar logic. Pazopanib's PDGFR activity is directly relevant to dermatofibrosarcoma protuberans (driven by the COL1A1-PDGFB fusion) and to fibroblastic tumours such as solitary fibrous tumour. Liposarcoma was excluded from the pivotal soft tissue sarcoma trial, so evidence there rests on Phase 2 studies, with modest and subtype-dependent efficacy.

## Clinical Trial Evidence

No clinical trials are registered for the lead prediction (unclassified renal cell carcinoma). Currently no related clinical trials registered.

The most relevant trials for the best-supported sarcoma predictions are shown below.

**Liposarcoma**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable or metastatic liposarcoma |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib in advanced or metastatic liposarcoma after relapse on standard therapy (population only partly confirmed) |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomized, double-blind: gemcitabine with or without pazopanib in refractory soft tissue sarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib plus oral topotecan in metastatic, non-resectable soft tissue and bone sarcoma |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Completed | 140 | Neoadjuvant pazopanib with or without chemoradiation in non-rhabdomyosarcoma soft tissue sarcoma (indirectly relevant) |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Maintenance pazopanib with radiotherapy in non-rhabdomyosarcoma soft tissue sarcoma (likely mostly pediatric) |

**Fibroblastic neoplasm and dermatofibrosarcoma protuberans**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) | Phase 2 | Completed | 96 | Single-agent pazopanib 800 mg daily in unresectable or metastatic solitary fibrous tumour and extraskeletal myxoid chondrosarcoma |
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Phase 2a | Terminated | 23 | Pazopanib in unresectable dermatofibrosarcoma protuberans; early termination limits conclusions |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | Phase 1/2 | Terminated | 151 | MLN0128 (TAK-228) versus pazopanib in advanced sarcoma; pazopanib was the comparator |

## Literature Evidence

**Unclassified renal cell carcinoma (lead prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 (single-arm) | Cancer Res Treat | Efficacy and safety of pazopanib in non-clear-cell RCC |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective multicenter | Clin Genitourin Cancer | PANORAMA: first-line pazopanib in non-clear-cell RCC |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Outcomes of metastatic non-clear-cell RCC treated with pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world | Ecancermedicalscience | Sunitinib versus pazopanib in non-clear-cell and sarcomatoid RCC |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Real-world cohort | Eur Urol Oncol | First-line therapy outcomes in metastatic non-clear-cell RCC (IMDC) |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospective cohort | Clin Genitourin Cancer | Carcinoma of unknown primary with RCC features treated with targeted therapy |

**Selected sarcoma literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 report | Expert Opin Investig Drugs | Pazopanib in advanced intermediate- or high-grade liposarcoma |
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Phase 2 | J Invest Dermatol | Multicenter Phase 2 of pazopanib in unresectable DFSP |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 | Br J Cancer | Pazopanib with oral topotecan in sarcoma |
| [25269954](https://pubmed.ncbi.nlm.nih.gov/25269954/) | 2014 | Preclinical and clinical | Eur J Cancer | Activity of pazopanib in solitary fibrous tumour |
| [29614488](https://pubmed.ncbi.nlm.nih.gov/29614488/) | 2018 | Retrospective | Oncology | Efficacy and safety in recurrent or metastatic solitary fibrous tumour |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Preclinical | Cancer Sci | Pazopanib identified as a potential inhibitor of the COL1A1-PDGFB fusion |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Commentary | Lancet Oncol | Pazopanib for advanced liposarcoma |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | Systemic treatment options for advanced liposarcoma |

## India Market Information

Approved indication text is blank in the licence records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 233990 | Votrient 200mg Tablet | Bottle of 30 tablets | Glaxo SmithKline Pharmaceuticals Ltd |
| 233449 | Votrient 400mg Tablet | Strip of 30 tablets | Glaxo SmithKline Pharmaceuticals Ltd |
| 177899 | Pazoci 200 Tablet | Bottle of 30 tablets | Cipla Ltd |
| 174988 | Pazoci 400 Tablet | Bottle of 30 tablets | Cipla Ltd |
| 180225 | Pazocam 200mg Tablet | Bottle of 30 tablets | Medicamen Biotech Ltd |

Two further registrations exist: Pazocam 400mg Tablet (175799) and Pazliz 400 Tablet (178266). All 7 registrations are valid single-ingredient oral tablets.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, blood pressure, ECG/QT and electrolytes, thyroid function, urinary protein, complete blood count (based on the contraindication and risk signals below) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease-level risk signals (knowledge graph, not label text)**: Conditions flagged as contraindicated include hypertension, long QT syndrome and torsades de pointes, liver failure and drug-induced liver injury, hyperbilirubinemia (including Gilbert syndrome), hypothyroidism, myocardial infarction, intracerebral hemorrhage, active peptic ulcer disease, pancreatitis, proteinuria, diarrheal disease, and electrolyte disorders (potassium deficiency, hypercalcemia, phosphorus metabolism disease). Cardiac and hepatic risks are especially relevant to heart fibrosarcoma and to patients with hepatic impairment.
- **Drug Interactions**: 519 interactions were identified. Major interactions include acid-suppressing agents (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), clarithromycin and dolasetron. Moderate interactions include dexamethasone, budesonide, aprepitant, loperamide, bisacodyl, pioglitazone, saxagliptin, eliglustat, magnesium oxide and polyethylene glycol with electrolytes.

Please refer to the package insert for approved warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For the lead prediction, unclassified renal cell carcinoma, the evidence is limited to retrospective series, real-world data and one single-arm Phase 2 study, with no randomized or registered trials (L3). Three top-ranked predictions have no evidence at all (L5). Liposarcoma (L2), fibroblastic neoplasm (L2) and dermatofibrosarcoma protuberans (L2) have Phase 2 evidence, but efficacy is modest, one DFSP trial was terminated early, and imatinib remains the standard targeted therapy for DFSP. All of these are best treated as research questions rather than ready-to-use indications.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- Package insert warnings and contraindications from Indian regulatory sources (a blocking gap for safety screening)
- Verification of full-text results from the single-arm Phase 2 non-clear-cell RCC study (PMID 28546525) and the dedicated liposarcoma Phase 2 trial (NCT01506596)
- Confirmation of the histologies enrolled in NCT01692496, NCT01532687 and NCT02066285
- A comparative benefit-risk assessment against current standard therapies in each candidate indication
- A cardiac, hepatic and blood-pressure monitoring plan, plus a drug-interaction review (particularly acid suppressants)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

