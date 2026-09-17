---
layout: default
title: Halothane
parent: Model Prediction Only (L5)
nav_order: 403
evidence_level: L5
indication_count: 6
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Halothane: From General Anesthesia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Halothane is a halogenated volatile agent historically used as an inhalational general anesthetic for surgical procedures. The TxGNN model predicts it may be relevant to **Manic Bipolar Affective Disorder**, but this direction is currently supported only by **0 clinical trials** and **5 publications**, most of which use halothane merely as a background anesthetic in animal studies of *other* psychiatric drugs rather than as a treatment being tested itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (inhalational anesthetic) — not documented as structured data in this evidence pack |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.82% (rank 3,747) |
| Evidence Level | L4 (indirect/mechanistic literature only, no clinical trials) |
| Taiwan Market Status | ✗ Not Marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, halothane is a halogenated volatile general anesthetic that acts on the central nervous system, primarily via potentiation of GABA-A receptor activity and modulation of other ion channels, to produce reversible loss of consciousness during surgery. No structured original-indication data was returned from the source registry used to build this evidence pack.

The mechanistic link to bipolar disorder is weak and indirect. GABAergic modulation is pharmacologically relevant to mood stabilization in a general sense (several approved mood stabilizers act on related CNS pathways), which is likely what drives the TxGNN association. However, the supporting literature retrieved for this candidate does not actually study halothane as a treatment for bipolar disorder — instead, halothane-anesthetized animals are used as an experimental *model* to study the cardiovascular or neuromuscular effects of other drugs (lithium, lamotrigine, neuroleptics). This is an important distinction: the co-occurrence of "halothane" and "bipolar disorder" in these papers reflects shared experimental context, not evidence of therapeutic effect.

Separately, halothane is administered as an inhaled gas for short-term intraoperative use under general anesthesia, which is operationally incompatible with the chronic, outpatient dosing required for a psychiatric maintenance therapy. This route/formulation mismatch should be considered a significant practical barrier independent of the mechanistic score. It is worth noting that several other TxGNN-predicted indications for this drug (bipolar disorder, major affective disorder, Tourette syndrome, trichotillomania) cluster around CNS/psychiatric conditions, but none currently has direct supporting clinical or observational evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29845450](https://pubmed.ncbi.nlm.nih.gov/29845450/) | 2018 | Preclinical (animal) | Cardiovascular Toxicology | Assessed lithium carbonate's cardiovascular safety margin in halothane-anesthetized dogs; halothane used as the anesthesia vehicle, not as the study drug |
| [835845](https://pubmed.ncbi.nlm.nih.gov/835845/) | 1977 | Preclinical (animal) | Anesthesiology | Evaluated lithium's effect on neuromuscular blocking agents in dogs anesthetized with halothane/N2O |
| [33136260](https://pubmed.ncbi.nlm.nih.gov/33136260/) | 2021 | Preclinical (animal) | Heart and Vessels | Reverse-translational study of lamotrigine-induced cardiovascular adverse events using halothane-anesthetized dogs |
| [3019784](https://pubmed.ncbi.nlm.nih.gov/3019784/) | 1986 | Mechanism study | Federation Proceedings | Studied lithium's effect on phosphoinositide metabolism in vivo; notes halothane (as an anesthetic) diminishes endogenous neural activity-related metabolite elevations |
| [6126494](https://pubmed.ncbi.nlm.nih.gov/6126494/) | 1982 | Case report | Journal of Clinical Psychopharmacology | Case of neuroleptic malignant syndrome compared in vitro with malignant hyperthermia (a known halothane-triggered condition); no abstract available |

**Note:** None of the above literature directly evaluates halothane's efficacy in bipolar disorder — all use halothane incidentally as an anesthetic in models studying other agents or conditions.

## Taiwan Market Information

Currently no registration information available — this product is not marketed in Taiwan (0 licenses on file).

## Safety Considerations

- **Drug Interactions**: 137 total interactions on record. Major-level interactions include Epinephrine, Dolasetron, Cisapride, Papaverine, and Macimorelin; Moderate-level interactions include Famotidine, Loperamide, Morphine, Clarithromycin, Levofloxacin, Ondansetron, Granisetron, and Promethazine, among others.

Detailed label warnings and contraindications are not yet available (Blocking data gap — TFDA label has not been retrieved); please refer to the package insert for full safety information once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting literature is indirect — it reflects halothane's incidental use as an anesthetic vehicle in studies of other drugs, not direct evidence of psychotropic efficacy — and there are no clinical trials. Combined with the drug's acute, inhalational route of administration (incompatible with chronic psychiatric treatment), its absence from the Taiwan market, and a Blocking data gap on TFDA label warnings/contraindications, the evidence base does not currently support advancing this candidate.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) to clear the Blocking data gap (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Dedicated pharmacological or clinical studies directly testing halothane's effect on mood/psychiatric symptoms (not merely using it as an anesthetic vehicle)
- Assessment of a clinically feasible route/formulation for chronic administration, given halothane's current use is limited to acute inhalational anesthesia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

