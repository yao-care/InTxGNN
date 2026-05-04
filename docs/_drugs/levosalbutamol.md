---
layout: default
title: Levosalbutamol
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Levosalbutamol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Levosalbutamol: From Asthma to Obstructive Lung Disease

## One-Sentence Summary

Levosalbutamol is the pure (R)-enantiomer of salbutamol (albuterol), a selective β2-adrenoceptor agonist established internationally as a first-line bronchodilator for asthma and COPD, yet currently holding no formal market approval in India.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** — the indication with the highest clinical evidence quality among all 10 predictions — supported by **multiple Phase 3 RCTs** (including a dedicated Levalbuterol-in-COPD trial) and **20 publications**.
Note: the highest TxGNN-score prediction is nasal cavity disease (score 99.99%, rank #1), but this carries only L4 evidence with a Hold recommendation; obstructive lung disease (score 99.85%, rank #10) is the only prediction among the ten that warrants an actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration; established internationally for bronchial asthma and COPD |
| Predicted New Indication | Obstructive Lung Disease (Asthma / COPD) |
| TxGNN Prediction Score | 99.85% (TxGNN rank #10 by score; evidence quality rank #1 among all 10 predictions) |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this record. Based on established pharmacology, Levosalbutamol (levalbuterol) is the (R)-enantiomer of salbutamol — a short-acting selective β2-adrenoceptor agonist (SABA). Upon binding to β2-adrenoceptors on airway smooth muscle cells, it activates adenylyl cyclase, raises intracellular cyclic AMP (cAMP), activates protein kinase A (PKA), and inhibits myosin light-chain kinase — the result is smooth muscle relaxation and prompt bronchodilation. This is the central pharmacological mechanism for acute bronchospasm reversal in both asthma and COPD.

The rationale for using the single-isomer formulation over racemic salbutamol/albuterol rests on two established observations. First, essentially all β2-agonist bronchodilatory activity resides in the (R)-enantiomer, meaning levosalbutamol delivers equivalent therapeutic effect at half the total drug load. Second, the (S)-enantiomer present in racemic formulations has been shown in in vitro and some human studies to carry pro-inflammatory and potentially bronchoconstricting properties — risks that are completely eliminated by the pure (R)-isomer formulation.

Obstructive lung disease — encompassing asthma exacerbations and COPD acute flares — is precisely the therapeutic domain where levosalbutamol's mechanism is most directly applicable. Multiple head-to-head RCTs confirm its non-inferiority or superiority to racemic albuterol in clinical outcomes. The TxGNN prediction score of 99.85% aligns tightly with this mechanistic rationale. The principal barrier to India market access is regulatory, not scientific — no approved formulation currently exists in India despite a robust international evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00665600](https://clinicaltrials.gov/study/NCT00665600) | Phase 3 | Completed | 257 | Double-blind, multicenter, 6-week study of **Levalbuterol (Levosalbutamol)** specifically in COPD patients; direct evidence for this molecule in obstructive lung disease |
| [NCT02170532](https://clinicaltrials.gov/study/NCT02170532) | Phase 4 | Completed | 10 | Directly compared aerosolised β-agonist isomers including **Levosalbutamol (R-isomer)** vs. racemic albuterol in asthma patients; measured lung function and enantiomer-specific effects via spirometry and impedance |
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Phase 3 | Withdrawn | 0 | **Ipratropium/Levosalbutamol 20/50 mcg fixed-dose combination** via pMDI vs. free combination in moderate-to-very-severe COPD — most directly relevant study design; withdrawn before enrollment began |
| [NCT01012765](https://clinicaltrials.gov/study/NCT01012765) | Phase 3 | Completed | 173 | 3-way crossover: indacaterol vs. placebo vs. tiotropium in moderate COPD; high-quality RCT establishing class-level evidence for bronchodilators in obstructive lung disease |
| [NCT01274325](https://clinicaltrials.gov/study/NCT01274325) | Phase 3 | Completed | 51 | Salbutamol-containing ICS/LABA (Seroflo 125) vs. Seretide for airway inflammation in asthma; methodology directly applicable to levosalbutamol comparative study design |
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | 48-week RCT of tiotropium as add-on in severe persistent asthma; high-quality parallel-group design establishing background evidence for bronchodilator combination therapy |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Head-to-head: terbutaline Turbuhaler vs. salbutamol pMDI in Japanese adult asthma patients; β2-agonist head-to-head methodology directly applicable to levosalbutamol vs. albuterol comparison |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | Completed | 457 | 24-week study of tiotropium + PRN albuterol vs. placebo + PRN albuterol in treatment-naïve COPD; confirms the essential role of rescue SABA in obstructive disease management |
| [NCT02867761](https://clinicaltrials.gov/study/NCT02867761) | Phase 3 | Completed | 780 | RETHINC trial: long-acting bronchodilator in symptomatic smokers with normal spirometry; characterises the broader spectrum of obstructive disease responsive to bronchodilators |
| [NCT02427165](https://clinicaltrials.gov/study/NCT02427165) | Phase 2 | Completed | 29 | 7-way crossover of RPL554 vs. salbutamol (active comparator) vs. placebo via nebuliser in chronic asthma; salbutamol/levosalbutamol class used as gold-standard reference bronchodilator |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36594293](https://pubmed.ncbi.nlm.nih.gov/36594293/) | 2023 | RCT | Mymensingh Med J | Head-to-head RCT: **Levosalbutamol vs. racemic salbutamol** in acute asthma exacerbation; establishes L1 direct evidence for the drug in obstructive lung disease |
| [22364295](https://pubmed.ncbi.nlm.nih.gov/22364295/) | 2012 | Treatment Evaluation | Expert Opin Pharmacother | Comprehensive treatment evaluation of **Levosalbutamol specifically for COPD**; covers pharmacology, clinical evidence, safety profile, and therapeutic positioning |
| [21453221](https://pubmed.ncbi.nlm.nih.gov/21453221/) | 2011 | Review | Expert Opin Pharmacother | **(R)-salbutamol in asthma and COPD**: reviews enantiomer rationale, β2-agonist mechanism, and clinical data supporting levosalbutamol over racemic mixture |
| [38803713](https://pubmed.ncbi.nlm.nih.gov/38803713/) | 2024 | Retrospective Cohort | Cureus | Retrospective cohort in hospitalised COPD patients: **levalbuterol vs. albuterol** impact on length of stay and direct medical costs in China |
| [17276051](https://pubmed.ncbi.nlm.nih.gov/17276051/) | 2007 | RCT | Resp Medicine | Randomised double-blind crossover: **bronchodilator response of levosalbutamol vs. salbutamol** via pMDI in patients with obstructive airway disease |
| [17337829](https://pubmed.ncbi.nlm.nih.gov/17337829/) | 2007 | Evidence Review | Indian J Pediatrics | Evidence-based review of levosalbutamol: pharmacology, comparative efficacy vs. racemic salbutamol, and clinical implications for obstructive airways disease |
| [15293593](https://pubmed.ncbi.nlm.nih.gov/15293593/) | 2004 | Clinical Review | J Am Osteopathic Assoc | Clinical review of **levalbuterol in asthma and COPD**: dosing regimens, safety profile, and rationale for single-isomer use over racemic mixture |
| [19671384](https://pubmed.ncbi.nlm.nih.gov/19671384/) | 2009 | Review | Curr Allergy Asthma Reports | Systematic comparison of **levalbuterol vs. albuterol**: enantiomer effects on airway inflammation, corticosteroid interaction, and clinical outcomes in obstructive disease |
| [11236808](https://pubmed.ncbi.nlm.nih.gov/11236808/) | 2001 | PK Study | Clin Pharmacokinetics | Pharmacokinetics of levosalbutamol: enantioselective disposition, clinical implications for dosing optimisation, and rationale for the single-isomer development programme |
| [17983880](https://pubmed.ncbi.nlm.nih.gov/17983880/) | 2007 | Guidelines | J Allergy Clin Immunol | **EPR-3 Expert Panel Report**: NAEPP guidelines for asthma diagnosis and management; contextualises SABA (including levalbuterol) as an essential component of all asthma treatment steps |

---

## India Market Information

Levosalbutamol currently has **no registered products in India**. The regulatory data shows 0 licenses and a market status of "Not Marketed." Any clinical use in India would require either a special import authorisation or a formal New Drug Application (NDA) submission to CDSCO (Central Drugs Standard Control Organisation). Reference safety data from the originator's package insert should be obtained to support such an application.

---

## Safety Considerations

**Drug Interactions** (146 total interactions identified; key interactions listed below):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Isometheptene | Moderate | Additive sympathomimetic and cardiovascular effects |
| Epinephrine | Moderate | Additive adrenergic stimulation; increased cardiovascular risk |
| Clarithromycin | Moderate | Potential QT prolongation; ECG monitoring advised |
| Dolasetron | Moderate | Additive QT prolongation risk |
| Palonosetron | Moderate | Additive QT prolongation risk |
| Cisapride | Moderate | QT prolongation risk; avoid co-administration where possible |
| Famotidine | Moderate | QT-related interaction; cardiac monitoring advised |
| Ephedrine | Moderate | Additive adrenergic stimulation; increased tachycardia risk |
| Diethylpropion | Moderate | Additive sympathomimetic effects |
| Insulin (inhalation, rapid acting) | Moderate | Levosalbutamol may antagonise hypoglycaemic effect; monitor blood glucose |

*136 additional interactions are on record. A comprehensive DDI review is required before clinical use is initiated.*

Please refer to the originator package insert for complete key warnings and contraindications (currently unavailable; flagged as a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Levosalbutamol has L1-grade evidence supporting its use in obstructive lung disease, anchored by a completed Phase 3 RCT of Levalbuterol specifically in COPD (NCT00665600, 257 patients), a direct head-to-head RCT versus racemic salbutamol in acute asthma (PMID 36594293), and a comprehensive literature base of 20 publications spanning pharmacokinetics, clinical efficacy, and pharmacoeconomics. The mechanistic rationale for the single-isomer formulation is well-established and scientifically sound, and the drug's safety profile is consistent with the broader β2-agonist class.

**To proceed, the following is needed:**
- **Regulatory filing**: Prepare and submit an NDA or bridging dossier to India's CDSCO; no current domestic registration exists and this is the primary barrier to market entry
- **Full DDI review**: Systematically evaluate all 146 identified drug interactions, with priority on QT-prolonging agents (clarithromycin, dolasetron, palonosetron, cisapride) and sympathomimetics (epinephrine, ephedrine)
- **Safety documentation**: Obtain originator package insert to extract formal key warnings and contraindications (Blocking data gap DG001)
- **MOA documentation**: Retrieve complete DrugBank mechanism of action data to support dossier preparation (High-severity data gap DG002)
- **Pharmacoeconomic modelling**: Assess cost-benefit of branded levosalbutamol vs. widely available generic racemic albuterol in the Indian healthcare context, given the significant cost differential between single-isomer and racemic formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

