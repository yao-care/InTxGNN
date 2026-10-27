---
layout: default
title: Ferrous Bisglycinate
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ferrous Bisglycinate: predicted new indication Bronchitis (evidence level L5). Approved use: Not stated in the India license data (iron supplementation is the typ…"
monitor_inn: "Ferrous bisglycinate"
predicted_indications: ["bronchitis", "bronchial neoplasm (disease)", "gastroduodenitis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "peptic ulcer disease", "thrombophilia", "Chagas cardiomyopathy", "infective urethral stricture"]
---

# Ferrous Bisglycinate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ferrous Bisglycinate: From Iron Supplementation to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Ferrous bisglycinate is an iron chelate (iron bound to the amino acid glycine) marketed in India as an oral iron supplement. The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials and no publications** were found to support this prediction, so it rests on a graph-based model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (iron supplementation is the typical use) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous bisglycinate is an iron chelate used to replenish iron, and its established role is in correcting iron deficiency. It is not an anti-infective or anti-inflammatory agent.

No plausible mechanistic link between iron supplementation and the treatment of bronchitis has been established. The high TxGNN score (0.974) reflects proximity in a knowledge graph, not clinical or biological evidence. Because the original indication is missing from the license data, the relationship between the original and predicted indications cannot be assessed.

Other top-ranked predictions are also unsupported. These include bronchial neoplasm, gastroduodenitis, peptic ulcer disease, and several clotting disorders (heparin cofactor 2 deficiency, antithrombin deficiency type 2, thrombophilia). Several of them, such as the cancer and Chagas cardiomyopathy predictions, raise a concern that supplemental iron could be harmful rather than helpful. For peptic ulcer, iron supports anemia care after bleeding but does not treat the ulcer.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84828 | Fenton-PR Tablet | Strip of 10 tablets | Not stated |
| 85861 | Ferro-Svp Tablet | Strip of 10 tablets | Not stated |
| 6753 | Albuvit-Fe Tablet | Strip of 10 tablets | Not stated |
| 26774 | Bisred Tablet | Strip of 10 tablets | Not stated |
| 200366 | Sayfer XT Tablet | Strip of 10 tablets | Not stated |

Six valid single-ingredient licenses are registered in total (a sixth product, Hbqte-XT Tablet, license 104189, comes in strips of 15 tablets). All are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature, and no credible mechanistic link between iron supplementation and bronchitis. Safety label information is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source
- Mechanism of action data (e.g., from DrugBank)
- The approved indication text for the registered products
- Any preclinical or clinical evidence linking iron chelates to bronchitis, which is currently absent
- Route and dosage-form compatibility assessment for a respiratory indication (currently only oral tablets are registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

