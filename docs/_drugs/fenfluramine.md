---
layout: default
title: Fenfluramine
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
monitor_inn: "Fenfluramine"
predicted_indications: ["proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "obsolete hypertelorism (disease)", "frontorhiny"]
description: "Fenfluramine: predicted new indication Proximal 16p11.2 microdeletion syndrome (evidence level L5). In India: 1 listed product (1 not discontinued)"
---

# Fenfluramine
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

## Fenfluramine: Proximal 16p11.2 microdeletion syndrome
{: .text-alpha }

## One-Sentence Summary

Fenfluramine was originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **proximal 16p11.2 microdeletion syndrome**,
but **no clinical trials or publications** currently support this prediction, so it is a model-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Proximal 16p11.2 microdeletion syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fenfluramine: "The precise mechanism by which fenfluramine exerts its therapeutic effects in the treatment of seizures associated with Dravet syndrome and Lennox-Gastaut syndrome is unknown. Fenfluramine and the metabolite, norfenfluramine, exhibit agonist activity at serotonin 5-HT2 receptors." ([DailyMed: Fintepla (fenfluramine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d), label version 2026-10-22; accessed 2026-11-19.) Based on known information, fenfluramine is a serotonergic agent that is understood to release serotonin and act on 5-HT receptors. Its efficacy in obesity was the basis of its original use, and it has also been used in seizure disorders.

The 16p11.2 deletion is associated with obesity and with neurodevelopmental and epilepsy phenotypes. This overlaps with both fenfluramine's original obesity use and its use in seizure disorders, which may explain the high model score.

This link is plausible but unverified. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be treated as clinical evidence or proof of efficacy.

Other predictions from the model (hypervitaminosis, hypertelorism, frontorhiny) show no identifiable mechanistic link to fenfluramine and are likely network artifacts or data-quality issues. They are not pursued in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 176203 | Ponderax 20mg Tablet (Serdia Pharmaceuticals India Pvt Ltd) | Strip of 10 tablets (oral) | Not specified |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (model-derived associations, not label text): hypertension, pulmonary hypertension, substance abuse/dependence, type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, glaucoma.
- **Drug Interactions**: 303 interactions are recorded. Major-level examples include:
  - Fentanyl, alfentanil and tramadol (opioids)
  - Dextromethorphan
  - Almotriptan

  Moderate-level examples include antidiabetic agents (acarbose, alogliptin, pioglitazone, albiglutide), NSAIDs (ibuprofen, ketorolac), codeine, dihydrocodeine, salbutamol, formoterol and ethanol.

Please also refer to the package insert for full warnings and contraindications, as label-based safety text was not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9993), but it is a model prediction only, with no clinical trials or literature (Evidence Level L5). The proposed serotonergic link to 16p11.2 microdeletion syndrome remains hypothetical.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications for the India-marketed product
- A literature and trial search specific to fenfluramine in 16p11.2 microdeletion syndrome
- A review of the cardiovascular and pulmonary hypertension risks, given the contraindication signals and the serotonergic mechanism
- Assessment of route and formulation compatibility for the proposed indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fintepla (fenfluramine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

