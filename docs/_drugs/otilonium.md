---
layout: default
title: Otilonium
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Otilonium: predicted new indication Hypertrichosis (evidence level L5). Approved use: Not stated in the licence data compiled for this report (the drug is…"
monitor_inn: "Otilonium"
predicted_indications: ["hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "polyp of vocal cord", "polyp of middle ear", "uterine polyp", "polyp of external auditory canal", "polyp of frontal sinus"]
---

# Otilonium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Otilonium: From Gastrointestinal Spasm (Antispasmodic Use) to Hypertrichosis

## One-Sentence Summary

Otilonium is a gut-selective antispasmodic marketed in India in several tablet products.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **no clinical trials and no publications** supporting this prediction.
It is a model-only prediction, and the pharmacology does not offer a plausible explanation for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (the drug is known as an antispasmodic) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Otilonium is a quaternary ammonium antispasmodic that acts locally in the gut. It blocks L-type and T-type calcium channels, has antimuscarinic activity (M1/M2/M4/M5), and antagonises tachykinin NK2 receptors. Because it is a quaternary ammonium compound, very little is absorbed into the bloodstream. Detailed mechanism data were not formally available in the data compiled for this report, so this description reflects the pharmacological assessment attached to the prediction.

On that basis, **the prediction is not well supported.** Nothing in this pharmacology connects to hair follicle biology or hair growth regulation. The high score (0.989) most likely reflects the structure of the knowledge graph, such as proximity to related disease terms, rather than real biology.

The other top-ranked predictions show the same pattern. All have a score above 98.5%, all are Evidence Level L5, and none has trials or literature:

- Dandy-Walker malformation syndrome
- Ambras-type hypertrichosis universalis congenita
- Malformation syndromes with a dental or periodontal component
- Isolated genetic hair shaft abnormality
- Polyps of the vocal cord, middle ear, uterus, external auditory canal and frontal sinus

Most of these are congenital or developmental disorders, or inflammatory or hormone-driven lesions. A gut-restricted, poorly absorbed antispasmodic has no known way to act on them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 162545 | Obgram 40 Tablet | Strip of 10 tablets | Not stated |
| 34675 | Colirid Tablet | Strip of 10 tablets | Not stated |
| 164936 | OB 40mg Tablet | Strip of 10 tablets | Not stated |
| 133610 | Menoctyl Tablet | Strip of 10 tablets | Not stated |
| 133734 | Menoctyl Tablet | Strip of 15 tablets | Not stated |

All five registrations are valid single-ingredient oral tablets. None has been cancelled.

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug-interaction data were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and there is no plausible mechanistic link between a gut-restricted antispasmodic and hypertrichosis or the other predicted conditions. The same holds for all ten top predictions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's website, which are required before any safety screening
- Approved indication text for the five registered products
- Formal mechanism-of-action data from DrugBank
- A biological rationale for hair growth effects, with preclinical evidence, before any further investment
- An assessment of whether a poorly absorbed oral drug could reach the target tissue at all (route compatibility is still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

