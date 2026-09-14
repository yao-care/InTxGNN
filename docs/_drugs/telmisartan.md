---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 805
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Intracerebral Hemorrhage Recurrence Prevention

## One-Sentence Summary

> Telmisartan is a well-established angiotensin II receptor blocker (ARB) used globally to treat hypertension. Among **10 candidate indications** screened by TxGNN for this drug, **Intracerebral Hemorrhage (recurrence prevention)** stands out as the strongest candidate, supported by a **completed Phase 3 trial (TRIDENT, n=1,671)** and **10 relevant preclinical/clinical publications** — though the human evidence is for a triple-pill combination regimen, not telmisartan monotherapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(well-established use of telmisartan; not available in this Evidence Pack — see Data Gap DG001)* |
| Predicted New Indication | Intracerebral Hemorrhage (recurrence prevention) |
| TxGNN Prediction Score | 99.93% (score 0.99925, model rank 1792/multiple candidates) |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: This Evidence Pack screened 10 TxGNN-predicted indications for telmisartan. The top TxGNN-scored candidate (Prinzmetal angina, 99.98%) has zero supporting trials/literature (L5, Hold) and is not evidence-actionable. Intracerebral hemorrhage — ranked #9 by raw TxGNN score — has the strongest actual evidence base and is used as the lead candidate in this report. See "Why is This Prediction Reasonable?" for context on other candidates screened.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for telmisartan is currently a documented data gap (DG002, High severity). Based on the mechanistic rationale captured alongside the TxGNN predictions, telmisartan is an **AT1 receptor antagonist with partial PPARγ agonist activity** ("metabosartan"). This dual mechanism gives it antihypertensive effects plus antioxidant, anti-inflammatory, and anti-apoptotic properties that extend beyond simple blood pressure lowering.

Hypertension is the dominant modifiable risk factor for both primary and recurrent intracerebral hemorrhage (ICH). Mechanistically, AT1 blockade reduces the vascular shear stress and oxidative injury that drive hemorrhagic stroke recurrence, and multiple rodent ICH/subarachnoid hemorrhage models show telmisartan reduces apoptosis, inflammation, and vasospasm at the injury site. This provides a plausible biological bridge from telmisartan's approved antihypertensive use to secondary ICH prevention.

Clinically, this mechanistic link has already been tested in humans: the TRIDENT trial (NCT02699645) enrolled 1,671 ICH survivors and evaluated a fixed-dose "Triple Pill" (which includes telmisartan) for recurrent stroke prevention — a direct, completed Phase 3 human dataset. The caveat is that TRIDENT tested a **combination regimen**, so telmisartan's independent contribution cannot be isolated from this trial alone. Other TxGNN-predicted candidates for telmisartan (e.g., cerebral artery occlusion, L3, backed by 14 preclinical AT1/PPARγ neuroprotection studies) reinforce the same underlying cerebrovascular mechanism but lack any human trial data, and were therefore not selected as the lead indication for this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: fixed-dose "Triple Pill" (including telmisartan) vs. usual care for prevention of recurrent stroke after intracerebral hemorrhage — direct human evidence, but combination-drug design, not telmisartan monotherapy. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; terminated early with only 4 participants — no meaningful conclusions possible. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated early with only 1 participant — no meaningful conclusions possible. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial protocol | Int J Stroke | Rationale and design of the TRIDENT trial evaluating triple-pill BP control (including telmisartan) for recurrent ICH prevention. |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Cohort (secondary analysis) | Int J Stroke | Analysis within the PRoFESS secondary stroke prevention trial comparing ischemic vs. hemorrhagic recurrence rates across race-ethnic groups. |
| [15834293](https://pubmed.ncbi.nlm.nih.gov/15834293/) | 2005 | Comparative study | J Hypertension | Telmisartan vs. ramipril effects on cerebrovascular structure in hypertensive rats — reversal of arteriolar remodeling. |
| [22957022](https://pubmed.ncbi.nlm.nih.gov/22957022/) | 2012 | Preclinical (animal) | PLoS One | Short-term telmisartan (vs. candesartan) improves pial arteriole diameter in spontaneously hypertensive rats via PPARγ. |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical (animal) | J Pharmacol Exp Ther | AT1 receptor blockade with telmisartan reduces apoptosis, inflammation, and oxidative stress in a normotensive rat ICH model. |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical (animal) | Neurological Research | Telmisartan reduces oxidative stress and vasospasm after subarachnoid hemorrhage in animal model. |
| [40045320](https://pubmed.ncbi.nlm.nih.gov/40045320/) | 2025 | Preclinical (animal) | J Neuroinflammation | Angiotensin II-driven hypertension model of cerebral microhemorrhage development — mechanistic relevance to AT1-blocker protection. |
| [19148963](https://pubmed.ncbi.nlm.nih.gov/19148963/) | 2009 | Commentary | NEJM | "Telmisartan for prevention of cardiovascular events" — commentary/correspondence on cardiovascular outcome data. |

---

## India Market Information

Telmisartan currently has **no registered authorizations on file** in this dataset (0 licenses; market status: Not Marketed). No product/indication table can be generated until India regulatory registration data is obtained.

---

## Safety Considerations

- **Drug Interactions**: Telmisartan has **185 total documented interactions**. Notable **Major-severity** interactions include **Potassium citrate** and **Potassium bicarbonate** (risk of hyperkalemia, consistent with ARB pharmacology). Multiple **Moderate-severity** interactions are also documented, including corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide), SGLT2 inhibitors (Canagliflozin, Dapagliflozin, Empagliflozin), insulin/incretin agents (Insulin human, Insulin aspart, Exenatide), Bupropion, Morphine, Acetylsalicylic acid, and bowel-prep agents (Picosulfuric acid, Polyethylene glycol with electrolytes, Sodium sulfate).
- Key warnings and contraindications (product labeling) are a documented data gap (DG001, Blocking severity) — TFDA/local label warnings have not yet been obtained. Please refer to the official package insert once available.
- **Mechanism-specific caution**: One of the other screened candidates ("malignant renovascular hypertension") was flagged as a *safety-relevant, not efficacy-relevant* signal — ARBs are contraindicated or require caution in bilateral renal artery stenosis due to risk of acute kidney injury from efferent arteriolar dilation. This should inform renal function monitoring for any ICH-prevention use as well, particularly given concurrent Major hyperkalemia interaction risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among 10 TxGNN-predicted indications for telmisartan, intracerebral hemorrhage recurrence prevention is the only one supported by a completed Phase 3 human trial (TRIDENT, n=1,671) combined with a coherent, multiply-replicated preclinical mechanism (AT1 blockade + PPARγ agonism → reduced oxidative stress, inflammation, and vasospasm). However, TRIDENT tested a fixed-dose triple-pill combination, so telmisartan's independent contribution is not isolated, and two related TRIDENT sub-studies were terminated with negligible enrollment.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/local label warnings and contraindications — Blocking) before any safety initial screening (S1) can be completed
- Resolve DG002 (verified DrugBank MOA data) to confirm mechanistic rationale
- India-specific regulatory/registration data, since telmisartan currently has zero registered licenses in this market
- Analysis to isolate telmisartan's independent effect from the TRIDENT triple-pill combination (e.g., component-level subgroup or monotherapy trial data)
- Renal function and serum potassium monitoring plan, given the Major-severity potassium-related DDIs and known ARB caution in renovascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

