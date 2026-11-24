---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: at least 20 listed products"
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker originally used to treat hypertension and diabetic nephropathy.
but **no clinical trials** and **no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for irbesartan: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), label version 2026-08-24; accessed 2026-11-19.) Based on known pharmacology, irbesartan is an AT1 receptor blocker. Its efficacy in hypertension and diabetic nephropathy has been established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, which is the pathway irbesartan blocks. This makes the prediction biologically plausible.

There is an important caveat. ARBs are generally contraindicated or used with great caution in bilateral renal artery stenosis because of the risk of acute kidney injury. The knowledge graph also lists renal artery obstruction among the contraindicated conditions. The high TxGNN score is a computational prediction only and does not address this safety concern.

Other predicted indications were also reviewed:
- **Malignant hypertensive renal disease** (score 0.9931): This is largely an extension of the existing hypertension and diabetic nephropathy label. It has no direct trials or literature, and the evidence level is L5.
- **Pulmonary hypertension, unclear multifactorial mechanism** (score 0.9925): Angiotensin II contributes to pulmonary vascular remodeling, so the approach is plausible but unproven. It has no trials or literature (L5), and systemic hypotension is a concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9925): This is the only prediction with literature support, all of it preclinical (L4). It is described in the notes below.

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

Irbesartan is marketed in India, with 20 valid registrations. The records contain no approved indication text.

<!-- review:begin in-lic-20261124c-irbesartan-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Irbesartan is marketed in India, with 20 valid single-ingredient registrations." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-irbesartan-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3146 | Aprovel 150mg Tablet | Strip of 14 tablets | Valid |
| 38738 | Coaprovel 150mg/12.5mg Tablet | Strip of 14 tablets | Valid |
| 53412 | Clindasaratan Plus 150mg/12.5mg/5mg Tablet | Strip of 10 tablets | Valid |
| 68635 | Debipro 150mg Tablet | Strip of 10 tablets | Valid |
| 69510 | Debipro H 150mg/12.5mg Tablet | Strip of 10 tablets | Valid |
| 98702 | Granry-AM Tablet | Strip of 10 tablets | Valid |
| 99527 | Granry 150 Tablet | Strip of 10 tablets | Valid |
| 100571 | Granry-D Tablet | Strip of 10 tablets | Valid |
| 100601 | Gatovel 300mg Tablet | Strip of 10 tablets | Valid |
| 108149 | Irovel H Tablet | Strip of 10 tablets | Valid |
| 108229 | Irovel 300 Tablet | Strip of 10 tablets | Valid |
| 110163 | Irbesdak-CT Tablet | Strip of 10 tablets | Valid |
| 110352 | Irbemax 150mg Tablet | Strip of 10 tablets | Valid |
| 110501 | Irbepex-AM Tablet | Strip of 10 tablets | Valid |
| 111392 | Irbenol 150mg Tablet | Strip of 10 tablets | Valid |
| 112286 | Irboris 150mg Tablet | Strip of 10 tablets | Valid |
| 113758 | Irbesdak 150mg Tablet | Strip of 10 tablets | Valid |
| 211875 | Sebri 300mg Tablet | Strip of 10 tablets | Valid |
| 244464 | Xarb 300 Tablet | Strip of 10 tablets | Valid |
| 252737 | Zognis H 150mg/12.5mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Conditions flagged as contraindicated in the knowledge graph** (not taken from label text): angioedema (including ARB-induced and hereditary forms), renal artery obstruction, anuria, hypotensive disorder, pancreatitis, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, hyperkalaemia-related and electrolyte disorders (potassium deficiency disease, hypercalcaemia, phosphorus metabolism disease), gout and hyperuricaemia, hyperparathyroidism, hepatic coma and encephalopathy, myopathy and rhabdomyolysis, and neonatal jaundice.
- **Drug Interactions**: 216 interactions were recorded. The **Major** interactions in the retrieved list are **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, acetylsalicylic acid, morphine, bupropion, aprepitant, dronabinol, and several bowel-preparation agents.

The package insert warnings and contraindications could not be obtained, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (0.9931) with no clinical trials or literature (L5). ARBs also carry a known risk of acute kidney injury in renal artery stenosis, which is the central lesion in renovascular hypertension.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, since this blocks safety screening
- Mechanism of action data for irbesartan from DrugBank
- A literature and trial search focused on ARBs in renovascular hypertension, including renal safety in unilateral versus bilateral renal artery stenosis
- A clinical review of whether the pulmonary hypertension (hypoxia) direction, which has preclinical support only, merits further preclinical or early clinical work

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

