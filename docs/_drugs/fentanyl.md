---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 2
---

# Fentanyl
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

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid analgesic; no Taiwan-specific approved indication text is available since the drug is currently **not marketed in Taiwan**. The TxGNN model predicts a possible link to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is supported by **no clinical trials and no literature** — the model's own rationale flags the mechanistic link as weak and possibly contradictory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and `original_moa` is a data gap; Fentanyl is not currently marketed in Taiwan, so no TFDA-approved indication text exists in this evidence pack |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, Fentanyl is a potent synthetic mu-opioid receptor agonist whose established clinical effects are central analgesia and respiratory depression.

NSIAD is a rare, genetically determined disorder caused by gain-of-function mutations in the AVPR2 (V2 vasopressin) receptor gene, structurally distinct from any opioid signaling pathway. The evidence pack's own mechanistic rationale is explicit that there is **no established mechanistic link** between mu-opioid receptor activity and AVPR2 receptor structure: opioids can influence ADH secretion via the hypothalamic-pituitary axis (occasionally producing SIADH-like effects), but this is an acquired, drug-induced phenomenon distinct from the structural receptor mutation underlying NSIAD — and the rationale notes the direction of effect may even run opposite to what would be needed (opioids more typically *suppress* rather than mimic V2 receptor activation).

A second candidate in this evidence pack, Tourette syndrome (TxGNN score 99.05%, rank 13994), is similarly flagged with a weak, indirect mechanistic rationale (opioid modulation of dopaminergic tone via GABA interneurons) and is explicitly noted as clinically infeasible given the addiction and respiratory-depression risk of using a potent opioid for a non-life-threatening movement disorder. Neither candidate currently has independent mechanistic or clinical support beyond the TxGNN score itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Fentanyl is currently **not marketed in Taiwan** — `taiwan_regulatory.total_licenses` is 0 and no license records are present in this evidence pack.

---

## Safety Considerations

**Drug Interactions** (from DDI database; 327 total interactions on record, 20 representative entries returned in this evidence pack):

| Interacting Drug | Severity |
|---|---|
| Alvimopan | Major |
| Aprepitant | Major |
| Bupropion | Major |
| Clarithromycin | Major |
| Clotrimazole | Major |
| Dexamethasone | Major |
| Dexfenfluramine | Major |
| Dolasetron | Major |
| Fenfluramine | Major |
| Granisetron | Major |
| Lorcaserin | Major |
| Atropine | Moderate |
| Cimetidine | Moderate |
| Clidinium | Moderate |
| Dicyclomine | Moderate |
| Dronabinol | Moderate |
| Eluxadoline | Moderate |
| Glycerol phenylbutyrate | Moderate |
| Glycopyrronium | Moderate |
| Hyoscyamine | Moderate |

Key warnings and contraindications are not available in this evidence pack (marked as a **Blocking** data gap, DG001 — TFDA label warnings/contraindications must be sourced before this candidate can enter S1 safety screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — the TxGNN score is unsupported by any clinical trial or literature evidence, and the model's own mechanistic rationale explicitly describes the receptor-level link to NSIAD (and to the alternative Tourette syndrome candidate) as weak or potentially contradictory. Combined with the Blocking data gap on TFDA safety labeling, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Confirmed mechanism of action data from DrugBank (DG002)
- Independent preclinical or mechanistic evidence linking mu-opioid receptor activity to AVPR2-mediated antidiuresis, beyond the TxGNN score alone
- Clarification of regulatory pathway given Fentanyl is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

