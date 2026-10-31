---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L2). Approved use: Not stated in the India registration data compiled for this report"
monitor_inn: "Clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "psychotic disorder", "Malan overgrowth syndrome"]
---

# Clozapine
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

## Clozapine: From Treatment-Resistant Psychosis to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic marketed in India as 20 single-ingredient tablet products. It is best known for treatment-resistant schizophrenia, although the registrations compiled for this report carry no indication text.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **1 completed Phase 2 trial** and **20 publications** (including a 2020 systematic review and meta-analysis) supporting this direction.
The strongest direct evidence is for treatment-refractory bipolar disorder, a closely related condition, where a completed Phase 3 placebo-controlled trial exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India registration data compiled for this report |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails (restricted to treatment-refractory cases) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, clozapine has a broad receptor profile: dopamine D2 and serotonin 5-HT2A antagonism, plus muscarinic and adrenergic activity. This profile plausibly supports antimanic and mood-stabilising effects.

Mania and psychosis share dopaminergic and serotonergic features, and antipsychotics are widely used in acute mania. Clozapine is usually reserved for patients who have not responded to, or cannot tolerate, conventional treatments. The available evidence is accordingly concentrated in refractory populations.

Related predictions in the same disease family are also supported. Bipolar disorder (general) has the strongest package: a completed Phase 3 pediatric trial, a Phase 2 trial and a 2020 meta-analysis. Psychotic disorder and schizophreniform disorder are close to clozapine's established use, so "repurposing" is a limited framing there. The remaining predictions (Tourette syndrome, trichotillomania, ADHD, Malan overgrowth syndrome) have weak or no supporting evidence, and some literature suggests clozapine may induce tic-like or obsessive-compulsive symptoms.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of clozapine efficacy and pathophysiology in treatment-resistant mania |

Related trials in the broader bipolar disorder prediction (not specific to manic episodes):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00036582](https://clinicaltrials.gov/study/NCT00036582) | Phase 3 | Completed | 116 | Clozapine vs placebo in treatment-refractory bipolar disorder in children and adolescents |
| [NCT02562287](https://clinicaltrials.gov/study/NCT02562287) | Phase 4 | Unknown | 54 | Randomised comparison of clozapine vs olanzapine, quetiapine or risperidone in treatment-resistant bipolar disorder |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1254 | Intensified pharmacological treatment (including clozapine) after first-line failure in schizophrenia, major depression and bipolar depression |
| [NCT06011460](https://clinicaltrials.gov/study/NCT06011460) | N/A | Enrolling by invitation | 30 | Registry of adverse events during clozapine treatment in bipolar disorder |
| [NCT04580134](https://clinicaltrials.gov/study/NCT04580134) | Phase 4 | Recruiting | 524 | Randomised double-blind biotype-based clozapine response study in psychosis |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic review/Meta-analysis | J Psychiatr Res | Assessed clinical efficacy and adverse effects of clozapine in bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort/Effectiveness study | Lancet Psychiatry | Transdiagnostic effectiveness and safety of clozapine vs other antipsychotics across psychiatric disorders |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disord | Efficacy and safety of clozapine in treatment-resistant bipolar disorder |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based treatment options for bipolar mania |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Mol Psychiatry | Treatment-resistant bipolar disorder, including inadequate response in acute mania |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series | Clin Neuropharmacol | 36 patients on combined ECT and clozapine; 67% benefited, adverse reactions in 16.6% |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Dosing/DDI study | Drug Des Devel Ther | Model-informed precision dosing and drug interactions of clozapine in bipolar disorder |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 82346 | Ericloza 100 Tablet | Strip of 10 tablets | Not specified |
| 205850 | Sizolam 100mg Tablet | Strip of 10 tablets | Not specified |
| 1409 | Alkepin Odt 50mg Tablet | Strip of 10 tablets | Not specified |
| 45310 | Clonex 50mg Tablet | Strip of 10 tablets | Not specified |
| 193052 | Restopax 50mg Tablet | Strip of 15 tablets | Not specified |

20 valid single-ingredient registrations in total; all are oral tablets.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease-level associations, not label text): neutropenia, agranulocytosis, leukopenia, epilepsy, liver disease, heart conduction disease, coronary artery disease, sudden cardiac arrest, paralytic ileus, angle-closure glaucoma, benign prostatic hyperplasia, orthostatic hypotension, diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hyperlipidaemia, obesity, stroke and cerebrovascular disorders, pulmonary embolism, and respiratory failure.
- **Drug interactions**: 449 interactions are recorded. Examples classed as Major include bupropion, morphine and potassium citrate. Moderate examples include metformin, pioglitazone, omeprazole, cimetidine, famotidine, epinephrine, atropine and glycopyrronium.
- **Guardrails identified in the evidence review**: absolute neutrophil count (ANC) monitoring for agranulocytosis, myocarditis, seizures, metabolic risk, and constipation or ileus. Literature also notes clozapine may induce obsessive-compulsive symptoms.

Please refer to the package insert for label warnings, as no label text was available.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind trial in treatment-resistant mania and a 2020 meta-analysis support clozapine in bipolar disorder, and the stronger related bipolar package includes a completed Phase 3 placebo-controlled trial. However, trials are small, partly paediatric, and heterogeneous, and clozapine carries serious risks. Use should be limited to treatment-refractory cases under specialist supervision, so this is a research-stage candidate rather than a broad recommendation.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian registrations (currently missing, and a blocking gap for safety screening)
- Approved indication text for the Indian registrations
- Detailed mechanism of action data
- A monitoring plan covering ANC/haematology, cardiac (myocarditis), seizure and metabolic risk
- Confirmation of results for the Phase 3 and Phase 4 bipolar trials, and larger adult trials in refractory mania
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

