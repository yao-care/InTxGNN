---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cyclopentolate: From Ophthalmic Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a short-acting antimuscarinic agent used clinically as an ophthalmic mydriatic/cycloplegic (pupil dilation and ciliary muscle paralysis for eye exams). The TxGNN model assigns a high prediction score (**99.54%**) linking it to **Cauda Equina Syndrome**, but currently **0 clinical trials** and **0 publications** support this association, and the evidence pack's own mechanistic review flags this specific link as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic cycloplegia/mydriasis (based on known pharmacological class; not recorded in the current regulatory data extract) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological class information, cyclopentolate is a short-acting antimuscarinic that blocks muscarinic (M) receptors in the eye's sphincter and ciliary muscles, producing pupil dilation and temporary loss of accommodation. It is used exclusively as a topical ophthalmic agent for diagnostic and pre/post-operative purposes, not as a systemic therapeutic.

Cauda equina syndrome, however, is a surgical emergency caused by mechanical compression of the lumbosacral nerve roots — a structural/neurological problem with no established connection to muscarinic receptor blockade. The evidence pack's own rationale is explicit on this point: the high TxGNN score most likely reflects an indirect knowledge-graph association (e.g., shared "nervous system" node clustering) rather than a real pharmacological pathway, and no causal mechanism can be identified.

Notably, the pack's two lower-ranked candidates for this drug — neurogenic bladder and irritable bowel syndrome — have a *stronger* mechanistic rationale, since antimuscarinics are an established drug class for both conditions (via bladder detrusor M3 or gut smooth-muscle M3 blockade). Cauda equina syndrome stands out as the weakest-supported of the three predictions and should not be prioritized over them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Cyclopentolate is currently **not marketed**, with no registration records available in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5, decision stage S0) with no clinical trials, no literature, and — per the evidence pack's own mechanistic analysis — no plausible causal pathway between antimuscarinic action and cauda equina syndrome's compressive pathophysiology. The drug is also not currently marketed, so there is no existing indication base to build on.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action from DrugBank or primary literature
- Preclinical or mechanistic studies establishing a credible biological rationale before further evaluation
- If pursuing repurposing for this drug, re-evaluate the higher-plausibility candidates (neurogenic bladder, irritable bowel syndrome) instead of this top-ranked but mechanistically weak candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

