---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 1
---

# Dacarbazine
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

# Dacarbazine: From Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is a classic triazene alkylating agent, widely used as first-line or combination chemotherapy for melanoma and Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm (UADT)**,
with **1 clinical trial** (for its structural analogue Temozolomide) and **20 publications** providing only indirect supporting evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Melanoma, Hodgkin lymphoma (alkylating agent standard of care) |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Dacarbazine is a prodrug belonging to the triazene class of alkylating agents. It requires hepatic CYP450 metabolism to generate its active metabolite MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide), which methylates DNA at the O6 and N7 positions of guanine, ultimately inducing DNA double-strand breaks and apoptosis. Importantly, Temozolomide—a second-generation oral triazene—shares this same active metabolite MTIC, making the two drugs mechanistically equivalent at the molecular target level.

Upper aerodigestive tract neoplasms (including head and neck squamous cell carcinoma, thyroid carcinoma, esthesioneuroblastoma, and pharyngeal/laryngeal tumours) are anatomically diverse but share features of rapid cell proliferation that may render them susceptible to DNA alkylation. There is historical precedent: Dacarbazine-containing regimens (e.g., CYVADIC) were used for head and neck angiosarcoma, and Dacarbazine combined with 5-fluorouracil has been reported in advanced medullary thyroid carcinoma (a neuroendocrine UADT tumour). Furthermore, a published Phase II trial (PMID 23443801, NCT00423150) demonstrated that MGMT promoter methylation status predicts response to Temozolomide in aerodigestive tract cancers, indirectly implicating the MTIC pathway in this tumour group.

However, the mechanistic extrapolation from Temozolomide evidence to Dacarbazine must be treated cautiously. UADT squamous cell carcinoma (the predominant subtype) has standard-of-care regimens built around platinum-based chemotherapy plus radiotherapy, and there is no direct evidence that Dacarbazine's triazene mechanism offers a clinically meaningful advantage in this setting. The TxGNN prediction may reflect the shared MTIC pathway and the neuroendocrine/rare UADT subtype experience rather than broad UADT applicability.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | ⚠️ Used **Temozolomide** (not Dacarbazine). Evaluated MGMT promoter methylation as a predictive biomarker in advanced aerodigestive tract, colorectal, NSCLC, and esophageal cancers. Trial was terminated early; published results (PMID 23443801) showed limited efficacy even in MGMT-methylated patients. Indirect evidence only — Temozolomide and Dacarbazine share active metabolite MTIC but are distinct drugs. |

> **Note:** No clinical trials evaluating Dacarbazine directly in upper aerodigestive tract neoplasm were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase III RCT | JAMA Oncology | Toripalimab vs **Dacarbazine** as first-line therapy for advanced acral melanoma. Dacarbazine used as active comparator, confirming its established role in melanoma but not UADT. |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase II Trial | Molecular Cancer Therapeutics | Temozolomide in MGMT-methylated advanced aerodigestive tract and colorectal cancers (NCT00423150). Showed limited efficacy; MGMT methylation alone insufficient for response prediction. Indirect evidence for MTIC-pathway in UADT. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Prospective Study | Annals of Oncology | **Dacarbazine + 5-FU** in advanced medullary thyroid carcinoma (a neuroendocrine UADT tumour). Most directly relevant publication — demonstrates Dacarbazine's actual use in a UADT-adjacent neuroendocrine neoplasm. |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Case Series | Gan to Kagaku Ryoho | CYVADIC regimen (includes DTIC/Dacarbazine) for head and neck angiosarcoma. Reports historical use of Dacarbazine-containing combination in a rare UADT malignancy. |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clinical Oncology | Comprehensive review of medullary thyroid carcinoma management, including systemic chemotherapy options. Contextualises the limited evidence base for cytotoxic therapy in this UADT neuroendocrine tumour. |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective Study | Int J Radiation Oncology | Radiotherapy outcomes in esthesioneuroblastoma. Background reference for rare UADT malignancy where alkylating agents have been used in combination protocols. |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Retrospective Study | Cancer | Characteristics and outcomes of Hodgkin lymphoma presenting in head and neck sites. Dacarbazine is part of ABVD (standard HL regimen), establishing indirect UADT region activity. |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Systematic Review | Journal of Cancer Research & Clinical Oncology | Global burden of EBV-related cancers (including UADT types such as nasopharyngeal carcinoma). Epidemiological background; no direct relevance to Dacarbazine. |

---

## India Market Information

Dacarbazine currently has **no registered products** in India. There are no approved licenses on record.

> Dacarbazine is not commercially available through the Indian regulatory pathway. Any clinical use would require importation or special compassionate use authorization.

---

## Cytotoxicity

Dacarbazine is a conventional cytotoxic alkylating agent (triazene class) with established antineoplastic activity.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Triazene alkylating agent (prodrug, same active metabolite MTIC as Temozolomide) |
| Myelosuppression Risk | Moderate to High — leukopenia and thrombocytopenia are dose-limiting toxicities; nadirs typically at 3–4 weeks |
| Emetogenicity Classification | High — Dacarbazine is classified as a highly emetogenic agent; prophylactic antiemetics mandatory |
| Monitoring Items | CBC with differential (before each cycle and at nadir), liver function tests (hepatotoxicity including hepatic vein thrombosis reported), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations — requires PPE, closed-system drug transfer devices (CSTD), and dedicated preparation in a laminar-flow safety cabinet |

---

## Safety Considerations

Detailed package insert warnings and contraindications data were not available in this Evidence Pack.

**Key Drug Interactions** (from DDInter database; 233 total interactions identified):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Naltrexone | Moderate | Monitor — potential immune/pharmacodynamic interaction with cytotoxic therapy |
| Levofloxacin | Minor | Low clinical concern under standard monitoring |
| Pantoprazole, Omeprazole, Lansoprazole | Unknown | PPIs commonly co-administered; interaction significance unclear |
| Ondansetron, Palonosetron, Dolasetron, Aprepitant | Unknown | Antiemetics routinely used with Dacarbazine; interaction significance requires clarification |
| Prednisone / Prednisolone | Unknown | Corticosteroids often combined in ABVD; monitor |
| Morphine | Unknown | Pain management interaction; monitor CNS effects |

> For comprehensive warnings, contraindications, and full drug interaction data, please refer to the official package insert and a validated drug interaction database prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single identified clinical trial used Temozolomide (not Dacarbazine) and was terminated without demonstrating sufficient efficacy in UADT cancers; the literature evidence is predominantly indirect, historical, or focused on rare UADT subtypes (medullary thyroid carcinoma, angiosarcoma) rather than the dominant squamous cell carcinoma histology. With an evidence level of L4, no approved product in India, and critical data gaps in MOA documentation and safety warnings, this candidate does not yet meet the threshold for active development consideration.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full Dacarbazine mechanism of action from DrugBank API (DG002 — High severity gap)
- **Safety package**: Download and parse the TFDA/approved regulatory package insert to complete warnings and contraindications (DG001 — Blocking severity gap)
- **Histology clarification**: Determine whether the repurposing hypothesis targets the rare neuroendocrine/angiosarcoma UADT subtypes (where limited historical evidence exists) or broadly all UADT squamous cell carcinomas (where evidence is absent)
- **Direct Dacarbazine trials**: Search specifically for Dacarbazine (DTIC) trials in head and neck cancer, thyroid cancer, and UADT neuroendocrine tumours — the current search retrieved only a Temozolomide trial
- **Comparator analysis**: Given Temozolomide is the oral, better-tolerated analogue with the same MTIC mechanism, a clinical and regulatory rationale for using Dacarbazine (IV) over Temozolomide (oral) in UADT must be established before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

