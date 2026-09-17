---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Anxiolytic/Sedative Use to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lorazepam is a benzodiazepine-class GABA-A receptor modulator with no India/Taiwan market registration and no confirmed original indication on file in this dataset. The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, with a very high similarity score (**99.87%**) but **zero supporting clinical trials and zero literature citations** — the model's own rationale flags this as a likely false-positive artifact of knowledge-graph embedding proximity rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no India/Taiwan license on file (drug is not marketed); general pharmacology suggests anxiolytic/sedative-hypnotic use, but this is not confirmed by the evidence pack |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lorazepam is flagged as a data gap in this dataset (DG002). Based on general pharmacological class knowledge, lorazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, enhancing inhibitory neurotransmission to produce sedative, anxiolytic, and anticonvulsant effects.

There is no known mechanistic pathway connecting GABA-A receptor modulation to the tumorigenesis or suppression pathways implicated in trigeminal nerve neoplasm (a nerve sheath tumor). No clinical trials, no published literature, and no mechanistic hypothesis in the evidence pack support a link between the two.

Given the complete absence of corroborating evidence despite the top-tier prediction score, this candidate is best interpreted as a **high-score false positive arising from knowledge-graph embedding similarity** rather than a biologically plausible repurposing signal. Notably, a lower-ranked prediction in the same evidence pack — **insomnia** (rank 2, score 99.80%) — has a coherent mechanistic rationale (GABA-A-mediated sedation, the well-established pharmacological basis for benzodiazepine hypnotic use) and is backed by 23 clinical trials and 18 publications, making it a substantially stronger candidate than the top-ranked prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: DrugBank/DDInter records 265 total interactions for lorazepam. Notable examples include:

| Interacting Drug | Severity |
|---|---|
| Morphine | Major |
| Morphine (liposomal) | Major |
| Bupropion | Moderate |
| Dronabinol | Moderate |
| Nabilone | Moderate |
| Metoclopramide | Moderate |
| Opium | Moderate |
| Sibutramine | Moderate |
| Teduglutide | Moderate |
| Aluminum hydroxide / Calcium carbonate / Magaldrate / Magnesium salts | Minor (absorption-related) |

Major interactions cluster around opioids and other CNS depressants, consistent with the known risk of additive sedation/respiratory depression for benzodiazepines. Detailed TFDA-style warnings and contraindications are not available in this dataset (DG001, Blocking) — please refer to the official package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Trigeminal Nerve Neoplasm) has no supporting clinical trials or literature, and the model's own rationale identifies it as a probable embedding-similarity artifact rather than a credible signal — this does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- TFDA/India-equivalent package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- If repurposing evaluation continues for lorazepam, redirect focus to **insomnia** (rank 2, evidence level L2, "Proceed with Guardrails"), which has a coherent mechanistic basis and substantial clinical trial/literature support, rather than the trigeminal nerve neoplasm candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

