---
layout: default
title: Beta Carotene
parent: Moderate Evidence (L3-L4)
nav_order: 104
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Beta Carotene: predicted new indication Acne (disease) (evidence level L4). Approved use: Not stated"
monitor_inn: "Beta carotene"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "tetanic cataract", "mature cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract"]
---

# Beta Carotene
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Beta Carotene: From Nutritional Supplement (Original Indication Not Specified) to Acne
{: .text-alpha }

## One-Sentence Summary

Beta carotene is a provitamin A carotenoid with antioxidant activity, currently marketed in India as an oral soft-gel capsule supplement.
The TxGNN model predicts it may be useful for **acne**, but **no clinical trials** are registered and the 7 retrieved publications are observational, biochemical or general reviews.
The prediction is therefore a computational signal only, supported at the weakest evidence level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (the approved indication text is blank on both registrations) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, beta carotene is a provitamin A carotenoid with antioxidant properties. Oxidative stress and altered antioxidant status have been described in acne vulgaris, and vitamin A pathways are relevant to the pilosebaceous unit (the hair follicle and oil gland), which gives the prediction a plausible biological basis.

The retrieved literature, however, only describes associations: serum vitamin A and beta carotene levels in skin disease, oxidant/antioxidant status in adolescents with acne, and oxidative changes during isotretinoin treatment. No study has tested beta carotene as a treatment for acne. The very high TxGNN score should be read as a model prediction, not as proof of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20049267](https://pubmed.ncbi.nlm.nih.gov/20049267/) | 2009 | Cohort | Indian J Dermatol | Oxidant/antioxidant status assessed in obese adolescent females with acne vulgaris |
| [22517509](https://pubmed.ncbi.nlm.nih.gov/22517509/) | 2012 | Clinical biomarker study | Cell Biochem Funct | Isotretinoin treatment altered antioxidant vitamins and induced oxidative toxicity in acne patients |
| [7618499](https://pubmed.ncbi.nlm.nih.gov/7618499/) | 1995 | Review | J Am Board Fam Pract | General overview of vitamins used as therapy |
| [2073211](https://pubmed.ncbi.nlm.nih.gov/2073211/) | 1990 | Review | Australas J Dermatol | Skin findings in anorexia nervosa, including elevated beta carotene levels and acne in a small subset |
| [4230169](https://pubmed.ncbi.nlm.nih.gov/4230169/) | 1967 | Cross-sectional | Dermatol Wochenschr | Vitamin A and beta carotene serum levels in people with and without skin diseases |

Two further retrieved papers (plant essential oil studies) are not specific to beta carotene and are omitted.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 197872 | Resumer Pro Softgel Capsule | Bottle of 60 soft gelatin capsules | Not stated |
| 98656 | Glowishma Softgel Capsule | Strip of 10 soft gelatin capsules | Not stated |

---

## Safety Considerations

Beyond the data below, please refer to the package insert for safety information.

- **Drug Interactions**:
  - Verteporfin: Moderate
  - Lutein: Minor
- **Disease associations flagged by the knowledge graph (not label text)**: blood coagulation disease, sickle cell anaemia, hereditary persistence of fetal haemoglobin, primary hyperoxaluria, hereditary haemochromatosis, haemosiderosis, iron metabolism disease and Wilson disease. These should be verified against the label before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction has a very high model score but no clinical trials and only observational or biochemical literature, with no study testing beta carotene as an acne treatment. Evidence is at L4, which does not justify advancing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the two Indian products (currently missing, blocking safety screening)
- Mechanism of action data from DrugBank
- Controlled human studies, or at least well-designed mechanistic work, testing beta carotene in acne
- Review of the knowledge-graph contraindication flags and the verteporfin interaction

---

## Other Predicted Indications (For Reference)

Other predictions in the data are also weakly supported. None has a registered clinical trial.

| Predicted Indication | Evidence Level | Assessment |
|------|------|------|
| Diabetic retinopathy | L4 | Research question. Animal studies and mixed observational data only; no human interventional trial |
| Diabetic cataract | L4 | Research question. Observational nutrition associations, mostly in non-diabetic populations |
| Cortical cataract | L4 | Hold. Antioxidant supplement RCTs (combination with vitamins C and E, or alpha-tocopherol) showed no meaningful benefit; they do not isolate beta carotene |
| Type 2 diabetes-associated cataract | L4 | Hold. A single observational study |
| Severe nonproliferative diabetic retinopathy, nuclear senile cataract | L5 | Hold. No trials or literature; computational prediction only |
| Tetanic cataract, mature cataract, craniostenosis cataract | L5 | Hold. No plausible mechanistic link or clinical support; likely graph-propagation artifacts |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

