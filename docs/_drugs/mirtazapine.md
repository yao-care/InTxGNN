---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Mirtazapine: predicted new indication Ohdo syndrome and variants (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
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

## Mirtazapine: From Depression to Ohdo Syndrome and Variants
{: .text-alpha }

## One-Sentence Summary

Mirtazapine is an antidepressant originally used for depressive disorders (unipolar depression, major depressive disorder) and anxiety disorder.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mirtazapine: "The mechanism of action of mirtazapine for the treatment of major depressive disorder, is unclear. However, its efficacy could be mediated through its activity as an antagonist at central presynaptic α 2 -adrenergic inhibitory autoreceptors and heteroreceptors and enhancing central noradrenergic and serotonergic activity." ([DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887), label version 2025-08-06; accessed 2026-11-19.) Based on general pharmacological knowledge, mirtazapine is an antidepressant that acts through central alpha-2 adrenergic antagonism, 5-HT2/5-HT3 antagonism and H1 antagonism. Its efficacy in depression is established.

The link to the predicted indication is weak. Ohdo syndrome is a rare genetic neurodevelopmental disorder (blepharophimosis, intellectual disability, hypotonia), associated with chromatin-modifier defects such as KAT6B or MED12 variants, depending on the subtype. Mirtazapine's monoaminergic pharmacology has no established connection to this pathology. The very high score (0.9942) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, benefit could be symptomatic (for example sleep, appetite or mood), and this is speculative.

Two other predictions were also generated, and they are equally unsupported:
- **Blepharophimosis - intellectual disability syndrome, Ohdo type** (score 0.9911): a closely related entity to the first prediction. The similar scores suggest the predictions are not independent. No plausible disease-modifying mechanism is evident.
- **Benign paroxysmal torticollis of infancy** (score 0.9911): an episodic movement disorder related to migraine equivalents, often linked to CACNA1A variants. Only a speculative, indirect link exists. The condition is self-limiting and managed supportively, and mirtazapine carries a boxed warning for suicidality in young patients and is not established in infants.

## India Market Information

Mirtazapine has 20 valid single-ingredient registrations, all oral tablets (including mouth-dispersible and orally disintegrating forms). The approved indication text is not available for these registrations.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 49986 | Cuzapine 7.5mg Tablet | Strip of 10 tablets | Valid |
| 60378 | Deples 7.5mg Tablet | Strip of 10 tablets | Valid |
| 62497 | Deples 30 Tablet MD | Strip of 10 tablet md | Valid |
| 79583 | Eriza 7.5 Tablet MD | Strip of 10 tablet md | Valid |
| 135805 | Mirtee 15mg Tablet | Strip of 10 tablets | Valid |
| 136526 | Mirnite 7.5mg Tablet DT | Strip of 10 tablet dt | Valid |
| 136766 | Mirza 15mg Tablet | Strip of 10 tablets | Valid |
| 138668 | Mirtaj 15mg Tablet | Strip of 10 tablets | Valid |
| 139616 | Mirzat 7.5mg Tablet | Strip of 10 tablets | Valid |
| 139717 | Mitamark 7.5mg Tablet | Strip of 10 tablets | Valid |
| 139816 | Mirtalin 15mg Tablet | Strip of 10 tablets | Valid |
| 140043 | Mirfit 15 Tablet | Strip of 10 tablets | Valid |
| 140832 | Mirzap 30 Tablet | Strip of 10 tablets | Valid |
| 141002 | Mirtadep 15mg Tablet | Strip of 10 tablets | Valid |
| 142085 | Merty 2.5mg Tablet | Strip of 10 tablets | Valid |
| 144333 | Mirpine 7.5mg Tablet | Strip of 10 tablets | Valid |
| 145990 | Metramax 15mg Tablet | Strip of 10 tablets | Valid |
| 146587 | Mirtacin 15mg Tablet | Strip of 10 tablets | Valid |
| 146733 | Mitraford 30 Tablet | Strip of 10 tablets | Valid |
| 217532 | Tetrapine 15 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications / risk conditions (from knowledge graph disease associations, not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, epilepsy, manic bipolar affective disorder, liver disease, gallbladder disease, impaired renal function, neutropenia, agranulocytosis, hemoglobinopathy, hypertriglyceridemia, obesity disorder (including monogenic obesity), stroke and cerebrovascular disorder, cerebral infarction, myocardial infarction, coronary thrombosis, serotonin syndrome and drug-induced akathisia.
- **Drug Interactions:** 324 interactions were identified. Major-level interactions include:
  - Bupropion
  - Lorcaserin
  - Dolasetron
  - Palonosetron

  Moderate-level examples include famotidine, cimetidine, loperamide, aprepitant, morphine, dexamethasone, clarithromycin, levofloxacin, dronabinol, nabilone, eliglustat, obeticholic acid and several bowel-preparation laxatives.
- **Special population note:** Mirtazapine carries a boxed warning for suicidality in young patients, and its use in infants is not established. This is particularly relevant for the paediatric indications predicted here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predictions are supported by model scores only. There are no clinical trials or publications, and no plausible mechanistic link between mirtazapine's monoaminergic pharmacology and the genetic or developmental nature of these conditions. The target populations are also paediatric, which raises the safety bar.

**To proceed, the following is needed:**
- Mechanism of action data for mirtazapine from DrugBank
- Package insert warnings and contraindications from the India product labels (currently unavailable, which blocks safety screening)
- Preclinical or mechanistic evidence linking mirtazapine to the pathways involved in Ohdo syndrome or benign paroxysmal torticollis of infancy
- A review of whether any symptomatic benefit (sleep, appetite, mood) is clinically relevant, with a paediatric safety assessment

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

