---
layout: default
title: Safinamide
parent: 僅模型預測 (L5)
nav_order: 753
evidence_level: L5
indication_count: 3
---

# Safinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Safinamide: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Safinamide is a MAO-B inhibitor publicly known for use as adjunctive therapy in Parkinson's disease, though detailed original-indication and mechanism-of-action data are missing from this dataset.
> The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**,
> but this prediction is currently supported by **no clinical trials** and **no published literature** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (publicly known: Parkinson's disease, MAO-B inhibitor adjunctive therapy) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on publicly known pharmacology, Safinamide is a reversible MAO-B inhibitor that also blocks voltage-dependent sodium/calcium channels and inhibits glutamate release; it is approved as adjunctive therapy for Parkinson's disease.

Rasmussen subacute encephalitis is a chronic, focal, immune/excitotoxicity-mediated encephalitis. In theory, glutamate-release inhibition could offer some neuroprotective effect in this setting, which may explain the high TxGNN association score (0.996). However, this link is a mechanistic extrapolation only — there is no direct preclinical or clinical evidence connecting Safinamide to this indication, and the connection rests entirely on the knowledge-graph prediction rather than experimental data.

Two other candidates were predicted with similar characteristics: **Myelitis** (score 0.995) — a plausible but unproven extension of the same glutamate-inhibition hypothesis — and **PLA2G6-associated neurodegeneration** (score 0.992), which has somewhat stronger mechanistic plausibility due to shared nigral degeneration and movement-disorder pathology with Parkinson's disease. All three remain at the model-prediction-only stage (S0).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Safinamide is currently **not marketed** in India, with no registered authorizations on file (0 licenses). No product-level registration data is available for review.

---

## Safety Considerations

**Drug Interactions**: A total of 110 documented interactions were identified. Notable examples include:

| Interacting Drug | Severity | Source |
|---|---|---|
| Bupropion | Major | ddinter |
| Isometheptene | Moderate | ddinter |
| Chlorpropamide | Moderate | ddinter |
| Diethylpropion | Moderate | ddinter |
| Empagliflozin | Moderate | ddinter |
| Phentermine | Moderate | ddinter |
| Glimepiride | Moderate | ddinter |
| Metoclopramide | Moderate | ddinter |
| Repaglinide | Moderate | ddinter |
| Rosuvastatin | Moderate | ddinter |

*(Full list contains 110 entries, predominantly insulin/insulin-analogue and sulfonylurea interactions consistent with MAO-B inhibitor–related hypoglycemic risk; Bupropion is the only Major-severity interaction identified.)*

Key warnings and contraindications are not available in this dataset — please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a TxGNN model score (L5, S0 stage), with zero clinical trials and zero published literature. Combined with the absence of original indication/MOA data and no current India market presence, there is insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank or primary literature — currently a High-severity data gap
- Preclinical or case-level evidence directly linking Safinamide to Rasmussen encephalitis, myelitis, or PLA2G6-associated neurodegeneration
- Assessment of route/formulation compatibility for the new indication once evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

