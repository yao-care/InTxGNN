---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Mupirocin: predicted new indication Pleural empyema (disease) (evidence level L5). Approved use: Not recorded in the local data"
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

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mupirocin is a topical antibacterial that inhibits bacterial isoleucyl-tRNA synthetase and is mainly active against gram-positive bacteria such as *Staphylococcus aureus*. Its efficacy in impetigo is established, and mechanistically it may be applicable to other *S. aureus*-driven conditions.

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

Mupirocin is marketed in India with 20 valid single-ingredient registrations. Five main registrations are shown below. The approved-indication text is not recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 203038 | Solum 2% Ointment | Ointment (5 g tube) | Not recorded |
| 134377 | Mupinase Cream | Cream (7.5 g tube) | Not recorded |
| 137947 | Mufect Ointment | Ointment (5 g tube) | Not recorded |
| 201780 | Supiroban 2% Ointment | Ointment (5 g tube) | Not recorded |
| 29591 | Bactifree Lotion | Lotion (100 ml bottle) | Not recorded |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

