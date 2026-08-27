---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin (Jardiance) is a well-established SGLT2 inhibitor approved globally for type 2 diabetes mellitus and heart failure with reduced ejection fraction.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, a rare autoimmune neurological disorder,
however **no clinical trials and no supporting publications** currently exist for this direction — making this a model-only hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus / Heart Failure (global approval; not registered in India) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established pharmacological knowledge, Empagliflozin is a selective sodium-glucose cotransporter 2 (SGLT2) inhibitor. It reduces blood glucose by blocking glucose reabsorption in the renal proximal tubule, and has demonstrated cardiovascular and renal protective effects likely mediated through reduction of oxidative stress, inflammation, and haemodynamic load.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder characterised by progressive muscle rigidity and spasms. Its core pathology involves anti-GAD65 antibodies attacking GABAergic inhibitory interneurons in the spinal cord and brain, fundamentally disrupting GABA-mediated motor suppression. This immunological and neurological mechanism has no established pharmacological overlap with SGLT2 inhibition.

The high TxGNN score (99.06%) is most likely a consequence of **network topology artefacts** — Empagliflozin occupies a highly connected node in the knowledge graph (touching metabolic, inflammatory, and cardiovascular disease clusters), and SPS may share indirect graph proximity via shared comorbidity nodes such as autoimmune disease or neuroinflammation. This does **not** indicate mechanistic specificity. Furthermore, the identical score shared between Classic SPS (rank 13,839) and Focal Stiff Limb Syndrome (rank 13,840) strongly suggests the model treats these as near-equivalent graph nodes, further reducing confidence in the prediction's specificity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Empagliflozin in Classic Stiff Person Syndrome, Focal Stiff Limb Syndrome, or Opsismodysplasia.

---

## Literature Evidence

Currently no related literature available for any of the three predicted indications.

---

## India Market Information

Empagliflozin currently has **no registered products** in India. No authorization records are available.

> Note: Empagliflozin (brand name Jardiance) is approved in the US (FDA, 2014), EU (EMA), and many other markets for type 2 diabetes and heart failure, but has not obtained regulatory approval in India as of the data cutoff (2026-04-04).

---

## Safety Considerations

**Drug Interactions:** A total of **369 drug-drug interactions** have been identified via DDInter. Key interactions to note include:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Furosemide | Moderate | Additive diuretic effect; risk of volume depletion and electrolyte imbalance |
| Acetazolamide | Moderate | Compounded risk of metabolic acidosis |
| Nifedipine | Moderate | Potential pharmacokinetic interaction affecting drug exposure |
| Ethanol | Moderate | Increased risk of hypoglycaemia and volume depletion |
| Fosinopril | Moderate | Additive hypotensive and renal effects |
| Fosphenytoin | Moderate | Possible alteration of glucose control |
| Phenylephrine | Moderate | May blunt glucose-lowering effect |
| Epinephrine | Moderate | May antagonise glycaemic benefit |
| Salbutamol / Formoterol | Moderate | Beta-agonists may counteract glycaemic effects |
| Ethinylestradiol | Moderate | Potential impact on glycaemic control |
| Hydrocortisone | Moderate | Corticosteroids may blunt SGLT2 inhibitor efficacy |
| Hydrocortisone (topical) | Minor | Low clinical significance |
| Alclometasone (topical) | Minor | Low clinical significance |

For complete warnings and contraindications, please refer to the approved package insert (e.g., FDA label or EMA SmPC for Jardiance), as India-specific label data is not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (Classic Stiff Person Syndrome, Focal Stiff Limb Syndrome, Opsismodysplasia) are classified as Evidence Level L5 — model prediction only, with zero supporting clinical trials or published literature. The mechanistic link between SGLT2 inhibition and the GABAergic/autoimmune pathology of Stiff Person Syndrome is highly speculative, and the identical TxGNN scores for two related conditions suggest network topology noise rather than genuine therapeutic signal. This candidate does not meet the minimum evidence threshold for further investment at this time.

**To proceed, the following is needed:**

- **Mechanistic validation:** Identify any published preclinical or in vitro data linking SGLT2 inhibition to GABAergic signalling, neuroinflammation, or anti-GAD65 antibody modulation
- **India regulatory data:** Clarify whether Empagliflozin has a pending CDSCO application or is available under import licence; obtain India-specific package insert for formal safety assessment
- **Literature review:** Commission a systematic literature search beyond PubMed (e.g., Embase, ICTRP, grey literature) to confirm the absence of any preliminary case reports or mechanism studies
- **Expert consultation:** Consult a neurologist specialising in rare movement disorders to assess clinical plausibility before any resource commitment
- **Network analysis audit:** Request TxGNN graph analysis to determine whether the high score reflects genuine mechanistic nodes or indirect comorbidity clustering artefacts

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. Data cutoff: 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

