---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Calcitriol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Hypoparathyroidism, renal osteodystrophy…"
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: From Hypoparathyroidism and Renal Osteodystrophy to Vitamin D Deficiency (Obsolete Term)

## One-Sentence Summary

Calcitriol is the active form of vitamin D. Its original uses centre on calcium and phosphate disorders such as hypoparathyroidism, renal osteodystrophy and hypophosphatemia.
The TxGNN model predicts it may be effective for **vitamin D deficiency** (a term now flagged as obsolete), but **no clinical trials and no publications** currently support this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypoparathyroidism, renal osteodystrophy, hypophosphatemia and related calcium/phosphate disorders (from the knowledge graph; the product records compiled for this report carry no indication text) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, calcitriol is the hormonally active form of vitamin D (1,25-dihydroxyvitamin D3). Its efficacy in disorders of calcium and phosphate balance is well established, and mechanistically it may be applicable to vitamin D deficiency.

The link between the original and predicted indications is biologically plausible, since calcitriol is the end product of the vitamin D pathway. That plausibility is also the main weakness of the prediction. The high score largely restates the drug's known physiology rather than revealing a new repurposing opportunity. The disease term is also flagged as obsolete, which reduces how actionable the prediction is. In practice, nutritional vitamin D deficiency is usually treated with native vitamin D (cholecalciferol or ergocalciferol) rather than calcitriol.

Other predictions in the same analysis are better supported. The strongest is **hereditary hypophosphatemic rickets** (including X-linked hypophosphatemia). There, calcitriol plus phosphate is the established standard of care, and two registered trials exist (details in the Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Calcitriol has 20 valid single-ingredient registrations and no cancelled ones. Approved-indication text is not listed in the records compiled for this report. Five main authorizations are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 35214 | Cal-Aid Soft Gelatin Capsule | Strip of 15 soft gelatin capsules | Indoco Remedies Ltd |
| 122271 | Laretol 1mcg Injection | Ampoule of 1 ml injection | La Renon Healthcare Pvt Ltd |
| 36119 | Calcirol 600000IU Injection | Packet of 6 injections | Cadila Pharmaceuticals Ltd |
| 188057 | Ritocal CT 0.25mcg Tablet | Strip of 10 tablets | Bodycare Pharmaceuticals |
| 43426 | Calcijet Injection | Ampoule of 1 ml injection | LG Lifesciences |

Marketed forms include oral soft gelatin capsules, oral tablets and injectables.

## Safety Considerations

- **Contraindications / disease conflicts (from the knowledge graph, not label text)**: kidney disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, hyperphosphatemia, hypervitaminosis, acute urate nephropathy, pyoureter, and arteriosclerosis obliterans. Because of the hypercalcemia and nephrocalcinosis conflicts, serum and urinary calcium need careful monitoring.
- **Drug Interactions**: 339 interactions were identified.
  - **Major**: other vitamin D products (cholecalciferol, calcifediol) and burosumab.
  - **Moderate**: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone and others), digoxin and digitoxin, anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butalbital), bile acid sequestrants (cholestyramine, colesevelam, colestipol), aluminum hydroxide, and topical calcipotriol.

Package insert warnings were not available for this report. Please refer to the package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for vitamin D deficiency has a very high model score but no trials or literature. It is largely a restatement of calcitriol's known physiology, and the disease term is obsolete. Calcitriol is not the usual treatment for nutritional vitamin D deficiency, so the repurposing case is weak.

Other predicted indications are better supported:
- **Hereditary hypophosphatemic rickets (XLH):** Evidence Level L2, with one completed early Phase 1 trial (NCT03748966, n=16) and one Phase 4 dose-comparison trial (NCT03820518, n=100, status unknown). Guidelines and a consensus statement support calcitriol plus phosphate. This is a candidate for **Proceed with Guardrails**, with monitoring of calcium, PTH and renal ultrasound for nephrocalcinosis.
- **Renal tubular acidosis:** Evidence Level L4, with only case reports, reviews and physiologic studies and no direct efficacy evidence.

**To proceed, the following is needed:**
- A clear, current disease definition replacing the obsolete vitamin D deficiency term, and a comparison with native vitamin D therapy
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Indian market products
- Comparative or controlled efficacy evidence if this indication is pursued
- Consider prioritising the hereditary hypophosphatemic rickets indication, with final trial results and a safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

