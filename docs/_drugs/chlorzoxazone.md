---
layout: default
title: Chlorzoxazone
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Chlorzoxazone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Indian license records (chlorzoxazone is generally…"
monitor_inn: "Chlorzoxazone"
predicted_indications: ["migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine with brainstem aura", "pulmonary hypertension", "atrophoderma vermiculata", "ulerythema ophryogenesis", "kyphoscoliotic heart disease", "rheumatoid arthritis"]
---

# Chlorzoxazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Chlorzoxazone: From Musculoskeletal Conditions to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Chlorzoxazone is a centrally acting skeletal muscle relaxant, marketed in India (the license records list no approved indication text).
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and only **3 indirect publications** (two reviews on vertigo and cerebellar disorders and one mouse study) are linked to this prediction.
This is a model-only prediction with very weak supporting evidence.

<!-- review:begin in-lic-20261124c-chlorzoxazone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Chlorzoxazone is a centrally acting skeletal muscle relaxant, marketed in India as a single-ingredient product (the license records list no approved indication text)." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-chlorzoxazone-1 -->

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian license records (chlorzoxazone is generally known as a muscle relaxant for musculoskeletal pain and spasm) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for chlorzoxazone: "Data available from animal experiments as well as human study indicate that chlorzoxazone acts primarily at the level of the spinal cord and subcortical areas of the brain where it inhibits multisynaptic reflex arcs involved in producing and maintaining skeletal muscle spasm of varied etiology. The clinical result is a reduction of the skeletal muscle spasm with relief of pain and increased mobility of the involved muscles." ([DailyMed: chlorzoxazone prescribing information, Solubiomix](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c3d40a90-6df8-4b44-bc61-d7655c52bacb), label version 2026-10-05; accessed 2026-11-19.) Based on known information, chlorzoxazone is a centrally acting muscle relaxant that also activates Ca²⁺-dependent K⁺ channels (SK/IK/BK).

The one mechanistic thread is a preclinical study (PMID 23115190). In mice carrying a CACNA1A mutation that enhances CaV2.1 currents, Ca²⁺-dependent K⁺-channel activators relieved cerebellar ataxia. CACNA1A mutations are also linked to familial hemiplegic migraine, so a plausible but **indirect** connection exists. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (such as migraine with brainstem aura), not biological evidence.

This link has clear limits. The ataxia study is in mice and does not test migraine. The other two papers are reviews of vertigo and cerebellar disorders and do not address migraine treatment. No data in migraine patients were provided.

Other predictions were also reviewed, and none is better supported:
- **Rheumatoid arthritis** (score 0.9905, L4, "Research Question"): the only other prediction with clinical-type literature, but it is limited to symptomatic pain and spasm relief.
- **The remaining predictions** (nephrogenic syndrome of inappropriate antidiuresis, pulmonary hypertension, atrophoderma vermiculata, ulerythema ophryogenesis, kyphoscoliotic heart disease): no trials or literature were supplied.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | J Neurol | Overview of drug treatment for cerebellar and central vestibular disorders (e.g., 4-aminopyridine for downbeat nystagmus); does not address migraine therapy |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Dtsch Arztebl Int | Treatment and natural course of peripheral and central vertigo; vestibular migraine accounts for about 11.4% of cases |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclinical (mouse) | J Neurosci | Ca²⁺-dependent K⁺-channel activators relieved ataxia caused by enhanced CaV2.1 currents in Cacna1a(S218L) mutant mice; this gene is also linked to hemiplegic migraine |

None of these papers evaluates chlorzoxazone in migraine patients.

---

## India Market Information

Valid registrations are on file; those held in the data, all of them combination products according to the Indian Medicine Dataset, are listed below, and no approved indication text is recorded for any of them.

<!-- review:begin in-lic-20261124b-chlorzoxazone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty valid single-ingredient registrations are on file. The first five are listed below; no approved indication text is recorded for any of them." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. The sentence also described the products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for some of them. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-chlorzoxazone-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4553 | Apgesic-S Tablet | Strip of 10 tablets | Valid |
| 65207 | Diproze MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 65210 | Dicron-MR Tablet | Strip of 10 tablets | Valid |
| 65830 | Dolozer MR Tablet | Strip of 10 tablets | Valid |
| 66101 | Declan MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 70543 | Demofen MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 71722 | Difquick MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 71790 | Dictus MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 83094 | Egiflam Tablet MR | Strip of 10 tablet mr | Valid |
| 92767 | Fibonac-MR Tablet | Strip of 10 tablets | Valid |
| 110686 | Inac MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 111667 | Inflacure MR 500mg/50mg/500mg Tablet | Strip of 10 tablets | Valid |
| 112112 | Integ MR Tablet | Strip of 10 tablets | Valid |
| 126199 | Ligesic-MR Tablet | Strip of 10 tablets | Valid |
| 138714 | Moufen-MR Tablet | Strip of 10 tablets | Valid |
| 160557 | Nobspas-MR Tablet | Strip of 10 tablets | Valid |
| 204842 | Stalogesic Forte 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 206196 | Seralin MR 250mg/50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 210702 | Surginac Forte Tablet | Strip of 10 tablets | Valid |
| 222195 | Teflam Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral tablets. The strengths in several product names (for example 250mg/50mg/325mg) reflect fixed-dose combination products, and the Indian Medicine Dataset lists further active ingredients for them.

<!-- review:begin in-lic-20261124b-chlorzoxazone-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The strengths in several product names (for example 250mg/50mg/325mg) suggest fixed-dose combination products, even though they are classified as single-ingredient in the records." Revised: the sentence said the data classify these products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for several of them (they are fixed-dose combinations). Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-chlorzoxazone-2 -->

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver failure, liver disease, gallbladder disease, substance abuse/dependence, drug-induced liver injury, paracetamol poisoning.
- **Drug interactions:** 72 interactions were identified. The main ones:
  - **Major:** morphine, liposomal morphine
  - **Moderate:** dronabinol, nabilone, metoclopramide, naltrexone, opium, sibutramine, ethanol, promethazine
  - Several others (for example warfarin, metformin, omeprazole) have an unclassified severity level.
- **Overdose:** a case report (PMID 19606800) describes methemoglobinemia after a multi-drug overdose that included chlorzoxazone. The drug's own contribution cannot be separated from the other agents taken.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a single indirect preclinical link (K⁺-channel activation in a CaV2.1 mouse model). No clinical trials or migraine-specific studies exist in the data compiled for this report. The liver-related contraindication signals and the sedative interactions with opioids and alcohol also call for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Indian regulatory sources (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search for chlorzoxazone in migraine and tension-type headache, and preclinical testing of K⁺-channel activation in migraine models
- Confirmation of the original approved indications in India
- If preclinical results are supportive, a small exploratory clinical study with hepatic monitoring

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available from the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: chlorzoxazone prescribing information, Solubiomix](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c3d40a90-6df8-4b44-bc61-d7655c52bacb) |
| 2026-11-24 | Revised: wording about the earlier partial table and the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Revised: the single-ingredient classification | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

