---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 4
---

# Labetalol
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha1 and non-selective beta adrenergic blocker widely used internationally for hypertension management and hypertensive emergencies.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
with **0 clinical trials** and **2 case reports** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (not registered in India; based on known international use) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Labetalol is a distinctive antihypertensive agent that uniquely combines alpha1 and non-selective beta adrenergic receptor blockade in a single molecule. The beta-blocking component reduces cardiac output and suppresses renin release from the kidneys, while alpha1 blockade lowers peripheral vascular resistance. This dual mechanism allows for rapid, titratable blood pressure reduction, which is why labetalol has historically been favoured in hypertensive emergencies.

Malignant renovascular hypertension is a severe hypertensive crisis driven primarily by renal artery stenosis (RAS) activating the renin-angiotensin-aldosterone (RAA) system. Labetalol's beta-blocking component theoretically targets a key upstream driver of this cascade by suppressing renin release. Two historical case reports — from 1981 and 2004 — describe clinically meaningful blood pressure control with labetalol in patients presenting with malignant hypertension in a renovascular context, lending limited but real-world plausibility to the prediction.

However, an important mechanistic caveat must be acknowledged: in bilateral renal artery stenosis, inhibiting the compensatory RAA system with beta-blockers may paradoxically worsen renal perfusion and accelerate acute kidney injury. The safe boundaries of labetalol use in this specific renovascular subtype have not been defined in any controlled study. The TxGNN prediction likely reflects shared graph topology between labetalol and hypertensive disease nodes, rather than a validated biological link specific to the renovascular subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case Report | Medical Journal of Australia | 20-year-old with hallucinogen-induced malignant hypertension and renal arteritis; labetalol combined with minoxidil achieved impressive initial blood pressure control; renal angiography confirmed vasculitic changes |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case Report | BMC Nephrology | 18-month-old child with hyponatremic hypertensive syndrome (HHS) presenting as malignant hypertension with renovascular involvement; documents the clinical setting where labetalol is considered in paediatric renovascular crisis |

---

## India Market Information

Labetalol is currently **not registered** in India. No product authorizations are on record.

---

## Safety Considerations

**Drug Interactions (240 total interactions identified; key interactions listed below):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Epinephrine | **Major** | Risk of paradoxical severe hypertension followed by bradycardia; alpha-blockade unmasks epinephrine's alpha-agonist activity |
| Dolasetron | **Major** | Potential additive cardiovascular and QT-prolonging effects |
| Hydrocortisone | Moderate | Corticosteroids may attenuate the antihypertensive effect |
| Dexamethasone | Moderate | Same mechanism as hydrocortisone |
| Betamethasone | Moderate | Same mechanism as hydrocortisone |
| Budesonide | Moderate | Same mechanism as hydrocortisone |
| Triamcinolone | Moderate | Same mechanism as hydrocortisone |
| Canagliflozin | Moderate | Beta-blockade may mask hypoglycaemia symptoms in diabetic patients |
| Dapagliflozin | Moderate | Same as canagliflozin |
| Chlorpropamide | Moderate | Beta-blockade may mask and prolong hypoglycaemia |
| Cimetidine | Moderate | May increase labetalol plasma levels by reducing hepatic first-pass metabolism |
| Morphine | Moderate | Additive hypotensive effect; monitor haemodynamics closely |
| Atropine | Moderate | May counteract labetalol-induced bradycardia |
| Dicyclomine | Moderate | Anticholinergic agents may reduce labetalol efficacy |
| Hyoscyamine | Moderate | Same as dicyclomine |
| Methscopolamine | Moderate | Same as dicyclomine |
| Calcium Phosphate | Moderate | Calcium salts may reduce antihypertensive effect |
| Calcium acetate | Moderate | Same as calcium phosphate |
| Acetylsalicylic acid | Minor | May slightly reduce antihypertensive effect via prostaglandin inhibition |
| Magnesium oxide | Minor | Antacids may alter labetalol absorption |

> The full interaction database lists 240 interactions. Prescribers should conduct a comprehensive medication review before use. Please also refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to two historical case reports with no registered clinical trials, placing this candidate at L4. While there is theoretical mechanistic plausibility through renin suppression, an unresolved safety concern in bilateral renal artery stenosis — where beta-blockade may worsen renal function — represents a potentially blocking issue. The absence of India market registration adds a further regulatory barrier to any near-term development.

**To proceed, the following is needed:**
- Retrieve and review the full MOA data from DrugBank (DG002) to confirm the alpha1/beta selectivity ratio and its relevance to the renovascular subtype
- Retrieve CDSCO/TFDA package insert or equivalent labelling (DG001) to formally assess contraindications, particularly renal impairment and heart block
- Clarify the intended patient population: unilateral vs. bilateral renal artery stenosis, as the safety profile diverges significantly between these two groups
- Conduct a structured pharmacovigilance review of published real-world beta-blocker use in renovascular hypertension
- Commission a focused narrative review or case series analysis before advancing to any prospective observational study
- Establish renal function monitoring criteria and haemodynamic safety endpoints as prerequisites for any clinical investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

