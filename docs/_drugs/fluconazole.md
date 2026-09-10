---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a triazole antifungal agent, primarily used to treat systemic and mucocutaneous fungal infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is based solely on knowledge-graph embedding similarity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (no Taiwan licenses on file); Fluconazole is a known triazole-class antifungal per the mechanistic rationale data |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% (rank 11,709) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available (original_moa: Data Gap). Based on the mechanistic notes in the evidence pack, Fluconazole is a triazole antifungal that inhibits fungal cytochrome P450-dependent 14α-demethylase (lanosterol demethylase), blocking ergosterol synthesis and disrupting fungal cell membrane integrity.

Punctate epithelial keratoconjunctivitis is, in the large majority of cases, caused by viral infection (e.g., adenovirus, herpes simplex virus), dry eye disease, or immune-mediated inflammation; only a small subset of cases (superficial forms of fungal/candidal keratitis) are fungal in origin. Fluconazole's antifungal mechanism therefore has no direct relevance to the viral or inflammatory etiologies that account for most cases of this condition.

The high TxGNN score (99.24%) most likely reflects structural proximity between Fluconazole and other anti-infective or ophthalmic agents within the knowledge-graph embedding space, rather than a demonstrated pathophysiological link. Given the missing MOA data and the empty original-indication record, this mechanistic rationale should be treated as weak and speculative pending further evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Fluconazole currently has no marketing license on record in Taiwan (market_status: 未上市, total_licenses: 0). No registration entries are available to summarize.

---

## Safety Considerations

**Drug Interactions**: A total of 783 documented interactions were found. Notable entries include:

| Interacting Drug | Severity Level |
|---|---|
| Chlorpropamide | Major |
| Famotidine | Moderate |
| Rabeprazole | Moderate |
| Hydrocortisone | Moderate |
| Loperamide | Moderate |
| Aprepitant | Moderate |
| Triamcinolone | Moderate |
| Omeprazole | Moderate |
| Dexamethasone | Moderate |
| Betamethasone | Moderate |
| Budesonide | Moderate |
| Saxagliptin | Moderate |
| Dexlansoprazole | Moderate |
| Clarithromycin | Minor |
| Amphotericin B | Minor |

Key warnings and contraindications are not currently available in the evidence pack (flagged as a Blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is at evidence level L5 — a model prediction with no supporting clinical trials or literature, and a mechanistic link assessed as weak given the predominantly non-fungal etiology of the target condition. In addition, TFDA label warnings/contraindications are marked as a **Blocking** data gap (DG001), which by itself prevents this candidate from entering the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the Blocking gap before any safety review
- Confirmed mechanism of action (MOA) data from DrugBank
- Targeted literature/clinical trial search for antifungal use in punctate epithelial keratoconjunctivitis or fungal keratitis, to test whether any subset of the target population (fungal-etiology cases) is mechanistically relevant
- Route/formulation compatibility assessment — the predicted indication is ophthalmic, and available Fluconazole formulations/routes have not yet been confirmed as suitable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

