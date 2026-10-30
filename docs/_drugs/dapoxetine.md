---
layout: default
title: Dapoxetine
parent: Model Prediction Only (L5)
nav_order: 231
evidence_level: L5
indication_count: 3
monitor_inn: "Dapoxetine"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-30
description: "Dapoxetine: predicted new indication migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Dapoxetine
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

## Dapoxetine: selective serotonin reuptake inhibitor (SSRI) → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Dapoxetine is a short-acting selective serotonin reuptake inhibitor (SSRI) that is marketed in India under a number of single-ingredient licences.
The TxGNN model predicts it may be useful for **migraine disorder**, but there are **no registered clinical trials** and **no publication that directly studies dapoxetine in migraine**, so the prediction rests on the model score and an indirect mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Pharmacology data show that dapoxetine acts on the serotonin transporter (SERT, gene SLC6A4) and is a short-acting SSRI.

Serotonergic dysregulation is implicated in migraine, and some serotonergic agents and SSRIs have been explored for migraine prevention. This gives a plausible but indirect rationale for the prediction. One review of off-label SSRI uses covers migraine among many other conditions, but it concerns the SSRI class in general and not dapoxetine.

There are also practical concerns. Dapoxetine is designed for short-acting, on-demand dosing, whereas migraine prevention usually needs chronic daily dosing. The very high score is a computational output only and should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Review | Current Neuropharmacology | Review of off-label uses of SSRIs as a class, with migraine among the conditions covered; not specific to dapoxetine |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohort | Urologia | Treatment compliance with dapoxetine in premature ejaculation; not related to migraine |

Neither publication directly studies dapoxetine in migraine disorder.

## India Market Information

The data list 20 valid single-ingredient licences and none cancelled; the list may be partial. The licence records carry no approved-indication text. Main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26353 | Bold Care 30 Tablet | Strip of 4 tablets | Not recorded |
| 11465 | Amjoy 60mg Tablet | Strip of 4 tablets | Not recorded |
| 120971 | Long Drive 30mg Tablet | Strip of 4 tablets | Not recorded |
| 60135 | Duraject 30mg Tablet | Strip of 2 tablets | Not recorded |
| 58268 | Duralast 30 Tablet | Strip of 4 tablets | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information.

Pharmacology data identify SERT as the target of dapoxetine. No specific drug-interaction records with other drugs are available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a high model score and an indirect serotonergic rationale. No trial or publication directly addresses dapoxetine in migraine, and its on-demand, short-acting profile does not fit the chronic prophylactic dosing usually needed for migraine.

**To proceed, the following is needed:**
- Dapoxetine-specific preclinical or clinical data in migraine
- Mechanism-of-action data from DrugBank to support the mechanistic link
- Package insert warnings and contraindications from the India licence holders
- Assessment of whether a dosing regimen suitable for migraine prevention is feasible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

