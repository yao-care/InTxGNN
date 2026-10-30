---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 828
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-30
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a bronchodilator used for airway diseases such as asthma, bronchitis and emphysema. The TxGNN model predicts it may be effective for **thrombotic disease**, but this is a computational prediction only: **0 clinical trials** are registered, and none of the 18 retrieved publications tests theophylline in thrombotic disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (relation recorded in the knowledge graph; the India licence records contain no indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, theophylline is a non-selective phosphodiesterase inhibitor and an adenosine receptor antagonist. Raised cAMP in platelets could in theory reduce platelet aggregation, which gives a plausible but unproven link to thrombosis.

The original use (airway disease) and the predicted use (thrombosis) are not closely related clinically. The prediction rests on a shared pharmacological pathway (cAMP signalling in platelets), not on demonstrated benefit. The retrieved literature does not test theophylline for thrombotic disease. The papers concern ticlopidine pharmacokinetics, platelet biomarker assays, blood-sample processing and a theophylline aptasensor. The high TxGNN score is therefore a computational prediction with no clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved publication studies theophylline for thrombotic disease. The items below are the closest in topic (platelet function, vascular disease) and are background only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet agent; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostaglandins, platelets and atherosclerosis; prostacyclin acts through adenylate cyclase to inhibit platelets |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone and adenosine inhibit human platelet response via cAMP; not theophylline |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort (ex vivo) | Inflammatory Bowel Diseases | Platelet-leukocyte aggregates in inflammatory bowel disease |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay | British Journal of Haematology | Platelet factor 4 radioimmunoassay; theophylline is only an additive in the anticoagulant |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical sensor | Analytica Chimica Acta | Electrochemical aptasensor for detecting theophylline; no clinical data |

## India Market Information

The approval records contain no indication text. At least 20 single-ingredient registrations are valid, and the list may be partial. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 221818 | Theobid 600mg Tablet | Strip of 10 tablets | Not stated in the records |
| 222065 | TR Phyllin 250mg Capsule | Strip of 10 capsules | Not stated in the records |
| 230300 | Unicontin-E 600 Tablet CR | Strip of 10 controlled-release tablets | Not stated in the records |
| 64646 | Duralyn 400mg Capsule CR | Strip of 10 controlled-release capsules | Not stated in the records |
| 171945 | Onimar 300mg Tablet CR | Strip of 10 controlled-release tablets | Not stated in the records |

## Safety Considerations

- **Contraindication-type relations in the knowledge graph (not label text):** hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis, among others.
- **Drug Interactions:** 371 interactions are recorded. Notable examples are:
  - **Major:** bupropion.
  - **Moderate:** cimetidine, clarithromycin, omeprazole, famotidine, ranitidine, rabeprazole, doxycycline, tetracycline, minocycline, systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide) and activated charcoal.
  - **Minor:** ephedrine.
- Theophylline has a narrow therapeutic window and is toxic above certain blood levels (PMID 29254574). Please refer to the package insert for label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies theophylline in thrombotic disease, so the evidence level is L5. The mechanistic link (platelet cAMP) is plausible but unproven, and the safety profile (narrow therapeutic window, cardiovascular and interaction concerns) argues against advancing on model prediction alone.

**To proceed, the following is needed:**
- Mechanism of action data and in vitro or in vivo evidence of antithrombotic effect of theophylline
- Label warnings and contraindications from the India package inserts
- Clinical or observational data in thrombotic patients, and a risk-benefit assessment given the drug's narrow therapeutic window

---

### Other Predicted Indications (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|------|------|------|------|
| Nasal cavity disease | 0.9953 | L5 | Research question | One small human study of slow-release theophylline in nasal allergen challenge in allergic rhinitis (PMID 9648963); no registered trials |
| Laryngotracheitis | 0.9951 | L5 | Hold | No trials or literature |
| Tracheal disease | 0.9949 | L5 | Hold | Evidence is preclinical, veterinary or indirect; no human study of tracheal disease itself |
| Pharyngitis | 0.9946 | L5 | Hold | No theophylline-specific evidence |
| Acute laryngopharyngitis | 0.9935 | L5 | Hold | No trials or literature |

Because the L3 ratings for nasal cavity disease and tracheal disease were not supported by a study that directly addresses the disease itself in a way that meets the ceiling rule for tracheal disease, tracheal disease is shown here as L5. Nasal cavity disease (allergic rhinitis challenge study) is the most evidence-supported lead and is the best candidate for follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

