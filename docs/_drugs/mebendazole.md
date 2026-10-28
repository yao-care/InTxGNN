---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 516
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
description: "Mebendazole: predicted new indication Acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mebendazole
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

## Mebendazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Mebendazole is an anthelmintic (anti-worm) drug, originally used for intestinal worm infections such as pinworm (enterobiasis), roundworm (ascariasis) and whipworm (trichuriasis).
The TxGNN model predicts it may be effective for **acne**, but the data compiled for this report contain **no clinical trials** and **only 1 publication**, an unrelated case report, so the prediction is essentially unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available in the compiled data. Based on general knowledge, mebendazole is a benzimidazole anthelmintic that is understood to bind parasite tubulin, disrupting microtubule-dependent processes such as glucose uptake. This is well established for intestinal worm infections.

That mechanism does not map onto acne. Acne is driven by excess sebum, follicular blockage, *Cutibacterium acnes* and inflammation, and none of these is a recognised target of tubulin-binding anthelmintics. The high TxGNN score (0.9920) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only retrieved publication is an unrelated parasitic case report that mentions acne-like skin lesions, which looks like a spurious match.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report (unrelated condition) | The American Journal of Tropical Medicine and Hygiene | Report of human proliferative sparganosis in Venezuela. The patient had acne-like skin lesions as a symptom of the parasitic infection, which does not support mebendazole as an acne treatment. |

---

## India Market Information

There are 20 valid single-ingredient registrations. Five are listed below. The registration data supplied no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 193683 | Raid Suspension | Suspension, bottle of 10 ml | Not specified in registration data |
| 136436 | Min Min 100mg Tablet | Tablet, strip of 10 | Not specified in registration data |
| 136932 | Mebenth 100mg Tablet | Tablet, strip of 6 | Not specified in registration data |
| 202362 | Sta 500mg Tablet | Tablet, strip of 1 | Not specified in registration data |
| 134860 | Mebex 500mg Tablet | Tablet, strip of 1 (Cipla Ltd) | Not specified in registration data |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver disease and gallbladder disease.
- **Drug Interactions (10 recorded)**:
  - Moderate: metronidazole, iodide I-131, iodide I-123, phenobarbital, carbamazepine, ritonavir, fosphenytoin, phenytoin, primidone.
  - Minor: cimetidine.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, the single retrieved publication is irrelevant to acne, and there is no plausible mechanistic link between mebendazole and acne pathophysiology.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that mebendazole affects acne-relevant pathways (sebum production, *C. acnes*, inflammation)
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India registrations
- Route and formulation assessment (the current products are oral or suspension forms)

**Other predictions in the same data set (for reference):**
- Support comes from observational studies, reviews and the WHO guideline. Benzimidazoles, mainly albendazole with mebendazole as an alternative, are already standard antiparasitic therapy, so these are existing-use confirmations rather than new repurposing. Long-term use requires liver function and blood count monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

