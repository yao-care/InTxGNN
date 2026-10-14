---
layout: default
title: Fusidic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 385
evidence_level: L4
indication_count: 10
---

# Fusidic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Fusidic Acid: From Bacterial Skin and Systemic Infections to Exposure Keratitis

## One-Sentence Summary

Fusidic acid is an antibacterial agent, originally used for infections such as urinary tract infection, bronchitis, acne, folliculitis and bacterial pneumonia, and in India it is marketed as topical creams and ointments.
The TxGNN model predicts it may be effective for **Exposure Keratitis**, but there are **0 clinical trials** and only **1 publication** (an unrelated case series of ocular infections), so the prediction is not supported by clinical data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated on the Indian licences; the knowledge graph lists urinary tract infection, bronchitis, acne, folliculitis, seborrheic dermatitis, bacterial pneumonia and others |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, fusidic acid inhibits bacterial protein synthesis by blocking elongation factor G, and it is strongly active against Gram-positive bacteria such as *Staphylococcus*.

Exposure keratitis is mainly a mechanical or desiccation disorder of the cornea, caused by incomplete eyelid closure. An antibacterial would only be relevant if a secondary bacterial infection developed. The single retrieved paper is a case series on ocular *Tsukamurella* infections and does not study fusidic acid in this condition. The very high TxGNN score therefore appears to reflect proximity in the knowledge graph (ocular and infectious disease nodes) rather than clinical support.

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

Product indication text is not recorded on the licences. All 20 registrations are valid single-ingredient products, and the main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 88191 | Fusy Cream | Cream (5 g tube) | Not recorded |
| Registration No. 85771 | Fusidox 20mg Cream | Cream (5 g tube) | Not recorded |
| Registration No. 87795 | Fusilife Cream | Cream (10 g tube) | Not recorded |
| Registration No. 209057 | Safoban Ointment | Ointment (10 g tube) | Not recorded |
| Registration No. 85644 | Fusi Ointment | Ointment (5 g tube) | Not recorded |

All registered products are topical creams or ointments; no oral or ophthalmic forms are registered.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The knowledge graph links fusidic acid with contraindications in conditions including liver failure, liver disease, kidney disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, atrial fibrillation, atrioventricular block, myasthenia gravis, glaucoma, ocular hypertension, herpes simplex virus keratitis, eye infectious disease, conjunctivitis, *Clostridium difficile* colitis and respiratory failure. These associations are model-derived and should be checked against the official package insert.
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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

