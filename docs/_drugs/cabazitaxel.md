---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel (Jevtana) is a next-generation taxane approved by the FDA in 2010 for metastatic castration-resistant prostate cancer (mCRPC) in patients previously treated with docetaxel, notable for its ability to bypass P-glycoprotein (MDR1)-mediated drug resistance.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, particularly in taxane-resistant subtypes such as triple-negative breast cancer (TNBC),
with **0 registered clinical trials** (in this query) and **20 publications** — including 1 Phase 2 RCT and 1 Phase 1/II study — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), post-docetaxel |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel is a semisynthetic taxane derivative that stabilises microtubules by binding to β-tubulin, thereby preventing microtubule depolymerisation, arresting the cell cycle at the G2/M phase, and triggering apoptosis. Its key pharmacological advantage over earlier taxanes (paclitaxel, docetaxel) lies in its markedly lower affinity for P-glycoprotein (MDR1), the ATP-dependent efflux pump responsible for taxane resistance in many tumour types. This property was the mechanistic rationale for its approval in docetaxel-refractory prostate cancer, and the same logic extends directly to breast cancer.

Breast cancer — particularly TNBC and luminal B/HER2-negative subtypes — frequently overexpresses βIII-tubulin and MDR1, both of which reduce sensitivity to standard taxanes. PMID 28567478 directly demonstrated that high βIII-tubulin expression creates an environment where cabazitaxel outperforms docetaxel in microtubule-binding efficacy. Beyond cytotoxicity, PMID 33753567 revealed an additional immunological dimension: cabazitaxel reprogrammes tumour-associated macrophages (TAMs) in the TNBC microenvironment, enhancing CD47-targeted phagocytosis — a mechanism entirely absent from earlier taxanes.

The clinical rationale is further reinforced by the GENEVIEVE Phase 2 RCT (PMID 28768217), which directly compared cabazitaxel versus weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer, and by the Phase I/II study (PMID 21339064) establishing the maximum tolerated dose and activity of cabazitaxel plus capecitabine in taxane- and anthracycline-pretreated metastatic breast cancer patients. Both studies confirm that the mechanistic hypothesis translates into measurable clinical signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack's query scope (ClinicalTrials.gov query returned 0 results for "Cabazitaxel" + "female breast carcinoma"). However, the literature below documents Phase 1/2 interventional studies with registered identifiers; a broader direct search on ClinicalTrials.gov using "cabazitaxel breast cancer" is recommended.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase 2 RCT | European Journal of Cancer | GENEVIEVE trial: cabazitaxel vs weekly paclitaxel as neoadjuvant therapy in operable HER2-negative (TNBC and luminal B) breast cancer; directly compared pCR rates between the two taxanes |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/2 Dose-Escalation | European Journal of Cancer | Multicentre study of cabazitaxel + capecitabine in metastatic breast cancer (MBC) patients previously treated with anthracyclines and taxanes; established MTD and showed clinical activity in refractory MBC |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase 2 Study | Clinical Breast Cancer | Cabazitaxel + lapatinib in HER2+ MBC with intracranial metastases (NCT01934894); leveraged cabazitaxel's blood-brain barrier penetration combined with lapatinib's CNS activity |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical / Mechanistic | Journal for Immunotherapy of Cancer | Cabazitaxel reprogrammes tumour-associated macrophages (TAMs) in TNBC, enhancing CD47 antibody-mediated programmed cell removal (PrCR); reveals an immunomodulatory mechanism distinct from microtubule inhibition |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Preclinical / Comparative | Cancer Chemotherapy and Pharmacology | Confirms that high βIII-tubulin expression (a hallmark of taxane-resistant, aggressive breast cancers) specifically enhances cabazitaxel's binding and efficacy relative to docetaxel |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | Characterised cabazitaxel resistance mechanisms using MCF-7 breast cancer cell models; found cabazitaxel significantly less cross-resistant than paclitaxel/docetaxel in MDR variants (15-fold vs 200-fold) |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | Comprehensive review of taxane pharmacokinetics and TDM-based personalisation; covers cabazitaxel's PK profile, metabolism, and clinical use optimisation |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical / Formulation | Chemistry and Physics of Lipids | Cabazitaxel + thymoquinone co-loaded lipospheres targeting p53, STAT3, Bax/BCL-2, and NF-κB pathways in breast tumour models; demonstrates synergistic multi-target activity |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | PACA nanoparticle-encapsulated cabazitaxel in patient-derived xenograft (PDX) models of TNBC; nanoformulation significantly improved efficacy and reduced M2 macrophage infiltration vs free drug |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | Poly(2-ethylbutyl cyanoacrylate) NP-encapsulated cabazitaxel in basal-like breast cancer PDX; nanoparticle formulation achieved complete remission in 6/8 tumours vs 1/8 with free drug |

---

## India Market Information

Cabazitaxel is currently **not marketed in India**. No drug registrations or authorisations were found in the regulatory database query. Regulatory approval would need to be pursued independently should this repurposing programme advance to clinical translation.

For reference, cabazitaxel is approved in other major markets:

| Market | Product Name | Approved Indication |
|--------|-------------|-------------------|
| USA (FDA, 2010) | Jevtana® | mCRPC post-docetaxel (with prednisone) |
| EU (EMA) | Jevtana® | mCRPC post-docetaxel (with prednisone) |

---

## Cytotoxicity

Cabazitaxel is a cytotoxic antineoplastic agent (semisynthetic taxane class). This section is mandatory.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilising agent) |
| Myelosuppression Risk | **High** — Febrile neutropenia is the most common and potentially life-threatening toxicity; Grade 3/4 neutropenia reported in >80% of patients in pivotal trials; granulocyte colony-stimulating factor (G-CSF) prophylaxis is recommended |
| Emetogenicity Classification | Low to moderate (similar to other taxanes; antiemetic pre-medication standard) |
| Monitoring Items | Complete blood count with differential (before each cycle and as clinically needed), liver function tests (ALT, AST, bilirubin), renal function (creatinine), neuropathy assessment, hypersensitivity monitoring during infusion |
| Handling Protection | Must be handled following cytotoxic drug handling regulations; preparation in a dedicated pharmacy laminar flow hood; personal protective equipment (gloves, gown, eye protection) required; disposal as cytotoxic waste |

---

## Safety Considerations

Detailed package insert warnings and contraindications are not available in this evidence pack (Data Gap: TFDA/CDSCO package insert not yet retrieved). Based on the known drug class profile from literature:

- **Key known risks from literature**: Severe neutropenia (febrile neutropenia can be fatal — G-CSF support required), peripheral neuropathy, hypersensitivity reactions during infusion, diarrhoea, fatigue, alopecia
- **Special population caution**: Patients with severe hepatic impairment (bilirubin >3× ULN) should not receive cabazitaxel; dose reduction required for moderate hepatic impairment
- **Drug interactions**: DDI database query failed due to missing local data file; formal DDI assessment against concomitant medications (especially CYP3A4 inhibitors/inducers such as ketoconazole, rifampicin) is required before clinical use

> Please retrieve the full package insert from the CDSCO/FDA official website to complete the safety assessment before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for cabazitaxel in female breast carcinoma is mechanistically well-grounded — the drug's MDR1-bypass property directly addresses a central resistance mechanism in taxane-pretreated TNBC and luminal B breast cancers. The GENEVIEVE Phase 2 RCT (PMID 28768217) and the Phase I/II dose-escalation study (PMID 21339064) provide L2 clinical evidence of activity, supporting advancement beyond pure hypothesis. However, the absence of a completed Phase 3 trial in breast cancer, no registered clinical trials returned in this search, and missing formal safety documentation for the Indian regulatory context require guardrails before proceeding.

**To proceed, the following is needed:**

- **Regulatory safety documentation**: Retrieve and parse the full CDSCO/FDA package insert PDF to complete the S1 safety assessment (currently a Blocking data gap)
- **Broader clinical trial search**: Conduct a direct ClinicalTrials.gov search using "cabazitaxel AND breast cancer" — the zero-result return in this pack reflects a narrow query; registered trials (e.g., GENEVIEVE NCT number, NCT01934894) exist and should be formally catalogued
- **DDI assessment**: Restore the DDInter database file and run the drug-drug interaction analysis, particularly for CYP3A4-affecting co-medications common in breast cancer patients
- **Subtype-specific strategy**: Define the target breast cancer population (TNBC vs HER2+ vs luminal B) and confirm whether the repurposing claim is histology-agnostic or subtype-specific — the mechanistic rationale is strongest for MDR1-overexpressing, taxane-refractory TNBC
- **Formulation and dosing plan**: Cabazitaxel requires IV infusion with polysorbate 80 solubiliser; an Indian supply chain and pharmacy infrastructure assessment is needed given zero current market presence
- **Phase 3 evidence gap**: Commission a systematic review of all available cabazitaxel breast cancer data to determine whether a Phase 3 trial has been completed or is underway globally before committing to a new trial

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions are generated by the TxGNN computational model and must be interpreted alongside clinical expertise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

