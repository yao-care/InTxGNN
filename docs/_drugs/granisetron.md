---
layout: default
title: Granisetron
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not stated in the Indian licence records compiled for this report (gr…"
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetron: From Chemotherapy-Associated Nausea and Vomiting to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist that is widely marketed in India as an antiemetic. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records compiled for this report (granisetron is generally known as an antiemetic) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for granisetron: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), label version 2026-04-30; accessed 2026-11-19.) Granisetron is generally described as a selective 5-HT3 receptor antagonist. Its established use is to prevent nausea and vomiting, although none of the 20 Indian licence entries lists an approved indication text.

The proposed link to manic bipolar disorder is hypothetical. 5-HT3 antagonism has been suggested to modulate dopaminergic and serotonergic signalling in the central nervous system, and these pathways are implicated in mood disorders. No trials or publications were supplied to test this idea, so the high score (0.9962) should be read as a computational association only.

Other top-ranked predictions have varying degrees of biological plausibility. Tourette syndrome (99.5%) and trichotillomania (99.2%) have loose serotonergic or dopaminergic rationales. Allergic urticaria (99.3%) has a weak itch-related rationale. Several others, such as nephrogenic syndrome of inappropriate antidiuresis, contagious conjunctivitis and bronchitis, have no evident mechanistic connection. All ten predictions are at evidence level L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty valid single-ingredient registrations exist and none are cancelled. The licence records contain no approved indication text. The first five registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 98677 | Granipel Oral Drops (Pelzar Healthcare) | Bottle of 15 ml oral drops | Not stated |
| 78780 | Emergan 1mg Injection (H & Care Incorp) | Vial of 3 ml injection | Not stated |
| 9427 | Anset G 3mg Injection (Bennet Mypher Pharmaceuticals LLP) | Vial of 3 ml injection | Not stated |
| 97683 | Grawel 1mg Tablet (Zee Laboratories) | Strip of 4 tablets | Not stated |
| 94658 | Graniset 1 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 4 tablets | Not stated |

Available routes are oral (drops, tablets, orally disintegrating and dispersible tablets) and injectable (1 ml and 3 ml presentations). Route compatibility with the predicted indication has not been assessed.

## Safety Considerations

- **Knowledge-graph contraindication signals**: Drug–disease contraindication links in the TxGNN knowledge graph (not label text) include long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest and heart conduction disease. These point to a QT-prolongation and arrhythmia concern.
- **Drug Interactions**: The interaction query returned 461 interacting drugs. The 20 examples compiled include these Major-level interactions:
  - Opioids and analgesics: fentanyl, alfentanil, tramadol, dextromethorphan
  - Triptans: almotriptan, sumatriptan
  - QT-relevant or cardiac drugs: amiodarone, amisulpride, amitriptyline, anagrelide
- **Moderate-level examples**: abametapir (topical), abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin and propofol.

This matters for a bipolar disorder population, where antipsychotics, antidepressants and other QT-prolonging or serotonergic drugs are commonly co-prescribed. Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for manic bipolar affective disorder is supported only by a model score (L5), with no registered trials or publications. The mechanistic link is speculative, and the cardiac-conduction signals and interaction burden are relevant to a population likely to take multiple psychotropic drugs.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the Indian regulatory source
- Mechanism of action data from DrugBank
- A systematic literature and trial search on 5-HT3 antagonists in mania or bipolar disorder
- Preclinical or mechanistic evidence linking 5-HT3 antagonism to mood regulation
- A QT and interaction risk assessment for co-medication with psychotropic drugs
- A comparison with the other top predictions (such as Tourette syndrome and trichotillomania) to decide which has the strongest rationale for further study

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

