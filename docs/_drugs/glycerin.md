---
layout: default
title: Glycerin
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Glycerin"
predicted_indications: ["cauda equina syndrome", "open-angle glaucoma", "primary hereditary glaucoma", "alopecia", "congenital hypotrichosis milia", "irritable bowel syndrome", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "migraine disorder", "migraine with brainstem aura"]
description: "Glycerin: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Glycerin
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

## Glycerin: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Glycerin is an osmotic agent, originally used to treat constipation.
The TxGNN model's top-ranked prediction is **cauda equina syndrome**, but **no clinical trials and no publications** currently support it.
The best-supported alternative among the top 10 predictions is **open-angle glaucoma**, which has only indirect, low-level literature (3 publications, none showing efficacy).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycerin is a hyperosmotic agent. Its efficacy in constipation is established, as it draws water into the bowel lumen.

For cauda equina syndrome, no mechanistic link has been identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no supporting clinical or literature evidence, so the prediction should be treated as a hypothesis only.

Other predictions in the top 10 are also weak:
- **Open-angle glaucoma (0.9959, L4):** Oral glycerin has a historical role as a hyperosmotic agent that lowers intraocular pressure, which gives a plausible indirect rationale. However, it was used mainly for acute angle-closure episodes rather than chronic open-angle glaucoma. The retrieved papers address closed-angle glaucoma pathogenesis, glycerin-preserved corneoscleral grafts, and osmoprotection in dry eye, and none supports efficacy.
- **Irritable bowel syndrome (0.9949, L4):** Glycerin's osmotic laxative action gives indirect relevance to constipation-predominant IBS. The literature is weak, a 1964 commentary and an unrelated nanoemulsion paper.
- **Alopecia, hypotrichosis and alopecia areata variants, migraine and migraine with brainstem aura, primary hereditary glaucoma:** prediction only, with no credible mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome or for any of the other top 10 predicted indications.

## Literature Evidence

No literature is available for cauda equina syndrome. The table below lists the most relevant retrieved publications for the next-ranked predictions. None demonstrates a therapeutic effect of glycerin in the predicted condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1614157](https://pubmed.ncbi.nlm.nih.gov/1614157/) | 1992 | Review | Klin Monatsbl Augenheilkd | Pathogenesis and treatment of primary closed-angle glaucoma (not open-angle) |
| [32890110](https://pubmed.ncbi.nlm.nih.gov/32890110/) | 2020 | Case series | J Glaucoma | Glycerin-preserved donor corneoscleral patch grafts are safe and effective for glaucoma drainage devices (tissue preservation use) |
| [20872359](https://pubmed.ncbi.nlm.nih.gov/20872359/) | 2011 | Clinical study | Eur J Ophthalmol | Osmoprotective artificial tears and ocular surface damage in glaucoma patients on topical therapy |
| [14215532](https://pubmed.ncbi.nlm.nih.gov/14215532/) | 1964 | Review/commentary | JAMA | "Irritable colon" clinical commentary (no abstract) |
| [3896179](https://pubmed.ncbi.nlm.nih.gov/3896179/) | 1985 | Double-blind RCT | Arch Intern Med | Polysorbate 60 was ineffective in male pattern baldness; glycerin served as the control |
| [14555416](https://pubmed.ncbi.nlm.nih.gov/14555416/) | 2003 | Safety review | Int J Toxicol | Safety assessment of triacetin (glyceryl triacetate), a different compound |

## India Market Information

Glycerin has 20 valid single-ingredient registrations, all injectable or infusion products. Approved indication text is not recorded for these registrations. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 154076 | Newtol 100ml Infusion | Bottle of 100 ml infusion | Not specified |
| 144415 | Megtil 10gm/10gm Infusion | Bottle of 100 ml infusion | Not specified |
| 38730 | Chemitol Injection | Bottle of 100 ml injection | Not specified |
| 99961 | Glycerim 10gm/10gm Infusion | Bottle of 100 ml infusion | Not specified |
| 98270 | Grapitol G 10mg/10mg Infusion | Vial of 100 ml infusion | Not specified |

## Safety Considerations

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for safety information.

**Drug Interactions:** The interaction screen identified 220 potential interacting drugs. The list available here includes mostly moderate-level interactions, for example:
- Abiraterone, tramadol, acetazolamide, hydrocortisone, salbutamol
- Alfuzosin, hydrochlorothiazide, amiloride, amiodarone, amisulpride
- Benazepril, anagrelide, propofol, apalutamide, apomorphine
- Triamcinolone, arsenic trioxide, lumefantrine, asenapine

Doxycycline is the one listed minor interaction. Clinical significance should be checked for each specific combination.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, cauda equina syndrome, rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials, no literature, and no mechanistic link. Even the more plausible candidates (open-angle glaucoma, IBS) lack supporting efficacy evidence. The India market is well established, but the registered products are all injectable or infusion forms and have no recorded indication text.

**To proceed, the following is needed:**
- Mechanism of action data for glycerin
- Package insert warnings and contraindications for the Indian products
- A defined mechanistic hypothesis and preclinical or clinical evidence for any selected indication, with glaucoma (IOP lowering) as the most plausible starting point
- Confirmation that the registered injectable and infusion routes are compatible with the intended use, since route compatibility has not been assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

