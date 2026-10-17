---
layout: default
title: Methdilazine
parent: Model Prediction Only (L5)
nav_order: 533
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Methdilazine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Angioedema, allergic rhinitis, vasomotor rhinitis…"
monitor_inn: "Methdilazine"
predicted_indications: ["nasal cavity disease"]
---

# Methdilazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Methdilazine: From Allergic Conditions (Angioedema, Allergic Rhinitis, Urticaria) to Nasal Cavity Disease

## One-Sentence Summary

Methdilazine is a phenothiazine-class first-generation H1 antihistamine, originally used for allergic and histamine-related conditions such as allergic rhinitis, urticaria, angioedema and conjunctivitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **no registered clinical trials and no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angioedema, allergic rhinitis, vasomotor rhinitis, urticaria and related allergic conditions (the India licence record has no approved indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, methdilazine is a phenothiazine-class first-generation H1 antihistamine. Its use in allergic rhinitis, vasomotor rhinitis and the common cold has been established, and mechanistically it may be applicable to nasal cavity conditions through general H1-receptor blockade and anticholinergic effects typical of the class. This reasoning rests on class properties, not on drug-specific evidence.

The high TxGNN score is most likely driven by overlap with the existing indications. Allergic rhinitis, vasomotor rhinitis and the common cold are already nasal cavity conditions. "Nasal cavity disease" is a broad category that largely duplicates these uses, so it is not a distinct new indication and does not amount to a strong repurposing signal. A genuinely new use would need a more specific nasal condition that is not already covered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 60812 | Dilosyn Tablet (Glaxo SmithKline Pharmaceuticals Ltd) | Strip of 10 tablets (oral) | Not specified in the licence record |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 401 potential interactions. The entries listed here are the first 20 returned, which include two rated Major:
  - **Major**: Bupropion, Potassium citrate
  - **Moderate** (examples): Epinephrine, Morphine, Atropine, Hyoscyamine, Glycopyrronium, Loperamide, Lorcaserin, and several antidiabetic agents (Acarbose, Metformin, Pioglitazone, Alogliptin, Albiglutide, Saxagliptin, Canagliflozin, Dapagliflozin, Chlorpropamide)
  - Additive anticholinergic effects are plausible with the antimuscarinic agents listed (atropine, hyoscyamine, glycopyrronium).

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications. The predicted indication largely overlaps with allergic and vasomotor rhinitis and the common cold, which are already established uses, so it is not a distinct new indication.

**To proceed, the following is needed:**
- Retrieve the India package insert (warnings, contraindications, approved indications), as the current safety record is incomplete
- Obtain mechanism of action data for methdilazine from DrugBank
- Define a specific, non-overlapping nasal indication (for example, a particular rhinitis subtype or sinonasal condition) in place of the broad "nasal cavity disease" label
- Conduct a literature and trial search on that specific indication
- Confirm the full interaction profile, particularly the Major interactions and additive anticholinergic effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

