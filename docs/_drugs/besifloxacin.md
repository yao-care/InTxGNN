---
layout: default
title: Besifloxacin
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Besifloxacin: predicted new indication Bronchitis (evidence level L5). Approved use: Conjunctivitis (including acute contagious conjunctivitis)"
monitor_inn: "Besifloxacin"
predicted_indications: ["bronchitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa"]
---

# Besifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Besifloxacin: From Conjunctivitis to Bronchitis

## One-Sentence Summary

Besifloxacin is a fluoroquinolone antibiotic, originally used as an ophthalmic treatment for bacterial conjunctivitis.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Conjunctivitis (including acute contagious conjunctivitis) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on known drug-class information, besifloxacin is a fluoroquinolone. This class inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy in bacterial conjunctivitis has been established.

Bacterial bronchitis is plausibly within the antibacterial spectrum of a fluoroquinolone, which is likely why the model scores it highly. However, besifloxacin is formulated only as an ophthalmic suspension with minimal systemic exposure, so there is no pharmacological basis for efficacy in the respiratory tract. The high score reflects a network-based association, not demonstrated activity.

Other predictions for this drug are similarly weak. The most mechanistically plausible alternative is **otitis externa** (score 99.03%), because topical fluoroquinolones such as ciprofloxacin and ofloxacin are established there. Even so, besifloxacin is not formulated or tested for ear use, and no trials or literature exist for it.

## Clinical Trial Evidence

Currently no related clinical trials are registered for bronchitis.

For context, one trial was linked to a different prediction ("post-bacterial disorder"). It is not evidence for bronchitis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | Systemic pharmacokinetics after single and multiple ocular instillations in subjects with suspected bacterial conjunctivitis; informs exposure and safety only, not efficacy |

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28740 | Besivance Opthalmic Suspension (Bausch & Lomb Inc) | Bottle of 5 ml ophthalmic suspension | Not stated in the compiled data |
| 29534 | Besibact Eye Drop (Micro Labs Ltd) | Packet of 5 ml eye drop | Not stated in the compiled data |
| 26310 | Besix Eye Drop (Ajanta Pharma Ltd) | Bottle of 5 ml ophthalmic suspension | Not stated in the compiled data |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph lists an association with superimposed infection (obsolete term).
- **Drug Interactions**: No interactions were found in the queried data.

For other safety information, please refer to the package insert. Because the topical ocular formulation gives negligible systemic exposure, any respiratory use would need its own safety assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a model score alone (L5), with no clinical or literature support. The only marketed formulation is ophthalmic, with minimal systemic exposure, so there is no pharmacological basis for respiratory efficacy.

**To proceed, the following is needed:**
- Mechanism of action data for besifloxacin
- Package insert warnings and contraindications
- A feasibility assessment of a formulation and route suitable for respiratory delivery
- Preclinical or clinical evidence of efficacy in bronchitis
- If a more plausible direction is wanted, a separate evaluation of otitis externa (formulation, middle-ear safety with tympanic membrane perforation, and efficacy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

