---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 874
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration records"
---

# Tyrosine
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

# Tyrosine: From Thyroid Hormone Replacement Products to Cauda Equina Syndrome

## One-Sentence Summary

The data compiled for this report list tyrosine (DrugBank DB00135) under 20 valid single-ingredient Indian registrations, most of them thyroid hormone tablets. The registration records contain no approved-indication text, so the original indication cannot be confirmed from them. The TxGNN model predicts **cauda equina syndrome** as the top new indication, but **no clinical trials and no relevant publications** support it. This is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is an amino acid and a precursor of catecholamines (dopamine, norepinephrine) and of thyroid hormones, but the data compiled for this report do not describe a mechanism for any specific therapeutic use.

Cauda equina syndrome is a compressive disorder of the lumbosacral nerve roots. No plausible pathway links tyrosine supplementation to this condition, and there are no trials or literature. The high score (rank 3450) should be treated as a model output that has not been validated.

Other predictions in the list have a somewhat stronger biological connection, but none has supporting efficacy data:

- **Hyperthyroidism and hyperthyroxinemia:** Tyrosine is a structural precursor of thyroid hormones. Giving more substrate would not be expected to treat excess hormone, and could theoretically be counterproductive.
- **Postural orthostatic tachycardia syndrome:** Catecholamine involvement is plausible. The only evidence is a case report of alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor, which acts in the opposite direction to tyrosine.
- **Resistance to thyroid hormone (receptor beta mutation):** This is a receptor-level defect, so more precursor would not be expected to correct it.
- **Glaucoma subtypes and aqueous misdirection:** No therapeutic link to tyrosine is shown.
- **Obsolete neurogenic bladder:** Catecholamines play a role in bladder control in principle, but there are no data, and the disease term is obsolete.

---

## Clinical Trial Evidence

No trials are registered for the top-ranked indication, cauda equina syndrome. Among the other predictions, only one trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | NA | Not yet recruiting | 150 | Zinc, selenium and L-tyrosine supplement versus placebo for preventing thyrotoxicosis in adults with elevated TPOAb and the SEPP1 r25191G/A polymorphism (for hyperthyroidism, rank 4). This tests a combination, so tyrosine's contribution cannot be isolated, and no efficacy data exist. |

---

## Literature Evidence

No literature was found for cauda equina syndrome. The table below shows the most relevant papers retrieved for other predicted indications. None evaluates tyrosine as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome case with a positive response to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor (linked to POTS). It acts opposite to tyrosine. |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | Plasma amino acid alterations in early primary angle-closure glaucoma. This is an association only, not a treatment effect. |
| [27758063](https://pubmed.ncbi.nlm.nih.gov/27758063/) | 2017 | Cohort | Clin Exp Ophthalmol | Serum autoantibodies after acute angle-closure glaucoma attack. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma etiopathogenesis and treatment, centered on VEGF inhibition. |
| [15135777](https://pubmed.ncbi.nlm.nih.gov/15135777/) | 2004 | Review | Growth Horm IGF Res | Molecular mechanisms of end-organ hormone resistance. |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Preclinical | Endocrinology | Three novel thyroid hormone receptor beta mutations (S314) impairing ligand binding in resistance to thyroid hormone. |
| [19169471](https://pubmed.ncbi.nlm.nih.gov/19169471/) | 2008 | Case report | Arq Bras Endocrinol Metabol | E449X thyroid hormone receptor beta mutation with autoimmune thyroid disease and neuropsychomotor involvement. |
| [22644448](https://pubmed.ncbi.nlm.nih.gov/22644448/) | 2012 | Review | Jpn J Ophthalmol | General review of retinal remodeling (linked to traumatic glaucoma). |

---

## India Market Information

There are 20 valid single-ingredient registrations and no cancelled ones. The registration records contain no approved-indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 106750 | Hormonorm 25mcg Tablet | Bottle of 100 tablets | Not stated |
| 73934 | Euthyrox 12.5mcg Tablet | Bottle of 100 tablets | Not stated |
| 216173 | Thyronorm 50mcg Tablet | Bottle of 30 tablets | Not stated |
| 216209 | Thyrocip 100 Tablet | Bottle of 120 tablets | Not stated |
| 122253 | Lethyrox 100 Tablet | Bottle of 100 tablets | Not stated |

All products are oral tablets.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available in the data compiled for this report, and the knowledge-graph contraindication list is empty.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, cauda equina syndrome, has a high model score but no trials, no literature, and no plausible mechanism. The same is true of the other nine predictions. The only trial found tests a multi-component supplement and has not started recruiting. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products, which are a blocking gap for safety screening
- Confirmed original indication and mechanism of action data (for example from DrugBank)
- A mechanistic rationale or preclinical evidence linking tyrosine to the proposed indication
- Results from NCT06264544, with analysis separating tyrosine's effect from the other components, if the hyperthyroidism direction is pursued
- Route and formulation compatibility assessment for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

