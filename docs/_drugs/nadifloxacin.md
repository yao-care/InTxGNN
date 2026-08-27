---
layout: default
title: Nadifloxacin
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Nadifloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nadifloxacin: From Acne / Skin Infections to Malaria

## One-Sentence Summary

Nadifloxacin is a topical fluoroquinolone antibiotic approved in several markets for the treatment of acne vulgaris and superficial bacterial skin infections. The TxGNN model predicts it may be effective for **Malaria**, with a prediction score of 99.16%; however, **no clinical trials** and **no published literature** currently support this direction. The prediction almost certainly reflects a class-level fluoroquinolone association in the knowledge graph rather than any property specific to Nadifloxacin itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris / superficial bacterial skin infections (topical antibiotic; no India registration on record) |
| Predicted New Indication | Malaria |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Nadifloxacin belongs to the fluoroquinolone class of antibiotics. Its mechanism of action is shared with other fluoroquinolones — inhibition of bacterial DNA gyrase (topoisomerase II) and topoisomerase IV — which disrupts DNA replication and transcription in susceptible micro-organisms. As a topical preparation, however, it achieves meaningful drug concentrations only within the skin, with negligible systemic absorption.

The knowledge-graph rationale for the malaria prediction rests on the fact that certain fluoroquinolones (e.g., Ciprofloxacin) display in-vitro inhibitory activity against *Plasmodium falciparum* DNA gyrase homologues (PfGyrA/B). Some quinolone derivatives have been investigated as anti-malarial scaffolds in early-stage research, creating a documented edge in the TxGNN knowledge graph between "fluoroquinolone class" and "malaria."

In practice, this mechanistic link does not transfer to Nadifloxacin for two fundamental reasons. First, Nadifloxacin is formulated exclusively as a topical cream/ointment; systemic bioavailability after dermal application is extremely low and far below any anti-malarial therapeutic threshold. Second, no in-vitro or in-vivo data exist for Nadifloxacin against *Plasmodium* spp. specifically. The high TxGNN score most likely reflects a class-level generalisation — a known limitation of knowledge-graph models that do not differentiate between systemic and topical members of the same drug class.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Nadifloxacin currently has **no registered products** in India. The drug is therefore not available through any licensed domestic channel and carries no approved local indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warning and contraindication data (DG001) were not available in this Evidence Pack. As a fluoroquinolone-class antibiotic, prescribers should be aware of general class effects (photosensitivity, potential for bacterial resistance, skin irritation at the application site) until full label data can be retrieved from the regulatory authority.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are classified as L5 (model prediction only), with zero supporting clinical trials or publications across every disease queried. More critically, Nadifloxacin's topical-only formulation creates a fundamental route-of-administration mismatch for every systemic indication in the prediction list (malaria, relapsing fever, leishmaniasis, spondyloarthropathy, rheumatoid vasculitis, Zollinger-Ellison syndrome, elevated plasma zinc). The only indication that carries any residual biological plausibility is **demodicidosis of the sebaceous gland** (Rank 6), where Nadifloxacin's established activity against *Cutibacterium acnes* could address secondary bacterial co-infection — but even this would require reclassification as adjunctive therapy rather than primary treatment.

**To proceed, the following is needed:**

- **Retrieve full prescribing information** (DG001): Download and parse the official package insert (e.g., Acuatop®, OzenoxaCe®) to complete safety, contraindication, and warning data.
- **Confirm MOA data** (DG002): Query DrugBank API for Nadifloxacin's mechanistic profile (targets, enzyme inhibition constants, spectrum of activity) to enable proper mechanistic-link scoring.
- **Route-compatibility assessment**: Any future repurposing candidate must be a **dermatological indication** compatible with topical application, or require a new formulation development programme (oral/IV) — a substantially higher development burden.
- **Focused evidence search for demodicidosis**: If a decision is made to investigate one indication further, search PubMed and ClinicalTrials.gov specifically for *Demodex*-related skin disease and topical antibiotics to determine whether a research question (not a development programme) is warranted.
- **India regulatory pathway**: If any indication is validated, a full new-drug application or labelling-extension dossier would be required given zero current Indian registrations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

