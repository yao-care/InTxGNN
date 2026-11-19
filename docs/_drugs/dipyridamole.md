---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 6
monitor_inn: "Dipyridamole"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-11-03
description: "Dipyridamole: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). In India: 6 listed products (6 not discontinued)"
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is a long-established antiplatelet medicine that is marketed in India.
The TxGNN model predicts it may be relevant to **sick sinus syndrome 2, autosomal dominant**, a rare inherited heart-rhythm disorder.
Currently **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dipyridamole: "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), label version 2026-04-29; accessed 2026-11-19.) Dipyridamole is generally understood to inhibit platelet aggregation and to raise extracellular adenosine by blocking its cellular uptake. It also has vasodilating effects.

The model gives this prediction a very high score, but the data compiled for this report show no mechanistic support for it. Adenosine can slow conduction in the sinus node and the atrioventricular node. Higher adenosine levels could therefore worsen sinus node dysfunction rather than treat it. The disease is an inherited channel disorder, likely related to the HCN4 gene. Nothing in the available data suggests that an antiplatelet or adenosine-modulating drug would correct that defect.

The score should be read as a computational signal for further investigation. It is not evidence of benefit, and the plausible direction of effect may be harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Six single-ingredient dipyridamole licences are currently valid in India. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 111097 | Infartin 60 Tablet | Strip of 30 tablets | Jenburkt Pharmaceuticals Ltd |
| 220671 | Thrombonil 75mg Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 176522 | Persantin 100mg Tablet | Strip of 10 tablets | German Remedies |
| 41947 | Cardiwell 75mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 44912 | Cardiwell 100mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |

All listed products are oral tablets.

## Safety Considerations

- **Drug Interactions**: 321 interaction records were found. The ones with a Moderate rating are:
  - dexfenfluramine
  - sibutramine
  - fenfluramine

  Many other records have no severity rating. They include acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, glimepiride, morphine and simvastatin.
- **Rhythm-related concern**: Dipyridamole increases adenosine activity, which may slow sinus and atrioventricular node conduction. This is a theoretical concern in patients with sinus node dysfunction.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score of 0.9989, but there are no clinical trials or publications for this disease. The evidence level is L5. The known adenosine-related effects on the sinus node point toward possible harm rather than benefit.

**To proceed, the following is needed:**
- Mechanistic evidence on whether dipyridamole interacts with HCN4-related sinus node dysfunction, including a safety assessment of its adenosine-mediated effects on conduction
- Preclinical data in a relevant disease model
- Detailed mechanism of action data and package insert warnings and contraindications for the marketed products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

