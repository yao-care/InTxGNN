---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Irbesartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, diabetic nephropathy"
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **no clinical trials** and **no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, diabetic nephropathy (the license records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, irbesartan is an AT1 receptor blocker. Its efficacy in hypertension and diabetic nephropathy has been established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, which is the pathway irbesartan blocks. This makes the prediction biologically plausible.

There is an important caveat. ARBs are generally contraindicated or used with great caution in bilateral renal artery stenosis because of the risk of acute kidney injury. The knowledge graph also lists renal artery obstruction among the contraindicated conditions. The high TxGNN score is a computational prediction only and does not address this safety concern.

Other predicted indications were also reviewed:
- **Malignant hypertensive renal disease** (score 99.31%): This is largely an extension of the existing hypertension and diabetic nephropathy label. It has no direct trials or literature, and the evidence level is L5.
- **Pulmonary hypertension, unclear multifactorial mechanism** (score 99.25%): Angiotensin II contributes to pulmonary vascular remodeling, so the approach is plausible but unproven. It has no trials or literature (L5), and systemic hypotension is a concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.25%): This is the only prediction with literature support, all of it preclinical (L4). It is described in the notes below.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other predicted indications.

## Literature Evidence

No literature is available for the top-ranked prediction. The only literature retrieved concerns the fourth-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia. Most of it is preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Pleiotropic effects of AT-1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical (in vitro) | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical (animal) | Sleep Breath | Irbesartan attenuated sleep apnea-induced cardiac apoptosis and upregulated Sirtuin 1 |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical (rat) | Biomed Pharmacother | Irbesartan ameliorated pulmonary artery lesions in chronic mountain sickness, possibly via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preclinical (rat) | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in high-altitude pulmonary hypertension, with involvement of intestinal flora |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical (animal) | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |

These studies address cardiac or systemic hypoxic injury and high-altitude models rather than renovascular hypertension. Other retrieved papers (herbal extracts, a roxadustat case report, cyclosporine nephrotoxicity) are only tangentially relevant and are not listed.

## India Market Information

Irbesartan is marketed in India, with 20 valid single-ingredient registrations. Five main authorizations are listed below. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 3146 | Aprovel 150mg Tablet | Strip of 14 tablets | Sanofi India Ltd |
| 38738 | Coaprovel 150mg/12.5mg Tablet | Strip of 14 tablets | Sanofi India Ltd |
| 244464 | Xarb 300 Tablet | Strip of 10 tablets | Abbott |
| 108229 | Irovel 300 Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 108149 | Irovel H Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |

## Safety Considerations

- **Conditions flagged as contraindicated in the knowledge graph** (not taken from label text): angioedema (including ARB-induced and hereditary forms), renal artery obstruction, anuria, hypotensive disorder, pancreatitis, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, hyperkalaemia-related and electrolyte disorders (potassium deficiency disease, hypercalcaemia, phosphorus metabolism disease), gout and hyperuricaemia, hyperparathyroidism, hepatic coma and encephalopathy, myopathy and rhabdomyolysis, and neonatal jaundice.
- **Drug Interactions**: 216 interactions were recorded. The **Major** interactions in the retrieved list are **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, acetylsalicylic acid, morphine, bupropion, aprepitant, dronabinol, and several bowel-preparation agents.

The package insert warnings and contraindications could not be obtained, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (99.31%) with no clinical trials or literature (L5). ARBs also carry a known risk of acute kidney injury in renal artery stenosis, which is the central lesion in renovascular hypertension.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, since this blocks safety screening
- Mechanism of action data for irbesartan from DrugBank
- A literature and trial search focused on ARBs in renovascular hypertension, including renal safety in unilateral versus bilateral renal artery stenosis
- A clinical review of whether the pulmonary hypertension (hypoxia) direction, which has preclinical support only, merits further preclinical or early clinical work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

