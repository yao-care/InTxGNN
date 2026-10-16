---
layout: default
title: Allantoin
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Allantoin: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Psoriasis, parapsoriasis, seborrheic dermatitis, pityriasis simplex…"
monitor_inn: "Allantoin"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial", "exanthem (disease)"]
---

# Allantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Allantoin: From Psoriasis and Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Allantoin is a topical dermatologic agent, originally used for skin conditions such as psoriasis, seborrheic dermatitis and dermatitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, seborrheic dermatitis, pityriasis simplex, dermatitis, seborrheic keratosis (from the knowledge graph; no approved indication text on the Indian licenses) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, allantoin is a topical keratolytic, wound-healing and anti-irritant agent. Its use in inflammatory and scaling skin conditions is established, but there is no documented mechanistic connection to diabetic retinopathy.

The prediction is therefore weak. Diabetic retinopathy is a retinal microvascular disease, while allantoin is used on the skin and is not expected to reach the retina in relevant amounts. The high score (99.56%) reflects proximity in a knowledge graph, not clinical or biological evidence.

Other predictions from the model were also reviewed. They are all supported by no trials or literature:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Acrodermatitis chronica atrophicans | 99.50% | Caused by Borrelia infection, which allantoin does not treat |
| 3 | Neonatal dermatomyositis | 99.48% | Immune-mediated; no immunomodulatory mechanism documented; neonatal safety unevaluated |
| 4 | Acne keloid | 99.48% | Most biologically plausible, given allantoin's use in scar care and wound healing, but unsupported by data |
| 5 | Childhood secondary interstitial lung disease with connective tissue disease | 99.44% | No plausible link to a topical skin agent |
| 6 | Amyopathic dermatomyositis | 99.43% | Autoimmune; topical symptomatic care conceivable only |
| 7 | Hydroa vacciniforme, familial | 99.23% | Soothing effect loosely related; no photoprotective activity shown |
| 8 | Exanthem | 99.10% | Too broad to define a repurposing hypothesis |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 218715 | Trioclin Gel | Gel (15 g tube) | Not stated |
| 174331 | Paknet-C Gel | Gel (15 g tube) | Not stated |
| 95593 | Glintra Gel | Gel (30 g tube) | Not stated |
| 84965 | F Next Dusting Powder | Dusting powder (75 g box) | Not stated |
| 34860 | Candid Gold Dusting Powder | Dusting powder (100 g bottle) | Not stated |

Eleven valid single-ingredient registrations are on file in total; all are topical or dusting-powder products. Only the first five are listed here.

## Safety Considerations

The knowledge graph links allantoin to the following conditions as contraindications. This is graph-derived information, not label text:

- **Contraindication-linked conditions**: porphyria (including inherited porphyria and porphyrin metabolism disease), kidney disease, pyoureter, hematologic disease, liver disease, gallbladder disease, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, folliculitis, seborrheic dermatitis, dermatitis

Some of these (seborrheic dermatitis, dermatitis) overlap with the original indications, which suggests the graph edges should be interpreted cautiously.

No drug interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for severe nonproliferative diabetic retinopathy has no clinical trial or literature support, no established mechanism, and no plausible route of retinal exposure from topical use. It remains at Evidence Level L5 (model prediction only). The same applies to all other predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data for allantoin (e.g., from DrugBank)
- A mechanistic rationale and route-of-administration assessment for the retina
- Preclinical or literature evidence for any predicted indication
- If a lead is pursued, acne keloid is the most plausible dermatologic candidate and should be examined first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

