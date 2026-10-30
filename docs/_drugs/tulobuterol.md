---
layout: default
title: Tulobuterol
parent: Model Prediction Only (L5)
nav_order: 873
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Tulobuterol: predicted new indication Bronchitis (evidence level L4). Approved use: Asthma, intrinsic asthma, allergic asthma, pulmonary emphysema"
monitor_inn: "Tulobuterol"
predicted_indications: ["bronchitis", "obstructive lung disease", "respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
---

# Tulobuterol
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

## Tulobuterol: From Asthma to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Tulobuterol is a beta-2 adrenergic agonist bronchodilator, originally used to treat asthma and pulmonary emphysema.
The TxGNN model predicts it may be effective for **bronchitis** with a very high score, but so far only **2 publications** (one 1987 mucociliary clearance study and one 1985 review) bear on this indication, and **no clinical trials** are registered for it.
This is a computational prediction with limited direct clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, intrinsic asthma, allergic asthma, pulmonary emphysema |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tulobuterol is a beta-2 adrenergic agonist. It relaxes airway smooth muscle, and its efficacy in asthma and emphysema is established.

Bronchitis with airflow obstruction shares the same airway-narrowing problem. Bronchodilation could plausibly give symptomatic relief. A 1987 study also found that tulobuterol improved mucociliary clearance in patients with chronic obstructive bronchitis, which is a second plausible benefit.

This evidence is indirect. Neither available publication is a bronchitis-specific efficacy trial. The very high TxGNN score is a computational prediction and does not replace clinical evidence.

**Other predictions in the same analysis:**
- **Obstructive lung disease and chronic obstructive pulmonary disease (COPD):** these are close to the approved uses, so they are largely on-label or near-label rather than true repurposing. Evidence is stronger (L3), including Phase 4 trials and comparative studies (see below).
- **Respiratory malformation, Rienhoff syndrome, hyperlucent lung and tracheal stenosis:** no plausible mechanistic link or clinical evidence was found. Several involve fixed structural problems that bronchodilation is unlikely to change. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

No clinical trials are registered for bronchitis. Currently no related clinical trials registered for this indication.

For the closely related obstructive airway indications (rank 2 and rank 4 predictions):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01465906](https://clinicaltrials.gov/study/NCT01465906) | Phase 4 | Unknown | 160 | Tulobuterol patch plus tiotropium for relieving dyspnea in COPD; multicentre randomized trial. Results not verified |
| [NCT00950794](https://clinicaltrials.gov/study/NCT00950794) | Phase 4 | Completed | 367 | Salmeterol vs tulobuterol (Hokunalin) tape in adult asthma; tulobuterol is the comparator, not the focus |

## Literature Evidence

**Bronchitis:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2884705](https://pubmed.ncbi.nlm.nih.gov/2884705/) | 1987 | Mechanistic/physiological study | Respiration | In 8 patients with chronic obstructive bronchitis and 2 with asthma, tulobuterol and fenoterol significantly improved mucociliary clearance in a double-blind crossover design |
| [2861899](https://pubmed.ncbi.nlm.nih.gov/2861899/) | 1985 | Review | Clinical Therapeutics | Beta-2 agonists are useful in asthma; chronic bronchitis and emphysema respond less well, but a trial is warranted to look for a reversible component |

**Related obstructive airway disease (COPD and asthma):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2876775](https://pubmed.ncbi.nlm.nih.gov/2876775/) | 1986 | RCT | Clinical Therapeutics | Double-blind comparison of tulobuterol and salbutamol in 40 men with COPD |
| [1974678](https://pubmed.ncbi.nlm.nih.gov/1974678/) | 1990 | RCT | Lung | Tulobuterol aerosol vs fenoterol aerosol over two months in 36 adults; FEV1 increases were greater with tulobuterol |
| [22270072](https://pubmed.ncbi.nlm.nih.gov/22270072/) | 2012 | Review | Allergology International | Review of the tulobuterol transdermal patch as a long-acting beta-2 agonist |
| [41234762](https://pubmed.ncbi.nlm.nih.gov/41234762/) | 2025 | Phase 4 clinical study | Annals of Thoracic Medicine | Safety, tolerability and efficacy of the tulobuterol patch (Tuloplast) in asthma and COPD |
| [16336029](https://pubmed.ncbi.nlm.nih.gov/16336029/) | 2005 | Open-label study | Treatments in Respiratory Medicine | Transdermal tulobuterol compared with inhaled salmeterol in stable COPD |
| [22817699](https://pubmed.ncbi.nlm.nih.gov/22817699/) | 2013 | Comparative study | Geriatrics & Gerontology International | Better adherence to the tulobuterol patch than inhaled salmeterol in elderly COPD patients |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 219028 | Tulomax 2.0 Transdermal Patch | Packet of 1 patch | Not specified |
| 218159 | Tulomax 0.5 Transdermal Patch | Packet of 1 patch | Not specified |
| 216894 | Tuloplast 2 Transdermal Patch | Packet of 14 transdermal patches | Not specified |
| 218169 | Tulo-Touch 2mg Patch | Box of 14 patches | Not specified |
| 219840 | Tulo-Touch 0.5mg Patch | Box of 14 patches | Not specified |

There are 9 valid single-ingredient registrations in total, all transdermal patches, from Hetero Healthcare, Zuventus Healthcare and Sparsha Pharma International.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For bronchitis, the evidence is limited to a 1987 mucociliary clearance study and a 1985 review, with no registered clinical trials, so the prediction rests mainly on the model score. The related indications of obstructive lung disease and COPD have stronger support (L3) but are largely on-label.

**To proceed, the following is needed:**
- Bronchitis-specific clinical evidence, such as a controlled trial of the tulobuterol patch in chronic bronchitis with airflow obstruction
- Mechanism of action data
- Package insert warnings and contraindications from the Indian regulator, which are required before safety screening
- Approved indication wording for the Indian registrations, to confirm how the current labels relate to bronchitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

