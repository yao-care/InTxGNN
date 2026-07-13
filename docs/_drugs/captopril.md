---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is a first-generation ACE inhibitor with proven efficacy in treating systemic hypertension and heart failure.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
with **0 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Heart Failure, Post-MI left ventricular dysfunction |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism of action data was not retrieved for this report. However, based on its established pharmacological profile, Captopril is the prototypical angiotensin-converting enzyme (ACE) inhibitor — it competitively inhibits ACE, blocking the conversion of angiotensin I (Ang I) to angiotensin II (Ang II), and also prevents bradykinin degradation. The net result is vasodilation, reduced aldosterone secretion, and lower systemic vascular resistance.

The mechanistic connection to malignant renovascular hypertension is particularly direct. The core pathophysiology of this condition is: renal artery stenosis → renal ischemia → massive renin release → elevated Ang II → malignant hypertensive cycle. Captopril's ACE inhibition cuts this cascade at its central enzymatic step, reducing renin-dependent vascular resistance more effectively than agents acting downstream. The predictive model's confidence is further reinforced by the fact that **captopril renography** (the captopril-augmented nuclear scintigram) is already an established diagnostic standard for identifying renovascular hypertension — demonstrating that the drug's mechanism is tightly coupled to this disease entity's pathophysiology.

This is therefore not a distant extrapolation: the same renin-angiotensin axis that Captopril was designed to block is the primary driver of malignant renovascular hypertension. The key clinical uncertainty is whether ACE inhibition is safe in the setting of bilateral renal artery stenosis or stenosis to a solitary functioning kidney, where abrupt Ang II reduction can precipitate acute renal failure — a risk that must be built into any clinical protocol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical study | Clinical Science | Captopril induced plasma renin activity >14 ng/h/mL in 43 of 44 patients with untreated renovascular hypertension; absent in normal-renin essential HTN — establishing the diagnostic utility of captopril challenge |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Cohort/Case series | Pediatric Nephrology | 27 NF1 patients followed 2–10 years; captopril test used alongside Doppler and angiography to screen for renal artery stenosis and secondary hypertension |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Clinical study | Japanese Heart Journal | Serial measurement of PRA, Ang I, Ang II, and catecholamines in 2K2C Goldblatt hypertensive dogs during benign-to-malignant phase transition; delineates neurohormonal profile of malignant renovascular HTN |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical series | Bulletin of the All-Union Cardiology Scientific Centre | Direct clinical use of captopril in patients with stable and malignant-course arterial hypertension |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinology & Metabolism Clinics of North America | In renin-secreting (JG cell) tumors, captopril drops blood pressure; reactive renin rise under captopril used to characterise secretory autonomy |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case report + Review | Clinical Nephrology | Two NF cases with renovascular HTN; captopril challenge raised PRA from 2.8 to 12.6 ng/mL/h in first patient, confirming RAAS dependence |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case report | Klinische Wochenschrift | NF patient with aortic coarctation and bilateral RAS refused surgery; captopril as sole ACE inhibitor provided satisfactory long-term blood pressure control |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Renovascular hypertension clinical concepts; ACE inhibitors highlighted as mechanistically rational but cautioned in bilateral RAS due to acute kidney injury risk |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case report | Clinical Nuclear Medicine | Malignant hypertension patient with positive captopril renal scintigraphy but intact renal arteries on angiography; illustrates false-positive scenarios and interpretation caveats |
| [1436350](https://pubmed.ncbi.nlm.nih.gov/1436350/) | 1992 | Case report | Nephron | Von Hippel-Lindau patient with pheochromocytoma, extreme hyperreninaemia, and severe HTN; captopril further enhanced renin secretion while improving blood pressure, confirming RAAS-driven mechanism |

---

## India Market Information

Captopril currently holds **no registered licenses** in India under this dataset. The drug is not marketed as a locally approved product in this registry.

---

## Safety Considerations

**Drug Interactions (245 total interactions on record; key moderate interactions listed):**

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|-------------------|-------------------|
| Hydrocortisone | Moderate | Corticosteroids may attenuate antihypertensive effect |
| Dexamethasone | Moderate | Same class concern as hydrocortisone |
| Betamethasone / Triamcinolone / Budesonide | Moderate | Corticosteroid class — reduced ACE inhibitor efficacy |
| Metformin | Moderate | ACE inhibitors may enhance hypoglycaemic effect |
| Alogliptin / Exenatide | Moderate | Additive hypoglycaemia risk with antidiabetics |
| Canagliflozin / Dapagliflozin / Empagliflozin / Ertugliflozin | Moderate | SGLT2 inhibitor combination: monitor renal function and potassium |
| Acetohexamide / Chlorpropamide | Moderate | Sulfonylurea class: enhanced glucose-lowering |
| Acetylsalicylic acid | Moderate | High-dose aspirin may reduce antihypertensive efficacy of captopril |
| Morphine | Moderate | Additive hypotensive effect |
| Bupropion | Moderate | Potential additive hypotensive interaction |
| Dronabinol | Moderate | Additive hypotension risk |
| Aluminum hydroxide / Calcium carbonate | Minor | Antacids may reduce captopril absorption; separate administration |

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between captopril's ACE inhibition and the renin-driven pathophysiology of malignant renovascular hypertension is among the strongest possible for a repurposing candidate — the drug's diagnostic use in captopril renography already confirms deep mechanistic coupling. Twenty publications provide observational and case-level evidence at L3, which is sufficient to justify a structured clinical evaluation, but the absence of any registered clinical trial in this specific indication and the known risk of acute kidney injury in bilateral RAS require careful patient selection and monitoring guardrails.

**To proceed, the following is needed:**
- Retrieve and review full DrugBank MOA data and pharmacokinetic profile to confirm no barriers to renal-context use
- Retrieve TFDA/package insert data to document contraindications (bilateral RAS, pregnancy, hyperkalaemia) as part of patient eligibility criteria
- Design a prospective observational registry or pilot study specifically in unilateral RAS patients to generate controlled evidence (current gap: zero registered trials)
- Establish mandatory renal function and potassium monitoring protocol at baseline, 1 week, 1 month, and quarterly thereafter
- Define clear stopping rules: serum creatinine rise >30% or potassium >5.5 mEq/L triggers immediate reassessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

