---
layout: default
title: Terbutaline
parent: Model Prediction Only (L5)
nav_order: 821
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-03
monitor_inn: "Terbutaline"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
description: "Terbutaline: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Terbutaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Terbutaline: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Terbutaline is a beta-2 adrenergic agonist that is currently marketed in India. The approved indication is not recorded in the local licence data. The TxGNN model predicts it may be useful for **respiratory malformation**. The data compiled for this report include **1 clinical trial** and **13 publications**, but none of them studies this disease directly, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Terbutaline belongs to the beta-2 agonist class. These drugs relax airway smooth muscle and relieve reversible bronchoconstriction.

Beta-2 agonism could plausibly ease the reversible airway narrowing that sometimes accompanies structural airway anomalies. It cannot correct the malformation itself. The high score most likely reflects the model's closeness to other airway diseases, not disease-specific biology.

No cited study tests terbutaline in respiratory malformation. The link is therefore a hypothesis only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Broad pediatric study of the pharmacokinetics, pharmacodynamics and safety of understudied drugs. It may supply terbutaline dosing and safety data in children but does not test efficacy in respiratory malformation. |

---

## Literature Evidence

None of these papers studies respiratory malformation as a treatment target. They are listed for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3281307](https://pubmed.ncbi.nlm.nih.gov/3281307/) | 1988 | RCT | Thorax | Double-blind comparison of subcutaneous adrenaline and terbutaline in 20 patients with acute severe bronchospasm. |
| [1629507](https://pubmed.ncbi.nlm.nih.gov/1629507/) | 1992 | RCT | J Allergy Clin Immunol | Inhaled budesonide compared with inhaled terbutaline on symptoms, lung function and airway inflammation in 14 adults. |
| [12061354](https://pubmed.ncbi.nlm.nih.gov/12061354/) | 2002 | Cohort | Acta Paediatr | Structural central airway stenosis in 14 children (vascular rings, subglottic stenosis). Discusses the differential diagnosis from airway disease. |
| [8327281](https://pubmed.ncbi.nlm.nih.gov/8327281/) | 1993 | Methodological | Pediatr Pulmonol | Flow-volume analysis of lung mechanics in intubated premature infants after terbutaline. |
| [19254906](https://pubmed.ncbi.nlm.nih.gov/19254906/) | 2009 | Cohort | Arch Dis Child | Inhaled budesonide improved reduced airway conductance in infants with cough or wheeze. |
| [42303000](https://pubmed.ncbi.nlm.nih.gov/42303000/) | 2026 | Cohort | Respir Med | Lung function and imaging during long-term treatment of post-infectious bronchiolitis obliterans in infants. |
| [1620986](https://pubmed.ncbi.nlm.nih.gov/1620986/) | 1992 | Cohort | Respiration | Abnormal respiratory impedance in chronic bronchitis was acutely reversed by inhaled terbutaline. |
| [11813927](https://pubmed.ncbi.nlm.nih.gov/11813927/) | 2001 | Case report | Cardiol Young | Oral terbutaline raised fetal heart rate in some fetuses with complete heart block. Not related to the airway. |

---

## India Market Information

Terbutaline is marketed in India as single-ingredient products. All records in the data compiled for this report are valid, and the list below may be partial. The approved indication text is not recorded in the local data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 27654 | Bricanyl 0.5mg Injection (AstraZeneca) | Vial of 1 ml injection | Not stated |
| 140276 | MT 4 Syrup (Abron Healthcare) | Bottle of 100 ml syrup | Not stated |
| 202119 | Somavent Forte AF Tablet (Somatico Pharmacal) | Strip of 10 tablets | Not stated |
| 67051 | Doxofast T 5mg/400mg Tablet (Innovative Pharmaceuticals) | Strip of 10 tablets | Not stated |
| 27321 | Bronchosolvin Syrup (Ipca Laboratories) | Bottle of 60 ml syrup | Not stated |

---

## Safety Considerations

- **Conditions of concern:** The data compiled for this report flag the following conditions as ones where terbutaline may be problematic. This is not label text.
  - hypertension
  - epilepsy
  - diabetes mellitus and hyperglycemia
  - diabetic ketoacidosis
  - potassium deficiency
  - hyperthyroidism and thyrotoxicosis
  - heart conduction disease
  - sudden cardiac arrest
  - myocardial ischemia and coronary artery disease
  - respiratory failure
  - pulmonary edema
  - placental abruption
- **Drug Interactions:** 406 interactions are recorded. Examples:
  - Moderate: epinephrine, clarithromycin, famotidine, loperamide, and several antidiabetic drugs (acarbose, pioglitazone, alogliptin, canagliflozin, chlorpropamide, albiglutide).
  - Moderate: laxatives such as bisacodyl and picosulfuric acid.
  - Minor: corticosteroids such as hydrocortisone, dexamethasone, budesonide and betamethasone.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on the model score alone (0.9952).
- No trial or publication directly studies terbutaline in respiratory malformation.
- Beta-2 agonism cannot treat a structural defect, so any benefit would at most be symptomatic.

**To proceed, the following is needed:**
- Evidence that terbutaline benefits patients with respiratory malformation, such as case series or controlled studies.
- Mechanism of action data and package insert warnings and contraindications for the marketed products.
- A clinical rationale that separates symptomatic relief of reversible bronchoconstriction from any disease-modifying effect.
- Pediatric safety and dosing data, for example from the ongoing understudied-drugs pharmacokinetics study (NCT04278404).

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

