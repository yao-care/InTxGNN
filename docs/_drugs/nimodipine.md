---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 596
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Nimodipine: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid h…"
monitor_inn: "Nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Nimodipine is a calcium channel blocker originally used to treat subarachnoid hemorrhage, including aneurysmal subarachnoid hemorrhage.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid hemorrhage) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (17 of 17) – CDSCO approval status is not included in this data |
| Number of Listed Products | 17 (valid: 17) |
| Recommended Decision | Hold |

Note: The approved indication text is blank in all India registration records compiled for this report, so the original indication above is not taken from those records. Any TxGNN model (deep learning) score may reflect similarities the model learned between related diseases, not biological evidence.

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nimodipine: "Nimodipine is a dihydropyridine calcium channel blocker. The contractile processes of smooth muscle cells are dependent upon calcium ions, which enter these cells during depolarization as slow ionic transmembrane currents." ([DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10), label version 2024-08-30; accessed 2026-11-19.) Based on general pharmacology, nimodipine is a dihydropyridine L-type calcium channel blocker. It is used in subarachnoid hemorrhage to help limit the vascular consequences of the bleed.

Homozygous familial hypercholesterolemia is caused mainly by defects in the LDL receptor pathway (LDLR, APOB, PCSK9, LDLRAP1). The data compiled for this report do not support a direct mechanistic link between nimodipine and this pathway. Some calcium channel blockers have been reported to have minor effects on vascular lipid handling or atherosclerosis in preclinical settings. This connection is indirect and does not address the underlying LDL receptor deficiency.

The very high TxGNN score (0.9929) is a computational prediction only. It is not corroborated by any trial or publication, so it should be treated as a hypothesis to test, not as evidence of benefit.

A second prediction, nephrogenic syndrome of inappropriate antidiuresis (score 0.9905), is also at the model-only stage (L5, Hold). Its link is speculative: calcium signaling plays a role in renal water handling, but there is no evidence that nimodipine acts on the vasopressin V2 receptor pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

There are 17 valid single-ingredient registrations. Five representative ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43926 | Caldip 10mg Infusion | Bottle of 10 infusions | Not stated |
| 151292 | Nimocer 30mg Tablet | Strip of 10 tablets | Not stated |
| 152225 | Nimotide 30mg Tablet | Strip of 6 tablets | Not stated |
| 234530 | Vasotop 30mg Tablet | Strip of 10 tablets | Not stated |
| 236460 | Vasotop 30mg Infusion | Bottle of 50 ml infusion | Not stated |

Both oral tablets and intravenous infusions are available on the market.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, hypotensive disorder.
- **Drug Interactions**: 147 interactions were identified in total. Major-level interactions include:
  - Clarithromycin
  - Dolasetron

  Moderate-level interactions include bupropion, aprepitant, morphine, acetylsalicylic acid, cimetidine, magnesium sulfate, miconazole, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), aminoglycosides (kanamycin, neomycin), and several calcium salts.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or literature (L5), and no plausible direct mechanism links nimodipine to the LDL receptor pathway. Nimodipine is widely marketed in India, but that does not support the new indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator or manufacturers (currently a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic studies testing nimodipine in LDL receptor-deficient models
- A literature and trial search specific to nimodipine and lipid metabolism
- Review of route compatibility and the hypotension risk, since patients with this condition often have cardiovascular disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

