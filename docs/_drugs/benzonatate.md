---
layout: default
title: Benzonatate
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Benzonatate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the India license records (the drug is generally known…"
monitor_inn: "Benzonatate"
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
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, benzonatate is a local anaesthetic-like agent that blocks voltage-gated sodium channels in peripheral sensory nerves and stretch receptors, which is how it suppresses the cough reflex.

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

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 120994 | Lupin's Benz Pearls Capsule | Strip of 10 soft gelatin capsules | Not stated |
| 25866 | Benz 100mg Capsule | Strip of 12 capsules | Not stated |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

