---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 1
monitor_inn: "Benzocaine"
predicted_indications: ["papillary conjunctivitis"]
last_modified_at: 2026-11-24
description: "Benzocaine: predicted new indication papillary conjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Benzocaine
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

## Benzocaine: topical ester-type local anesthetic (sodium channel blocker) → papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Benzocaine is a topical ester-type local anesthetic that is marketed in India in ear drop, dental gel, syrup and lozenge products.
The TxGNN model predicts it may be relevant to **papillary conjunctivitis**, but **no clinical trials and no publications** were found to support this direction, so it remains a computational hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | papillary conjunctivitis |
| TxGNN Prediction Score | 0.9938 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, benzocaine blocks voltage-gated sodium channels, which reduces nerve conduction of pain and itch signals.

A speculative link is symptomatic relief of ocular surface discomfort or itching in papillary conjunctivitis, such as contact-lens-related or allergic forms. However, a local anesthetic would not treat the underlying immune-mediated or mechanical cause. Its existing uses are also not mechanistically close to ocular inflammation.

The high model score (0.9938) is a computational output only, and no study backs it up. No ophthalmic formulation of benzocaine is established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Records may be partial. The valid licences found are listed in the table below; according to the Indian Medicine Dataset, several of them are combination products.

<!-- review:begin in-lic-20261124b-benzocaine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The 20 valid single-ingredient licences found are shown below in part (the first 5)." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. The sentence also described the products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for some of them. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-benzocaine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34616 | Curewax Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 59547 | Dizolwax Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 60803 | Dava Wax Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 73113 | E-Wax Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 78462 | Exwax Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 108225 | IG-Wax Ear Drop | Bottle of 10 ear drops | Valid |
| 117049 | Kira-Neo Ear Drop | Bottle of 5 ml Ear Drop | Valid |
| 151721 | Nugel Mps Syrup | Bottle of 170 ml Syrup | Valid |
| 162503 | Otoclean Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 163763 | Omnisoothe 10mg Lozenges | Strip of 8 lozenges | Valid |
| 164224 | Oriwax Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 187216 | Remowax Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 220125 | T Jel 7.50% Gel | Tube of 10 gm Dental Gel | Valid |
| 233886 | Vovax Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 241433 | Wax-Off Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 241476 | Waxrid Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 241566 | Waxactin Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 241610 | Waxoff Ear Drop | Packet of 10 ml Ear Drop | Valid |
| 242070 | Waxotec Ear Drop | Bottle of 10 ml Ear Drop | Valid |
| 242184 | Waxap Ear Drop | Bottle of 10 ml Ear Drop | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the data compiled for this report. Please refer to the package insert for safety information.

Points of concern if ocular use were ever considered (general pharmacological knowledge, not label data):
- Repeated ocular anesthetic exposure can cause corneal toxicity and delayed epithelial healing.
- Ester anesthetics are known contact sensitizers.
- Topical benzocaine products carry a risk of methemoglobinemia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, so the evidence level is L5. Ocular safety concerns and the lack of any ophthalmic formulation add further caution.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer rationale for ocular surface use
- Preclinical or clinical evidence that directly studies papillary conjunctivitis
- Package insert warnings and contraindications for the marketed products
- An ocular safety assessment (corneal toxicity, sensitization) and a suitable ophthalmic formulation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Revised: wording about the earlier partial table and the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

