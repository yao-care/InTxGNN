---
layout: default
title: Prulifloxacin
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
---

# Prulifloxacin
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

# Prulifloxacin: From Bacterial Infections to Heart Disease

## One-Sentence Summary

Prulifloxacin is a fluoroquinolone prodrug antibiotic (active metabolite: ulifloxacin) that works by inhibiting bacterial DNA gyrase and topoisomerase IV. The TxGNN model's top prediction suggests possible relevance to **Heart Disease**, but this is currently supported by only **1 publication** — an animal cardiac-safety study, not an efficacy study — and **0 clinical trials**, indicating very weak evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (India licensing data absent); drug class is fluoroquinolone antibacterial |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured DrugBank field. Based on the available evidence, Prulifloxacin is a fluoroquinolone prodrug that is hydrolyzed to its active metabolite ulifloxacin, which inhibits bacterial DNA gyrase and topoisomerase IV — the standard fluoroquinolone antibacterial mechanism. This mechanism has no established pharmacological pathway connecting it to cardiovascular disease pathophysiology.

The single supporting publication (PMID 15018156) is an animal proarrhythmia model comparing prulifloxacin's active metabolite against other quinolones for QT-interval prolongation and arrhythmia risk — a **cardiac safety** study, not a treatment-efficacy study. It documents a known class-effect risk (quinolone-associated QT prolongation) rather than any therapeutic benefit in heart disease.

Notably, all 10 of this drug's top TxGNN predictions score within a narrow band (~0.9993–0.9994) and span pharmacologically unrelated conditions — structural heart defects, congenital craniofacial syndromes, chromosomal deletions, and a rare glycosylation disorder. This tight score clustering across mechanistically implausible diseases is a signature of knowledge-graph embedding artifacts rather than genuine differential signal, and should be treated as a strong caution flag rather than a positive finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15018156](https://pubmed.ncbi.nlm.nih.gov/15018156/) | 2004 | Animal safety/PK-PD study | The Journal of Toxicological Sciences | Compared prulifloxacin's active metabolite (ulifloxacin) with sparfloxacin, gatifloxacin, and levofloxacin in a rabbit proarrhythmia model, assessing QT-interval prolongation and arrhythmia risk — a cardiac **safety** comparison, not evidence of therapeutic benefit in heart disease |

---

## India Market Information

Currently no market registration information available (India market status: Not Marketed; 0 registrations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, no clinical or observational evidence), the drug's antibacterial mechanism has no known pathway relevant to heart disease, the one retrieved publication addresses cardiac safety risk rather than efficacy, and the drug is not currently marketed in India. The tight, mechanistically incoherent clustering of scores across this drug's top 10 predictions further suggests a knowledge-graph embedding artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank/primary literature
- India (or reference-market) label warnings and contraindications, particularly regarding QT prolongation
- A plausible mechanistic hypothesis linking fluoroquinolone activity to a specific cardiac disease subtype
- Prospective preclinical or observational data before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

