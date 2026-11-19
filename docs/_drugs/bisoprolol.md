---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Bisoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: at least 20 listed products"
---

# Bisoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Bisoprolol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Bisoprolol is a beta-1 selective blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for bisoprolol: "BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose." ([DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e), label version 2026-11-11; accessed 2026-11-19.) Based on known information, bisoprolol is a beta-1 selective blocker, its efficacy in hypertension is established, and mechanistically it may be applicable to hypertensive kidney disease through blood pressure lowering and reduced renin release.

However, malignant hypertensive renal disease is a hypertensive emergency with kidney involvement. It is managed with rapid, carefully titrated parenteral therapy and blockade of the renin-angiotensin-aldosterone system (RAAS). Oral beta-blockers are not a primary therapy. The very high score from the TxGNN model (deep learning) may reflect similarities the model learned between related diseases, such as the existing hypertension indication, not biological evidence.

Other top-ranked predictions are similarly weak:
- **Malignant renovascular hypertension** (0.9994): beta-1 blockade lowers renin secretion, which is plausible, but definitive management is revascularisation and RAAS inhibitors.
- **Pulmonary hypertension** (two entries, 0.9993): the link is weak. It is a distinct pulmonary vascular disease, and beta-blockers are generally avoided or used cautiously because of the risk of right ventricular dysfunction. Eight publications were retrieved for the hypoxia-related entry, but none shows bisoprolol treating pulmonary hypertension. They are heart failure, preclinical and physiology studies that give only indirect context.
- **Braddock syndrome** (0.9991): no mechanistic rationale can be established from the available data.

## India Market Information

Bisoprolol is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. Approved indication text was not available for these registrations. Five of them are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 29839 | Bisopil H 2.5 Tablet | Strip of 10 tablets | Psychotropics India Ltd |
| 26711 | Biselect 10 Tablet | Strip of 10 tablets | Intas Pharmaceuticals Ltd |
| 27597 | Besicor 2.5 Tablet | Strip of 15 tablets | Ajanta Pharma Ltd |
| 28963 | Bitoprol 25 XL Tablet | Strip of 10 extended-release tablets | Bi-Cure Remedies |
| 26325 | Bisosafe 5 Tablet | Strip of 10 tablets | Abbott |

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Disease associations flagged in the knowledge graph (not label text):** asthma, diabetes mellitus and diabetic ketoacidosis, kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, systemic lupus erythematosus, psoriasis, gout, anuria, myasthenia gravis, anxiety and related mood disorders, and several electrolyte or metabolic conditions (potassium deficiency, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease). These should be verified against the official label.
- **Drug interactions:** 226 interactions were identified. Those listed are mostly Moderate, including epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, acetohexamide, and calcium salts (acetate, carbonate, citrate, gluconate). Acetylsalicylic acid, aluminium hydroxide and attapulgite are Minor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or literature for the top indication (Evidence Level L5). Standard care for malignant hypertensive renal disease relies on other therapies, and oral bisoprolol is not a primary option.

**To proceed, the following is needed:**
- Clinical or observational evidence of bisoprolol in malignant hypertensive renal disease or related hypertensive kidney injury
- Mechanism of action data
- Package insert warnings and contraindications from the India regulatory source, which is a blocking gap for safety screening
- Review of the knowledge-graph contraindications (notably kidney disease) against the label, given the renal target population
- Assessment of route compatibility, since the emergency setting normally requires parenteral therapy and only oral forms are marketed

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

