---
layout: default
title: Rimonabant
parent: Model Prediction Only (L5)
nav_order: 735
evidence_level: L5
indication_count: 7
---

# Rimonabant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

Using no additional skill — this is a direct report-generation task per the supplied template with a fully specified Evidence Pack; no ambiguity requiring brainstorming/debugging.

# Rimonabant: From Obesity (CB1 Receptor Blockade) to Hypervitaminosis

## One-Sentence Summary

> Rimonabant is a synthetic CB1 receptor antagonist whose pharmacology data describes its historical clinical use as an obesity treatment (marketed as Acomplia® before global withdrawal).
> The TxGNN model's top-ranked prediction is **Hypervitaminosis**, but the model's own rationale explicitly flags this link as lacking any known biological plausibility and possibly representing knowledge-graph noise.
> **No clinical trials and no literature** currently support this or any of the other six top-ranked candidates in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in India market licenses (0 licenses); pharmacology data lists historical `clinical_use`: "CB1 receptor blocker for obesity" |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as Blocking/High-severity data gap DG002). Based on the pharmacology data provided, rimonabant acts as a CB1 cannabinoid receptor (CNR1) antagonist and also binds GPR55, and was historically used to treat obesity by suppressing appetite via the endocannabinoid system.

However, the model's own repurposing rationale for this candidate states there is **no known mechanistic overlap** between CB1/endocannabinoid signaling and fat-soluble vitamin excess metabolism, and explicitly notes the high TxGNN score may reflect knowledge-graph connection noise rather than genuine biology.

This weakness is not isolated to the top candidate: of the seven ranked predictions in this pack, most are flagged by the model's own rationale as mechanistically implausible — three involve obsolete ontology terms or non-druggable congenital structural syndromes (16p11.2 microdeletion, obsolete hypertelorism, frontorhiny, Boissel-type lethal polymalformative syndrome), and one (insomnia, rank 6) is flagged as **directionally contradictory** — CB1 blockade is associated with sleep disturbance as a known adverse effect of rimonabant, not a therapeutic benefit. No candidate in this pack currently rises above L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Rimonabant currently holds **no market licenses in India** (`total_licenses: 0`, `market_status: Not marketed`). No dosage forms or registered products are on file.

---

## Safety Considerations

- **Pharmacological Target Data**: Rimonabant binds the CB1 receptor (CNR1, human) and GPR55 (human) as its primary pharmacological targets. These are target-binding annotations, not clinical drug-drug interaction (DDI) records — no clinical DDI data is currently available.
- **Known Safety History (from model rationale, rank 6)**: Insomnia/sleep disturbance is noted as a known adverse effect of rimonabant from prior clinical experience. This is consistent with rimonabant's broader regulatory history of withdrawal due to psychiatric safety signals (depression, suicidal ideation), though formal TFDA/package-insert warnings are not yet available (DG001, Blocking).

Full package insert warnings and contraindications are not currently available and must be sourced before any safety evaluation proceeds (see DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications are L5 (model prediction only), with zero clinical trials or literature support. The top-ranked candidate's own generated rationale identifies it as likely knowledge-graph noise, several lower-ranked candidates involve non-druggable congenital syndromes, and one candidate (insomnia) is mechanistically contradictory to rimonabant's known pharmacology. The drug is also unmarketed in India and missing both MOA confirmation and package insert safety data — two data gaps, one of which is Blocking.

**To proceed, the following is needed:**
- Resolve DG001: obtain official package insert warnings/contraindications (Blocking — required before any S1 safety screening)
- Resolve DG002: confirm mechanism of action via DrugBank or primary literature
- Given rimonabant's known history of market withdrawal for psychiatric safety concerns, obtain full pharmacovigilance/regulatory withdrawal rationale before allocating further evaluation resources
- If repurposing evaluation continues, deprioritize candidates already flagged by the model as mechanistically implausible (ranks 1, 2, 3, 4, 7) and treat rank 6 (insomnia) as a safety signal rather than an efficacy lead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

