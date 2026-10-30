---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-10-30
description: "Acetazolamide: predicted new indication exercise-induced malignant hyperthermia (evidence level L5). Approved use: Relations recorded in the knowledge graph: absence epilepsy…"
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

## Acetazolamide: From Glaucoma and Heart Failure Uses to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor, with known uses in absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, and altitude sickness.
The TxGNN model ranks **hypertrophic cardiomyopathy** as its top prediction with literature support (score 0.9993), but the evidence consists only of general heart failure reviews and one case report, with **0 clinical trials** and **3 publications**, none of which studies the disease directly in a controlled way.
This is an early prediction from the TxGNN model (deep learning) and not a validated new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph: absence epilepsy, congestive heart failure, open-angle glaucoma, angle-closure glaucoma, altitude sickness (the local licence records contain no indication text) |
| Predicted New Indication | Hypertrophic cardiomyopathy (the overall top-ranked prediction is exercise-induced malignant hyperthermia, which has no supporting evidence) |
| TxGNN Prediction Score | 0.9993 (hypertrophic cardiomyopathy); 0.9995 (exercise-induced malignant hyperthermia) |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 licences (the list may be partial), all valid single-ingredient products |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, acetazolamide inhibits carbonic anhydrase, which alters acid-base balance and fluid handling. In heart failure it is used as an adjunct diuretic to aid decongestion and to correct metabolic alkalosis.

The only link to hypertrophic cardiomyopathy is indirect, through the heart failure phenotype. It is not a disease-modifying effect on the cardiomyopathy itself. The retrieved publications are general heart failure updates and a single case report of hypochloremia treated with acetazolamide in an advanced heart failure patient who also had hypertrophic cardiomyopathy. None provides data specific to hypertrophic cardiomyopathy.

Because no cited study directly addresses hypertrophic cardiomyopathy as a treatment target, the evidence level is capped at L5, which is a model prediction only. The 0.9993 score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and it does not demonstrate efficacy.

The other top predictions are weaker still:
- **Exercise-induced malignant hyperthermia, congenital myopathy with excess of thin filaments, distal myopathy (Tateyama type), glycogen storage disease (late-onset acid maltase deficiency):** no trials or literature.
- **Hypertrophic cardiomyopathy due to intensive athletic training:** a physiological adaptation that is generally not treated with drugs.
- **Cirrhotic cardiomyopathy:** acetazolamide carries a risk of hyperammonemia and encephalopathy in cirrhosis, so this is a safety concern rather than an opportunity.
- **Intestinal obstruction and intestinal pseudoobstruction:** the literature reports acetazolamide-induced ileus, which points in the opposite direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Publications retrieved for hypertrophic cardiomyopathy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | 2024 heart failure update covering guideline changes; not specific to acetazolamide or hypertrophic cardiomyopathy |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Overview of new cardiovascular drugs in 2022, including mavacamten for obstructive hypertrophic cardiomyopathy; no acetazolamide data |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | J Cardiol Cases | Acetazolamide treated hypochloremia in an advanced heart failure patient who also had hypertrophic cardiomyopathy |

For the broader category of cardiomyopathy, a preclinical study ([22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/), 2012, Saudi Med J) examined acetazolamide in ischemia-reperfused isolated rabbit hearts. A case report ([29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/), 2017, Acute Med Surg) described non-cardiogenic pulmonary edema after intravenous acetazolamide in a patient with dilated cardiomyopathy, which is an adverse event signal.

## India Market Information

At least 20 valid single-ingredient licences are on record, and the list may be partial. The records contain no approved indication text. Five main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 12121 | AT Zol 250mg Tablet | Strip of 10 tablets | Not stated in the record |
| Registration No. 2332 | Avva 250mg Tablet SR | Strip of 10 sustained-release tablets | Not stated in the record |
| Registration No. 60301 | Diamox ER 500 Capsule | Strip of 15 extended-release capsules | Not stated in the record |
| Registration No. 3222 | ACTAMIDE 250MG TABLET | Strip of 10 tablets | Not stated in the record |
| Registration No. 107801 | Iopar-SR Capsule | Strip of 10 sustained-release capsules | Not stated in the record |

All available forms are oral.

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure, liver disease, kidney disease, hematologic disease, gallbladder disease, gout, type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, respiratory failure, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), renal tubular acidosis and pyoureter.
- **Drug interactions:** 165 interactions were found. Major ones include acetylsalicylic acid and cisapride. Moderate ones include antidiabetic drugs (acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin), corticosteroids (betamethasone, dexamethasone, beclomethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil). Doxycycline is a minor interaction.
- **Literature safety signals:** acetazolamide-induced adynamic ileus and non-cardiogenic pulmonary edema after intravenous use were reported in case reports. Acetazolamide also carries a risk of hyperammonemia and encephalopathy in cirrhosis.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN scores are predictions from the TxGNN model (deep learning) only and may reflect similarities the model learned between related diseases, not biological evidence. No clinical trials exist, and no publication studies acetazolamide in hypertrophic cardiomyopathy itself, so the evidence level is L5. Some neighbouring predictions (cirrhotic cardiomyopathy, intestinal obstruction) are contradicted by known safety signals.

**To proceed, the following is needed:**
- Mechanism of action data and a clearly defined mechanistic hypothesis for hypertrophic cardiomyopathy
- Disease-specific preclinical or clinical studies in hypertrophic cardiomyopathy
- Package insert warnings and contraindications from the India regulatory records
- Approved indication text for the local licences
- A safety review covering interactions and the contraindicated conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

