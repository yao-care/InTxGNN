---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Erythromycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L4). Approved use: Bacterial infections, including acne, otitis media…"
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "acute contagious conjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
---

# Erythromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Erythromycin: From Bacterial Infections (Acne, Otitis Media, Pneumonia, Conjunctivitis) to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Erythromycin is a macrolide antibiotic, originally used for bacterial infections such as acne, otitis media, streptococcal and staphylococcal infections, pneumonia, gonorrhoea, pertussis and conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **no registered clinical trials** and only **1 publication** (a general review) for this indication, so the prediction rests mainly on the model and mechanistic plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including acne, otitis media, pneumonia and conjunctivitis (taken from the drug's known indications, because the approved-indication text in the Indian licence records is empty) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, erythromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. It also has anti-inflammatory activity. Its efficacy in bacterial conjunctivitis and other infections is established.

The original indications include conjunctivitis, so an ocular surface condition is a natural neighbour. Chronic blepharokeratoconjunctivitis is driven by meibomian gland dysfunction, bacterial overgrowth and ocular surface inflammation, and macrolides (topical or systemic) are used in its management. This makes the link plausible, but it is indirect. The only retrieved paper is a review of diagnosis and management in children, not a study of erythromycin for this specific condition.

Other predicted indications fall into two groups. Acute contagious conjunctivitis (score 0.9955) largely overlaps the existing label and has no retrieved evidence. Lymphogranuloma venereum (score 0.9905) has the strongest mechanistic link, because it is a *Chlamydia trachomatis* infection, but the literature lists erythromycin only as an alternative to doxycycline, and no trials were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | Describes the history, symptoms, clinical signs and treatment of blepharokeratoconjunctivitis in children; does not test erythromycin specifically |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 78989 | Erythrocin Granules (Pfizer Ltd) | Granules, sachet of 30 ml | Not stated in licence record |
| 80278 | Erythrox 250mg Tablet (Medicraft Group) | Tablet, strip of 10 | Not stated in licence record |
| 79299 | Eromed 125mg Suspension (Comed Chemicals Ltd) | Suspension, bottle of 60 ml | Not stated in licence record |
| 5250 | Acnebenz Gel (A. Menarini India Pvt Ltd) | Topical gel, tube of 60 g | Not stated in licence record |
| 79419 | Erylent Gel (Talent Healthcare) | Topical gel, tube of 20 g | Not stated in licence record |

There are 20 valid single-ingredient registrations in total. They include oral tablets, suspensions and granules, plus two topical gels. No ophthalmic formulation appears among them.

## Safety Considerations

- **Contraindication-related conditions (from knowledge-graph drug-disease links, not label text)**: long QT syndrome (including familial), torsades de pointes, porphyria, kidney disease, liver disease, gallbladder disease, haematologic disease, myasthenia gravis and other neuromuscular junction disease, hearing disorders, *Clostridium difficile* colitis, exfoliative dermatitis and other dermatitis, folic acid deficiency anaemia, pyoureter, and perinatal necrotising enterocolitis.
- **Drug Interactions**: 755 interactions were recorded. Major-level ones include **clarithromycin** and **loperamide**. Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), cimetidine, famotidine, aprepitant, pioglitazone, chlorpropamide and alosetron. Amoxicillin is minor.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9989), but the evidence is limited to a single general review with no clinical trials, and no ophthalmic erythromycin product is registered in India. The prediction is mechanistically plausible but not yet supported by direct evidence.

**To proceed, the following is needed:**
- Studies or trials of erythromycin (topical or systemic) specifically in punctate epithelial keratoconjunctivitis
- Package insert warnings and contraindications from Indian regulatory sources, to allow safety screening
- Mechanism of action data confirmed from DrugBank
- Route and formulation assessment, since the registered products are oral or topical skin gels rather than ophthalmic preparations
- A comparison against standard ocular therapies, since the retrieved evidence also notes macrolide resistance limits in MRSA-related eye infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

