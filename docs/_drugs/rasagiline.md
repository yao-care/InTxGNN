---
layout: default
title: Rasagiline
parent: Model Prediction Only (L5)
nav_order: 721
evidence_level: L5
indication_count: 6
---

# Rasagiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Rasagiline: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

> Rasagiline is a selective MAO-B inhibitor conventionally used to treat Parkinson's disease.
> The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
> but this prediction is currently supported by **no clinical trials** and **no published literature** — it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (based on known drug class; not captured in Taiwan regulatory data as the product is not marketed locally) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Rasagiline is currently marked as a data gap in this evidence pack. Based on known clinical information, Rasagiline is a selective, irreversible MAO-B (monoamine oxidase-B) inhibitor, established for use in Parkinson's disease, where it reduces dopamine breakdown in the central nervous system and is thought to have a secondary neuroprotective (anti-apoptotic) effect on dopaminergic neurons.

PLA2G6-associated neurodegeneration (which includes NBIA/INAD subtypes) shares a pathological hallmark with Parkinson's disease: basal ganglia iron accumulation and progressive degeneration of dopaminergic neurons. This overlap gives the TxGNN prediction some theoretical mechanistic plausibility — a drug that protects dopaminergic neurons in one iron/dopamine-related neurodegenerative pathway could plausibly extend to another. However, this remains an indirect, knowledge-graph-derived inference rather than a proven pharmacological relationship, and no direct molecular-level evidence in this rare disease exists.

It is worth noting that among the six candidates in this evidence pack, "paralysis agitans, juvenile, of Hunt" (juvenile parkinsonism) has the strongest mechanistic rationale, since it is clinically similar to classic Parkinson's disease. The remaining candidates (Rasmussen encephalitis, myelitis, transaldolase deficiency, and a cortical malformation syndrome) have no known mechanistic link to MAO-B inhibition and should be treated as low-confidence statistical associations only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Rasagiline is currently **not marketed** in Taiwan (0 registered licenses). No product-level registration data is available for review.

## Safety Considerations

**Drug Interactions** (137 total interactions on file; selected examples):

| Interacting Drug | Severity |
|---|---|
| Bupropion | Major |
| Morphine | Major |
| Epinephrine | Moderate |
| Chlorpropamide | Moderate |
| Cimetidine | Moderate |
| Diethylpropion | Moderate |
| Difenoxin | Moderate |
| Diphenoxylate | Moderate |
| Dronabinol | Moderate |
| Obeticholic acid | Moderate |
| Phentermine | Moderate |
| Glimepiride | Moderate |
| Multiple insulin formulations (aspart, degludec, detemir, glargine, glulisine, isophane, regular, inhaled) | Moderate |

These interaction patterns (sympathomimetics, opioids, and glucose-lowering agents) are consistent with known MAO-B inhibitor pharmacology and warrant caution regardless of the indication under consideration.

Detailed labeling warnings and contraindications are not yet available (TFDA package insert data gap — see Conclusion below).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications are at Evidence Level L5 — model prediction only, with zero supporting clinical trials or literature. The drug is also not currently marketed in Taiwan, and a blocking data gap (missing TFDA label warnings/contraindications) prevents the candidate from passing the S1 safety screening gate.

**To proceed, the following is needed:**
- Obtain TFDA package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirm mechanism of action via DrugBank API — currently a **High** severity data gap (DG002)
- Preclinical or mechanistic studies specifically linking MAO-B inhibition to PLA2G6-associated neurodegeneration
- If further exploration is warranted, prioritize "paralysis agitans, juvenile, of Hunt" for follow-up given its stronger mechanistic overlap with Parkinson's disease, rather than the current top-ranked candidate by TxGNN score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

