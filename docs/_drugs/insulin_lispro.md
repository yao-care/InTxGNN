---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue primarily used for glycaemic control in diabetes mellitus (both Type 1 and Type 2).
The TxGNN model predicts it may have activity in **Autoimmune Oophoritis** with a score of **99.78%**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this direction — evidence is model-prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (glycaemic control) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Insulin lispro is a rapid-acting insulin analogue engineered by inverting the Pro28–Lys29 sequence of human insulin, reducing self-association and accelerating subcutaneous absorption. It binds the insulin receptor to promote glucose uptake in muscle and adipose tissue, and suppresses hepatic glucose output. Beyond its metabolic role, insulin has mild immunomodulatory properties — it can reduce oxidative stress in immune cells and has been studied in the context of modulating autoimmune inflammation at the β-cell level.

Autoimmune oophoritis is a rare autoimmune condition in which the body attacks ovarian tissue, often occurring as part of polyglandular autoimmune syndrome (APS-2), which co-presents with Type 1 diabetes mellitus in a significant proportion of patients. The TxGNN model's high prediction score likely arises from this well-documented co-morbidity linkage in the knowledge graph, rather than from a direct pharmacological mechanism of insulin on ovarian tissue.

Critically, no known direct mechanistic pathway exists whereby insulin lispro would treat the underlying ovarian autoimmunity. The knowledge-graph signal appears to be driven by shared autoimmune aetiology (anti-ovarian antibodies co-occurring with anti-islet antibodies) rather than a drug–disease pharmacological effect. This distinction is important: co-morbidity does not equate to therapeutic applicability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions (352 interactions on record):**

Insulin lispro has an extensive interaction profile. Representative interactions from the dataset include:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Epinephrine | Moderate | Catecholamines antagonise insulin-mediated glucose uptake; may blunt hypoglycaemia warning signs |
| Phenylephrine | Moderate | Sympathomimetics may raise blood glucose and reduce insulin efficacy |
| Pseudoephedrine | Moderate | Similar sympathomimetic hyperglycaemic effect |
| Hydrocortisone | Moderate | Glucocorticoids antagonise insulin action; significant dose-dependent hyperglycaemia risk |
| Hydrochlorothiazide | Moderate | Thiazides can worsen glycaemic control |
| Acebutolol | Moderate | Beta-blockers may mask tachycardia as a hypoglycaemia warning sign |
| Formoterol | Moderate | Beta-2 agonists may cause hyperglycaemia |
| Salbutamol | Moderate | Same class as Formoterol; raises blood glucose |
| Albiglutide | Moderate | Additive glucose-lowering effect; increased hypoglycaemia risk |
| Alogliptin | Moderate | Additive glucose-lowering; monitor for hypoglycaemia |
| Metformin | Moderate | Additive glucose-lowering; generally beneficial but monitor |
| Ethanol | Moderate | Alcohol inhibits hepatic gluconeogenesis; severe hypoglycaemia risk |
| Estradiol / Ethinylestradiol / Levonorgestrel | Moderate | Oestrogens and progestins may impair glucose tolerance |
| Alpelisib | Moderate | PI3K inhibitor; known to cause severe hyperglycaemia, may exacerbate insulin resistance |
| Doxycycline | Moderate | May alter glucose metabolism |
| Acetazolamide | Moderate | Carbonic anhydrase inhibition may affect glucose handling |

> ⚠️ Note: The full interaction dataset contains **352 interactions**. The above represents a clinically relevant subset. Please consult a complete DDI database before co-prescribing.

Please refer to the package insert for key warnings and contraindications (detailed label data not available in this dataset).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.78%), but this appears to be driven by a co-morbidity linkage in the knowledge graph (APS-2 co-occurrence of autoimmune oophoritis and Type 1 diabetes) rather than a direct pharmacological mechanism. There is no clinical trial evidence, no published literature, and no plausible direct mechanistic pathway supporting insulin lispro as a treatment for autoimmune oophoritis itself. A "Hold" is appropriate until a credible mechanistic hypothesis beyond shared autoimmune aetiology can be established.

**To proceed, the following is needed:**
- Establish a direct mechanistic hypothesis: does insulin lispro modulate the anti-ovarian immune response independently of its glycaemic effect? (e.g., through insulin receptor signalling on immune effector cells)
- Conduct a systematic literature review on insulin's immunomodulatory effects in autoimmune oophoritis or related ovarian autoimmunity models
- Retrieve the full package insert (CDSCO / originator label) to assess key warnings and contraindications before any clinical feasibility assessment
- If a mechanism is identified, consider a preclinical in vitro/animal model study as the minimum L4 evidence threshold before any further progression

---

> *This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

