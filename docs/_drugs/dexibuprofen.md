---
layout: default
title: Dexibuprofen
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexibuprofen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Dexibuprofen
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

# Dexibuprofen: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Dexibuprofen (the S-enantiomer of ibuprofen) is an NSAID originally used for inflammatory and degenerative joint conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model's top-ranked prediction is **brachydactyly-syndactyly syndrome**, but **no clinical trials and no publications** support it. The only prediction with any literature is **ankylosing spondylitis** (rank 9), which is backed by **3 general review articles** and no disease-specific trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (other graph-listed indications include osteoarthritis, juvenile idiopathic arthritis and spondyloarthropathy; the registration records contain no approved indication text) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome (top-ranked) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexibuprofen is an NSAID and the active S-enantiomer of ibuprofen. It inhibits cyclooxygenase (COX) and so reduces prostaglandin-mediated inflammation and pain. Its use in inflammatory and degenerative joint disease is established.

For the top-ranked prediction, the mechanistic link is weak. Brachydactyly-syndactyly syndrome is a congenital skeletal malformation, and COX inhibition has no recognised way of altering such a developmental defect. The high score most likely reflects network proximity to musculoskeletal terms in the knowledge graph rather than a true mechanism. The same applies to most of the other top-ten predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, Hunter-Thompson acromesomelic dysplasia, brachyolmia and its amelogenesis imperfecta variant, pseudoachondroplasia, and WHIM syndrome). At most, NSAIDs might give symptomatic pain relief in some of them, with no evidence of disease modification.

Two predictions are more plausible:
- **Ankylosing spondylitis (rank 9, score 99.70%):** NSAIDs are first-line therapy, and dexibuprofen is already linked to spondyloarthropathy. The available evidence is indirect, and the class effect is better supported by other NSAIDs.
- **Spondyloarthropathy, susceptibility to (rank 8, score 99.73%):** this is closely related to an existing indication and is a susceptibility-locus entry rather than a treatable clinical indication, so it may be redundant.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction. The table below covers the most relevant prediction with literature, ankylosing spondylitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Review | Clinical Rheumatology | Overview of dexibuprofen clinical data: 8 GCP trials with 1,463 patients (dose finding, pharmacokinetics, tolerability, compliance), including double-blind comparisons against placebo, racemic ibuprofen and diclofenac |
| [9013382](https://pubmed.ncbi.nlm.nih.gov/9013382/) | 1996 | Review | Journal of Clinical Pharmacology | Reanalysis of double-blind randomized studies of dexibuprofen in lumbar syndrome, rheumatoid arthritis, ankle distortion, gonarthrosis, ankylosing spondylitis and activated coxarthrosis |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Critical Reviews in Therapeutic Drug Carrier Systems | Microencapsulation as a drug-delivery approach for NSAIDs in arthritis, including ankylosing spondylitis; not specific to dexibuprofen |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 63789 | Debura 300 mg/500 mg Tablet | Strip of 10 tablets | Not stated in registration record |
| 155424 | Nuprin 200 Tablet | Strip of 10 tablets | Not stated in registration record |
| 153219 | Nuprin 300mg Tablet | Strip of 10 tablets | Not stated in registration record |
| 109579 | Ibusoft 400mg Tablet | Strip of 10 tablets | Not stated in registration record |
| 153180 | Nuprin Plus Tablet | Strip of 10 tablets | Not stated in registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a graph-based score alone, with no trials or publications and no plausible COX-related mechanism (evidence level L5). Ankylosing spondylitis is the only biologically plausible lead (L4), but its evidence is indirect, so it is better treated as a research question than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products, which are required before any safety screening
- Detailed mechanism of action data
- For ankylosing spondylitis: disease-specific clinical data for dexibuprofen, and a comparison with established NSAIDs
- For spondyloarthropathy susceptibility: confirmation that it is not redundant with the existing spondyloarthropathy indication
- For the rare genetic syndromes: a mechanistic rationale before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

