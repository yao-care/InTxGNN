---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Atenolol: predicted new indication Posterolateral myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Atenolol: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this is an anatomical subtype of an indication it already covers, so it is not a true repurposing candidate. There are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (the registration records compiled for India contain no approved indication text) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atenolol is a cardioselective beta-blocker. Its efficacy in hypertension and myocardial infarction is established, and mechanistically it may be applicable to myocardial infarction at other locations. Beta-1 blockade lowers heart rate and myocardial oxygen demand, which can limit ischaemic injury.

Posterolateral myocardial infarction describes where the infarct sits in the heart, not a different disease. The high TxGNN score mainly reflects how close this term is to the already approved myocardial infarction indication in the knowledge graph. It is not new evidence of benefit. No trials or literature were retrieved for this subtype.

Other predictions in the same list show the same pattern. Posteroinferior and septal myocardial infarction are also subtypes of an approved use. Malignant hypertensive renal disease and malignant renovascular hypertension are severe forms of hypertension. Pulmonary hypertension, chronic pulmonary heart disease and Braddock syndrome have weak or unfavourable rationales and are not supported by direct clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For the closely related subtype **posteroinferior myocardial infarction**, one article was retrieved. It is indirect support only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | RCT (single-blind, crossover) | La Revue de medecine interne | Atenolol 200 mg vs diltiazem 240 mg compared for anti-ischaemic activity in 23 patients undergoing retraining 4 weeks after a postero-inferior or anterior myocardial infarction; the title does not specify an MI subtype |

---

## India Market Information

The compiled registration records show 20 valid single-ingredient registrations and no cancelled ones. Approved indication text is not available in these records. Five main registrations are listed:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54419 | Cadpres 100mg Tablet | Strip of 14 tablets | Not available |
| 105077 | Hyten 50mg Tablet | Strip of 10 tablets | Not available |
| 28378 | BP-Nol 100mg Tablet | Strip of 10 tablets | Not available |
| 3862 | AT Tablet | Strip of 10 tablets | Not available |
| 218444 | Tenil 50 Tablet | Strip of 10 tablets | Not available |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationships in the model's knowledge graph, not from package insert text): liver failure, anxiety and neurotic disorders, pancreatitis, systemic lupus erythematosus, asthma (including intrinsic and allergic), potassium deficiency, psoriasis, gout and hyperuricaemia, anuria, hypercalcaemia, nephrocalcinosis, type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, atrioventricular block, Raynaud disease, and anaphylaxis.
- **Drug Interactions**: 293 interactions were recorded. Those retrieved include moderate-level interactions with epinephrine, hydrocortisone and other corticosteroids (triamcinolone, betamethasone, budesonide), hyoscyamine, atropine, bupropion, morphine, acetohexamide, and calcium salts (acetate, carbonate, citrate, gluconate and others). Minor-level interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.
- **Other considerations from the compiled analysis**: atenolol is cleared by the kidneys and needs dose adjustment in renal impairment. Beta-blockers carry a theoretical risk of reducing right ventricular reserve in pulmonary hypertension, and they are not a first-line choice for hypertensive emergencies.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posterolateral myocardial infarction is a subtype of an indication atenolol already holds, so the high score reflects graph proximity rather than new therapeutic evidence. No trials or literature support this specific prediction (evidence level L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's records (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A decision on whether this subtype adds anything beyond the existing myocardial infarction indication. If not, focus on predictions with real repurposing potential instead.
- Approved indication text for the India registrations, to confirm the current labelled uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

