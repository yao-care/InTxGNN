---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 3
---

# Carbimazole
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone Receptor Beta Mutation

## One-Sentence Summary

Carbimazole is a thionamide antithyroid prodrug widely used internationally for the treatment of hyperthyroidism and Graves' disease, though it is not currently registered in India.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTHβ)**, with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism / Graves' disease (no India registration on record) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, carbimazole is a thionamide class antithyroid prodrug that is rapidly converted to methimazole after oral absorption. Methimazole acts as a competitive inhibitor of thyroid peroxidase (TPO), blocking the oxidation of iodide and the iodination of tyrosine residues on thyroglobulin, thereby directly suppressing the synthesis of both T3 and T4. This mechanism is well-established and forms the foundation of its use in any condition involving excessive thyroid hormone production.

Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTHβ) is a genetic disorder caused by loss-of-function mutations in the *THRB* gene. The hallmark is impaired negative feedback at the pituitary, resulting in persistently elevated TSH despite high circulating T3 and T4. This TSH excess chronically over-stimulates the thyroid gland, generating genuinely elevated thyroid hormone levels — the very endpoint carbimazole is designed to suppress. In this narrow pathophysiological framing, a mechanistic link exists.

However, the rationale is paradoxical in an important way. RTHβ patients require elevated thyroid hormone levels to compensate for reduced receptor sensitivity in TRβ-expressing tissues. Reducing hormone production with carbimazole risks inducing functional hypothyroidism in these very tissues. The sole available publication (PMID [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/)) describes a patient with RTHβ who was **incorrectly diagnosed as hyperthyroid** and treated intermittently with carbimazole for over ten years without benefit — fT4 remained elevated (25–35.7 pmol/L) and TSH remained non-suppressed throughout, which is the diagnostic signature of RTHβ, not Graves' disease. This case illustrates the clinical trap rather than a therapeutic success, and underlines why this TxGNN prediction, despite its high computational score, warrants significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case Report | BMJ Case Reports | A young man with elevated fT4 (25–35.7 pmol/L) and persistently non-suppressed TSH (6.78–22.1 mIU/L) was treated with carbimazole intermittently for 10 years without resolution; thyroid function never normalised, consistent with RTHβ rather than true hyperthyroidism. This case illustrates misapplication of carbimazole in RTHβ, not therapeutic success. |

---

## India Market Information

Carbimazole currently has no registered products in India. No authorisation records are available from the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.71%), there are no registered clinical trials, and the only available publication describes a patient with RTHβ who was incorrectly managed with carbimazole for a decade without benefit — making this an example of therapeutic misuse rather than evidence of efficacy. The underlying mechanistic logic is paradoxical: RTHβ patients depend on elevated thyroid hormone levels to achieve adequate tissue signalling through residual receptor function, and suppressing synthesis with carbimazole risks worsening their functional hormone deficiency.

**To proceed, the following is needed:**

- **MOA data**: Obtain full DrugBank pharmacology entry (DB00389) to formally document TPO inhibition mechanism and any known effects on thyroid hormone receptor pathways
- **Regulatory review**: Obtain CDSCO/TFDA package insert to document approved indications, black-box warnings, and contraindications (currently a Blocking data gap)
- **Mechanistic clarification**: Commission a preclinical literature review specifically addressing antithyroid drug use in THRB-mutation animal models or cell-line studies
- **Endocrinology expert consultation**: Assess whether there is any subtype of RTHβ (e.g., pituitary-selective resistance with peripheral hyperthyroid symptoms) where TSH suppression via carbimazole could be net beneficial
- **Comparative positioning**: Evaluate against established RTHβ management options (e.g., triiodothyroacetic acid / TRIAC, selective TRβ agonists) to determine whether carbimazole could offer any additive or complementary role
- **India regulatory pathway**: Since carbimazole is unregistered in India, any clinical investigation would require new drug application or import exemption under Schedule Y
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

