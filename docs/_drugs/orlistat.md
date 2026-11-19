---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 622
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder, monogenic obesity"
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Orlistat: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Orlistat is a gastric and pancreatic lipase inhibitor originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but **no clinical trials and no publications** were found in the data compiled for this report. The prediction rests on model output and pharmacological reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder, monogenic obesity (the approved-indication text in the India licence records is blank) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for orlistat: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), label version 2026-09-30; accessed 2026-11-19.) Based on known pharmacology, orlistat inhibits gastric and pancreatic lipases and reduces dietary fat absorption by roughly 30%. This is how it helps with weight loss in obesity.

The link to the new indication is indirect. Fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat. Less fat absorption could therefore lower their uptake, which is a plausible way of reducing vitamin burden in hypervitaminosis, especially for vitamins A and D.

This reasoning has important limits:
- It is inferred from pharmacology only. No study in the compiled data tests orlistat as a treatment for vitamin excess.
- Reduced absorption of fat-soluble vitamins is a known **adverse effect** of orlistat in its approved use, not a recognised benefit.
- Hypervitaminosis from supplement overuse is normally managed by stopping the supplement, so the case for adding a drug is unclear.
- The high TxGNN score (0.9942) is a computational prediction, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty valid single-ingredient registrations exist in India. Five are listed below. All are oral forms, and no approved-indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 87617 | Finostat 60mg Capsule | Strip of 10 capsules | Cubit Healthcare |
| 108993 | Ishape 60mg Capsule | Strip of 10 capsules | Primus Pharmaceuticals |
| 108568 | Ishape 120mg Capsule | Strip of 10 capsules | Primus Pharmaceuticals |
| 232244 | Ultislim 120mg Tablet | Strip of 10 tablets | Akumentis Healthcare Ltd |
| 167365 | Orli-Misia 120mg Tablet | Strip of 10 tablets | Concord Drugs Ltd |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease relationships, not label text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, drug-induced liver injury.
  - The flag for **vitamin deficiency disorder** is directly relevant here. Orlistat can reduce absorption of fat-soluble vitamins, so using it in a vitamin-excess setting carries a risk of overshooting into deficiency.
- **Drug Interactions**: 314 interactions are recorded. Examples include:
  - Moderate: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptin, canagliflozin, metformin, chlorpropamide, amiodarone, cannabidiol, clofarabine, brentuximab vedotin, asparaginase products, calaspargase pegol.
  - Minor: cholecalciferol, calcifediol, calcitriol.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and a pharmacological inference, with no clinical trials or publications. The proposed mechanism is also the cause of a known adverse effect of orlistat, and hypervitaminosis already has a simple management route (stopping the supplement).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's records
- Detailed mechanism-of-action data from DrugBank
- A literature and trial search for orlistat in vitamin A or D excess, including case reports
- Evidence that orlistat adds benefit over stopping the supplement, and a clear target population
- A safety plan addressing vitamin deficiency risk, liver and cholestasis contraindications, and interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data from the source database is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

