---
layout: default
title: Mephentermine
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Mephentermine: predicted new indication Postural orthostatic tachycardia syndrome (evidence level L5). Approved use: Hypotensive disorder"
monitor_inn: "Mephentermine"
predicted_indications: ["postural orthostatic tachycardia syndrome", "sinoatrial node disease", "sinoatrial block", "variably protease-sensitive prionopathy"]
---

# Mephentermine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Mephentermine: From Hypotensive Disorder to Postural Orthostatic Tachycardia Syndrome
{: .text-alpha }

## One-Sentence Summary

Mephentermine is an indirect sympathomimetic originally used to treat low blood pressure (hypotensive disorder).
The TxGNN model predicts it may be effective for **postural orthostatic tachycardia syndrome (POTS)**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypotensive disorder (the registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Postural orthostatic tachycardia syndrome |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 6 of 6) |
| Number of Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, mephentermine is an indirect sympathomimetic that releases endogenous norepinephrine and has alpha- and beta-adrenergic effects. This raises blood pressure and vascular tone, which is why it is used for low blood pressure.

In POTS, standing up causes blood to pool in the lower body and the heart rate rises sharply. Raising vascular tone could, in theory, counter the pooling and the orthostatic blood pressure component. This is the main reason the prediction looks plausible.

However, the same mechanism is likely to push the heart rate higher, and a rapid heart rate is the defining feature of POTS. The net effect is therefore uncertain and could be harmful. The high score of 0.9984 is a computational prediction only, and no trials or literature were found to back it up.

Other lower-ranked predictions were also generated, but they are weaker:
- **Sinoatrial node disease** (score 0.9933) and **sinoatrial block** (score 0.9933): a stimulant of heart rate might theoretically help a slow heartbeat, but it carries arrhythmia risk and established treatments are better supported. These two predictions are likely correlated and add little independent support.
- **Variably protease-sensitive prionopathy** (score 0.9911): no plausible mechanistic link was identified, and this is likely a false positive.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 214828 | Termin 30mg Injection | Vial of 10 ml injection | Not stated in the data compiled |
| 216311 | Termin 15mg Injection | Vial of 1 ml injection | Not stated in the data compiled |
| 136078 | Mephentine 15mg Injection | Vial of 1 ml injection | Not stated in the data compiled |
| 133933 | Mephentine 30mg Injection | Vial of 10 ml injection | Not stated in the data compiled |
| 179666 | Phentin 15mg Injection | Vial of 1 ml injection | Not stated in the data compiled |

A sixth valid single-ingredient registration (216899, Termiva Injection, vial of 10 ml) is also on record. All six registrations are injectable products, and none is cancelled.

## Safety Considerations

- **Drug Interactions**: 64 interactions are recorded. All of those reviewed are rated Moderate. They mainly involve:
  - Diabetes medicines: acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, insulins (aspart, degludec, detemir, glargine)
  - GLP-1 and DPP-4 agents: albiglutide, dulaglutide, semaglutide, lixisenatide, alogliptin, linagliptin
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - Other stimulant or appetite-suppressant drugs: phentermine, diethylpropion
- **Cardiac caution**: As a sympathomimetic, mephentermine carries a risk of arrhythmia and rapid heart rate. This matters for all of the predicted indications, particularly POTS and sinoatrial conditions.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or literature (evidence level L5). The drug's likely effect of raising heart rate conflicts with the core feature of POTS, so benefit is uncertain and harm is possible. Package insert safety information is also still missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator or manufacturer (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank to allow a proper mechanistic analysis
- Approved indication text for the registered products
- A literature and clinical trial search for sympathomimetics in POTS to see whether any supporting or opposing evidence exists
- A cardiac safety assessment (heart rate and arrhythmia risk) before any exploratory study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

