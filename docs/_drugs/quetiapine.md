---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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

# Quetiapine: From Schizophrenia and Bipolar Disorder to Retinal Dystrophy

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
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, quetiapine is an atypical antipsychotic. Its efficacy in schizophrenia and bipolar disorder is established. Its receptor pharmacology is generally described as dopamine D2 and serotonin 5-HT2A antagonism, with histamine H1 and alpha-1 adrenergic blockade.

Inherited retinal dystrophies are genetic degenerative conditions of the retina. From the data compiled for this report, no plausible mechanistic link can be established between quetiapine's receptor pharmacology and the pathology of these conditions. The high score (rank 7,551 in the model's overall ranking) reflects a pattern in the knowledge graph rather than demonstrated biology. This prediction should be treated as a hypothesis only.

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

For context, among the top 10 predicted indications, **trichotillomania** (score 99.38%) has the most supporting evidence. It has six publications, mostly case reports and reviews, including quetiapine-specific reports (PMIDs 19142421, 12405081). It has no registered trials and sits at L4, so it is a research question rather than an actionable indication. The other predictions, such as congenital glycosylation disorders, structural brain malformations and X-linked myopia, are also unsupported.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a mechanistic assessment
- A literature and preclinical search specific to retinal dystrophy, to show any biological plausibility
- Package insert warnings and contraindications from Indian regulatory sources, for safety screening
- If a better-supported candidate is wanted, a more focused evaluation of trichotillomania, starting with a verified review of the case-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

