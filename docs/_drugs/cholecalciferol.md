---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
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

# Cholecalciferol: From Vitamin D Deficiency and Bone Disorders to Familial Isolated Hypoparathyroidism (Impaired PTH Secretion)

## One-Sentence Summary

Cholecalciferol (vitamin D3) is originally used for vitamin D deficiency and related bone and mineral disorders such as rickets, osteomalacia and osteoporosis.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**.
So far there are **no clinical trials and no publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism (general), and related calcium and phosphorus disorders |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cholecalciferol is a native vitamin D (a pro-hormone) that is converted in the body to active metabolites, which raise intestinal calcium absorption. Its efficacy in vitamin D deficiency and bone mineralisation disorders is well established, and mechanistically it may be applicable to hypoparathyroidism.

Hypoparathyroidism in general is already among the drug's original indications, which probably explains the very high model score. The predicted disease is a familial form in which PTH secretion is impaired. The model likely scores it highly because of its closeness to the already-recognised hypoparathyroidism indication, not because of new evidence.

There is an important practical caveat. Converting vitamin D to its active form in the kidney depends on PTH. When PTH is deficient, this step is impaired, so active analogues such as calcitriol or alfacalcidol are generally preferred over native cholecalciferol. The benefit of cholecalciferol in this specific condition is therefore uncertain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty valid single-ingredient registrations exist in India. Five representative ones are listed below; the dossier does not record approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 38874 | Cholvac-D3 Softgel Capsule | Strip of 4 soft gelatin capsules | Zydus Cadila |
| 217773 | Tonecal-D3 Softgel Capsule | Strip of 4 soft gelatin capsules | Soigner Medicament Pvt Ltd |
| 94298 | Gemsoline-D3 Nano Shot | Bottle of 5 ml oral solution | Medley Pharmaceuticals |
| 242252 | Werol 600000IU Injection | Vial of 1 ml injection | Welgenic Pharma |
| 5934 | Astesol-D3 60K Chewable Tablet | Strip of 4 chewable tablets | Asterism Pharmaceuticals Pvt Ltd |

Available forms include oral soft capsules, tablets, chewable tablets, oral solutions and injections.

## Safety Considerations

- **Drug Interactions** (56 interactions recorded; examples from the first 20 reviewed):
  - **Major:** calcifediol, calcitriol, dihydrotachysterol and doxercalciferol. These are other vitamin D-active agents, so combining them risks additive hypercalcaemia.
  - **Moderate:** thiazide diuretics (bendroflumethiazide, benzthiazide, chlorothiazide, chlorthalidone), barbiturates (amobarbital, butabarbital, butalbital), carbamazepine, bile acid sequestrants (cholestyramine, colesevelam, colestipol), digoxin and digitoxin, and topical calcipotriol and calcitriol.
  - **Minor:** cimetidine.
- **Disease associations flagged in the knowledge graph** (derived from graph data, not package insert text). The graph links the drug to caution in the following conditions:
  - Calcium and phosphate disorders: hypercalcaemia, nephrocalcinosis, hyperparathyroidism, phosphorus metabolism disorders, primary hyperoxaluria.
  - Organ disease: kidney disease, liver disease, gallbladder disease, sarcoidosis.
  - Cardiometabolic conditions: hypertension, atrial fibrillation, diabetes mellitus, hyperlipidaemia.
  - Iron and blood disorders: haemochromatosis and other iron metabolism disorders, Wilson disease, sickle cell anaemia, blood coagulation disorders.
  - Other: some cancers (prostate, female breast).

Because treating hypoparathyroidism involves close management of calcium levels, the hypercalcaemia and nephrocalcinosis risks are especially relevant here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the high model score most likely reflects closeness to the existing general hypoparathyroidism indication. Standard care in PTH-deficient states already favours active vitamin D analogues over native cholecalciferol, and narrow calcium margins add a safety concern.

For context, among the other predictions generated for this drug, **renal osteodystrophy** has the strongest support (one Phase 3 trial, NCT00752401, in vitamin D-deficient kidney transplant recipients, one completed comparison trial, and several reviews and observational studies). It may be a better candidate for further evaluation, with calcium, phosphate, PTH and 25(OH)D monitoring.

**To proceed, the following is needed:**
- Disease-specific clinical or literature evidence for familial isolated hypoparathyroidism
- A comparison against active vitamin D analogues (calcitriol, alfacalcidol) in PTH-deficient patients
- Detailed mechanism of action data
- Package insert warnings and contraindications for the India-marketed products
- A calcium and renal monitoring plan to manage hypercalcaemia and nephrocalcinosis risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

