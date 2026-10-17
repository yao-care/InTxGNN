---
layout: default
title: Labetalol
parent: Moderate Evidence (L3-L4)
nav_order: 466
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Labetalol: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertensive disorder, hypertension"
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Labetalol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1 and beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **no registered clinical trials** and only **1 publication** (a 1981 case report) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension (from the knowledge graph; no approved indication text is available from the India licences) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, labetalol combines alpha-1 and non-selective beta-adrenergic blockade, and its efficacy in hypertension and hypertensive emergencies is established. Mechanistically, it may be applicable to malignant renovascular hypertension.

However, caution is needed. In renovascular disease, blood pressure is driven largely by activation of the renin-angiotensin system, and beta-blockade only partly reduces renin release. This predicted indication is also very close to the drug's existing hypertension use, so it is better viewed as an extension of the current indication than as true repurposing.

The high TxGNN score (about 99%) most likely reflects closeness to the original hypertension indication in the knowledge graph, not independent clinical evidence.

The other predicted indications are weaker still:
- **Malignant hypertensive renal disease** (score 99.08%, L5): no trials or literature. Any benefit would come through general blood pressure control rather than a kidney-specific mechanism.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.08%, L4): the retrieved literature concerns pregnancy, perioperative hypertension and animal studies, not pulmonary hypertension. Non-selective beta-blockade may worsen bronchospasm in lung disease.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.08%, L5): no supporting studies. Beta-blockade may be harmful in some patients with right ventricular dysfunction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top predicted indication (malignant renovascular hypertension):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | The Medical Journal of Australia | A 20-year-old man with malignant hypertension after hallucinogenic drug use developed vasculitis of the renal vessels. The arteritis resolved with prednisone, and minoxidil and labetalol were used for initial blood pressure control. |

The literature retrieved for the pulmonary hypertension predictions is mostly about preeclampsia, perioperative hypertension, beta-blocker toxicity and animal studies. It does not directly address pulmonary hypertension and is therefore not listed here.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121877 | Lebatens Tablet | Strip of 10 tablets | Not stated |
| 129476 | Labimeg 20mg Injection | Vial of 4 ml injection | Not stated |
| 63253 | DavaIndia Labetalol 100mg Tablet | Strip of 10 tablets | Not stated |
| 175101 | Pregnasafe Tablet | Strip of 10 tablets | Not stated |
| 121186 | Lablol 100mg Tablet | Strip of 10 tablets | Not stated |

There are 20 valid single-ingredient registrations in total, covering oral tablets and injectable vials (4 ml and 20 ml).

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph links labetalol to contraindication with several conditions, including:
  - Liver conditions: liver failure, liver disease, hepatic coma, hepatic encephalopathy
  - Kidney and metabolic conditions: kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, gout
  - Cardiopulmonary conditions: atrioventricular block, hypotensive disorder, pulmonary emphysema, bronchial disease
  - Others: systemic lupus erythematosus, pancreatitis, gallbladder disease, intraoperative floppy iris syndrome
  
  These should be verified against the official package insert.
- **Drug Interactions**: 240 interactions were identified in total. Major interactions include **epinephrine** and **dolasetron**. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine, dicyclomine), morphine, cimetidine, canagliflozin, dapagliflozin and chlorpropamide.
- **Additional concern**: Non-selective beta-blockade may worsen bronchospasm in lung disease, which is relevant to the pulmonary hypertension predictions.

The package insert warnings could not be obtained for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for the top prediction is a single 1981 case report, with no registered clinical trials. The high TxGNN score likely reflects similarity to the existing hypertension indication rather than independent evidence. The pulmonary hypertension predictions lack mechanistic support and carry potential safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences, which are required for safety screening
- Detailed mechanism of action data
- Controlled clinical evidence in malignant renovascular hypertension, including comparison with renin-angiotensin system–targeted therapy
- Clarification of whether this indication is a genuine new use or already covered by the existing hypertension label
- Approved indication text for the India registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

