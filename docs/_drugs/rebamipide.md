---
layout: default
title: Rebamipide
parent: High Evidence (L1-L2)
nav_order: 723
evidence_level: L2
indication_count: 10
---

# Rebamipide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Rebamipide: From Gastroduodenal Ulcer to Esophageal Dyskinesia (GERD/NERD)

## One-Sentence Summary

Rebamipide is a mucosal protective agent originally used for gastroduodenal ulcer healing and gastritis. Across 10 TxGNN-predicted indications for this drug, the strongest evidence supports use in **esophageal dyskinesia (GERD/NERD)**, backed by **2 clinical trials (including 1 completed Phase 4 RCT)** and **5 publications**. The remaining 9 candidate indications currently have weak or no supporting evidence and are held at model-prediction stage only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured data; known clinical use is gastric mucosal protection / gastroduodenal ulcer healing / gastritis (per pharmacology reference data) |
| Predicted New Indication | Dyskinesia of Esophagus (GERD/NERD spectrum) |
| TxGNN Prediction Score | 96.86% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> Note: Of the 10 TxGNN-predicted indications provided for this drug, "dyskinesia of esophagus" is not the single highest-scoring candidate by raw TxGNN score, but it is the only one with clinical trial and literature support reaching evidence level L2. The top-scored candidate ("achlorhydria," 98.90%) has no supporting evidence (L5, Hold). See "Other Predicted Indications" below.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this evidence pack (flagged as a data gap). However, literature within the evidence pack (PMID 32598706, PMID 29069891) describes rebamipide's mechanism: it induces cyclooxygenase-2 and prostaglandin synthesis, scavenges oxygen free radicals, stimulates epidermal growth factor and VEGF, reduces lipid peroxidation and neutrophil migration, and — specifically relevant to the esophagus — upregulates tight junction protein expression in the esophageal mucosa, reducing mucosal permeability.

Rebamipide's original, well-established use is protecting the gastric mucosa. Esophageal dyskinesia/GERD-NERD involves impaired esophageal mucosal integrity and increased permeability from acid/reflux exposure — a pathophysiology closely related to the gastric mucosal injury rebamipide already treats. The mechanistic extension from "stomach mucosal protection" to "esophageal mucosal protection" is therefore biologically plausible and is not a purely computational (TxGNN-only) leap.

This is also the only candidate in the set with an actual completed randomized controlled trial: a Phase 4, multicenter, double-blind, placebo-controlled pilot study (NCT02755753, n=143) evaluating rebamipide as adjuvant therapy for erosive reflux esophagitis, plus a study specifically in PPI-refractory NERD patients (PMID 22367114) showing benefit when PPI monotherapy is insufficient. This combination of mechanistic plausibility and completed trial data separates it from the other 9 predicted indications in this drug's evidence pack, which are model-score-only or supported by indirect/animal data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02755753](https://clinicaltrials.gov/study/NCT02755753) | Phase 4 | Completed | 143 | Multicenter, randomized, double-blind, placebo-controlled pilot study (REPAIR) evaluating rebamipide as adjuvant therapy to heal erosive reflux esophagitis |
| [NCT07174882](https://clinicaltrials.gov/study/NCT07174882) | N/A | Active, not recruiting | 60 | Evaluates clinical course of non-erosive reflux disease (NERD) and esophageal mucosal resistance before/after combined therapy; relevance to rebamipide's mechanism is indirect (graded B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22367114](https://pubmed.ncbi.nlm.nih.gov/22367114/) | 2012 | RCT | Digestive Diseases and Sciences | Prospective randomized multicenter placebo-controlled study showing rebamipide efficacy in PPI-refractory NERD patients |
| [29069891](https://pubmed.ncbi.nlm.nih.gov/29069891/) | 2018 | Mechanistic/Clinical | Gut and Liver | Rebamipide plus PPI increases tight junction protein expression in esophageal mucosa in a rat GERD model |
| [20198424](https://pubmed.ncbi.nlm.nih.gov/20198424/) | 2010 | Clinical Study | Digestive Diseases and Sciences | Synergistic effect of rebamipide with low-dose (15mg) lansoprazole in preventing GERD symptom recurrence |
| [35552457](https://pubmed.ncbi.nlm.nih.gov/35552457/) | 2022 | Review (Pharmacovigilance) | Scientific Reports | Disproportionality analysis of adverse events for rebamipide vs. other PUD/GERD drugs using KIDS-KAERS database |
| [32598706](https://pubmed.ncbi.nlm.nih.gov/32598706/) | 2020 | Review | Terapevticheskii Arkhiv | Summarizes rebamipide's mucoprotective mechanism (COX-2/prostaglandin induction, free radical scavenging, EGF/VEGF/NO stimulation) in GERD treatment |

---

## Taiwan Market Information

Rebamipide currently has **no marketing authorization in Taiwan** (0 registrations). No license records are available to summarize product name, dosage form, or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and formal drug-drug interaction data are not currently available in this evidence pack (flagged as a **Blocking** data gap — TFDA label warnings/contraindications require retrieval and parsing from the TFDA website before this candidate can proceed to formal safety review). The single DDI-classified record in this dataset is a pharmacological target-binding profile (rebamipide binding to the CCK₁ receptor in a rat model) rather than a clinically validated drug interaction, and should not be treated as interaction guidance.

---

## Other Predicted Indications (Context)

For completeness, the remaining candidates predicted for rebamipide in this evidence pack, ranked by TxGNN score, are listed below. All currently sit at evidence level L3–L5 with a "Hold" or "Research Question" status due to absent or indirect (animal-only) evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------|------|------|
| 1 | Achlorhydria | 98.90% | L5 | Hold |
| 2 | Hiatus hernia | 98.71% | L4 | Hold |
| 3 | Cascade stomach | 98.55% | L4 | Hold |
| 4 | Gastric dilatation | 98.55% | L3 | Research Question |
| 5 | Dieulafoy lesion | 98.55% | L5 | Hold |
| 6 | Pylorospasm | 98.55% | L5 | Hold |
| 7 | Small bowel Crohn disease | 98.47% | L5 | Hold |
| 8 | Hemorrhagic duodenitis | 97.87% | L3 | Research Question |
| 9 | Esophageal ulcer | 97.50% | L5 | Hold |
| 10 | **Dyskinesia of esophagus** | 96.86% | **L2** | **Proceed with Guardrails** |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (specific to the esophageal dyskinesia/GERD-NERD indication)

**Rationale:**
Rebamipide has one completed Phase 4 RCT and a PPI-refractory NERD trial with a mechanistically consistent rationale (esophageal tight-junction protection), making this the only candidate in the set with real-world clinical support. All other 9 predicted indications for this drug currently lack sufficient evidence and should remain at Hold/Research Question status.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (currently a Blocking data gap — required before any safety review can proceed)
- Formal DrugBank-sourced mechanism of action data to replace the current literature-derived summary
- A validated drug-drug interaction dataset (the current DDI record is a pharmacology target-binding entry, not clinical interaction data)
- If pursuing Taiwan market entry, a full regulatory filing strategy, as rebamipide currently has zero registrations in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

