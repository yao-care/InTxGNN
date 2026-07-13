---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor with well-established global use for hypertension, heart failure, and post-MI left ventricular dysfunction, though it currently holds no approved registration in India.
The TxGNN model's top-ranked prediction is that it may be effective for **Posterolateral Myocardial Infarction**, a specific anatomical subtype of acute MI; there are currently **0 clinical trials** and **0 publications** specifically supporting this direction.
Notably, among the 10 predicted indications in this pack, **Chronic Pulmonary Heart Disease** (cor pulmonale, rank 9) carries substantially stronger evidence (L3), with two direct clinical studies documenting Lisinopril's efficacy, and may represent the higher-priority repurposing candidate for follow-on investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration; globally established for hypertension, chronic heart failure, and post-MI left ventricular dysfunction |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only — no indication-specific studies identified) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved for Lisinopril in this evidence pack. Based on well-established pharmacology, Lisinopril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II (Ang II), thereby suppressing the renin-angiotensin-aldosterone system (RAAS). This results in vasodilation, reduced aldosterone secretion, lower blood pressure, and decreased cardiac afterload and preload. Its efficacy across hypertension, heart failure, and post-MI management is supported by landmark trials (GISSI-3, CONSENSUS, ATLAS).

Posterolateral myocardial infarction is an anatomical subtype of acute MI involving the posterior and lateral walls of the left ventricle, typically resulting from occlusion of the circumflex artery or a dominant right coronary artery. Following any MI, RAAS activation is a key driver of adverse cardiac remodeling — progressive ventricular dilation, wall thinning, and decline in ejection fraction. ACE inhibitors are mechanistically well-suited to interrupt this remodeling cascade, and their benefit in the broader post-MI population is unequivocal.

The TxGNN prediction is therefore mechanistically coherent: the same RAAS-suppression mechanism that reduces ventricular remodeling after anterior or inferior MI should apply to posterolateral MI as an anatomical subtype. The L5 evidence level reflects not mechanistic implausibility, but the absence of any subtype-specific clinical trial or publication in the current data retrieval — an evidence gap that is common for rare anatomical MI classifications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Lisinopril in posterolateral myocardial infarction.

---

## Literature Evidence

Currently no related literature available specifically for Lisinopril in posterolateral myocardial infarction.

---

## Safety Considerations

**Drug Interactions**: Lisinopril has 308 documented interactions. The following are the most clinically significant:

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|-----------------|
| Major | Potassium citrate | Risk of severe hyperkalemia; ACEi reduces aldosterone → potassium retention |
| Major | Potassium bicarbonate | Same mechanism as above; concurrent use requires close electrolyte monitoring |
| Moderate | Hydrocortisone / Dexamethasone / Betamethasone / Budesonide / Triamcinolone | Corticosteroids may antagonise the antihypertensive effect via sodium retention |
| Moderate | Acetylsalicylic acid | NSAIDs/aspirin may attenuate ACEi efficacy and increase renal risk, especially at higher doses |
| Moderate | Metformin | Renal impairment from ACEi may elevate metformin levels; monitor renal function |
| Moderate | Canagliflozin / Dapagliflozin / Empagliflozin | Additive blood pressure–lowering and diuretic effects; monitor for hypotension and acute kidney injury |
| Moderate | Alogliptin / Saxagliptin / Chlorpropamide | Possible enhanced hypoglycaemic effect and angioedema risk with DPP-4 inhibitors |
| Moderate | Morphine | Additive hypotensive effect in acute settings |
| Moderate | Bupropion | May lower seizure threshold in combination; monitor neurological status |
| Moderate | Dronabinol | Additive hypotensive effect |

Please refer to the package insert for complete warnings and contraindications, as these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature specifically address Lisinopril in posterolateral myocardial infarction. Although the underlying RAAS-inhibition mechanism is biologically sound, this prediction remains an inference from broader post-MI evidence and cannot be elevated beyond L5 without subtype-specific data.

**To proceed, the following is needed:**
- Retrieve full Lisinopril mechanism of action and toxicity profile from DrugBank (DrugBank ID: DB00722) to complete the pharmacological rationale
- Obtain India-specific package insert (if available through CDSCO or manufacturer labeling) for warnings and contraindications
- Conduct a broadened literature search covering posterior MI, inferolateral MI, and circumflex territory MI alongside ACE inhibitor therapy, to determine whether any publications address overlapping anatomical subtypes
- **Priority reallocation recommended**: Consider redirecting the primary evaluation to **Chronic Pulmonary Heart Disease (cor pulmonale)** — ranked 9th by TxGNN score but carrying **L3 evidence** with two direct clinical studies of Lisinopril in cor pulmonale (PMID [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) — prospective study; PMID [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) — clinical study), which together represent a substantially more actionable repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

