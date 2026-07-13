---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a selective CCR5 antagonist and antiretroviral agent approved for HIV-1 infection, preventing viral entry into CD4+ T cells by blocking the CCR5 co-receptor.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia** (MEN, score rank 1),
however, **no clinical trials** and **no supporting literature** currently exist for this specific indication — the prediction is classified as L5 (model-only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral, CCR5 antagonist entry inhibitor) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Maraviroc is a first-in-class small-molecule CCR5 antagonist. It binds allosterically to CCR5 on the surface of CD4+ T cells and macrophages, blocking the interaction between HIV-1 gp120 and the CCR5 co-receptor, thereby preventing R5-tropic HIV-1 from entering host cells. Beyond antiviral activity, CCR5 is broadly expressed on innate and adaptive immune effector cells, giving this mechanism theoretical immunomodulatory reach.

Multiple Endocrine Neoplasia (MEN) refers to a family of inherited neuroendocrine tumor syndromes driven by germline mutations in MEN1, RET, or CDKN1B, causing proliferation in pituitary, parathyroid, and pancreatic islet cells. The pathological hallmark is cell-autonomous oncogenic signaling — not chemokine-driven immune trafficking. CCR5 expression and functional role in neuroendocrine tumors is not documented in the existing literature, and no established signaling pathway connects CCR5 blockade to MEN tumorigenesis.

As the TxGNN repurposing rationale notes, this high prediction score most likely arises from indirect proximity between tumor-associated nodes in the knowledge graph rather than a direct biological mechanism. Graph-based models can rank indications highly when a drug shares neighborhood nodes with a disease, even when no direct mechanistic link exists. This is a known limitation of knowledge-graph inference methods, and the score should be interpreted with caution in the absence of corroborating experimental data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Maraviroc in Multiple Endocrine Neoplasia.

---

## Literature Evidence

Currently no related literature available for Maraviroc in Multiple Endocrine Neoplasia.

---

## India Market Information

Maraviroc (DrugBank: DB04835) currently has **no registrations** in the Indian market.

For reference, Maraviroc is approved in other major jurisdictions:

| Jurisdiction | Brand Name | Dosage Form | Approved Indication |
|-------------|-----------|-------------|-------------------|
| USA (FDA, 2007) | Selzentry® | Tablet 150/300 mg | HIV-1 infection (R5-tropic, treatment-experienced adults) |
| EU (EMA, 2007) | Celsentri® | Tablet 150/300 mg | HIV-1 infection (R5-tropic, treatment-experienced adults) |

*Note: The above information is provided for regulatory context; no Indian (CDSCO) registrations are on record in this dataset.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/CDSCO label warnings and contraindications are currently unavailable (Data Gap DG001). DDI database query returned no results due to a missing data file. Both gaps should be resolved before any clinical or regulatory assessment proceeds.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for Maraviroc — Multiple Endocrine Neoplasia — is an L5 signal with no clinical trials, no literature support, and a mechanistic rationale assessed as having "no clinical significance." Progressing this pairing without any biological foundation would not be a responsible use of research resources.

**To proceed toward any clinical evaluation, the following is needed:**

- **Mechanistic validation:** CCR5 expression profiling in MEN tumor tissue (IHC or RNA-seq), to establish whether the target is even present
- **Preclinical proof-of-concept:** In vitro studies in neuroendocrine tumor cell lines (e.g., BON-1, QGP-1) and MEN1-knockout mouse models
- **MOA documentation:** Query DrugBank API to retrieve full pharmacology entry (DG002)
- **Safety baseline:** Download and parse TFDA/FDA package insert PDF for key warnings and contraindications (DG001)
- **DDI data:** Restore the DDInter CSV database file to enable drug–drug interaction analysis

---

### Notable Finding: More Promising Indication Exists in This Dataset

Although **Multiple Endocrine Neoplasia** ranks first by TxGNN score, the mechanistic rationale across all 10 predictions is strongest for **HER2-positive breast carcinoma (rank 10, L4)**:

> PMID [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) (Zazo et al., *Mol Cancer Ther*, 2020) directly demonstrates that HER2+ breast cancer cells deploy autocrine **CCL5 → CCR5 → ERK** signaling to develop trastuzumab (Herceptin) resistance. Maraviroc, as a CCR5 antagonist, theoretically blocks this resistance axis and could restore trastuzumab sensitivity — a clinically actionable hypothesis worth dedicated investigation.

Similarly, **primary cutaneous T-cell lymphoma (rank 3, L4)** has indirect support from chemokine network literature (PMID [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/)), given high CCR5 and CCL5 expression on malignant T cells in CTCL.

If prioritization is required, these two indications — not the top-ranked MEN — represent the more scientifically defensible candidates for Maraviroc repurposing research.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

