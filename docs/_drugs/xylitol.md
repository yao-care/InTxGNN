---
layout: default
title: Xylitol
parent: Model Prediction Only (L5)
nav_order: 899
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Xylitol: predicted new indication Meningococcal infection (evidence level L5). Approved use: Not stated in the licence records"
monitor_inn: "Xylitol"
predicted_indications: ["meningococcal infection"]
---

# Xylitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Xylitol: From an Unspecified Original Indication to Meningococcal Infection

## One-Sentence Summary

Xylitol is a sugar alcohol currently marketed in India as oral tablets, but the licence records compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **meningococcal infection**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The original indication is also not recorded in the data compiled for this report, so a direct link between the original use and the new indication cannot be drawn.

The prediction therefore rests on the model's very high score (0.997). Some hypotheses are plausible but unverified. Xylitol may interfere with bacterial adhesion to the nasopharyngeal lining, as has been described for *Streptococcus pneumoniae* and *Haemophilus influenzae* in the upper airway. It may also limit bacterial growth because many bacteria cannot ferment it readily. Neither effect has been shown for *Neisseria meningitidis*.

Systemic exposure to xylitol is low when it is taken orally or nasally. It is therefore unlikely to treat invasive meningococcal disease (meningitis or sepsis), which requires systemic antibiotics. Any realistic role would be limited to nasopharyngeal carriage or colonisation, and even that is speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 241987 | Wysliva Tablet | Strip of 10 tablets | Not stated |
| 201656 | Salitol Tablet | Bottle of 60 tablets | Not stated |

Both products are single-ingredient oral tablets with valid status.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (PrimeKG) links xylitol to a contraindication with **dental fluorosis**. This comes from graph relationships, not from package insert text, and should be verified.
- **Drug Interactions**: No interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5). Xylitol's low systemic exposure makes treatment of invasive meningococcal disease implausible. The mechanism and the original indication are also missing.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the Indian regulator's records (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence (for example, in vitro effects on *N. meningitidis* adhesion or growth) and a defined use case, such as nasopharyngeal carriage
- Verification of the dental fluorosis contraindication signal
- Route compatibility assessment for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

