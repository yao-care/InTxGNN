---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Quetiapine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "Quetiapine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "distal 17p13.3 microdeletion syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "trichotillomania", "syndromic myopia", "myopia 26, X-linked, female-limited"]
---

# Quetiapine
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

## Quetiapine: From Schizophrenia and Bipolar Disorder to retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Quetiapine is an atypical antipsychotic originally used to treat schizophrenia and bipolar disorder.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**,
but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; bipolar disorder (including manic bipolar affective disorder and major affective disorder). The Indian licence records list no indication text. |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for quetiapine: "The mechanism of action of quetiapine in the listed indications is unclear. However, the efficacy of quetiapine in these indications could be mediated through a combination of dopamine type 2 (D 2 ) and serotonin type 2A (5HT 2A ) antagonism." ([DailyMed: Quetiapine Extended Release (quetiapine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6953175c-78ec-442c-b91d-97dfb57db933), label version 2026-10-08; accessed 2026-11-19.) Based on known information, quetiapine is an atypical antipsychotic. Its efficacy in schizophrenia and bipolar disorder is established. Its receptor pharmacology is generally described as dopamine D2 and serotonin 5-HT2A antagonism, with histamine H1 and alpha-1 adrenergic blockade.

Inherited retinal dystrophies are genetic degenerative conditions of the retina. From the data compiled for this report, no plausible mechanistic link can be established between quetiapine's receptor pharmacology and the pathology of these conditions. The high score (rank 7,551 in the model's overall ranking) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Quetiapine is marketed in India as single-ingredient oral tablets, in both immediate-release and sustained-release (SR) forms. There are 20 valid registrations and none cancelled. Five are shown below. The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 183101 | Qtripil 50mg Tablet | Strip of 10 tablets | Arinna Lifescience Pvt Ltd |
| 177775 | Pine 50mg Tablet | Strip of 10 tablets | Suraksha Pharma Pvt Ltd |
| 183623 | Q-Zac 50 SR Tablet | Strip of 10 SR tablets | Dorris Pharmaceutical Pvt Ltd |
| 182912 | Quel 100 Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |
| 208161 | Sera 200mg Tablet SR | Strip of 10 SR tablets | Curelogic Pharma |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: Associations were found with the following conditions:
  - Cardiovascular: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, long QT syndrome (including familial), torsades de pointes, myocardial infarction.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm.
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypothyroidism (including myxedema and congenital hypothyroidism), potassium deficiency, hyperlipidemia (including familial), hypertriglyceridemia, obesity (including monogenic obesity).
  - Haematological: neutropenia, agranulocytosis.
  - Other: liver disease, gallbladder disease, female breast carcinoma.
- **Drug Interactions**: 356 interactions were identified. The two **Major** interactions among those listed are **bupropion** and **morphine**. Other interactions are Moderate, including:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, albiglutide, chlorpropamide.
  - Anticholinergic agents: atropine, hyoscyamine, glycopyrronium, clidinium.
  - Others: epinephrine, famotidine, loperamide, aprepitant, dexamethasone, lorcaserin, bisacodyl.

Please also refer to the package insert for label-based warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature and no identifiable mechanistic link. Quetiapine also carries notable cardiometabolic and haematological safety signals, which raise the bar for any new use.

For context, among the top 10 predicted indications, **trichotillomania** (score 0.9938) has the most supporting evidence. It has six publications, mostly case reports and reviews, including quetiapine-specific reports (PMIDs 19142421, 12405081). It has no registered trials and sits at L4, so it is a research question rather than an actionable indication. The other predictions, such as congenital glycosylation disorders, structural brain malformations and X-linked myopia, are also unsupported.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a mechanistic assessment
- A literature and preclinical search specific to retinal dystrophy, to show any biological plausibility
- Package insert warnings and contraindications from Indian regulatory sources, for safety screening
- If a better-supported candidate is wanted, a more focused evaluation of trichotillomania, starting with a verified review of the case-level evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Quetiapine Extended Release (quetiapine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6953175c-78ec-442c-b91d-97dfb57db933) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

