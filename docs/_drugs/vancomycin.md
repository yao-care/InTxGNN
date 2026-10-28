---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis (also staphylococcal infections…"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic, originally used to treat Gram-positive bacterial infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model's top-ranked prediction is **diffuse scleroderma**, but there are **no clinical trials** and only **1 unrelated case report** behind it, so the prediction is essentially model-only and has no plausible biological support.
Among the ten predictions reviewed, only **streptococcal pneumonia** has a credible mechanistic rationale, and it is closer to an extension of existing antibacterial use than to true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridium difficile* colitis (also staphylococcal infections, endocarditis, bacterial arthritis, staphylococcal pneumonia) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, vancomycin binds the D-Ala-D-Ala termini of peptidoglycan precursors and so inhibits bacterial cell wall synthesis. This makes it active against Gram-positive bacteria but not against Gram-negative organisms, whose outer membrane it cannot cross.

For **diffuse scleroderma**, there is no plausible mechanistic link. It is an autoimmune fibrotic disease, and a cell wall synthesis inhibitor has no known action on it. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only retrieved paper is a case report on erythroderma with sepsis, which is not about scleroderma.

The other predictions follow a similar pattern:
- **Paratyphoid fever, salmonellosis and typhoid fever** are caused by Gram-negative *Salmonella*, which vancomycin cannot effectively penetrate. The retrieved literature consists of resistance surveys, veterinary papers, reviews and case reports, none showing vancomycin benefit.
- **Congenital analbuminemia, polyclonal hyperviscosity syndrome, hyperamylasemia, blood group incompatibility and premalignant hematological system disease** have no mechanistic rationale and no supporting trials or relevant literature.
- **Streptococcal pneumonia** is the exception. *Streptococcus pneumoniae* is Gram-positive, and vancomycin is used clinically for penicillin-resistant pneumococcal infection. Staphylococcal pneumonia is already among its original indications. This is rated L4 and framed as a research question, but the literature is mostly reviews and resistance surveillance rather than comparative efficacy data.

## Clinical Trial Evidence

Currently no related clinical trials registered for diffuse scleroderma, or for any of the other nine predicted indications.

## Literature Evidence

For diffuse scleroderma, the only publication retrieved is a case report that does not address the predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | Diffuse exfoliative rash with sepsis and eosinophilia in a 56-year-old man, evaluated as possible erythroderma; not about scleroderma |

For the most relevant alternative prediction, streptococcal pneumonia, the best-matched publications are reviews and surveillance studies:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16735146](https://pubmed.ncbi.nlm.nih.gov/16735146/) | 2006 | Review | The American Journal of Medicine | Rising antibiotic-resistant Gram-positive infections (MRSA, VRE) in hospitalised patients |
| [15360092](https://pubmed.ncbi.nlm.nih.gov/15360092/) | 2004 | Review | The American Journal of Medicine | Epidemiology and resistance patterns of *S. pneumoniae* |
| [36028454](https://pubmed.ncbi.nlm.nih.gov/36028454/) | 2022 | Cohort | Indian Journal of Medical Microbiology | Antibiotic resistance rates and penicillin MIC distribution in streptococcal pneumonia, 2013–2019 |
| [10501315](https://pubmed.ncbi.nlm.nih.gov/10501315/) | 1999 | Review | Seminars in Respiratory Infections | Treatment of pneumococcal pneumonia in the setting of emerging resistance |
| [16341681](https://pubmed.ncbi.nlm.nih.gov/16341681/) | 2005 | Review | Eur J Clin Microbiol Infect Dis | Antibiotic management of ventilator-associated pneumonia caused by resistant Gram-positive bacteria |

## India Market Information

Twenty single-ingredient injectable licences are valid in India, with none cancelled. The data compiled for this report does not include approved indication text for any of them. Five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 235916 | Vancoled 1gm Injection (Pfizer Ltd) | Vial of 1 injection | Not available |
| 236610 | Vancoled 500mg Injection (Pfizer Ltd) | Vial of 1 injection | Not available |
| 235341 | Vancocin 500mg Injection (Eli Lilly and Company India Pvt Ltd) | Vial of 1 injection | Not available |
| 234558 | Vancocin CP 500mg Injection (AstraZeneca) | Vial of 10 ml injection | Not available |
| 240618 | Vancomate 500mg Injection (Baxter India Pvt Ltd) | Vial of 1 injection | Not available |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder, and auditory system disease.
- **Drug Interactions**: 454 interactions are recorded. Major-level interactions include human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, and live cholera vaccine (*Vibrio cholerae* CVD 103-HgR strain). Moderate-level interactions include nephrotoxic or ototoxic agents (amphotericin B, amikacin, capreomycin, carboplatin, bacitracin), NSAIDs (ketorolac, ibuprofen, diclofenac, celecoxib), and others (metformin, estradiol, ethinylestradiol, mesalazine, balsalazide, ibandronate, cholestyramine).

Package insert warnings and contraindications were not available and should be reviewed separately.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, diffuse scleroderma, has no clinical trials, no relevant literature, and no plausible mechanism. Its high score appears to be a TxGNN model (deep learning) artefact. The Gram-negative infections (typhoid, paratyphoid, salmonellosis) are biologically contradicted by vancomycin's spectrum. Only streptococcal pneumonia is plausible, and it is an extension of existing antibacterial use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India label (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For streptococcal pneumonia, comparative efficacy data and registered trials, if it is pursued as a research question
- No further work is justified for diffuse scleroderma without new biological evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

