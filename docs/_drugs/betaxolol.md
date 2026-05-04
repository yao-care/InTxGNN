---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a selective β1-adrenergic receptor antagonist traditionally used for open-angle glaucoma and ocular hypertension management by reducing aqueous humor production.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** (including primary congenital glaucoma and juvenile open-angle glaucoma),
with **no clinical trials** and **no publications** specifically supporting this direction — evidence is currently model-prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular Hypertension (selective β1-blocker, ophthalmic use) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Betaxolol is a cardioselective β1-adrenergic receptor antagonist. When applied topically to the eye, it acts on the ciliary body epithelium to suppress cAMP-dependent aqueous humor secretion, thereby lowering intraocular pressure (IOP). This mechanism is well-established for open-angle glaucoma and ocular hypertension, and represents the pharmacological rationale underlying the TxGNN model's prediction.

Primary hereditary glaucoma — encompassing primary congenital glaucoma (PCG) and juvenile open-angle glaucoma (JOAG) — is pathophysiologically distinct from adult open-angle glaucoma. The defining lesion is a developmental abnormality of the trabecular meshwork and anterior chamber angle, leading to impaired aqueous outflow rather than overproduction. Betaxolol's mechanism targets the production side of the IOP equation, offering a theoretical compensatory role when outflow is structurally compromised.

However, the mechanistic link is of moderate rather than strong plausibility. The first-line treatment for PCG is surgical (goniotomy or trabeculotomy), with pharmacotherapy reserved for pre-operative stabilisation or adjunctive use. Critically, genetic subtypes of hereditary glaucoma (e.g., *CYP1B1*, *MYOC* mutations) introduce variable trabecular biology that may substantially alter beta-blocker responsiveness — and no direct genotype-stratified data currently exist to quantify this effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Betaxolol in Primary Hereditary Glaucoma.

---

## Literature Evidence

Currently no related literature available for Betaxolol specifically in Primary Hereditary Glaucoma.

---

## India Market Information

Betaxolol has no registered products in India (0 authorisations on record). The drug is currently classified as **Not Marketed** in the Indian regulatory database.

---

## Safety Considerations

**Drug Interactions:** Betaxolol has 173 documented interactions in the DDInter database. Key moderate-level interactions include:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Epinephrine | Moderate | Risk of hypertensive response followed by bradycardia; caution in ophthalmic emergency settings |
| Hydrocortisone / Dexamethasone / Betamethasone / Triamcinolone / Budesonide | Moderate | Corticosteroids may attenuate antihypertensive effect and elevate IOP — clinically relevant in glaucoma management |
| Calcium salts (acetate, carbonate, citrate, gluconate, lactate, glubionate) | Moderate | May affect beta-blocker absorption or cardiovascular response |
| Bupropion | Moderate | Potential for pharmacodynamic interaction affecting heart rate and blood pressure |
| Atropine / Hyoscyamine | Moderate | Anticholinergic agents may counteract beta-blocker-mediated bradycardia |
| Morphine | Moderate | Additive hypotensive and cardiodepressant effects |
| Acetohexamide | Moderate | Beta-blockers may mask hypoglycaemia symptoms |
| Acetylsalicylic acid | Minor | Possible modest attenuation of antihypertensive effect |
| Aluminium hydroxide / Attapulgite | Minor | May reduce oral betaxolol absorption if given simultaneously |

> **Note:** Formal warnings and contraindications (CDSCO/package insert) are not available in the current evidence pack. Please refer to the manufacturer's prescribing information for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.74%), and the proposed mechanism — IOP reduction via β1-receptor blockade — is biologically coherent. However, there is currently zero clinical trial or published literature evidence specifically linking Betaxolol to Primary Hereditary Glaucoma, the disease has a structurally distinct pathophysiology from typical open-angle glaucoma, and the drug is not registered in India. This does not meet the minimum evidence threshold to proceed.

**To advance beyond Hold, the following is needed:**

- **MOA confirmation:** Retrieve DrugBank full mechanism-of-action data to formally document the ciliary body IOP-lowering pathway (Data Gap DG002)
- **Safety dossier:** Obtain and parse the CDSCO/package insert PDF for complete warnings and contraindications (Data Gap DG001)
- **Targeted literature search:** Expand PubMed query to include broader terms (e.g., "betaxolol AND congenital glaucoma", "beta-blocker AND CYP1B1 glaucoma", "beta-blocker AND pediatric glaucoma") to determine if any evidence exists under adjacent search terms
- **Regulatory pathway assessment:** Evaluate CDSCO orphan drug designation eligibility for primary congenital glaucoma
- **Genotype-stratification consideration:** Assess whether *CYP1B1* or *MYOC* mutational status would moderate beta-blocker responsiveness before any translational study design
- **Surgical standard-of-care alignment:** Define the proposed clinical role (pre-operative IOP control vs. long-term adjunct) to frame a realistic feasibility hypothesis

> *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

