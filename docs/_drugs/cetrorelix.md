---
layout: default
title: Cetrorelix
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Cetrorelix
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

# Cetrorelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Cetrorelix is a GnRH receptor antagonist used to prevent premature LH surges in women undergoing controlled ovarian stimulation as part of fertility treatment.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhibition of premature LH surges in women undergoing controlled ovarian stimulation (fertility treatment). The India licence records contain no indication text, so this comes from the pharmacology data compiled for this report. |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the pharmacology information, cetrorelix is a peptide antagonist of the GnRH1 receptor (GNRHR). It suppresses LH and FSH, and therefore downstream sex steroids, without the initial flare seen with GnRH agonists.

The link to hypertrichosis is weak. Hypertrichosis is not primarily driven by gonadotropins. Androgen suppression might matter only in a hormone-dependent subset of patients. The very high TxGNN score is a graph-based prediction, and no clinical or literature evidence supports it.

The other top-ranked predictions are mostly congenital or structural conditions (for example Ambras syndrome, Dandy-Walker malformation, hair shaft abnormalities) with no plausible GnRH-axis mechanism. They look like network artifacts from shared phenotype nodes. The most biologically credible candidate in the list is **central precocious puberty**, because it is driven by early activation of the GnRH axis. However, standard care is GnRH agonist therapy, short-acting cetrorelix is not well suited to chronic paediatric use, and no direct evidence is available. Familial male-limited precocious puberty is flagged as a research question only, since its driver (activating LHCGR mutations) acts downstream of GnRH and LH.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 236604 | Vestova 0.25mg Injection (Alkem Laboratories) | Vial of 2 ml injection | Not stated in the licence record |
| 35079 | Cetrolix 0.25mg Injection (Intas Pharmaceuticals) | Vial of 1 injection | Not stated in the licence record |
| 163165 | Ovucet 0.25mg Injection (Zydus Cadila) | Vial of 1 injection | Not stated in the licence record |
| 96301 | Gonapress 0.25mg Injection (Ferring Pharmaceuticals) | Vial of 1 injection | Not stated in the licence record |
| 34799 | Cetrotide 0.25mg Injection (Merck Ltd) | Vial of 1 injection | Not stated in the licence record |

All 16 registrations are valid single-ingredient injectable products; the five above are shown as representative examples.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypertrichosis rests only on a graph-based model score. There are no trials or publications, and the mechanistic link is weak. Cetrorelix is well established and widely marketed in India for fertility treatment, but that does not support the predicted new use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, since safety data are currently missing
- Detailed mechanism of action data
- Any clinical or literature evidence for hypertrichosis, ideally in a hormone-dependent subset
- If a different direction is pursued, a focused review of central precocious puberty, covering short-acting formulation suitability, paediatric safety and comparison with GnRH agonists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

