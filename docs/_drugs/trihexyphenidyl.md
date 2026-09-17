---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 858
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Trihexyphenidyl is a classical anticholinergic agent, conventionally used for Parkinsonism and drug-induced extrapyramidal symptoms.
The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
but this is currently supported by **0 clinical trials** and only **1 indirectly relevant case series**, and the evidence pack itself flags the mechanistic direction as contradictory.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (Trihexyphenidyl is a classical anticholinergic, typically used for Parkinsonism / drug-induced extrapyramidal symptoms) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Trihexyphenidyl is a well-established antimuscarinic (anticholinergic) drug, and this class is known to reduce central cholinergic tone — a property useful for controlling tremor and dystonia in Parkinsonism, but generally considered to *impair* rather than improve attention and cognition.

For this specific candidate (ADHD), the only supporting literature is a single case series (PMID 21506147) describing tic disorder associated with dystonia — a topic only tangentially related to ADHD, with no direct evidence of Trihexyphenidyl's efficacy in ADHD. The evidence pack's own mechanistic assessment states that anticholinergic drugs may theoretically *worsen* cognitive function, which runs counter to the therapeutic goal in ADHD.

Given the absence of direct clinical or mechanistic support, and an explicit contradiction between the drug's known pharmacology and the target indication, this prediction should be treated as a low-confidence signal from the knowledge graph rather than a biologically grounded hypothesis. (Note: a separate, better-supported candidate in this evidence pack — PLA2G6-associated neurodegeneration, rank 5, evidence level L3 — is mechanistically consistent with Trihexyphenidyl's known use in dystonia-Parkinsonism syndromes, and may warrant separate evaluation.)

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case Series | Movement Disorders | Describes a clinical series of tic disorder associated with dystonia; relevance to ADHD is indirect, with no data on Trihexyphenidyl's efficacy in ADHD |

## Safety Considerations

**Drug Interactions**: A total of 107 documented interactions were identified. Notable examples include:
- **Major**: Potassium citrate, Potassium chloride (risk of additive GI effects potentially affecting absorption/dissolution)
- **Moderate**: Other anticholinergics (Hyoscyamine, Atropine, Glycopyrronium, Dicyclomine, Scopolamine, Trospium, Mepenzolate, Methscopolamine, Propantheline), opioids (Morphine, Loperamide), prokinetics (Metoclopramide, Prucalopride), Eluxadoline, Dronabinol, Nabilone, Pramlintide, and Magnesium hydroxide — generally reflecting additive anticholinergic burden or altered GI motility/absorption

No package insert warnings or contraindications data are currently available for this drug (data gap — blocking issue for full safety review).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence and only one indirectly relevant case series for the ADHD indication, and the proposed mechanism (anticholinergic action) runs counter to the therapeutic direction needed for ADHD. The drug is also not currently marketed in this jurisdiction (0 registrations), and core safety documentation (warnings/contraindications) is missing.

**To proceed, the following is needed:**
- Obtain TFDA/local package insert warnings and contraindications (Blocking gap — required before any S1 safety evaluation)
- Obtain confirmed mechanism of action data via DrugBank API (High-priority gap)
- Direct pharmacological or clinical evidence linking anticholinergic activity to ADHD symptom improvement, given the currently contradictory mechanistic rationale
- If pursuing repurposing work on this drug, consider prioritizing the PLA2G6-associated neurodegeneration candidate instead, which has stronger mechanistic consistency (L3 evidence, Proceed with Guardrails)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

