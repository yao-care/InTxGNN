---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 706
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line antituberculosis agent, historically used as part of combination therapy for tuberculosis. The TxGNN model predicts it may be effective for **Infectious Otitis Media**, but this top-ranked prediction currently has **no supporting clinical trials or literature** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred from evidence-pack rationale text; formal license/indication data not provided — original_moa and original_indications fields are empty) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Pyrazinamide in this evidence pack. Based on information embedded in the evidence pack's own analysis of related predictions, Pyrazinamide is a first-line antituberculosis drug whose active metabolite, pyrazinoic acid, requires activation by a *Mycobacterium tuberculosis*-specific pyrazinamidase and acts within the acidic environment of macrophages/caseous necrosis to kill semi-dormant tubercle bacilli.

For the top-ranked prediction, **Infectious Otitis Media**, the evidence pack explicitly states there is no trial or literature support — the connection is purely a TxGNN score, with only a loose semantic proximity to other TB-related ear conditions. This is different from several lower-ranked predictions in the same evidence pack (e.g., middle ear disease, chronic otitis media, suppurative otitis media), which are supported by case reports and reviews describing **tuberculous otitis media** — a rare extrapulmonary manifestation of TB in which Pyrazinamide is used as part of the standard multi-drug anti-TB regimen, not as an independently validated treatment for otitis media itself.

In other words, the high TxGNN scores across this disease cluster likely reflect semantic clustering of "TB-related" disease terms in the knowledge graph rather than a genuinely new pharmacological mechanism specific to otologic disease. This should be treated as a research signal requiring independent validation rather than a mechanistically established repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Pyrazinamide is currently **not marketed** under this evidence pack's regulatory record (0 registrations, no license entries available). No product/dosage-form data can be reported.

---

## Safety Considerations

- **Drug Interactions**: 56 total interactions identified (source: DDInter). Two flagged at **Moderate** severity — Picosulfuric acid and Naltrexone. The remaining listed interactions (e.g., proton pump inhibitors, H2-antagonists, Vancomycin, Amphotericin B, corticosteroids, Metronidazole, Acetylsalicylic acid, Glyburide, Amoxicillin, Streptomycin) are recorded with **Unknown** severity classification in the source database and require individual clinical review.

Key warnings and contraindications are not available in this evidence pack — please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Infectious Otitis Media) has zero clinical trial or literature support and is explicitly flagged by the evidence pack as a prediction-score-only signal (L5). Related, better-evidenced candidates in the same cluster (L4, "Research Question" stage) only support Pyrazinamide's existing role within standard anti-TB combination therapy for extrapulmonary TB, not a novel independent indication.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to assess biological plausibility beyond TB-cluster semantics
- TFDA/regulatory package insert data for warnings and contraindications (currently a Blocking data gap per meta.data_gaps)
- Targeted literature or preclinical search specific to non-tuberculous infectious otitis media (to rule out the TB-semantic-clustering confound)
- Clarification of whether the TxGNN signal reflects a distinct pharmacological hypothesis or simply reproduces known extrapulmonary-TB treatment patterns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

