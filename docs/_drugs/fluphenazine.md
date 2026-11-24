---
layout: default
title: Fluphenazine
parent: Model Prediction Only (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Fluphenazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "myopia X-linked", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
description: "Fluphenazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). In India: 12 listed products (12 not discontinued)"
---

# Fluphenazine
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

## Fluphenazine: Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Fluphenazine is a phenothiazine antipsychotic, originally used for psychotic disorders including schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**,
but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (12 of 12) – CDSCO approval status is not included in this data |
| Number of Listed Products | 12 (valid: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for fluphenazine: "Fluphenazine hydrochloride has activity at all levels of the central nervous system as well as on multiple organ systems. The mechanism whereby its therapeutic action is exerted is unknown." ([DailyMed: Fluphenazine Hydrochoride (fluphenazine hydrochloride) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91b85b8d-4c10-4395-915e-272b81ef3b12), label version 2026-07-03; accessed 2026-11-19.) Based on known information, fluphenazine is a high-potency phenothiazine and a dopamine D2 receptor antagonist. Its efficacy in psychotic disorders and schizophrenia is well established.

Mechanistically, no plausible pathway connects D2 antagonism to inherited retinal degeneration. Retinal dystrophies are generally genetically driven, and no data compiled for this report links fluphenazine to the causal genes or pathways. The high TxGNN score (0.9999) should be read as a model output, not as biological validation.

The model also produced other high-scoring predictions, such as syndromic myopia, X-linked myopia and several rare neurodevelopmental or metabolic disorders. None of these has supporting trials or publications. The only prediction with any literature is **manic bipolar affective disorder**. It sits close to fluphenazine's existing psychiatric uses and is therefore an adjacent indication rather than a true repurposing. Even there, the literature is indirect (reviews of long-acting injectable antipsychotics, case reports) and contains no fluphenazine-specific trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

All registrations are valid, with no cancelled licences. The registration data lists no approved indication text.

<!-- review:begin in-lic-20261106-fluphenazine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twelve valid single-ingredient registrations exist, with no cancelled licences." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-fluphenazine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 7089 | Anatensol Decanoate 25mg Injection | Vial of 1 ml Injection | Valid |
| 7771 | Arkane 2mg Tablet | Strip of 10 tablets | Valid |
| 84857 | F Tensil 25mg Injection | Vial of 1 ml Injection | Valid |
| 85612 | Fludecan 25mg Injection | Vial of 2 ml Injection | Valid |
| 135318 | Monazine Injection | Vial of 1 ml Injection | Valid |
| 135507 | Medipax 25mg Injection | Ampoule of 1 ml Injection | Valid |
| 175233 | Phenasol 25mg Injection | Vial of 1 ml Injection | Valid |
| 175287 | Phenate 25mg Injection | Ampoule of 1 ml Injection | Valid |
| 179181 | Phenodec 25mg Injection | Vial of 1 ml Injection | Valid |
| 179558 | Phenasol 25mg Injection | Vial of 1 Injection | Valid |
| 180783 | Phenvator 25mg Injection | Vial of 1 Injection | Valid |
| 216178 | Tripnor 0.5 mg/10 mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

The registrations are mostly 25 mg injections, plus Arkane 2 mg tablets (licence 7771) and Tripnor 0.5 mg/10 mg tablets (licence 216178), a combination with nortriptyline.

<!-- review:begin in-lic-20261124b-fluphenazine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The remaining registrations are mostly 25 mg injections, plus Tripnor 0.5 mg/10 mg tablets (licence 216178)." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-fluphenazine-1 -->

---

## Safety Considerations

Package insert warnings and label contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

- **Disease-level contraindications (knowledge graph, not label text)**:
  - Cardiovascular: long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, orthostatic hypotension.
  - Haematological: neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anaemia.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm.
  - Other: liver disease, gallbladder disease, hyperglycaemia, benign prostatic hyperplasia, substance abuse/dependence, obesity, female breast carcinoma.
- **Drug Interactions**: 313 interactions were identified. The two **Major** interactions listed are bupropion and morphine. Moderate interactions include antidiabetics (metformin, pioglitazone, acarbose, alogliptin, albiglutide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), anticholinergics (atropine, hyoscyamine), loperamide, epinephrine, famotidine and amphotericin B.
- **Population concern**: Phenothiazines carry neurological adverse effects such as extrapyramidal symptoms. This would need careful consideration in any neurological or paediatric genetic population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. No trials or publications exist, and no mechanistic link to retinal dystrophy is identified. The safety profile (QT prolongation, blood dyscrasias, neurological effects) is substantial, so there is no basis to advance this indication.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking dopamine D2 antagonism, or other fluphenazine pharmacology, to retinal degeneration, tested in preclinical models.
- Detailed mechanism of action data (MOA).
- Package insert warnings and contraindications for the Indian products.
- A benefit-risk assessment in the target population, including cardiac and haematological monitoring.
- If the team wants a near-term research question, reprioritise toward the adjacent indication of manic bipolar affective disorder. It has indirect literature support, but fluphenazine-specific data would still be needed.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fluphenazine Hydrochoride (fluphenazine hydrochloride) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91b85b8d-4c10-4395-915e-272b81ef3b12) |
| 2026-11-24 | Revised: wording about the earlier partial table and hard-coded counts | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

