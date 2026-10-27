---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Absence epilepsy, congestive heart failure, open-angle glaucoma…"
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
---

# Acetazolamide
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

## Acetazolamide: From Absence Epilepsy, Glaucoma and Heart Failure to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor originally used for conditions such as absence epilepsy, congestive heart failure, glaucoma (open-angle and angle-closure) and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy, congestive heart failure, open-angle glaucoma, angle-closure glaucoma, altitude sickness (the product labels in the India data have no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetazolamide is a carbonic anhydrase inhibitor. Its efficacy in glaucoma, altitude sickness and as an adjunct diuretic is established, and mechanistically it may influence acid-base balance and muscle ion handling.

A link to exercise-induced malignant hyperthermia is plausible but unverified. The data compiled for this report contain no trials or literature on this condition, so the prediction rests on the model score alone.

Other predicted indications were also reviewed. The only one with any literature is **cardiomyopathy** (rank 7, L4, "Research Question"). That literature includes reviews, a case report on correcting hypochloremia in advanced heart failure, and a rabbit ischemia-reperfusion study, and none of it is cardiomyopathy-specific. Several other predictions (intestinal obstruction, myopathic intestinal pseudo-obstruction, cirrhotic cardiomyopathy) carry signals of potential harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for exercise-induced malignant hyperthermia.

For reference, the closest related literature (cardiomyopathy, a separate predicted indication):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | 2024 update on heart failure management; not specific to acetazolamide |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Advances in cardiovascular pharmacology in 2022, including mavacamten for obstructive HCM |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | J Cardiol Cases | Acetazolamide used to treat hypochloremia in advanced heart failure with hypertrophic cardiomyopathy |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case report (adverse event) | Acute Med Surg | Non-cardiogenic pulmonary edema after IV acetazolamide |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Preclinical (animal) | Saudi Med J | Effects of acetazolamide on ischemia-reperfused isolated rabbit hearts |

## India Market Information

Twenty valid single-ingredient registrations are listed; the main ones are shown below. None of them has approved indication text in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 60301 | Diamox ER 500 Capsule (Sun Pharmaceutical Industries Ltd) | Strip of 15 extended-release capsules | Not listed |
| Registration No. 2332 | Avva 250mg Tablet SR (Intas Pharmaceuticals Ltd) | Strip of 10 sustained-release tablets | Not listed |
| Registration No. 3222 | Actamide 250mg Tablet (Micro Labs Ltd) | Strip of 10 tablets | Not listed |
| Registration No. 12121 | AT Zol 250mg Tablet (Medivision Pharm) | Strip of 10 tablets | Not listed |
| Registration No. 107801 | Iopar-SR Capsule (FDC Ltd) | Strip of 10 sustained-release capsules | Not listed |

All products are oral formulations (tablets, sustained-release tablets and capsules, extended-release capsules).

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver failure, liver disease, kidney disease, hematologic disease, gallbladder disease, gout, diabetes mellitus (type 1 and type 2), diabetic ketoacidosis, respiratory failure, renal tubular acidosis, and adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia).
- **Drug Interactions**: 165 interactions were identified. Examples include Major interactions with acetylsalicylic acid and cisapride. Moderate interactions include antidiabetic agents (acarbose, chlorpropamide, alogliptin, canagliflozin, dapagliflozin, dulaglutide), corticosteroids (dexamethasone, betamethasone, beclomethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil). Doxycycline is a Minor interaction.
- **Signals from the literature**: case reports describe acetazolamide-induced adynamic ileus and non-cardiogenic pulmonary edema after intravenous use. In cirrhosis, acetazolamide can precipitate hyperammonemia and encephalopathy.

Package insert warnings were not available for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for exercise-induced malignant hyperthermia is supported only by the model score (99.95%), with no trials or publications, so evidence is L5. Safety information is also incomplete, because package insert warnings were not obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India product labels (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or clinical evidence directly linking carbonic anhydrase inhibition to exercise-induced malignant hyperthermia
- Assessment of whether the better-supported cardiomyopathy direction (L4) merits a dedicated research question, with attention to the pulmonary edema and ileus safety signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

