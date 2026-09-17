---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 773
evidence_level: L5
indication_count: 7
---

# Sodium Fluoride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sodium Fluoride: From Unregistered Status to Predicted Multiple Infectious/Inflammatory Indications

## One-Sentence Summary

Sodium fluoride (DrugBank DB09325) is not marketed in Taiwan and has no established original indication or mechanism of action on record. The TxGNN model predicts high-confidence associations with several infectious and inflammatory conditions (epiglottitis, urinary tract infection, gonococcal urethritis, and others), but **no clinical trials, no mechanistic data, and only tangential literature (primarily diagnostic PET imaging studies)** support these associations, indicating the predictions are likely knowledge-graph artifacts rather than genuine therapeutic signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug has no registered indications |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium fluoride. The drug is not registered in Taiwan and has no documented original indication, meaning there is no established pharmacological baseline from which to reason about repurposing to infectious/inflammatory disease.

The six predicted indications (epiglottitis, urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis) are all conditions with well-characterized infectious etiologies requiring antimicrobial treatment. Sodium fluoride has no documented antibacterial or anti-inflammatory activity. The most plausible explanation for these high TxGNN scores is a **confounding signal from ¹⁸F-NaF (fluorine-18 sodium fluoride)**, a radiotracer used in PET/CT bone and cartilage imaging that frequently co-occurs in the biomedical literature with head/neck and genitourinary pathology descriptions — not because the drug treats these conditions, but because it is used to *image* related bone/cartilage lesions (e.g., metastases to the thyroid/cricoid cartilage). This is a classic case of a knowledge-graph embedding capturing a diagnostic co-occurrence pattern rather than a true drug-disease treatment relationship.

Mechanistically, none of these predictions have biological plausibility grounded in known fluoride pharmacology (dental/bone mineralization effects, radiotracer uptake), and no supplementary evidence (clinical trials or treatment-focused literature) closes this gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the six predicted indications.

---

## Literature Evidence

Literature evidence exists only for **laryngitis** (rank 7); all other predicted indications have no supporting literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29245332](https://pubmed.ncbi.nlm.nih.gov/29245332/) | 2017 | Case Report (Imaging) | Medicine | ¹⁸F-NaF PET-CT used diagnostically to detect cricoid cartilage invasion in laryngeal carcinoma — imaging use, not treatment |
| [33156044](https://pubmed.ncbi.nlm.nih.gov/33156044/) | 2021 | Case Report (Imaging) | Clinical Nuclear Medicine | ¹⁸F-NaF PET/CT detected thyroid cartilage metastasis from breast cancer — diagnostic imaging only |
| [26204214](https://pubmed.ncbi.nlm.nih.gov/26204214/) | 2015 | Case Report (Imaging) | Clinical Nuclear Medicine | ¹⁸F-NaF and ¹⁸F-FDG PET/CT findings in multiple myeloma with thyroid cartilage involvement — diagnostic, not therapeutic |
| [24178785](https://pubmed.ncbi.nlm.nih.gov/24178785/) | 2013 | Animal Toxicology Study | Biological Trace Element Research | High dietary fluoride suppressed intestinal development in broiler chickens — toxicity signal, unrelated to laryngitis treatment |
| [235491](https://pubmed.ncbi.nlm.nih.gov/235491/) | 1975 | Basic Research | Infection and Immunity | Ammonium chloride (not sodium fluoride) blocked diphtheria toxin action in cultured cells — no direct relevance |

**Assessment**: None of these five papers describe sodium fluoride as a treatment for laryngitis or any related condition. Three are diagnostic ¹⁸F-NaF PET imaging case reports (the likely source of the knowledge-graph confound), one is an unrelated toxicology study, and one does not even study sodium fluoride.

---

## India Market Information

Sodium fluoride is currently **not marketed** in Taiwan (Not marketed), with zero registered licenses. No market authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warning, contraindication, or drug-interaction data is currently available for this compound (data collection pending — see Data Gaps below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predicted indications lack mechanistic plausibility, clinical trial evidence, and therapeutic literature support. The available literature for the top-evidence indication (laryngitis) consists entirely of diagnostic PET-imaging case reports and unrelated toxicology/basic research, strongly suggesting the TxGNN associations are knowledge-graph artifacts driven by ¹⁸F-NaF's role as an imaging radiotracer rather than genuine repurposing signals. Combined with the drug's unregistered status in Taiwan and absent MOA data, there is no basis to advance any of these candidates beyond S0.

**To proceed, the following is needed:**
- TFDA label/warning and contraindication data (currently a Blocking data gap — DG001)
- Confirmed mechanism of action from DrugBank or primary literature (High-severity gap — DG002)
- Investigation into whether TxGNN training data conflates therapeutic sodium fluoride with ¹⁸F-NaF diagnostic radiotracer entries, which appears to be driving spurious high-confidence predictions
- If pursued further, in vitro/preclinical evidence of any antimicrobial or anti-inflammatory activity before any clinical hypothesis is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

