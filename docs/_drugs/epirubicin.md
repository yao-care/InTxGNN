---
layout: default
title: Epirubicin
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 7
---

# Epirubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Epirubicin: From Breast Cancer to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is an anthracycline cytotoxic drug — the 4'-epimer of doxorubicin — with an established history in the treatment of breast cancer, gastric cancer, and other malignancies, acting principally through Topoisomerase IIα inhibition and DNA intercalation.
The TxGNN model's top prediction is that it may be effective for **Primary Pulmonary Lymphoma** (score: 99.71%), with **no registered clinical trials** and **9 publications** offering only indirect mechanistic support at this stage; the evidence base is built on related lymphoma subtypes rather than direct studies in this rare entity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Breast cancer and various malignancies (no India regulatory data available) |
| Predicted New Indication (Rank 1) | Primary Pulmonary Lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## All Predicted Indications — TxGNN Summary

This Evidence Pack covers 7 predicted indications for Epirubicin. TxGNN scores are tightly clustered (99.06%–99.71%), which means small score differences should not be over-interpreted. For immediate actionability, **Small Cell Lung Carcinoma** (rank 3) and **Upper Aerodigestive Tract Neoplasm** (rank 7) carry the strongest clinical evidence.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Primary Pulmonary Lymphoma | 99.71% | L4 | Research Question |
| 2 | Well-Differentiated Fetal Adenocarcinoma of the Lung | 99.69% | L5 | Hold |
| **3** | **Small Cell Lung Carcinoma** | **99.69%** | **L1** | **Proceed with Guardrails** |
| 4 | Pulmonary Blastoma | 99.65% | L4 | Research Question |
| 5 | Lung Mixed Small Cell and Squamous Cell Carcinoma | 99.17% | L5 | Hold |
| 6 | Myeloid Leukemia | 99.07% | L3 | Research Question |
| **7** | **Upper Aerodigestive Tract Neoplasm** | **99.06%** | **L1** | **Proceed with Guardrails** |

> The following detailed sections focus on the top-ranked TxGNN prediction: **Primary Pulmonary Lymphoma**.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the manufacturer's label is not currently available. Based on established pharmacological literature, Epirubicin exerts its antitumour effects by intercalating into DNA strands and inhibiting Topoisomerase IIα — an enzyme essential for DNA unwinding during replication. This generates irreversible DNA double-strand breaks that trigger apoptosis in rapidly dividing cells, with peak activity during the S phase of the cell cycle. As the 4'-epimer of doxorubicin, epirubicin shares the same core mechanism while offering a modestly more favourable cardiac safety profile at equivalent myelosuppressive doses.

Primary pulmonary lymphoma (PPL) is a rare extranodal lymphoid malignancy originating in the lung parenchyma, most commonly presenting as MALT-type (indolent, low-grade) or DLBCL-type (aggressive). Both subtypes involve lymphoid cell populations characterised by high proliferative activity — precisely the biological context in which anthracyclines are most effective. The gold-standard CHOP backbone for DLBCL contains doxorubicin as its anthracycline; epirubicin is pharmacologically interchangeable within this framework. Historical regimens containing epirubicin — MOPPEBVCAD (containing epidoxorubicin, i.e., epirubicin) and VEBEP — have demonstrated durable efficacy in Hodgkin's lymphoma, providing indirect cross-indication support.

However, no clinical trial has ever directly studied epirubicin specifically in PPL, and the available publications are entirely indirect evidence. The TxGNN score of 99.71% reflects the structural proximity between epirubicin's drug-disease knowledge graph nodes and the PPL disease node — this is a mechanistic extrapolation signal, not clinical proof of concept. PPL's extreme rarity (estimated 0.5–1% of all lung malignancies) further limits the feasibility of a dedicated RCT in the near term.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Epirubicin in primary pulmonary lymphoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Pharmacological Review | *Drugs* | Landmark comprehensive review of epirubicin pharmacodynamics and clinical use; confirms Topoisomerase IIα inhibition as mechanism and documents use across multiple malignancy types including lymphoid tumours |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | RCT Sub-analysis | *Annals of Hematology* | Pola-R-CHP (polatuzumab + R-CHP) as first-line DLBCL therapy in Polarix-ineligible patients and IPI 0–1; benchmark for anthracycline-based treatment in DLBCL subtypes applicable to DLBCL-type PPL |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective Cohort | *Zhongguo shi yan xue ye xue za zhi* | Clinical features and prognostic factors of primary extranodal DLBCL in the rituximab era; provides treatment outcome context for extranodal lymphomas in accessible lung sites |
| [16428496](https://pubmed.ncbi.nlm.nih.gov/16428496/) | 2006 | Retrospective Observational | *Clinical Cancer Research* | 10-year results of MOPPEBVCAD (containing epidoxorubicin = epirubicin) + limited radiotherapy in advanced Hodgkin's lymphoma; documents durable remissions and late toxicity profile of epirubicin-containing lymphoma regimens |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Prospective Observational | *The Cancer Journal* | VEBEP regimen (including epirubicin) + involved-field radiotherapy in advanced Hodgkin's disease not previously treated; demonstrates feasibility and activity of epirubicin in combination lymphoma therapy |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case Report + Literature Review | *Translational Cancer Research* | First Chinese case of pleural MALT lymphoma; highlights diagnostic challenges in rare pulmonary lymphoid tumours and typical indolent clinical course |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case Series | *Revista de Investigación Clínica* | Primary non-Hodgkin's lymphoma of the lung with haemorrhagic pleural effusion; historical case documenting clinical presentation and chemotherapy response in primary pulmonary NHL |
| [8386780](https://pubmed.ncbi.nlm.nih.gov/8386780/) | 1993 | Case Report | *Rinsho Ketsueki (Jpn J Clin Haematology)* | Secondary lymphoblastic lymphoma developing after SCLC resection and chemotherapy; documents chemotherapy-resistant pulmonary lymphoma and underlines treatment complexity |
| [7525516](https://pubmed.ncbi.nlm.nih.gov/7525516/) | 1994 | Retrospective | *Int J Radiation Oncology Biol Phys* | Extended-field radiotherapy alone in Stage IA–IIA Hodgkin's disease; radiotherapy-only design limits relevance to epirubicin in PPL, included for context |

---

## India Market Information

Epirubicin is **not registered in India**. There are no approved products, valid marketing authorisations, or recorded dosage form registrations on file. Any clinical use would require a special import licence or compassionate use authorisation through the regulatory authority prior to procurement.

---

## Cytotoxicity

Epirubicin meets all criteria for classification as a conventional antineoplastic cytotoxic agent: it belongs to the anthracycline class, its mechanism targets actively replicating tumour cells, and its indications are exclusively oncological.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline / Topoisomerase II poison |
| Myelosuppression Risk | **High** — dose-limiting granulocytopenia and leucopenia are common; thrombocytopenia and anaemia also occur; nadir typically at days 10–14 post-infusion |
| Emetogenicity Classification | Moderate to High (dose-dependent; prophylactic 5-HT₃ antagonist + dexamethasone recommended) |
| Monitoring Items | CBC with differential (before each cycle and at nadir), LVEF by echocardiogram or MUGA scan (baseline, then at cumulative dose thresholds ~450–550 mg/m²), liver function tests, renal function, serum electrolytes |
| Handling Protection | Must comply with cytotoxic drug handling regulations — closed-system drug transfer devices, chemotherapy-rated gloves and gown, face/eye protection, dedicated laminar-flow preparation area required |

---

## Safety Considerations

**Drug Interactions**: 487 interactions are documented (DDInter database). Key clinically significant interactions:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Cimetidine | **Major** | H₂-blocker significantly reduces hepatic clearance of epirubicin, raising plasma drug exposure — avoid; substitute with proton pump inhibitor |
| Dolasetron | **Major** | Combined QT prolongation risk — cardiac ECG monitoring required; consider alternative antiemetics (e.g., ondansetron with ECG monitoring) |
| Clarithromycin | Moderate | CYP3A4 inhibition may increase epirubicin systemic exposure and toxicity risk |
| Levofloxacin | Moderate | Additive QT prolongation — ECG monitoring recommended during concurrent use |
| Palonosetron | Moderate | Additive QT prolongation potential; monitor cardiac conduction |
| Bupropion | Moderate | Potential pharmacokinetic interaction and lowered seizure threshold |
| Loperamide | Moderate | Cardiac conduction concern in combination; monitor for arrhythmia |

Please refer to the full package insert for comprehensive safety data, including cumulative cardiotoxicity lifetime dose limits, contraindications in patients with hepatic impairment or prior anthracycline exposure, and pregnancy/lactation restrictions.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
No clinical trials of epirubicin specifically in primary pulmonary lymphoma have ever been conducted, and all 9 available publications represent indirect, mechanistically related evidence from adjacent lymphoma subtypes (Hodgkin's disease, extranodal DLBCL) rather than direct proof of concept. The TxGNN score of 99.71% reflects knowledge-graph structural proximity, not clinical validation, and this indication requires a translational research foundation before it can be considered actionable.

**To proceed, the following is needed:**

- **Regulatory data gap (DG001)**: Retrieve the full epirubicin package insert to document key warnings, contraindications, and cumulative cardiotoxicity thresholds — this is a blocking requirement for safety evaluation
- **MOA data gap (DG002)**: Query the DrugBank API to formally characterise epirubicin's mechanism of action for the mechanistic link analysis
- **Literature gap**: Conduct a targeted systematic review on anthracycline use (doxorubicin and epirubicin) in primary pulmonary MALT lymphoma and DLBCL-type PPL specifically
- **Extrapolation assessment**: Evaluate whether existing R-CHOP efficacy data in extranodal DLBCL supports the design of an epirubicin-substituted regimen
- **Minimum viable evidence**: A retrospective case registry or multicentre compassionate-use protocol would represent the lowest feasible evidence-generation pathway given PPL's rarity
- **India regulatory pathway**: Establish a special import licence or compassionate use authorisation route given current non-registration status before any clinical procurement

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

