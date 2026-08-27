---
layout: default
title: Mephentermine
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 4
---

# Mephentermine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Mephentermine: From Hypotension to Postural Orthostatic Tachycardia Syndrome

## One-Sentence Summary

Mephentermine is a sympathomimetic amine historically used as a vasopressor for the treatment of hypotension, particularly in perioperative and anaesthetic settings.
The TxGNN model predicts it may be effective for **Postural Orthostatic Tachycardia Syndrome (POTS)**, the highest-ranked indication with a prediction score of **99.84%**.
However, **no clinical trials and no published literature** currently support this repurposing direction, and significant mechanistic concerns exist.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypotension (vasopressor use in perioperative/anaesthetic settings) |
| Predicted New Indication | Postural Orthostatic Tachycardia Syndrome (POTS) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological properties, Mephentermine is a mixed adrenergic agonist with both α- and β-adrenoceptor activity. Its vasopressor effect is mediated primarily through α-adrenergic vasoconstriction and positive chronotropic/inotropic effects via β₁-adrenoceptor stimulation. These properties form the mechanistic basis for its historical use in hypotension.

POTS is characterised by an excessive compensatory sinus tachycardia upon standing, driven by inadequate venous return and orthostatic hypotension. The α-adrenergic vasoconstrictive component of Mephentermine could theoretically improve venous return and reduce orthostatic hypotension — a rationale analogous to Midodrine, the selective α₁-agonist currently used as a POTS standard of care.

However, the prediction carries an inherent mechanistic contradiction: Mephentermine's β-adrenergic activity accelerates heart rate, which directly worsens POTS's defining symptom — compensatory sinus tachycardia. Unlike Midodrine's selective α₁ profile, Mephentermine's mixed adrenergic action may amplify rather than relieve the core pathophysiology. This internal inconsistency substantially undermines the repurposing hypothesis, and no clinical data exists to resolve it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Mephentermine is currently not marketed in India. No regulatory authorizations or product registrations are on record.

---

## Safety Considerations

**Drug Interactions (64 interactions on record; selected key examples below):**

Mephentermine has 64 documented drug-drug interactions, predominantly at a **Moderate** severity level. A notable pattern is interaction with antidiabetic agents — Mephentermine's sympathomimetic activity can antagonise insulin secretion and impair glucose uptake, reducing the efficacy of hypoglycaemic medications.

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Metformin | Moderate | Sympathomimetic-induced hyperglycaemia may reduce antidiabetic efficacy |
| Insulin glargine / aspart / detemir / degludec | Moderate | Adrenergic stimulation can antagonise insulin action and mask hypoglycaemic symptoms |
| Semaglutide / Dulaglutide / Lixisenatide / Albiglutide | Moderate | GLP-1 agonist efficacy may be attenuated |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | SGLT-2 inhibitor glucose-lowering effect may be reduced |
| Pioglitazone | Moderate | Potential attenuation of insulin-sensitising effect |
| Glimepiride / Chlorpropamide | Moderate | Risk of altered glycaemic control |
| Phentermine / Diethylpropion | Moderate | Additive sympathomimetic effects; cardiovascular risk amplified |
| Alogliptin / Linagliptin | Moderate | DPP-4 inhibitor efficacy potentially reduced |
| Acarbose | Moderate | Carbohydrate absorption modulation may interact with glycaemic response |

For complete contraindications and package insert warnings, please refer to the official prescribing information, as these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.84% is high, but the evidence base is entirely absent — zero clinical trials, zero publications — placing this at Evidence Level L5 (model prediction only). More critically, the mechanistic hypothesis contains a direct internal contradiction: Mephentermine's β-adrenergic activity would be expected to worsen the defining tachycardia of POTS, opposing the therapeutic goal. The drug is also not marketed in India, adding a significant regulatory hurdle.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Obtain complete MOA data from DrugBank (DG002) to formally evaluate α vs. β receptor selectivity and relevance to POTS pathophysiology
- **Safety baseline**: Retrieve TFDA (or equivalent) package insert for full warnings and contraindications (DG001) before any clinical consideration
- **Preclinical evidence**: Generate in vitro/in vivo data on Mephentermine's effect on heart rate and venous capacitance in POTS models before advancing — this is the minimum scientific threshold given the mechanistic contradiction
- **Comparator analysis**: Benchmark against Midodrine and Fludrocortisone (established POTS therapies) to identify whether a mixed adrenergic agent offers any differentiated benefit
- **Regulatory feasibility assessment**: Given zero Indian market presence, a full registration pathway analysis would be required prior to any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

