---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK+ Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Ceritinib (Zykadia) is a second-generation ALK/IGF-1R tyrosine kinase inhibitor, globally approved for ALK-positive, metastatic non-small cell lung cancer (NSCLC), though it is not currently registered in India.
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival** with a prediction score of 99.86%.
However, **no clinical trials and no publications** currently support this specific repurposing direction — the prediction is based on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK+ metastatic NSCLC (global approval; not registered in India) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Ceritinib is a potent second-generation ALK (anaplastic lymphoma kinase) tyrosine kinase inhibitor that also inhibits IGF-1R (insulin-like growth factor 1 receptor) and FAK (focal adhesion kinase). Its efficacy in ALK-rearranged NSCLC has been established in pivotal clinical trials, and these same kinase targets are implicated in fibroblast proliferation and extracellular matrix remodelling pathways.

Gingival fibromatosis is characterised by excessive proliferation of gingival fibroblasts, either through hereditary GINGF gene mutations or drug-induced mechanisms (e.g. phenytoin, calcium channel blockers). The TxGNN prediction likely originates from knowledge graph network traversal linking "fibrous proliferation → growth factor signalling → ALK/IGF-1R nodes." IGF-1R in particular has documented roles in fibroblast activation and connective tissue overgrowth, which provides a tenuous but non-zero mechanistic rationale.

However, there is **no experimental or clinical evidence** directly linking ALK or IGF-1R inhibition to gingival fibromatosis pathology. The prediction should be interpreted as a hypothesis-generating signal rather than an actionable therapeutic lead. Molecular profiling of gingival fibroblasts for ALK expression or IGF-1R overactivation would be a necessary first step before considering any translational programme.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ceritinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Ceritinib in Fibromatosis, Gingival.

---

## Cytotoxicity

Ceritinib meets the criteria for antineoplastic classification (targeted kinase inhibitor, indicated for malignant NSCLC).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Second-generation ALK tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low to Moderate (less myelosuppressive than conventional cytotoxics; anaemia and neutropenia reported but uncommon) |
| Emetogenicity Classification | Moderate (nausea, vomiting, and diarrhoea are among the most frequent adverse effects; antiemetic prophylaxis recommended) |
| Monitoring Items | Liver function tests (ALT/AST — hepatotoxicity is a known risk), ECG (QT interval prolongation), blood glucose, CBC, amylase/lipase (pancreatitis), pulmonary function (interstitial lung disease/pneumonitis) |
| Handling Protection | Standard cytotoxic drug handling precautions apply; avoid crushing or splitting capsules |

---

## Safety Considerations

**Drug Interactions:** Ceritinib has **629 documented drug interactions** in the DDI database. Key interactions identified include:

| Severity | Interacting Drug | Clinical Relevance |
|----------|----------------|--------------------|
| **Major** | Triamcinolone | Risk of enhanced corticosteroid exposure via CYP3A4 inhibition; systemic toxicity |
| **Major** | Budesonide | Same CYP3A4-mediated mechanism; elevated corticosteroid plasma levels |
| Moderate | Omeprazole, Rabeprazole, Famotidine, Ranitidine | Gastric pH elevation may reduce ceritinib absorption |
| Moderate | Dexamethasone, Betamethasone, Hydrocortisone | CYP3A4 interactions; corticosteroid exposure alteration |
| Moderate | Metformin, Canagliflozin, Pioglitazone, Alogliptin, Albiglutide, Acarbose | Potential pharmacodynamic interaction with blood glucose regulation; hyperglycaemia is a known ceritinib adverse effect |
| Moderate | Aprepitant | CYP3A4 inhibitor; may increase ceritinib plasma levels |
| Moderate | Loperamide, Bisacodyl | Used to manage ceritinib-induced diarrhoea; monitor for over-correction |

> ⚠️ With 629 total interactions, a comprehensive medication reconciliation review is mandatory before initiation. Please refer to the full package insert for complete warnings and contraindications (TFDA/EMA/FDA prescribing information should be consulted directly).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN model inference (Evidence Level L5) with no supporting clinical trials, publications, or preclinical data linking Ceritinib's ALK/IGF-1R inhibition mechanism to gingival fibromatosis pathobiology. The mechanistic plausibility is speculative and the benefit-risk ratio for applying a drug with 629 interactions and significant hepatotoxicity, QT prolongation, and GI toxicity risk to a non-malignant fibrous condition is unfavourable without any experimental basis.

**To proceed, the following is needed:**
- Basic science investigation: assess ALK and IGF-1R expression in gingival fibroblasts from fibromatosis patients (immunohistochemistry, RNA-seq)
- Ceritinib mechanism of action data (DrugBank API retrieval; DG002 remediation)
- TFDA/global package insert warnings and contraindications (DG001 remediation — required before any S1 safety evaluation)
- Literature review broadened to ALK inhibitors + fibroblast proliferation / connective tissue disorders (not restricted to gingival fibromatosis)
- Pathway analysis: confirm whether IGF-1R or FAK (Ceritinib's secondary targets) play a documented role in gingival fibroblast hyperplasia models
- If preclinical rationale is established: in vitro study in primary gingival fibroblast cultures before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

