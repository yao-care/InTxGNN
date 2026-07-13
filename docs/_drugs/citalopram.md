---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Citalopram: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) established for the treatment of major depressive disorder.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **28 clinical trials** and **16 publications** currently supporting this direction — primarily through evidence from its active enantiomer, Escitalopram, with direct Citalopram studies also available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the regulatory record. Based on known pharmacological information, Citalopram is a selective serotonin reuptake inhibitor (SSRI) that blocks the serotonin transporter (SERT), raising synaptic serotonin concentrations across limbic and cortical regions. This makes it pharmacologically identical in class to agents already FDA-approved for OCD (fluoxetine, fluvoxamine, paroxetine, sertraline).

OCD's core pathophysiology involves dysfunction of the cortico-striato-thalamo-cortical (CSTC) circuit, tightly coupled with serotonergic dysregulation. Because serotonin modulation directly addresses the neurobiological substrate of OCD, SSRIs are the universally recommended first-line pharmacological treatment across major international guidelines. Critically, Citalopram's active S-enantiomer — Escitalopram — has been evaluated in multiple completed Phase 3 and Phase 4 trials specifically for OCD, providing a strong mechanistic bridge for inference.

Importantly, direct Citalopram evidence exists: PMID 10572334 examined Citalopram in treatment-resistant adult OCD (randomized open-label, n=16), and PMID 12839522 evaluated Citalopram specifically in pediatric and adolescent OCD (open-label, n=15). These studies, while small and older, confirm the drug's activity in the target indication. The prediction is therefore mechanistically sound, class-supported, and backed by preliminary direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized double-blind comparison of conventional (20 mg) vs. high-dose (40 mg) Escitalopram in OCD; evaluated via Y-BOCS, HAM-D, CGI — largest Escitalopram OCD dose-ranging trial |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized comparison of group CBT vs. Fluoxetine (SSRI class) for OCD including patients with comorbidities; demonstrates SSRI class efficacy in real-world OCD populations |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | International multi-center naturalistic follow-up (US, Brazil, India, Netherlands) examining clinical, neurocognitive, and neuroimaging predictors of OCD treatment response |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Pediatric OCD partial SRI responders; assessed whether augmentation with CBT (by psychologists or psychiatrists) improves SRI treatment outcomes |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label high-dose Escitalopram (up to 50 mg) for OCD outpatients; 18-week titration study with Y-BOCS-guided dose escalation |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | SSRIs vs. ERP vs. combination therapy in Chinese OCD population; identified biological and psychological predictors of treatment response |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Head-to-head comparison of Clomipramine vs. Escitalopram for OCD; explored pharmacogenomic and clinical predictors of medication response |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assessed efficacy and optimal dose of Escitalopram for OCD; directly applicable to Citalopram via enantiomer relationship |
| [NCT04336228](https://clinicaltrials.gov/study/NCT04336228) | Phase 4 | Active, not recruiting | 46 | Investigates serotonin system status in compulsive behavior and mechanistic effects of sub-chronic Escitalopram on 5-HT function and goal-directed vs. habitual cognition |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study evaluating safety and effectiveness of Escitalopram in OCD symptom reduction |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Open-label Trial | European Psychiatry | **Direct Citalopram evidence**: Randomized open-label trial of Citalopram vs. Citalopram + Clomipramine in 16 treatment-resistant adult OCD patients (90 days); provides direct efficacy signal for this drug-disease pair |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label Trial | Psychiatry & Clinical Neurosciences | **Direct Citalopram evidence**: 8-week open-label study of Citalopram (20–30 mg/day) in 15 children and adolescents with OCD; assessed efficacy and tolerability via CY-BOCS |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review | Int Clinical Psychopharmacology | Review specifically examining Citalopram's role in OCD beyond depression; covers serotonin neurobiology and OCD pharmacological rationale |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Network Meta-analysis | J Psychiatric Research | Network meta-analysis comparing pharmacological vs. psychological treatments (alone and combined) for OCD in children and adolescents; establishes SSRI class superiority benchmarks |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Comprehensive Psychiatry | Long-term safety and tolerability of off-label high-dose SRIs in OCD; directly relevant to Citalopram dosing strategy and cardiac monitoring (QTc) |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Antidepressant (including SSRI) efficacy, tolerability, and suicidality in children and adolescents across multiple psychiatric indications including OCD; synthesizes safety data |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affective Disorders | OCD shows reduced placebo response compared to other anxiety disorders; antidepressant effect sizes in OCD remain robust; methodological reference for trial design |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clinical Evidence | Comprehensive OCD clinical evidence review; confirms SSRIs as first-line treatment and characterizes clinical course and treatment response rates in adults and children |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Clinical Study | CNS Spectrums | BDNF Val66Met polymorphism impact on Escitalopram/Paroxetine response in OCD; pharmacogenomic predictors relevant to personalized Citalopram dosing |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biological Psychiatry | Mechanistic review of OCD neurobiology: serotonin system, frontal-basal ganglia-thalamo-cortical circuitry, and pharmacological rationale for serotonergic interventions |

---

## India Market Information

Citalopram currently has **no registered products** in India (CDSCO). There are 0 active market authorizations on file.

> Any clinical development program or market entry for Citalopram in the OCD indication would require a new drug application submitted to CDSCO, as there is no existing regulatory foothold to build upon.

---

## Safety Considerations

**Drug Interactions**: Citalopram has 414 documented drug-drug interactions. Clinically significant interactions include:

- **Major**: Bupropion, Omeprazole, Lorcaserin, Cimetidine, Cisapride, Clarithromycin, Dexfenfluramine, Diethylpropion, Dolasetron
- **Moderate**: Famotidine, Loperamide, Morphine, Acetylsalicylic acid (Aspirin), Bisacodyl, Chlorpropamide, Acetohexamide, Dronabinol, Castor oil

> Warnings and contraindications data were not available in the current Evidence Pack. Please refer to the package insert (obtainable from CDSCO or the originator company) for full safety information before any clinical use or protocol design.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Citalopram's SSRI mechanism directly addresses the serotonergic pathology underlying OCD, its active enantiomer (Escitalopram) has been studied in multiple completed Phase 3/4 OCD trials, and direct Citalopram evidence in OCD exists in the published literature. The evidence base is sufficient to justify advancing to a formal development assessment, though the absence of India market presence and incomplete safety documentation require remediation before proceeding.

**To proceed, the following is needed:**

- Obtain and review the full package insert for Citalopram to resolve the blocking safety data gap (key warnings and contraindications)
- Query DrugBank API for complete mechanism of action documentation
- Assess QTc prolongation risk at higher OCD doses (Citalopram carries a known dose-dependent cardiac risk not shared equally by Escitalopram)
- Determine whether Citalopram or Escitalopram is the preferred development candidate for India, given Escitalopram's larger and more recent OCD-specific trial base
- Map a CDSCO regulatory pathway for a novel indication filing given zero existing India registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

