---
layout: default
title: Potassium
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
---

# Potassium
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

# Potassium: From Electrolyte Supplementation to Hypertensive Disorder

## One-Sentence Summary

Potassium (DrugBank DB14500) is an essential electrolyte; this dataset contains no approved indication or market presence for it in Taiwan. The TxGNN model predicts a strong association with **Hypertensive Disorder**, and while 50 clinical trials were screened, most are only tangentially related — the real weight of evidence comes from **20 publications**, including a landmark RCT and multiple systematic reviews on potassium/salt-substitute intake and blood pressure.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Potassium has no registered indication or license in Taiwan; it functions as a physiological electrolyte rather than a marketed drug product in this dataset |
| Predicted New Indication | Hypertensive Disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available from DrugBank in this pack (flagged as a High-severity data gap). Based on established physiology, dietary/supplemental potassium acts on the renal distal convoluted tubule by suppressing the WNK–SPAK–NCC (Na⁺/Cl⁻ co-transporter) pathway, promoting natriuresis, reducing sympathetic tone, and improving vascular endothelial function — a well-characterized, consensus mechanism for blood-pressure lowering rather than a novel repurposing hypothesis.

This means the TxGNN score is essentially rediscovering long-established nutrition-physiology knowledge (low potassium intake / high sodium-to-potassium ratio raises blood pressure) rather than surfacing a truly new mechanistic link. The practical repurposing question is therefore not "does potassium lower blood pressure" (well established) but "can this specific DrugBank entity (elemental/ionic potassium) be positioned as a regulated therapeutic product" — since the record shows zero Taiwan licenses and no defined dosage form, formulation (e.g., potassium chloride, potassium-enriched salt substitute) and target population (especially renal function) would need to be defined before any regulatory pathway is pursued.

---

## Clinical Trial Evidence

Note: the search for "Potassium" + "hypertensive disorder" returned 50 trials, but most are general antihypertensive-drug studies with no direct potassium intervention (graded C — not shown). The trials below are the ones with a direct thematic link to potassium/salt-substitute intervention or the potassium–aldosterone axis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07178964](https://clinicaltrials.gov/study/NCT07178964) | N/A | Not yet recruiting | 80 | Evaluates potassium-rich salt substitutes for blood pressure control in kidney transplant recipients — most directly on-topic trial in the set |
| [NCT05638009](https://clinicaltrials.gov/study/NCT05638009) | N/A | Unknown | 2490 | EPIC trial: cluster-randomized, double-blind comparison of two potassium-enriched salt substitutes vs. regular salt on systolic BP (Argentina) |
| [NCT05593055](https://clinicaltrials.gov/study/NCT05593055) | Phase 4 | Recruiting | 75 | Mineralocorticoid receptor antagonism vs. thiazide-like diuretic on coronary microvascular function in hypertensive LVH patients — relevant to the potassium–aldosterone axis but not a direct potassium intervention |
| [NCT06569589](https://clinicaltrials.gov/study/NCT06569589) | N/A | Recruiting | 80 | Non-invasive tissue Na⁺/K⁺ quantification (23Na-MRI) in primary aldosteronism, analogous to HbA1c as a long-term metabolic marker |
| [NCT06597630](https://clinicaltrials.gov/study/NCT06597630) | N/A | Recruiting | 100 | Pathology, genetics, and clinical phenotype of unilateral primary aldosteronism in Asians (K⁺/aldosterone axis, observational only) |
| [NCT03326583](https://clinicaltrials.gov/study/NCT03326583) | Phase 2 | Completed | 27 | Patiromer (a potassium-*binder*) effects on serum K⁺ and gut microbiome in ESRD hyperkalemia — opposite therapeutic direction, included only as mechanistic context |
| [NCT01318746](https://clinicaltrials.gov/study/NCT01318746) | N/A | Completed | 30 | Circadian rhythm and day-to-day variability of serum potassium and cystatin C in renal impairment |
| [NCT04761354](https://clinicaltrials.gov/study/NCT04761354) | N/A | Completed | 514 | Multicenter analysis of blood-pressure reduction following adrenalectomy for primary aldosteronism |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34459569](https://pubmed.ncbi.nlm.nih.gov/34459569/) | 2021 | RCT | The New England Journal of Medicine | Salt substitution (reduced sodium, increased potassium) significantly reduced cardiovascular events and death in a large randomized trial |
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Dose-response Meta-Analysis of RCTs | J Am Heart Assoc | Establishes a dose-response relationship between potassium supplementation and blood pressure across RCTs ≥4 weeks |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic Review / Meta-Analysis | BMJ | Increased potassium intake associated with reduced blood pressure and lower stroke risk |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Review | Nutrients | Reviews potassium bioavailability and its role in blood pressure and glucose control |
| [29771736](https://pubmed.ncbi.nlm.nih.gov/29771736/) | 2018 | Review | Current Opinion in Cardiology | Dietary approaches, including potassium intake, for prevention/management of hypertension |
| [30190007](https://pubmed.ncbi.nlm.nih.gov/30190007/) | 2018 | Review | J Am Coll Cardiol | Identifies inadequate dietary potassium as a modifiable risk factor in hypertension prevention/control |
| [23674806](https://pubmed.ncbi.nlm.nih.gov/23674806/) | 2013 | Review | Advances in Nutrition | Moderate evidence linking potassium intake to blood pressure reduction and downstream stroke/CHD risk |
| [31060074](https://pubmed.ncbi.nlm.nih.gov/31060074/) | 2019 | Review | Annals of Internal Medicine | Contemporary hypertension management guideline review referencing dietary potassium |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Review | American Journal of Hypertension | State-of-the-art review on potassium and hypertension, contrasting emphasis on sodium restriction vs. potassium supplementation |
| [39472546](https://pubmed.ncbi.nlm.nih.gov/39472546/) | 2025 | Review | Hypertension Research | Role of dietary potassium and salt substitution in prevention and management of hypertension |

---

## Taiwan Market Information

No marketing authorizations are on file for this candidate — `taiwan_regulatory.total_licenses = 0` and the license list is empty. Potassium (DB14500) is currently **not marketed** in Taiwan as a registered drug product under this record.

---

## Safety Considerations

Please refer to the package insert for safety information — no key warnings, contraindications, or drug-interaction data are on file for this candidate, and the DDI lookup returned no results.

One point worth flagging independent of this data gap: because the candidate is elemental/ionic potassium itself, any therapeutic use for blood-pressure control carries an inherent, drug-class-level hyperkalemia risk — particularly in patients with renal impairment or those on RAAS-active agents (ACEi/ARB/MRA) — that should be assumed and verified once a specific TFDA label is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and epidemiological/RCT evidence linking potassium intake to blood pressure reduction is strong and well-replicated (L1), including a large NEJM RCT on potassium-enriched salt substitutes. However, this specific DrugBank record has zero Taiwan market presence, no defined formulation, and — critically — a **Blocking** data gap on TFDA label warnings/contraindications, which by policy prevents this candidate from clearing even the initial (S1) safety screen. The guardrails therefore apply to regulatory and safety readiness, not to the underlying scientific plausibility.

**To proceed, the following is needed:**
- TFDA label/package-insert warnings and contraindications (Blocking gap DG001) — required before any S1 safety pre-assessment can be completed
- DrugBank mechanism-of-action data (High-severity gap DG002) to formally document the WNK–SPAK–NCC pathway link
- Definition of the specific product form to be repositioned (e.g., potassium chloride supplement vs. potassium-enriched salt substitute) and its intended route/dosage
- A renal-function-stratified safety plan addressing hyperkalemia risk, especially in combination with ACEi/ARB/MRA therapy
- Clarification of the regulatory pathway, since the product currently holds no Taiwan license to build on
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

