---
layout: default
title: Desvenlafaxine
parent: Model Prediction Only (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Desvenlafaxine: predicted new indication Obsessive-compulsive disorder (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
---

# Desvenlafaxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI), originally used to treat depressive disorders (unipolar depression, major depressive disorder) and anxiety disorder.
The TxGNN model's top-ranked prediction is **Obsessive-Compulsive Disorder (OCD)**, but this prediction currently has **no registered clinical trials** and only **3 general or indirect publications** behind it, so it remains a research question.
The only prediction with direct clinical trial support is **Dysthymic Disorder**, which has **2 small completed trials** and **2 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (the licence records compiled for India contain no approved indication text) |
| Predicted New Indication | Obsessive-compulsive disorder (top-ranked prediction); dysthymic disorder is the best-supported prediction |
| TxGNN Prediction Score | 99.91% (OCD); 99.73% (dysthymic disorder) |
| Evidence Level | L4 (OCD); L3 (dysthymic disorder) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold for OCD (research question); Proceed with Guardrails for dysthymic disorder |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for desvenlafaxine are not available in the data compiled for this report. Based on known information, desvenlafaxine is an SNRI, a class that blocks reuptake of serotonin and norepinephrine. Its efficacy in major depressive disorder is established.

**Obsessive-compulsive disorder:** Serotonergic modulation is the mechanistic basis of OCD pharmacotherapy (SSRIs and clomipramine), so a plausible link exists. However, evidence for the SNRI class in OCD is weaker and less consistent than for SSRIs, and no desvenlafaxine-specific data were found. The literature identified is a review of serotonergic antidepressants in OCD, a review of postpartum depression that mentions OCD only as a later complication, and a study of risperidone augmentation in somatic symptom disorder. All of these are indirect.

**Dysthymic disorder:** This is a chronic, less severe depressive condition closely related to major depressive disorder, and monoaminergic reuptake inhibition is the shared mechanism. A meta-analysis supports antidepressant efficacy in dysthymia as a class. Direct desvenlafaxine data are limited to two small studies and do not by themselves establish drug-specific efficacy.

**Other predictions:** Several other predictions (histrionic, schizoid, paranoid and schizotypal personality disorders, Ohdo syndrome, benign paroxysmal torticollis of infancy, agoraphobia) have no clinical trials or literature. Their high scores appear to be computational outputs only. Agoraphobia has a plausible class-level link, since serotonergic and noradrenergic antidepressants are effective in panic and related anxiety disorders. Melancholia is a severe subtype of major depressive disorder, which is already an approved indication, so it is largely an overlap with the existing label rather than true repurposing.

---

## Clinical Trial Evidence

**Obsessive-compulsive disorder:** Currently no related clinical trials registered.

**Dysthymic disorder (best-supported prediction):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01537068](https://clinicaltrials.gov/study/NCT01537068) | Phase 4 | Completed | 59 | Desvenlafaxine vs placebo in chronic depression (dysthymic disorder); placebo-controlled but small |
| [NCT01948895](https://clinicaltrials.gov/study/NCT01948895) | N/A | Completed | 30 | 8-week open-label, flexible-dose desvenlafaxine monotherapy in dysthymia; uncontrolled, supportive only |

**Melancholia (overlaps with the approved MDD indication):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Phase 4 | Completed | 53 | Effects of treatment on decision-making in major depression; a cognitive outcome study that does not isolate the melancholic subtype |

---

## Literature Evidence

**Obsessive-compulsive disorder:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Review of double-blind studies of serotonergic antidepressants in OCD, supporting the role of the serotonin system |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression; OCD is noted as a possible later complication (indirect) |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical study | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder (indirect to OCD) |

**Dysthymic disorder:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Meta-analysis of placebo-controlled randomized trials of antidepressants in dysthymia |
| [28064115](https://pubmed.ncbi.nlm.nih.gov/28064115/) | 2017 | Observational study | J Affect Disord | Continuation treatment with the SNRI duloxetine in persistent depression and effects on symptoms and functioning |

**Melancholia / major depressive disorder (selected):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36813043](https://pubmed.ncbi.nlm.nih.gov/36813043/) | 2023 | RCT | J Affect Disord | Multicenter, double-blind trial of desvenlafaxine XR vs duloxetine in MDD (non-inferiority design) |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Network meta-analysis | Mol Psychiatry | Antidepressants for maintenance-phase MDD |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic review | Lancet | Network meta-analysis of cardiometabolic and physiological effects of antidepressants |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guideline | Clin Pharmacol Ther | CPIC pharmacogenetic guideline for serotonin reuptake inhibitor antidepressants, including desvenlafaxine |
| [19057238](https://pubmed.ncbi.nlm.nih.gov/19057238/) | 2008 | Pharmacology study | J Psychiatr Pract | Effect of desvenlafaxine on the CYP2D6 enzyme system |

---

## India Market Information

Desvenlafaxine is marketed in India with 20 valid single-ingredient registrations (no cancelled registrations). The licence records compiled for this report do not include approved indication text. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 65334 | Desteyn Plus 100mg/0.5mg Tablet ER | Strip of 10 extended-release tablets | Not stated in the data |
| 60249 | Defmind 50mg Tablet | Strip of 10 tablets | Not stated in the data |
| 60632 | Dexfin 50 Tablet ER | Strip of 10 extended-release tablets | Not stated in the data |
| 234579 | Venpower 100mg Tablet | Strip of 10 tablets | Not stated in the data |
| 58319 | D-Veniz 50 Tablet ER | Strip of 10 extended-release tablets | Not stated in the data |

All forms are oral tablets (extended-release, prolonged-release or standard).

---

## Safety Considerations

- **Disease-level cautions (from knowledge-graph contraindication associations, not package insert text):** hypertension and hypertensive disorder, epilepsy, bipolar disorder and major affective disorder, liver disease, impaired renal function, gallbladder disease, blood coagulation disease, hypertriglyceridemia, ocular hypertension and angle-closure glaucoma, cardiovascular and heart disease, cerebrovascular disorder, neuroleptic malignant syndrome, inappropriate ADH syndrome (including the nephrogenic form), interstitial lung disease, and serotonin syndrome.
- **Drug Interactions:** 184 interactions were identified in total. Major-level interactions in the listed results include **bupropion, lorcaserin, dexfenfluramine, fenfluramine, diethylpropion, mazindol, dolasetron and granisetron**, which largely reflect serotonergic or related risks. Moderate-level examples include epinephrine, ephedrine, morphine, acetylsalicylic acid, dronabinol and mannitol; cimetidine is minor.
- **Other considerations:** Antidepressant-induced activation could theoretically be a concern in paranoid personality disorder. Desvenlafaxine is not approved for pediatric use. Package insert warnings and contraindications were not available for this report, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold (OCD, the top-ranked prediction, treated as a research question); Proceed with Guardrails (dysthymic disorder, the best-supported prediction)**

**Rationale:**
- For OCD, the high TxGNN score rests on a plausible serotonergic link, but there are no trials, the SNRI class evidence is weak, and the literature found is indirect, so evidence is L4 at best.
- For dysthymic disorder, direct data come from one small Phase 4 placebo-controlled trial (n=59) and one small open-label study (n=30), plus class-level meta-analytic support. This is L3 evidence that does not establish desvenlafaxine-specific efficacy.
- The remaining predictions (personality disorders, Ohdo syndrome, benign paroxysmal torticollis of infancy, agoraphobia) have no supporting evidence and should stay on hold. Melancholia mostly duplicates the existing MDD indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian-market products (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- For OCD: a systematic search for desvenlafaxine or SNRI-specific OCD trials, and a comparison with established SSRI evidence
- For dysthymic disorder: review of the published results of NCT01537068 and NCT01948895, and an adequately powered controlled trial
- A safety monitoring plan covering blood pressure, bipolar-disorder screening, serotonergic drug interactions, and hepatic and renal function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

