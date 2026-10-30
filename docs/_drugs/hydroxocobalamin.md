---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Hydroxocobalamin"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
description: "Hydroxocobalamin: predicted new indication Esophageal varices without bleeding (evidence level L5). Approved use: Not recorded in the local data"
---

# Hydroxocobalamin
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

## Hydroxocobalamin: Esophageal varices without bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, originally used to treat vitamin B12 deficiency, pernicious anemia and cyanide poisoning.
The TxGNN model predicts it may be effective for **esophageal varices without bleeding**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Esophageal varices without bleeding |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroxocobalamin is a vitamin B12 form whose efficacy in B12 deficiency and cyanide poisoning is established. It can scavenge cyanide and bind nitric oxide.

A link to portal hypertension through nitric oxide modulation is conceivable, but nothing in the data compiled for this report supports it. No trial or publication tests this idea.

The model gives the same score (0.9923) to both the non-bleeding and bleeding varices indications. This suggests the prediction reflects a shared disease-ontology relationship rather than biology specific to either indication. The high score should not be read as clinical evidence.

A related prediction, **esophageal varices with bleeding**, has the same score, the same L5 evidence level and the same Hold recommendation. Acute variceal bleeding is managed with vasoactive agents, endoscopic band ligation and antibiotic prophylaxis. Nothing in the data suggests hydroxocobalamin has a role there.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 44607 | Cox 1mg Injection (Bryogen Pharmaceuticals Pvt. Ltd.) | Vial of 1 ml injection | Not stated in the compiled data |
| 216332 | Trineurosol HV Injection (Wockhardt Ltd) | Vial of 5 ml injection | Not stated in the compiled data |
| 216200 | Trineurosol HP 1000mg Injection (Wockhardt Ltd) | Vial of 1 ml injection | Not stated in the compiled data |
| 215018 | Trineurosol HP Injection (Wockhardt Ltd) | Vial of 5 ml injection | Not stated in the compiled data |

All four licences are valid single-ingredient injectables. No oral or other non-injectable forms are registered.

## Safety Considerations

- **Knowledge-graph contraindications**: Hypertensive disorder and hypertension are listed as contraindications. These come from drug-disease relationships in the knowledge graph, not from label text. This is relevant because hydroxocobalamin can cause transient hypertension, which matters in portal hypertension and bleeding settings.
- **Other known effects**: Hydroxocobalamin can cause red discoloration of skin and urine.
- **Drug Interactions**: 32 interactions were identified. Most are of unknown severity. Those graded **Moderate** are:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Other listed interacting drugs include omeprazole, lansoprazole, ranitidine, simvastatin, prednisolone, budesonide, acetylsalicylic acid, valsartan, ramipril, lorazepam, citalopram, mirtazapine, levothyroxine, folic acid, loperamide and acetaminophen.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials and no publications, and the proposed mechanism is speculative. Hydroxocobalamin's potential to raise blood pressure is also a concern in portal hypertension.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence on hydroxocobalamin in portal hypertension or varices
- A literature and trial search specific to varices to confirm whether any evidence exists
- Route and dosing compatibility assessment for the new indication
- An assessment of blood pressure effects in patients with portal hypertension or variceal bleeding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

