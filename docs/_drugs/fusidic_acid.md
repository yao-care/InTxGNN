---
layout: default
title: Fusidic Acid
parent: Model Prediction Only (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Fusidic acid"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
description: "Fusidic Acid: predicted new indication Exposure keratitis (evidence level L5). In India: at least 20 listed products"
---

# Fusidic Acid
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

## Fusidic Acid: Exposure keratitis
{: .text-alpha }

## One-Sentence Summary

Fusidic acid is an antibacterial agent, originally used for infections such as urinary tract infection, bronchitis, acne, folliculitis and bacterial pneumonia, and in India it is marketed as topical creams and ointments.
The TxGNN model predicts it may be effective for **Exposure Keratitis**, but there are **0 clinical trials** and only **1 publication** (an unrelated case series of ocular infections), so the prediction is not supported by clinical data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of fusidic acid as: Elongation factor G inhibitor ([ChEMBL CHEMBL374975 (fusidic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL374975), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, fusidic acid inhibits bacterial protein synthesis by blocking elongation factor G, and it is strongly active against Gram-positive bacteria such as *Staphylococcus*.

Exposure keratitis is mainly a mechanical or desiccation disorder of the cornea, caused by incomplete eyelid closure. An antibacterial would only be relevant if a secondary bacterial infection developed. The single retrieved paper is a case series on ocular *Tsukamurella* infections and does not study fusidic acid in this condition. The very high TxGNN score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case series | Cornea | Ophthalmic infections caused by *Tsukamurella* species, including the first report of ocular implant infection after enucleation; it does not evaluate fusidic acid or exposure keratitis |

---

## India Market Information

Product indication text is not recorded on the licences.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 39809 | Cudic 20mg Cream | Tube of 10 gm Cream | Valid |
| 65606 | Dicfu 20mg Cream | Tube of 10 gm Cream | Valid |
| 84105 | Fudic Cream | Tube of 10 gm Cream | Valid |
| 84253 | Fusiwal Cream | Tube of 5 gm Cream | Valid |
| 85040 | Fuzi Cream | Tube of 10 gm Cream | Valid |
| 85333 | Fexit Cream | Tube of 10 gm Cream | Valid |
| 85644 | Fusi Ointment | Tube of 5 gm Ointment | Valid |
| 85771 | Fusidox 20mg Cream | Tube of 5 gm Cream | Valid |
| 85884 | Fusic Cream | Tube of 10 gm Cream | Valid |
| 86122 | Fubact Cream | Tube of 10 gm Cream | Valid |
| 86130 | Fucid 2% Cream | Tube of 5 gm Cream | Valid |
| 86224 | Fusipan B Cream | Tube of 10 gm Cream | Valid |
| 87660 | Fudine Cream | Tube of 5 gm Cream | Valid |
| 87795 | Fusilife Cream | Tube of 10 gm Cream | Valid |
| 88191 | Fusy Cream | Tube of 5 gm Cream | Valid |
| 88895 | Fusidox 20mg Cream | Tube of 7.5 gm Cream | Valid |
| 88906 | Fusivic Cream | Tube of 10 gm Cream | Valid |
| 165148 | Optimix Cream | Tube of 10 gm Cream | Valid |
| 204470 | Sofibet 2% Cream | Tube of 10 gm Cream | Valid |
| 209057 | Safoban Ointment | Tube of 10 gm Ointment | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All registered products are topical creams or ointments; no oral or ophthalmic forms are registered.

---

## Safety Considerations

- **Contraindications (TxGNN model associations, not label text)**: The TxGNN model (deep learning) associates fusidic acid with contraindications in conditions including liver failure, liver disease, kidney disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, atrial fibrillation, atrioventricular block, myasthenia gravis, glaucoma, ocular hypertension, herpes simplex virus keratitis, eye infectious disease, conjunctivitis, *Clostridium difficile* colitis and respiratory failure. These associations may reflect similarities the model learned between related diseases, not biological evidence, and should be checked against the official package insert.
- **Ocular relevance**: Several of these associations involve the eye (glaucoma, ocular hypertension, herpes simplex keratitis, eye infection, conjunctivitis), which needs particular scrutiny for any ophthalmic use.

No drug-interaction data were found, and package-insert warnings were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials and no directly relevant literature. Exposure keratitis is not primarily an infectious disease, and all marketed Indian products are topical skin formulations, not ophthalmic ones.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications from the Indian regulator's records
- Mechanism-of-action data (for example from DrugBank)
- Evidence that secondary bacterial infection in exposure keratitis is a meaningful, fusidic-acid-susceptible target
- An ophthalmic formulation and route-compatibility assessment, including the ocular contraindication signals above

**Other predictions worth noting:** Otitis externa (rank 3, evidence level L4) has a plausible mechanism, since *S. aureus* and *S. pseudintermedius* are within fusidic acid's spectrum and topical use is reasonable. However, the retrieved literature is mostly veterinary or indirect, and rising staphylococcal resistance is a concern. It is better framed as a research question than as a candidate for advancement. The remaining predictions (ranks 2 and 4–10) have no supporting evidence and should stay on hold.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL374975 (fusidic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL374975) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

