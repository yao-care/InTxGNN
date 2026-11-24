---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 762
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is a keratolytic and anti-inflammatory agent, widely used on the skin for acne, seborrheic dermatitis, warts, corns and fungal skin infections, and also listed for inflammatory joint conditions and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, with a very high score but **no clinical trials and no publications** currently supporting this direction.
This is a model-only prediction, and the evidence is too weak to justify moving forward at present.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for salicylic acid: "Although the exact mode of action for salicylic acid in the treatment of warts is unknown, its activity appears to be associated with its keratolytic action, which results in mechanical removal of epidermal cells infected with wart viruses." ([DailyMed: Xalix (salicylic acid) prescribing information, Cintex Services, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41369b38-7f15-b597-e063-6394a90a614b), label version 2025-10-15; accessed 2026-11-19.) Based on known information, salicylic acid is a salicylate, and it is proposed to act through inhibition of COX enzymes and reduced prostaglandin synthesis. However, no public bioactivity data confirm this at a specific molecular target. Its effect on the skin is mainly keratolytic and anti-inflammatory.

The link to the new indication is plausible but indirect. Salicylic acid is associated with allergic rhinitis, and papillary conjunctivitis shares an allergic/atopic inflammatory component. This overlap is the only basis for the prediction, and it is not supported by any trial or publication.

There is also a practical concern. Topical salicylates are irritants, and the existing Indian products are for skin use (ointments, gels, serums, face washes). None are suited to the eye, so a new ophthalmic formulation and its safety work would be needed. The very high prediction score should be read as a model signal, not as proof of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

There are 20 valid single-ingredient registrations and no cancelled ones. Approved indication text is not recorded in the licence data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 23440 | Antichy Ointment | Tube of 15 gm Ointment | Valid |
| 31996 | Benzosil Ointment | Tube of 25 gm Ointment | Valid |
| 59379 | Dersol 6% Ointment | Tube of 25 gm Ointment | Valid |
| 60595 | Dersol 3% Ointment | Tube of 25 gm Ointment | Valid |
| 72627 | Epiwart Solution | Bottle of 15 ml Solution | Valid |
| 77026 | Eremis 2% Face Wash | Tube of 60 ml Face Wash | Valid |
| 88999 | Furr FURR 2% Salicylic Anti Acne Face Serum | Bottle of 30 ml Serum | Valid |
| 89442 | Furr 20% Vitamin C Skin Face Serum | Bottle of 30 ml Serum | Valid |
| 99205 | Galenus Salizoic DS Ointment | Tube of 30 gm Ointment | Valid |
| 118043 | Kerosalic Foaming Face Wash | Pump bottle of 100 ml Face Wash | Valid |
| 137547 | Minoz S Face Wash pH 5.5 | Bottle of 50 ml Face Wash | Valid |
| 200305 | Salicure Ointment | Tube of 30 gm Ointment | Valid |
| 200334 | SLC Face Wash | Tube of 50 gm Face Wash | Valid |
| 200983 | Saliderm Ointment | Tube of 20 gm Ointment | Valid |
| 201510 | SA 20 Ointment | Tube of 25 gm Ointment | Valid |
| 201818 | Salilac SF Ointment | Tube of 20 gm Ointment | Valid |
| 202401 | Saliderm CL Face Wash | Tube of 60 gm Face Wash | Valid |
| 202495 | Siliryl Ointment | Tube of 25 gm Ointment | Valid |
| 204837 | Salisis 6% Ointment | Tube of 15 gm Ointment | Valid |
| 234301 | Vedasol 30mg Gel | Tube of 60 gm Gel | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry was found, involving the acid-sensing ion channel ASIC3 (a target interaction, not a drug-drug interaction). No interaction severity level is available.
- **Ocular concern**: Topical salicylic acid carries a risk of irritation, which is a major obstacle for any use on the eye surface.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and an indirect allergic-inflammation argument. There are no trials or publications, the mechanism of action is not established, and ocular irritation risk is a significant concern. The other nine predicted indications are also model-only. Most (for example, rare skeletal dysplasias) have no credible mechanistic link and are probably TxGNN model (deep learning) artifacts. Of these, only spondyloarthropathy has plausible class-level support (NSAIDs), which could justify a focused literature review.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- A systematic literature search on salicylates in allergic and papillary conjunctivitis
- Ocular tolerability and formulation feasibility assessment (no eye-appropriate route is currently available)
- Preclinical evidence for the ocular indication before any clinical planning

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xalix (salicylic acid) prescribing information, Cintex Services, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41369b38-7f15-b597-e063-6394a90a614b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

