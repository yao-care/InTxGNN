---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 481
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Leuprolide: predicted new indication Osteoarthritis (evidence level L5). Approved use: Endometriosis"
monitor_inn: "Leuprolide"
predicted_indications: ["osteoarthritis", "pseudoachondroplasia"]
---

# Leuprolide
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

## Leuprolide: From Endometriosis to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Leuprolide is a GnRH agonist, originally used for endometriosis and precocious puberty.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **0 clinical trials** and only **1 publication** (an unrelated case report) behind this prediction, so it rests on **model output alone**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the data compiled for this report lists endometriosis, endometriosis of uterus, precocious puberty, aromatase excess syndrome and familial male-limited precocious puberty; Indian licence entries contain no approved indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for leuprolide: "Leuprolide acetate, a gonadotropin releasing hormone (GnRH) agonist, acts as an inhibitor of gonadotropin secretion when given continuously in therapeutic doses. Animal and human studies indicate that after an initial stimulation, chronic administration of leuprolide acetate results in suppression of testicular and ovarian steroidogenesis." ([DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f), label version 2026-04-30; accessed 2026-11-19.) Based on general pharmacology, leuprolide is a GnRH agonist. It suppresses the pituitary-gonadal axis and lowers sex steroid levels, which is why it works in estrogen-driven conditions such as endometriosis and in precocious puberty.

For osteoarthritis, however, **no established mechanistic link** was found. Estrogen deficiency is generally associated with worse joint health (for example, higher osteoarthritis risk after menopause), and GnRH agonist therapy can reduce bone mineral density. This points to **potential harm rather than benefit**.

The very high TxGNN score (0.997) is a computational prediction only. The one publication retrieved is a case report of metastatic prostate cancer mimicking inflammatory breast cancer. It does not address osteoarthritis. The second-ranked prediction, pseudoachondroplasia (score 0.9969), also has no plausible mechanistic link and no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostate adenocarcinoma in a 78-year-old man presented with skin changes mimicking inflammatory breast carcinoma. Not relevant to osteoarthritis. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 29892 | Bdsure 3.75mg Injection | Vial of 1 injection | Not stated |
| 124422 | Luprova 22.5mg Injection | Vial of 1 injection | Not stated |
| 73419 | Endorelin 3.75mg Injection | Vial of 1 injection | Not stated |
| 96852 | Gonadoreg 3.75mg Injection | Vial of 2 ml injection | Not stated |
| 127312 | Lutrate 3.75mg Injection | Vial of 1 injection | Not stated |

All 20 registrations are valid single-ingredient injectable products. None are cancelled.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, obesity (including monogenic obesity), stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, hemoglobinopathy, and urinary tract obstruction.
- **Drug Interactions**: 261 interactions were recorded. Major-level interactions include **dolasetron** and **cisapride**. Many moderate-level interactions involve antidiabetic drugs (e.g. acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, linagliptin, metformin, saxagliptin), as well as famotidine, loperamide, clarithromycin, bisacodyl and other laxatives.
- Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no clinical trials, and the single retrieved publication is unrelated. Known pharmacology (estrogen suppression and bone density loss) suggests possible harm to joint and bone health in osteoarthritis.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic assessment
- Package insert warnings and contraindications from the Indian regulatory source
- Preclinical or clinical evidence that GnRH agonism has any benefit in osteoarthritis
- Safety review of bone density loss and cardiometabolic risks, given the contraindication-related conditions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

