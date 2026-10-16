---
layout: default
title: Sodium Acetate
parent: Model Prediction Only (L5)
nav_order: 777
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sodium Acetate: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: No approved indication text available in the registration data"
---

# Sodium Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sodium Acetate: From an Electrolyte and Alkalinizing Agent to Congenital Prothrombin Deficiency

## One-Sentence Summary

Sodium acetate is an electrolyte and alkalinizing agent, supplying sodium and an acetate/bicarbonate source, and it is marketed in India as an infusion product.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it.
Overall evidence is very weak, and the prediction currently looks like a network artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text available in the registration data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium acetate is an electrolyte replenisher and alkalinizing agent. It supplies sodium and acetate, which the body converts to bicarbonate.

Congenital prothrombin deficiency is a rare inherited bleeding disorder caused by missing or defective coagulation factor II. Sodium acetate has no known role in the synthesis or function of factor II, so no plausible mechanistic link can be identified. The high TxGNN score appears to come from the graph structure and is not backed by clinical or literature evidence.

Other predictions in the top 10 (for example epiglottitis, urinary tract infection, sclerosing cholangitis, Ureaplasma and gonococcal urethritis, uterine inflammatory disease and xanthogranulomatous pyelonephritis) show the same pattern. None has a supportable mechanism or clinical evidence. For dyspepsia and gastroparesis, the retrieved papers only concern gastric emptying tests that use 13C-labelled acetate as a diagnostic tracer. They do not show a therapeutic effect of sodium acetate.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 202754 | Sodium Lactate 5% Infusion (Albert David Ltd) | Bottle of 500 ml infusion | Not stated |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph-derived disease associations, not label text): kidney disease (including chronic kidney disease, chronic renal failure and end-stage renal failure), anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, hypercalcemia (including humoral hypercalcemia of malignancy), sarcoidosis, heart disease and cardiovascular disease, atrioventricular block, ventricular fibrillation, digitalis poisoning, hyperkalemic periodic paralysis, hypoaldosteronism, myotonia congenita, phenylketonuria and other phenylalanine metabolism disorders, and phosphorus metabolism disease.
- **Drug Interactions**: 30 interactions were identified in total; the 20 detailed in the compiled data are mostly Moderate or Minor.
  - **Moderate:** doxycycline, tetracycline, minocycline, acetylsalicylic acid, choline salicylate, ephedrine, pseudoephedrine, amphetamine, dextroamphetamine, benzphetamine, methenamine
  - **Minor:** sulfonylureas (chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide), memantine, methotrexate

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score. There are no clinical trials or relevant literature, no plausible mechanism, and no approved indication text in the registration data. The graph-derived contraindications involving kidney and cardiac disease add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank to allow a proper mechanistic-link analysis
- Any preclinical or clinical evidence linking acetate to coagulation factor II biology
- Reassessment of whether lower-ranked predictions (for example urinary alkalinization in urinary tract infection) merit evaluation, given that none currently has supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

