---
layout: default
title: Metolazone
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 5
---

# Metolazone
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

# Metolazone: From Hypertension and Edema to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic used for treating hypertension and fluid overload, with particular utility in patients with renal impairment where conventional thiazides lose efficacy.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** with a prediction score of **99.84%**,
however, **no clinical trials or direct supporting literature** have been identified for this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and edema (no India registration record found) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (mechanistic reasoning; no direct clinical evidence identified) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Metolazone is a thiazide-like diuretic that inhibits the sodium-chloride cotransporter (NCC/SLC12A3) in the distal convoluted tubule, reducing sodium and water reabsorption to lower blood volume and blood pressure. A key clinical distinguishing feature is that Metolazone also acts on the proximal tubule, retaining diuretic efficacy even when GFR falls below 30 mL/min — making it particularly valuable in patients with chronic kidney disease and diuretic resistance where standard thiazides become ineffective.

Malignant renovascular hypertension is a severe hypertensive emergency driven by critical renal artery stenosis, which triggers pathological overactivation of the renin-angiotensin-aldosterone system (RAAS). The TxGNN model likely draws a connection through Metolazone's antihypertensive and volume-reducing properties. However, this is mechanistically problematic: in RAAS-driven hypertension, diuretic-induced volume depletion can paradoxically further stimulate renin release, potentially worsening renal ischemia. Standard management centers on revascularization (angioplasty or stenting) and RAAS blockade (ACEI/ARB, with significant caution in bilateral stenosis), while the malignant phase as an acute emergency requires carefully titrated intravenous antihypertensives rather than oral diuretics.

The TxGNN prediction score is high (99.84%, ranked #3,485), but clinical plausibility for this specific indication remains limited. The prediction appears to reflect shared knowledge graph associations between Metolazone's antihypertensive mechanism and renal hypertensive conditions broadly, rather than a disease-specific biological signal. This pattern is further supported by the observation that four of the top five predictions are all related to hypertension or vascular conditions, suggesting topology-driven scoring rather than indication-specific mechanistic differentiation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Metolazone currently has no products registered in India. The CDSCO market status is **Not Marketed** with zero license records on file.

---

## Safety Considerations

**Drug Interactions — 249 total interactions identified (DDInter database):**

Key interactions of clinical note:

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|-------------------|--------------------|
| Dexamethasone | Moderate | Corticosteroids antagonize diuretic effect; additive potassium loss |
| Hydrocortisone | Moderate | As above |
| Betamethasone | Moderate | As above |
| Beclomethasone dipropionate | Moderate | As above |
| Triamcinolone | Moderate | As above |
| Amphotericin B | Moderate | Additive risk of hypokalemia |
| Amphotericin B (lipid complex) | Moderate | Additive risk of hypokalemia |
| Morphine | Moderate | Enhanced hypotensive effect |
| Bupropion | Moderate | Electrolyte disturbance may lower seizure threshold |
| Acarbose | Moderate | Thiazides may impair glycemic control |
| Alogliptin | Moderate | Thiazides may reduce hypoglycemic drug efficacy |
| Albiglutide | Moderate | Thiazides may reduce hypoglycemic drug efficacy |
| Cholecalciferol | Moderate | Risk of hypercalcemia with thiazide co-administration |
| Calcium Phosphate | Moderate | Thiazide-related calcium homeostasis disruption |
| Bisacodyl | Moderate | Combined gastrointestinal potassium loss |
| Omeprazole | Moderate | Possible electrolyte interaction |
| Rabeprazole | Moderate | Possible electrolyte interaction |
| Doxycycline | Minor | — |
| Hyoscyamine | Minor | — |
| Atropine | Minor | — |

Please refer to the official package insert for complete warnings, contraindications, and safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No direct clinical trial or literature evidence supports Metolazone for malignant renovascular hypertension, and mechanistic analysis suggests that RAAS activation triggered by diuretic-induced volume depletion may be counterproductive in this condition — making the TxGNN prediction biologically plausible in concept but clinically problematic in practice.

**To proceed, the following is needed:**
- Official package insert retrieval from CDSCO/FDA sources to fill MOA, contraindication, and key warning data gaps
- Targeted literature search specifically for Metolazone in renovascular or malignant hypertension clinical settings
- Knowledge graph topology audit to determine whether TxGNN's score reflects a unique biological signal or shared antihypertensive/renal node proximity
- Review of the Rank 2 prediction (Malignant Hypertensive Renal Disease), which shares the same score and may carry a more defensible mechanistic rationale given Metolazone's preserved efficacy in low GFR settings
- If the program is to move forward, a formal preclinical study design would be needed before any clinical translation consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

