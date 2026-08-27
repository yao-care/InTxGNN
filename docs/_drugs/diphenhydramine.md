---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diphenhydramine: From Allergic Reactions to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1 receptor antagonist, widely used globally for allergic reactions, motion sickness, and insomnia, though it holds no approved indications in the India market.
The TxGNN model predicts it may be effective for **Rosacea Conjunctivitis**, with a high model confidence score of **99.20%**;
however, **no clinical trials** and **no published literature** currently support this specific indication, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic reactions, motion sickness, insomnia (global use; no India market approval on record) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Diphenhydramine is a first-generation H1 receptor antagonist with pronounced anticholinergic properties. It competitively blocks histamine at H1 receptors, thereby attenuating vasodilation, increased vascular permeability, and pruritus associated with allergic and inflammatory responses. It also crosses the blood–brain barrier, producing sedation and local anesthetic effects.

Rosacea conjunctivitis (ocular rosacea) is a chronic inflammatory condition of the ocular surface involving mast cell activation, histamine release, and neurogenic inflammation. In theory, H1 receptor blockade could suppress histamine-mediated vasodilation and conjunctival itch. Additionally, diphenhydramine's local anesthetic properties might transiently relieve surface irritation. These mechanistic bridges—shared with general allergic conjunctivitis—are likely the basis for the TxGNN model's high score, given graph connectivity between "allergic eye disease" and "conjunctivitis" nodes.

However, several critical mechanistic mismatches temper this prediction. The primary pathological drivers in rosacea are Demodex mite infestation, innate immune dysregulation (TLR2 overexpression), and neurovascular dysregulation—not a histamine-dominant pathway. More importantly, diphenhydramine's strong anticholinergic activity suppresses lacrimal gland secretion, which may substantially worsen dry eye syndrome—the most debilitating core complication of ocular rosacea. The high TxGNN score (0.992) more likely reflects indirect graph-level associations rather than rosacea-specific mechanistic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Diphenhydramine has **394 documented drug interactions** on record. The following represent the highest-priority interactions:

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|-----------------|
| **Major** | Potassium citrate | Potential for significant adverse interaction; close monitoring required |
| **Major** | Eliglustat | CYP2D6 inhibition by diphenhydramine may elevate eliglustat plasma levels substantially |
| Moderate | Hyoscyamine | Additive anticholinergic effects (dry mouth, urinary retention, confusion) |
| Moderate | Atropine | Additive anticholinergic toxicity |
| Moderate | Dicyclomine | Additive anticholinergic burden |
| Moderate | Glycopyrronium | Additive anticholinergic burden |
| Moderate | Methscopolamine | Additive anticholinergic burden |
| Moderate | Morphine | Additive CNS and respiratory depression |
| Moderate | Bupropion | Increased risk of CNS adverse effects |
| Moderate | Metoclopramide | Opposing gastrointestinal motility effects; potential pharmacodynamic antagonism |

> Please refer to the package insert for complete warnings, contraindications, and precautions, including use in elderly patients (high anticholinergic burden), pregnancy, and renal/hepatic impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting diphenhydramine for rosacea conjunctivitis, and the mechanistic rationale has a critical safety liability—diphenhydramine's anticholinergic effect on lacrimal secretion may actively worsen dry eye, which is a hallmark and often disabling complication of ocular rosacea.

**To proceed, the following is needed:**

- Formal MOA documentation (DrugBank API query recommended per DG002 remediation plan)
- CDSCO/TFDA package insert to retrieve warnings and contraindications (per DG001 remediation plan)
- Preclinical or in vitro evidence demonstrating diphenhydramine efficacy in rosacea or Demodex-driven ocular inflammation models
- A safety assessment specifically addressing whether anticholinergic effects exacerbate dry eye in ocular rosacea patients
- Mechanistic clarification on whether H1 blockade plays a clinically meaningful role in ocular rosacea pathophysiology (distinct from simple allergic conjunctivitis)
- Ophthalmic route compatibility assessment before any translational consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

