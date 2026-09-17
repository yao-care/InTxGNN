---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor (EGFR-TKI) originally developed for EGFR mutation-positive non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-score prediction with no mechanistic or empirical backing found in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (NSCLC), EGFR mutation-positive (per repurposing rationale notes; formal MOA/indication fields are a data gap — see below) |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for gefitinib is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the repurposing rationale fields, gefitinib is known to act as an EGFR tyrosine kinase inhibitor, and its established efficacy is in EGFR mutation-positive NSCLC.

Gingival fibromatosis is a connective-tissue overgrowth disorder with no established EGFR-driven pathogenesis. The evidence pack's own mechanistic assessment for this candidate states explicitly that despite the high TxGNN score, there is no known EGFR-driven mechanism linking the two conditions, and the prediction is unsupported by any clinical trial or literature evidence — it should be treated as a pure knowledge-graph artifact rather than a validated hypothesis.

For context, two lower-ranked candidates in this pack — **lung hilum carcinoma** (rank 5) and **pulmonary sulcus neoplasm** (rank 8) — carry somewhat stronger rationale, since both are anatomical subtypes of NSCLC and align with gefitinib's known EGFR-TKI mechanism. However, the pack's own analysis notes these represent an anatomical extension of the existing NSCLC indication rather than genuine repurposing, and both remain at evidence level L4 with only case-report/overview-level support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Gefitinib currently holds **0 registered licenses** in the Taiwan regulatory dataset (market status: not marketed). No product, dosage form, or approved-indication records are available to list.

---

## Cytotoxicity

Gefitinib's original indication (NSCLC) is an oncology indication and its class (EGFR-TKI) qualifies it for cytotoxicity/antineoplastic assessment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: The evidence pack's DDI query returned 349 total catalogued interactions; a sample of 20 is available below. Most listed interactions are **Moderate**-level and involve gastric-acid-modifying agents (H2 antagonists and proton pump inhibitors), which is mechanistically notable since gefitinib absorption is pH-dependent:

| Interacting Drug | Level | Source |
|------|------|------|
| Famotidine | Moderate | ddinter |
| Ranitidine | Moderate | ddinter |
| Rabeprazole | Moderate | ddinter |
| Aprepitant | Moderate | ddinter |
| Cimetidine | Moderate | ddinter |
| Clarithromycin | Moderate | ddinter |
| Dexlansoprazole | Moderate | ddinter |
| Omeprazole | Moderate | ddinter |
| Dexamethasone | Moderate | ddinter |
| Naltrexone | Moderate | ddinter |
| Lansoprazole | Moderate | ddinter |
| Miconazole | Moderate | ddinter |
| Nizatidine | Moderate | ddinter |
| Pantoprazole | Moderate | ddinter |
| Esomeprazole | Moderate | ddinter |
| Clotrimazole | Moderate | ddinter |
| Ranitidine (bismuth citrate) | Moderate | ddinter |
| Troglitazone | Moderate | ddinter |
| Calcitriol | Unknown | ddinter |
| Glimepiride | Unknown | ddinter |

Key warnings and contraindications are not available in this evidence pack (data gap DG001, Blocking severity) — this must be sourced from the TFDA/manufacturer package insert before any safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (gingival fibromatosis) has no clinical trial or literature support and no plausible mechanistic link to gefitinib's known EGFR-TKI activity — it is a model-score-only (L5) hypothesis. Gefitinib is also not currently marketed in Taiwan, and the evidence pack lacks the drug-level safety data (MOA, key warnings, contraindications) needed to even begin a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Verified mechanism of action data from DrugBank (DG002)
- If pursuing repurposing further, prioritize re-evaluating rank 5 (lung hilum carcinoma) and rank 8 (pulmonary sulcus neoplasm) instead — both reached decision stage S1 with gefitinib-specific literature, though the pack's own analysis flags them as anatomical extensions of the existing NSCLC indication rather than novel repurposing candidates
- Independent mechanistic plausibility review for gingival fibromatosis before any further evidence collection is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

