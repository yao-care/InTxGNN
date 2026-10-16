---
layout: default
title: Colistimethate
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Colistimethate: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
monitor_inn: "Colistimethate"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "hepatic porphyria", "brachyolmia", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis"]
---

# Colistimethate
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

# Colistimethate: From Bacterial Infection to Osteoarthritis

## One-Sentence Summary

Colistimethate is a polymyxin antibiotic (a prodrug of colistin) that is marketed in India as an injectable product.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal with no biological rationale identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, colistimethate is a polymyxin antibiotic and a prodrug of colistin. It disrupts the outer membrane of Gram-negative bacteria, and its established use is in Gram-negative infections.

No known pathway connects this antibacterial action to the pathophysiology of osteoarthritis (cartilage degradation and inflammation). The high TxGNN score appears to be a graph-based prediction only, likely reflecting network proximity to other arthritis-related drugs rather than a biological rationale.

Systemic use also carries nephrotoxicity and neurotoxicity risks. These are unfavourable for a chronic, non-infectious condition such as osteoarthritis.

Other top-ranked predictions show the same pattern. These include rheumatoid arthritis (97.48%), osteoarthritis susceptibility (97.41%), gout (96.85%), pseudoachondroplasia (96.74%), hepatic porphyria (96.71%), brachyolmia (96.40%), and three hepatic vascular conditions (primitive portal vein thrombosis, hepatopulmonary syndrome and hepatoportal sclerosis, each 96.27%). None has any identified mechanistic support, and the three hepatic vascular conditions share an identical score, suggesting a graph-neighbourhood artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Colistimethate has 20 valid single-ingredient registrations, all injectable (vials). Approved indication text is not recorded for any of them. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 111319 | Ibicolist 4.5MIU Injection | Vial of 1 injection | Not recorded |
| 46540 | Colifen 2 MIU Injection | Vial of 1 injection | Not recorded |
| 13915 | Acostin 3Million IU Injection (Sun Pharmaceutical Industries Ltd) | Vial of 1 injection | Not recorded |
| 204939 | Sudostar 3MIU Injection (Lupin Ltd) | Vial of 1 injection | Not recorded |
| 243851 | Xylistin 1MIU Injection (Cipla Ltd) | Vial of 1 injection | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 33 interactions were identified, of which the main ones are listed below.
  - **Major**: Kanamycin, Neomycin and Streptomycin (other aminoglycosides, with additive nephrotoxicity and neurotoxicity as a likely concern); Deferasirox; and iodinated contrast agents (Diatrizoate, Iodipamide, Iodixanol, Iohexol, Iopamidol, Iopromide, Iothalamic acid, Ioversol, Ioxilan).
  - **Moderate**: Mesalazine, Balsalazide, Olsalazine, Sulfasalazine, Picosulfuric acid, Exenatide and Vancomycin.
- **Toxicity profile**: Systemic use is associated with nephrotoxicity and neurotoxicity, which is a major barrier for any chronic non-infectious use.

For other warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score, with no clinical trials, no literature and no plausible mechanism. Together with the known nephrotoxicity and neurotoxicity of systemic colistimethate, the benefit-risk balance for osteoarthritis is unfavourable.

**To proceed, the following is needed:**
- Mechanism of action data and preclinical evidence linking colistimethate to cartilage or joint inflammation pathways
- Package insert warnings and contraindications from the India regulatory source, which are needed for safety screening
- Approved indication text for the registered products
- Assessment of route compatibility, since the drug is available only as an injectable and the predicted indication would need a suitable route (for example intra-articular) and formulation
- Any supporting clinical or preclinical studies before reconsidering the decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

