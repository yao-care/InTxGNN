---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective beta-1 adrenergic blocker, established in clinical use for hypertension, angina pectoris, and cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** (rank #1, score 99.87%),
with **no clinical trials** and **no literature** currently available specifically supporting this indication — yielding an evidence level of L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Angina Pectoris, Cardiac Arrhythmias |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Atenolol is a selective β1-adrenergic receptor blocker. Its core actions include reducing heart rate (negative chronotropy) and contractility (negative inotropy), thereby lowering myocardial oxygen demand. It also suppresses renin secretion from juxtaglomerular cells and exerts anti-arrhythmic effects through Class II antiarrhythmic properties.

Posterolateral myocardial infarction typically involves occlusion of the circumflex artery (LCx), affecting the posterolateral wall of the left ventricle. The mechanistic link is theoretically sound: selective β1-blockade during and after any MI subtype reduces myocardial oxygen consumption, blunts the post-infarction catecholamine surge, limits infarct zone expansion, and prevents malignant ventricular arrhythmias. These mechanisms apply equally to the posterolateral territory as to anterior or inferior MI.

Importantly, beta-blockers as a class are already guideline-recommended (Class I) for all post-MI patients without contraindications. The TxGNN prediction likely reflects these well-established pharmacological properties rather than a genuinely novel repurposing opportunity. The key evidence gap is the absence of posterolateral MI-specific clinical data for atenolol as a distinct indication, separate from broad post-MI beta-blocker therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Atenolol is currently not registered or marketed in India. No CDSCO authorization records are on file for this compound.

---

## Safety Considerations

- **Drug Interactions**: 293 interactions documented in total (DDInter database). Key interactions of clinical relevance are listed below:

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Epinephrine | Moderate | Risk of paradoxical hypertension followed by reflex bradycardia; caution in anaphylaxis management |
| Atropine | Moderate | Anticholinergic agents may antagonize atenolol's bradycardic effect |
| Morphine | Moderate | Additive hypotensive effects; monitor blood pressure closely |
| Hydrocortisone | Moderate | Corticosteroids may blunt antihypertensive efficacy |
| Triamcinolone | Moderate | Same mechanism as hydrocortisone |
| Betamethasone | Moderate | Same mechanism as hydrocortisone |
| Budesonide | Moderate | Same mechanism as inhaled/systemic corticosteroids |
| Bupropion | Moderate | May lower seizure threshold and affect cardiovascular response |
| Hyoscyamine | Moderate | Anticholinergic antagonism of bradycardic effect |
| Acetohexamide | Moderate | Beta-blockers may mask hypoglycaemia symptoms; caution in diabetic patients |
| Calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate) | Moderate | Calcium may interfere with beta-blocker bioavailability or cardiac effects |
| Acetylsalicylic acid | Minor | Minimal clinical interaction |
| Aluminum hydroxide | Minor | May reduce atenolol gastrointestinal absorption; separate dosing recommended |

> **Note:** Full warnings and contraindications (e.g., complete heart block, cardiogenic shock, uncontrolled heart failure, severe bradycardia) are not available in this Evidence Pack. Please refer to the official package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.87%) and the β1-blockade mechanism is theoretically applicable to all MI subtypes including posterolateral infarction, the complete absence of posterolateral MI-specific clinical trials or published literature leaves this at evidence level L5 — insufficient to advance beyond hypothesis generation.

**To proceed, the following is needed:**
- Retrieve mechanism of action (MOA) data from DrugBank (currently unavailable)
- Obtain official package insert to document warnings and contraindications (currently a blocking data gap)
- Conduct a subgroup analysis of existing general post-MI beta-blocker trials (e.g., REDUCE-SWEDEHEART, NCT03278509) to extract any posterolateral MI-specific outcomes
- Register a pilot clinical study or identify existing registry data where MI territory can be cross-referenced with atenolol use
- Evaluate whether the existing broad-MI guideline recommendation is sufficient to cover this subtype, removing the need for a separate repurposing filing

> **Additional Finding:** Among the 9 predicted indications in this multi-indication pack, **Chronic Pulmonary Heart Disease** (rank #9, score 99.04%) carries the strongest evidence base — 1 Phase 4 clinical trial (NCT03278509) and 15 supporting publications, with a direct 1978 study of atenolol in obstructive pulmonary patients (PMID 31524). Its evidence level is L3 with a decision of **Proceed with Guardrails**, and may warrant a dedicated evaluation report.

---

*This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

