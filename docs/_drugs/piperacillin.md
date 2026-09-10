---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 668
evidence_level: L5
indication_count: 9
---

# Piperacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a broad-spectrum ureidopenicillin antibiotic used to treat susceptible bacterial infections; it is not currently marketed in Taiwan. The TxGNN model predicts a possible new indication in **Rheumatoid Arthritis** with a very high prediction score (**99.94%**), but this signal is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the score as a likely knowledge-graph artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Piperacillin has no approved license record in Taiwan; pharmacologically it is a broad-spectrum antibiotic for susceptible bacterial infections |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.94% (global rank 1502) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) field is not available for this drug. Based on known pharmacology, Piperacillin is a ureidopenicillin-class broad-spectrum antibiotic that irreversibly binds penicillin-binding proteins (PBPs) to inhibit bacterial cell wall synthesis. This mechanism acts on bacterial cell-wall biosynthesis and has no established connection to the autoimmune, joint-driven inflammatory pathophysiology of rheumatoid arthritis (RA).

The evidence pack's own mechanistic assessment agrees: no known anti-inflammatory or immunomodulatory activity has been described for piperacillin that would explain a therapeutic effect in RA. The very high TxGNN score (99.94%) most plausibly reflects a structural/topological artifact in the knowledge-graph embedding space — for example, piperacillin's dense connectivity to 81 other drugs through documented drug-drug interactions — rather than a genuine pharmacological signal.

This pattern is consistent across the broader candidate list in this evidence pack: of the 9 TxGNN-ranked indications reviewed, most are rare genetic/developmental syndromes with no plausible mechanistic link to an antibacterial agent, and the two candidates with any literature hits (diabetic nephropathy, WHIM syndrome) reflect piperacillin's supportive role in treating secondary bacterial infections in those patient populations — not disease-modifying activity against the underlying conditions themselves. None of the 9 candidates have direct clinical trial or literature support for the predicted indication itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Piperacillin currently has no market authorization records in Taiwan (0 registrations; market status: 未上市).

---

## Safety Considerations

**Drug Interactions**: 81 interactions on file (source: DDInter). Notable entries include:
- **Major**: Vancomycin
- **Moderate**: Doxycycline, Tetracycline, Picosulfuric acid, Minocycline, Kanamycin, Streptomycin
- **Minor**: Clarithromycin
- **Severity not classified in source**: Pantoprazole, Morphine, Sucralfate, Prednisone, Simvastatin, Nystatin, Potassium chloride, Prednisolone, Ranitidine, Rabeprazole, Omeprazole, Lansoprazole (61 additional interactions not listed here)

Key warnings and contraindications are not available in this evidence pack — please refer to the TFDA package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Rheumatoid Arthritis signal has no mechanistic basis, zero clinical trial evidence, and zero literature support (L5 — model prediction only), and the evidence pack itself assesses the score as likely reflecting knowledge-graph topology bias rather than true biology. Piperacillin is also not currently marketed in Taiwan, so there is no existing regulatory foothold to build on.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Structured MOA/pharmacology confirmation from DrugBank — currently a High-severity data gap (DG002)
- Independent mechanistic or preclinical evidence for any immunomodulatory activity of piperacillin before this candidate can advance past S0
- If this candidate is pursued further, re-review the remaining 8 predicted indications in this pack together, as none currently clear L4/L3 evidence thresholds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

