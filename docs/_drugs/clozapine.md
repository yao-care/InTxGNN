---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "Malan overgrowth syndrome"]
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Clozapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Clozapine: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic with a broad receptor profile, marketed in India as oral tablets.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**,
with **1 clinical trial** and **20 publications** currently listed for this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, clozapine acts on several receptor systems, including D2 and 5-HT2A antagonism, together with muscarinic and adrenergic activity. This broad profile plausibly supports antimanic and mood-stabilizing effects.

Mania and the psychotic conditions clozapine is known for share overlapping dopaminergic and serotonergic circuitry. A completed Phase 2 double-blind trial in treatment-resistant mania and a 2020 systematic review and meta-analysis of clozapine in bipolar disorder point in the same direction. However, the evidence comes mostly from refractory populations, so it should not be generalised to all patients with mania.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of clozapine's safety and efficacy in treatment-resistant mania, with a companion pathophysiology study |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic review/Meta-analysis | Journal of Psychiatric Research | Assesses clinical efficacy and adverse-effect profile of clozapine in bipolar disorder |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disorders | Efficacy and safety of clozapine in treatment-resistant bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort / meta-analytic comparison | The Lancet Psychiatry | Transdiagnostic effectiveness and safety of clozapine versus other antipsychotics across psychiatric disorders |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based options for managing a manic episode, including choice of mood stabilizer and antipsychotic |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Molecular Psychiatry | Treatment-resistant bipolar disorder in acute and maintenance phases |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bulletin of the Menninger Clinic | Newer treatments for bipolar disorder rest largely on case reports and case series |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disorders | Overview of what is known about clozapine in bipolar disorder and next steps |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Modelling study | Drug Design, Development and Therapy | Clozapine drug interactions and individualized dosing in bipolar disorder |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series | Clinical Neuropharmacology | 36 patients given ECT with clozapine; 67% benefited and the combination was mostly well tolerated |
| [9448668](https://pubmed.ncbi.nlm.nih.gov/9448668/) | 1998 | Review | Journal of Clinical Psychiatry | Role of antipsychotics, including clozapine, in bipolar disorder |

## India Market Information

At least 20 licences are recorded, all valid single-ingredient products, and the list may be partial. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 82346 | Ericloza 100 Tablet | Strip of 10 tablets | Not specified |
| 205850 | Sizolam 100mg Tablet | Strip of 10 tablets | Not specified |
| 1409 | Alkepin Odt 50mg Tablet | Strip of 10 tablets | Not specified |
| 45310 | Clonex 50mg Tablet | Strip of 10 tablets | Not specified |
| 193052 | Restopax 50mg Tablet | Strip of 15 tablets | Not specified |

## Safety Considerations

- **Drug Interactions**: 449 interactions are recorded. Major-level examples include bupropion, morphine and potassium citrate. Moderate-level examples include metformin, pioglitazone, omeprazole, famotidine, atropine and epinephrine.
- **Conditions flagged as contraindication-related** (not taken from label text): epilepsy, liver disease, neutropenia, agranulocytosis, leukopenia, diabetes mellitus, diabetic ketoacidosis, hyperglycemia, orthostatic hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest, stroke, pulmonary embolism, respiratory failure, angle-closure glaucoma, paralytic ileus and benign prostatic hyperplasia.
- **Literature-noted risks**: agranulocytosis and blood-count monitoring, myocarditis and cardiomyopathy, seizures, and metabolic risk.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind trial and a systematic review and meta-analysis directly address clozapine in mania and bipolar disorder. The evidence is small, concentrated in treatment-refractory patients, and carries serious safety demands.

**To proceed, the following is needed:**
- Larger controlled trials in mania, beyond treatment-resistant groups
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Indian products
- A monitoring plan covering neutrophil counts, cardiac effects, seizures and metabolic risk, with use restricted to refractory cases
- A drug-interaction management plan

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

