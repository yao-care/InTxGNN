---
layout: default
title: Halothane
parent: Model Prediction Only (L5)
nav_order: 407
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Halothane: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not stated in the India licence data (the approved indication text is…"
monitor_inn: "Halothane"
predicted_indications: ["manic bipolar affective disorder", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "trichotillomania", "bipolar disorder", "major affective disorder"]
---

# Halothane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Halothane: From General Anaesthesia to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Halothane is a volatile inhaled anaesthetic. The TxGNN model (deep learning) predicts it may be effective for **manic bipolar affective disorder**, but this is a model prediction only, with **0 clinical trials** and **4 publications**. None of those publications studies halothane as a treatment for mania; they concern lithium or lamotrigine tested under halothane anaesthesia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence data (the approved indication text is blank). Halothane is a general inhalation anaesthetic. |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Halothane is generally known as a volatile anaesthetic that enhances GABA-A receptor activity and modulates K2P potassium channels. A speculative link to mood disorders could be drawn through GABAergic modulation, but no study in the compiled data supports this.

The high score (0.9982) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. All four retrieved publications concern lithium or lamotrigine, which are mood stabilisers. They cover anaesthetic interactions, cardiovascular safety margins and phosphoinositide metabolism, and halothane appears only as the anaesthetic used in the animal models. The association most likely reflects drug-interaction or anaesthetic-management links with lithium rather than any benefit of halothane for mania.

Other predicted indications are even less supported. Nephrogenic syndrome of inappropriate antidiuresis, Tourette syndrome and trichotillomania have no trials or literature, and bipolar disorder and major affective disorder have only indirect, non-halothane literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29845450](https://pubmed.ncbi.nlm.nih.gov/29845450/) | 2018 | Preclinical (safety pharmacology) | Cardiovascular Toxicology | Cardiovascular safety margin of lithium carbonate assessed in halothane-anaesthetised dogs; halothane is the experimental background, not the treatment. |
| [33136260](https://pubmed.ncbi.nlm.nih.gov/33136260/) | 2021 | Preclinical (reverse translational) | Heart and Vessels | Lamotrigine-induced cardiovascular adverse events analysed in halothane-anaesthetised dogs (n = 4). |
| [835845](https://pubmed.ncbi.nlm.nih.gov/835845/) | 1977 | Pharmacology study | Anesthesiology | Lithium carbonate altered responses to neuromuscular blocking agents in halothane/N2O-anaesthetised dogs. |
| [3019784](https://pubmed.ncbi.nlm.nih.gov/3019784/) | 1986 | Preclinical | Federation Proceedings | Lithium effects on phosphoinositide metabolism in vivo; halothane reduced the lithium-induced rise in brain inositol phosphate. |

These papers do not show that halothane treats mania or bipolar disorder. For major affective disorder, the only retrieved paper (PMID 11239906, a 2001 preclinical study of cold exposure and locus coeruleus activity in *Biological Psychiatry*) is also unrelated to halothane.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 104507 | Hypnothane Liquid For Inhalation (Neon Laboratories Ltd) | Bottle of 250 ml solution for inhalation | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): liver disease, gallbladder disease, hypotensive disorder, sudden cardiac arrest, heart conduction disease, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri and intracranial hypertension.
- **Known risks noted in the analysis**: a narrow therapeutic index, hepatotoxicity (halothane hepatitis) and cardiac sensitisation. These make chronic use for a psychiatric or neurological condition impractical.
- **Drug Interactions**: 137 interactions were recorded. Major-level ones include:
  - Epinephrine
  - Dolasetron
  - Cisapride
  - Papaverine
  - Macimorelin

  Moderate-level examples include morphine, ondansetron, granisetron, levofloxacin, clarithromycin and promethazine.

Please refer to the package insert for warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the retrieved literature is about lithium and lamotrigine rather than halothane. Halothane's hepatotoxicity and cardiac risks, together with the lack of a plausible mechanism, argue against chronic use in mania or any other predicted indication.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic link between halothane and mood regulation
- Package insert warnings and contraindications from the India licence (currently missing, and a blocking gap for safety screening)
- The approved indication text for the India licence
- Direct preclinical or clinical evidence of halothane efficacy in mania, which does not currently exist in the compiled data
- A risk-benefit assessment showing a feasible dosing route, since halothane is only available as an inhalation solution
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

