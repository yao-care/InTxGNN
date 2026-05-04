---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Amiloride: From Hypertension and Edema to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic historically used as adjunctive therapy for hypertension, heart failure-related edema, and hyperaldosteronism states, acting by directly blocking epithelial sodium channels (ENaC) in the renal collecting duct. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** with a confidence score of 99.82%, though currently only **1 publication** — a general review of mineralocorticoid hypertension — provides indirect mechanistic background, with no dedicated clinical trials available. Evidence strength is at a preclinical/mechanistic level (L4), warranting foundational research before any clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and edema (potassium-sparing diuretic) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiloride is a well-established potassium-sparing diuretic that works by directly blocking the epithelial sodium channel (ENaC) in the principal cells of the renal collecting duct. Unlike aldosterone antagonists (e.g., spironolactone, eplerenone) which work at the mineralocorticoid receptor, amiloride acts downstream at the channel level — meaning it can suppress aldosterone-driven sodium reabsorption regardless of aldosterone receptor status. Detailed MOA data from DrugBank was not retrieved for this report, but the drug's ENaC-blocking mechanism is well-established in the pharmacological literature.

Malignant renovascular hypertension is mechanistically driven by severe and sustained overactivation of the renin-angiotensin-aldosterone system (RAAS). Critically elevated angiotensin II stimulates aldosterone secretion, which in turn powerfully upregulates ENaC-mediated sodium and water retention in the renal tubule — the exact pathway amiloride targets. Theoretically, ENaC blockade could attenuate this aldosterone-driven sodium overload, reduce intravascular volume, lower blood pressure, and confer renal protection by mitigating tubular hyperfiltration stress.

However, significant clinical limitations constrain this rationale. Malignant hypertension is a medical emergency requiring fast, often parenteral blood pressure reduction, whereas oral potassium-sparing diuretics have a slow onset and are conventionally adjunctive agents. More critically, the severe renal dysfunction that frequently accompanies malignant renovascular hypertension (eGFR < 30 mL/min) is a standard contraindication to amiloride due to life-threatening hyperkalemia risk — making safety concerns the dominant consideration over theoretical efficacy in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for amiloride in malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Examination of mineralocorticoid hypertension workup; describes aldosterone excess in primary aldosteronism (Conn's syndrome) as a driver of ENaC-mediated sodium retention and hypokalaemic hypertension — provides mechanistic background relevant to ENaC-targeting strategies in RAAS-driven hypertension |

---

## India Market Information

Amiloride is currently not approved or marketed in India. No registered license records are available.

---

## Safety Considerations

**Drug Interactions:** A total of 136 drug interactions have been identified for amiloride. Key clinically relevant interactions are summarised below:

| Interacting Drug | Severity | Clinical Notes |
|-----------------|----------|----------------|
| Metformin | Moderate | Amiloride inhibits renal tubular secretion of metformin (via OCT2 transporter competition), potentially raising metformin plasma concentrations |
| Hydrocortisone | Moderate | Glucocorticoids counteract amiloride's potassium-sparing and natriuretic effects; risk of electrolyte imbalance |
| Dexamethasone | Moderate | Same class mechanism as hydrocortisone; electrolyte dysregulation risk |
| Betamethasone / Budesonide | Moderate | Corticosteroid-class interaction; sodium retention may oppose amiloride's action |
| Canagliflozin / Dapagliflozin / Empagliflozin / Ertugliflozin | Moderate | SGLT2 inhibitors combined with potassium-sparing diuretics increase risk of hyperkalemia and symptomatic volume depletion |
| Exenatide | Moderate | GLP-1 receptor agonist; potential for altered renal haemodynamics and additive glucose/electrolyte effects |
| Bupropion | Moderate | Interaction mechanism not fully characterised; monitor cardiovascular and CNS parameters |
| Bisacodyl / Lactulose / Lactitol / Castor oil / Glycerin | Moderate | Stimulant and osmotic laxatives may exacerbate electrolyte losses; compounding amiloride's potassium retention creates unpredictable electrolyte balance |
| Dronabinol | Moderate | Potential interaction with cardiovascular tone or fluid balance |
| Doxycycline / Amoxicillin / Cimetidine | Minor | Low clinical significance under standard dosing; routine monitoring sufficient |

> Package insert warnings and contraindications data were not available for this report (Data Gap DG001). Please refer to the full prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the ENaC-blocking pharmacology of amiloride is mechanistically consistent with the RAAS-driven pathophysiology of malignant renovascular hypertension, direct clinical evidence is absent — supported only by a single tangentially relevant review. The acute and life-threatening nature of malignant hypertension, combined with the common contraindication of amiloride in renal impairment (a hallmark of this condition), makes advancing this indication without substantially more evidence premature.

**To proceed, the following is needed:**
- Retrieve full DrugBank MOA profile (Data Gap DG002) to formally document the ENaC-blocking mechanism and any secondary targets
- Obtain CDSCO/TFDA package insert (Data Gap DG001) to characterise the complete contraindication and warning profile, particularly renal function thresholds
- Commission preclinical studies specifically evaluating amiloride efficacy and safety in malignant renovascular hypertension animal models
- Define whether amiloride could serve as an adjunctive agent (alongside first-line parenteral antihypertensives) rather than monotherapy, with a clear renal safety cutoff (eGFR threshold)
- Evaluate India regulatory pathway requirements, given zero current domestic registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

