---
layout: default
title: Vildagliptin
parent: Model Prediction Only (L5)
nav_order: 889
evidence_level: L5
indication_count: 9
monitor_inn: "Vildagliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-30
description: "Vildagliptin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Vildagliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Vildagliptin is an oral DPP-4 inhibitor used to manage type 2 diabetes mellitus.
The TxGNN model (deep learning) predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly studying this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Vildagliptin is known as a selective inhibitor of dipeptidyl peptidase-4 (DPP-4), which raises active incretin hormones (GLP-1, GIP) and enhances glucose-dependent insulin secretion. Pharmacology records also list DPP-4, DPP-8, DPP-9 and TRPV4 as targets.

The link to stiff person syndrome is weak. Stiff person syndrome is an autoimmune neurological disorder involving anti-GAD65 antibodies and impaired GABAergic signalling. DPP-4 inhibition might theoretically modulate immune or incretin pathways, but no supporting data exist. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the overlap of anti-GAD autoimmunity with autoimmune diabetes, not biological evidence or a true therapeutic effect.

The same applies to other top-ranked predictions (focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and several lipodystrophy conditions). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; they have no trial or literature support. Pancreatic agenesis (rank 9) is biologically implausible, since there is no functional pancreatic tissue for the drug to act on.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

(For reference, the only publications retrieved in the compiled data relate to a lower-ranked prediction, pancreatic agenesis, and none supports a benefit: two general reviews of DPP-4 inhibitors in type 2 diabetes, one animal study of a different drug, and one case report of probable vildagliptin-associated acute pancreatitis.)

## India Market Information

At least 20 valid single-ingredient licences are recorded (the list may be partial). The licence records contain no approved-indication text. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 233750 | Vildanex 50mg Tablet | Strip of 15 tablets | Not stated in licence record |
| 236907 | Venna 100mg Tablet SR | Strip of 10 SR tablets | Not stated in licence record |
| 233613 | Vilnip Tablet | Strip of 15 tablets | Not stated in licence record |
| 238614 | Vildamence 50mg Tablet | Strip of 15 tablets | Not stated in licence record |
| 235163 | Vildalor 50mg Tablet | Strip of 10 tablets | Not stated in licence record |

## Safety Considerations

- **Drug Interactions**: Pharmacology records list interactions at the target level (DPP-4, DPP-8, DPP-9, TRPV4), with no graded drug-drug interactions.
- **Related literature signal**: A 2026 case report describes probable vildagliptin-associated acute pancreatitis in a patient with type 2 diabetes. The link between DPP-4 inhibitors and pancreatitis remains controversial.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. No clinical trials or publications address classic stiff person syndrome, and no mechanistic link is supported, so the evidence level is L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the licence holders
- Preclinical or mechanistic studies testing DPP-4 inhibition in stiff person syndrome models or anti-GAD65 autoimmunity
- Review of whether the TxGNN model (deep learning) score simply reflects similarities the model learned between related diseases, such as anti-GAD overlap with autoimmune diabetes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

