---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

*Note: Fosaprepitant's original indication is not recorded in the structured regulatory data (the drug is not marketed in India, so no license text is available). The characterization below as an antiemetic used in chemotherapy support is drawn directly from the clinical trial and literature evidence contained in this evidence pack, not from an external or assumed source.*

## One-Sentence Summary

Fosaprepitant is a neurokinin-1 (NK1)/substance P receptor antagonist prodrug, historically used as supportive antiemetic therapy alongside chemotherapy (evidenced by the trial records collected here). The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the model's own mechanistic annotation states there is no known biological link between NK1 antagonism and NSIAD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in regulatory data (drug not marketed in India); trial evidence points to chemotherapy-induced nausea and vomiting (CINV) supportive care |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fosaprepitant is not available in the structured drug record (marked as a data gap). However, evidence gathered elsewhere in this pack consistently identifies fosaprepitant as a prodrug of aprepitant, acting as a neurokinin-1 (NK1)/substance P receptor antagonist, historically used as adjunct antiemetic therapy for chemotherapy-induced nausea and vomiting.

For the top-ranked prediction, NSIAD, the model's own repurposing rationale is explicit and should be read at face value: NSIAD is caused by gain-of-function mutations in the AVPR2 (vasopressin V2 receptor) gene, a pathway with **no known interaction** with the substance P/NK1 receptor system that fosaprepitant targets. No clinical trial, case report, or mechanistic study in this evidence pack connects the two.

In short, this candidate is a **pure statistical association from the TxGNN knowledge graph**, not a mechanistically or clinically supported hypothesis. It should not be interpreted as validated repurposing evidence at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Fosaprepitant is not currently marketed in India (0 registrations, 0 licenses on file), so no product/authorization information is available.

## Safety Considerations

**Drug Interactions**: DDI screening returned 158 total interactions on record. Notable interactions include:

| Interacting Drug | Severity |
|---|---|
| Eliglustat | Major |
| Naloxegol | Major |
| Rabeprazole | Moderate |
| Hydrocortisone | Moderate |
| Alosetron | Moderate |
| Betamethasone | Moderate |
| Budesonide (systemic and nasal) | Moderate |
| Cimetidine | Moderate |
| Clarithromycin | Moderate |
| Dronabinol | Moderate |
| Pioglitazone | Moderate |
| Triamcinolone | Moderate |
| Dexamethasone | Moderate |
| Saxagliptin | Moderate |
| Glimepiride | Moderate |
| Naldemedine | Moderate |
| Lansoprazole | Moderate |
| Miconazole | Moderate |
| Nateglinide | Moderate |

Formal key warnings and contraindications (e.g., TFDA/India label text) are not yet available for this drug — this is flagged as a Blocking data gap (DG001) and must be resolved before any safety assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for NSIAD is very high (99.92%), there is zero clinical trial or literature support, and the model's own mechanistic annotation explicitly states no known biological connection between NK1 antagonism and the AVPR2-driven pathophysiology of NSIAD. This is evidence level L5 (model prediction only) and does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- Mechanism of action data for fosaprepitant (DrugBank API query, currently a High-severity gap)
- TFDA/India label warnings and contraindications (Blocking gap, DG001) — required before any safety pre-screening (S1)
- Preclinical or in vitro studies specifically testing NK1 antagonism in vasopressin/AVPR2-related pathways
- Consider re-evaluating lower-ranked but mechanistically better-supported candidates in this pack — notably retinitis (rank 5, L4, evidence level "Research Question"), which has preclinical literature showing fosaprepitant blocks UVR-B-induced NK1 receptor expression in ocular tissue
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

