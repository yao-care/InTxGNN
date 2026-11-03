---
layout: default
title: Tiotropium
parent: Model Prediction Only (L5)
nav_order: 839
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-03
monitor_inn: "Tiotropium"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
description: "Tiotropium: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tiotropium: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Tiotropium is an inhaled long-acting anticholinergic bronchodilator that is already marketed in India.
The TxGNN model predicts it may be relevant to **respiratory malformation** (score 0.9995).
Only indirect support exists: **3 clinical trials** in cystic fibrosis and **5 publications** that do not study this condition directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the compiled data. Tiotropium belongs to the long-acting muscarinic antagonist (anticholinergic) class. These drugs relax airway smooth muscle and reduce airflow resistance when delivered by inhalation.

No direct mechanistic link to respiratory malformation was established. Respiratory malformations are structural defects, and bronchodilation would not be expected to correct them. At most it might ease secondary airflow limitation. The trials retrieved for this prediction were most likely matched through disease-ontology proximity, because they study other airway conditions.

The high score is therefore a computational signal only. It should not be read as evidence of clinical benefit.

## Clinical Trial Evidence

None of the trials below enrolled patients with respiratory malformation. All three studied tiotropium in cystic fibrosis, and their relevance to the predicted indication was graded as indirect.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | Completed | 464 | Placebo-controlled trial of tiotropium 5 mcg once daily via Respimat for 12 weeks in cystic fibrosis, testing efficacy and safety |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | Completed | 510 | Placebo-controlled dose-finding study (2.5 mcg and 5 mcg) of tiotropium via Respimat for 12 weeks in cystic fibrosis, assessing lung function, safety and pharmacokinetics |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | Completed | 113 | Safety, tolerability and pharmacokinetics of single and multiple doses (28 days) in children and adolescents/adults with cystic fibrosis |

## Literature Evidence

None of these publications directly studies tiotropium in respiratory malformation.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | RCT | Respiratory Medicine | Tiotropium/olodaterol-induced lung deflation and its effect on cardiocirculatory responses to exercise in patients with chronic airway disease |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Review | Int J Chron Obstruct Pulmon Dis | Role of dual bronchodilation (indacaterol-glycopyrronium) on patient-related outcomes and quality of life |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohort | Respiratory Medicine | Nasal ciliary beating is depressed in subjects with chronic airway disease |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Preclinical | Chemico-biological Interactions | Mechanisms of ventilatory dysfunction in mice exposed to an organophosphorus nerve agent, a cholinergic-pathway model |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Case report | Rev Fac Cienc Med (Córdoba) | COVID-19 in a young patient with pectus excavatum, a chest-wall deformity |

## India Market Information

Tiotropium is marketed in India as a single-ingredient product, and all licences in the compiled data are valid. The list below may be partial, and the approved indication text is not recorded in the local data. Five main authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2361 | Aerotrop 18mcg Rotacap (Macleods) | Packet of 15 rotacaps | Not stated in the records |
| 215127 | Tiova Rotacap (Cipla) | Bottle of 30 rotacaps | Not stated in the records |
| 215189 | Tiate Transhaler (Lupin) | Packet of 180 MDI Transhaler | Not stated in the records |
| 216396 | Tiomist CFC Free 9mcg Inhaler (Zydus Cadila) | Packet of 120 MDI Inhaler | Not stated in the records |
| 206247 | Solbihale T Redicaps (Dr Reddy's) | Packet of 30 redicaps | Not stated in the records |

## Safety Considerations

- **Drug Interactions**: 430 interactions are recorded. The main ones are with other anticholinergic agents, which may add to tiotropium's effects. All are rated Moderate:
  - Hyoscyamine
  - Atropine
  - Glycopyrronium (including topical)
  - Clidinium
  - Dicyclomine
  - Trospium
  - Scopolamine
  - Methscopolamine
  - Propantheline
  - Mepenzolate

  Other moderate interactions are with eluxadoline, prucalopride and inhaled human insulin. Cimetidine is rated Minor.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study has tested tiotropium in respiratory malformation, and a bronchodilator is not expected to correct a structural defect. The high score is a model prediction without supporting clinical data, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a plausible biological rationale for a structural airway disorder
- A clear definition of the target patient population, since respiratory malformation covers heterogeneous conditions
- Any clinical or observational data in patients with the target condition
- Package insert warnings and contraindications for a safety review

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

