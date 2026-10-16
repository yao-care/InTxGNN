---
layout: default
title: Arformoterol
parent: High Evidence (L1-L2)
nav_order: 67
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Arformoterol: predicted new indication Obstructive lung disease (evidence level L1). Approved use: Chronic obstructive pulmonary disease, bronchitis, pulmonary emphysema"
---

# Arformoterol
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Arformoterol: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

Arformoterol is a long-acting beta-2 agonist bronchodilator, originally used to treat chronic obstructive pulmonary disease (COPD), bronchitis and emphysema.
The TxGNN model predicts it may be effective for **obstructive lung disease**,
with **1 clinical trial** and **20 publications** currently supporting this direction.
Note that this predicted indication overlaps heavily with the drug's existing indications, so it mainly confirms the current use rather than opening a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic obstructive pulmonary disease, bronchitis, pulmonary emphysema |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, arformoterol is the (R,R)-enantiomer of formoterol, a long-acting beta-2 adrenergic agonist. It relaxes airway smooth muscle and produces sustained bronchodilation.

Obstructive lung disease is the broad category that includes COPD, chronic bronchitis and emphysema, which are the drug's established indications. Bronchodilation is directly relevant to this group of conditions.

This should be read as a confirmation of the existing label rather than a true repurposing opportunity. The other nine predictions (for example compensatory emphysema, interstitial emphysema, tracheal stenosis and congenital lobar emphysema) have no trials or literature, and their mechanistic rationale is weak. They appear to reflect proximity in the knowledge graph rather than pharmacological logic, so they are on Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | Randomized, double-blind, double-dummy, active-controlled 6-month safety study of arformoterol 15 μg and 25 μg twice daily in COPD, also monitoring long-term efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25451347](https://pubmed.ncbi.nlm.nih.gov/25451347/) | 2014 | RCT | Chest | One-year safety and efficacy of arformoterol 15 μg twice daily in moderate to severe COPD |
| [20214460](https://pubmed.ncbi.nlm.nih.gov/20214460/) | 2010 | RCT | COPD | 6-month double-blind comparison of nebulized arformoterol (15 and 25 μg) and racemic formoterol dry powder inhaler in COPD |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | RCT | Ther Adv Respir Dis | 12-month safety and tolerance of arformoterol versus salmeterol in COPD, including whether benefit diminished over time |
| [18259972](https://pubmed.ncbi.nlm.nih.gov/18259972/) | 2008 | RCT | COPD | Effect of nebulized arformoterol on airway function in COPD, from two randomized trials |
| [25563342](https://pubmed.ncbi.nlm.nih.gov/25563342/) | 2015 | Review | Expert Opin Drug Saf | Review of the safety and efficacy of arformoterol in COPD |
| [39186816](https://pubmed.ncbi.nlm.nih.gov/39186816/) | 2024 | Review | Med Lett Drugs Ther | Overview of drugs for COPD |
| [32960872](https://pubmed.ncbi.nlm.nih.gov/32960872/) | 2020 | Review | Med Lett Drugs Ther | Overview of drugs for COPD |
| [18501650](https://pubmed.ncbi.nlm.nih.gov/18501650/) | 2008 | PK/PD study | Pulm Pharmacol Ther | Comparison of exposure and FEV1 between nebulized arformoterol and racemic formoterol dry powder inhaler in COPD |
| [31215259](https://pubmed.ncbi.nlm.nih.gov/31215259/) | 2019 | Cohort | COPD | Retrospective Medicare analysis of predictors of nebulized arformoterol treatment |
| [19011503](https://pubmed.ncbi.nlm.nih.gov/19011503/) | 2008 | Pooled analysis of 2 Phase 3 trials | Medicine | Arrhythmia frequency and effect of arformoterol and salmeterol in COPD, using 24-hour Holter monitoring |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121883 | Labaneb Respules (2ml Each) (Lupin Ltd) | Packet of 5 respules | Not specified in the data compiled for this report |

## Cytotoxicity

Not applicable. Arformoterol is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Drug Interactions**: 145 interactions were recorded. Those listed in the compiled data include:
  - **Moderate**: isometheptene, famotidine, epinephrine (including ophthalmic and topical forms), cisapride, clarithromycin, diethylpropion, dolasetron, ephedrine (including nasal), fenfluramine, granisetron, inhaled rapid-acting human insulin, levofloxacin
  - **Minor**: corticosteroids such as hydrocortisone, beclomethasone dipropionate, betamethasone, budesonide and dexamethasone
- **Cardiac safety**: A pooled Holter-monitoring analysis of two Phase 3 trials (PMID 19011503) evaluated arrhythmias with arformoterol and salmeterol in COPD patients. Cardiac monitoring remains a reasonable precaution with beta-agonists.

Warnings and contraindications from the package insert were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 trial data and several randomized trials support arformoterol in COPD, which fits the predicted obstructive lung disease indication (evidence level L1). However, this overlaps with the existing label and is not new repurposing. The other nine predicted indications have no supporting evidence and should remain on Hold.

**To proceed, the following is needed:**
- India package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Approved indication text for the Indian license, to confirm that the use is covered by the label
- Confirmation of whether any genuinely new indication beyond the existing label is of interest, since the top prediction is mainly a label confirmation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

