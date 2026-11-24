---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 150
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Carvedilol: predicted new indication Malignant hypertensive renal disease (evidence level L5). In India: at least 20 listed products"
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Carvedilol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Carvedilol is a marketed beta-blocker with alpha-1 blocking activity, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** specific to this indication were found, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for carvedilol: "COREG is a racemic mixture in which nonselective β-adrenoreceptor blocking activity is present in the S(-) enantiomer and α1-adrenergic blocking activity is present in both R(+) and S(-) enantiomers at equal potency. COREG has no intrinsic sympathomimetic activity." ([DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39), label version 2026-07-31; accessed 2026-11-19.) Based on known pharmacology, carvedilol is a non-selective beta-blocker with additional alpha-1 blockade. Its efficacy in hypertension is established, and mechanistically it may be applicable to severe hypertension with kidney involvement through blood pressure lowering and reduced renin release.

The new indication is very close to the original one. Malignant hypertensive renal disease is a severe, kidney-damaging form of hypertension, so the high score may largely reflect proximity to the existing hypertension label rather than a genuinely new repurposing signal. In clinical practice, malignant hypertension is usually managed with rapid-acting parenteral agents, so the role of an oral beta-blocker is uncertain and cannot be verified from the available data.

The same model also ranks other related predictions: malignant renovascular hypertension (0.9955, also L5, no trials or literature), two forms of pulmonary hypertension (0.9954), and Braddock syndrome (0.9937, no identifiable mechanistic link). Among these, the pulmonary hypertension entry linked to lung disease and/or hypoxia has the only retrieved literature (indirect, mostly preclinical, L4). It includes a rat study showing carvedilol reversed hypertension induced by chronic intermittent hypoxia (PMID 26291659) and a rat study showing adrenergic blockade reversed right heart remodeling in pulmonary hypertension (PMID 20508210). Beta-blockade in lung disease and pulmonary arterial hypertension carries safety concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## India Market Information

Carvedilol is marketed in India with 20 valid registrations. Approved indication text was not available for these products.

<!-- review:begin in-lic-20261124c-carvedilol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Carvedilol is marketed in India with 20 valid single-ingredient registrations." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-carvedilol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34126 | Carca 3.125 Tablet | Strip of 15 tablets | Valid |
| 35451 | Carca 12.5 Tablet | Strip of 15 tablets | Valid |
| 35899 | Carloc 6.25 Tablet | Strip of 15 tablets | Valid |
| 35923 | Cardivas CR 40 Tablet | Strip of 10 tablet er | Valid |
| 36191 | Carloc I 3.125 Tablet | Strip of 10 tablets | Valid |
| 40998 | Carvipress 25mg Tablet | Strip of 10 tablets | Valid |
| 41659 | Cvl 6.25mg Tablet | Strip of 10 tablets | Valid |
| 42152 | Carvedil 25mg Tablet | Strip of 10 tablets | Valid |
| 42319 | Carvedil 12.5mg Tablet | Strip of 10 tablets | Valid |
| 45513 | Carveford 12.5mg Tablet | Strip of 10 tablets | Valid |
| 45707 | Cvdol-CR 10 Tablet | Strip of 10 tablet cr | Valid |
| 48837 | Carvizole 3.125mg Tablet | Strip of 10 tablets | Valid |
| 49849 | Carvitop 6.25mg Tablet IR | Strip of 10 tablet ir | Valid |
| 51806 | Carvenita 6.25mg Tablet | Strip of 10 tablets | Valid |
| 54264 | Carlant 3.125mg Tablet | Strip of 10 tablets | Valid |
| 62772 | DavaIndia Carvedilol 25mg Tablet | Strip of 10 tablets | Valid |
| 79172 | Edocar 6.25mg Tablet | Strip of 10 tablets | Valid |
| 109099 | Ivabid CV 3.125 Tablet | Strip of 14 tablets | Valid |
| 110821 | Irban Beta 6.25mg/5mg Tablet | Strip of 10 tablets | Valid |
| 118712 | Kar-B 6.25mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral tablets (immediate-release, controlled-release, and extended-release).

## Safety Considerations

- **Contraindications (not label text):** liver failure, asthma (including intrinsic and allergic), bronchitis, pulmonary emphysema and other bronchial disease, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), atrioventricular block, sick sinus syndrome (including the familial form), Prinzmetal angina, anaphylaxis, intraoperative floppy iris syndrome.
- **Drug Interactions:** 329 interactions were recorded. The main one is **Epinephrine (Major)**. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), bupropion, morphine, atropine, hyoscyamine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate). Minor interactions include acetylsalicylic acid, aluminum hydroxide, and attapulgite.
- For pulmonary hypertension in particular, the non-selective beta-blockade raises a theoretical bronchospasm concern in lung disease and hypoxia.

Please also refer to the package insert for label warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or literature for this indication (Evidence Level L5). The new indication overlaps heavily with the existing hypertension use, and standard management of malignant hypertension relies on parenteral agents.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to support the mechanistic link
- Package insert warnings and contraindications from the Indian regulator, which are currently missing and block safety screening
- Indication-specific clinical or observational evidence for malignant hypertensive renal disease
- A safety review of the knowledge-graph contraindications, especially bronchospastic disease, diabetes, hypotension, and conduction disorders
- If the pulmonary hypertension predictions are pursued, dedicated preclinical and clinical evidence addressing beta-blocker safety in that setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

