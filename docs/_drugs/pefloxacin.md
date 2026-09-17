---
layout: default
title: Pefloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 644
evidence_level: L3
indication_count: 10
---

# Pefloxacin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Pefloxacin: From Bacterial Infections to Heart Valve Disease

> **Note on candidate selection:** The TxGNN pack ranks 10 cardiac-disease candidates for Pefloxacin. The #1-ranked candidate ("heart conduction disease," score 99.90%) has **zero** supporting trials or literature, and the pack's own rationale flags it as likely confounded with Pefloxacin's known QT-prolongation/hERG-blockade risk — a documented adverse effect, not a treatment signal. This report instead features **rank 3 (heart valve disease)**, the only candidate with any directionally consistent supporting evidence (preclinical), and treats rank 1 as a safety caution rather than a lead worth pursuing.

## One-Sentence Summary

Pefloxacin is a fluoroquinolone-class antibacterial agent (original indication and MOA not documented in this evidence pack — both flagged as data gaps). Among 10 TxGNN-predicted cardiac indications, **Heart Valve Disease** (score 99.89%) is the only one with any supporting evidence — a single 2000 animal-model study on fluoroquinolone efficacy in experimental endocarditis — while the top-scored candidate ("heart conduction disease") is unsupported and likely reflects a known cardiotoxicity signal rather than a genuine therapeutic lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in source data; Pefloxacin is a fluoroquinolone-class antibacterial used for bacterial infections |
| Predicted New Indication | Heart Valve Disease (evidence points specifically to infective endocarditis) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Pefloxacin is not available in this evidence pack (DG002). Based on known pharmacology, Pefloxacin is a second-generation fluoroquinolone that acts via inhibition of bacterial DNA gyrase and topoisomerase IV — a mechanism with no established direct relevance to cardiac valve pathology.

The link to "heart valve disease" is indirect but coherent: the only supporting document (PMID 10671762) evaluated Pefloxacin, alongside other fluoroquinolones, in a rabbit model of **left-sided Pseudomonas aeruginosa endocarditis** — i.e., an infection of the heart valve. Antibacterial treatment of infective endocarditis is an established, mechanistically consistent use case for a bactericidal antibiotic; the model appears to be capturing this real (if narrow) association. However, "heart valve disease" as a KG term covers far more than infective endocarditis (e.g., degenerative or congenital valve disease), and no clinical (human) data exist to confirm Pefloxacin's role even within endocarditis specifically.

By contrast, the top-ranked candidate, "heart conduction disease," has no mechanistic rationale, no trials, and no literature — and fluoroquinolones are independently known to block hERG potassium channels, causing QT prolongation and arrhythmia. This is a well-documented **adverse effect**, not a treatment mechanism, so the model's top-ranked signal most likely reflects safety/adverse-event associations embedded in the knowledge graph rather than a therapeutic relationship. It should not be pursued as an indication and is flagged here as a caution rather than a candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04496986](https://clinicaltrials.gov/study/NCT04496986) | N/A | Withdrawn | 0 | Studies post-cardiac-surgery dysphagia mechanisms; unrelated to Pefloxacin or valve-disease treatment (relevance grade C, no enrollment) |
| [NCT05304416](https://clinicaltrials.gov/study/NCT05304416) | N/A | Active, not recruiting | 347 | Studies risk factors/clinical markers of post-cardiac-surgery dysphagia; unrelated to Pefloxacin or valve-disease treatment (relevance grade C) |

Neither trial actually tests Pefloxacin or valve disease treatment — both were retrieved as keyword matches ("heart valve" surgery context) and provide no supporting evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10671762](https://pubmed.ncbi.nlm.nih.gov/10671762/) | 2000 | Preclinical (animal model) | Chemotherapy | In a rabbit model of induced left-sided *Pseudomonas aeruginosa* endocarditis, Pefloxacin (with amikacin, ofloxacin, ciprofloxacin, enoxacin, fleroxacin) given IM as monotherapy for 5 days achieved high survival with no sterile vegetations reported for most agents — the only direction-consistent evidence for this candidate, but animal-only, no human data. |

## India Market Information

Pefloxacin is currently **not marketed** in India — 0 registrations on file, no license records available in the source data.

## Safety Considerations

Please refer to the package insert for safety information. *(Note: TFDA/India label warnings and contraindications are a documented blocking data gap — see Conclusion below. Independently, fluoroquinolones as a class carry known risks of QT prolongation, tendinopathy/tendon rupture, and aortic aneurysm/dissection, which are directly relevant to interpreting several of the other cardiac-disease candidates in this pack as safety signals rather than efficacy signals.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate with any supporting evidence (heart valve disease, via a single 2000 animal endocarditis model) provides no human clinical data, and Pefloxacin is not currently marketed in India. Combined with a blocking gap in label safety data and no verified MOA, the evidence base is insufficient to proceed. The higher-scored "heart conduction disease" candidate should be actively deprioritized, as it likely reflects a known cardiotoxicity association rather than a genuine repurposing opportunity; the remaining 8 candidates (ranks 2, 4–10) have no supporting evidence at all (L5, Hold).

**To proceed, the following is needed:**
- TFDA/India label warnings and contraindications (DG001, currently blocking S1 safety review)
- Verified mechanism of action from DrugBank (DG002)
- Human clinical evidence for Pefloxacin in infective endocarditis/valve disease — current evidence is a single animal study from 2000
- Explicit safety review confirming/ruling out QT-prolongation risk before any cardiac-indication work proceeds
- India market/regulatory pathway assessment, given the drug is not currently registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

