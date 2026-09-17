---
layout: default
title: Piracetam
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
---

# Piracetam
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

# Piracetam: From Myoclonus to Osteoarthritis

## One-Sentence Summary

Piracetam is a cyclic GABA derivative (nootropic) that is approved in the UK for myoclonus (in combination with other anti-myoclonic therapies) and used in several European, Asian, and South American countries for cognitive/circulatory indications, but it is **not marketed in Taiwan** and not FDA-approved. The TxGNN model predicts it may be effective for **Osteoarthritis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-embedding signal with no external validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Taiwan (0 licenses); internationally approved for myoclonus (UK), per DrugBank pharmacology record |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L5 (model prediction only) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Piracetam's `original_moa` field is a formal data gap, but the DrugBank pharmacology record captures its known target profile: it binds the AMPA-type ionotropic glutamate receptor subunits **GluA1–GluA4** (genes GRIA1–GRIA4), consistent with its established nootropic/anti-myoclonic effects. Its clinically documented actions center on neuronal membrane fluidity, red blood cell deformability, and microcirculation — it is used for myoclonus and, in some jurisdictions, for cognitive and vascular indications.

Osteoarthritis, by contrast, is driven by cartilage degradation, chondrocyte senescence, and local joint inflammation — pathways with no established connection to glutamate-receptor modulation or hemorheology. The model's own rationale is explicit on this point: **"no known mechanistic overlap between piracetam's known pharmacology and osteoarthritis cartilage degeneration or joint inflammation pathways."**

In short, this is a case where the TxGNN embedding score is high (98.45%, rank 21,123) but is not corroborated by any independent mechanistic, preclinical, or clinical signal. The prediction should be read as a hypothesis-generating signal only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Piracetam is **not marketed in Taiwan** — `total_licenses` = 0, no product registrations on file. No dosage forms or approved indications are available for the local market.

---

## Safety Considerations

TFDA-specific warnings and contraindications are not currently available (blocking data gap — see Conclusion below). No package-insert-level DDI list was returned; the pharmacology data on file describes piracetam's AMPA-receptor target-binding profile (GluA1–GluA4) rather than drug-drug interactions, so it is reported under mechanism above instead of as a safety warning.

> Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at decision stage S0 with Evidence Level L5 — a TxGNN score alone, with zero supporting clinical trials or literature, and an explicit mechanistic mismatch between piracetam's known glutamatergic/hemorheological activity and osteoarthritis pathophysiology. There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently a **blocking** data gap (DG001) that prevents entry into the S1 safety pre-screen
- Confirmed mechanism-of-action documentation beyond the raw pharmacology target list (DG002)
- Preclinical or observational evidence directly linking piracetam to cartilage/joint inflammation pathways before any clinical exploration is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

