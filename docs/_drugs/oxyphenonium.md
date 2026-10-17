---
layout: default
title: Oxyphenonium
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Oxyphenonium: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Gastric and duodenal ulcer"
monitor_inn: "Oxyphenonium"
predicted_indications: ["irritable bowel syndrome"]
---

# Oxyphenonium
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

# Oxyphenonium: From an Antispasmodic for Gastric and Duodenal Ulcer to Irritable Bowel Syndrome

## One-Sentence Summary

Oxyphenonium is a quaternary ammonium antimuscarinic (anticholinergic) agent, used in India as an antispasmodic and for gastric and duodenal ulcer.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**,
but at present **no clinical trials and no publications** support this prediction, so it rests on model output and drug-class reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric and duodenal ulcer (from pharmacology reference data; the India licence record has no indication text) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known drug-class information, oxyphenonium is an antimuscarinic agent that blocks muscarinic acetylcholine receptors. Pharmacology reference data list the M4 receptor (CHRM4) as a proposed target, but no publicly available bioactivity data confirm it, so no primary target has been assigned.

Blocking muscarinic receptors in the gut can reduce smooth muscle hypermotility and visceral cramping. These are features of irritable bowel syndrome (IBS), particularly the pain-predominant and diarrhoea-predominant subtypes. Related antimuscarinics such as hyoscine butylbromide, dicyclomine and hyoscyamine have been studied in IBS and showed modest symptom benefit. No data specific to oxyphenonium were available.

The high TxGNN score is a computational prediction only. Class-level anticholinergic effects (dry mouth, constipation, urinary retention, blurred vision) may limit use, especially in constipation-predominant IBS.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2299 | Antrenyl 5mg Tablet (Novartis India Ltd) | Strip of 10 tablets | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one entry, a pharmacological target association (M4 receptor, CHRM4) rather than an interaction with another drug. No graded drug-drug interactions were identified.
- **Class-level effects (inferred, not from a label)**: Anticholinergic adverse effects such as dry mouth, constipation, urinary retention and blurred vision are expected.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score and class-level reasoning. No clinical trials or literature support oxyphenonium in IBS, and package-insert safety data are missing, so the evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Antrenyl, obtained from the manufacturer or regulator (currently a blocking gap for safety screening)
- Detailed mechanism of action and receptor-binding data
- Approved indication text for the India licence
- Literature review of antimuscarinics in IBS to estimate the expected benefit and tolerability of oxyphenonium
- Preclinical or early clinical data specific to oxyphenonium in IBS
- Assessment of formulation and route suitability (the only registered form is an oral tablet)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

