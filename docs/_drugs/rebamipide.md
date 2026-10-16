---
layout: default
title: Rebamipide
parent: Model Prediction Only (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rebamipide: predicted new indication Esophageal dyskinesia (evidence level L5). Approved use: Peptic ulcer disease, gastritis"
---

# Rebamipide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Rebamipide: From Peptic Ulcer Disease and Gastritis to Esophageal Dyskinesia

## One-Sentence Summary

Rebamipide is a mucosal protective agent originally used to treat peptic ulcer disease and gastritis.
The TxGNN model predicts it may be effective for **esophageal dyskinesia** (the top-ranked prediction, achlorhydria, has no supporting evidence and no plausible mechanism, so the best-supported candidate is reported here). Support currently consists of **1 completed clinical trial** (in reflux esophagitis, an adjacent condition) and **5 publications**, mostly in reflux disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastritis (the licence records in India carry no indication text) |
| Predicted New Indication | Esophageal dyskinesia (best-supported of the 10 predictions; the highest TxGNN-scored prediction is achlorhydria) |
| TxGNN Prediction Score | 96.86% (achlorhydria, the top-scored prediction: 98.90%, evidence level L5) |
| Evidence Level | L2 (capped at L2 because the evidence comes from an adjacent reflux population) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Literature describes rebamipide as a mucoprotective drug that induces cyclooxygenase-2 and prostaglandins, scavenges oxygen free radicals, stimulates epidermal growth factor, VEGF and nitric oxide, and reduces lipid peroxidation and neutrophil migration.

Its efficacy as a gastric mucosal protectant is established. Esophageal dyskinesia is a motility disorder, so rebamipide does not directly address its core problem. The link is indirect: the evidence concerns reflux disease (GERD and non-erosive reflux disease), where rebamipide improves tight junction protein expression and mucosal integrity, especially combined with proton pump inhibitors. The prediction is therefore plausible mainly as an adjunct for reflux-related mucosal injury rather than as a treatment for the motility abnormality itself.

For context, other predictions fare differently. Esophageal ulcer has the broadest literature (L3), including a meta-analysis in dyspepsia and animal and clinical data in reflux esophagitis. Hemorrhagic duodenitis is supported by preclinical and cohort data (L4). Achlorhydria, Dieulafoy lesion, pylorospasm and small bowel Crohn disease have no direct evidence and weak or speculative mechanistic links.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02755753](https://clinicaltrials.gov/study/NCT02755753) | Phase 4 | Completed | 143 | Randomized, double-blind, placebo-controlled pilot (REPAIR) of rebamipide as an adjuvant to heal erosive reflux esophagitis; population is reflux, not esophageal dyskinesia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22367114](https://pubmed.ncbi.nlm.nih.gov/22367114/) | 2012 | Randomized placebo-controlled clinical study | Dig Dis Sci | Efficacy of rebamipide in PPI-refractory non-erosive reflux disease |
| [20198424](https://pubmed.ncbi.nlm.nih.gov/20198424/) | 2010 | Clinical study | Dig Dis Sci | Synergistic effect of rebamipide with low-dose lansoprazole in managing GERD symptom recurrence |
| [32598706](https://pubmed.ncbi.nlm.nih.gov/32598706/) | 2020 | Review | Ter Arkh | Rebamipide plus PPI is more effective for GERD symptom relief; mechanism via COX-2, prostaglandins and antioxidant effects |
| [29069891](https://pubmed.ncbi.nlm.nih.gov/29069891/) | 2018 | Preclinical (rat) | Gut Liver | Additive effect of rebamipide and PPIs on tight junction proteins in GERD model |
| [35552457](https://pubmed.ncbi.nlm.nih.gov/35552457/) | 2022 | Pharmacovigilance analysis | Sci Rep | Adverse event signals of rebamipide compared with other peptic ulcer and GERD drugs in the elderly |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185346 | Rebator 100mg Tablet | Strip of 10 tablets | Not stated |
| 187266 | Rebam 100mg Tablet | Strip of 10 tablets | Not stated |
| 134965 | Mucogen 100mg Tablet | Strip of 10 tablets | Not stated |
| 184145 | Rebagen Tablet | Strip of 10 tablets | Not stated |
| 184375 | Rebagen-Otic Capsule | Strip of 10 capsules | Not stated |

Four more registrations are eye-drop products: Finetears, Rebacer, Eyesec and Rebasoothe (10 ml bottle or packet). All 9 registrations are valid single-ingredient products.

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only a pharmacology target record (rebamipide at the CCK1 receptor in rat), not a clinical drug-drug interaction.
- **Pharmacovigilance**: A 2022 analysis of Korean adverse event reports compared rebamipide's safety signals with other peptic ulcer and GERD drugs in the elderly.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rebamipide has solid mucosal protection data in reflux disease, but esophageal dyskinesia is a motility disorder. The only randomized evidence (a Phase 4 pilot, n=143) comes from reflux esophagitis, so support for the predicted indication is indirect. The top TxGNN-scored prediction (achlorhydria) is not mechanistically credible.

**To proceed, the following is needed:**
- Direct clinical evidence in esophageal motility disorders, or a refined target such as reflux-related mucosal injury, where evidence is stronger (esophageal ulcer, erosive reflux esophagitis)
- Detailed mechanism of action data
- Package insert warnings and contraindications for the India-marketed products
- Confirmation of the approved indication text for the registered products
- Route compatibility assessment (oral tablets and capsules are available; the other registered forms are ophthalmic)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

