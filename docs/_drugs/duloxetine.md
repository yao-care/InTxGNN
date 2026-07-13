---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Duloxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Duloxetine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) established for major depressive disorder, generalized anxiety disorder, and several chronic pain conditions. The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, supported by **1 completed Phase 4 clinical trial** and **10+ publications** including a double-blind RCT — making OCD the highest-evidence repurposing target in this analysis. (Note: While benign paroxysmal torticollis of infancy ranks #1 by TxGNN score (99.85%), it carries no clinical trial or literature evidence (L5/Hold); OCD ranks #3 (99.84%) but has the strongest actionable evidence at L2.)

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder, Generalized Anxiety Disorder, Chronic Pain (diabetic neuropathic pain, fibromyalgia, musculoskeletal pain) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Duloxetine is a balanced dual-acting SNRI that simultaneously inhibits the serotonin transporter (SERT) and norepinephrine transporter (NET), elevating synaptic concentrations of both 5-HT and norepinephrine across multiple brain circuits. This dual mechanism underlies its regulatory approvals in MDD, GAD, and several pain conditions. Detailed DrugBank MOA data was not retrieved in this analysis and should be supplemented from the DrugBank API.

OCD is neurobiologically characterised by hyperactivity in the orbitofrontal cortex (OFC)–caudate nucleus–thalamus circuit, with serotonin system dysregulation as the primary pharmacological target — precisely the rationale for SSRIs being first-line OCD therapy. Duloxetine's SERT inhibition provides the same 5-HT tone enhancement as SSRIs. Critically, its additional NET inhibition strengthens norepinephrine signalling in the prefrontal cortex, which may improve cognitive inhibition and executive control — offering a mechanistic advantage in SSRI-refractory patients where pure serotonergic agents have failed. PMID 27811556, a double-blind RCT, directly validates this augmentation hypothesis in treatment-resistant OCD.

The mechanistic overlap between duloxetine's approved indications (anxiety and mood disorders) and OCD is substantial. Both domains involve amygdala hyperresponsiveness and serotonin-mediated fear/threat processing. Multiple case series, open-label studies, and at least one double-blind RCT have now documented OCD symptom reduction with duloxetine, placing it among the best-evidenced SNRI repurposing candidates in the psychiatric space.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Directly assessed duloxetine efficacy in OCD; the most relevant registered trial for this indication |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Investigated medication response predictors in OCD; duloxetine evaluated as an alternative arm alongside clomipramine and escitalopram |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Individual patient data meta-analysis of antidepressant efficacy across anxiety disorders; duloxetine included as a comparator drug |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | Double-blind RCT | J Clin Psychopharmacol | Duloxetine augmentation produced statistically significant OCD symptom improvement in SSRI-resistant patients |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Evaluated efficacy and tolerability of antidepressants across paediatric psychiatric disorders including OCD; includes duloxetine-class data |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | Demonstrated OCD has lower antidepressant and placebo response than other anxiety disorders; calibrates expectations for effect sizes |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label study | Int J Neuropsychopharmacol | Prospective open-label trial of duloxetine in DSM-IV OCD; demonstrated clinically meaningful symptom reduction |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Systematic Review | Front Psychiatry | Comprehensive systematic review of duloxetine use in psychiatric disorders beyond approved indications, including OCD evidence synthesis |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Systematic Review | Expert Opin Pharmacother | Updated review of serotonergic antidepressants in OCD; summarises double-blind evidence and confirms 5-HT system centrality |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical Review | J Clin Psychiatry | Critical appraisal of SNRI anti-obsessional properties as SSRI alternatives; discusses venlafaxine and clomipramine data with implications for duloxetine |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Case Report | Cureus | Supratherapeutic-dose duloxetine combined with CBT achieved sustained remission in a decade-long treatment-resistant OCD case with comorbid MDD |
| [22567604](https://pubmed.ncbi.nlm.nih.gov/22567604/) | 2012 | Case Report | Innov Clin Neurosci | Suprathreshold duloxetine achieved remission in treatment-resistant OCD with comorbid anorexia and depression; discusses dose-response considerations |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case Report | Prim Care Companion J Clin Psychiatry | First reported case of OCD responding specifically to duloxetine after inadequate SSRI response |

---

## India Market Information

Duloxetine currently has **no registered licenses** in the India dataset provided. The market status is recorded as "Not Marketed" with zero authorizations. This represents a data gap that should be cross-checked against the CDSCO drug registration database, as duloxetine is commercially available in several markets under brand names such as Cymbalta.

---

## Safety Considerations

**Drug Interactions (329 total interactions identified):**

Major interactions requiring avoidance or close monitoring:

| Severity | Interacting Drug | Clinical Concern |
|---------|-----------------|-----------------|
| **Major** | Bupropion | Combined serotonergic/noradrenergic load; seizure and serotonin syndrome risk |
| **Major** | Lorcaserin | Serotonin syndrome risk (5-HT2C agonism + SNRI) |
| **Major** | Diethylpropion | CNS stimulant interaction; cardiovascular and serotonergic risk |
| **Major** | Dolasetron | QTc prolongation and serotonin syndrome risk |
| **Major** | Dexfenfluramine | Serotonin syndrome (historical agent; avoid combination) |
| **Moderate** | Epinephrine | Enhanced cardiovascular effects due to NE reuptake inhibition |
| **Moderate** | Morphine | Additive CNS depression; possible serotonin syndrome |
| **Moderate** | Acetylsalicylic acid | Increased bleeding risk (platelet 5-HT depletion + antiplatelet effect) |
| **Moderate** | Cimetidine | CYP1A2/CYP2D6 inhibition may increase duloxetine plasma levels |
| **Minor** | Famotidine, Ranitidine, Rabeprazole | Gastric pH changes with minimal clinical impact |

Please refer to the official prescribing information for complete warnings and contraindications — these were not retrieved in this analysis and represent a blocking data gap (DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 4 clinical trial directly evaluating duloxetine in OCD, combined with a double-blind RCT demonstrating efficacy in treatment-resistant OCD augmentation, provides sufficient clinical evidence to justify moving beyond a pure research stage. The serotonergic mechanism is well-founded, and convergent evidence from open-label studies, case series, and systematic reviews corroborates the signal.

**To proceed, the following is needed:**
- Retrieve official prescribing information (warnings and contraindications) from CDSCO or international sources (DG001 — currently Blocking)
- Retrieve detailed MOA data from DrugBank API to support mechanistic analysis (DG002 — currently High severity)
- Confirm actual duloxetine registration status in India via CDSCO database (market_status may be underreported in this dataset)
- Conduct a larger, adequately powered RCT specifically targeting OCD as the primary endpoint (current Phase 4 trial: N=20, which limits statistical conclusions)
- Develop a safety monitoring plan addressing the 329 known drug interactions — particularly serotonin syndrome risk with co-prescribed serotonergic or stimulant agents
- Consult a clinical psychiatrist specialising in OCD for dosing strategy (supratherapeutic doses may be required per case evidence)
- Ensure all published content includes YMYL disclaimer: *"Results are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application."*

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing predictions require independent clinical validation prior to any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

