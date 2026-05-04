---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Aliskiren: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Aliskiren is the first-in-class oral direct renin inhibitor, approved globally for the treatment of essential hypertension by blocking RAAS at its most upstream, rate-limiting step.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism** (TxGNN Rank #1, score 99.98%),
however **no clinical trials or publications** currently support this specific direction (Evidence Level: L5). Across all 7 predicted indications in this pack, **cerebrovascular disorder** holds the strongest evidence base (L3, 2 trials, 13 publications), though a major safety signal from the ALTITUDE trial remains unresolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential hypertension |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Aliskiren directly binds to and inhibits renin — the enzyme that catalyses the conversion of angiotensinogen to angiotensin I — thereby blocking the entire renin-angiotensin-aldosterone system (RAAS) at its most upstream, rate-limiting step. This mechanism is distinct from ACE inhibitors and ARBs, which act further downstream; by targeting renin itself, Aliskiren prevents compensatory rises in plasma renin activity that are commonly seen with downstream RAAS blockade.

The biological rationale connecting RAAS inhibition to pulmonary hypertension rests on the observation that angiotensin II overactivation promotes proliferation and contraction of pulmonary vascular smooth muscle cells, contributing to vascular remodelling. Theoretically, upstream renin inhibition could reduce Ang II in the pulmonary circulation and attenuate this remodelling cascade. This connection is further supported by the known role of RAAS in systemic vascular biology and left ventricular afterload reduction.

However, the specific WHO classification targeted here — pulmonary hypertension with **unclear multifactorial mechanism** (WHO Group 5) — is driven primarily by heterogeneous and poorly understood pathological processes, with RAAS playing only a minor and indirect role. Core PAH pathways (nitric oxide deficiency, endothelin-1 overproduction, prostacyclin deficiency) are largely unaffected by renin inhibition. No preclinical or clinical study has directly tested Aliskiren in this disease subtype, making the TxGNN prediction biologically plausible but highly speculative at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for **pulmonary hypertension with unclear multifactorial mechanism**.

> **Note on other predicted indications:** Clinical trial evidence does exist for other TxGNN-predicted indications in this pack. The most notable is a terminated Phase 2/3 trial for **cerebrovascular disorder** ([NCT01417104](https://clinicaltrials.gov/study/NCT01417104) — Aliskiren vs. placebo in atherosclerosis, n=71, terminated early) and a large observational registry ([NCT01454583](https://clinicaltrials.gov/study/NCT01454583), n=15,337).

---

## Literature Evidence

Currently no related literature directly linking Aliskiren to **pulmonary hypertension with unclear multifactorial mechanism**.

> **Note on Rank #2 indication:** Literature retrieved for the closely related indication "pulmonary hypertension owing to lung disease and/or hypoxia" (Rank #2) contains 19 publications on hypoxia biology, but **none directly study Aliskiren in this context**. Retrieved articles cover general hypoxia mechanisms (HIF-1α, CMGC kinases, tumour hypoxia), and are not clinically relevant to Aliskiren repurposing. Evidence Level remains L5 for this indication as well.

---

## All Predicted Indications — Summary Table

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|------------|---------------|---------|
| 1 | Pulmonary hypertension with unclear multifactorial mechanism | 99.98% | L5 | Hold |
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.98% | L5 | Hold |
| 3 | Malignant renovascular hypertension | 99.98% | L4 | Research Question |
| 4 | Malignant hypertensive renal disease | 99.98% | L4 | Research Question |
| 5 | Braddock syndrome | 99.97% | L5 | Hold |
| 6 | Chronic pulmonary heart disease | 99.78% | L4 | Hold |
| **7** | **Cerebrovascular disorder** | **99.19%** | **L3** | **Hold (safety signal)** |

**Cerebrovascular disorder (Rank #7)** carries the most evidence, including:
- Animal studies showing Aliskiren reduces brain damage in chronic cerebral hypoperfusion models and ischaemic stroke (PMID [21859961](https://pubmed.ncbi.nlm.nih.gov/21859961/), [27180190](https://pubmed.ncbi.nlm.nih.gov/27180190/))
- The AQUARIUS trial subgroup analysis showing potential harm in diabetic patients with dual RAAS blockade (PMID [26523993](https://pubmed.ncbi.nlm.nih.gov/26523993/))
- A critical safety signal from the ALTITUDE trial: **increased non-fatal stroke risk** attributed to acute hypotension-induced cerebral ischaemia (PMID [23418282](https://pubmed.ncbi.nlm.nih.gov/23418282/))

**Malignant renovascular hypertension (Rank #3)** holds the highest mechanistic alignment: high-renin hypertension is theoretically the optimal context for renin inhibition. However, acute RAAS blockade in severe renal artery stenosis carries risk of acute kidney failure — the same contraindication that applies to ACE inhibitors and ARBs in this population.

---

## India Market Information

Aliskiren is currently **not marketed in India**. No product registrations or approved licenses were found in the regulatory database.

> For reference: Aliskiren (brand name Rasilez / Tekturna) is approved in the US, EU, and several other markets for essential hypertension at doses of 150–300 mg once daily.

---

## Safety Considerations

Package insert warnings and contraindications data are not available for India (no local regulatory filings). Please refer to the US FDA prescribing information or EMA SmPC for full safety details.

**Drug Interactions** (114 interactions identified; representative moderate-severity interactions listed below):

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Potassium bicarbonate / chloride / citrate / gluconate | Moderate | Additive hyperkalaemia risk; monitor serum potassium closely |
| Canagliflozin / Dapagliflozin / Empagliflozin / Ertugliflozin | Moderate | SGLT2 inhibitors may alter renal haemodynamics; increased risk of AKI and hyperkalaemia when combined with RAAS inhibitors |
| Clarithromycin | Moderate | CYP3A4/P-gp inhibition may increase Aliskiren plasma levels |
| Clotrimazole / Miconazole | Moderate | Azole antifungals inhibit P-gp transport; may raise Aliskiren bioavailability |
| Aprepitant | Moderate | P-gp/CYP3A4 inhibition; potential increase in Aliskiren exposure |
| Hydrocortisone / Betamethasone / Budesonide / Dexamethasone / Prednisolone / Prednisone | Moderate | Corticosteroids antagonise antihypertensive effect via sodium/water retention; may blunt Aliskiren efficacy |
| Acetylsalicylic acid (Aspirin) | Moderate | NSAIDs may reduce antihypertensive efficacy and increase renal impairment risk |
| Eliglustat | Moderate | P-gp inhibition; monitor for enhanced Aliskiren effect |

> **Critical known safety signals from clinical trials (not in DDI database):**
> - **ALTITUDE trial**: Aliskiren added to ACE-I or ARB in patients with type 2 diabetes and CKD showed increased risk of renal failure, hyperkalaemia, hypotension, and **non-fatal stroke**. This combination is now contraindicated.
> - **ASTRONAUT trial**: Aliskiren failed to improve post-hospitalisation outcomes in heart failure and caused harm in preserved EF subgroups.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns high confidence scores to Aliskiren across multiple cardiovascular and pulmonary vascular indications, which is mechanistically coherent given RAAS involvement in vascular biology. However, the top-ranked indication (pulmonary hypertension with unclear multifactorial mechanism) has absolutely no supporting clinical evidence (L5), and critically, **existing large randomised trials have generated safety signals** — particularly increased stroke and renal failure risk — that substantially restrict the repurposing space for Aliskiren.

**To move forward, the following is needed:**

- **Obtain full safety data**: Download and parse the Indian prescribing information (or US FDA label / EMA SmPC) to establish contraindications and black-box warnings before any S1 evaluation.
- **Resolve the ALTITUDE safety signal**: Before pursuing any cardiovascular or renal repurposing candidate, formally assess whether the target population shares risk characteristics with the ALTITUDE cohort (diabetic, CKD, dual RAAS blockade).
- **Prioritise Rank #3 (malignant renovascular hypertension) for mechanistic deep-dive**: This is the highest mechanistic alignment indication — high-renin state is the theoretical ideal for renin inhibition. A research protocol to characterise renal safety guardrails in this specific population is the most scientifically defensible next step.
- **Cerebrovascular disorder (Rank #7)**: Requires a redesigned study hypothesis that separates blood-pressure-dependent stroke protection from direct RAAS neuroprotection, and must explicitly address the ALTITUDE hypotension-stroke signal. Animal data are encouraging but insufficient without human safety reassurance.
- **Confirm MOA from DrugBank API**: Obtain full pharmacological profile to enable complete mechanism-to-indication mapping for all 7 candidates.
- **Commission India-specific epidemiological assessment**: Prevalence data for high-renin hypertension and renovascular disease subtypes in the Indian population would inform which indication carries the highest unmet need.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

