---
layout: default
title: Metaxalone
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Metaxalone: predicted new indication Infectious otitis media (evidence level L5). Approved use: Not stated in the data compiled for this report (metaxalone is genera…"
monitor_inn: "Metaxalone"
predicted_indications: ["infectious otitis media", "endocarditis", "endocardial fibroelastosis"]
---

# Metaxalone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Metaxalone: From Skeletal Muscle Relaxation to Infectious Otitis Media

## One-Sentence Summary

Metaxalone is a centrally acting skeletal muscle relaxant that is marketed in India as a single-ingredient oral tablet.
The TxGNN model predicts it may be effective for **infectious otitis media**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (metaxalone is generally known as a skeletal muscle relaxant) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metaxalone is a centrally acting skeletal muscle relaxant, and its exact mechanism is incompletely characterized.

The review of the prediction found no established mechanistic link to infectious otitis media. Metaxalone has no known antimicrobial, anti-inflammatory, or Eustachian tube-related activity. The high score (99.06%) is a graph-based computational prediction only and is not backed by any trial or literature evidence.

Two other predictions were also generated, and neither is supported by evidence:
- **Endocarditis** (score 99.02%): no plausible mechanistic link, because infective endocarditis is treated with targeted antimicrobial therapy and metaxalone has no antibacterial or cardiac-specific activity.
- **Endocardial fibroelastosis** (score 99.00%): no identified mechanistic link, and pediatric safety data for metaxalone are limited.

All three predictions are rated L5 and Hold.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84259 | Flexura 400 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets (oral) | Not stated |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): liver failure, acute liver failure, hepatitis, hemolytic anemia.
- **Drug Interactions**: 53 interactions are recorded. The Major-level ones among those listed are:
  - Morphine (including liposomal morphine)
  - Codeine
  - Hydrocodone

  Moderate-level interactions include:
  - Cannabinoids (dronabinol, nabilone)
  - Naltrexone
  - Metoclopramide
  - Opium
  - Sibutramine
  - Ethanol
  - Sedating antihistamines (promethazine, chlorpheniramine, cetirizine, brompheniramine, carbinoxamine, clemastine, mepyramine, doxylamine)
  - Dextromethorphan

  Many of these are central nervous system depressants, so additive sedation is a likely concern.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score. There are no clinical trials or publications, no mechanistic link to otitis media, and the package insert safety data are missing. The evidence level is L5.

**To proceed, the following is needed:**
- The India package insert (warnings, contraindications, approved indication), obtained from the India Pharma website. This is currently a blocking gap for safety screening.
- Mechanism of action data for metaxalone from DrugBank, to allow a mechanistic-link analysis.
- Any preclinical or clinical evidence linking metaxalone to infectious otitis media. Without it, the prediction should not advance.
- A review of the knowledge-graph liver-related contraindication signals and the CNS-depressant interactions if the project is reconsidered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

