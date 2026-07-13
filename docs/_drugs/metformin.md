---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a first-line oral antidiabetic agent widely used for the management of Type 2 Diabetes Mellitus, acting primarily through hepatic glucose production suppression.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, with a high prediction score of 99.45%.
However, **0 clinical trials** and **0 publications** currently support this direction, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (well-established; not captured in this data pack's regulatory records) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Metformin is a biguanide antidiabetic agent whose primary action involves activation of AMP-activated protein kinase (AMPK). This leads to suppression of hepatic gluconeogenesis, improved peripheral insulin sensitivity, and—at a broader level—anti-inflammatory effects and modulation of T regulatory cell function.

Focal stiff limb syndrome is a localized variant of stiff person syndrome, whose core pathophysiology involves autoimmune-mediated GABAergic dysfunction driven by anti-GAD65 antibodies. Metformin's AMPK-mediated anti-inflammatory and T-cell regulatory properties offer a theoretically indirect link to autoimmune modulation. However, there is no direct mechanistic connection between Metformin and the GABAergic system, and no evidence that it can specifically target the anti-GAD65 autoimmune cascade.

The TxGNN high score (0.9945) likely reflects shared nodes in neuroimmune pathways within the knowledge graph, rather than a specific mechanistic prediction. With zero supporting clinical or preclinical evidence, this prediction should be interpreted as a hypothesis-generating signal only, not a clinically actionable finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Metformin in Focal Stiff Limb Syndrome.

---

## Literature Evidence

Currently no related literature available for Metformin in Focal Stiff Limb Syndrome.

---

## India Market Information

No registered products found for Metformin in the India regulatory dataset included in this evidence pack.

> **Note:** Metformin is a globally established generic medication available in numerous markets worldwide under various brand names (e.g., Glucophage, Fortamet). The absence of records here reflects a data gap in this specific pack, not the drug's actual global market presence.

---

## Safety Considerations

**Drug Interactions (642 total interactions identified; selected key interactions shown):**

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Acetazolamide | **Major** | Risk of lactic acidosis; both drugs affect renal tubular secretion |
| Ethanol | **Major** | Increased risk of lactic acidosis; alcohol potentiates Metformin's effect on lactate metabolism |
| Dolutegravir | Moderate | Dolutegravir inhibits renal OCT2/MATE transporters, potentially increasing Metformin plasma levels |
| Abemaciclib | Moderate | May increase Metformin exposure via transporter inhibition |
| Nifedipine | Moderate | May enhance Metformin absorption |
| Ibuprofen | Moderate | NSAIDs can reduce renal clearance, increasing Metformin accumulation risk |
| Ketorolac | Moderate | Similar renal clearance concern as other NSAIDs |
| Hydrochlorothiazide | Moderate | Thiazides may elevate blood glucose, reducing Metformin efficacy |
| Hydrocortisone | Moderate | Corticosteroids raise blood glucose, counteracting Metformin's effect |
| Formoterol / Salbutamol / Pseudoephedrine | Moderate | Beta-2 agonists and sympathomimetics may antagonize glycaemic control |
| Epinephrine / Phenylephrine | Moderate | Sympathomimetics elevate blood glucose |
| Ethinylestradiol | Moderate | Oestrogens may impair glucose tolerance |
| Ranitidine | Moderate | H2 blockers inhibit renal tubular secretion of Metformin, increasing plasma levels |
| Acetohexamide | Moderate | Additive hypoglycaemic effect with other antidiabetics |
| Acarbose | Minor | Additive glucose-lowering; generally beneficial but monitor for GI effects |
| Alclometasone (topical) / Hydrocortisone (topical) | Minor | Minimal systemic absorption; low clinical impact |

> Full label warnings and contraindications were not available in this evidence pack. Please refer to the approved package insert for complete safety information.

---

### ⚠ Special Safety Note for Predicted Indications

Among the five predicted indications in this pack, **Thiamine-Responsive Dysfunction Syndrome (rank 4)** presents a potential safety conflict: Metformin inhibits mitochondrial complex I, and published literature suggests it may reduce thiamine absorption and worsen pre-existing mitochondrial dysfunction—which is the core pathology of this syndrome. This is a mechanistic contraindication, not a therapeutic opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for Metformin in this pack are rated L5 (model prediction only), with zero supporting clinical trials or published literature. The top prediction—Focal Stiff Limb Syndrome—lacks any direct mechanistic or empirical support, and one of the predicted indications (Thiamine-Responsive Dysfunction Syndrome) may pose an active safety risk.

**To proceed, the following is needed:**

- Obtain Metformin's full mechanism of action data from DrugBank (DG002) to enable proper mechanistic linkage analysis
- Retrieve approved label warnings and contraindications from regulatory sources (DG001) to complete safety evaluation
- Commission a targeted literature review for Metformin in neuroimmune or stiff person spectrum disorders to determine if any preclinical evidence exists
- Obtain India regulatory registration records to confirm actual market availability and approved indications
- Before any clinical consideration, conduct in vitro or animal model studies to establish proof-of-concept for GABAergic or autoimmune pathway modulation by Metformin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

