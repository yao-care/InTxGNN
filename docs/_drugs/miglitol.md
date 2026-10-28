---
layout: default
title: Miglitol
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 9
monitor_inn: "Miglitol"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pancreatic agenesis", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
last_modified_at: 2026-10-28
description: "Miglitol: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Miglitol
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

## Miglitol: Focal stiff limb syndrome
{: .text-alpha }

## One-Sentence Summary

Miglitol is an oral alpha-glucosidase inhibitor, and type 2 diabetes mellitus is its original use.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 18 of 18) |
| Number of Registrations | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, miglitol is an intestinal alpha-glucosidase inhibitor that delays carbohydrate absorption and has minimal systemic exposure.

Focal stiff limb syndrome, like classic stiff person syndrome, is an autoimmune or neurological disorder involving reduced GABAergic and glycinergic inhibition (for example anti-GAD or anti-glycine receptor antibodies). No credible mechanistic link to miglitol was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same pattern applies to the other top-ranked predictions:

- **Classic stiff person syndrome** (score 0.9987): frequent comorbid type 1 diabetes likely inflates the score. Miglitol has no known effect on GABA signalling or autoimmunity.
- **Thiamine-responsive dysfunction syndrome** (0.9987): diabetes is a feature of the disease, but thiamine supplementation is the disease-specific treatment.
- **Opsismodysplasia** (0.9987): the INPPL1 (SHIP2) gene relates to insulin signalling, but miglitol does not act on this pathway.
- **Lipodystrophy-type conditions** (drug-induced localized, centrifugal, pressure-induced, idiopathic; 99.70–0.9973): these appear to be clustering artefacts with no link to carbohydrate absorption.
- **Pancreatic agenesis** (0.9971): patients need insulin and enzyme replacement, and miglitol cannot substitute for them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

There are 18 valid single-ingredient licences. The records contain no approved-indication text. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 142594 | Migset 25mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 136339 | Mignar 50 Tablet (Glenmark Pharmaceuticals Ltd) | Strip of 15 tablets | Not stated in the records |
| Registration No. 101510 | Glybloc 50mg Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 76480 | Etilox 25mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 67698 | Diamig 25mg Tablet (Micro Labs Ltd) | Strip of 10 tablets | Not stated in the records |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: contraindication links exist for kidney disease, pyoureter, inflammatory bowel disease, infectious disease, ulcerative colitis, hypoglycaemia and injury.
- **Drug Interactions**: 241 interactions are recorded. Examples at moderate level include phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, hydrochlorothiazide, acetazolamide, ethinylestradiol, estradiol, hydrocortisone, triamcinolone, alpelisib, aripiprazole, asenapine, ethanol and asparaginase. Minor-level examples include ranitidine and topical corticosteroids (hydrocortisone, alclometasone).
- **Population concern**: in conditions with exocrine pancreatic insufficiency, such as pancreatic agenesis, gastrointestinal effects and malabsorption are an unresolved concern.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies miglitol in focal stiff limb syndrome, and no credible mechanistic link was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Established therapies already act on the relevant pathways.

**To proceed, the following is needed:**
- Mechanism of action data for miglitol
- Package insert warnings and contraindications from the India licence holders
- Any preclinical or clinical rationale linking alpha-glucosidase inhibition to GABAergic or glycinergic dysfunction
- Reassessment of lower-ranked predictions, or of other drugs, if a mechanism-based candidate is sought
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

