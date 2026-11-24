---
layout: default
title: Fluorometholone
parent: Model Prediction Only (L5)
nav_order: 365
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Fluorometholone: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Uveitis and related ocular inflammatory conditions (iritis…"
monitor_inn: "Fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
---

# Fluorometholone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for fluorometholone: "Corticosteroids inhibit the inflammatory response to a variety of inciting agents and probably delay or slow healing. They inhibit the edema, fibrin deposition, capillary dilation, leukocyte migration, capillary proliferation, fibroblast proliferation, deposition of collagen, and scar formation associated with inflammation. […] In clinical studies of documented steroid-responders, fluorometholone demonstrated a significantly longer average time to produce a rise in intraocular pressure than dexamethasone phosphate; however, in a small percentage of individuals, a significant rise in intraocular pressure occurred within one week." ([DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01), label version 2026-08-12; accessed 2026-11-19.) Based on known information, fluorometholone is a synthetic glucocorticoid that acts on the glucocorticoid receptor (NR3C1). Its efficacy in ocular inflammation is established, and mechanistically it may be applicable to immune-mediated inflammation elsewhere.

In theory, a glucocorticoid could suppress immune-mediated vasculitis. However, fluorometholone is formulated as a topical eye drop with minimal systemic exposure, so it is unlikely to reach concentrations relevant to a systemic vascular disease. The high score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions of note.** The other nine predictions have no clinical trial support either. Three are close to the existing ocular indications and are better framed as research questions:
- **Glaucomatocyclitic crisis** (score 0.9982): a recurrent anterior uveitis-like condition with raised intraocular pressure, where fluorometholone's lower IOP risk is relevant.
- **Punctate epithelial keratoconjunctivitis** (score 0.9989): the only prediction with any retrieved literature. It is the only one rated L4, but the two papers are indirect.

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

Twenty single-ingredient registrations are valid, and none are cancelled. All are ophthalmic eye drops or suspensions (5 ml packs). The data compiled for this report do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 84104 | FML Liquifilm | Packet of 5 ml Opthalmic Suspension | Valid |
| 84883 | Flosoft Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 85343 | Flotrust Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 85950 | Flosight Eye Drop | Bottle of 5 ml Opthalmic Suspension | Valid |
| 86084 | Flurocot Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 86269 | Flacox 0.1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 86373 | Floress Eye Drop | Bottle of 5 ml Opthalmic Suspension | Valid |
| 86694 | Fluroace Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 86808 | FM 1 Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 87038 | Fluster Eye Drop | Bottle of 5 ml Opthalmic Suspension | Valid |
| 87381 | F Lone 0.1% Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 87649 | Flosef Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 88223 | Flumace Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 89900 | FMN Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 90124 | Flurowyn 0.1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 90262 | Flumetha 0.1% Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 90508 | Fluvilone Eye Drop | Bottle of 5 ml Opthalmic Suspension | Valid |
| 131546 | Lowin Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 151524 | New Biflace Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 236010 | Veflu Eye Drop | Bottle of 5 ml Ophthalmic Solution | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

