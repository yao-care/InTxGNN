---
layout: default
title: Roxithromycin
parent: Model Prediction Only (L5)
nav_order: 757
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Roxithromycin: predicted new indication Leprosy (evidence level L5). Approved use: Respiratory tract, urinary and soft tissue infections"
monitor_inn: "Roxithromycin"
predicted_indications: ["leprosy", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis", "pulmonary hypertension", "migraine disorder", "female breast carcinoma"]
---

# Roxithromycin
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

# Roxithromycin: From Bacterial Infections to Leprosy

## One-Sentence Summary

Roxithromycin is a macrolide antibiotic, used for respiratory tract, urinary and soft tissue infections.
The TxGNN model predicts it may be effective for **leprosy**,
but there are **no registered clinical trials** and only **5 publications** (mostly preclinical studies from 1988 to 1991, plus two reviews) behind this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Respiratory tract, urinary and soft tissue infections (from pharmacology reference data; no approved indication text is available in the Indian licence records) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L3 (generous; strictly between L3 and L4, as the evidence is mostly preclinical) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, roxithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. Its in vitro antibacterial activity is similar to that of erythromycin, mainly against Gram-positive bacteria and some Gram-negative bacteria such as *Legionella pneumophila*.

Leprosy is caused by *Mycobacterium leprae*, so an antibacterial drug with activity against this organism is a plausible fit. Preclinical studies support this. In a mouse footpad study, roxithromycin and clarithromycin were consistently active and bactericidal against *M. leprae*, while erythromycin and azithromycin were inactive. Clarithromycin was superior to roxithromycin. Other work describes anti-inflammatory and immunomodulatory effects of macrolides that may also matter in leprosy-related nerve inflammation.

Roxithromycin-specific data are limited, and clarithromycin is the better-characterised macrolide for leprosy. The other nine TxGNN predictions (for example hypertrichosis, Dandy-Walker syndrome, migraine) have no identifiable mechanistic link and are not supported by trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Review | Am J Clin Dermatol | Guide to selecting and using macrolides in skin infections; macrolides have established efficacy in many skin infections |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Review | Nihon Hansenbyo Gakkai Zasshi | Clarithromycin, roxithromycin, minocycline and fosfomycin show anti-inflammatory and immunomodulatory action alongside anti-*M. leprae* activity, relevant to leprous neuropathy |
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | Preclinical (mouse model) | Antimicrob Agents Chemother | Roxithromycin and clarithromycin were bactericidal against *M. leprae* in mouse footpads; clarithromycin was superior |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | Preclinical (in vitro/in vivo) | Antimicrob Agents Chemother | Compared newer macrolides against *M. leprae*; erythromycin was already known to be active in vitro |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | Preclinical (in vitro) | Antimicrob Agents Chemother | Over 25 antimicrobials evaluated for antileprosy potential in mouse macrophages |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 194696 | Roxmed 150mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 193707 | Retrox 150mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 235022 | Ventrox PD Tablet | Strip of 3 tablets | Not stated in the licence record |
| 189568 | Roxychem Suspension | Bottle of 30 ml oral suspension | Not stated in the licence record |
| 195042 | Roxitem 50mg Tablet DT | Strip of 10 dispersible tablets | Not stated in the licence record |

There are 20 valid single-ingredient registrations in total. Some are combinations of roxithromycin 150 mg with a 30 mg partner drug (for example Roxi A and Xerobect AX).

## Safety Considerations

- **Drug Interactions**: The pharmacology data list roxithromycin as a ligand of the motilin receptor (MLNR), consistent with the prokinetic activity of macrolides. No specific drug-drug interaction levels are available.
- **Combination with antibody-drug conjugates**: A 2023 in vitro study found macrolides and ketolides inhibited the cytotoxic effect of trastuzumab emtansine in HER2-positive breast cancer cells, suggesting a possible antagonistic interaction in cancer chemotherapy.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Leprosy is the only prediction with a plausible mechanism, and its support is limited to old preclinical studies (1988 to 1991) and two reviews. No clinical trials exist, and clarithromycin outperformed roxithromycin in the mouse model. The other nine predictions have no supporting evidence. The breast cancer link points to a possible antagonistic interaction rather than a benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory records
- Mechanism of action data
- Clinical data in leprosy, or a comparison against clarithromycin, which is better characterised
- Pharmacokinetic and tissue-penetration data relevant to *M. leprae* infection
- Evaluation of the interaction with trastuzumab emtansine if oncology use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

