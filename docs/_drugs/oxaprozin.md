---
layout: default
title: Oxaprozin
parent: Model Prediction Only (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
---

# Oxaprozin
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

# Oxaprozin: From NSAID Use in Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Oxaprozin is a propionic-acid NSAID historically used for osteoarthritis and rheumatoid arthritis (local approved-indication text and detailed MOA are not available in this evidence pack). The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal disorder, but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely false positive from knowledge-graph node proximity rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis / Rheumatoid Arthritis (NSAID class; local approved-indication text not available in this evidence pack) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Oxaprozin is a propionic acid derivative NSAID that non-selectively inhibits COX-1/COX-2, with proven efficacy in inflammatory and degenerative joint conditions such as osteoarthritis and rheumatoid arthritis.

The top-ranked candidate, Acromesomelic Dysplasia (Hunter-Thompson type), is a rare autosomal recessive skeletal dysplasia caused by GDF5 gene defects, with pathology rooted in abnormal cartilage/bone morphogenesis rather than inflammation. There is no established or plausible pharmacological pathway connecting COX inhibition to this condition, and the evidence pack's own annotation explicitly characterizes the score as likely arising from knowledge-graph node proximity rather than a real biological relationship.

Among the remaining top-10 candidates, three (spondyloarthropathy susceptibility, rheumatoid nodulosis, and RF-positive polyarticular juvenile idiopathic arthritis) fall within the rheumatologic/inflammatory disease space where NSAID class-level mechanistic rationale is genuinely applicable — these were scored at L4/S1 ("Research Question") rather than L5/S0 ("Hold"), and may warrant further scoping ahead of the current top-ranked candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No registration records are currently available for Oxaprozin in this jurisdiction (market status: Not Marketed; 0 licenses on file).

---

## Safety Considerations

Key warnings and contraindications are not available in this evidence pack (a Blocking data gap — TFDA label warnings/contraindications, DG001 — prevents full safety review).

**Drug Interactions** (190 total interactions on file; 20 detailed below):

| Interacting Drug | Level |
|---|---|
| Hydrocortisone | Moderate |
| Metformin | Moderate |
| Mesalazine | Moderate |
| Triamcinolone | Moderate |
| Acetylsalicylic acid | Moderate |
| Balsalazide | Moderate |
| Dexamethasone | Moderate |
| Betamethasone | Moderate |
| Budesonide | Moderate |
| Chlorpropamide | Moderate |
| Potassium citrate | Moderate |
| Picosulfuric acid | Moderate |
| Polyethylene glycol (3350 with electrolytes) | Moderate |
| Acetohexamide | Moderate |
| Dexfenfluramine | Moderate |
| Exenatide | Moderate |
| Fenfluramine | Moderate |
| Famotidine | Minor |
| Ranitidine | Minor |
| Cimetidine | Minor |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acromesomelic Dysplasia, Hunter-Thompson Type) has no clinical trial or literature support, no plausible mechanistic link, and is explicitly annotated in the source data as a probable knowledge-graph artifact rather than a genuine repurposing signal. The drug is also not currently marketed in this jurisdiction, and a Blocking safety data gap (local label warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data from DrugBank (High priority gap, DG002)
- If pursuing repurposing further, re-scope toward the L4/S1 "Research Question" candidates (spondyloarthropathy susceptibility, rheumatoid nodulosis, RF-positive polyarticular JIA), which have stronger class-level mechanistic plausibility than the current top-ranked candidate, and seek supporting trial/literature evidence for those instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

