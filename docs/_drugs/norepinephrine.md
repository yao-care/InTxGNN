---
layout: default
title: Norepinephrine
parent: Model Prediction Only (L5)
nav_order: 601
evidence_level: L5
indication_count: 3
---

# Norepinephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Norepinephrine: From Acute Hypotension/Shock to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine is an endogenous catecholamine vasopressor, clinically established for managing acute hypotension and shock via α/β-adrenergic receptor activation. The TxGNN model predicts potential relevance to **Obstructive Lung Disease**, supported by **18 clinical trials** and **19 publications** — but nearly all of this evidence is mechanistic or observational rather than direct treatment evidence, and the drug is not currently registered in India.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hypotension / shock (vasopressor) — no India registration record; based on established global clinical use |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (preclinical / mechanistic studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for Norepinephrine in this evidence pack. Based on established pharmacology, Norepinephrine is a direct-acting α1/α2/β1-adrenergic receptor agonist, used clinically as a first-line vasopressor to restore perfusion pressure in acute hypotension and distributive/septic shock.

The predicted link to obstructive lung disease is plausible in principle: sympathetic noradrenergic tone modulates airway smooth muscle and bronchial vascular caliber, and the airway is richly innervated by noradrenergic fibers alongside cholinergic and peptidergic systems. Several older physiology studies also show elevated plasma noradrenaline in COPD patients, correlating with hypoxia and pulmonary hemodynamics.

However, the supporting literature largely characterizes norepinephrine as a **disease-associated biomarker or a component of the body's stress/hypoxic response in COPD**, not as an administered therapeutic agent for airway obstruction. None of the identified clinical trials tested norepinephrine as an intervention for obstructive lung disease — where it appears, it is typically a supportive vasopressor in critically ill patients who happen to have respiratory failure. This suggests the TxGNN score may partly reflect graph co-occurrence between the "norepinephrine" and "COPD/respiratory" nodes rather than a genuine therapeutic signal, and should be interpreted cautiously.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | NA | Completed | 35 | Extracorporeal CO2 removal in hypercapnic COPD patients who failed NIV and refused intubation; norepinephrine is supportive care, not the tested intervention |
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | NA | Completed | 18 | Mechanistic study of endothelial/sympathetic dysfunction underlying exercise intolerance in COPD |
| [NCT01536587](https://clinicaltrials.gov/study/NCT01536587) | Phase 4 | Completed | 32 | Inhaled salmeterol reduces sympathetic (noradrenergic) activity via microneurography in COPD GOLD II/III |
| [NCT07332442](https://clinicaltrials.gov/study/NCT07332442) | Phase 3 | Not yet recruiting | 250 | Arousal threshold and CPAP adherence in obstructive sleep apnea; autonomic/adrenergic mechanism study, no direct NE dosing |
| [NCT04234217](https://clinicaltrials.gov/study/NCT04234217) | NA | Recruiting | 300 | Mechanisms linking sleep apnea to prediabetes; catecholamine pathways implicated but NE not an intervention |
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | NA | Completed | 20 | Inhaled budesonide's non-genomic inhibition of noradrenaline uptake into airway vascular smooth muscle |
| [NCT05664204](https://clinicaltrials.gov/study/NCT05664204) | NA | Recruiting | 200 | Intraoperative ECMO strategy in lung transplantation; NE used as periprocedural vasopressor support |
| [NCT02627378](https://clinicaltrials.gov/study/NCT02627378) | Phase 1 | Completed | 35 | ECMO support for MERS-CoV respiratory failure; NE as supportive hemodynamic therapy only |
| [NCT00834509](https://clinicaltrials.gov/study/NCT00834509) | N/A | Completed | 181 | Blood-based biomarker study for diagnosing obstructive sleep apnea; catecholamines among analytes |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular tone regulation and sympathetic afferent feedback in exercise/hypertension rehabilitation |

**Note:** None of the identified trials evaluate norepinephrine as a treatment for obstructive lung disease itself; it appears either as supportive ICU/perioperative therapy or as a physiological marker.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Cohort | Monaldi Arch Chest Dis | Plasma noradrenaline and hemodynamics measured by right heart catheterization in early-stage COPD |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Review | Am Rev Respir Dis | Autonomic (noradrenergic/cholinergic) nerve control of airway caliber in asthma and COPD |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Observational | Scand J Clin Lab Invest | Elevated plasma noradrenaline in COPD, inversely correlated with arterial oxygen saturation |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Noradrenergic/cholinergic airway innervation contributing to airway narrowing in asthma/COPD |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Observational | Am J Physiol Heart Circ Physiol | Functional sympatholysis (endogenous NE-driven vasoconstriction blunting) is further impaired in COPD during exercise |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Review | Br Med Bull | Sympathetic noradrenaline/NPY constricts, parasympathetic ACh/VIP dilates tracheobronchial vasculature in asthma |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | Overview of catecholamines (norepinephrine, epinephrine, dopamine) in critical illness, including respiratory failure |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Review | Semin Immunol | Sympathetic nervous system–immune interactions relevant to airway inflammation |
| [3420304](https://pubmed.ncbi.nlm.nih.gov/3420304/) | 1988 | Observational | Respiration | Catecholaminergic (dopamine/L-dopa) hemodynamic effects in pulmonary hypertension secondary to COPD |
| [40064568](https://pubmed.ncbi.nlm.nih.gov/40064568/) | 2024 | Preclinical (animal) | Nature | Brainstem noradrenergic (Dbh+) neurons control allergen-induced airway hyperreactivity in mice |

---

## India Market Information

Norepinephrine currently has **no registered products** in the India regulatory dataset used for this evaluation (0 licenses, market status: Not Marketed). No authorization or product-level information is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 70 documented moderate-severity interactions (DDInter), concentrated in antidiabetic agents — including Metformin, insulin analogs (aspart, degludec, detemir), GLP-1 receptor agonists (Dulaglutide, Semaglutide, Albiglutide), DPP-4 inhibitors (Alogliptin, Linagliptin, Saxagliptin, Sitagliptin), SGLT2 inhibitors (Canagliflozin, Dapagliflozin, Empagliflozin), sulfonylureas (Chlorpropamide, Repaglinide), a thiazolidinedione (Pioglitazone), and sympathomimetic appetite suppressants (Phentermine, Diethylpropion). These interactions reflect norepinephrine's hyperglycemic/sympathomimetic effects, which may counteract glycemic control from these agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked indication (obstructive lung disease) is supported only at evidence level L4 — mechanistic and observational studies showing norepinephrine as a disease-associated biomarker, not as a tested treatment. No clinical trial evaluates norepinephrine as an intervention for airway obstruction, and the drug has no registration or market presence in India. The two lower-ranked candidates (respiratory malformation, Rienhoff syndrome) are L5 with negligible-to-zero supporting evidence and should not be pursued further.

**To proceed, the following is needed:**
- Resolve Blocking gap DG001: obtain official label warnings/contraindications before any safety pre-screening (S1) can begin
- Resolve High-priority gap DG002: confirm detailed mechanism-of-action data via DrugBank/primary pharmacology sources
- A targeted mechanistic or preclinical study directly testing norepinephrine (or adrenergic pathway modulation) in an airway obstruction model, since current literature is associative rather than interventional
- Independent review of whether the TxGNN score reflects a true therapeutic signal or a knowledge-graph co-occurrence artifact (biomarker confound), given the pattern seen across all three predicted indications for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

