---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamine: From SSRI Antidepressant Use to Schizotypal Personality Disorder

## One-Sentence Summary

Fluvoxamine (DB00176) is a selective serotonin reuptake inhibitor (SSRI); the evidence pack does not carry a confirmed original indication record (drug is unregistered in Taiwan), though the literature it does contain repeatedly documents historical use in obsessive-compulsive disorder and related anxiety-spectrum conditions. The TxGNN model's top-ranked prediction for this compound is **Schizotypal Personality Disorder**, but this candidate currently has **zero clinical trials** and **zero publications** supporting it — the score reflects knowledge-graph embedding similarity only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Schizotypal Personality Disorder |
| TxGNN Prediction Score | 99.9972% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

*(Original Indication is omitted from this table — it is not recorded in the evidence pack; see below.)*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (flagged as a Blocking/High-severity data gap). No original indication is on file in Taiwan's regulatory record either, since the drug is currently unregistered (未上市) here. The only mechanistic context present in the evidence pack comes indirectly from the literature and clinical trial titles collected for other predicted indications in this same pack, which consistently describe fluvoxamine as a serotonin reuptake inhibitor historically studied in obsessive-compulsive disorder, panic disorder, and social/generalized anxiety.

For the top-ranked candidate itself — schizotypal personality disorder — there is no clinical trial or published study of any kind linking fluvoxamine to this condition. The model's very high score (99.9972%, TxGNN internal rank 114) reflects graph-embedding similarity to other conditions in TxGNN's knowledge graph, not an observed pharmacological or clinical relationship. As stated in the underlying rationale: this should be treated as a first-pass screening hit only, not a candidate ready for further mechanistic or clinical evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

- **Drug Interactions**: DDI query returned 283 total interactions. Notable **Major**-level interactions include Alosetron, Diethylpropion, Dolasetron, and Bupropion. Numerous **Moderate**-level interactions were also identified, including Rabeprazole, Clarithromycin, Acetylsalicylic acid, and several corticosteroids (Hydrocortisone, Betamethasone, Budesonide, Dexamethasone, Triamcinolone). Given the scale of the interaction profile (283 total), a full DDI screen against the patient's concurrent medications is required before any clinical use.

Key warnings and contraindications are not available in this evidence pack (TFDA label data not yet collected — see Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (schizotypal personality disorder) has no supporting clinical trials or literature — it is a pure model-score prediction (L5) with no mechanistic corroboration. Combined with missing MOA and TFDA labeling data for the drug itself, there is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) per Data Gap DG001 — currently blocking any safety pre-screen
- Drug mechanism of action (MOA) data per Data Gap DG002, to support a mechanistic-link analysis
- Primary preclinical or clinical research specifically evaluating fluvoxamine (or SSRIs generally) in schizotypal/schizophrenia-spectrum personality disorder, since none currently exists in this pack
- Note: other predicted indications within this same evidence pack — notably **anxiety disorder** (43 trials, 20 publications) and **endogenous depression** (multiple trials and publications including direct fluvoxamine-vs-comparator RCTs) — carry substantially stronger evidence bases and may warrant separate, higher-priority evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

