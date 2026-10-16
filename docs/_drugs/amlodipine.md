---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amlodipine: predicted new indication Brain stem infarction (evidence level L5). Approved use: Hypertension, stroke and cerebrovascular disorders…"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant renovascular hypertension", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a calcium channel blocker, originally used to treat hypertension and to prevent stroke and other cerebrovascular disorders.
The TxGNN model predicts it may be effective for **brain stem infarction**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, stroke and cerebrovascular disorders, cerebral infarction, Prinzmetal angina (from knowledge-graph indication data; the Indian license records list no indication text) |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amlodipine is a dihydropyridine calcium channel blocker. It relaxes vascular smooth muscle and lowers blood pressure, and its efficacy in hypertension and stroke prevention is established.

Brain stem infarction is a type of ischaemic stroke. Amlodipine is already indicated for stroke and cerebrovascular disorders through blood pressure control. Any link to brain stem infarction is therefore most likely a secondary-prevention extension of the existing indication, not a genuinely new use.

A high model score means the disease is close to amlodipine's known indications in the knowledge graph. It is not evidence of benefit in brain stem infarction specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

---

## Literature Evidence

Currently no related literature available for brain stem infarction.

---

## India Market Information

There are 20 valid registrations, all for single-ingredient records, including fixed-dose products that pair amlodipine with other agents such as metoprolol, valsartan and atorvastatin. The data compiled for this report contain no approved-indication text for any of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 1017 | Amlopin 2.5 Tablet | Strip of 10 tablets | USV Ltd |
| 262 | Amlong 2.5 Tablet | Strip of 15 tablets | Micro Labs Ltd |
| 73116 | Exforge 10 mg/160 mg Tablet | Strip of 14 tablets | Novartis India Ltd |
| 39186 | Caduet 5 mg/10 mg Tablet | Strip of 10 tablets | Pfizer Ltd |
| 122755 | Lipril AM Tablet | Strip of 10 tablets | Lupin Ltd |

All available forms are oral (tablets, extended-release or prolonged-release tablets, and capsules).

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are not label text and need confirmation against the package insert): liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, hypothyroidism and myxedema, angioedema (including hereditary and RAAS-blocker-induced forms), systemic lupus erythematosus, myopathy and muscle disease, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, hypotensive disorder, hyperparathyroidism.
- **Drug interactions**: 292 known interactions. The main ones retrieved are all rated Moderate:
  - corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone)
  - aprepitant
  - acetylsalicylic acid
  - bupropion
  - clarithromycin
  - clotrimazole
  - calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate and others)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin)
- **Hypotension risk**: In stroke patients, blood pressure lowering that is too aggressive can be harmful. This needs particular attention.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The brain stem infarction prediction has a very high model score but no trials or publications behind it. It is also largely an extension of amlodipine's existing stroke and cerebrovascular indications. There is no basis yet to advance it as a separate repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory records, since no safety label data are currently available
- Mechanism of action data for amlodipine
- Any clinical or observational data specific to brain stem infarction, such as subgroup analyses of secondary-prevention stroke trials
- A defined patient population and blood pressure targets for acute and post-acute stroke

**Related candidate worth evaluating separately:** For intracerebral haemorrhage, the completed Phase 3 TRIDENT trial (NCT02699645, n=1,671) tested a single pill of three low-dose antihypertensives that includes amlodipine, and its results were published in 2026 (PMID 42019018). The effect cannot be attributed to amlodipine alone, and this is still a blood pressure control strategy rather than a new mechanism. It would be a stronger candidate for a "Proceed with Guardrails" assessment than brain stem infarction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

