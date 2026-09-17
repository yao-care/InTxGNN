---
layout: default
title: Xylometazoline
parent: Model Prediction Only (L5)
nav_order: 891
evidence_level: L5
indication_count: 2
---

# Xylometazoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Xylometazoline: From Nasal Decongestion to Nasal Cavity Disease

## One-Sentence Summary

> Xylometazoline is a widely used over-the-counter (OTC) nasal decongestant, an imidazoline-derivative α-adrenergic agonist traditionally used to relieve nasal congestion associated with colds and allergic rhinitis.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
> with **2 clinical trials** and **7 publications** currently supporting this direction — though most of this evidence reflects the drug's already-known decongestant/vasoconstrictive effect rather than a genuinely novel mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No formal India regulatory license on record; per DrugBank pharmacology data, used as a component of OTC nasal decongestants for nasal congestion/allergy-related mucosal swelling |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 (observational/small clinical studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank MOA description is not available for Xylometazoline (flagged as a data gap, DG002). However, pharmacology-target data in the Evidence Pack shows Xylometazoline binds α1D, α2A, α2B, and α2C adrenoceptors. Agonism at these receptors on nasal mucosal vascular smooth muscle causes vasoconstriction, which is the well-established basis for its decongestant effect.

Because "Nasal Cavity Disease" is essentially the anatomical category that already contains congestion, mucosal swelling, and rhinitis — the conditions Xylometazoline is already used to treat as an OTC decongestant — this TxGNN prediction is less a discovery of a *new* indication and more a confirmation of an *already-known* pharmacological effect. Several of the supporting studies directly measure nasal airway resistance, nasal cavity volume, or nasal mucosal decongestion after Xylometazoline administration, which mechanistically maps onto the predicted disease category rather well.

By contrast, the second-ranked prediction (acute laryngopharyngitis, TxGNN score 99.89%) has no supporting clinical trials or literature at all — it appears to rely purely on anatomical proximity (nasal mucosa vs. laryngopharyngeal mucosa) as a model-level inference, with no direct evidence connecting Xylometazoline to that indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Triple-crossover comparison of cocaine, lidocaine/xylometazoline, and saline for intranasal analgesia during awake fiberoptic nasotracheal intubation. Grade B relevance — evaluates a lidocaine/xylometazoline combination for a procedural (anesthetic) purpose, not xylometazoline alone as a disease treatment; small sample (n=16). |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | N/A | Unknown | 80 | Foley catheter-assisted nasal intubation vs. conventional practice to reduce nasal bleeding during nasotracheal intubation. Grade C relevance — evaluates a mechanical intubation technique, not xylometazoline's therapeutic effect on nasal cavity disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT | JAMA Otolaryngology–Head & Neck Surgery | Double-blind, placebo-controlled RCT in children: intranasal topical local anesthetic/decongestant (including xylometazoline) improved tolerance and visualization for flexible nasendoscopy. |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Cohort/Small clinical study | Korean Journal of Anesthesiology | Prophylactic intranasal xylometazoline spray compared to epinephrine gauze packing for nasal mucosa constriction and nasal cavity expansion before nasotracheal intubation. |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Cohort/Small clinical study | Rhinology | Topical xylometazoline reduced nasal airway resistance asymmetry in healthy subjects and those with acute rhinitis from the common cold. |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective RCT | European Archives of Oto-Rhino-Laryngology | Randomized, blinded study comparing cotton pledget packing vs. topical decongestant spray for nasal preparation before endoscopy; supports decongestant efficacy in nasal cavity preparation. |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | RCT | Arzneimittel-Forschung | Double-blind rhinomanometric study of a tuaminoheptane/N-acetyl-cysteine combination vs. xylometazoline and placebo for nasal resistance reduction — xylometazoline used as active comparator, not primary study drug. |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestnik Otorinolaringologii | Review of nasal mucosa changes in the elderly and treatment approaches for inflammatory diseases of the nasal cavity and paranasal sinuses, discussing decongestant-containing nasal sprays. |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal study | Pneumologie | Animal (canine) model study showing xylometazoline reduced pathologically elevated intranasal airway resistance in brachycephalic dogs by ~50%. |

---

## India Market Information

Xylometazoline currently has **no India regulatory license or market authorization on record** (Market Status: Not Marketed; 0 registrations). No product-level dosage form or approved-indication data is available in the Evidence Pack.

---

## Safety Considerations

The Evidence Pack does not contain TFDA/India-specific warnings or contraindications data (flagged as a Blocking data gap, DG001).

- **Receptor Pharmacology Profile**: Xylometazoline shows binding activity at α1D, α2A, α2B, and α2C adrenoceptors (pharmacology database), consistent with its vasoconstrictive decongestant mechanism. No formal clinical drug-drug interaction (DDI) data with severity levels is currently available — the listed entries represent receptor-binding pharmacology, not clinical DDI pairs.

Please refer to the package insert for further safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (Nasal Cavity Disease) is mechanistically well-supported and largely reflects an already-established pharmacological effect of Xylometazoline as a nasal decongestant, but formal MOA documentation, India regulatory safety data (warnings/contraindications), and direct high-quality RCTs targeting "nasal cavity disease" as a defined clinical endpoint are still missing. The second predicted indication (acute laryngopharyngitis, L5, Hold) lacks any supporting evidence and should not be advanced at this time.

**To proceed, the following is needed:**
- TFDA/India-equivalent package insert warnings and contraindications (DG001, Blocking — required before S1 safety review)
- Confirmed DrugBank/manufacturer MOA documentation (DG002, High priority)
- India market authorization status confirmation, given current "Not Marketed" status
- Direct clinical evidence (ideally RCTs) evaluating xylometazoline monotherapy against a defined "nasal cavity disease" endpoint, rather than as a procedural/comparator agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

