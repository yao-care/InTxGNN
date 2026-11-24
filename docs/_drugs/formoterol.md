---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). In India: at least 20 listed products"
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Formoterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting beta2-adrenergic agonist that relaxes airway smooth muscle and is marketed in India as inhaled and capsule products.
The TxGNN model predicts it may be relevant to **respiratory malformation**, but **no clinical trials** and **no publications directly studying this condition** were found.
The prediction rests on model output alone and is not supported by a plausible mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for formoterol: "Formoterol fumarate is a long-acting, beta 2 -adrenergic receptor agonist (beta 2 -agonist). Inhaled formoterol fumarate acts locally in the lung as a bronchodilator. In vitro studies have shown that formoterol has more than 200-fold greater agonist activity at beta 2 -receptors than at beta 1 -receptors." ([DailyMed: Formoterol Fumarate Inhalation Solution (formoterol fumarate dihydrate) prescribing information, Ritedose Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9bf685-8886-4865-834b-2748af124b79), label version 2025-12-10; accessed 2026-11-19.) Formoterol is known as a long-acting beta2-adrenergic agonist, which causes bronchodilation by relaxing airway smooth muscle.

Respiratory malformation is a structural, developmental defect of the airways or lungs. Bronchodilation could at most ease secondary airflow symptoms; it cannot correct or treat the malformation itself. No plausible mechanistic link is supported.

The high score appears to reflect the drug's closeness to respiratory disease in the model's network rather than a true therapeutic relationship. The prediction should be treated as a weak hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications directly studies respiratory malformation. They concern COPD, asthma and other conditions, and are listed only as background on formoterol in airway disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT (crossover) | Eur Respir J | Repeated-dose budesonide/formoterol compared with salbutamol in stable adult asthma (bronchodilator, systemic and cardiovascular effects) |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Long-term safety and asthma control of budesonide/formoterol pMDI in African American patients |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Systematic review / meta-analysis | J Am Pharm Assoc | Safety and efficacy of budesonide/glycopyrrolate/formoterol versus glycopyrrolate/formoterol in COPD |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Budesonide/formoterol pMDI in persistent asthma |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Mechanistic clinical study | Eur Respir J | Formoterol protects against platelet-activating factor-induced effects in asthma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Physiological study | Eur J Appl Physiol | Compensatory responses to increased mechanical abnormalities in COPD during sleep |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | Small airway disease in post-acute COVID-19 syndrome |

## India Market Information

At least 20 valid licences were found, and the list may be partial.

<!-- review:begin in-lic-20261124c-formoterol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 valid single-ingredient licences were found, and the list may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-formoterol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3183 | Airwin-BF 200 Capsule | Bottle of 30 capsules | Valid |
| 10114 | Airwin-BF 400 Inhaler | Bottle of 120 MDI Inhaler | Valid |
| 29498 | Budevin F 6mcg/400mcg Inhaler | Box of 120 MDI Inhaler | Valid |
| 29967 | Budirik 200 Capsule | Bottle of 30 capsules | Valid |
| 41789 | Combihale FF 100 DPI Capsule | Bottle of 30 capsules | Valid |
| 61813 | Duova Rotacap | Packet of 20 rotacaps | Valid |
| 84129 | Formoflo 250 Transhaler | Packet of 120 MDI Transhaler | Valid |
| 84424 | Formoflo Forte Transcaps | Bottle of 30 transcaps | Valid |
| 84701 | Fluticort F 250 Inhaler | Packet of 120 MDI Inhaler | Valid |
| 84807 | Fomtide 400 CFC Free Inhaler | Packet of 120 MDI Inhaler | Valid |
| 85742 | Fabhale 200 Capsule | Bottle of 30 capsules | Valid |
| 87347 | Flutidin F 6mcg/250mcg Divicap | Strip of 30 capsules | Valid |
| 87423 | Formonide 200 Novocart | Packet of 100 MDI Novocart | Valid |
| 95920 | Glycoprl-F Dpicaps | Bottle of 30 capsules | Valid |
| 176746 | Pulmofor B 200 Inhaler | Bottle of 120 MDI Inhaler | Valid |
| 199689 | Symbicort 160mcg/4.5mcg Turbuhaler | Packet of 60 MDI Inhaler | Valid |
| 216849 | Tiomate Hfa 6mcg/9mcg Inhaler | Packet of 1 Inhaler | Valid |
| 221330 | Tioform Hfa 6mcg/9mcg Inhaler | Packet of 120 MDI Inhaler | Valid |
| 230532 | Unipuff FB 6mcg/200mcg Capsule | Bottle of 30 capsules | Valid |
| 241736 | Winkast F Inhaler | Packet of 120 MDI Inhaler | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 462 interactions are recorded. Examples at moderate level include acarbose, famotidine, clarithromycin, cisapride, dolasetron, ephedrine, isometheptene, diethylpropion, and several antidiabetic agents (alogliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide, dulaglutide, chlorpropamide). Minor interactions include corticosteroids such as beclomethasone, betamethasone, budesonide and dexamethasone.

Please refer to the package insert for warnings and contraindications; this information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trial or publication studies respiratory malformation, and bronchodilation cannot plausibly treat a structural developmental defect.

**To proceed, the following is needed:**
- Mechanism-of-action data and a credible biological rationale linking beta2-agonism to the target condition
- Package insert warnings and contraindications
- Any direct preclinical or clinical study in respiratory malformation, or a clearly defined symptom-relief use case with a defined patient group

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Formoterol Fumarate Inhalation Solution (formoterol fumarate dihydrate) prescribing information, Ritedose Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9bf685-8886-4865-834b-2748af124b79) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

