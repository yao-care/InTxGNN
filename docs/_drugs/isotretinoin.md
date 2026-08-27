---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# Isotretinoin: From Severe Acne to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is a synthetic retinoid (vitamin A derivative) primarily used for the treatment of severe nodular acne and related dermatological conditions.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, however **0 clinical trials** and **0 publications** currently support this direction — this is a purely model-driven prediction without any clinical validation identified to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe nodular acne (and related dermatological conditions) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Isotretinoin is a synthetic retinoid that modulates gene expression by binding to nuclear retinoic acid receptors (RARα, RARβ, RARγ) and retinoid X receptors (RXRs). Its efficacy in severe acne has been well established through decades of clinical use due to its ability to reduce sebaceous gland size, normalise keratinisation, and suppress inflammatory signalling. It is also used in neuroblastoma maintenance therapy for its capacity to induce cellular differentiation.

Malignant renovascular hypertension is a life-threatening condition driven by renal artery stenosis, leading to pathological activation of the renin-angiotensin-aldosterone system (RAAS) and severe end-organ damage. Exploratory research suggests that retinoic acid signalling can influence vascular smooth muscle cell phenotype, renal tubular function, and inflammatory cascades — biological pathways that are relevant to renovascular disease. Some preclinical data have also indicated that retinoids may modulate renin expression and RAAS activity, providing a theoretical mechanistic bridge.

However, the knowledge-graph topology that drives TxGNN's high score does not guarantee a direct therapeutic relationship. No published clinical or translational evidence specifically linking Isotretinoin to malignant renovascular hypertension was identified during evidence collection. This prediction should be treated as a hypothesis-generating signal requiring independent experimental validation rather than a clinically supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** (98 total interactions identified; key interactions listed below):

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|--------------------|
| Doxycycline | **Major** | Combined use significantly raises risk of intracranial hypertension (pseudotumour cerebri); concurrent use is contraindicated in standard practice |
| Minocycline | **Major** | Same mechanism as Doxycycline; concurrent tetracycline-class antibiotics should be avoided |
| Tetracycline | **Major** | Combined use markedly increases intracranial hypertension risk |
| Vitamin A | **Major** | Additive retinoid toxicity; may precipitate hypervitaminosis A syndrome |
| Betamethasone | Moderate | Corticosteroid interaction; monitor for additive adverse effects |
| Budesonide | Moderate | Corticosteroid interaction; monitor closely |
| Dexamethasone | Moderate | Corticosteroid interaction; monitor closely |
| Hydrocortisone | Moderate | Corticosteroid interaction |
| Prednisolone | Moderate | Corticosteroid interaction |
| Prednisone | Moderate | Corticosteroid interaction |
| Triamcinolone | Moderate | Corticosteroid interaction |
| Warfarin | Moderate | May alter anticoagulation effect; INR monitoring recommended |
| Dicoumarol | Moderate | Anticoagulant effect may be altered |
| Ethanol | Moderate | Increased hepatotoxicity risk; alcohol should be minimised |
| Naltrexone | Moderate | Interaction reported; monitor for adverse effects |

> Full warning and contraindication data are not available in this evidence pack. Please refer to the official package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently no clinical trial or published literature evidence supporting the use of Isotretinoin in malignant renovascular hypertension. The TxGNN score of 99.01% reflects a strong knowledge-graph signal, but with zero supporting studies, the evidence level is L5 (model prediction only). Advancing this candidate without any experimental validation would not be justified.

**To proceed, the following is needed:**

- **Mechanistic validation**: Confirm whether retinoic acid receptor signalling meaningfully modulates RAAS activity or vascular remodelling in renovascular hypertension models (preclinical studies required)
- **Preclinical evidence**: Animal model studies (e.g., 2-kidney 1-clip rat model) to test Isotretinoin's antihypertensive effect before any clinical step
- **Safety data completion**: Retrieve TFDA/CDSCO package insert to obtain key warnings, contraindications, and teratogenicity classification (currently a blocking data gap — DG001)
- **MOA data**: Query DrugBank API for full mechanism of action details (DG002) to strengthen the repurposing rationale
- **Literature sweep**: Conduct a broader PubMed search on retinoids + hypertension + renal disease to identify any indirect supporting evidence
- **India regulatory pathway**: Since Isotretinoin is not currently marketed in India, a de novo regulatory filing strategy would be required if the candidate advances
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

