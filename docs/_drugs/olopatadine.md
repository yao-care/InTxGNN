---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 1
---

# Olopatadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Olopatadine: From Allergic Rhinitis and Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an antiallergic drug originally used for allergic rhinitis, vasomotor rhinitis, and several forms of allergic conjunctivitis (atopic, papillary, and vernal).
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but at present there are **no registered clinical trials and no publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olopatadine is marketed as a histamine H1 antagonist and mast cell stabilizer. It is used for allergic conjunctivitis, and mechanistically it may be applicable to rosacea conjunctivitis.

Rosacea conjunctivitis involves inflammation of the ocular surface. Olopatadine could plausibly reduce ocular surface inflammation and itching. This is an inference from general pharmacology and is not supported by the data compiled for this report.

The high TxGNN score likely reflects network proximity to the approved conjunctivitis indications in the knowledge graph. It should be read as a computational signal, not as proof of efficacy. In addition, rosacea conjunctivitis is driven largely by meibomian gland dysfunction and non-allergic inflammation, so an antihistamine may address only part of the disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Olopatadine is marketed in India as single-ingredient products, with 20 valid registrations and none cancelled. Both oral tablets and ophthalmic solutions are available. The data compiled for this report do not include approved indication text for any of them. The main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 61853 | Dynolap 5 Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 174208 | Patadin Tablet | Strip of 10 tablets | Ajanta Pharma Ltd |
| 5691 | Allenil 5mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 175802 | Pataone Eye Drop | Bottle of 5 ml ophthalmic solution | Choroid Laboratories |
| 4747 | Alerchek OD Ophthalmic Solution | Packet of 3 ml ophthalmic solution | Indoco Remedies Ltd |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, and upper respiratory tract disease. These come from computational drug-disease contraindication edges and should be verified against the approved labelling.
- **Drug Interactions:** The interaction screen returned 112 potential interacting drugs, but the severity level is unclassified for all of them. Examples include pantoprazole, omeprazole, lansoprazole, cimetidine, metformin, simvastatin, rosuvastatin, prednisone, prednisolone, hydrocortisone, triamcinolone, epinephrine, doxycycline, and tetracycline. Clinical significance must be assessed individually.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications supporting it (Evidence Level L5). The mechanism data and the package-insert safety information needed for safety screening are also missing.

**To proceed, the following is needed:**
- Obtain the Indian package insert (warnings and contraindications) for the safety screening
- Obtain detailed mechanism of action data from DrugBank
- Conduct a literature and trial search for olopatadine or antihistamine/mast cell stabilizer use in ocular rosacea
- Confirm that an ophthalmic route is suitable for the target use, since the registered products include both oral tablets and eye drops
- Classify the severity of the 112 potential drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

