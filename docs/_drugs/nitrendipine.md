---
layout: default
title: Nitrendipine
parent: Model Prediction Only (L5)
nav_order: 600
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Nitrendipine: predicted new indication Migraine disorder (evidence level L5). Approved use: Mild to moderate hypertension"
monitor_inn: "Nitrendipine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension"]
---

# Nitrendipine
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

## Nitrendipine: From Hypertension to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Nitrendipine is a dihydropyridine calcium channel blocker used for mild to moderate hypertension.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no clinical trials** and **no relevant publications** supporting this prediction.
Of the four predicted indications, **pulmonary hypertension** and **Prinzmetal angina** have more supporting data, and they are discussed below for comparison.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mild to moderate hypertension (from pharmacology reference data; the approved indication text on the India licences is blank) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Nitrendipine is known as a dihydropyridine L-type calcium channel blocker. It also shows activity at several Cav1.x channels and at KCa3.1 in pharmacology records. Its efficacy in hypertension is established, and mechanistically it could be applicable to migraine.

Other calcium channel blockers, such as flunarizine and verapamil, are used for migraine prophylaxis. This gives a class-level rationale, based on modulation of cerebrovascular tone and neuronal calcium influx. However, there is no nitrendipine-specific data in migraine. The retrieved literature does not support the prediction. It covers grapefruit juice interactions, a general review of dihydropyridines, and a case of abdominal migraine, and none evaluates nitrendipine in migraine. The high TxGNN score is a computational prediction only.

The second prediction, migraine with brainstem aura, rests on the same calcium channel hypothesis. Some familial hemiplegic migraine subtypes involve CACNA1A channelopathy, but there are no trials or literature for nitrendipine in this rare subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for migraine disorder.

For reference, the only registered trial listed for any predicted indication is under pulmonary hypertension, and it is not relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | Suspended | 2414 | COVID-19 trial of ACE inhibitors/ARBs. It does not test nitrendipine in pulmonary hypertension, so it provides no direct evidence. |

---

## Literature Evidence

Migraine disorder (none of the three papers evaluates nitrendipine in migraine):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15449971](https://pubmed.ncbi.nlm.nih.gov/15449971/) | 2004 | Review | Am J Cardiovasc Drugs | Grapefruit juice interactions with cardiovascular drugs; not about migraine |
| [3319491](https://pubmed.ncbi.nlm.nih.gov/3319491/) | 1987 | Review | Drugs | Second-generation dihydropyridines, including nitrendipine; general pharmacology and indications |
| [9760558](https://pubmed.ncbi.nlm.nih.gov/9760558/) | 1998 | Case report | Neurol Neurochir Pol | Adult abdominal migraine; not related to nitrendipine |

Comparison with other predicted indications:

**Pulmonary hypertension (score 99.14%, Evidence Level L3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2013178](https://pubmed.ncbi.nlm.nih.gov/2013178/) | 1991 | Clinical hemodynamic study | Clin Cardiol | Acute sublingual nitrendipine lowered mean pulmonary artery pressure in 11 patients with pulmonary fibrosis; chronic effects also examined |
| [2468866](https://pubmed.ncbi.nlm.nih.gov/2468866/) | 1988 | Clinical hemodynamic study | J Cardiovasc Pharmacol | 5 mg sublingual nitrendipine lowered blood pressure and right heart pressures in 10 patients with precapillary pulmonary hypertension |
| [2468868](https://pubmed.ncbi.nlm.nih.gov/2468868/) | 1988 | Clinical hemodynamic study | J Cardiovasc Pharmacol | Acute and chronic hemodynamic and antianginal effects in 25 patients with angina and hypertension |
| [2937355](https://pubmed.ncbi.nlm.nih.gov/2937355/) | 1986 | Preclinical (animal) | Am Rev Respir Dis | Nitrendipine reduced pulmonary vascular remodeling and right ventricular hypertrophy in rats exposed to intermittent hypoxia |
| [1339619](https://pubmed.ncbi.nlm.nih.gov/1339619/) | 1992 | Comparative study | Zhonghua Jie He He Hu Xi Za Zhi | Captopril and nitrendipine both lowered pulmonary artery pressure in pigs with acute hypoxic pulmonary hypertension |
| [7712585](https://pubmed.ncbi.nlm.nih.gov/7712585/) | 1994 | Animal study | Zhonghua Jie He He Hu Xi Za Zhi | Nitrendipine, nifedipine and L-arginine helped prevent chronic intermittent hypoxic pulmonary hypertension in rats |

**Prinzmetal angina (score 99.10%, Evidence Level L3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1920816](https://pubmed.ncbi.nlm.nih.gov/1920816/) | 1991 | Clinical study (single-blind, 21 patients) | Jpn Heart J | Anginal attacks fell significantly from 2.1 to 0.7 per day on nitrendipine 10 to 20 mg daily |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Review | Herz | Differential use of calcium antagonists |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 53595 | Cardif 10mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| Registration No. 45718 | Cardif 20mg Tablet | Strip of 10 tablets | Not stated in the licence record |

Both are valid single-ingredient oral products from Concept Pharmaceuticals Ltd.

---

## Safety Considerations

Please refer to the package insert for safety information.

Pharmacology records show nitrendipine binding to calcium channel targets (Cav1.1 to Cav1.4) and KCa3.1. These are target interactions, not drug-drug interactions, and no clinically graded interactions were identified. Grapefruit juice may increase oral bioavailability of dihydropyridines through CYP3A4 inhibition (PMID 15449971). This is a general class caution, not specific to this label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score, but there are no clinical trials, no nitrendipine-specific literature, and no mechanism data. This leaves it at L5, prediction only. The pulmonary hypertension and Prinzmetal angina predictions have more support (L3) and can be treated as research questions. For pulmonary hypertension, the evidence is small and old, and calcium channel blockers are used today only in vasoreactive responders. For Prinzmetal angina, it is a plausible on-class extension, but nitrendipine has no clear advantage over approved agents such as amlodipine, diltiazem or nifedipine.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Cardif products
- Detailed mechanism of action data
- For migraine, nitrendipine-specific preclinical or clinical evidence, or a head-to-head rationale against established calcium channel blockers such as flunarizine
- For pulmonary hypertension or Prinzmetal angina, a controlled study or systematic review, plus a comparison with current standard therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

