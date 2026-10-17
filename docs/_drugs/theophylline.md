---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 828
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma (also intrinsic and allergic asthma, bronchitis, emphysema…"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Asthma and Chronic Airway Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator, originally used for asthma, bronchitis, emphysema and related airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but there are **0 clinical trials** and **19 retrieved publications**, none of which evaluates theophylline as an antithrombotic.
This prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (also intrinsic and allergic asthma, bronchitis, emphysema, other lung and bronchial disease) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Theophylline is a nonselective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from general pharmacology.

Inhibiting PDE can raise cyclic AMP in platelets, which can weakly reduce platelet aggregation. That is a plausible but unproven link to thrombosis. The old airway indication (bronchodilation) and the predicted thrombotic indication share only this general cAMP pathway.

The high TxGNN score is not backed by clinical data. The retrieved literature mostly covers platelet biomarkers, ticlopidine pharmacokinetics, assay methods and a theophylline biosensor.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved papers tests theophylline as a treatment for thrombosis. The most relevant items are listed below, mostly background on platelet cAMP biology or older work on theophylline derivatives in vascular disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone (another PDE inhibitor) reduced platelet aggregation and raised platelet cAMP, and it interacted with adenosine's effect. Theophylline was not studied. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Describes prostacyclin acting through adenylate cyclase and cAMP to inhibit platelet aggregation. This is background for the cAMP mechanism. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Not classified | Minerva Cardioangiologica | Theophylline nicotinate derivative studied in chronic obliterating peripheral arteriopathy. No abstract available. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Not classified | Cardiologia Practica | Cardiocirculatory effects of a theophylline nicotinate ester in cerebral and peripheral angiopathies. No abstract available. |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | Not classified | Annali di Ottalmologia e Clinica Oculistica | Theophylline nicotinate in some retinal vascular diseases. No abstract available. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Pharmacokinetic review | Clinical Pharmacokinetics | Concerns ticlopidine, not theophylline. It is relevant only as background on antiplatelet drugs. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay method | British Journal of Haematology | Theophylline appears only as an additive in the anticoagulant solution used for a platelet factor 4 assay. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | Electrochemical aptasensor for detecting theophylline. It is not about antithrombotic efficacy. |

---

## India Market Information

Twenty single-ingredient theophylline registrations are valid and none are cancelled. The registration records do not state an approved indication. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 221818 | Theobid 600mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 222065 | TR Phyllin 250mg Capsule | Strip of 10 capsules | Not specified |
| Registration No. 64646 | Duralyn 400mg Capsule CR | Strip of 10 controlled-release capsules | Not specified |
| Registration No. 230300 | Unicontin-E 600 Tablet CR | Strip of 10 controlled-release tablets | Not specified |
| Registration No. 150742 | New Theo-Asthalin Syrup | Bottle of 100 ml syrup | Not specified |

---

## Safety Considerations

- **Disease associations flagged as contraindications (knowledge graph, not label text):**
  - Cardiovascular and neurological: hypertension, epilepsy.
  - Mental health: anxiety, psychotic disorders, schizophreniform and schizoaffective disorders, neurotic and dysthymic disorders.
  - Liver, kidney and gallbladder: liver failure, liver disease, kidney disease, gallbladder disease.
  - Metabolic and endocrine: porphyria, hypothyroidism, diabetes mellitus, diabetic ketoacidosis.
  - Blood: thrombocytopenia, neutropenia, agranulocytosis.
  - Other: peptic ulcer disease, open-angle glaucoma, benign prostatic hyperplasia, dermatitis herpetiformis.
- **Drug interactions:** 371 interactions are recorded.
  - Major: bupropion.
  - Moderate: H2 blockers and PPIs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), tetracyclines (doxycycline, tetracycline, minocycline), clarithromycin, activated charcoal and some bowel-preparation agents.
  - Minor: ephedrine.
- **General:** Theophylline has a narrow therapeutic window, so any new use would need serum level monitoring. Please also refer to the package insert, as label warnings were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.62% TxGNN score is not supported by any clinical trial or relevant publication. The only link is a plausible but unproven platelet cAMP effect. Theophylline also has a narrow therapeutic window and many drug interactions.

Among the other predictions, only obstructive lung disease has strong support (L1, Proceed with Guardrails). That is essentially theophylline's existing labeled airway use, not true repurposing.

**To proceed, the following is needed:**
- Preclinical or ex vivo data showing that theophylline at clinically achievable concentrations meaningfully inhibits platelet aggregation or thrombus formation
- Any clinical signal (observational or interventional) for theophylline in thrombotic outcomes
- Package insert warnings and contraindications from the Indian regulator's records, so a safety screen can be done
- Detailed mechanism-of-action data from DrugBank
- A dosing and monitoring plan that addresses the narrow therapeutic index, CYP1A2 variability and the interaction burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

