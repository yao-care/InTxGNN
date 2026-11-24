---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Mupirocin: predicted new indication Pleural empyema (disease) (evidence level L5). In India: at least 20 listed products"
---

# Mupirocin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Mupirocin: Pleural empyema (disease)
{: .text-alpha }

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo and bullous impetigo.
The TxGNN model's top-ranked prediction is **pleural empyema** (score 0.9949), but this prediction has **no clinical trials and no publications** behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pleural empyema (disease) |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 (pleural empyema); L3 (SSSS) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold (pleural empyema); SSSS is a Research Question |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for mupirocin: "Mupirocin is an RNA synthetase inhibitor antibacterial. […] Mupirocin inhibits bacterial protein synthesis by reversibly and specifically binding to bacterial isoleucyl-transfer RNA (tRNA) synthetase. Mupirocin is bactericidal at concentrations achieved by topical administration." ([DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870), label version 2020-03-20; accessed 2026-11-19.) Based on known information, mupirocin is a topical antibacterial that inhibits bacterial isoleucyl-tRNA synthetase and is mainly active against gram-positive bacteria such as *Staphylococcus aureus*. Its efficacy in impetigo is established, and mechanistically it may be applicable to other *S. aureus*-driven conditions.

**Pleural empyema (rank 1)** is a weak fit. *S. aureus* can cause empyema, but mupirocin is not used systemically and would not reach the pleural space, so there is no plausible route of use. The high score appears to be a model artefact rather than a pharmacologically grounded signal.

Topical mupirocin can reduce local bacterial load as an adjunct to systemic antistaphylococcal therapy. Its limits are that it would not be a standalone treatment, topical therapy has limited efficacy in generalised disease, and mupirocin-resistant *S. aureus* clones have been reported.

Other predictions are weak or unsupported:
- The only paper concerns MRSA vaginitis, a different condition.
- **Punctate epithelial keratoconjunctivitis, neurotrophic keratopathy, vaginal discharge, leukoplakia of vagina:** prediction only, with no plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pleural empyema or for any other predicted indication.

---

## Literature Evidence

No literature is available for pleural empyema (the top-ranked prediction).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Rev Anti Infect Ther | Treatment of bullous impetigo and SSSS in infants; bullous impetigo is caused by *S. aureus* exfoliative toxin |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatol Clin | Control of staphylococci in skin disease; topical mupirocin described as a valuable addition for impetigo |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Epidemiology/molecular | J Med Microbiol | Emergence of a mupirocin- and fusidic acid-resistant, toxin-producing MSSA clone (ST121) causing SSSS |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Epidemiology/molecular | J Clin Microbiol | A mupirocin- and fusidic acid-resistant *S. aureus* clone carrying exotoxin genes, mainly causing skin infections |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case report series | Adv Neonatal Care | SSSS identification and wound care in neonates |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Cohort/epidemiology | Pediatr Infect Dis J | Rising SSSS cases caused by ST121 in Houston, Texas |
| [42509990](https://pubmed.ncbi.nlm.nih.gov/42509990/) | 2026 | Retrospective cohort | Children (Basel) | Epidemiology, management and complications of paediatric SSSS over 11 years |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Outbreak investigation | J Hosp Infect | Nosocomial SSSS outbreak in neonates and its control |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case report | Dermatopathology (Basel) | SSSS in an adult receiving chemotherapy |

Evidence for other predictions is limited to low-tier reports:
- Study design could not be confirmed.

---

## India Market Information

Mupirocin is marketed in India with 20 valid single-ingredient registrations. The approved-indication text is not recorded for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 29323 | Bactirel Ointment | Tube of 5 gm Ointment | Valid |
| 29591 | Bactifree Lotion | Bottle of 100 ml Lotion | Valid |
| 63333 | Dibact Powder | Sachet of 5 gm Powder | Valid |
| 134132 | Mupivate Ointment | Tube of 3 gm Ointment | Valid |
| 134377 | Mupinase Cream | Tube of 7.5 gm Cream | Valid |
| 134999 | Mupricon Ointment | Tube of 5 gm Ointment | Valid |
| 137265 | Mocin 2% Ointment | Tube of 5 gm Ointment | Valid |
| 137329 | MU 2% Ointment | Tube of 5 gm Ointment | Valid |
| 137362 | Mucidal 2% Ointment | Tube of 5 gm Ointment | Valid |
| 137947 | Mufect Ointment | Tube of 5 gm Ointment | Valid |
| 139459 | Mupiron Ointment | Tube of 10 gm Ointment | Valid |
| 139960 | Muprax 2% Ointment | Tube of 5 gm Ointment | Valid |
| 145858 | Mupisel 2% Ointment | Tube of 5 gm Ointment | Valid |
| 145881 | Mupinova 2% Ointment | Tube of 3 gm Ointment | Valid |
| 201780 | Supiroban 2% Ointment | Tube of 5 gm Ointment | Valid |
| 203038 | Solum 2% Ointment | Tube of 5 gm Ointment | Valid |
| 216885 | Topibact 2% Ointment | Tube of 10 gm Ointment | Valid |
| 217325 | Tercin WHP Powder | Box of 5 gm Powder | Valid |
| 221452 | Tercin WHP Powder | Box of 10 gm Powder | Valid |
| 223968 | Topibact 2% Ointment | Tube of 5 gm Ointment | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The remaining registrations are mostly 2% ointments, plus powder products (Dibact, Tercin WHP). All are topical or external forms, and none is systemic or ophthalmic.

---

## Safety Considerations

- **Disease-level contraindication (knowledge graph):** dermatitis.
- **Drug Interactions:** 118 potential interactions were identified in a drug-interaction database, but none has a severity level assigned. Examples include calcitriol, clotrimazole, morphine, metformin, pantoprazole, omeprazole, vancomycin, triamcinolone, prednisone, simvastatin, nystatin and rosuvastatin. Because mupirocin is applied topically, the clinical relevance of these entries is uncertain.
- **Ocular use:** an in vitro study reported corneal epithelial toxicity, so the available formulations should not be assumed suitable for the eye.

Please refer to the package insert for other safety information, including warnings and contraindications, as these were not available.

---

## Conclusion and Next Steps

**Decision: Hold** (pleural empyema and the other prediction-only indications).

**Rationale:**
The top-ranked prediction, pleural empyema, has a very high model score but no trials, no literature and no plausible route of use for a topical drug. That evidence is still low-tier (L3), and mupirocin resistance is a concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For SSSS: a controlled study or systematic review of mupirocin as an adjunct, and local mupirocin resistance data in India
- Route-compatibility assessment, including whether available topical products suit any proposed use
- Confirmation of study design for the title-only report (PMID 1678836) if the candidiasis direction is pursued

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

