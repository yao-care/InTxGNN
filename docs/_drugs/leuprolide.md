---
layout: default
title: Leuprolide
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 2
---

# Leuprolide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leuprolide: From Hormone-Sensitive Cancers to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH (gonadotropin-releasing hormone) agonist widely used in the treatment of hormone-sensitive conditions such as prostate cancer and endometriosis.
The TxGNN model predicts it may be effective for **Osteoarthritis**, but this prediction carries **no supporting clinical evidence** — the single trial and publication retrieved were unrelated false positives.
With an evidence level of **L5**, this candidate is currently unsuitable for further development without foundational preclinical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer / hormone-sensitive cancers (endometriosis, uterine fibroids, central precocious puberty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only — no relevant studies found) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on established pharmacology, Leuprolide is a synthetic GnRH agonist that, upon continuous administration, causes paradoxical downregulation of pituitary GnRH receptors — leading to profound suppression of testosterone (in males) and estrogen (in females). This is its primary mechanism in oncology and gynaecology.

The theoretical link to osteoarthritis rests on the observation that sex hormones (estrogen and testosterone) play a modulatory role in cartilage metabolism, and that GnRH receptors have been identified on synoviocytes and chondrocytes in small in vitro studies. This provides a narrow biological rationale for the TxGNN graph-based prediction.

However, the mechanistic direction is arguably **unfavourable**: Leuprolide-induced sex hormone suppression is well associated with accelerated bone mineral density loss and increased fracture risk. Chronic hypogonadism from GnRH agonist therapy may, in fact, worsen joint loading and articular cartilage stress rather than ameliorate osteoarthritis. There is no preclinical animal model or human proof-of-concept study supporting the hypothesis that Leuprolide improves OA outcomes. The TxGNN connection most likely reflects graph topology clustering of "cartilage/bone" nodes rather than a true pharmacological relationship.

---

## Clinical Trial Evidence

> ⚠️ **Note:** The single trial retrieved is a **false positive** (Relevance Grade C). It is a prostate cancer study that uses Leuprolide as a comparator LHRH analogue and has no relationship to osteoarthritis. It is listed for transparency but must **not** be interpreted as supporting evidence for this repurposing hypothesis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | N/A | ⚠️ FALSE POSITIVE — Orchiectomy/LHRH analogue ± flutamide ± suramin in metastatic prostate cancer; no OA relevance |

**Effective clinical trial evidence for osteoarthritis: None**

---

## Literature Evidence

> ⚠️ **Note:** The single publication retrieved is a **false positive**. It is a case report of metastatic prostatic adenocarcinoma presenting as inflammatory breast carcinoma — it has no relevance to osteoarthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case Report | Clinical Breast Cancer | ⚠️ FALSE POSITIVE — Metastatic prostate cancer mimicking inflammatory breast carcinoma; no OA relevance |

**Effective literature evidence for osteoarthritis: None**

---

## India Market Information

Leuprolide is **not currently marketed in India**. No approved product licenses are on record. This section cannot be populated.

---

## Cytotoxicity

Leuprolide is classified as an antineoplastic agent used in hormone-sensitive malignancies. However, it is **not a conventional cytotoxic drug** — it acts through hormonal downregulation rather than direct DNA damage or cell-killing mechanisms.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal antineoplastic (GnRH agonist) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not a myelosuppressive agent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Bone mineral density (DEXA scan), serum testosterone/estradiol, PSA (if prostate cancer), liver function, cardiovascular risk markers |
| Handling Protection | Standard precautions apply; cytotoxic handling regulations are not required for GnRH agonists |

---

## Safety Considerations

Package insert warnings and contraindications are not available in this evidence pack. Please refer to the approved package insert for the relevant jurisdiction.

**Drug Interactions:** 261 drug-drug interactions have been identified via DDInter. Notable interactions include:

| Severity | Interacting Drug | Clinical Implication |
|----------|-----------------|---------------------|
| **Major** | Dolasetron | Risk of QT prolongation; cardiac monitoring advised |
| **Major** | Cisapride | Risk of QT prolongation; combination contraindicated |
| Moderate | Clarithromycin | Potential QT interval prolongation |
| Moderate | Metformin | Hormonal suppression may affect glycaemic control |
| Moderate | Canagliflozin, Dapagliflozin, Empagliflozin | Hormonal effects may interact with SGLT2-mediated glucose metabolism |
| Moderate | Acarbose, Alogliptin, Saxagliptin, Linagliptin | Potential interactions with glucose-lowering agents |
| Moderate | Albiglutide, Dulaglutide | GLP-1 agonist interactions with hormonal suppression |
| Moderate | Loperamide, Bisacodyl, Picosulfuric acid, Castor oil, PEG 3350 | Gastrointestinal motility effects |
| Moderate | Famotidine | Gastric pH-related pharmacokinetic interaction |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.70%) to the Leuprolide–Osteoarthritis pair, but this reflects graph topology rather than pharmacological plausibility. The mechanistic direction is likely **unfavourable** (sex hormone suppression is associated with bone loss, not joint protection), and zero relevant clinical trials or publications were identified — the single trial and paper retrieved were unrelated false positives. This candidate does not meet the minimum threshold (L4) for further evaluation.

**To proceed, the following would be needed:**

- **Mechanistic proof-of-concept data**: In vitro evidence that Leuprolide or GnRH modulation has a direct chondroprotective or anti-inflammatory effect in OA models (e.g., synoviocyte or chondrocyte assays)
- **Animal model data**: A preclinical OA model (e.g., DMM mouse model) demonstrating histological cartilage protection under Leuprolide treatment
- **MOA clarification**: Full DrugBank mechanism of action data to assess whether any off-target pathways (e.g., neuroinflammation, cytokine modulation) could be relevant to OA
- **Safety package**: TFDA / approved jurisdiction package insert to assess contraindications and warnings before any human study can be considered
- **Re-evaluation**: If preclinical data emerges, upgrade evidence level from L5 to L4 and re-assess at Stage 0 gate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

