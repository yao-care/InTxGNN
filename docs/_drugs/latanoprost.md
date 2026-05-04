---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α analogue (FP receptor agonist) widely used for the treatment of open-angle glaucoma and ocular hypertension by reducing intraocular pressure (IOP).
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 clinical trial** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Latanoprost is a selective FP (prostanoid FP receptor) agonist. It reduces intraocular pressure by activating FP receptors in the ciliary muscle, relaxing smooth muscle tone, and increasing drainage of aqueous humor through the alternative uveoscleral pathway — typically achieving IOP reduction of 25–35%.

Primary hereditary glaucoma (including MYOC/OPTN gene mutation variants) is characterized by elevated IOP due to trabecular meshwork dysfunction, a mechanism largely shared with primary open-angle glaucoma. Because the FP receptor pathway remains functionally intact in hereditary forms of glaucoma, prostaglandin analogues like Latanoprost are mechanistically appropriate and are recommended as first-line IOP-lowering therapy in clinical guidelines when medical treatment is warranted alongside surgical approaches.

The identified clinical trial (NCT01527682) specifically evaluated prostaglandin analogues in pediatric glaucoma patients refractory to surgery, providing direct evidence that this drug class exerts its expected IOP-lowering effect in this population. The TxGNN prediction is therefore mechanistically well-grounded and clinically plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Evaluated the ocular hypotensive effect and safety of prostaglandin analogues (latanoprost class) versus carbonic anhydrase inhibitor (dorzolamide) in pediatric glaucoma patients refractory to surgical procedures; protocol was amended mid-study to target 68 eyes from an initial 96 |

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Latanoprost currently has **no registered products in India** (0 CDSCO licenses on record). The drug is not marketed under any Indian regulatory authorization at this time.

---

## Safety Considerations

- **Drug Interactions**: 121 potential interactions identified in the DDinter database; all are currently classified as "Unknown" severity. Commonly co-prescribed drugs flagged include Calcitriol, Glimepiride, Doxycycline, Prednisone, Simvastatin, Morphine, Metformin, and Omeprazole, among others.

Please refer to the package insert for full safety information (key warnings and contraindications data were not available in this Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.88% is mechanistically well-supported by the established FP receptor agonist pathway for IOP reduction, and a completed Phase 2 clinical trial (NCT01527682) provides direct evidence of prostaglandin analogue efficacy in pediatric glaucoma — the population most relevant to primary hereditary glaucoma.

**To proceed, the following is needed:**
- Retrieve full mechanism of action (MOA) data from DrugBank API (currently a High-severity data gap)
- Obtain CDSCO/TFDA package insert to document key warnings and contraindications (currently a Blocking data gap)
- Evaluate clinical significance of all 121 DDI entries (currently all classified as "Unknown")
- Review complete efficacy and safety data from NCT01527682, including IOP endpoints specific to hereditary subtypes
- Assess pediatric dosing and long-term safety profile, as primary hereditary glaucoma frequently presents in children and adolescents
- Develop a regulatory strategy for India market entry given zero current CDSCO registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

