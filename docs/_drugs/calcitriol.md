---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 5
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-20
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). In India: at least 20 listed products"
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Calcitriol: active vitamin D hormone → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active form of vitamin D, a hormone that regulates calcium and phosphate balance.
The TxGNN model predicts it may be relevant for **obsolete vitamin D deficiency**, but **no clinical trials and no publications** directly study this disease in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for calcitriol: "Endogenous synthesis and catabolism of calcitriol, as well as physiological control mechanisms affecting these processes, play a critical role regulating the serum level of calcitriol. Physiological daily production is normally 0.5 to 1.0 mcg and is somewhat higher during periods of increased bone synthesis (eg, growth or pregnancy)." ([DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e), label version 2026-10-15; accessed 2026-11-19.) Calcitriol is the biologically active form of vitamin D (1,25-dihydroxyvitamin D3). It acts on the vitamin D receptor to raise intestinal absorption of calcium and phosphate and to regulate bone mineral metabolism.

Because calcitriol is the active hormone itself, a link to vitamin D deficiency is biologically plausible and likely explains the very high score. However, the disease term is flagged as obsolete, and the prediction largely restates the drug's known physiology rather than offering a novel repurposing signal. In practice, deficiency of the precursor vitamin is usually corrected with native vitamin D, while calcitriol is typically reserved for situations where activation is impaired.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## India Market Information

Calcitriol is marketed in India. The records compiled for this report show 20 valid single-ingredient licences and none cancelled; the list may be partial. The licence records carry no indication text. Available forms:

| Route | Dosage Forms |
|------|------|
| Oral | Strips of 15 or 10 soft gelatin capsules; strips of 10 tablets |
| Injectable | 1 ml ampoule; packet of 6 injections |

## Safety Considerations

- **Drug Interactions** (339 interactions recorded; examples):
  - Major: cholecalciferol, calcifediol, burosumab
  - Moderate: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide), enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butalbital, butabarbital), bile-acid binders (cholestyramine, colesevelam, colestipol), aluminium hydroxide, digoxin and digitoxin, topical calcipotriol

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high score but no supporting trials or literature, and the disease term is obsolete. It restates calcitriol's known physiology rather than a new use, so the evidence level is L5.

**To proceed, the following is needed:**
- Clarify which current disease term replaces the obsolete one (e.g., vitamin D deficiency vs. impaired vitamin D activation)
- Studies directly addressing calcitriol in the target condition
- Mechanism-of-action data and package insert warnings and contraindications
- Calcium, phosphate and PTH monitoring plan, given the hypercalcaemia risk and the major interactions with other vitamin D products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

