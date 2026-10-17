---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 708
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Hypertension, atrial fibrillation, hypertrophic cardiomyopathy…"
monitor_inn: "Propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
---

# Propranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Propranolol: From Hypertension and Cardiac Arrhythmias to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker, originally used for hypertension, atrial fibrillation, hypertrophic cardiomyopathy and infantile hemangioma.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on the model score alone.
The report also covers two better-supported alternatives from the same prediction list: **cirrhotic cardiomyopathy** (3 publications) and **cardiomyopathy** (19 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, hypertrophic cardiomyopathy, hemangioma (the India licence records contain no indication text) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propranolol is a non-selective beta-blocker (it blocks beta-1 and beta-2 receptors) whose efficacy in cardiovascular conditions such as hypertension, arrhythmia and hypertrophic cardiomyopathy is well established.

For the top-ranked prediction, **no mechanistic link is supported by the data compiled for this report**. Tateyama-type distal myopathy is a rare skeletal muscle disorder, and there is no known pathway by which beta-adrenergic blockade would address its pathology. The high score (0.994) is a model output only. Notably, the knowledge graph lists myopathy and skeletal muscle disease among propranolol's contraindications, which argues against this prediction.

The other predictions differ in plausibility:
- **Congenital myopathy with excess of thin filaments** (score 99.30%): no mechanistic link, no trials, no literature.
- **Hypertrophic cardiomyopathy due to intensive athletic training** (99.17%): there is a plausible link through reduced heart rate and contractility, because propranolol is already used in hypertrophic cardiomyopathy. However, this athlete's-heart phenotype is a physiological adaptation usually managed by detraining, and no studies were found.
- **Chondroma** (99.14%): no clear link, no evidence.
- **Cirrhotic cardiomyopathy** (99.12%): propranolol is widely used in cirrhosis for portal hypertension, and one 2024 report suggests it can correct prolonged QT intervals. Other work shows blunted cardiovascular effects in severe disease and possible harm to circulatory and renal function in refractory ascites, so benefit and risk both depend on disease stage.
- **Cardiomyopathy** (99.12%): this overlaps largely with the existing hypertrophic cardiomyopathy indication, and beta-blockade has different considerations in other forms, such as systolic dysfunction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for the top-ranked prediction or for any of the other five predictions.

---

## Literature Evidence

**Top-ranked prediction (distal myopathy, Tateyama type):** Currently no related literature available.

**Cirrhotic cardiomyopathy (rank 5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Clinical study | Front Pharmacol | Propranolol may correct prolonged QT intervals, which are common in cirrhosis |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Clinical study | PLoS One | Real-time propranolol infusion studied across degrees of cirrhosis severity; cardiovascular effects of beta-blockers were blunted in more severe disease |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical study | J Hepatol | Non-selective beta-blockers impaired circulatory homeostasis and renal function in refractory ascites |

**Cardiomyopathy (rank 6, selected from the retrieved literature)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical hemodynamic study | Eur Heart J | Effects of propranolol and verapamil on diastolic stiffness in hypertrophic cardiomyopathy |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical hemodynamic study | Br Heart J | Nifedipine plus propranolol appeared superior to nifedipine alone in 12 patients with hypertrophic obstructive cardiomyopathy |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical study | Am J Cardiol | Propranolol and arrhythmia in hypertrophic cardiomyopathy |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Clinical study | Cardiology | Propranolol and disopyramide effects on left ventricular function at rest and during exercise in hypertrophic cardiomyopathy |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Clinical study | Br Heart J | Propranolol effects on myocardial oxygen consumption and haemodynamics in hypertrophic obstructive cardiomyopathy |
| [28431779](https://pubmed.ncbi.nlm.nih.gov/28431779/) | 2017 | Drug monograph/Review | Profiles Drug Subst Excip Relat Methodol | Propranolol is a non-cardioselective beta-blocker used in hypertension, arrhythmias and hypertrophic cardiomyopathy |

Most of the cardiomyopathy literature concerns hypertrophic cardiomyopathy, which is already an established indication, and part of it consists of generic drug monographs. It therefore adds little new evidence.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 68981 | DavaIndia Propranolol 40mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 164232 | Oslol 10 Tablet | Strip of 10 tablets | Not stated in the licence record |
| 39327 | Capinol LA 40mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 175129 | Provanol SR 60 Tablet | Strip of 10 sustained-release tablets | Not stated in the licence record |
| 25747 | Betacap TR 40 Capsule | Strip of 10 prolonged-release capsules | Not stated in the licence record |

All 20 registrations are valid single-ingredient products; none are cancelled. Some are fixed combinations or low-dose variants, as their names suggest (for example Megcool F, Flunorm P and Zeflurin Plus). All are oral formulations.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (drug-disease edges, not package insert text): the graph links propranolol to 30 conditions, including:
- Muscle disorders: myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, myasthenia gravis
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, gout, hyperparathyroidism, hypercalcemia
- Liver and kidney: liver disease, hepatic coma and encephalopathy, kidney disease, anuria
- Others: bronchitis, pancreatitis, gallbladder disease, systemic lupus erythematosus, anxiety disorders

The muscle-related entries are directly relevant to the top-ranked prediction, since it is a myopathy.

**Drug Interactions:** 307 interactions were found. The main ones are:
- **Major:** epinephrine
- **Moderate:** bupropion, morphine, cimetidine, canagliflozin, chlorpropamide, lorcaserin, atropine and other anticholinergics, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- **Minor:** aspirin, ascorbic acid, magnesium oxide

Please also refer to the package insert for official warnings, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, distal myopathy of the Tateyama type, rests on a model score alone (evidence level L5). There are no trials or literature, no plausible mechanism, and the knowledge graph lists myopathy as a contraindication. Of the other predictions, cirrhotic cardiomyopathy is the only one with a plausible link and recent literature (L4), but that evidence is indirect and mixed, with signals of possible harm in advanced disease. It is best treated as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator. This is a blocking gap for safety screening.
- Mechanism of action data, which would allow a proper mechanistic analysis.
- For cirrhotic cardiomyopathy: prospective or randomised data that stratify by cirrhosis severity and ascites status, and a clear benefit-risk assessment.
- Any preclinical or clinical rationale for beta-blockade in Tateyama-type distal myopathy; without it, this prediction should not be pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

