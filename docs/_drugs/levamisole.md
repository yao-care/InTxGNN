---
layout: default
title: Levamisole
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Levamisole
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

# Levamisole: From Immunostimulation to Drug-Induced Osteoporosis

## One-Sentence Summary

Levamisole is a broad-spectrum anthelmintic and immunostimulant historically used for parasitic infections and as adjuvant immunotherapy (notably in combination with 5-FU for colorectal cancer).
The TxGNN model predicts it may be relevant to **Drug-Induced Osteoporosis** as its highest-ranked new indication (score 99.9993%), with **0 clinical trials** and **0 publications** directly supporting this use.
Critically, the proposed mechanistic link carries a potentially adverse signal: as an ALP inhibitor, Levamisole may theoretically **impair** bone mineralization rather than treat osteoporosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (drug not registered in India regulatory records) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.9993% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on information cited in the repurposing rationale, Levamisole is known to function as an **alkaline phosphatase (ALP) inhibitor** and immunostimulant — activating T cells and macrophages, and inhibiting ecto-5'-nucleotidase (CD73), which converts AMP to immunosuppressive adenosine in the tumor microenvironment.

Regarding the connection to drug-induced osteoporosis: ALP is an enzyme indispensable for bone mineralization. **Inhibiting ALP would theoretically impair bone formation**, which is precisely the opposite of what an osteoporosis therapy aims to achieve. This creates a **potentially adverse mechanistic signal** — Levamisole's ALP-inhibitory property could contribute to, rather than protect against, reduced bone density. No supporting clinical or preclinical evidence offsets this concern.

The TxGNN score of 99.9993% reflects a graph-based prediction derived from molecular relationships in the knowledge graph, not demonstrated clinical or biological efficacy. Given the contradictory mechanistic direction and complete absence of supporting evidence, this remains a purely computational prediction at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Levamisole is currently **not marketed in India** based on available regulatory data, with **0 approved registrations** on record.

---

## Safety Considerations

**Drug Interactions** (73 total interactions documented):

Major interactions requiring clinical attention:

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|-------------------|--------------------|
| Deferiprone | Major | Potential additive myelosuppression risk |
| Adalimumab | Major | Immunostimulant opposing immunosuppressive biologics |
| Baricitinib | Major | Conflicting immune pathway modulation |
| Certolizumab pegol | Major | Opposing TNF-axis modulation |
| Cladribine | Major | Additive immunosuppression risk |
| Samarium (153Sm) lexidronam | Major | Hematologic toxicity risk |

Notable moderate interactions:

| Interacting Drug | Interaction Level |
|-----------------|-------------------|
| Warfarin | Moderate — anticoagulation monitoring recommended |
| Ethanol | Moderate |
| Zidovudine | Moderate |
| Azathioprine | Moderate |
| Clostridium tetani toxoid antigen | Moderate — immune response alteration |
| Anthrax vaccine | Moderate |
| Alemtuzumab, Anakinra, Canakinumab, Alefacept | Moderate — immunomodulatory overlap |

Package insert warnings and contraindications are not currently available in this Evidence Pack. Please refer to the official package insert for complete safety information.

---

## Appendix: Full Top-10 Prediction Landscape

For reference, all 10 TxGNN predictions evaluated in this multi-indication candidate are summarized below:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Notes |
|------|---------------------|-------------|----------------|----------|-------|
| 1 | Drug-Induced Osteoporosis | 99.9993% | L5 | Hold | Adverse mechanistic signal (ALP inhibition) |
| 2 | Benign Neoplasm of Tongue | 99.9963% | L5 | Hold | No evidence; weak mechanistic link |
| 3 | Cervical Neuroblastoma | 99.9963% | L5 | Hold | 1 tangential cell-line study (PMID [12825832](https://pubmed.ncbi.nlm.nih.gov/12825832/)); not clinical evidence |
| 4 | Benign Neoplasm of Buccal Mucosa | 99.9963% | L4 | Research Question | 2 animal studies (1970s hamster DMBA model); very limited translatability |
| 5 | Epiglottis Neoplasm | 99.9963% | L5 | Hold | HPV hypothesis unverified; no evidence |
| 6 | Cystic Neoplasm | 99.9962% | L5 | Hold | Heterogeneous etiology; non-specific prediction |
| 7 | Benign Neoplasm of Floor of Mouth | 99.9961% | L5 | Hold | Glandular obstruction etiology; weak immune link |
| 8 | Schwannoma of Jugular Foramen | 99.9961% | L5 | Hold | NF2/Merlin-driven; no known mechanistic intersection |
| 9 | Benign Neoplasm of Hypopharynx | 99.9961% | L4 | Research Question | 2 publications on malignant H&N tumors — indication mismatch (benign vs. malignant) |
| 10 | Inner Ear Neoplasm | 99.9960% | L5 | Hold | NF2-driven acoustic neuroma; no mechanistic link |

Most promising for further inquiry (L4): **Benign Neoplasm of Buccal Mucosa** (Rank 4) and **Benign Neoplasm of Hypopharynx** (Rank 9), where indirect animal or head-and-neck malignancy literature exists, though both carry significant translational limitations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (drug-induced osteoporosis) carries zero supporting evidence and a mechanistically adverse signal — ALP inhibition could worsen rather than treat osteoporosis. All remaining top-10 predictions are also L4–L5, with no completed clinical trials across any indication.

**To proceed with any indication, the following is needed:**

- **MOA clarification**: Retrieve full mechanism of action data from DrugBank (DB00848) to resolve current data gap — specifically to confirm ALP inhibitory activity and its net bone metabolic effect
- **Safety data**: Download and parse TFDA/CDSCO package insert PDF to address missing warnings and contraindications (currently blocking S1 safety screening)
- **For Ranks 4 & 9 (L4 indications)**: Define specific research questions — e.g., does Levamisole's immune modulation extend to benign oral/pharyngeal mucosal tumors? Does modern PD-1/PD-L1 immunotherapy supersede any potential role for Levamisole in head-and-neck disease?
- **Re-evaluation of Rank 1**: Conduct preclinical assessment of net osteoblast/osteoclast activity under Levamisole exposure before this prediction can be reconsidered

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. This content is YMYL-sensitive and should not be used to guide therapeutic decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

