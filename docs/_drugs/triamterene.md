---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 862
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Triamterene"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
description: "Triamterene: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Triamterene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Triamterene: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Triamterene is generally known as an epithelial sodium channel (ENaC) blocker that acts as a potassium-sparing diuretic. Its use in hypertension and heart failure is established, and it may therefore be conceptually applicable to hypertensive kidney disease through volume and blood pressure control.

However, this link is only conceptual. The very high TxGNN score most likely reflects similarity to the already approved hypertension indication rather than independent evidence. In malignant hypertension with kidney involvement, kidney function is often impaired, and a potassium-sparing agent carries a real risk of hyperkalaemia. This weakens the case for the prediction.

Other predicted indications were also reviewed and are weaker or equally unsupported:
- **Malignant renovascular hypertension** (0.9989): this form is largely driven by the renin-angiotensin system, which a potassium-sparing diuretic does not address.
- **Pulmonary hypertension** (two entries, 0.9988): there is no clear mechanistic rationale, and diuretics would at most relieve volume overload symptomatically.
- **Braddock syndrome** (0.9984): no mechanistic rationale can be established.
- **Chronic pulmonary heart disease** (0.9975): the only indication with indirect, symptom-level support, from two small studies of diuretic therapy in chronic heart failure (Evidence Level L4).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature is available for the lead predicted indication, malignant hypertensive renal disease. The publications retrieved for related predicted indications are listed below for reference; they do not support the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Randomised crossover study (classified as Review) | Dtsch Med Wochenschr | 16 patients with heart failure received a hydrochlorothiazide + triamterene combination or a digitalis glycoside in a crossover design; relevant to chronic pulmonary heart disease only indirectly |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Clinical hemodynamic study | Fortschr Med | 12 patients with chronic heart failure given a verapamil/triamterene/hydrochlorothiazide fixed combination for 4 weeks; blood pressure and heart rate decreased (combination, not triamterene alone) |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Pulmonary oedema after a triamterene-hydrochlorothiazide tablet, attributed to the hydrochlorothiazide component; an adverse event, not evidence of efficacy |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Preclinical (animal physiology) | J Physiol | Rat colon transmucosal potential study; not relevant to efficacy in this indication |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 222000 | Trymax 2mg Tablet | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph records contraindication links to many conditions. The most relevant to the predicted indication are:
  - Kidney disease, anuria, nephrolithiasis, nephrocalcinosis and acute urate nephropathy
  - Liver disease, liver failure, hepatic coma and hepatic encephalopathy
  - Diabetes mellitus (types 1 and 2) and diabetic ketoacidosis
  - Gout, hyperuricaemia and hypercalcaemia
  - Acidosis and lactic acidosis
  - Systemic lupus erythematosus, folic acid deficiency anaemia, pancreatitis and gallbladder disease

  The kidney-related entries are directly relevant to malignant hypertensive renal disease.
- **Drug Interactions**: 104 interactions are recorded. The notable ones are:
  - **Major**: potassium citrate (hyperkalaemia risk)
  - **Moderate**: metformin, canagliflozin, dapagliflozin, bupropion, morphine, dronabinol, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide) and some laxatives and bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes)
  - **Minor**: famotidine, ranitidine, cimetidine, doxycycline, minocycline
- Combining triamterene with ACE inhibitors or ARBs also raises hyperkalaemia risk, which matters in renal and renovascular hypertension.

Please also refer to the package insert for label-based warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials or supporting publications for the lead indication. The hyperkalaemia risk and the kidney-related contraindications in the knowledge graph argue against use in malignant hypertensive renal disease.

**To proceed, the following is needed:**
- The Indian package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- A systematic literature search specific to triamterene in hypertensive nephropathy and malignant hypertension
- A renal and potassium safety assessment for patients with impaired kidney function
- If any indication is pursued first, chronic pulmonary heart disease is the only one with indirect supporting data and could be treated as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

