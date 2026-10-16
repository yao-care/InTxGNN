---
layout: default
title: Vinpocetine
parent: Model Prediction Only (L5)
nav_order: 893
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Vinpocetine: predicted new indication Coronary artery disease (evidence level L5). Approved use: Dementia"
monitor_inn: "Vinpocetine"
predicted_indications: ["coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery", "lissencephaly", "alexia", "respiratory malformation", "Rienhoff syndrome"]
---

# Vinpocetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Vinpocetine: From Dementia to Coronary Artery Disease

## One-Sentence Summary

Vinpocetine is a drug originally used for dementia and cerebrovascular and cognitive disorders.
The TxGNN model predicts it may be effective for **Coronary Artery Disease**,
but **no clinical trials** and only **2 loosely related publications** (neither specific to coronary disease) currently support this prediction. The evidence is essentially computational.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dementia |
| Predicted New Indication | Coronary artery disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, vinpocetine inhibits phosphodiesterase 1 (PDE1A and PDE1C are listed as targets), which raises cyclic nucleotide levels and promotes vasodilation. It is also described as a voltage-gated sodium channel blocker with anti-inflammatory activity (for example, IKK inhibition).

Its established uses are in cerebrovascular disorders and age-related memory impairment, where it is thought to increase cerebral blood flow and provide neuroprotection. Coronary artery disease is also a vascular disease, so a vasodilatory and anti-inflammatory drug could plausibly be relevant.

This link is indirect. The available literature covers cerebrovascular disease and hypoxic pulmonary vascular remodelling, not coronary artery disease. The high TxGNN score is a computational prediction only.

Related preclinical work exists for a neighbouring indication, **myocardial ischemia** (ranked second). Two animal studies report cardioprotective effects of vinpocetine, one in isoproterenol-induced myocardial infarction in rats (2019) and one in mouse ischemia/reperfusion injury (2026). This supports a cardiovascular signal, but only in animals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17631470](https://pubmed.ncbi.nlm.nih.gov/17631470/) | 2007 | Review | Orvosi Hetilap | Reviews human studies of vinpocetine in cerebrovascular disease. Increasing cerebral blood flow may help patients with chronic hypoperfusion. Not specific to coronary disease. |
| [15377497](https://pubmed.ncbi.nlm.nih.gov/15377497/) | 2005 | Preclinical | Am J Physiol Lung Cell Mol Physiol | cAMP phosphodiesterase inhibitors potentiate prostacyclin analogs in hypoxic pulmonary vascular remodelling. Indirect, non-coronary evidence. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 35786 | COGNITOL 5 MG TABLET (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not specified |
| 40975 | Cogvin 10mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 36214 | Cogvin 5mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 150661 | Neurovin Tablet (Micro Labs Ltd) | Strip of 10 tablets | Not specified |
| 28592 | Brainpro 10mg Tablet (Vatican Life Sciences Pvt Ltd) | Strip of 10 tablets | Not specified |

There are 13 valid single-ingredient registrations in total, all oral tablets.

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 2 entries. Both are pharmacological target relationships rather than drug-drug interactions: vinpocetine acts on phosphodiesterase 1A (PDE1A) and phosphodiesterase 1C (PDE1C). No interaction severity levels are available.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The coronary artery disease prediction rests only on a computational score. There are no clinical trials, and the supplied literature does not address coronary disease. Animal data for the related indication of myocardial ischemia are encouraging but preclinical.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory sources, which is a blocking gap for safety screening
- Detailed mechanism-of-action data (for example, from DrugBank)
- Direct evidence in coronary artery disease, such as targeted literature searches or preclinical models
- Further evaluation of myocardial ischemia as a more evidence-supported research question
- Human cardiac safety and efficacy data before any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

