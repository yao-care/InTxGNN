---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: From Prolactinoma / Hyperprolactinemia to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a highly selective dopamine D2/D3 receptor agonist, established as first-line therapy for hyperprolactinemia and prolactin-secreting pituitary adenomas (prolactinomas).
The TxGNN model predicts it may be effective for **Pituitary Adenocarcinoma** with a prediction score of 99.06%; however, current supporting evidence is limited to **3 case reports** and **no registered clinical trials** specifically for this malignant indication.
Given the extreme rarity of the disease and significant mechanistic uncertainty, this prediction represents a research hypothesis rather than an immediately actionable clinical target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperprolactinemia / Prolactinoma (inferred from clinical context; no India registration data available) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not captured in this Evidence Pack. Based on available clinical and pharmacological information, Cabergoline is a selective ergot-derived dopamine D2/D3 receptor agonist whose efficacy in treating prolactinomas — benign prolactin-secreting pituitary adenomas — is well-established and guideline-endorsed. It acts by binding pituitary cell surface D2 receptors, suppressing prolactin gene transcription and secretion, and inducing tumor cell apoptosis that leads to measurable tumor volume reduction.

The biological rationale for extending this mechanism to pituitary adenocarcinoma rests on a plausible molecular cascade: D2 receptor activation → inhibition of adenylyl cyclase → reduction of intracellular cAMP → suppression of tumor cell proliferation and induction of apoptosis. The critical question is whether this pathway remains intact in malignant pituitary cells. Pituitary adenocarcinoma is defined by cerebrospinal or systemic metastasis and is exceptionally rare, accounting for fewer than 0.2% of all pituitary tumors. Whether D2 receptor expression and downstream signaling are preserved — or are altered or lost — in the malignant phenotype is currently unknown.

The extrapolation from a robust mechanistic and clinical foundation in benign adenoma to a rare, poorly characterized malignancy therefore carries significant biological uncertainty. The three identified publications are incidental case reports and do not directly test Cabergoline as therapy for adenocarcinoma. This prediction is best interpreted as a scientifically motivated hypothesis requiring preclinical validation before any clinical translation is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pituitary adenocarcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case Report | Endocrine Practice | Long-term octreotide or cabergoline management in a patient with ectopic ACTH hypersecretion who underwent adrenalectomy; documents cabergoline use in a corticotropin-related pituitary context |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case Report | Rev Esp Enferm Dig | A patient on cabergoline for pituitary adenoma was incidentally diagnosed with poorly differentiated pancreatic adenocarcinoma presenting as duodenal lymphangiectasia; cabergoline use is background history, not the investigated treatment |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case Report | Medicine | MEN1 gene variant of uncertain pathogenicity presenting with multiple endocrine tumors; cabergoline mentioned as part of clinical management, not as an investigational agent for adenocarcinoma |

> **Note:** None of these publications directly study Cabergoline as treatment for pituitary adenocarcinoma. Their relevance is incidental. Evidence is L4 (case-level, mechanism-adjacent only).

---

## India Market Information

Cabergoline currently has **no registered products** in India. No authorization or licensing data is available from the regulatory database.

---

## Safety Considerations

**Drug Interactions** (60 total interactions identified across all severity levels):

| Interacting Drug | Severity | Clinical Implication |
|------|---------|---------------------|
| Lorcaserin | **Major** | Serious interaction; combination should be avoided |
| Clarithromycin | **Major** | Serious interaction; use with caution or avoid |
| Metoclopramide | Moderate | Dopamine antagonist — directly opposes Cabergoline's mechanism; monitor or avoid concurrent use |

Additional interactions of unknown severity have been identified with: Calcitriol, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Rosiglitazone, Lansoprazole, Lactulose, Prednisone, Simvastatin, Hydrocortisone, Prednisolone, Ranitidine, Famotidine, Rabeprazole, and Pioglitazone.

Formal warning and contraindication data (from the package insert) are not yet available in this Evidence Pack and must be retrieved before any safety evaluation can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pituitary adenocarcinoma is an extremely rare malignancy with no dedicated clinical trial program for Cabergoline and only marginally relevant case-level literature. Although the D2 receptor mechanistic hypothesis is biologically coherent, extrapolation from well-evidenced benign adenoma data to a malignant context requires explicit preclinical and receptor-expression validation that does not yet exist.

**To proceed, the following is needed:**
- Confirm D2 receptor expression and cAMP signaling integrity in pituitary adenocarcinoma tissue (immunohistochemistry or transcriptomic evidence from tumor registries)
- Conduct in vitro studies in malignant pituitary cell lines to verify antiproliferative activity of Cabergoline
- Retrieve full MOA documentation from DrugBank (DG002) to support mechanistic narrative
- Obtain the India package insert / product label to assess warnings, contraindications, and population-specific restrictions (DG001 — currently a blocking data gap)
- Consider pivoting the primary repurposing target to **Pituitary Cancer (Rank 3)**, which carries L2 evidence with 20 clinical trials and 20 publications, including an ongoing Phase 3 RCT — a substantially more tractable near-term development pathway than the rare adenocarcinoma subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

