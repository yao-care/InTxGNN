---
layout: default
title: Losartan
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Losartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, hypertensive disorder, diabetic nephropathy"
monitor_inn: "Losartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
---

# Losartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Losartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Losartan is an angiotensin II receptor blocker originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but the data compiled for this report contain **no clinical trials** and only **1 supporting publication** (an animal model study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (from the knowledge graph; no approved indication text is available in the India license records) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, losartan blocks the angiotensin II type 1 (AT1) receptor. Its efficacy in hypertension and diabetic kidney disease is established, and mechanistically it may be applicable to hypertensive kidney injury.

Malignant hypertensive renal disease is a severe form of kidney damage driven by very high blood pressure. It overlaps closely with losartan's existing uses in blood pressure control and renal protection. The only supporting paper is a rat model study showing that angiotensin II and NF-κB signaling contribute to malignant hypertensive nephrosclerosis. This makes AT1 blockade biologically plausible, but it is preclinical evidence only.

Other predictions in the list have similarly limited support:
- **Malignant renovascular hypertension** (score 99.73%, L4): one case report of enalapril plus losartan in Takayasu's arteritis and one rat methods paper. ARBs can reduce renal perfusion in bilateral renal artery stenosis, so caution is needed.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.71%, L4): a small human study showed losartan abolished intermittent-hypoxia-induced oxidative stress, and rat studies link AT1 blockade to hypoxia-induced right ventricular hypertrophy. A high-altitude trial found no benefit. No study tests pulmonary hypertension outcomes in patients.
- **Brain small vessel disease 1 with or without ocular anomalies** (score 99.37%, L4): evidence is indirect, drawn from Marfan syndrome ARB reviews, Alport syndrome, and sporadic small vessel disease studies.
- Pulmonary hypertension with unclear multifactorial mechanism, Braddock syndrome, Prinzmetal angina, and a rare COL4A1-related hematuria syndrome are prediction-only, with no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical animal model | Hypertension Research | Angiotensin II and the NF-κB system play a pathogenic role in a rat model of malignant hypertensive nephrosclerosis |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 126491 | Lopassium 50mg Tablet | Strip of 10 tablets | Not stated |
| 133326 | Losawun 25mg Tablet | Strip of 10 tablets | Not stated |
| 94577 | Giftan-HC Tablet | Strip of 10 tablets | Not stated |
| 128730 | Losaline H 50mg/12.5mg Tablet | Strip of 10 tablets | Not stated |
| 1374 | Amlozaar Tablet | Strip of 15 tablets | Not stated |

All 20 registrations are currently valid. Only the first 5 are listed here.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (disease-level links, not label text): pancreatitis, liver disease, gallbladder disease, systemic lupus erythematosus, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, hyperparathyroidism, hepatic coma/encephalopathy, neonatal jaundice, anuria, gout, hypercalcemia, nephrocalcinosis, renal artery obstruction, and impaired renal function. These should be verified against the official label, since several appear to reflect combination products such as losartan with hydrochlorothiazide.
- **Drug Interactions**: 253 interactions were recorded. Major interactions include **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, acetylsalicylic acid, morphine, bupropion, aprepitant and dronabinol.
- **Renal perfusion caution**: ARBs can reduce renal perfusion in bilateral renal artery stenosis, which is relevant to the renovascular hypertension prediction.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, and AT1 blockade is mechanistically plausible for hypertensive kidney injury. However, the only evidence is one animal study, with no clinical trials, so the evidence level is L5. Among the other predictions, pulmonary hypertension due to lung disease/hypoxia and brain small vessel disease are the most promising as research questions (L4), but both rely on indirect evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Human clinical data (observational studies or trials) in malignant hypertensive nephrosclerosis
- Review of the knowledge-graph contraindications against the official label
- A safety plan covering potassium monitoring, renal function, and renal artery stenosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

