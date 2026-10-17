---
layout: default
title: Alfacalcidol
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Alfacalcidol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism…"
monitor_inn: "Alfacalcidol"
predicted_indications: ["Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Alfacalcidol: From Hyperparathyroidism to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Alfacalcidol is an active vitamin D analogue, originally used for hyperparathyroidism, osteitis fibrosa, hypoparathyroidism and renal osteodystrophy.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**,
but currently there are **no clinical trials** and **no literature** specific to this subtype, so the prediction rests on the model score and mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; no approved indication text in the India licence records) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, alfacalcidol is a 1-alpha-hydroxylated vitamin D prodrug. It is converted in the liver to calcitriol, the active form of vitamin D, and so bypasses the PTH-dependent 1-alpha-hydroxylation step in the kidney.

This is mechanistically coherent with hypoparathyroidism, where PTH is low or absent and the kidney cannot adequately activate vitamin D. Hypoparathyroidism in general is already among the drug's original indications. The familial isolated form is therefore closer to an extension of an existing indication to a genetic subtype than to true repurposing.

However, no trials or publications specific to this subtype were found. The high score (0.996) is a model prediction only.

### Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Dahlberg-Borer-Newcomer syndrome | 99.60% | L5 | Retrieved literature is general (Fanconi-type disorders, FGF23 hypophosphataemia, vitamin D pharmacology) and does not study this syndrome. Hold. |
| 3 | Craniofacial conodysplasia | 99.55% | L5 | No clear mechanistic link; no trials or literature. Hold. |
| 4 | Acromesomelic dysplasia, Campailla Martinelli type | 99.53% | L5 | No clear mechanistic link; no trials or literature. Hold. |
| 5 | Renal tubular acidosis | 99.27% | L4 | Five case reports describe osteomalacia secondary to RTA treated with alfacalcidol plus alkali and other therapy, with improvement. Alfacalcidol acts on the bone complication rather than the tubular defect, and its specific contribution cannot be separated from co-treatments. Research question. |

## Clinical Trial Evidence

Currently no related clinical trials registered for the primary predicted indication.

## Literature Evidence

Currently no related literature available for the primary predicted indication (familial isolated hypoparathyroidism).

For the fifth-ranked prediction (renal tubular acidosis), the literature is limited to case reports:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) | 2013 | Case report | Modern Rheumatology | Osteomalacia from Sjögren's-associated RTA; bone density normalised after sodium bicarbonate, risedronate, alfacalcidol and prednisolone |
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Case report | Internal Medicine | Rapid improvement of osteomalacia in a patient with Sjögren's syndrome, rheumatoid arthritis and type 1 RTA treated with alkali and an alfacalcidol-containing regimen |
| [33398781](https://pubmed.ncbi.nlm.nih.gov/33398781/) | 2021 | Case report | CEN Case Reports | Osteomalacia due to atypical RTA with vitamin D deficiency, previously treated with active vitamin D |
| [28509074](https://pubmed.ncbi.nlm.nih.gov/28509074/) | 2012 | Case report/Review | CEN Case Reports | Osteomalacia secondary to distal RTA in Sjögren's syndrome, with literature review |
| [36412607](https://pubmed.ncbi.nlm.nih.gov/36412607/) | 2023 | Case report | Kidney & Blood Pressure Research | Zoledronic acid-related Fanconi syndrome and distal RTA presenting with severe hypophosphataemia |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2235 | Alphadol-C Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not stated in the licence record |
| 1308 | Alphadol 0.5mcg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not stated in the licence record |
| 328 | Alphadol 0.25mcg Capsule | Strip of 10 soft gelatin capsules | Not stated in the licence record |
| 2489 | Alphadol 1mcg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not stated in the licence record |
| 64293 | Decalcid 0.25mcg Tablet | Strip of 10 tablets | Not stated in the licence record |

A sixth registration, Vitalpha Soft Gelatin Capsule (No. 235436), is also valid. All six registrations are single-ingredient oral products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is mechanistically plausible, because alfacalcidol bypasses the renal activation step that PTH normally drives. But it is an extension of an existing hypoparathyroidism use rather than new evidence, and there are no trials or literature specific to the familial isolated subtype (Evidence Level L5). The other predictions are either mechanistically unsupported or rest only on indirect case reports.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licence holders, since safety screening cannot proceed without them
- Detailed mechanism of action data (MOA)
- Disease-specific literature or clinical data on alfacalcidol in familial isolated hypoparathyroidism, such as case series or registry data
- Approved indication text for the registered products, to confirm whether hypoparathyroidism is already covered
- For renal tubular acidosis, controlled data that separate alfacalcidol's effect from alkali and phosphate co-treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

