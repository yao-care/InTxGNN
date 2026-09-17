---
layout: default
title: Stavudine
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 3
---

# Stavudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Stavudine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Stavudine (d4T, DB00649) is a nucleoside reverse transcriptase inhibitor (NRTI) publicly known for HIV antiretroviral therapy, though this evidence pack contains no documented original indication or approved label text.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, not human, disease — supported only by **2 animal-model publications** and **no clinical trials**.
> Given the animal-disease target and absent safety/MOA data, current evidence does not support a human repurposing pathway for this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no India licenses on file); publicly known as an NRTI for HIV-1 infection |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 (preclinical/animal studies only) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on public knowledge, stavudine is a thymidine-analog NRTI that inhibits viral reverse transcriptase — a mechanism shared across lentiviruses, including HIV, FIV, and SIV.

The mechanistic rationale linking stavudine to FIV is therefore *class-level* plausible: both HIV and FIV are lentiviruses, and NRTIs as a class inhibit their reverse transcriptase. However, the two supporting publications (PMID 16570826, 12654652) actually studied **stampidine**, an aryl phosphoramidate prodrug derivative of d4T, not stavudine itself — making the mechanistic extension indirect even within the animal literature.

Critically, FIV is a **veterinary disease affecting domestic cats**, not a human condition. This prediction falls outside the scope of human drug repurposing decision-making, regardless of TxGNN's high confidence score. The same limitation applies to the second-ranked prediction (simian immunodeficiency virus infection), which is likewise a non-human primate model disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16570826](https://pubmed.ncbi.nlm.nih.gov/16570826/) | 2006 | Animal PK/Toxicity (dog/cat) | Arzneimittel-Forschung | Stampidine (a d4T prodrug derivative, not stavudine itself) achieved therapeutic plasma levels at 100 mg/kg oral dose in dogs and FIV-infected cats with an acceptable safety profile |
| [12654652](https://pubmed.ncbi.nlm.nih.gov/12654652/) | 2003 | Animal in vivo efficacy (FIV-infected cats) | Antimicrobial Agents and Chemotherapy | Single oral bolus of stampidine (50–100 mg/kg) produced a transient ≥1-log reduction in FIV load in 5/6 infected cats with no observed side effects |

*Note: Both studies evaluate stampidine, a chemically modified d4T prodrug — not stavudine (d4T) itself.*

---

## India Market Information

Stavudine has no registered licenses in the India regulatory dataset (market status: Not Marketed, 0 registrations). No product/dosage form information is available.

---

## Safety Considerations

**Drug Interactions**: DDI database returns 134 total interactions. Selected interactions rated Moderate severity include:
- Metronidazole
- Naltrexone
- Orlistat
- Rosuvastatin
- Simvastatin
- Tinidazole

An additional 14+ interactions (e.g., Metformin, Omeprazole, Proton pump inhibitors, Vancomycin, Sulfasalazine) are flagged in the database with severity level listed as Unknown and would require individual review.

No label-level key warnings or contraindications are currently on file for this drug (blocking data gap DG001); please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top two TxGNN predictions target veterinary/non-human primate diseases (FIV, SIV), which fall outside human drug repurposing scope despite high model confidence scores; the third prediction (a rare neurodevelopmental disorder) has zero supporting literature or trials (L5, pure model prediction). Combined with the absence of MOA and safety label data, this candidate does not meet the evidence bar to advance.

**To proceed, the following is needed:**
- Resolve blocking gap DG001: obtain official label/package insert warnings and contraindications
- Resolve high-priority gap DG002: confirm stavudine MOA via DrugBank API
- Re-run TxGNN prediction filtering to exclude non-human disease ontology terms (FIV, SIV) from repurposing candidate lists
- If pursuing further, prioritize identification of any human-relevant predicted indications not currently surfaced in this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

