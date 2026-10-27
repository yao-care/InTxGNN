---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 812
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Hypertension, stroke, cerebrovascular disorder, cerebral infarction"
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Telmisartan: From Hypertension to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker, originally used to treat hypertension and to reduce stroke and cerebral infarction risk.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (vasospastic angina) with a very high score, but **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, stroke, cerebrovascular disorder, cerebral infarction (from the knowledge graph; the licence records list no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, telmisartan blocks the angiotensin II type 1 (AT1) receptor. It is also a partial agonist of PPAR-gamma. Its efficacy in hypertension and cerebrovascular disease is established, and mechanistically it may be applicable to vasospastic angina.

Prinzmetal angina is caused by spasm and hypercontractility of coronary smooth muscle. AT1 blockade and PPAR-gamma activity could plausibly modulate vascular tone and endothelial function. This connects the drug's established vascular effects to the predicted disease.

This link is a hypothesis only. No trial or publication supporting telmisartan in Prinzmetal angina was retrieved. The high graph score should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty valid registrations were found, all with valid status. The five below are examples. The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| 226234 | Temcar 40mg Tablet | Strip of 10 tablets |
| 227759 | Teloris 40mg Tablet | Strip of 10 tablets |
| 129212 | Lintel-CT 80 Tablet | Strip of 10 tablets |
| 201139 | Stamlo-T 80 Tablet | Strip of 10 tablets |
| 216483 | Tetan Beta 50 Tablet ER | Strip of 15 extended-release tablets |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph derived, not label text)**: liver failure, liver disease, hepatic coma and encephalopathy, cholestasis (including benign recurrent and familial intrahepatic forms), kidney disease, anuria, renal artery obstruction, pancreatitis, gallbladder disease, systemic lupus erythematosus (including pediatric), diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, potassium deficiency, hypercalcemia, nephrocalcinosis, hyperparathyroidism, osteitis fibrosa, phosphorus metabolism disease, gout, hyperuricemia, pyoureter, neonatal jaundice. Many of these likely reflect hydrochlorothiazide combination products, so they need confirmation against the actual package inserts.
- **Drug Interactions**: 185 interactions were recorded.
  - **Major**: potassium citrate and potassium bicarbonate, which carry a hyperkalemia risk.
  - **Moderate examples**:
    - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
    - Acetylsalicylic acid
    - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
    - Insulin products and exenatide
    - Bupropion
    - Morphine
    - Dronabinol
    - Bowel-preparation laxatives

Package insert warnings were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction has a very high model score but no supporting trials or literature (L5). Telmisartan is already widely marketed in India, so access is not a barrier. The barrier is the absence of any indication-specific evidence.

**To proceed, the following is needed:**
- Targeted literature and trial searches for ARBs and telmisartan in vasospastic angina
- Mechanism of action data (MOA) to support the AT1 and PPAR-gamma hypothesis
- Package insert warnings and contraindications for the marketed products
- A comparison with established first-line therapy for vasospastic angina (calcium channel blockers)

**Note on other predictions:** Among the other predicted indications, **intracerebral hemorrhage** has the strongest support (L1). It is backed by the completed Phase 3 TRIDENT trial (NCT02699645, n=1671) and a 2026 NEJM publication. That trial tested a three-drug low-dose pill, so telmisartan's own contribution cannot be separated. **Cerebral artery occlusion** has Phase 4 trial and preclinical support (L2). A separate evaluation of these indications is worth considering.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

