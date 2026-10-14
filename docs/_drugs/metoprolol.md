---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol: From Hypertension and Myocardial Infarction to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker, originally used to treat hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials or publications** currently support this specific prediction.
The prediction is largely an extension of the original hypertension indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, acute coronary syndrome, myocardial infarction (approved indication text is not listed in the Indian licence records) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, metoprolol is a beta-1 selective adrenergic blocker. It lowers heart rate and blood pressure and reduces renin release.

Malignant hypertensive renal disease is kidney injury driven by severely elevated blood pressure. Because metoprolol is already an established antihypertensive, a link through blood pressure control and suppression of the renin-angiotensin system is plausible.

This is mainly an extension of the existing hypertension indication, not a new mechanism. No trials or publications were found for this specific condition, so the high score is a computational result only.

**Other predictions in the top 10 (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Malignant renovascular hypertension | 99.91% | L5 | Only one linked paper, which is a diagnostic study unrelated to metoprolol efficacy |
| 3 | Pulmonary hypertension, unclear multifactorial mechanism | 99.91% | L5 | Beta-blockers are used cautiously because of right ventricular concerns |
| 4 | Pulmonary hypertension due to lung disease/hypoxia | 99.91% | L4 | Literature is heterogeneous and mostly off-target |
| 6–8 | Posterolateral, posteroinferior and septal myocardial infarction | 99.8–99.84% | L4–L5 | Subtypes of an already approved use |
| 9 | Chronic pulmonary heart disease | 99.40% | L3 | The only candidate with trials; the evidence is mainly about safety in COPD |
| 10 | Trichotillomania | 99.05% | L5 | No data |

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (malignant hypertensive renal disease). The only trials in the data relate to the rank 9 prediction, chronic pulmonary heart disease, and are shown below for reference:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol in heart failure with reduced ejection fraction and COPD; compares doses and looks at deaths and re-hospitalisation |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | BLOCK-COPD: metoprolol vs placebo for preventing COPD exacerbations; stopped early |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | Carvedilol vs metoprolol respiratory assessment in heart failure; no data |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | Terminated | 14 | Post-COVID exertional dyspnoea and tachycardia; only tangentially related |

---

## Literature Evidence

No literature was found that directly supports metoprolol in malignant hypertensive renal disease. The publications below relate to other predicted indications (rank 6–9) and are the most relevant available:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | Bisoprolol in COPD at high exacerbation risk; notes that metoprolol did not reduce exacerbations and increased hospitalised exacerbations |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised crossover trial | J Am Coll Cardiol | Switching between beta1-selective and nonselective beta-blockers in heart failure with COPD |
| [8737105](https://pubmed.ncbi.nlm.nih.gov/8737105/) | 1996 | Clinical study (RCT) | Eur Heart J | MEXIS: metoprolol vs xamoterol on left ventricular function in heart failure after myocardial infarction |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in geriatric patients with heart failure, COPD, diabetes and renal failure |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Carvedilol, bisoprolol and metoprolol in coexistent heart failure and COPD (Taiwan database) |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | Eur J Heart Fail | Danish cohort of beta-blocker use in heart failure with COPD |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Review | Expert Rev Respir Med | Practical recommendations for beta-blockers in COPD |
| [6401230](https://pubmed.ncbi.nlm.nih.gov/6401230/) | 1983 | Small clinical study | Circulation | Metoprolol, nitroglycerin and nifedipine effects on regional left ventricular function |
| [3568727](https://pubmed.ncbi.nlm.nih.gov/3568727/) | 1987 | Clinical study | Crit Care Med | Metoprolol in multifocal atrial tachycardia in 11 patients with serious lung disease |

---

## India Market Information

Metoprolol is marketed in India with 20 valid single-ingredient registrations. The records do not list approved indication text. The main authorisations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73288 | Embeta XR 75mg Tablet (Intas Pharmaceuticals) | Extended-release tablet | Not listed |
| 6427 | Angibloc 50 Tablet PR (Alkem Laboratories) | Prolonged-release tablet | Not listed |
| 139154 | Metored 50mg Tablet XL (Morepen Laboratories) | Extended-release tablet | Not listed |
| 140719 | Metosan XR 25 Tablet (Sanofi India) | Extended-release tablet | Not listed |
| 48318 | Clovet M 50mg/6.25mg Tablet (Ajanta Pharma) | Tablet | Not listed |

All formulations are oral.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** anxiety and neurotic disorders, pancreatitis, liver disease, diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus, psoriasis, gout, hypotension, myasthenia gravis, pheochromocytoma, and several metabolic conditions (potassium deficiency, hypercalcaemia, hyperparathyroidism). These come from graph relationships and must be checked against the official package insert.
- **Drug interactions:** 337 interactions were identified. Examples at moderate level include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, glycopyrronium), bupropion, morphine, cimetidine, canagliflozin, dapagliflozin and chlorpropamide. Acetylsalicylic acid and magnesium oxide interact at minor level.
- **Respiratory safety:** In the BLOCK-COPD trial, metoprolol did not reduce COPD exacerbations and was associated with more exacerbations requiring hospitalisation. Caution is warranted in lung disease.
- Package insert warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease has a very high model score (99.91%), but there are no clinical trials or publications for it, so the evidence level is L5. It is also an extension of metoprolol's existing hypertension use rather than a distinct new indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Targeted literature on beta-blockers in malignant hypertension with renal involvement, including renal safety
- Clarification of whether this prediction represents a genuinely new use or a subtype of the approved hypertension indication
- If pursuing the cardiopulmonary direction (chronic pulmonary heart disease), a dedicated safety assessment given the BLOCK-COPD findings, and follow-up of NCT06825728
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

