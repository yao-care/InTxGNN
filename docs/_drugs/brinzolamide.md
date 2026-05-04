---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 1
---

# Brinzolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase inhibitor (CAI) primarily used to lower intraocular pressure (IOP) in patients with open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with **0 clinical trials** and **0 publications** currently registered specifically for this indication.
The mechanistic rationale is exceptionally strong — this prediction represents a direct subtype expansion within the same therapeutic target rather than conventional drug repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (inferred from mechanism; formal indication data unavailable) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brinzolamide is a carbonic anhydrase inhibitor that acts by blocking carbonic anhydrase II (CA2) and carbonic anhydrase XII (CA12) in the ciliary body of the eye. This blockade suppresses bicarbonate (HCO₃⁻) production, which in turn reduces aqueous humor secretion and lowers intraocular pressure (IOP) — the central mechanism by which the drug exerts its therapeutic effect.

Primary hereditary glaucoma encompasses genetically defined subtypes of glaucoma associated with mutations in genes such as *CYP1B1*, *MYOC*, and *LTBP2*. Regardless of the underlying genetic variant, these conditions share the same core pathological cascade: abnormally elevated IOP → mechanical compression of the optic nerve → progressive retinal ganglion cell apoptosis and irreversible vision loss. Brinzolamide's IOP-reducing mechanism directly addresses this shared pathophysiology.

This TxGNN prediction is therefore best understood as a **subtype expansion within the same therapeutic category** rather than classical drug repurposing. The drug already acts on the same biological target and disease pathway; the question is whether established efficacy in sporadic open-angle glaucoma extends to genetically determined forms. The mechanistic confidence is rated **High** by the TxGNN analysis, and the prediction score of 99.48% reflects this direct mechanistic alignment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Brinzolamide has **no registered products** in the India market (0 authorizations on record). The drug is currently classified as **not marketed** in India.

---

## Safety Considerations

**Drug Interactions (32 interactions identified; all rated "Unknown" severity):**

Brinzolamide has 32 drug interactions on record in the DDInter database. All are currently classified as "Unknown" severity, meaning clinical significance has not yet been formally characterized. Key co-medications flagged include:

| Drug Class | Interacting Drugs |
|-----------|------------------|
| Proton pump inhibitors | Pantoprazole, Omeprazole, Lansoprazole |
| Corticosteroids | Triamcinolone, Prednisone, Prednisolone, Dexamethasone |
| Statins | Simvastatin, Rosuvastatin |
| Anticoagulants / Antiplatelets | Warfarin, Clopidogrel |
| Antihistamines | Cetirizine, Fexofenadine |
| H2 blockers | Ranitidine, Famotidine |
| Other | Potassium chloride, Pioglitazone, Lactulose, Metoclopramide, Salbutamol |

Formal warning and contraindication data from the product package insert should be reviewed before any clinical use. Package insert data is currently unavailable in this Evidence Pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score (99.48%) and an exceptionally strong mechanistic rationale — brinzolamide's IOP-lowering mechanism directly addresses the core pathology of primary hereditary glaucoma — there is currently zero specific clinical trial or published literature evidence for this precise indication. The evidence level is L5 (model prediction only), and critical safety data (package insert warnings, contraindications) are also absent, which is a blocking data gap per the meta assessment.

**To proceed, the following is needed:**
- **[DG001 — Blocking]** Obtain and parse the TFDA/CDSCO package insert PDF to extract formal warnings and contraindications
- **[DG002 — High]** Confirm full MOA details from DrugBank API (target binding affinities, off-target activity)
- Conduct a systematic literature search for carbonic anhydrase inhibitors (dorzolamide, acetazolamide, brinzolamide) specifically in *CYP1B1*-, *MYOC*-, or *LTBP2*-mutation carriers to identify any indirect or bridging evidence
- Identify observational studies or case series on IOP-lowering therapy in pediatric or congenital glaucoma, where hereditary forms are most prevalent
- Assess India regulatory pathway (CDSCO) for filing a new indication extension based on mechanistic bridging and existing safety data from the approved open-angle glaucoma indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

