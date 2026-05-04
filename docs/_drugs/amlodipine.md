---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a well-established L-type calcium channel blocker (CCB) globally approved for hypertension and angina, though it is not currently registered in India per available regulatory data.
The TxGNN model ranks **Brain Stem Infarction** as its top predicted new indication (score 99.94%),
however there are currently **0 clinical trials** and **0 publications** directly supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Angina (global approval; not registered in India per current data) |
| Predicted New Indication | Brain Stem Infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Amlodipine is a dihydropyridine-class L-type calcium channel blocker. It works by blocking voltage-gated L-type calcium channels in vascular smooth muscle, producing arterial vasodilation, reducing peripheral vascular resistance, and lowering systemic blood pressure. It also relieves coronary vasospasm, which underpins its use in angina.

The theoretical basis for this prediction lies in the role of calcium in ischemic brain injury. During cerebral ischemia, excessive intracellular calcium influx — so-called "calcium overload" — is a well-characterised driver of neuronal death. Blocking L-type calcium channels could theoretically limit this overload and provide neuroprotection. For brain stem infarction specifically, dilation of the basilar and vertebral arteries may additionally improve perfusion pressure to the affected territory. Supporting this general direction, preclinical evidence does exist for Amlodipine in middle cerebral artery occlusion models (see cerebral artery occlusion, ranked #6 in this Evidence Pack).

However, this mechanistic reasoning has never been specifically tested — preclinically or clinically — in the context of brain stem infarction as a distinct anatomical location. Brain stem ischemia involves the basilar territory and carries unique physiological constraints not fully captured in broader stroke models. The TxGNN prediction most likely reflects high-order indirect associations within the knowledge graph rather than a direct, validated biological pathway, and should be treated as a computational hypothesis requiring experimental confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brain Stem Infarction.

---

## Literature Evidence

Currently no related literature available for Brain Stem Infarction.

---

## Safety Considerations

**Drug Interactions** (292 total interactions identified; all rated Moderate by DDInter):

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|--------------------|
| Clarithromycin | Moderate | CYP3A4 inhibitor — may substantially increase amlodipine plasma exposure |
| Calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate, phosphate, etc.) | Moderate | Calcium supplementation may partially antagonise CCB pharmacodynamic effects |
| Corticosteroids (Hydrocortisone, Betamethasone, Budesonide, Dexamethasone) | Moderate | Corticosteroids can blunt antihypertensive response via sodium/water retention |
| Canagliflozin / Dapagliflozin | Moderate | Additive hypotensive effects; monitor for symptomatic hypotension |
| Aprepitant | Moderate | CYP3A4 moderate inhibitor — potential increase in amlodipine levels |
| Bupropion | Moderate | Potential additive cardiovascular effects |
| Clotrimazole | Moderate | CYP3A4 interaction — may alter amlodipine exposure |

Please refer to the full package insert for complete safety information including key warnings and contraindications, which were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature directly investigating Amlodipine for brain stem infarction. The prediction rests entirely on computational modelling (L5 evidence), with no preclinical or clinical validation in this specific anatomical region.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank to support or challenge the mechanistic hypothesis
- **Regulatory safety data**: Obtain India package insert (or global SmPC) to complete key warnings and contraindication assessment
- **Preclinical validation**: Commission or identify in vitro / in vivo studies using brainstem ischemia models (e.g., basilar artery occlusion)
- **Cross-indication extrapolation review**: Assess whether the 5 existing animal studies on cerebral artery occlusion (Rank #6, L3) can reasonably support a brainstem-specific hypothesis
- **Broader landscape review**: Consider that stronger evidence exists within this same Evidence Pack for related indications — notably **intracerebral hemorrhage** (Rank #10, L2: TRIDENT Phase 3 trial, 1,671 patients, completed) and **cerebral artery occlusion** (Rank #6, L3: 5 consistent animal studies) — which may be more actionable near-term repurposing candidates for further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

