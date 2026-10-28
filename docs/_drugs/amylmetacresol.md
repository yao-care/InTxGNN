---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amylmetacresol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data (marketed as throat/cough lozenge…"
monitor_inn: "Amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Amylmetacresol: From Throat Lozenge Antiseptic to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Amylmetacresol is a local antiseptic used in throat lozenges, marketed in India in several cough and sore-throat lozenge products.
The TxGNN model predicts it may be relevant for **cauda equina syndrome**, but this is a purely computational prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (marketed as throat/cough lozenges) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 6 of 6) |
| Number of Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amylmetacresol is a single-ingredient topical antiseptic used in oropharyngeal lozenges, with minimal systemic exposure expected from lozenge use.

The predicted indication, cauda equina syndrome, is a compressive neurological emergency that requires surgical decompression. There is no plausible pharmacological route from a local throat antiseptic to this condition. The high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions are also unsupported. They include an obsolete neurogenic bladder entry (likely a TxGNN model (deep learning) artifact), irritable bowel syndrome, and several eye conditions (uveitis, panuveitis, iris and ciliary body diseases and neoplasms). None has clinical, literature, or mechanistic backing. The only weak, speculative link is infectious anterior uveitis, based on the drug's in-vitro antibacterial and antiviral activity in the throat. There is no evidence of intraocular penetration or ocular safety.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 219813 | Tusq-D Lozenges Ginger | Strip of 6 lozenges | Not stated |
| 248366 | Zedex Lozenges | Strip of 10 lozenges | Not stated |
| 215973 | Tusq-D Cough Lozenges Honey Lemon | Strip of 6 lozenges | Not stated |
| 37682 | Cof Q Lozenges | Strip of 6 lozenges | Not stated |
| 214969 | Tusq-D Cough Lozenges Sugar Free | Strip of 6 lozenges | Not stated |

One further registration (214990, Tusq-D Cough Lozenges Orange) is also valid. All 6 registrations are single-ingredient products with valid status.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found, and no contraindication edges were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. No clinical trials, publications, or plausible mechanism support using a local throat antiseptic for cauda equina syndrome. The same holds for the other nine predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's product information (currently blocking for safety screening)
- Mechanism of action data for amylmetacresol
- A credible biological rationale linking the drug to the predicted condition, plus evidence that the drug can reach the target tissue (the current lozenge route is local and oropharyngeal)
- Any preclinical or clinical evidence for the predicted indication, or review of whether a different candidate indication is more plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

