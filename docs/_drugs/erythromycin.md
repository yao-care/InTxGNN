---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
description: "Erythromycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Erythromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Erythromycin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Erythromycin is a macrolide antibiotic that blocks bacterial protein synthesis and also has anti-inflammatory activity.
The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**,
but so far there are **no registered clinical trials** and only **1 publication** (a pediatric review), so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Erythromycin is a macrolide. It binds the bacterial 50S ribosomal subunit and stops protein synthesis, and it also has anti-inflammatory effects. This description relies on the general pharmacology of the macrolide class. According to the Mechanism of Action section of the US FDA-approved prescribing information for erythromycin: "Erythromycin acts by inhibition of protein synthesis by binding 50S ribosomal subunits of susceptible organisms. It does not affect nucleic acid synthesis." ([DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd), label version 2018-12-04; accessed 2026-11-19.)

Punctate epithelial keratoconjunctivitis and related chronic blepharokeratoconjunctivitis involve ocular surface inflammation, often linked to meibomian gland dysfunction and bacterial overgrowth. In that setting, a drug with both antibacterial and anti-inflammatory activity could plausibly help. Topical and systemic macrolides are used in related eyelid and ocular surface conditions.

This link is plausible but indirect. The only retrieved paper is a general review of the diagnosis and management of chronic blepharokeratoconjunctivitis in children. It is not a study of erythromycin in punctate epithelial keratoconjunctivitis itself. Because no cited study directly examines this disease, the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | Describes history, symptoms, signs and treatment of chronic blepharokeratoconjunctivitis in children; does not test erythromycin directly for the predicted disease |

## India Market Information

At least 20 licences are recorded, all valid, and the list may be partial.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 5250 | Acnebenz Gel | Tube of 60 gm Gel | Valid |
| 11034 | Arthrox 500mg Tablet | Strip of 10 tablets | Valid |
| 11692 | Arthrox 250mg Tablet | Strip of 10 tablets | Valid |
| 21528 | Althraled 250mg Tablet | Strip of 10 tablets | Valid |
| 23465 | Avithrocin 250mg Tablet | Strip of 10 tablets | Valid |
| 50640 | Cythrocin 500mg Tablet | Strip of 10 tablets | Valid |
| 75344 | Erocin 100mg Tablet | Strip of 10 tablets | Valid |
| 76594 | Ethril 250mg Tablet | Strip of 10 tablets | Valid |
| 77113 | E Mycin 100mg Suspension | Bottle of 60 ml Suspension | Valid |
| 77292 | Eroate 500mg Tablet | Strip of 10 tablets | Valid |
| 78989 | Erythrocin Granules | Sachet of 30 ml Granules | Valid |
| 79299 | Eromed 125mg Suspension | Bottle of 60 ml Suspension | Valid |
| 79419 | Erylent Gel | Tube of 20 gm Gel | Valid |
| 80278 | Erythrox 250mg Tablet | Strip of 10 tablets | Valid |
| 81362 | Ertomac 500mg Tablet | Strip of 10 tablets | Valid |
| 82127 | Erocyn 250mg Tablet | Strip of 10 tablets | Valid |
| 82826 | Elithron 250mg Tablet | Strip of 10 tablets | Valid |
| 83454 | Erygin 250mg Tablet | Strip of 10 tablets | Valid |
| 183429 | Q Mycin 125mg Tablet | Strip of 10 tablets | Valid |
| 212734 | Suzithrocin 125mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include oral tablets, granules and suspensions, and topical gels. No ophthalmic form appears among the recorded licences.

## Safety Considerations

- **Contraindications / cautions in related conditions:** Erythromycin is linked to caution in long QT syndrome, torsades de pointes, porphyria, kidney disease, liver disease, haematologic disease, myasthenia gravis and other neuromuscular junction disease, hearing disorders, *Clostridium difficile* colitis, and exfoliative dermatitis or dermatitis. This list is not drawn from label text.
- **Drug Interactions:** 755 interactions were recorded. Major-level ones include **clarithromycin** and **loperamide**. Moderate-level ones include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), famotidine, cimetidine, pioglitazone, aprepitant and alosetron. QT-prolonging and CYP3A4-interacting combinations deserve particular attention.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9989), and the mechanism is plausible given erythromycin's antibacterial and anti-inflammatory activity. However, there are no clinical trials and no study directly examining this disease, so the evidence rests on the model prediction alone.

**To proceed, the following is needed:**
- Studies or case series of erythromycin, preferably topical ophthalmic, in punctate epithelial keratoconjunctivitis
- Confirmed mechanism-of-action data
- Package insert warnings and contraindications, which are currently missing
- Assessment of whether an ophthalmic formulation is available, since no ophthalmic form is among the recorded licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on the general pharmacology of the macrolide class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

