---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Citalopram: predicted new indication Obsessive-compulsive disorder (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder…"
monitor_inn: "Citalopram"
predicted_indications: ["obsessive-compulsive disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder"]
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From Depression and Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI), originally used to treat depressive and anxiety disorders.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **4 related clinical trials** and **16 publications** currently supporting this direction. However, most of the trial evidence supports the SSRI class rather than citalopram specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder, unipolar depression, endogenous depression, major depressive disorder (the Indian licence records contain no approved indication text) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (see note in the Conclusion) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, citalopram is a selective serotonin reuptake inhibitor (SSRI). Its efficacy in depression and anxiety disorders is established.

OCD is known to respond to drugs that inhibit serotonin reuptake. Other SSRIs, such as fluoxetine, are established OCD therapies, and fluoxetine was the comparator drug in one of the trials listed below. Citalopram shares this mechanism, so it is mechanistically plausible for OCD, which is consistent with the high TxGNN score.

An important caveat: the Phase 3 trial evidence supports the serotonin reuptake inhibitor class and treatment strategy in OCD rather than citalopram itself. Citalopram-specific data come mainly from open-label and small studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Cognitive behavioral therapy added to serotonin reuptake inhibitor treatment in children with OCD who only partially responded; supports the class, and citalopram is not confirmed as the study drug |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Exposure and response prevention, SSRIs, and their combination in OCD, with predictors of response in a Chinese population |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Group cognitive behavioral therapy versus fluoxetine in OCD; fluoxetine, not citalopram, is the drug arm |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | Not applicable | Completed | 43 | Pilot study of gut microbiota in OCD patients versus healthy controls, before and after 12 weeks of SSRI treatment; not an efficacy trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomized open-label trial (n=16) | European Psychiatry | Citalopram alone versus citalopram plus clomipramine in treatment-resistant OCD |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Single-blind study | J Clin Psychopharmacol | Compared the antiobsessional efficacy of fluvoxamine, paroxetine, and citalopram in 30 OCD patients |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Cohort | CNS Drugs | Preliminary look at the relationship between citalopram concentrations and clinical response in OCD |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | Open pilot study | Acta Psychiatr Scand | 24-week open pilot study of citalopram in OCD |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label study (pediatric, n=15) | Psychiatry Clin Neurosci | 8-week citalopram treatment (mean 24 mg/day) in children and adolescents with OCD |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Open-label trial (pediatric, n=23) | J Child Adolesc Psychopharmacol | Significant Y-BOCS improvement after 10 weeks of citalopram (30 → 21, p<0.001) |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review/Commentary | Int Clin Psychopharmacol | Reviews the link between serotonin reuptake inhibitors and OCD, focusing on citalopram |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | OCD is responsive to psychological and serotonergic treatment; discusses neurobiology |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Review | Curr Med Chem | Past, present, and future drugs for OCD, with SSRIs central to treatment |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Overview of OCD epidemiology, course, and treatment |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 51897 | Citadelm 20mg Tablet | Strip of 10 tablets | Not specified |
| 46198 | Cytop 20mg Tablet | Strip of 10 tablets | Not specified |
| 42439 | Cita 40mg Tablet | Strip of 10 tablets | Not specified |
| 41468 | C Pram 5mg Tablet | Strip of 10 tablets | Not specified |
| 49382 | Citosys 10mg Tablet | Strip of 10 tablets | Not specified |

There are 20 valid single-ingredient registrations in total, all oral tablets.

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not label text): long QT syndrome (including familial form), torsades de pointes, epilepsy, bipolar disorder and major affective disorder, liver disease, gallbladder disease, potassium deficiency, blood coagulation disease, heart and cardiovascular disease, neuroleptic malignant syndrome, inappropriate ADH syndrome (including nephrogenic form), and serotonin syndrome.
- **Drug interactions**: 414 interactions were found in total. Examples of those classed as Major include bupropion, omeprazole, cimetidine, cisapride, clarithromycin, lorcaserin, dexfenfluramine, diethylpropion, and dolasetron. Moderate examples include famotidine, loperamide, morphine, acetylsalicylic acid, and bisacodyl.

Please also refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
OCD responds well to serotonin reuptake inhibition, and citalopram has multiple small open-label and single-blind studies in both adults and children, plus a favorable mechanistic fit. The L1 grading rests on a completed Phase 3 trial that supports the SRI class and strategy rather than citalopram specifically. Citalopram-specific evidence is therefore weaker than the label suggests, and the cardiac (QT) risks need to be managed.

**To proceed, the following is needed:**
- Citalopram-specific randomized controlled trial data in OCD
- Package insert warnings and contraindications from Indian sources (currently missing and blocking safety screening)
- Detailed mechanism of action data
- A QT/ECG monitoring plan and a drug interaction management plan, especially for patients with cardiac disease or taking QT-prolonging drugs
- Safety planning for pediatric use, since much of the available citalopram data comes from children and adolescents

**Other predicted indications (not recommended at present):** schizotypal, schizoid, histrionic, and paranoid personality disorders all have **Hold** decisions. They have no clinical trials, and the identical TxGNN scores (99.68%) suggest a class-level graph artifact. For paranoid personality disorder, three retrieved papers are only indirectly related.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

