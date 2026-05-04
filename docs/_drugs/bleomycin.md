---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Bleomycin: From Hodgkin's Lymphoma to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a glycopeptide antibiotic with antineoplastic properties, widely recognized as a component of the ABVD regimen for Hodgkin's lymphoma and the BEP regimen for testicular germ cell tumors.
The TxGNN model predicts it may be effective for **Cauda Equina Neoplasm**,
with **0 clinical trials** and **3 publications** currently supporting this direction — evidence remains sparse and largely indirect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin's lymphoma, testicular germ cell tumors, squamous cell carcinomas (internationally established; no India-registered indication on record) |
| Predicted New Indication | Cauda Equina Neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Bleomycin is a glycopeptide antibiotic that exerts its antitumor effect by inducing single- and double-strand DNA breaks through free radical generation, preferentially affecting cells in G2 and M phase. It is notably myelosuppression-sparing and is a core component of the ABVD regimen (Adriamycin–Bleomycin–Vinblastine–Dacarbazine) for Hodgkin's lymphoma and the BEP regimen (Bleomycin–Etoposide–Cisplatin) for testicular germ cell tumors.

Cauda equina neoplasms are heterogeneous: they most commonly include ependymomas, schwannomas, and — less frequently — lymphomatous or germ cell metastases. The mechanistic rationale put forward in the repurposing analysis is that Bleomycin's established activity against lymphoma and germ cell tumors could theoretically extend to lymphoma-related cauda equina involvement or germ cell tumors with spinal dissemination. This is a biologically plausible, but narrowly applicable, extrapolation.

The critical limitation is that none of the three supporting publications directly studies Bleomycin for cauda equina neoplasm. The evidence base consists of a case report of Hodgkin's lymphoma with cauda equina enhancement due to paraneoplastic neuropathy, a retrospective series on CNS germinoma salvage where bleomycin was part of a prior regimen, and a retrospective cohort reporting incidental cauda equina involvement in aggressive NHL. None of these constitute direct efficacy evidence, making this prediction primarily model-driven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bleomycin in cauda equina neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Retrospective | Journal of Clinical Oncology | Evaluated radiation therapy to salvage CNS germinoma patients who relapsed after primary chemotherapy including Bleomycin (carboplatin–etoposide–bleomycin / PEB); Bleomycin was part of prior treatment, not the salvage agent |
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Retrospective Cohort | American Journal of Clinical Oncology | CNS involvement in 277 patients with aggressive NHL; cauda equina involvement documented in 1 patient at autopsy; treatment regimens included bleomycin-containing combinations |
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case Report | Rinsho Shinkeigaku (Clinical Neurology) | 17-year-old with Hodgkin's lymphoma presenting with paraneoplastic sensory neuropathy; MRI showed cauda equina enhancement; managed with IVIG, not bleomycin specifically |

---

## India Market Information

No regulatory authorizations for Bleomycin are currently registered in India based on available data. This drug is not marketed in India.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Glycopeptide antibiotic class; DNA strand-break agent) |
| Myelosuppression Risk | Low — Bleomycin is notably myelosuppression-sparing compared to most cytotoxics; myelosuppression is not a primary dose-limiting toxicity |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function tests (DLCO, spirometry) before and during treatment; cumulative dose tracking (risk of pulmonary toxicity increases significantly above 400 units total); renal function (renal clearance-dependent elimination); skin changes (flagellate erythema, hyperpigmentation) |
| Handling Protection | Must follow cytotoxic drug handling regulations; reconstitution and administration require personal protective equipment per institutional chemotherapy safety protocols |

> **Special warning:** Bleomycin pulmonary toxicity (BPT) — manifesting as interstitial pneumonitis progressing to fibrosis — is the most serious and potentially fatal adverse effect. Risk factors include cumulative dose, advancing age, concurrent or prior chest irradiation, high inspired oxygen concentration (perioperative risk), and renal impairment. In the context of cauda equina or any lung-adjacent tumor, pulmonary function monitoring is critical.

---

## Safety Considerations

**Drug Interactions (205 interactions on record; selected below):**

| Interacting Drug | Interaction Level | Note |
|-----------------|------------------|-------|
| Levofloxacin | Minor | Classified interaction; monitor for additive effects |
| Ondansetron / Granisetron / Palonosetron | Unknown | Antiemetics commonly co-administered; interaction classification pending |
| Prednisone / Prednisolone / Hydrocortisone | Unknown | Corticosteroids often used in lymphoma regimens; interaction classification pending |
| Clarithromycin | Unknown | Potential pharmacokinetic interaction; monitor |
| Morphine | Unknown | Opioid co-administration common in oncology; monitor CNS effects |
| Vancomycin | Unknown | Both drugs with renal clearance; renal function monitoring recommended |
| Pantoprazole / Omeprazole / Lansoprazole / Ranitidine / Famotidine | Unknown | GI prophylaxis agents; interaction classification pending |

For complete safety information including black box warnings and contraindications, please refer to the current prescribing information / package insert. Key warnings and contraindications data were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.30%) to cauda equina neoplasm, but the underlying evidence is L4 (preclinical / mechanistic / indirect) — zero dedicated clinical trials exist and all three supporting publications are tangential case-level observations. The mechanistic rationale is biologically plausible only for the rare subset of cauda equina involvement by lymphoma or germ cell tumors, not for the more common histotypes (ependymoma, schwannoma). Additionally, Bleomycin's serious pulmonary toxicity risk adds a patient-safety dimension that requires careful monitoring infrastructure before any clinical exploration.

**To proceed, the following is needed:**

- Confirm histotype: Identify whether the target cauda equina neoplasm is lymphomatous or germ cell origin (the only biologically plausible subtypes for Bleomycin activity)
- Obtain full MOA documentation from DrugBank (DG002) and complete prescribing information including black box warnings and contraindications (DG001)
- Conduct a targeted literature search specifically for ependymoma and spinal schwannoma chemotherapy trials to confirm absence of existing data
- Establish India regulatory pathway: Bleomycin is currently not registered in India; importation or compassionate use pathways would need to be defined
- Design a pulmonary function monitoring protocol prior to any investigational use, given the well-documented bleomycin pulmonary toxicity risk
- Consider requesting a formal expert opinion from a neuro-oncology specialist before advancing to any clinical feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

