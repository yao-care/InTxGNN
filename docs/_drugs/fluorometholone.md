---
layout: default
title: Fluorometholone
parent: Model Prediction Only (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorometholone: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Uveitis and related ocular inflammatory conditions (iritis…"
monitor_inn: "Fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis", "lens-induced iridocyclitis"]
---

# Fluorometholone
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

## Fluorometholone: From Uveitis and Ocular Surface Inflammation to Postinfectious Vasculitis
{: .text-alpha }

## One-Sentence Summary

Fluorometholone is a topical ophthalmic corticosteroid, originally used for uveitis, iritis, iridocyclitis, allergic and vernal conjunctivitis, and corneal ulcer.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uveitis and related ocular inflammatory conditions (iritis, iridocyclitis, atopic/vernal conjunctivitis, corneal ulcer) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluorometholone is a synthetic glucocorticoid that acts on the glucocorticoid receptor (NR3C1). Its efficacy in ocular inflammation is established, and mechanistically it may be applicable to immune-mediated inflammation elsewhere.

In theory, a glucocorticoid could suppress immune-mediated vasculitis. However, fluorometholone is formulated as a topical eye drop with minimal systemic exposure, so it is unlikely to reach concentrations relevant to a systemic vascular disease. The high graph score therefore reflects a computational association rather than a demonstrated clinical rationale.

**Other predictions of note.** The other nine predictions have no clinical trial support either. Three are close to the existing ocular indications and are better framed as research questions:
- **Glaucomatocyclitic crisis** (score 99.82%): a recurrent anterior uveitis-like condition with raised intraocular pressure, where fluorometholone's lower IOP risk is relevant.
- **Lens-induced iridocyclitis** (score 99.82%): anterior segment inflammation that arguably falls within the existing indication class.
- **Punctate epithelial keratoconjunctivitis** (score 98.89%): the only prediction with any retrieved literature. It is the only one rated L4, but the two papers are indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for postinfectious vasculitis. The only literature retrieved across the predictions relates to punctate epithelial keratoconjunctivitis (rank 6), and it is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Review | Indian Journal of Ophthalmology | Characterises the sequelae of microsporidial keratoconjunctivitis and outlines its management |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Cohort | Journal of Current Ophthalmology | Uses anterior segment OCT to describe the phases of epidemic keratoconjunctivitis and the effect of topical steroid on its course |

Neither paper appears to test fluorometholone specifically.

## India Market Information

Twenty single-ingredient registrations are valid, and none are cancelled. All are ophthalmic eye drops or suspensions (5 ml packs). The data compiled for this report do not include approved indication text. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84104 | FML Liquifilm (Allergan India) | Ophthalmic suspension, 5 ml | Not listed |
| 84883 | Flosoft Eye Drop (Cipla) | Eye drop, 5 ml bottle | Not listed |
| 87649 | Flosef Eye Drop (Sun Pharmaceutical) | Eye drop, 5 ml | Not listed |
| 88223 | Flumace Eye Drop (Micro Labs) | Eye drop, 5 ml | Not listed |
| 151524 | New Biflace Eye Drop (Alembic) | Eye drop, 5 ml bottle | Not listed |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Fluorometholone is flagged against several conditions, notably eye infections (herpes simplex keratitis, fungal and viral eye infections, ocular tuberculosis), open-angle glaucoma and ocular hypertension, diabetes mellitus and diabetic ketoacidosis, and porphyria. This matters for the infectious keratoconjunctivitis prediction, since corticosteroids can worsen infectious keratitis.
- **Drug Interactions**: Twelve interaction records were found. Eleven are listed without a severity level: doxycycline, salbutamol, cyclosporine, acetaminophen, digoxin, brimonidine, cephalexin, alendronic acid, acyclovir, diazepam and fenofibrate. The twelfth is the pharmacological target record, the glucocorticoid receptor.

Please refer to the package insert for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for postinfectious vasculitis rests only on a model score. There are no trials or publications, and a topical eye drop has little systemic exposure. The ocular-adjacent predictions (glaucomatocyclitic crisis, lens-induced iridocyclitis, punctate epithelial keratoconjunctivitis) are more credible but also lack direct evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products
- Detailed mechanism of action data
- Direct clinical or literature evidence for fluorometholone in the predicted condition
- A route and formulation assessment, because the topical ophthalmic form may not suit a systemic vascular disease
- Consideration of prioritising the ocular-adjacent predictions as research questions, with intraocular pressure monitoring and infection screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

