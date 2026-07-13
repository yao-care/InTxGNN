---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuresis to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a classical osmotic diuretic, traditionally administered intravenously to reduce raised intracranial pressure and treat acute oliguria. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with **0 clinical trials** and **1 publication** currently supporting this direction — placing it at the earliest exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osmotic diuresis (raised intracranial pressure, acute oliguria) — India regulatory record unavailable |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mannitol is a non-metabolized sugar alcohol that works as an osmotic diuretic. When given intravenously, it raises plasma osmolality, draws free water from intracellular compartments into the bloodstream, and is then freely filtered and excreted by the kidney — producing net free-water loss without significant sodium depletion. This mechanism is the foundation of its established use in reducing cerebral oedema and managing acute oliguric states.

NSIAD is caused by gain-of-function mutations in AVPR2 (the V2 vasopressin receptor gene), resulting in constitutive, ADH-independent water reabsorption in the collecting duct. Patients develop persistent hyponatraemia and plasma hypo-osmolality with an inappropriately concentrated urine. In theory, Mannitol's osmotic diuretic action could counteract this free-water retention, increase free-water excretion, and partially restore serum osmolality — a plausible mechanistic bridge.

However, the case has real limitations. The effect would likely be transient and difficult to sustain without continuous infusion. More importantly, rapid osmotic shifts carry a meaningful risk of worsening electrolyte instability. No dedicated preclinical or clinical study has tested Mannitol specifically in NSIAD. The TxGNN high score most likely reflects shared osmolality-regulation network topology in the knowledge graph rather than established biological efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Clinical Review | European Journal of Internal Medicine | Describes 10 common pitfalls in evaluating hyponatraemic patients; emphasises accurate causative diagnosis — including distinguishing SIADH from NSIAD — to avoid inappropriate osmotic correction. Provides indirect context for how diuretics may be misapplied in these settings. |

---

## India Market Information

Mannitol is currently not registered with CDSCO. No product authorisations are on record.

---

## Safety Considerations

**Drug Interactions:** 249 interactions have been identified in total. The most clinically significant are listed below:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Amikacin | **Major** | Enhanced nephrotoxicity; combined osmotic and direct tubular injury risk |
| Lamivudine | Moderate | |
| Formoterol | Moderate | |
| Salbutamol | Moderate | |
| Amifostine | Moderate | |
| Benazepril | Moderate | |
| Captopril | Moderate | |
| Canagliflozin | Moderate | |
| Dapagliflozin | Moderate | |
| Carbamazepine | Moderate | |
| Cisatracurium | Moderate | |
| Citalopram | Moderate | |
| Desvenlafaxine | Moderate | |
| Bisacodyl | Moderate | |
| Picosulfuric acid | Moderate | |
| Polyethylene glycol (3350 with electrolytes) | Moderate | |
| Iothalamic acid | Moderate | |
| Diatrizoate | Moderate | |
| Arformoterol | Moderate | |
| Doxycycline | Minor | |

Please refer to the package insert for key warnings and contraindication details (formal India label data not available).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for Mannitol in NSIAD is virtually non-existent — only one tangentially relevant review article was identified and no clinical trials have been registered. While a mechanistic rationale can be sketched, the risks of osmotic overtreatment and electrolyte instability in this patient population are real and uncharacterised.

**To proceed, the following is needed:**

- Detailed pharmacodynamic profiling of Mannitol's effect on serum osmolality in AVPR2 gain-of-function models (preclinical — cell line or animal)
- A formal mechanistic study confirming that net free-water excretion is achievable without destabilising serum sodium in NSIAD
- Safety risk assessment covering osmotic demyelination syndrome potential during correction phases
- Review of dosing regimens: continuous vs bolus infusion feasibility for a chronic condition
- India regulatory pathway evaluation with CDSCO for an unlicensed osmotic diuretic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

