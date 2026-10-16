---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 824
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teriparatide: predicted new indication Duodenal ulcer (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "pregnancy associated osteoporosis", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Teriparatide: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but **no clinical trials and no publications** currently support this prediction, so it rests on a graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Teriparatide is a synthetic fragment of human parathyroid hormone. It acts on the PTH1 receptor (and also binds the PTH2 receptor) to stimulate new bone formation. This is why it is used for osteoporosis. Detailed mechanism-of-action data beyond these receptor targets are not available.

Based on the data compiled for this report, **no mechanistic link** was identified between PTH1 receptor-driven bone formation and duodenal ulcer. The two conditions differ in tissue, cause, and disease process: one is bone fragility, the other is damage to the lining of the upper intestine. The high TxGNN score reflects a pattern in the knowledge graph, not biological or clinical support. Without trials or literature, this prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Teriparatide is widely marketed in India, with 20 valid registrations, all single-ingredient injectable products and none cancelled. Approved indication text was not available for these registrations. Five main products are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 28520 | Bonspark Injection | Cartridge of 3 ml injection | Integrace Pvt Ltd |
| 215049 | Tricium PTH Injection | Cartridge of 3 ml injection | Corona Remedies Pvt Ltd |
| 214816 | Terifrac Injection | Cartridge of 1 injection | Intas Pharmaceuticals Ltd |
| 161859 | Osteri 750mcg Solution for Injection | Pre-filled pen of 3 ml | Emcure Pharmaceuticals Ltd |
| 94276 | Gemtide Injection | Pre-filled pen of 2.4 ml | Alkem Laboratories Ltd |

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

**Note on other predictions:** Among the other predicted indications, **pregnancy-associated osteoporosis** (rank 8, score 99.55%) has much stronger support. It is an extension of the approved osteoporosis use, supported by cohort studies, systematic reviews, and a recent position statement, though no RCTs. It is rated L3 with a "Proceed with Guardrails" recommendation, and it may be a better candidate for a separate evaluation. Use would be off-label, specialist-directed, and only after lactation has ended, with pregnancy excluded and calcium and bone density monitored.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

