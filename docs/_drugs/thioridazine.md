---
layout: default
title: Thioridazine
parent: Model Prediction Only (L5)
nav_order: 832
evidence_level: L5
indication_count: 10
monitor_inn: "Thioridazine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "major affective disorder", "bipolar disorder", "obsessive-compulsive disorder", "attention deficit-hyperactivity disorder", "schizoid personality disorder", "schizotypal personality disorder"]
last_modified_at: 2026-10-31
description: "Thioridazine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not stated in the India licence records compiled for this report"
---

# Thioridazine
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

## Thioridazine: From Antipsychotic Use to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Thioridazine is a phenothiazine antipsychotic that is marketed in India as single-ingredient oral tablets. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but the data compiled for this report contain **no clinical trials** and only **general or indirect publications** for this disease. Evidence is therefore weak, and a significant cardiac safety concern applies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records compiled for this report |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Thioridazine is a phenothiazine antipsychotic. Antipsychotics of this class are known to block dopamine D2 receptors, and this action is mechanistically plausible for antimanic activity.

Mania and psychotic illness share dopaminergic features, which is why the prediction is biologically reasonable. A 1980 report with another dopamine blocker (pimozide) described improvement in manic patients similar to that seen with phenothiazines, including thioridazine. This is a comparison reference, not a thioridazine efficacy study.

None of the retrieved publications is a thioridazine-specific efficacy study in mania. They are general antipsychotic reviews, pregnancy safety, interaction reports and a cardiac model. The QTc-prolongation liability of thioridazine is a major concern in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for manic bipolar affective disorder.

(For the broader prediction "bipolar disorder", one registered study, NCT02582736, is a retrospective cohort of atypical antipsychotics and hyperglycaemic emergencies. It is a metabolic safety study of a different drug class and gives no efficacy evidence for thioridazine.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Efficacy of typical and atypical antipsychotics for anxiety symptoms, including in bipolar disorder |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatr Pract | Use and safety of antipsychotics during pregnancy |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | J Appl Toxicol | Phenothiazine derivatives and apoptosis; notes use in mania of bipolar disorder |
| [20859110](https://pubmed.ncbi.nlm.nih.gov/20859110/) | 2010 | Review | J Psychiatr Pract | History of early CNS drug development |
| [8448267](https://pubmed.ncbi.nlm.nih.gov/8448267/) | 1993 | Cohort | Biol Psychiatry | Single woman with schizoaffective mania on thioridazine maintenance; timing of manic episodes |
| [6155678](https://pubmed.ncbi.nlm.nih.gov/6155678/) | 1980 | Clinical report | Psychopharmacology | Pimozide improved mania, with magnitude similar to chlorpromazine and thioridazine |
| [11910256](https://pubmed.ncbi.nlm.nih.gov/11910256/) | 2002 | Pharmacokinetic study | J Clin Psychopharmacol | Quetiapine co-administered with thioridazine; safety and pharmacokinetics |
| [38560725](https://pubmed.ncbi.nlm.nih.gov/38560725/) | 2024 | In vitro study | Biol Psychiatry Glob Open Sci | Bipolar-linked CACNA1C mutation causes a cardiac arrhythmia phenotype |
| [3945208](https://pubmed.ncbi.nlm.nih.gov/3945208/) | 1986 | Case report | Med J Aust | Encephalopathy with lithium and thioridazine combined |
| [14252012](https://pubmed.ncbi.nlm.nih.gov/14252012/) | 1964 | Historical report | Ann Med Psychol | Thioridazine with barbiturate and electroshock for psychomotor excitation and manic reactions |

---

## India Market Information

Authorisation records in the data compiled for this report are all single-ingredient oral tablets with a valid status. The records contain no approved-indication text. The list below shows 5 of at least 20 registrations; the full list may be partial.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228060 | Thiozid 50mg Tablet | Strip of 10 tablets | Not stated |
| 220834 | Thioridazine 10mg Tablet (Novartis India Ltd) | Strip of 10 tablets | Not stated |
| 225150 | Tensaril 100mg Tablet | Strip of 10 tablets | Not stated |
| 63261 | Delnil 25 Tablet | Strip of 10 tablets | Not stated |
| 208595 | Shiril 25mg Tablet | Strip of 10 tablets | Not stated |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links thioridazine to contraindication relations with long QT syndrome (including familial), orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, epilepsy, hematologic disease, potassium deficiency disease, neuroleptic malignant syndrome, Alzheimer disease, tardive dyskinesia and lingual-facial-buccal dyskinesia.
- **Cardiac risk:** The retrieved literature includes a report of recurrent major ventricular arrhythmias with thioridazine, and QTc prolongation is a major concern for this indication.
- **Drug interactions:** 282 interactions were recorded. Major-level interactions include bupropion, morphine and lorcaserin. Moderate-level examples include famotidine, epinephrine, hydrocortisone, metformin, pioglitazone, atropine, loperamide and several antidiabetic agents.
- **Reported combination toxicity:** Case reports describe neurotoxicity or encephalopathy when thioridazine is combined with lithium, and a severe toxic reaction with amitriptyline. Lithium is a standard mania treatment, which is directly relevant here.

Please also refer to the package insert, since label warnings and contraindications were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study in the data directly examines thioridazine for manic bipolar affective disorder, so the evidence level is L5 and the TxGNN score is the main support. The documented cardiac risk and the reported neurotoxicity with lithium make the benefit-risk unfavourable compared with established antimanic agents.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved-indication text from the India licences
- Detailed mechanism of action data
- Controlled clinical evidence of thioridazine efficacy in mania, compared with modern standard treatments
- A QTc and ECG monitoring plan, and an assessment of lithium co-treatment risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

