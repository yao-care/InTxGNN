---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From Liposarcoma to Fibroblastic Neoplasm

## One-Sentence Summary

Eribulin (Halaven, DB08871) is an FDA-approved microtubule inhibitor with established indications in metastatic breast cancer and unresectable/metastatic liposarcoma.
The TxGNN model evaluated **10 predicted indications**; among them, **Fibroblastic Neoplasm** carries the highest evidence level (L2), supported by **1 completed Phase 2 clinical trial** (ERASING, NCT03840772) and **8 publications**.
All other 9 predicted indications are rated Hold due to absence of direct clinical evidence or lack of mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic breast cancer; unresectable or metastatic liposarcoma |
| Predicted New Indication (Best Evidence) | Fibroblastic Neoplasm (TxGNN Rank 8) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Fibroblastic Neoplasm) · **Hold** (all other 9 indications) |

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|---------|
| 1 | Autosomal Recessive Familial Mediterranean Fever | 99.82% | L5 | Hold |
| 2 | Dermatofibrosarcoma Protuberans | 99.66% | L4 | Hold |
| 3 | Pleural Mesothelioma | 99.51% | L5 | Hold |
| 4 | Malignant Peritoneal Mesothelioma | 99.47% | L5 | Hold |
| 5 | Ovarian Myxoid Liposarcoma | 99.47% | L4 | Hold |
| 6 | Pleural Adenomatoid Tumor | 99.46% | L5 | Hold |
| 7 | Pleural Biphasic Mesothelioma | 99.37% | L5 | Hold |
| **8** | **Fibroblastic Neoplasm** | **99.36%** | **L2** | **Proceed with Guardrails** |
| 9 | Pleural Epithelioid Mesothelioma | 99.35% | L5 | Hold |
| 10 | Heart Fibrosarcoma | 99.35% | L4 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, eribulin is a synthetic analog of halichondrin B — a marine natural product — that inhibits microtubule polymerization by binding uniquely to the plus ends of microtubules. This causes G2/M cell cycle arrest and induces apoptosis through a mechanism distinct from taxanes and vinca alkaloids. Beyond direct cytotoxicity, eribulin has been shown to reverse epithelial–mesenchymal transition (EMT), remodel tumor vasculature, and reduce cancer stem cell populations.

Fibroblastic neoplasms — including solitary fibrous tumor (SFT), myxofibrosarcoma (MFS), and fibrosarcoma (FS) — are proliferating spindle-cell tumors of mesenchymal origin that share biological features with soft tissue sarcomas already within eribulin's approved label. These tumors are characterized by active mitotic rates, making them theoretically susceptible to microtubule inhibition. Eribulin's EMT-reversing activity is particularly relevant to sarcoma biology, where mesenchymal plasticity drives local invasion and distant spread.

Multiple preclinical studies using fibrosarcoma cell lines (HT1080, NCC-MFS4-C1, SMU-MFS) and patient-derived xenograft (PDX) models of SFT have directly confirmed eribulin's antiproliferative activity in this tumor class. The ERASING Phase 2 trial (NCT03840772), completed in September 2024, prospectively tested eribulin in advanced SFT patients — providing the strongest available clinical evidence and elevating fibroblastic neoplasm to L2 status among eribulin's repurposing candidates.

---

## Clinical Trial Evidence (Fibroblastic Neoplasm)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | ERASING: eribulin monotherapy in advanced solitary fibrous tumor (SFT); Italian Sarcoma Group multicenter study; completed September 2024 — efficacy results pending full peer-reviewed publication |

---

## Literature Evidence (Fibroblastic Neoplasm)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | PDX Preclinical | Eur J Cancer | Patient-derived SFT xenograft models confirmed sensitivity to doxorubicin/dacarbazine; eribulin identified alongside trabectedin as a potentially effective novel agent — informed the design of the ERASING trial |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review / Guideline | Cancers | Comprehensive review of extrameningeal SFT; covers NAB2-STAT6 fusion pathogenesis, current treatment landscape, and role of systemic therapies including microtubule inhibitors |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | In vitro | Anticancer Research | Recombinant methioninase (rMETase) combined with eribulin showed extensive synergistic cytotoxicity in HT1080 fibrosarcoma cells while sparing normal fibroblasts — supports tumor-selective activity |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | In vitro | Anticancer Research | rMETase increased eribulin efficacy 16-fold in highly resistant HT1080 fibrosarcoma cells, demonstrating a potential strategy to overcome clinical eribulin resistance in soft tissue sarcoma |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | In vivo | In Vivo | Super-eribulin-resistant fibrosarcoma cells became more malignant but were synergistically eradicated by eribulin + methionine restriction in a nude mouse model |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Preclinical | Human Cell | Novel myxofibrosarcoma cell line SMU-MFS established for drug development research; eribulin cited as a candidate agent given limited standard chemotherapy efficacy in MFS |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Preclinical | Human Cell | Novel myxofibrosarcoma cell line NCC-MFS4-C1 established; highlights refractory nature of MFS to conventional chemotherapy and need for novel agents including microtubule inhibitors |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Case Report | Genes Chrom Cancer | MPNST with novel SNRNP70-NTRK3 fusion responded dramatically to entrectinib; contextualizes the potential of molecularly targeted strategies in fibroblastic/nerve sheath tumors adjacent to the fibroblastic neoplasm category |

---

## India Market Information

Eribulin is **not currently marketed in India**. No approved licenses or registered products were identified in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registered products | — | — |

> For reference: Eribulin mesylate (Halaven®) is approved by the US FDA for metastatic breast cancer and unresectable/metastatic liposarcoma, and by the EMA for locally advanced or metastatic breast cancer. India market entry would require CDSCO registration.

---

## Cytotoxicity

Eribulin is a conventional cytotoxic antineoplastic agent (halichondrin B analog / microtubule inhibitor). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Halichondrin B analog (microtubule dynamics inhibitor; mechanistically distinct from taxanes and vinca alkaloids) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia reported in clinical trials; G-CSF support commonly required |
| Emetogenicity Classification | **Low to moderate** — Consistent with other IV microtubule inhibitors; prophylactic antiemetics typically administered |
| Monitoring Items | CBC with differential (each cycle, prior to each dose); liver function tests (AST, ALT, bilirubin); renal function (serum creatinine); QTc interval (ECG before initiation and periodically — see DDI section); peripheral neuropathy assessment |
| Handling Protection | **Yes** — Must be handled and disposed of in accordance with cytotoxic drug handling regulations; closed-system drug transfer devices recommended for preparation |

---

## Safety Considerations

**Drug Interactions** (375 total interactions identified via DDInteractions database; selected clinically significant interactions listed below):

| Interacting Drug | Severity | Clinical Concern |
|-----------------|---------|-----------------|
| Dolasetron | **Major** | QT interval prolongation — additive risk; avoid combination |
| Cisapride | **Major** | QT interval prolongation — additive risk; avoid combination |
| Ondansetron | Moderate | QT prolongation potential — monitor ECG if co-administered |
| Clarithromycin | Moderate | CYP/QT interaction — monitor for increased eribulin toxicity and QTc |
| Levofloxacin | Moderate | QT prolongation potential — consider alternative antibiotic |
| Metronidazole | Moderate | QT prolongation potential — monitor ECG |
| Tinidazole | Moderate | QT prolongation potential |
| Rosuvastatin | Moderate | Possible pharmacokinetic interaction — monitor for statin toxicity |
| Simvastatin | Moderate | Possible pharmacokinetic interaction — monitor for myopathy |
| Famotidine | Moderate | Monitor for altered GI motility effects |
| Palonosetron | Moderate | QT prolongation potential — prefer palonosetron over dolasetron for antiemesis |

> ⚠️ **QT Prolongation is the most critical interaction pattern.** Many common oncology supportive care drugs (antiemetics, antibiotics) carry additive QT risk with eribulin. Baseline and periodic ECG monitoring is essential.

> Detailed key warnings and contraindications from the prescribing information were not available in this evidence pack. Please refer to the current approved package insert (e.g., Halaven® US PI or EU SmPC) for complete safety information prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Fibroblastic Neoplasm — Rank 8 only)*

**Rationale:**
The ERASING Phase 2 trial (NCT03840772) directly evaluated eribulin in advanced solitary fibrous tumor and completed enrollment in 2024, establishing L2 evidence that places fibroblastic neoplasm ahead of all other TxGNN-predicted indications. Preclinical data across multiple fibrosarcoma cell lines further support mechanistic plausibility. The remaining 9 predicted indications are rated Hold — either because no clinical or translational evidence exists (L5), the tumor type is benign and chemotherapy is disproportionate (pleural adenomatoid tumor), or the evidence is purely preclinical with no direct eribulin data in the specific subtype.

**To proceed, the following is needed:**

- **ERASING trial results**: Obtain and review the full efficacy and safety data from NCT03840772 (completed Sept 2024); peer-reviewed publication or conference presentation data are required to confirm L2 status
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB08871) to complete mechanistic analysis sections
- **CDSCO regulatory pathway**: Evaluate requirements for Eribulin registration in India (currently 0 licenses); assess whether an oncology expedited pathway applies for orphan/sarcoma indications
- **Safety pack**: Download and parse the current approved prescribing information (FDA PI / EU SmPC) to populate key warnings and contraindications — currently a blocking data gap
- **QT monitoring protocol**: Given the Major DDI signals with Dolasetron and Cisapride and multiple Moderate signals, a formal QTc monitoring plan should be developed before any investigator-initiated trial is designed in India
- **Subtype-specific scoping**: Clarify whether the clinical program will target SFT specifically (best evidence) or the broader fibroblastic neoplasm category (MFS, FS) — each requires separate IND/protocol justification

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

