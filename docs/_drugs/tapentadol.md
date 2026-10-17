---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 807
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tapentadol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Tapentadol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to"]
---

# Tapentadol
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

# Tapentadol: From Pain Management to Migraine Disorder

## One-Sentence Summary

Tapentadol is an oral centrally acting analgesic with 20 valid marketed registrations in India, although the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** directly evaluating tapentadol in migraine.
The available indirect literature points to cautions rather than support, because opioids are generally not recommended for migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (approved indication text is empty in all registrations) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tapentadol is generally described as a mu-opioid receptor agonist and norepinephrine reuptake inhibitor. This description comes from general pharmacological knowledge rather than the compiled data.

A link to migraine is plausible through central pain modulation and descending noradrenergic inhibition. The original indication is not recorded in the available registration data, so the relationship between it and migraine cannot be assessed directly.

The high TxGNN score (99.67%) is a computational prediction and does not reflect clinical evidence. Opioids are generally not recommended for migraine because of the risks of medication-overuse headache, chronification and dependence. The prediction is therefore not supported by current clinical practice guidance.

Two closely related predictions were also generated, with the same limitations:
- **Migraine with brainstem aura** (score 99.57%): a subtype of migraine with aura. It has no subtype-specific rationale, trials or literature.
- **Migraine with or without aura, susceptibility to** (score 99.08%): a genetic susceptibility phenotype rather than a treatable clinical condition, so a direct therapeutic link is weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly evaluates tapentadol in migraine. Two indirect publications were retrieved for the related susceptibility-phenotype prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohort | Drug, Healthcare and Patient Safety | Opioids are not recommended for routine migraine treatment because the risks of medication-overuse headache and abuse/dependence outweigh the benefits. Also notes an FDA warning of serotonin syndrome when opioids are combined with triptans or serotonergic antidepressants. |
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opinion on Pharmacotherapy | Reviews NSAIDs and acetaminophen as non-opioid alternatives for acute pain, in light of the opioid overdose crisis. Does not evaluate tapentadol in migraine. |

---

## India Market Information

Tapentadol has 20 valid single-ingredient registrations and no cancelled ones. The approved indication text is not available for any of them. The main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 226603 | Tpd Plus 50mg Tablet | Strip of 10 tablets | Not available |
| 230052 | Tapencet ER 75 Tablet | Strip of 10 extended-release tablets | Not available |
| 151371 | Nudol 50mg Tablet | Strip of 10 tablets | Not available |
| 157712 | Newtap 75mg Tablet | Strip of 10 tablets | Not available |
| 67291 | Dazfast 100mg Tablet | Strip of 10 tablets | Not available |

All registered forms are oral (immediate-release and extended-release tablets).

---

## Safety Considerations

- **Drug Interactions**: 120 interactions were identified in total. Examples at the **Major** level include:
  - Bupropion
  - Morphine
  - Lorcaserin
  - Diethylpropion
  - Dolasetron
  - Palonosetron
  - Phentermine

  Examples at the **Moderate** level include epinephrine, hyoscyamine, atropine, glycopyrronium, dicyclomine, naloxone, dronabinol and nabilone.
- **Serotonergic interaction potential**: Published literature notes an FDA warning of serotonin syndrome risk when opioids are used with triptans or serotonergic antidepressants (SSRIs/SNRIs). This is directly relevant to migraine, where triptans are standard therapy.
- **Class-level concerns in migraine**: Medication-overuse headache, chronification of headache, and dependence are risks of opioid use in migraine.

Please refer to the package insert for warnings and contraindications, as this information is not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials and no literature showing tapentadol efficacy in migraine. The indirect evidence indicates that opioids are not recommended for migraine, and there is a serotonergic interaction concern with triptans and SNRIs/SSRIs.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, which currently block safety screening
- Approved indication text for the registered products, to establish the original indication
- Mechanism of action data from DrugBank
- Evidence that tapentadol offers a benefit over existing migraine therapies that outweighs the risks of medication-overuse headache and dependence
- Any preclinical or clinical studies of tapentadol in migraine, if such work is considered justified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

