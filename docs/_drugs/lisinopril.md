---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lisinopril: predicted new indication Posterolateral myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Lisinopril"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lisinopril: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but **no clinical trials or publications** specific to this subtype are currently available.
This prediction most likely reflects the closeness of the disease to the already-approved myocardial infarction indication, rather than a new therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; the licence records contain no indication text) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (below the L3 level reached by chronic pulmonary heart disease) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lisinopril belongs to the ACE inhibitor class. Its efficacy in hypertension and myocardial infarction is established, and ACE inhibition is known to reduce blood pressure and limit post-infarction cardiac remodeling.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an approved indication for lisinopril. The indication is therefore largely covered by the existing label. The high TxGNN score probably reflects ontology proximity to the approved indication, so this is not a true repurposing candidate in the strict sense.

Other high-scoring predictions follow the same pattern: posteroinferior and septal myocardial infarction, and malignant hypertensive renal disease and malignant renovascular hypertension, which are severe forms of hypertension. The mechanistic rationale for these is coherent, but they add little new information.

Several other predictions are less well supported:
- **Chronic pulmonary heart disease** has the most supporting literature (L3), consisting of two small lisinopril studies in cor pulmonale and pulmonary hypertension.
- **Pulmonary hypertension** (hypoxia-related and multifactorial) has only indirect evidence.
- **Braddock syndrome** and a rare familial hematuria–retinal arteriolar tortuosity syndrome are computational predictions only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For reference, the most relevant literature found for other predicted indications is shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (design unconfirmed) | Kardiologiia | Lisinopril 10 mg/day attenuated pulmonary hypertension and improved right ventricular systolic function in patients with heart failure, ischaemic heart disease and COPD (chronic pulmonary heart disease) |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (likely uncontrolled) | Probl Tuberk Bolezn Legk | Lisinopril in chronic cor pulmonale; no abstract available (chronic pulmonary heart disease) |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | ACE inhibitor plus coenzyme Q10 as adjunctive treatment in ventricular septal rupture after myocardial infarction (septal MI) |
| [10456287](https://pubmed.ncbi.nlm.nih.gov/10456287/) | 1999 | Ex vivo/animal | Fundam Clin Pharmacol | In isolated rat pulmonary arteries, endothelin rather than angiotensin II contributed to the hypoxic contractile response (pulmonary hypertension) |

## India Market Information

The licence records contain no approved indication text. Of the 20 valid single-ingredient registrations, five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 128096 | Lapril 10mg Tablet (Wockhardt Ltd) | Strip of 10 tablets | Not stated |
| 123445 | Listen 10mg Tablet (Litaka Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated |
| 126708 | Lisonol 5mg Tablet (Knoll Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated |
| 129806 | Lisnop 2.5mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |
| 121497 | Listril 10 Tablet (Torrent Pharmaceuticals Ltd) | Strip of 15 tablets | Not stated |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: kidney disease, liver disease, pancreatitis, gallbladder disease, angioedema (including hereditary and ACE-inhibitor-induced forms), systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, neutropenia and agranulocytosis, aortic stenosis, hypotensive disorders, hyperparathyroidism, hepatic encephalopathy, connective tissue disease and bone disease.
- **Drug interactions**: 308 interactions were recorded. Major-level interactions include potassium citrate and potassium bicarbonate (risk of hyperkalaemia). Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine and bupropion.
- **Case-report signals**: severe hypotension and bradycardia with concomitant tizanidine (PMID 20852161), and a report of small bowel angioedema attributed to lisinopril (PMID 42226836).
- **Prediction-specific cautions**: in malignant renovascular hypertension, bilateral renal artery stenosis or a solitary kidney can lead to acute kidney injury with ACE inhibitors. Hyperkalaemia and hypotension are also relevant.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posterolateral myocardial infarction is a subtype of an indication lisinopril already holds, so the prediction adds little new therapeutic information. No subtype-specific trials or literature support it (evidence level L4).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Detailed mechanism of action data (from DrugBank)
- Confirmation that the existing myocardial infarction indication already covers this subtype, which would make a separate repurposing effort unnecessary
- If a genuine repurposing signal is wanted, consider chronic pulmonary heart disease (L3). This would require retrieving the full text of the two lisinopril studies and a controlled trial to confirm efficacy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

