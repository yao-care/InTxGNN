---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 824
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Teriparatide: predicted new indication duodenal ulcer (disease) (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
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

## Teriparatide: From Postmenopausal Osteoporosis to duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but **no clinical trials and no publications** currently support this prediction, so it rests on the score from the TxGNN model (deep learning) alone, which may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Teriparatide is a synthetic fragment of human parathyroid hormone. It acts on the PTH1 receptor (and also binds the PTH2 receptor) to stimulate new bone formation. This is why it is used for osteoporosis. According to the Mechanism of Action section of the US FDA-approved prescribing information for teriparatide: "Endogenous 84-amino acid parathyroid hormone (PTH) is the primary regulator of calcium and phosphate metabolism in bone and kidney. Physiological actions of PTH include regulation of bone metabolism, renal tubular reabsorption of calcium and phosphate, and intestinal calcium absorption. […] The biological actions of PTH and teriparatide are mediated through binding to specific high-affinity cell-surface receptors." ([DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c), label version 2026-08-31; accessed 2026-11-19.)

Based on the data compiled for this report, **no mechanistic link** was identified between PTH1 receptor-driven bone formation and duodenal ulcer. The two conditions differ in tissue, cause, and disease process: one is bone fragility, the other is damage to the lining of the upper intestine. The high TxGNN score (0.9986) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical support. Without trials or literature, this prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Teriparatide is widely marketed in India, with 20 valid registrations, all single-ingredient injectable products and none cancelled. Approved indication text was not available for these registrations.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 25827 | Bonmax PTH 750mcg Solution for Injection | Cartridge of 3 ml Solution for Injection | Valid |
| 26201 | Bonotiode Injection | Penfill of 3 ml Injection | Valid |
| 26626 | Bonrange-PTH Injection | Cartridge of 3 ml Injection | Valid |
| 28216 | Bomastren Solution for Injection | Cartridge of 3 ml Solution for Injection | Valid |
| 28407 | Bonotiode 250mcg/ml Solution for Injection | Cartridge of 1 ml Solution for Injection | Valid |
| 28520 | Bonspark Injection | Cartridge of 3 ml Injection | Valid |
| 94276 | Gemtide Injection | Pre-filled pen of 2.4 ml Injection | Valid |
| 94569 | Gemtide Injection (2.4ml Each) | Box of 3 injections | Valid |
| 94875 | Gemtide Cartridge | Cartridge of 3 ml Injection | Valid |
| 161859 | Osteri 750mcg Solution for Injection | Pre-filled pen of 3 ml Solution for Injection | Valid |
| 162280 | Osteofrac 750mcg Injection | Vial of 3 ml Injection | Valid |
| 184828 | Rockbon PTH Solution for Injection | Prefilled syringe of 3 ml Solution for Injection | Valid |
| 214816 | Terifrac Injection | Cartridge of 1 Injection | Valid |
| 215049 | Tricium PTH Injection | Cartridge of 3 ml Injection | Valid |
| 215167 | Terifrac Injection (3ml Each) | Box of 3 injections | Valid |
| 215590 | Terifort 750mcg Solution for Injection | Cartridge of 3 ml Solution for Injection | Valid |
| 216629 | Tricium PTH TP3 250mcg Injection | Vial of 1 Injection | Valid |
| 218142 | Tricium PTH RU 250mcg/ml Solution for Injection | Pre-filled pen of 3 ml Solution for Injection | Valid |
| 246562 | Zotide Injection | Cartridge of 3 ml Injection | Valid |
| 250958 | Zotiram 750mcg Injection | Vial of 3 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (contraindication-type links, not label text):** hypercalcemia, hyperparathyroidism, bone Paget disease (including juvenile), bone osteosarcoma, nephrocalcinosis, urolithiasis, phosphorus metabolism disease, osteomalacia, rickets, renal osteodystrophy, osteitis fibrosa, and hypotensive disorder.
- **Drug interactions (8 entries found):**
  - Moderate: digoxin, digitoxin, topical calcitriol, topical calcipotriol
  - Minor: hydrochlorothiazide, furosemide

  Two further entries (PTH1 and PTH2 receptors) are pharmacological target records, not interactions.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction has no trials, no literature, and no plausible mechanism. The high score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- A biological rationale linking PTH1 receptor signalling to duodenal mucosal disease
- Preclinical or mechanistic studies showing any effect on ulcer healing
- Package insert warnings and contraindications for a formal safety screen

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data beyond these receptor targets are not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

