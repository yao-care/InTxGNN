---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 5
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Atenolol
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker whose original uses recorded in the knowledge graph are hypertension and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** directly studying this disease were found, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; the licence records contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, atenolol is a beta-1 selective blocker. It lowers blood pressure by reducing cardiac output and renin release.

Hypertension is a relation recorded in the knowledge graph for atenolol, and malignant hypertensive renal disease is kidney injury caused by severely elevated blood pressure. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Mechanistically, lowering blood pressure and renin release is biologically plausible for this condition.

However, malignant hypertension is usually managed with parenteral antihypertensives and renin-angiotensin system blockade. Nothing in the data compiled for this report supports a role for atenolol in this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For context, the other predicted indications drew only indirect literature. The pulmonary hypertension and chronic pulmonary heart disease searches returned mostly animal, mechanistic or general beta-blocker papers. These do not study atenolol in those diseases directly, and some findings conflict. For example, one rat study (PMID 8590992) reported reduced hypoxia-induced right heart hypertrophy with beta-blockade, while a rabbit study (PMID 6212672) found no such effect. Evidence for these diseases is therefore not strong enough to change the decision here.

---

## India Market Information

At least 20 single-ingredient atenolol registrations are valid, and the list may be partial. The records contain no approved-indication text. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54419 | Cadpres 100mg Tablet | Strip of 14 tablets | Not stated in the records |
| 105077 | Hyten 50mg Tablet | Strip of 10 tablets | Not stated in the records |
| 28378 | BP-Nol 100mg Tablet | Strip of 10 tablets | Not stated in the records |
| 3862 | AT Tablet | Strip of 10 tablets | Not stated in the records |
| 218444 | Tenil 50 Tablet | Strip of 10 tablets | Not stated in the records |

---

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph (not label text):** liver failure, asthma (including intrinsic and allergic asthma), atrioventricular block, Raynaud disease, anaphylaxis, diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, systemic lupus erythematosus, psoriasis, gout, pancreatitis, anuria, and several metabolic or mood disorders (anxiety, dysthymic and neurotic disorders, potassium deficiency, hypercalcaemia, nephrocalcinosis).
- **Drug Interactions:** 293 interactions are recorded. Examples at Moderate level include epinephrine, hydrocortisone, morphine, bupropion, atropine, calcium salts and several corticosteroids. Acetylsalicylic acid, aluminium hydroxide and attapulgite are Minor.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications that directly study atenolol in malignant hypertensive renal disease, so the evidence level is L5. Standard care for this condition relies on other drug classes. The knowledge graph also records several contraindications relevant to patients with kidney or metabolic disease.

**To proceed, the following is needed:**
- Clinical or observational data on atenolol in malignant hypertension with renal involvement
- Mechanism of action data and package insert warnings and contraindications (not yet available)
- Comparison against current standard therapy for this condition
- A safety plan covering the contraindication signals and interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

