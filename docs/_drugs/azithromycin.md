---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azithromycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Streptococcal infection, bacterial pneumonia…"
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Azithromycin is a macrolide antibiotic originally used for bacterial infections such as streptococcal and staphylococcal infections, bacterial pneumonia, and conjunctivitis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, staphylococcal infection, conjunctivitis, and others (the approved indication text on the India licences is blank) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azithromycin is a macrolide antibiotic, its efficacy in bacterial infections is established, and its antibacterial action does not plausibly address the predicted condition.

Polyclonal hyperviscosity syndrome is caused by excess circulating immunoglobulins. Nothing in the data compiled for this report links azithromycin to this mechanism. The high score (0.998) is a graph-based prediction only, and the evidence supporting it is at the model-prediction level, so it should be treated as a hypothesis rather than a finding.

The other top-ranked predictions are also weakly supported:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hyperamylasemia | 99.81% | L5 | A laboratory finding with heterogeneous causes; no supporting data |
| 3 | Congenital analbuminemia | 99.79% | L5 | Rare genetic disorder; likely a graph artifact |
| 4 | Punctate epithelial keratoconjunctivitis | 99.78% | L4 | Weak indirect rationale; the only paper is an unrelated microsporidial case report |
| 7 | Monoclonal gammopathy | 99.61% | L4 | In vitro myeloma data suggest macrolides block autophagy; no efficacy data |
| 9 | Septicemic plague | 99.52% | L4 | In vitro study showed poor azithromycin activity against *Yersinia pestis* |
| 10 | Congenital hematological disorder (sickle cell disease) | 99.40% | L4 | Both sickle-cell trials were withdrawn with no enrollment |

Of these, the sickle cell disease direction (anti-inflammatory effects to reduce acute chest syndrome) and the myeloma/plasma cell direction have the most plausible hypotheses, but neither has clinical data yet.

## Clinical Trial Evidence

Currently no related clinical trials are registered for polyclonal hyperviscosity syndrome.

For reference, the lower-ranked prediction of congenital hematological disorder (sickle cell disease) has these trials:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adults with sickle cell disease; no data generated |
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Azithromycin prophylaxis for acute chest syndrome in sickle cell disease; no data generated |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | General pharmacokinetics and safety of understudied drugs in children; not specific to this indication |

## Literature Evidence

Currently no related literature is available for polyclonal hyperviscosity syndrome.

For reference, the strongest items under the other predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | Preclinical (in vitro) | Int J Oncol | Macrolides including azithromycin blocked autophagy flux and enhanced bortezomib cytotoxicity in myeloma cells |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro susceptibility | Antimicrob Agents Chemother | Azithromycin showed poor activity against 78 *Yersinia pestis* strains |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Preclinical (animal) | Antibiot Khimioter | Azithromycin was highly active in experimental brucellosis |
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Antibiotics for preventing lower respiratory tract infections in high-risk children; indirect relevance |

## India Market Information

Azithromycin is marketed in India with 20 valid single-ingredient registrations. The approved indication text is not recorded on these licences. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 16792 | Azimycin 500mg Tablet | Strip of 3 tablets | Not specified |
| 18709 | Azelac 250mg Tablet | Strip of 6 tablets | Not specified |
| 129612 | Loromycin 500mg Capsule | Strip of 3 capsules | Not specified |
| 148642 | Mythro 200mg Syrup | Bottle of 15 ml syrup | Not specified |
| 19154 | Azintra 100mg Tablet DT | Strip of 10 dispersible tablets | Not specified |

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis, neuromuscular junction disease, hearing disorder, and auditory system disease.
- **Drug Interactions**: 235 interactions were identified. The major-severity ones among those listed are:
  - Cisapride (Major)
  - Dolasetron (Major)
  
  Moderate interactions include famotidine, loperamide, clarithromycin, levofloxacin, granisetron, and aluminum and magnesium antacids, as well as several laxatives. Many of the QT-related interactions are consistent with the long QT contraindications above.

Package insert warnings were not available for this report, so please refer to the package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.81% TxGNN score for polyclonal hyperviscosity syndrome is a graph-based prediction only. There are no trials or publications, and azithromycin's antibacterial action does not plausibly address hyperviscosity caused by excess immunoglobulins. No prediction on the list currently reaches the level of evidence needed to advance. Sickle cell disease and plasma cell disorders are the only directions worth tracking as research questions.

**To proceed, the following is needed:**
- Mechanism of action data for azithromycin to allow a mechanistic-link analysis
- Package insert warnings and contraindications from the India regulator, which are currently missing and block safety screening
- Any experimental or clinical evidence for the predicted indication; otherwise, redirect effort to the sickle cell disease (anti-inflammatory) or plasma cell disorder hypotheses
- A QT-prolongation and drug-interaction risk assessment if any new indication moves forward
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

