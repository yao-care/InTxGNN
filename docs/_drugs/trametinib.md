---
layout: default
title: Trametinib
parent: Model Prediction Only (L5)
nav_order: 853
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Trametinib: predicted new indication Choroideremia (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "Trametinib"
predicted_indications: ["choroideremia"]
---

# Trametinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Trametinib: From Metastatic Melanoma to Choroideremia
{: .text-alpha }

## One-Sentence Summary

Trametinib is an oral MEK inhibitor originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration, with a very high score of 0.9931.
However, **no clinical trials and no publications** currently support this prediction, so it rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trametinib blocks MEK1 and MEK2 (MAP2K1 and MAP2K2), two kinases in the MAPK signalling pathway that sit downstream of BRAF and RAS. It is used for BRAF V600-mutant melanoma, alone or with dabrafenib. In the US it is also approved in combination with dabrafenib for adjuvant melanoma treatment and for BRAF V600E-positive anaplastic thyroid cancer.

The link to choroideremia is weak. Choroideremia is caused by loss of function of the CHM gene (REP1 protein) and is not a MAPK-driven tumour. Melanoma responds to trametinib because MAPK signalling drives tumour growth, and that reasoning does not carry over to this retinal disease. The data compiled for this report do not support any mechanistic link. The high TxGNN score is a computational association only.

By contrast, the other predicted indications for trametinib are mostly melanoma subtypes (for example non-cutaneous melanoma and nodular melanoma). These are mechanistically much more plausible and have more supporting studies, including a completed Phase 2 trial. If the goal is to prioritise repurposing opportunities, those predictions deserve more attention than choroideremia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| Registration No. 136528 | Meqsel 0.5mg Tablet (Novartis India Ltd) | Oral; bottle of 30 tablets |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 15 moderate-level interactions were identified, with no severe-level interactions in the data compiled. The interacting drugs are:
  - Fostamatinib, elagolix, apalutamide, enzalutamide
  - Brigatinib, dabrafenib, encorafenib, erdafitinib, gilteritinib, idelalisib, midostaurin, tucatinib
  - Isavuconazonium, lasmiditan, sarecycline

  Dabrafenib and encorafenib are BRAF inhibitors that are typically co-prescribed with MEK inhibitors, so the interaction should be reviewed in that setting.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for choroideremia has no clinical trial or literature support (L5), and the disease biology is unrelated to the MAPK-driven mechanism through which trametinib works. Pursuing this indication is not justified on current evidence.

**To proceed, the following is needed:**
- A plausible biological hypothesis connecting MEK inhibition to CHM/REP1 deficiency, supported by preclinical retinal models
- Any published preclinical or clinical data on MEK inhibitors in inherited retinal degeneration
- Safety evaluation of systemic MEK inhibition in this population, including ocular toxicity, since retinal adverse events are a concern with this drug class
- The complete package insert for the India-marketed product (warnings, contraindications, approved indication text)
- Consideration of the better-supported melanoma-subtype predictions as higher-priority repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

