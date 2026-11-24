---
layout: default
title: Dalteparin
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 5
monitor_inn: "Dalteparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
last_modified_at: 2026-11-24
description: "Dalteparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). In India: 10 listed products (10 not discontinued)"
---

# Dalteparin
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

## Dalteparin: low-molecular-weight heparin (factor Xa inhibitor) → thrombophilia due to protein C deficiency, autosomal recessive
{: .text-alpha }

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin that potentiates antithrombin and inhibits factor Xa.
The TxGNN model predicts it may be relevant to **thrombophilia due to protein C deficiency, autosomal recessive**, with a score of 0.9988.
No clinical trials or publications directly studying this disease are available, so the support is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (10 of 10) – CDSCO approval status is not included in this data |
| Number of Listed Products | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dalteparin: "Dalteparin is a low molecular weight heparin with antithrombotic properties. It acts by enhancing the inhibition of Factor Xa and thrombin by antithrombin. In humans, dalteparin potentiates preferentially the inhibition of coagulation Factor Xa, while only slightly affecting the activated partial thromboplastin time (APTT)." ([DailyMed: Fragmin (dalteparin sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=23527b8b-9b28-4e6d-9751-33b143975ac7), label version 2025-09-30; accessed 2026-11-19.) Dalteparin is known as a low-molecular-weight heparin: it enhances antithrombin activity and inhibits factor Xa, which reduces clot formation.

Protein C deficiency removes an important natural brake on coagulation and produces a prothrombotic state. An anticoagulant is therefore biologically plausible in this setting, particularly in the severe homozygous form, which can cause purpura fulminans.

This is still only a plausible link. Standard management relies on protein C replacement together with anticoagulation, so any role for dalteparin would need to be defined by a dedicated review. The score is a model output, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered for this disease.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 62004 | Daltehep 5000IU Injection | Vial of 2 ml Injection | Valid |
| 63739 | Daltehep 2500IU Injection | Vial of 2 ml Injection | Valid |
| 64642 | Daltehep 10000IU Injection | Vial of 10 ml Injection | Valid |
| 65716 | Daltepin 10000IU Injection | Vial of 1 ml Injection | Valid |
| 67438 | Daltepin 5000IU Injection | Vial of 1 ml Injection | Valid |
| 67675 | Dalpin 2500IU Injection | Vial of 1 ml Injection | Valid |
| 67971 | Daltepin 2500IU Injection | Vial of 1 ml Injection | Valid |
| 84330 | Fragmin 5000IU Injection | Prefilled syringe of 0.2 ml Solution for Injection | Valid |
| 84416 | Fragmin 2500IU Injection | Prefilled syringe of 0.2 ml Solution for Injection | Valid |
| 85639 | Fragmin 10000IU Injection | Prefilled syringe of 1 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All 10 licences are single-ingredient products and currently valid.

## Safety Considerations

- **Drug Interactions**: 174 interactions are recorded. Major-level examples include acetylsalicylic acid, ibuprofen, ketorolac, fondaparinux, abciximab, acalabrutinib, deferasirox and trastuzumab emtansine. These mostly reflect additive bleeding risk. Moderate-level examples include fluvoxamine, fosinopril, sibutramine and sugammadex.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but there are no trials or publications for protein C deficiency, so the evidence is limited to model prediction (L5). Established treatment (protein C replacement plus anticoagulation) already exists.

**To proceed, the following is needed:**
- A focused literature review of LMWH use in severe congenital protein C deficiency
- Mechanism of action data and package insert warnings and contraindications
- Defined dosing and safety considerations for bleeding risk and for patients with renal impairment

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fragmin (dalteparin sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=23527b8b-9b28-4e6d-9751-33b143975ac7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

