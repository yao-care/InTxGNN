---
layout: default
title: Hydrocortisone
parent: Model Prediction Only (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydrocortisone: predicted new indication Alopecia areata (evidence level L5). Approved use: Adrenocortical insufficiency / Addison disease, autoimmune disease…"
---

# Hydrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Hydrocortisone: From Autoimmune and Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid originally used for adrenocortical insufficiency, autoimmune and inflammatory diseases (such as Crohn disease), and certain leukemias.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **1 clinical trial** (Phase 3) and **20 publications** retrieved, but most of these are old or low-relevance reports. Hydrocortisone served as a low-potency comparator in the key trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical insufficiency / Addison disease, autoimmune disease, Crohn disease and inflammatory bowel disease, acute lymphoblastic leukemia, and others (approved indication text was not provided in the India licence records) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 per the underlying scoring (see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (research question) |

*Note on evidence level:* The scoring assigns L1, but only one completed Phase 3 trial was found, and it used hydrocortisone as the comparator rather than the test therapy. By the stated rules (≥2 completed Phase 3 RCTs), the evidence is closer to L2 at best, and it does not show hydrocortisone-specific efficacy.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone is a glucocorticoid with anti-inflammatory and immunosuppressive effects. Its use in autoimmune and inflammatory diseases is established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is a T-cell-mediated autoimmune disease in which the immune system attacks hair follicles. Local glucocorticoid action could plausibly suppress the immune infiltrate around follicles, which links to hydrocortisone's original autoimmune and inflammatory uses.

There is an important caveat. Hydrocortisone is a low-potency steroid. In the one randomized trial, it was the comparator for the higher-potency clobetasol. The evidence therefore supports a steroid class effect more than hydrocortisone-specific efficacy. Older reports (1950s–1970s) describe hair regrowth after intralesional hydrocortisone injections, but these are historical and of low methodological quality.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Clobetasol propionate 0.05% cream vs hydrocortisone 1% cream in children with alopecia areata. Hydrocortisone was the low-potency comparator, and the trial was framed around clobetasol's advantage. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Clobetasol 0.05% vs hydrocortisone 1% for alopecia areata in children; the publication focuses on clobetasol's advantage. |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review | J Med Soc New Jersey | Clinical overview of alopecia areata and other common scalp problems. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Historical clinical report | Medical Times | Treatment of alopecia areata with cortisone, hydrocortisone and their analogs. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Historical clinical report | Der Hautarzt | Hair growth after intracutaneous hydrocortisone injection in alopecia areata. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | J Am Acad Dermatol | Four cases of congenital alopecia areata treated with minoxidil and topical agents. |

The remaining retrieved publications are mostly historical non-English reports or low-relevance papers (veterinary, preclinical mouse, survey, or unrelated case reports).

## India Market Information

Hydrocortisone has 20 valid single-ingredient registrations in India. The approved indication text was not provided in the registration records. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 113711 | Irap 100mg Injection | Vial of 1 injection | Not stated |
| 52816 | Criticort Injection | Vial of 1 injection | Not stated |
| 174259 | Primacort 200mg Injection | Vial of 5 ml injection | Not stated |
| 103759 | Hisone 5 Tablet | Strip of 10 tablets | Not stated |
| 104991 | HC-Cort 20 Tablet | Strip of 10 tablets | Not stated |

Most registered products are injectable. Two are oral tablets. No topical formulation appears among the registrations, and the pivotal alopecia areata trial used a topical cream, so the route would need to be addressed.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension, epilepsy, gastric ulcer, kidney disease, liver disease, hyperglycemia, herpes simplex virus keratitis, measles, and anogenital or common warts, among others. Various pituitary deficiency conditions are also listed.
- **Drug Interactions:** 722 interactions were identified. Examples include **adalimumab (Major)**, and Moderate-level interactions with ketorolac, ibuprofen, nifedipine, ethinylestradiol, acetazolamide, isotretinoin, and zidovudine. Interactions with antidiabetic agents (acarbose, acetohexamide, albiglutide) are also listed. Live or inactivated vaccine antigens appear as Moderate. Minor interactions include formoterol and salbutamol.
- **Hair-related note:** For telogen effluvium (a lower-ranked prediction), systemic glucocorticoid exposure can itself contribute to hair shedding.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The only Phase 3 trial used hydrocortisone as a weak comparator, and the literature is mostly historical or low-quality. This supports a steroid class effect for alopecia areata but does not show hydrocortisone-specific efficacy. Higher-potency steroids and other established options are likely more appropriate. The other predicted indications (alopecia mucinosa, telogen effluvium, folliculitis decalvans, and others) have no supporting hydrocortisone-specific evidence and rest on model prediction alone.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently missing and blocking safety screening)
- Mechanism of action data for hydrocortisone
- Head-to-head or placebo-controlled trials showing hydrocortisone-specific efficacy in alopecia areata
- Clarification of route and formulation (topical or intralesional), since the registered products are mainly injectable or oral
- A review of the approved indications for the registered Indian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

