---
layout: default
title: Levobunolol
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 3
---

# Levobunolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Levobunolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Levobunolol is a non-selective topical ophthalmic beta-blocker, internationally approved for lowering intraocular pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with a prediction confidence of 99.98%; however, **no clinical trials** and **no dedicated publications** currently support this specific genetic subtype as an indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-Angle Glaucoma / Ocular Hypertension (international approvals; no India registration on record) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for levobunolol is not currently available in this evidence pack. Based on published literature included in this report, levobunolol is a potent **non-selective β1/β2 adrenoceptor blocker** applied topically to the eye. It reduces intraocular pressure (IOP) by blocking β2 receptors in the ciliary body epithelium, thereby suppressing aqueous humor production. This mechanism is well-established across multiple randomised controlled trials for open-angle glaucoma and ocular hypertension, with IOP reductions of approximately 7–8 mmHg (27–30%) demonstrated over periods ranging from 3 months to 4 years.

Primary hereditary glaucoma — encompassing primary congenital glaucoma and juvenile open-angle glaucoma caused by mutations such as *CYP1B1* or *MYOC* — shares the central pathological feature of elevated IOP, even though the upstream cause is a structural malformation of the trabecular meshwork or a genetically defective outflow pathway. Because levobunolol reduces IOP through a mechanism that is upstream of (and independent from) trabecular outflow, the TxGNN model's prediction is mechanistically coherent: beta-blockade of aqueous humor production could theoretically provide adjunctive IOP lowering in any glaucoma subtype where elevated IOP contributes to disease.

However, the clinical reality of primary hereditary glaucoma limits this prediction's near-term translational value. Surgical approaches — goniotomy, trabeculotomy, or trabeculectomy — are the standard first-line treatment, particularly for congenital cases. The role of topical beta-blockers in this population has not been specifically studied, paediatric safety data are limited, and the primarily structural aetiology means IOP-lowering drops are typically adjuncts rather than definitive therapy. No dedicated trials or publications were identified for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials have been registered specifically for Levobunolol in Primary Hereditary Glaucoma.

---

## Literature Evidence

Currently no related literature is available specifically for Levobunolol in Primary Hereditary Glaucoma.

---

## India Market Information

Levobunolol is currently **not registered or marketed in India**. No product authorisations were identified. The drug is not available through formal regulatory channels in India, which constitutes an additional barrier to any local clinical evaluation.

---

## Safety Considerations

**Drug Interactions**: The DDInter database identified **24 drug-drug interactions** for levobunolol. All 24 are currently classified as **"Unknown"** severity, meaning interaction magnitude and clinical significance remain uncharacterised. Clinically notable interacting drug classes include:

| Interacting Drug | Class | Interaction Level |
|-----------------|-------|------------------|
| Warfarin | Anticoagulant | Unknown |
| Clopidogrel | Antiplatelet | Unknown |
| Tacrolimus | Immunosuppressant | Unknown |
| Fluconazole | Azole antifungal | Unknown |
| Prednisone | Corticosteroid | Unknown |
| Budesonide | Corticosteroid | Unknown |
| Triamcinolone | Corticosteroid | Unknown |
| Lansoprazole / Pantoprazole / Omeprazole / Rabeprazole | Proton pump inhibitors | Unknown |
| Metronidazole | Antibiotic | Unknown |

Given that levobunolol is a non-selective beta-blocker with known systemic absorption after topical administration (demonstrated heart rate reductions in published trials), interactions affecting cardiac conduction, bronchospasm, or metabolic masking of hypoglycaemia should be evaluated before clinical use.

Please refer to the package insert for complete warnings and contraindication data (currently not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or publication evidence specifically linking levobunolol to primary hereditary glaucoma. While the mechanistic rationale is plausible (beta-blockade of aqueous humor production is indication-agnostic), this genetic subtype is predominantly managed surgically, and the marginal utility of adjunctive IOP lowering in this population has not been studied.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full DrugBank pharmacology record (DB01210) to formally document mechanism and target profile
- **Safety data**: Download and parse the regulatory package insert (TFDA or FDA label) to identify contraindications, boxed warnings, and paediatric safety status — currently a blocking data gap (DG001)
- **Targeted literature search**: Conduct a structured search for topical beta-blockers specifically in congenital or juvenile hereditary glaucoma (CYP1B1/MYOC mutation carriers), which may exist under different MeSH terms than those queried
- **Paediatric considerations**: Assess whether levobunolol is appropriate for the congenital glaucoma age group, given systemic absorption risk in neonates and infants
- **India regulatory pathway**: Evaluate feasibility of registration in India given zero existing approvals and absence of local market precedent
- **DDI risk stratification**: Reclassify all 24 drug interactions from "Unknown" to specific severity levels before any clinical use recommendation can be made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

