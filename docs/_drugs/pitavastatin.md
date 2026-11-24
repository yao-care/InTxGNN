---
layout: default
title: Pitavastatin
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 4
monitor_inn: "Pitavastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-11-24
description: "Pitavastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Familial combined hyperlipidaemia"
---

# Pitavastatin
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

## Pitavastatin: From Familial Combined Hyperlipidaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Pitavastatin is a statin (cholesterol-lowering drug). It is marketed in this country with 20 valid licences.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, with a very high score.
However, **no clinical trials and no publications** in the data compiled for this report support this specific pairing, so the prediction is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Familial combined hyperlipidaemia (relation recorded in the knowledge graph; the licence records contain no approved-indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pitavastatin: "Pitavastatin is an inhibitor of 3-hydroxy-3-methylglutaryl-coenzyme A (HMG-CoA) reductase, the enzyme that catalyzes the conversion of HMG-CoA to mevalonate, a rate-limiting step in the biosynthetic pathway for cholesterol. As a result, the expression of LDL-receptors followed by the uptake of LDL from blood to liver is accelerated and then the plasma TC decreases." ([DailyMed: Livalo (pitavastatin calcium) prescribing information, Kowa Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44dcbf97-99ec-427c-ba50-207e0069d6d2), label version 2026-03-31; accessed 2026-11-19.) Pitavastatin belongs to the statin class, which lowers LDL cholesterol by inhibiting HMG-CoA reductase. Its recorded link is to inherited lipid disorders, so a connection to another inherited lipid-metabolism condition is biologically adjacent.

CETP deficiency is a genetic condition marked by high HDL cholesterol and altered lipoprotein metabolism. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a demonstrated therapeutic need. CETP deficiency is generally not associated with raised cardiovascular risk that would call for statin treatment, and the mechanistic link is therefore weak. No trial or publication supports the pairing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

The compiled data lists at least 20 valid licences for pitavastatin-containing products, and the list may be partial. None of the records include approved-indication text. Several products are fixed-dose combinations, so the table below shows only products that appear to be single-ingredient pitavastatin.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 64399 | Diabastat 4 Tablet | Strip of 10 tablets | Valid |
| 78681 | Ezenon-P4 Tablet | Strip of 10 tablets | Valid |
| 126527 | Livastat 4 Tablet | Strip of 10 tablets | Valid |
| 173897 | Pivasta 2 Tablet | Strip of 10 tablets | Valid |
| 174138 | Pivasta 4 Tablet | Strip of 10 tablets | Valid |
| 175394 | Pitava 2mg Tablet | Strip of 10 tablets | Valid |
| 176597 | Pitavamed 4mg Tablet | Strip of 10 tablets | Valid |
| 177475 | Pitsafe-FB Tablet | Strip of 10 tablets | Valid |
| 178242 | Ptvs Plus 2mg/10mg Tablet | Strip of 10 tablets | Valid |
| 178717 | Pitava 1mg Tablet | Strip of 10 tablets | Valid |
| 178965 | Pitamed-EZ Tablet | Strip of 10 tablets | Valid |
| 179208 | Pitsafe 4 Tablet | Strip of 10 tablets | Valid |
| 179529 | Pitamed 4 Tablet | Strip of 10 tablets | Valid |
| 179662 | Pitsafe-Plus Tablet | Strip of 10 tablets | Valid |
| 179727 | Ptvs 2mg Tablet | Strip of 10 tablets | Valid |
| 179844 | Pivastin 2 Tablet | Strip of 10 tablets | Valid |
| 180569 | Pivasta F 2mg/135mg Capsule DR | Strip of 10 Capsule DR | Valid |
| 181400 | Pevastin 2mg Tablet | Strip of 10 tablets | Valid |
| 182234 | Pitezo 2mg Tablet | Strip of 10 tablets | Valid |
| 237075 | Vytoz-F Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The following conditions are linked to pitavastatin as contraindications: liver disease, gallbladder disease, hypothyroidism (including myxedema and congenital hypothyroidism), myopathy and other muscle diseases, familial periodic paralysis, hypotensive disorder, rhabdomyolysis, nodular fasciitis, impaired renal function, and injury.
- **Drug interactions:** 86 interactions are recorded in total. The one rated Major is **erythromycin**. Examples rated Moderate include rosuvastatin, simvastatin, cobicistat, eltrombopag, metronidazole, chloroquine, hydroxychloroquine, naltrexone and ethanol. Warfarin and dicoumarol are rated Minor.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no trials or publications for this disease, and the mechanistic link is weak because CETP deficiency does not usually call for statin therapy.

**To proceed, the following is needed:**
- Evidence that CETP deficiency carries a clinical risk or lipid problem that a statin would address
- Detailed mechanism-of-action data for pitavastatin
- Package insert warnings and contraindications from the Indian licence holders
- Genetic and clinical validation, such as a pilot study or a review of existing patient cohorts

**Note on other candidates:** Among the other predictions for this drug, **HIV infectious disease** has substantial supporting evidence, including a published randomised trial (REPRIEVE) and several follow-up studies. That benefit is primary prevention of cardiovascular disease in people with HIV, not treatment of the infection itself. It could be evaluated as a separate report, with attention to interactions with antiretrovirals.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Livalo (pitavastatin calcium) prescribing information, Kowa Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44dcbf97-99ec-427c-ba50-207e0069d6d2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

