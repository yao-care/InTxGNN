---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 9
monitor_inn: "Glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-20
description: "Glimepiride: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Glimepiride
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

## Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Glimepiride is a sulfonylurea medicine, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; no approved indication text is available in the licence records) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for glimepiride: "Glimepiride primarily lowers blood glucose by stimulating the release of insulin from pancreatic beta cells. Sulfonylureas bind to the sulfonylurea receptor in the pancreatic beta-cell plasma membrane, leading to closure of the ATP-sensitive potassium channel, thereby stimulating the release of insulin." ([DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa), label version 2024-08-20; accessed 2026-11-19.) Glimepiride is generally known as a sulfonylurea that closes K-ATP channels in pancreatic beta cells and stimulates insulin release. This is background knowledge, not something confirmed by the compiled data.

Classic stiff person syndrome is an autoimmune neurological disorder usually associated with anti-GAD65 antibodies and impaired GABAergic signalling. It often co-occurs with type 1 diabetes. The high TxGNN score most likely reflects network proximity through diabetes and GAD-related associations, not a therapeutic effect. No mechanistic link between glimepiride and the neurological symptoms of this disease is established.

The same score was given to focal stiff limb syndrome (0.9975). This suggests the prediction is propagated from a shared parent or related disease node, not from independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

---

## India Market Information

At least 20 licences were found, and the list may be partial. All listed products are valid. The licence records contain no approved indication text. The table shows five of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 208521 | Supride 2mg Tablet | Strip of 10 tablets | Not stated in records |
| 15505 | Adride 4mg Tablet | Strip of 10 tablets | Not stated in records |
| 16440 | Asoride 1mg Tablet | Strip of 10 tablets | Not stated in records |
| 102727 | Glimtec 2mg Tablet | Strip of 10 tablets | Not stated in records |
| 99220 | Glenavon 2mg Tablet | Strip of 10 tablets | Not stated in records |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** Contraindication links exist for kidney disease, liver disease, gallbladder disease, congestive heart failure, hypopituitarism and other pituitary hormone deficiencies, hypogonadotropic hypogonadism (including Kallmann syndrome), thymus gland disease, osteoporosis, postmenopausal osteoporosis and infectious disease.
- **Drug Interactions:** 599 interactions were recorded. Examples at moderate level include phenylephrine, acebutolol, acetazolamide, famotidine, ranitidine, ibuprofen, ketorolac, ethinylestradiol, hydrocortisone, hydrochlorothiazide, salbutamol, epinephrine, ethanol and albiglutide. Topical hydrocortisone and topical alclometasone are rated minor.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications study glimepiride in stiff person syndrome, and no plausible mechanism is established. Evidence level is L5. The other predicted diseases (focal stiff limb syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, localized lipodystrophies and pancreatic agenesis) are also supported by no direct clinical evidence. For pancreatic agenesis, a secretagogue is biologically unlikely to work.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for safety screening
- Mechanism of action data
- A rationale linking glimepiride to GABAergic or autoimmune mechanisms, or preclinical data supporting one
- Any clinical or observational data in stiff person syndrome patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

