---
layout: default
title: Levobunolol
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Levobunolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
---

# Levobunolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Levobunolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Levobunolol is a non-selective beta-blocker, originally used for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** specific to this indication were found. The closely related open-angle glaucoma entries are supported by **about 20 publications each**, although these mostly confirm the drug's existing use rather than a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (the licence records supplied contain no approved-indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (for primary hereditary glaucoma) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

Two other predictions are also in the data compiled for this report:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Glaucoma 1, open angle | 99.58% | L3 | Proceed with Guardrails |
| Open angle glaucoma | 99.46% | L3 | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, levobunolol is a non-selective beta-adrenergic blocker. It lowers intraocular pressure (IOP) by reducing aqueous humour production. Its efficacy in open-angle glaucoma and ocular hypertension is established, and lowering IOP is plausibly relevant to other glaucoma types.

The high score for primary hereditary glaucoma should be read with caution. The term is likely a broad ontology parent of open-angle glaucoma, so the score may reflect hierarchy propagation rather than independent evidence. It is also unclear whether it refers to congenital or juvenile forms. Beta-blocker use in children carries additional safety considerations.

The two open-angle glaucoma predictions (including the genetic subtype GLC1) are on-label uses of the drug. They confirm existing use rather than represent true repurposing. No evidence specific to a genotype-defined population was identified.

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the three predicted indications.

## Literature Evidence

No literature was found for primary hereditary glaucoma. The table below shows the main publications for the related open-angle glaucoma predictions (up to 10 listed; study types are as classified in the compiled data).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review / network meta-analysis | Ophthalmology | Compares first-line medical treatments for primary open-angle glaucoma and ocular hypertension |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | Long-term study (4 years, randomised, double-masked) | Ophthalmology | 391 patients; IOP fell about 7 mmHg with levobunolol 0.5% and 1% versus timolol 0.5%, with little loss of effect over time |
| [2865710](https://pubmed.ncbi.nlm.nih.gov/2865710/) | 1985 | Long-term double-masked study | Ophthalmology | 391 patients; levobunolol reduced mean IOP by 27% over two years, comparable to timolol |
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | Comparative clinical study | Am J Ophthalmol | 162 patients; no significant difference in IOP reduction between levobunolol and timolol |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Review | Drugs | Levobunolol 0.5–1% reduced IOP by about 30%, superior to placebo and comparable to other beta-blockers |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Review | Med Lett Drugs Ther | Overview of drugs for open-angle glaucoma |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Review | Ann Pharmacother | Compares ocular beta-blockers on systemic adverse effects, tolerability and cost |
| [8123096](https://pubmed.ncbi.nlm.nih.gov/8123096/) | 1993 | Comparative clinical study | J Ocul Pharmacol | Levobunolol versus dipivefrin in 38 African American patients with open-angle glaucoma |
| [2883990](https://pubmed.ncbi.nlm.nih.gov/2883990/) | 1987 | Randomised, double-masked | Br J Ophthalmol | Levobunolol 0.5% versus metipranolol 0.6%; IOP fell about 7 mmHg in both groups |
| [2906644](https://pubmed.ncbi.nlm.nih.gov/2906644/) | 1988 | Randomised, double-masked | J Fr Ophtalmol | 40 patients; levobunolol and timolol showed no proven difference in IOP reduction |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31567 | Biozine 15mg Tablet | Strip of 10 tablets (oral) | Not specified in the data |
| 27221 | Betagan 0.5% Liquifilm | Packet of 5 ml ophthalmic solution | Not specified in the data |

Both registrations are valid single-ingredient products. The ophthalmic solution is the formulation relevant to glaucoma. Whether the oral tablet entry corresponds to levobunolol should be checked, since it is not an ophthalmic route.

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text)**: asthma (including intrinsic and allergic asthma), diabetes mellitus, diabetic ketoacidosis, myasthenia gravis and related neuromuscular junction disease, atrioventricular block, pulmonary emphysema, and anaphylaxis. Systemic beta-blocker precautions such as bradycardia and decompensated heart failure should also be considered.
- **Drug Interactions**: 24 interactions were recorded, none with a graded severity. Examples include omeprazole, pantoprazole, lansoprazole, warfarin, clopidogrel, prednisone, ibuprofen and tacrolimus. Interactions with oral beta-blockers and calcium channel blockers are of particular concern.
- **Paediatric use**: if "primary hereditary glaucoma" includes congenital or juvenile forms, beta-blocker use in children needs additional safety consideration.

Please refer to the package insert for label warnings, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold** (primary hereditary glaucoma)

**Rationale:**
The primary prediction is supported only by a model score. There are no trials or literature, and the score may reflect ontology hierarchy rather than independent evidence. The related open-angle glaucoma predictions are supported by a substantial body of comparative studies. They merit "Proceed with Guardrails", but they are on-label uses rather than repurposing.

**To proceed, the following is needed:**
- A clear definition of "primary hereditary glaucoma" (adult-onset versus congenital or juvenile) and a search for indication-specific evidence
- Paediatric safety data if congenital or juvenile forms are in scope
- Package insert warnings and contraindications from the India Pharma source
- Mechanism of action data from DrugBank
- Verification of study designs for the older comparative studies, which could support a higher evidence level
- Clarification of the oral tablet registration (Biozine 15mg) and its approved indication
- A safety monitoring plan for patients with respiratory, cardiac or diabetic comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

