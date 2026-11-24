---
layout: default
title: Benzonatate
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Benzonatate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the India license records (the drug is generally known…"
monitor_inn: "Benzonatate"
drugbank_id: DB00868
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
---

# Benzonatate
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

## Benzonatate: From Cough Suppression to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Benzonatate is an oral cough suppressant marketed in India as single-ingredient capsules. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license records (the drug is generally known as a cough suppressant) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for benzonatate: "Benzonatate acts peripherally by anesthetizing the stretch receptors located in the respiratory passages, lungs, and pleura by dampening their activity and thereby reducing the cough reflex at its source. It begins to act within 15 to 20 minutes and its effect lasts for 3 to 8 hours." ([DailyMed: Benzonatate 100 Mg (benzonatate) prescribing information, TIME CAP LABORATORIES, INC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5adfd324-b6d6-f624-e063-6294a90ab26e), label version 2026-09-07; accessed 2026-11-19.) Based on general pharmacology, benzonatate is a local anaesthetic-like agent that blocks voltage-gated sodium channels in peripheral sensory nerves and stretch receptors, which is how it suppresses the cough reflex.

A possible link to cauda equina syndrome is modulation of nociceptive or neuropathic signalling through sodium channel blockade. This link is speculative. Cauda equina syndrome is a surgical emergency caused by mechanical compression of nerve roots, and a sodium channel blocker would not treat that cause. At most, it might play a symptomatic role.

The second prediction, **obsolete neurogenic bladder (disease)**, has a TxGNN score of 0.9939. The theoretical rationale is that blocking sodium channels in sensory afferents could dampen bladder C-fibre signalling. The disease entry is marked "obsolete" in the ontology, so it probably maps to a broader neurogenic lower urinary tract dysfunction concept. It also has no supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 25866 | Benz 100mg Capsule | Strip of 12 capsules | Valid |
| 120994 | Lupin's Benz Pearls Capsule | Strip of 10 soft gelatin capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

Both licenses are valid single-ingredient oral products from Lupin Ltd.

---

## Safety Considerations

- **Drug Interactions**: One interaction was identified in the DDInter database: **tizanidine** (Moderate severity).

For other safety information, such as warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN scores (0.9966 for cauda equina syndrome and 0.9939 for obsolete neurogenic bladder) are model predictions only, with no clinical trials or literature behind them. The proposed mechanism is speculative, and cauda equina syndrome is driven by mechanical compression that sodium channel blockade would not address.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source, which are needed for safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Approved indication text for the two India licenses
- Preclinical or clinical evidence showing a benefit in cauda equina syndrome or neurogenic bladder symptoms
- Clarification of which current disease concept the "obsolete neurogenic bladder" entry maps to
- Route compatibility assessment for the proposed new indications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Benzonatate 100 Mg (benzonatate) prescribing information, TIME CAP LABORATORIES, INC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5adfd324-b6d6-f624-e063-6294a90ab26e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

