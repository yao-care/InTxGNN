---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Acne, streptococcal and staphylococcal infections…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis"]
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic originally used for bacterial infections (streptococcal, staphylococcal and anaerobic infections), bacterial vaginosis and acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis (the India licence records contain no approved indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis. Its efficacy in Gram-positive and anaerobic bacterial infections is established, so any benefit would be limited to a bacterial component of an eye surface disease.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is often viral or inflammatory rather than bacterial, so an antibacterial mechanism is not established. The very high score (99.97%) is most likely a graph-proximity artefact of the knowledge graph rather than evidence of real efficacy.

Other predictions for this drug show the same pattern. Exposure keratitis has only indirect literature on bacterial keratitis. Epidemic keratoconjunctivitis is adenoviral, and clindamycin has no antiviral activity. Postmenopausal atrophic vaginitis is driven by oestrogen deficiency. "Non-human animal disease" is not a usable human indication. Neurotrophic keratopathy is not primarily bacterial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (punctate epithelial keratoconjunctivitis).

For the second-ranked prediction, exposure keratitis, only indirect papers were retrieved. None addresses exposure keratitis or clindamycin treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective cohort | PLoS One | Hospital review of *S. aureus* keratitis comparing MRSA and MSSA isolates (demographics, antibiotic susceptibility, outcomes) |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of ocular MRSA vs MSSA infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis and ulcer linked to a contaminated lens case |
| [42763505](https://pubmed.ncbi.nlm.nih.gov/42763505/) | 2026 | Case report | IDCases | Vision-threatening ocular toxoplasmosis involving the fovea, diagnosed by intraocular fluid mNGS (not relevant to clindamycin use here) |

## India Market Information

Twenty valid single-ingredient licences are registered. The licence records contain no approved indication text. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 58772 | Dalacin C 150mg Capsule (Pfizer Ltd) | Strip of 10 capsules | Not recorded |
| 63474 | Dalcap 150mg Capsule (Torrent Pharmaceuticals Ltd) | Strip of 4 capsules | Not recorded |
| 35710 | Clid 300mg Injection (Bennet Pharmaceuticals Limited) | Vial of 4 ml injection | Not recorded |
| 106481 | Humclid 600mg Injection (Medic Biologicals And Pharmaceuticals Pvt Ltd) | Vial of 4 ml injection | Not recorded |
| 141344 | Mazocan Suppository (Canvarzys Healthcare Ltd) | Packet of 3 suppositories | Not recorded |

Available routes include oral capsules and tablets, injectables and vaginal capsules or suppositories. No ophthalmic formulation appears among the registrations.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver failure, sunburn, Crohn disease, inflammatory bowel disease, Crohn's colitis, ulcerative colitis, atopic eczema/dermatitis, exfoliative dermatitis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, vulvovaginal candidiasis.
- **Drug Interactions**: 320 interactions are recorded. Moderate-level interactions include balsalazide, clarithromycin, picosulfuric acid, attapulgite and kaolin. Others are of unknown severity, including amphotericin B, aspirin, amoxicillin, bupropion, pantoprazole, metformin, omeprazole, sucralfate, vancomycin and morphine.

Package insert warnings and contraindications were not obtained. Please refer to the package insert for full safety information. Clindamycin is also a well-known risk factor for *C. difficile* infection.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature, and the proposed disease is often viral or inflammatory, so an antibacterial mechanism is not plausible. The knowledge graph also flags several gastrointestinal and dermatological contraindications, and there is no ophthalmic formulation registered in India.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Evidence that a bacterial component exists in punctate epithelial keratoconjunctivitis, or a re-ranking toward better-supported ocular bacterial indications (for example bacterial keratitis)
- Assessment of ocular route feasibility and formulation, since only oral, injectable and vaginal products are registered
- Exclusion of non-actionable terms ("non-human animal disease") and name-matching false positives (epidemic keratoconjunctivitis) from the candidate list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

