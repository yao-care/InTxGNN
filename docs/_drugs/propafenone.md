---
layout: default
title: Propafenone
parent: Model Prediction Only (L5)
nav_order: 706
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Propafenone: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Atrial fibrillation"
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "catecholaminergic polymorphic ventricular tachycardia", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "incessant infant ventricular tachycardia", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Propafenone: From Atrial Fibrillation and Ventricular Tachycardia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Propafenone is a class IC antiarrhythmic originally used for atrial fibrillation and ventricular tachycardia.
The TxGNN model's top-ranked prediction is **manic bipolar affective disorder**, but the supporting literature (**3 publications, 0 clinical trials**) describes propafenone as a *cause* of mania and psychosis, not a treatment. This prediction is most likely a graph artifact and should not be pursued.
A far more credible candidate in the same prediction list is **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, which is discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; ventricular tachycardia (the India licence record has no approved indication text) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propafenone is a class IC antiarrhythmic (sodium channel blocker), and its efficacy in atrial fibrillation and ventricular tachycardia is established. No plausible therapeutic mechanism links it to mania.

The available literature points the other way. A 1985 case report describes mania secondary to propafenone, and the authors note a chemical relationship to the antidepressant bupropion. A 2001 case report describes an organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar disorder. A 2020 review covers harmful interactions between antipsychotics and cardiovascular drugs.

The high TxGNN score appears to be driven by the psychiatric adverse-event association rather than evidence of benefit. The signal points toward potential harm.

### A more credible alternative: CPVT

Among the other predictions, **catecholaminergic polymorphic ventricular tachycardia** (score 99.79%, evidence level L3) has a strong mechanistic rationale. CPVT is caused by gain-of-function ryanodine receptor (RyR2) variants. Preclinical studies show that propafenone, like flecainide, inhibits RyR2 channels and suppresses diastolic Ca²⁺ waves (PMIDs 21270101, 26121139, 21798265). A case report describes 35 years of effective propafenone treatment (PMID 30820400). No registered trials or RCTs were found. Flecainide is the better-established class IC option, so propafenone would be an alternative or second-line consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacological Reports | Harmful interactions between antipsychotics and cardiovascular drugs in patients with bipolar disorder or schizophrenia and cardiovascular comorbidity |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | Organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar disorder |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Mania secondary to propafenone, a previously unrecognized complication |

None of these studies show a therapeutic benefit in bipolar disorder.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 174927 | Pradil 150 Tablet (Emcure Pharmaceuticals Ltd) | Strip of 10 tablets (oral) | Not specified in the licence record |

## Cytotoxicity

Not applicable. Propafenone is not an antineoplastic drug, so this section is omitted from the assessment.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease associations, not package-insert text):
  - Cardiac: long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary artery disease and atherosclerosis, hypotensive disorders
  - Haematological: agranulocytosis, neutropenia (including congenital forms), hemoglobinopathy
  - Neuromuscular: myasthenia gravis and other neuromuscular junction diseases
  - Organ and metabolic: kidney disease, liver disease, gallbladder disease, potassium deficiency
- **Drug interactions:** 190 interactions were identified. Major-level interactions include **dolasetron** and **eliglustat**. Moderate-level interactions include famotidine, cimetidine, clarithromycin, levofloxacin, ondansetron, palonosetron, bupropion, aprepitant, loperamide and alosetron. Metronidazole is minor.
- **Psychiatric effects:** Published case reports link propafenone to mania and psychosis, which is directly relevant to this predicted indication.
- **Package insert:** Warnings and contraindications from the India package insert were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold** (for manic bipolar affective disorder)

**Rationale:**
The prediction rests on model score alone, and the only literature describes propafenone causing mania and psychosis. There are no clinical trials and no plausible mechanism, so the evidence points toward harm rather than benefit.

**Other predictions in the same list:**
- **CPVT** (L3): worth pursuing as a research question, given the RyR2 mechanism and a long-term case report.
- **Incessant infant ventricular tachycardia** (L3): old, small observational pediatric evidence, also a research question. Proarrhythmia risk in children limits it.
- **Arrhythmogenic right ventricular cardiomyopathy** (L4): Hold. The literature reports propafenone-induced QRS widening and incessant VT, which are safety concerns.
- **Periodic paralysis with transient compartment-like syndrome, Prinzmetal angina, nephrogenic syndrome of inappropriate antidiuresis and trichotillomania** (L5): Hold. No trials or literature exist, and only the model prediction supports them.

**To proceed with any indication, the following is needed:**
- India package insert warnings and contraindications (a blocking data gap)
- Mechanism of action data from DrugBank
- For CPVT: a propafenone-specific systematic review, and a comparison with flecainide covering beta-blocking and negative inotropic effects and structural-heart-disease contraindications
- For any psychiatric use: no further work is advised unless new evidence of benefit emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

