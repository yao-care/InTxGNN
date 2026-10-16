---
layout: default
title: Ripasudil
parent: Model Prediction Only (L5)
nav_order: 744
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ripasudil: predicted new indication Hyperprolactinemia (disease) (evidence level L5). Approved use: Ocular hypertension"
monitor_inn: "Ripasudil"
predicted_indications: ["hyperprolactinemia (disease)", "Axenfeld anomaly", "hydrophthalmos", "glaucoma 3, primary infantile, B", "familial hyperprolactinemia", "dense granule disease", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "thrombocytopenia"]
---

# Ripasudil
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

# Ripasudil: From Ocular Hypertension and Glaucoma to Hyperprolactinemia

## One-Sentence Summary

Ripasudil is a Rho kinase (ROCK) inhibitor originally used to treat glaucoma and ocular hypertension.
The TxGNN model ranks **hyperprolactinemia** as its top predicted new indication, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.
The ophthalmic predictions (Axenfeld anomaly, hydrophthalmos, primary infantile glaucoma) are mechanistically more plausible and are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular hypertension; glaucoma |
| Predicted New Indication | Hyperprolactinemia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, ripasudil inhibits ROCK1 and ROCK2 (and also shows pharmacological activity at PRKACA, the catalytic subunit of cAMP-dependent protein kinase). It lowers intraocular pressure by increasing outflow through the trabecular meshwork.

For the top prediction, hyperprolactinemia, **no clear mechanistic link was identified**. A connection through dopaminergic or pituitary signalling is speculative and not supported by the data. The high score most likely reflects knowledge-graph proximity rather than a demonstrated biological relationship. Familial hyperprolactinemia (rank 5) has the same weakness.

Other predictions are more biologically coherent:

- **Ophthalmic conditions (Axenfeld anomaly, hydrophthalmos, primary infantile glaucoma 3B):** These involve raised intraocular pressure, the same pathway targeted by the approved indication. The IOP-lowering mechanism is plausible, though paediatric safety and efficacy are not established, and surgery remains the standard of care for congenital forms.
- **Platelet disorders (dense granule disease, macrothrombocytopenia with mitral valve insufficiency, hereditary thrombocytopenia, transient neonatal thrombocytopenia, thrombocytopenia):** Rho/ROCK signalling affects platelet and megakaryocyte cytoskeletal function, so a theoretical link exists. ROCK inhibition might also worsen platelet function, which is a safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature exists only for lower-ranked predictions, not for hyperprolactinemia. It is indirect and does not test ripasudil in the predicted disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42774983](https://pubmed.ncbi.nlm.nih.gov/42774983/) | 2026 | Case report | Cureus | Asymmetric bilateral Axenfeld-Rieger anomaly misdiagnosed as unilateral iridocorneal endothelial syndrome; a diagnostic report that does not test ripasudil (relevant to the Axenfeld anomaly prediction) |
| [40189910](https://pubmed.ncbi.nlm.nih.gov/40189910/) | 2025 | Preclinical/in vitro | Virulence | Approved Src and ROCK inhibitors, including ripasudil and netarsudil, reduced dengue virus serotype 2-induced endothelial permeability in vitro (relevant to the thrombocytopenia prediction) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 184379 | Ripatec Eye Drop (Ajanta Pharma Ltd) | Bottle of 5 ml eye drop | Not specified in the data compiled for this report |

Ripasudil is available in India only as an ophthalmic preparation. This suits the ophthalmic predictions but not systemic conditions such as hyperprolactinemia or platelet disorders, for which route compatibility has not been assessed.

## Safety Considerations

**Drug Interactions / Pharmacological Targets:** The interaction query identified three pharmacological target interactions rather than drug-drug interactions:

- ROCK1 (Rho associated coiled-coil containing protein kinase 1)
- ROCK2 (Rho associated coiled-coil containing protein kinase 2)
- PRKACA (protein kinase, cAMP-dependent, catalytic, alpha subunit)

Because ROCK signalling is involved in platelet function, any use in platelet disorders would need particular safety attention. Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperprolactinemia, has no trials, no literature, and no supportable mechanistic rationale, so it is a model prediction only (L5). The ophthalmic predictions (Axenfeld anomaly, hydrophthalmos, primary infantile glaucoma 3B) are better framed as research questions because they share the IOP-lowering mechanism of the approved indication, but they also lack direct evidence.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications for Ripatec Eye Drop, which block safety screening
- Direct preclinical or clinical evidence testing ripasudil in the predicted disease; for hyperprolactinemia, a plausible biological pathway first
- For the ophthalmic candidates, paediatric safety and efficacy data and a comparison against standard surgical care
- Route-of-administration compatibility assessment, since only an ophthalmic formulation is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

