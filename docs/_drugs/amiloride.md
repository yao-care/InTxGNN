---
layout: default
title: Amiloride
parent: Moderate Evidence (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Amiloride: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
---

# Amiloride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Amiloride: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **no registered clinical trials** and only **1 publication** (a general review on mineralocorticoid hypertension that does not test amiloride), so the prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (from the knowledge graph; the Indian licence records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiloride blocks the epithelial sodium channel (ENaC) in the kidney, reducing sodium reabsorption while sparing potassium. It is already marketed for hypertension. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on known pharmacology.

Malignant renovascular hypertension is driven by activation of the renin-angiotensin-aldosterone system, which causes sodium retention and mineralocorticoid-type effects. Amiloride could plausibly counter these downstream effects. The link is indirect, however. The only supporting paper is a 2003 article on investigating mineralocorticoid hypertension, which does not test amiloride in malignant renovascular disease.

The very high TxGNN score most likely reflects the drug's existing hypertension indication and its closeness to related hypertensive disease nodes in the knowledge graph, rather than independent evidence for this condition.

Other predictions in the same set:

- **Malignant hypertensive renal disease** (99.82%): no trials or literature (L5). Amiloride's hyperkalaemia risk in renal impairment is a further concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.81%): L4. There is a coherent preclinical rationale (hypoxia downregulates alveolar ENaC; ASIC1a on pulmonary arterial smooth muscle contributes to hypoxic pulmonary hypertension and is inhibited by amiloride). However, the literature is mostly in vitro or animal work, several papers are off-topic, and there are no human efficacy data. It is best treated as a research question.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.81%) and **Braddock syndrome** (99.75%): no evidence (L5), computational prediction only.
- **Chronic pulmonary heart disease** (99.68%): L4. Supporting studies concern general congestive heart failure, not cor pulmonale specifically, so the evidence is indirect. It is best treated as a research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | Journal of Hypertension. Supplement | Overview of investigating mineralocorticoid (corticosteroid-induced) hypertension, which affects about 3% of hypertensive patients; primary aldosteronism is the most frequent cause. Amiloride is not tested in renovascular disease. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 11714 | Amiur H Forte 5mg/50mg Tablet | Strip of 10 tablets | Not stated |
| Registration No. 26232 | Biduret -L Tablet | Strip of 10 tablets | Not stated |
| Registration No. 3897 | Amiur 5mg Tablet | Strip of 10 tablets | Not stated |
| Registration No. 4158 | Amiur H 2.5mg/25mg Tablet | Strip of 10 tablets | Not stated |

---

## Safety Considerations

- **Disease contraindication signals (from the knowledge graph, not label text)**: kidney disease, anuria, diabetic nephropathy, liver disease, hepatic coma/encephalopathy, pancreatitis, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, gout, hyperuricaemia, hyperparathyroidism, osteitis fibrosa, acidosis (including acquired lactic acidosis), systemic lupus erythematosus (including paediatric), pyoureter and neonatal jaundice.
- **Drug Interactions**: 136 interactions were identified. Examples include:
  - Moderate: hydrocortisone, betamethasone, dexamethasone, budesonide, metformin, bupropion, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, dronabinol, and laxatives such as bisacodyl, castor oil, glycerin, lactitol and lactulose.
  - Minor: doxycycline, amoxicillin, cimetidine.
- **Hyperkalaemia**: this is a key safety signal, especially in renal impairment and with interacting drugs. A published case report describes severe hyperkalaemia (potassium 9.3 meq/L) in a geriatric patient with heart failure receiving trimethoprim-sulfamethoxazole.

The package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant renovascular hypertension has no clinical trials and only one indirect review, and the high TxGNN score appears to reflect similarity to the approved hypertension indication rather than independent evidence. The renal-impairment and hyperkalaemia risks add further caution for this population.

**To proceed, the following is needed:**
- Direct clinical or well-designed preclinical evidence of amiloride in renovascular or malignant hypertension
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the Indian licence holders, to allow a safety screen
- A potassium and renal function monitoring plan, plus an assessment of the interaction burden
- If a research direction is pursued, the stronger leads are hypoxic pulmonary hypertension (preclinical ASIC1a/ENaC rationale) and chronic pulmonary heart disease (heart failure data), each as a research question rather than a recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

