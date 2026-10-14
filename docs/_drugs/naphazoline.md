---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Ocular Redness Relief to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is a topical alpha-adrenergic vasoconstrictor, marketed in India as an eye drop that temporarily reduces eye redness.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Temporary relief of eye redness (vasoconstrictor eye drop). The licence records contain no approved indication text; this is taken from pharmacology data compiled for this report. |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Pharmacology records show that naphazoline binds alpha-1A, alpha-2A and alpha-2C adrenoceptors. It is a vasoconstrictor that narrows swollen blood vessels in the eye.

**The prediction is not mechanistically supported.** Hypotrichosis simplex of the scalp is a genetic disorder of hair development. A vasoconstrictor has no known way to change its underlying pathology. If anything, constricting scalp vessels could reduce follicle perfusion.

The high TxGNN score appears to reflect graph-based proximity rather than a real biological link. Supporting this view, the other top-ranked predictions include both hair-loss conditions (congenital hypotrichosis, alopecia areata, alopecia) and hair-overgrowth conditions (hypertrichosis). They also include unrelated congenital malformation syndromes. These predictions contradict one another, which suggests nonspecific scoring.

The one prediction with some ophthalmic plausibility is open-angle glaucoma. Alpha-agonists such as brimonidine lower intraocular pressure. Naphazoline is not an established IOP-lowering agent, however, and the retrieved paper does not study it.

## Literature Evidence

For the lead prediction, hypotrichosis simplex of the scalp, no related literature is currently available.

The only paper retrieved for any top-ranked prediction concerns a different drug class:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) | 1992 | Other (laser/corticosteroid study) | Aust N Z J Ophthalmol | Compared topical steroids and a non-steroid medication after argon laser trabeculoplasty for peripheral anterior synechiae and IOP. It does not study naphazoline and was retrieved for open-angle glaucoma (rank 8), not the lead prediction. |

## Clinical Trial Evidence

Currently no related clinical trials are registered for hypotrichosis simplex of the scalp, or for any of the other top 10 predicted indications.

## India Market Information

Naphazoline has 20 valid single-ingredient registrations and no combination or cancelled registrations. All are ophthalmic products. The records contain no approved indication text. The five main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 164326 | Opti Zee Eye Drop | Packet of 10 ml eye drop | Not stated |
| 151757 | Nefcoz Eye Drop | Bottle of 10 ml eye drop | Not stated |
| 162589 | Optizee Plus Eye Drop | Packet of 10 ml eye drop | Not stated |
| 156983 | Nizoline Z Eye Drop | Packet of 5 ml eye drop | Not stated |
| 137052 | Mil Eye Drop | Packet of 10 ml eye drop | Not stated |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** The TxGNN knowledge graph links naphazoline to caution in these conditions:
  - hypertension and other cardiovascular or heart disease
  - hyperglycaemia, diabetes mellitus and diabetic ketoacidosis
  - angle-closure glaucoma
  - hyperthyroidism, Graves disease and thyrotoxicosis
  - eye infections and conjunctivitis
- **Glaucoma concern:** Sympathomimetic vasoconstrictors can cause mydriasis and are used cautiously in narrow-angle glaucoma. This matters for the glaucoma-related predictions (primary hereditary glaucoma and open-angle glaucoma).
- **Drug interactions:** No drug-drug interactions were identified. The compiled data lists only pharmacological targets: alpha-1A, alpha-2A and alpha-2C adrenoceptors in humans, and the Taar4 gene in mouse.

Package insert warnings and contraindications could not be obtained, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature. It also has no plausible mechanism, and vasoconstriction could be counterproductive for hair follicles. The drug is marketed in India only as an ophthalmic product, and the available safety data are limited to knowledge-graph associations.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory records (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that an alpha-adrenergic agonist can affect hair follicle biology
- Route compatibility assessment, since only ophthalmic products are marketed and any scalp use would need a new formulation
- If the project is redirected, a targeted literature search on alpha-agonists and intraocular pressure, with attention to the angle-closure risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

