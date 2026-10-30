---
layout: default
title: Ranibizumab
parent: Model Prediction Only (L5)
nav_order: 725
evidence_level: L5
indication_count: 9
monitor_inn: "Ranibizumab"
predicted_indications: ["mature cataract", "immature cataract", "craniostenosis cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "hemorrhagic disease of newborn"]
last_modified_at: 2026-10-30
description: "Ranibizumab: predicted new indication Mature cataract (evidence level L5). Approved use: Diabetic retinopathy, macular degeneration…"
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ranibizumab: From Diabetic Retinopathy and Macular Degeneration to Mature Cataract
{: .text-alpha }

## One-Sentence Summary

Ranibizumab is an anti-VEGF eye injection.
The TxGNN model predicts it may be effective for **mature cataract**, but the data compiled for this report contain **no clinical trials** and only **2 publications** on this topic, and neither shows that ranibizumab treats cataract.
The prediction therefore rests almost entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetic retinopathy, macular degeneration, diabetic macular edema and related retinal conditions (relations recorded in the knowledge graph; no approved indication text is available in the local licence records) |
| Predicted New Indication | Mature cataract |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Ranibizumab is known as an anti-VEGF agent that is injected into the eye to treat retinal conditions with abnormal vessel growth or leakage, such as diabetic macular edema and macular degeneration.

The link to mature cataract is weak. Cataract is an opacity of the lens, and there is no recognised VEGF-driven mechanism by which ranibizumab would clear or prevent it. The two papers retrieved describe ranibizumab given alongside cataract surgery in eyes that also have diabetic macular edema, where the drug treats the retinal problem and not the cataract. The other paper describes rapid cataract progression after a dexamethasone implant, which is a different drug.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between cataract and the co-occurring diabetic eye conditions that ranibizumab does treat, not biological evidence. It should not be read as a therapeutic signal. Because no cited study directly examines ranibizumab as a treatment for mature cataract, the evidence level is L5.

Other cataract-type predictions (immature, craniostenosis, tetanic, nuclear senile, cortical, senile, and type 2 diabetes-associated cataract) have the same score range and equally little support. Hemorrhagic disease of newborn also appeared as a prediction. It is caused by vitamin K deficiency and has no VEGF-related mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for mature cataract.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40790176](https://pubmed.ncbi.nlm.nih.gov/40790176/) | 2025 | Cohort | BMC Ophthalmology | Compared combined cataract surgery with intravitreal ranibizumab injection against surgery alone in 39 eyes with diabetic macular edema and obscured fundus due to advanced cataract. The ranibizumab addresses the macular edema, not the cataract. |
| [30606142](https://pubmed.ncbi.nlm.nih.gov/30606142/) | 2019 | Case report | BMC Ophthalmology | Reports rapid progression of cataract to the mature stage after a dexamethasone implant (not ranibizumab) for macular edema. Not evidence of benefit. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 121668 | Lucentis Injection (Novartis India Ltd) | Vial of 1 ml injection | Not stated in the licence record |
| Registration No. 184362 | Razumab 2.3mg Injection (Intas Pharmaceuticals Ltd) | Vial of 1 injection | Not stated in the licence record |

Both licences are valid, single-ingredient products.

## Safety Considerations

- **Knowledge-graph contraindication relations (not label text)**: eye infectious disease and conjunctivitis. These come from the knowledge graph and should be checked against the official label.
- **Literature signal**: one case report (PMID 38476863) describes capsular block syndrome after an intravitreal ranibizumab injection in a patient with age-related macular degeneration, a possible eye-related adverse event.
- No drug interaction records were found.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for mature cataract is supported only by a model score. No clinical trial exists, and the two retrieved papers address retinal disease or a different drug. There is no plausible anti-VEGF mechanism for lens opacity. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data to test whether any biologically plausible link to lens opacity exists
- Package insert warnings and contraindications for the Indian products (Lucentis, Razumab)
- Any direct preclinical or clinical study of ranibizumab for cataract itself, as opposed to cataract surgery combined with retinal treatment
- Review of the knowledge-graph contraindication relations (eye infection, conjunctivitis) against official labelling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

