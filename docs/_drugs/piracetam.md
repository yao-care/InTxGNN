---
layout: default
title: Piracetam
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Piracetam: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the available licence data"
monitor_inn: "Piracetam"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "pseudoachondroplasia", "hepatic porphyria", "gout", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "early-onset familial noncirrhotic portal hypertension"]
---

# Piracetam
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

# Piracetam: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Piracetam is a cyclic GABA derivative marketed in India as a single-ingredient product, and the data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials and no publications** currently support this prediction.
It rests on model output alone, so the recommended decision is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Piracetam is described as a cyclic GABA derivative with putative effects on membrane fluidity and on neuronal and platelet function. Pharmacology records in the compiled data show it linked to the AMPA-type glutamate receptor subunits GluA1, GluA2, GluA3 and GluA4 (GRIA1 to GRIA4). Its best-known uses are cognitive enhancement and, in the UK, adjunctive treatment of myoclonus. None of these relates directly to joint disease.

No mechanistic link between piracetam and osteoarthritis is established in the data. The high score probably reflects proximity in the knowledge graph to other joint and musculoskeletal disease nodes, not a demonstrated biological rationale. The model's other top predictions are rheumatoid arthritis, gout, and several rare skeletal dysplasias. They show the same pattern, and all of them also lack supporting studies. This prediction should be treated as a hypothesis for screening, not as evidence of efficacy.

## India Market Information

Piracetam has 20 valid single-ingredient registrations in India and none are cancelled. The licence records contain no approved-indication text. Five representative authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 16967 | Anitam Syrup | Syrup, bottle of 100 ml | Not stated |
| 157765 | Normalite 800mg Tablet | Tablet, strip of 10 | Not stated |
| 156443 | Nutam 400mg Capsule | Capsule, strip of 10 | Not stated |
| 158155 | Neucitam 200mg Injection | Injection, ampoule of 15 ml | Not stated |
| 175326 | Pirament 800 Tablet | Tablet, strip of 10 | Not stated |

Available forms include oral tablets, capsules and syrups, as well as injectables.

## Safety Considerations

- **Drug Interactions**: The interaction screen was completed. It returned four pharmacology records, not clinical drug-drug interactions. They show piracetam acting on the AMPA receptor subunits GluA1, GluA2, GluA3 and GluA4, and no interaction severity levels were assigned.
- **Porphyria**: The prediction list includes hepatic porphyria. Piracetam's safety in porphyria has not been established, so porphyrinogenicity would need to be checked before any further consideration.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for osteoarthritis rests on a model score alone (Evidence Level L5). No clinical trials or literature were found, no mechanistic link is shown, and the original indication and mechanism of action are missing from the data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, which are needed for any safety screening
- Mechanism of action data (for example from DrugBank) to assess a plausible link to osteoarthritis
- The approved indications of the Indian products, to define the original indication
- A systematic search for preclinical or clinical studies of piracetam in osteoarthritis or other joint disease
- A comparison of the available oral and injectable routes with those needed for osteoarthritis treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

