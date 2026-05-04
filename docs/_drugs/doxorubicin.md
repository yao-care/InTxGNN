---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Established Chemotherapy Agent to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is a well-established anthracycline chemotherapy agent used broadly across multiple cancer types.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, the second most common primary bone cancer in children and adolescents,
with **10+ clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration data available |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| India Market Status | Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is listed as a data gap in this evidence pack. However, based on well-established pharmacological knowledge, Doxorubicin is an anthracycline antibiotic that exerts its antitumour effects primarily through two mechanisms: (1) intercalation into DNA double strands, causing structural disruption that blocks DNA replication and transcription; and (2) inhibition of Topoisomerase II, an enzyme essential for resolving DNA supercoiling during cell division. These mechanisms result in DNA double-strand breaks and subsequent apoptosis, with greatest impact on rapidly proliferating cells.

Ewing sarcoma is a highly malignant tumour of bone and soft tissue, arising primarily in children and young adults. It is characterised by highly proliferative, undifferentiated cells — precisely the cell population most vulnerable to Doxorubicin's DNA-damaging mechanism. The standard-of-care chemotherapy regimen for Ewing sarcoma — VDC/IE (Vincristine + Doxorubicin + Cyclophosphamide alternating with Ifosfamide + Etoposide) — already incorporates Doxorubicin as a backbone agent. This means the TxGNN prediction is not so much a novel discovery as a mechanistically grounded confirmation: the model correctly identifies an existing, guideline-endorsed application.

The strong TxGNN score (99.90%) reflects the extensive biological and clinical connections between Doxorubicin and Ewing sarcoma in the underlying knowledge graph. Multiple completed Phase 3 RCTs directly use Doxorubicin as the control arm reference standard, which further validates its central role in this indication. International cooperative groups across North America and Europe have all converged on Doxorubicin-containing regimens as the foundation of Ewing sarcoma treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Landmark COG trial evaluating whether adding vincristine-topotecan-cyclophosphamide (VTC) to standard VDC/IE improves outcomes in non-metastatic Ewing sarcoma; Doxorubicin is the backbone of the control arm |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, Not Recruiting | 312 | Randomised trial of IGF-1R monoclonal antibody ganitumab added to interval-compressed VDC/IE chemotherapy for newly diagnosed metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomised trial comparing dose intensification vs standard treatment for non-metastatic Ewing sarcoma; Doxorubicin included in both arms |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | AEWS0031: Established the interval-compressed VDC/IE schedule (including Doxorubicin) as the North American standard of care |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1,200 | EURO-E.W.I.N.G.99: Major European cooperative trial evaluating Doxorubicin-containing regimens and consolidation strategies |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, Not Recruiting | 437 | Tests vincristine-irinotecan-regorafenib (VIrR) combined with standard VDC/IE for newly diagnosed metastatic Ewing sarcoma |
| [NCT01696669](https://clinicaltrials.gov/study/NCT01696669) | Phase 2 | Completed | 43 | Prospective multicentre study of intensive chemotherapy including Doxorubicin, surgery, and radiotherapy in children and young adults with Ewing sarcoma |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Intensive Doxorubicin-based chemotherapy with growth factor support for patients with newly diagnosed metastatic Ewing sarcoma |
| [NCT00061893](https://clinicaltrials.gov/study/NCT00061893) | Phase 2 | Completed | 38 | Low-dose antiangiogenic chemotherapy (vinblastine + celecoxib) added to standard Doxorubicin-containing regimen for metastatic Ewing sarcoma |
| [NCT01095926](https://clinicaltrials.gov/study/NCT01095926) | Phase 2 | Completed | 101 | Pharmacokinetic study characterising age-dependent Doxorubicin clearance in paediatric cancer patients; assessed troponin and natriuretic peptides as cardiotoxicity biomarkers |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Landmark trial showing addition of ifosfamide and etoposide to standard doxorubicin-containing chemotherapy significantly improves survival in Ewing sarcoma and PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | Phase 3 RCT | Lancet | EE2012 trial: first head-to-head comparison of European (VIDE/VAI) vs North American (VDC/IE with Doxorubicin) regimens for newly diagnosed Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Phase 3 RCT | Trials | Euro Ewing 2012 protocol paper; describes the international randomised trial design comparing two Doxorubicin-containing induction strategies |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | Phase 3 RCT | J Clin Oncol | COG AEWS1221: Addition of ganitumab to interval-compressed VDC/IE (containing Doxorubicin) did not improve event-free survival in metastatic Ewing sarcoma |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | Phase 3 RCT | J Clin Oncol | Ewing 2008R3: Treosulfan/melphalan high-dose consolidation after Doxorubicin-based induction evaluated in high-risk metastatic Ewing sarcoma across 12 countries |
| [31553693](https://pubmed.ncbi.nlm.nih.gov/31553693/) | 2019 | RCT | J Clin Oncol | R2Pulm trial: BuMel high-dose chemotherapy vs standard Doxorubicin-containing chemotherapy + whole-lung irradiation in Ewing sarcoma with pulmonary metastases |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Comprehensive review of Ewing sarcoma management; covers the evolution of Doxorubicin-based combination chemotherapy and its impact on survival |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Clinical Guideline | Cancer | National Ewing Sarcoma Tumor Board consensus recommendations covering standard Doxorubicin-based VDC/IE chemotherapy and areas of ongoing debate |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | International collaborative review of Ewing sarcoma treatment strategy; outlines risk-adapted use of Doxorubicin-containing neoadjuvant and adjuvant regimens |
| [37093679](https://pubmed.ncbi.nlm.nih.gov/37093679/) | 2023 | Retrospective Cohort | Jpn J Clin Oncol | Analysis of clinical characteristics of primary cutaneous/subcutaneous Ewing sarcoma; treatment included Doxorubicin-containing multiagent chemotherapy |

---

## India Market Information

Doxorubicin (DB00997) does not appear in the current India regulatory database for this evidence pack. No approved product registrations were identified.

> **Note:** The absence of registrations in this dataset does not necessarily reflect the true availability of Doxorubicin in India, as it is a long-established generic injectable chemotherapy agent. Regulatory data completeness should be verified with the Central Drugs Standard Control Organisation (CDSCO).

---

## Cytotoxicity

Doxorubicin is a conventional cytotoxic anthracycline chemotherapy agent. The following cytotoxicity profile applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalator + Topoisomerase II inhibitor) |
| Myelosuppression Risk | High — Neutropenia and thrombocytopenia are expected dose-limiting toxicities; nadir typically occurs 10–14 days post-infusion |
| Emetogenicity Classification | Moderate to High — Doxorubicin at standard oncology doses carries significant emetogenic potential |
| Monitoring Items | CBC with differential (before each cycle); cardiac function — LVEF by echocardiogram or MUGA (baseline, then periodically); liver function tests; cumulative dose tracking (cardiotoxicity risk increases beyond 450–550 mg/m²) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in a biological safety cabinet, personnel use appropriate PPE including gloves, gowns, and eye protection |

---

## Safety Considerations

**Drug Interactions (665 total interactions identified):**

- **Major interactions** (avoid or use with extreme caution):
  - **Dolasetron** — risk of QT prolongation and cardiac arrhythmia
  - **Cisapride** — risk of serious QT prolongation (note: cisapride is withdrawn in many markets)
  - **Papaverine** — potential for cardiovascular complications

- **Moderate interactions** (monitor closely):
  - **Ondansetron, Granisetron, Palonosetron** — 5-HT3 antagonists commonly used for Doxorubicin-induced nausea; QT monitoring warranted
  - **Aprepitant, Rolapitant** — NK1 antagonists used as antiemetics; potential CYP3A4 interactions
  - **Dexamethasone** — frequently co-administered; interactions with immunosuppression and metabolism
  - **Clarithromycin** — CYP3A4 inhibitor; may increase Doxorubicin exposure
  - **Levofloxacin, Eliglustat** — QT prolongation risk with concurrent use
  - **Famotidine, Loperamide** — supportive care agents with moderate interaction signals

- **Minor interactions:**
  - **Ascorbic acid** — may reduce Doxorubicin efficacy at high doses in some contexts
  - **Metronidazole** — minor pharmacokinetic interaction

> Package insert warnings and contraindications data were not available in this evidence pack. Full prescribing information should be reviewed before clinical use, particularly regarding cumulative cardiotoxicity limits and hepatic impairment dose adjustments.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxorubicin is already embedded as the backbone agent in the internationally accepted VDC/IE standard-of-care regimen for Ewing sarcoma, supported by multiple completed Phase 3 RCTs across North American and European cooperative groups. The TxGNN prediction score of 99.90% is mechanistically consistent with decades of clinical evidence. This is a case where the model validates established clinical practice rather than proposing a genuinely novel repurposing.

**To proceed, the following is needed:**

- **Regulatory verification in India:** Confirm actual registration status and availability of Doxorubicin (branded and generic) with CDSCO; the dataset shows zero registrations which may reflect a data gap rather than true unavailability
- **MOA documentation:** Retrieve full DrugBank mechanism-of-action data (marked as Data Gap DG002) to complete the evidence pack
- **Package insert review:** Obtain CDSCO-approved or internationally recognised package insert for formal warnings, contraindications, and dose modification guidelines (Data Gap DG001)
- **Cardiotoxicity management plan:** Given the high myelosuppression and cardiotoxicity risk of Doxorubicin in paediatric populations (the primary Ewing sarcoma demographic), a monitoring protocol covering cumulative dose limits, cardiac surveillance schedule (LVEF), and dexrazoxane cardioprotection criteria should be defined
- **Paediatric pharmacokinetic consideration:** NCT01095926 highlights age-dependent differences in Doxorubicin clearance in paediatric patients; dose individualisation strategies should be documented
- **Local availability and supply chain:** Confirm that appropriate IV formulation (conventional or liposomal) and supportive care infrastructure (G-CSF, antiemetics, cardiac monitoring) are available in the intended clinical setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

