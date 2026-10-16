---
layout: default
title: Becaplermin
parent: Model Prediction Only (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Becaplermin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the India licence record"
---

# Becaplermin
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

# Becaplermin: From Diabetic Foot Ulcer Wound Healing to Amenorrhea

## One-Sentence Summary

Becaplermin is a recombinant human platelet-derived growth factor (PDGF-BB) applied topically as a gel to promote wound healing, and it is marketed in India.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials** and **no directly relevant publications** currently support this prediction.
The prediction rests on graph-based modelling alone and has no plausible biological support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence record; the literature describes topical treatment of diabetic neuropathic foot ulcers and pressure ulcers |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled drug record. From general knowledge, becaplermin is recombinant human PDGF-BB. It acts on PDGF receptors alpha and beta to drive fibroblast and smooth muscle proliferation, granulation tissue formation and angiogenesis. This is the basis of its use in chronic skin wounds.

For amenorrhea, no plausible mechanistic link has been established. Amenorrhea generally involves the hypothalamic-pituitary-ovarian axis or endometrial function, and PDGF-BB wound-healing biology does not obviously act on either. The high TxGNN score is a graph-based association and should not be read as evidence of benefit.

The other top predictions fall into similar groups, and none has supporting trials:
- **Breast cancers (several subtypes):** PDGFR agonism would be expected to promote tumour stroma and angiogenesis, so the biological rationale points the wrong way.
- **Pulmonary hypertension:** PDGF drives pulmonary vascular remodelling, and PDGFR inhibitors have been studied instead. An agonist would likely worsen the disease.
- **Erectile dysfunction, hypogonadotropic hypogonadism and Leydig cell hypoplasia:** Any link is indirect or loose, and none is supported by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature addresses amenorrhea. The only publications linked to any predicted indication were attached to "breast tumor luminal A or B". They all concern becaplermin in diabetic foot ulcers and wound healing, so they are off-topic for the predicted indication and serve only as background on the approved topical use.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20486728](https://pubmed.ncbi.nlm.nih.gov/20486728/) | 2010 | Review | Drug Safety | Benefit-risk assessment: RCTs show increased healing rates of neuropathic diabetic foot ulcers |
| [11849120](https://pubmed.ncbi.nlm.nih.gov/11849120/) | 2002 | Review | Expert Opin Biol Ther | Becaplermin as a recombinant PDGF treatment for healing diabetic foot ulcers |
| [18031145](https://pubmed.ncbi.nlm.nih.gov/18031145/) | 1999 | Review | BioDrugs | Topical rh-PDGF-BB promotes wound healing in diabetic neuropathic and pressure ulcers |
| [37894789](https://pubmed.ncbi.nlm.nih.gov/37894789/) | 2023 | Review | Int J Mol Sci | Becaplermin gel remains the only FDA-approved wound healing therapeutic after more than 25 years |
| [41220237](https://pubmed.ncbi.nlm.nih.gov/41220237/) | 2025 | Clinical safety study | Wound Repair Regen | Safety of up to 140 daily topical applications of rhPDGF-BB onto skin wounds |
| [17628536](https://pubmed.ncbi.nlm.nih.gov/17628536/) | 2007 | Preclinical | Eur J Pharmacol | PL 14736 compared with PDGF-BB for granulation tissue formation in rat wound models |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 174121 | Plermin Gel (Dr Reddy's Laboratories Ltd) | Tube of 7.5 gm gel (topical) | Not stated in the licence record |

---

## Safety Considerations

- **Oncologic concern:** Becaplermin carried a boxed warning for malignancy earlier in its label history. It was later removed, but caution continues. As a PDGFR agonist, it carries a theoretical risk of promoting tumour growth, which is especially relevant to the breast cancer predictions.
- **Fibrosis:** Systemic or local PDGF-BB exposure could theoretically promote fibrosis, which is relevant to the erectile dysfunction prediction.
- **Route:** The only registered product is a topical gel. Whether it could reach tissues relevant to the predicted indications has not been assessed.

Package insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score, with no clinical trials and no relevant literature. The known PDGFR agonist biology offers no mechanistic link to amenorrhea, and for several other top predictions (breast cancers, pulmonary hypertension) it points in the opposite direction.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed product
- Detailed mechanism of action data
- Preclinical or mechanistic evidence linking PDGF-BB to reproductive-axis or endometrial function
- Assessment of route compatibility, since the approved product is topical
- A formal safety review of the theoretical oncologic and fibrosis risks before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

