---
layout: default
title: Papain
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
---

# Papain
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

# Papain: From Original Indication Unavailable to Primary Release Disorder of Platelets

## One-Sentence Summary

Papain (DrugBank DB11193) is a proteolytic enzyme; the current evidence pack contains no record of its original approved indication or mechanism of action.
The TxGNN model's top prediction points to **Primary Release Disorder of Platelets**,
but this is supported by only **1 publication** and **0 clinical trials**, and that single publication appears unrelated to papain's actual pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication on record in this evidence pack) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 98.22% |
| Evidence Level | L4 |
| India Market Status | Not marketed (0 registrations) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Papain is not available, and no approved original indication is on record — the evidence pack's only successful inputs were a DrugBank identity match and PubMed literature search (`inputs_received: drugbank, pubmed`). Regulatory label data (warnings/contraindications) is flagged as a **Blocking** data gap, so no baseline safety or indication context can be established at this time.

For the top-ranked prediction, the single supporting article (PMID 38430019) is a rabbit osteoarthritis study comparing leukocyte-rich vs. leukocyte-poor platelet-rich plasma (PRP) on cartilage repair — it does not involve papain at all. The connection appears to be a keyword co-occurrence artifact ("platelet") in the knowledge graph rather than a genuine mechanistic pathway, which is consistent with the model's own scoring (Evidence Level L4, decision stage S0, recommendation **Hold**).

Reviewing the other 9 candidates in this pack reinforces the same pattern: ranks 2 and 4 use papain only as a laboratory reagent (platelet epitope digestion; antibody Fab-fragment preparation for imaging), rank 7's 19 "hits" are Hepatitis B vaccine/B-cell/HLA-B literature matched purely on the letter "B", and ranks 3, 5, 6, 8, 9, 10 have no literature or trial support at all (pure embedding similarity, L5). No candidate in this pack currently has a defensible mechanistic or clinical rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38430019](https://pubmed.ncbi.nlm.nih.gov/38430019/) | 2024 | Preclinical (rabbit model) | Cellular and Molecular Biology (Noisy-le-Grand) | Compares leukocyte-rich vs. leukocyte-poor PRP for cartilage repair in a rabbit osteoarthritis model; papain is not studied or mentioned — matched only via the "platelet" keyword, not mechanistically relevant to this indication. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Original indication, mechanism of action, and regulatory safety label data are all unavailable — including a Blocking-severity gap (DG001) that prevents even an initial safety screen (S1). The top-ranked predicted indication's only literature support is unrelated to papain's pharmacology, and no other candidate in this pack has stronger evidence, so there is currently no basis to advance beyond Hold.

**To proceed, the following is needed:**
- Papain's approved original indication(s) and mechanism of action (DrugBank/label lookup)
- TFDA/regulatory label warnings and contraindications (DG001, Blocking)
- A working DDI reference dataset (the DDInter interaction file was missing, causing the DDI query to error out)
- Independent mechanistic or clinical evidence directly linking papain to platelet-release disorders, beyond the single unrelated PRP study identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

