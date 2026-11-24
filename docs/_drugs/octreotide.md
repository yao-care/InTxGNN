---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). In India: at least 20 listed products"
---

# Octreotide
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

## Octreotide: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Octreotide is a somatostatin analog originally used to treat acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for octreotide: "Sandostatin Injection exerts pharmacologic actions similar to the natural hormone, somatostatin. It is an even more potent inhibitor of GH, glucagon, and insulin than somatostatin. […] By virtue of these pharmacological actions, octreotide has been used to treat the symptoms associated with metastatic carcinoid tumors (flushing and diarrhea), and VIP secreting adenomas (watery diarrhea)." ([DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39), label version 2026-07-22; accessed 2026-11-19.) Based on known information, octreotide is a somatostatin analog that acts mainly on somatostatin receptors SSTR2 and SSTR5. Its efficacy in hormone-secreting conditions such as acromegaly and carcinoid syndrome is established.

For vulvar inverted follicular keratosis, a benign epithelial skin lesion, no plausible mechanistic link is supported by the available data. The high TxGNN score is a computational output only. It is likely driven by similarity to related entries, such as seborrheic keratosis, which also appears among the top predictions. This prediction should be treated as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Octreotide is marketed in India as injectable products. There are 20 valid single-ingredient registrations and none are cancelled. The approved indication text is not available for these registrations.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 22138 | Astide 100mcg Injection | Vial of 1 Injection | Valid |
| 38332 | Celostatin Lar 20mg Injection | Vial of 1 Injection | Valid |
| 87272 | Ferotide 0.1mg Injection | Vial of 1 ml Injection | Valid |
| 89982 | Fetide 100mcg Injection | Vial of 1 Injection | Valid |
| 161758 | Octride 0.1mg Injection | Vial of 1 Injection | Valid |
| 162767 | Okeron 0.1mg Injection | Vial of 1 ml Injection | Valid |
| 162773 | Octride 0.05mg Injection | Vial of 1 ml Injection | Valid |
| 163527 | Octotide 0.1mg Injection | Vial of 1 ml Injection | Valid |
| 163875 | Octride Depot 10mg Injection | Vial of 1 Injection | Valid |
| 165950 | Octotide 0.05mg Injection | Vial of 1 ml Injection | Valid |
| 167046 | Okeron 0.05mg Injection | Vial of 1 ml Injection | Valid |
| 168167 | Octiviz Injection | Ampoule of 1 ml Injection | Valid |
| 168843 | Ozark 50mcg Injection | Vial of 1 Injection | Valid |
| 169320 | Ozark 100mcg Injection | Vial of 1 Injection | Valid |
| 170627 | Octatide 50mcg Injection | Vial of 1 Injection | Valid |
| 171136 | Ocumeg 50mcg Injection | Vial of 1 ml Injection | Valid |
| 171718 | Octiross 100mg Injection | Vial of 1 ml Injection | Valid |
| 201402 | Sandostatin LAR 20mg Injection | Vial of 1 ml Injection | Valid |
| 207477 | Sandostatin 0.05mg Injection | Vial of 1 Injection | Valid |
| 212202 | Supertide 100mcg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: The knowledge graph links octreotide to contraindications or cautions in several conditions, including:
  - Metabolic and endocrine: hyperglycemia, hypoglycemia, diabetes mellitus, diabetic ketoacidosis, hypothyroidism (including congenital hypothyroidism and myxedema)
  - Hepatobiliary: liver disease, cirrhosis, gallbladder disease, cholelithiasis (including cholecystolithiasis and choledocholithiasis)
  - Gastrointestinal: ileus, intestinal obstruction
  - Cardiac: sudden cardiac arrest, heart conduction disease
  - Renal and nutritional: kidney failure, uremia, vitamin B12 deficiency
- **Drug Interactions**: 272 interactions were recorded. The 20 listed are all of Moderate level and mostly involve glucose-lowering agents, including:
  - Insulins (aspart, degludec, detemir, glargine, glulisine and human insulins)
  - Metformin, acarbose and chlorpropamide
  - Glimepiride
  - DPP-4 inhibitors (alogliptin, linagliptin)
  - GLP-1 agonists (albiglutide, dulaglutide, semaglutide)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)

  Glucose monitoring is advisable when octreotide is combined with these agents.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and no plausible mechanistic link between somatostatin receptor agonism and a benign keratinocyte lesion. The other top-ranked predictions (such as seborrheic keratosis and several nephrotic syndromes) are also prediction-only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products. This is a blocking gap for safety screening.
- Mechanism of action data for octreotide, to assess any biological link to the predicted condition.
- Preclinical or mechanistic evidence showing somatostatin receptor involvement in the target skin lesion.
- Route compatibility assessment. Octreotide is only available as injections in India, which may not suit a benign skin lesion.
- A review of the other ranked predictions for any with stronger biological rationale.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

