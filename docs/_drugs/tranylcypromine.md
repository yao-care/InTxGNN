---
layout: default
title: Tranylcypromine
parent: Model Prediction Only (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tranylcypromine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Tranylcypromine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "Ohdo syndrome and variants", "dysthymic disorder", "agoraphobia", "melancholia", "blepharophimosis - intellectual disability syndrome, Ohdo type", "neurotic disorder", "ligneous conjunctivitis", "Keppen-Lubinsky syndrome"]
---

# Tranylcypromine
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

# Tranylcypromine: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Tranylcypromine is an irreversible monoamine oxidase inhibitor (MAOI) antidepressant, originally used for unipolar depression, major depressive disorder and anxiety disorder.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tranylcypromine is a non-selective, irreversible MAO inhibitor. It raises brain monoamine levels, and this is the basis of its efficacy in depression and anxiety disorders.

Benign paroxysmal torticollis of infancy is a rare paediatric movement disorder. It is often linked to channelopathy genes such as CACNA1A. No plausible link between MAO inhibition and this condition is established in the available data. Tranylcypromine also inhibits LSD1 (KDM1A), an epigenetic enzyme, but this has no demonstrated connection to this condition.

The high score (99.67%, model rank 6,198) is a graph-based prediction and not clinical evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| Registration No. 215705 | Trivon Tablet | Oral tablet (strip of 10 tablets) | Intas Pharmaceuticals Ltd |

The registration data does not include an approved indication text. Only an oral formulation is registered.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** The graph links tranylcypromine to contraindications in the following areas:
  - Cardiovascular: hypertension, orthostatic hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest.
  - Endocrine: pheochromocytoma and paraganglioma, hyperthyroidism and Graves disease, diabetes and diabetic ketoacidosis.
  - Organ disease: liver, kidney and gallbladder disease.
  - Neuropsychiatric: epilepsy, bipolar disorder, substance abuse or dependence.
- **Drug interactions:** 151 interactions are recorded. Major-level examples include isometheptene, bupropion, morphine, lorcaserin, diethylpropion, phentermine, dolasetron and palonosetron. Moderate and minor interactions also exist, for example with epinephrine, sulfonylureas, repaglinide, insulin aspart and anticholinergics.
- **Paediatric concern:** A non-selective irreversible MAOI carries substantial risk in infants, notably hypertensive crisis (including dietary tyramine reactions) and the extensive interaction burden above.

Package insert warnings and contraindications for the India product have not been reviewed. Please refer to the package insert for label-level safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature (L5). No mechanistic link to MAO inhibition is established, and the target population is infants, for whom the safety profile of an irreversible MAOI is unfavourable.

**To proceed, the following is needed:**
- Mechanism of action data, and a credible biological rationale linking MAO or LSD1 inhibition to this condition
- India package insert warnings and contraindications (a blocking gap for safety screening)
- Any preclinical or clinical signal in the condition (case reports, animal models)
- A paediatric safety assessment, including tyramine and interaction risks
- Route and formulation compatibility assessment (only oral tablets are registered)

**Note on other predictions:** Other predictions in the same analysis have more support and are better candidates for follow-up:
- **Melancholia** (L3) and **neurotic depression** (L2) largely overlap with the existing depression indications. Both were rated "Proceed with Guardrails", with tyramine diet restriction, interaction screening and monitoring for bipolar switching as guardrails.
- **Dysthymic disorder**, **agoraphobia** and **neurotic disorder** (all L3) are suitable as research questions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

