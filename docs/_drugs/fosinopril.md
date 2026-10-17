---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 381
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosinopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Fosinopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Fosinopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but currently there are **no registered clinical trials** and **no relevant publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fosinopril belongs to the ACE inhibitor class, its efficacy in hypertension is established, and it may mechanistically be applicable to malignant hypertensive renal disease.

Malignant hypertensive kidney disease involves severe blood pressure elevation and activation of the renin-angiotensin-aldosterone system (RAAS). Blocking angiotensin-converting enzyme is therefore biologically plausible. However, this prediction is essentially an extension of the approved hypertension indication rather than a true repurposing.

Other high-scoring predictions in the same list are:
- **Malignant renovascular hypertension** (99.87%): plausible because renal hypoperfusion drives RAAS activation, but caution is needed in bilateral renal artery stenosis because of the risk of acute kidney injury.
- **Pulmonary hypertension (unclear multifactorial mechanism, and due to lung disease/hypoxia)** (99.87%): the link is indirect, and ACE inhibitors have no established benefit here. Systemic vasodilation may also cause hypotension.
- **Braddock syndrome** (99.81%): no mechanistic rationale could be established; the score is likely a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature supports the top-ranked prediction. For the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), two publications were retrieved, and neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report | Rev Mal Respir | Two patients on enalapril or fosinopril for hypertension developed hypoxic eosinophilic pneumonia; a safety signal, not a benefit |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinical (bioinformatics) | Exp Ther Med | Gene expression analysis in mouse mesangial cells related to diabetic nephropathy; unrelated to pulmonary hypertension |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 89526 | Fosinace 20mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 89754 | Fosinace 10mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 88071 | Fovas 20mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 88802 | Fovas 10mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, pancreatitis, gallbladder disease, angioedema (including hereditary and ACE-inhibitor-related forms), systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, neutropenia/agranulocytosis, aortic stenosis and aortic valve disease, hypotensive disorder, hyperparathyroidism, hepatic coma/encephalopathy, connective tissue disease, and bone disease.
- **Drug Interactions**: 183 interactions were recorded. Major-level interactions include **potassium bicarbonate** and **potassium citrate** (risk of hyperkalaemia). Moderate-level interactions include corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone, dexamethasone), antidiabetic drugs (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion, and dronabinol.
- **Special caution**: in bilateral renal artery stenosis (relevant to the renovascular prediction), ACE inhibition carries a risk of acute kidney injury. A published case report also links ACE inhibitors to hypoxic eosinophilic pneumonia.

Package insert warnings and contraindications were not available; please refer to the package insert for the official safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction scores highly in the model (99.87%), but there are no clinical trials or supporting literature, so the evidence level is L5. It is also largely an extension of the approved hypertension indication rather than a new therapeutic direction.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma website (a blocking gap for safety screening)
- Mechanism of action data (e.g. from DrugBank)
- A targeted search for clinical studies of ACE inhibitors in malignant hypertension and hypertensive nephropathy
- Approved indication text for the four marketed products
- A review of the safety profile in renal impairment and renal artery stenosis, given the long list of kidney-related and other contraindicated conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

