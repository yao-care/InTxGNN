---
layout: default
title: Panitumumab
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Panitumumab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Metastatic malignant neoplasm in the colon"
---

# Panitumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is a fully human monoclonal antibody against EGFR, originally used to treat metastatic malignant neoplasm of the colon.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic malignant neoplasm in the colon |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, panitumumab is an anti-EGFR antibody, and its efficacy in metastatic colon cancer is established. EGFR signalling is known to play a role in bone remodelling (osteoblast differentiation and osteoclast regulation), which offers a speculative link to bone disease.

However, this link is background knowledge only and is not supported by the data compiled for this report. Blocking EGFR could affect bone metabolism in either direction, and it is not clear that the effect would be beneficial. The high TxGNN score is a computational prediction with no trial or literature backing, and the relationship between colon cancer and drug-induced osteoporosis is not mechanistically obvious.

A second predicted indication, severe nonproliferative diabetic retinopathy (TxGNN score 99.05%, also L5, Hold), was also generated. Its rationale is similarly speculative: EGFR signalling has been implicated in retinal angiogenesis, but panitumumab is a large systemic antibody with limited ocular penetration, and its known toxicities include ocular events such as keratitis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 234323 | Vectibix 100mg Solution for Infusion | Bottle of 5 ml solution for infusion | Not specified in the data compiled |

The product is manufactured by Glaxo SmithKline Pharmaceuticals Ltd and is an injectable single-ingredient product with valid status.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Dermatologic reactions and hypomagnesaemia are known concerns for this drug class |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions**: The interaction screening identified 27 interacting drugs in total. The main ones listed:

- **Major**: Bevacizumab, Irinotecan, Irinotecan (liposomal), Amiodarone, Arsenic trioxide, Dofetilide, Dronedarone, Droperidol, Aminolevulinic acid, Levacetylmethadol
- **Moderate**: Proton pump inhibitors (Rabeprazole, Omeprazole, Dexlansoprazole, Esomeprazole, Lansoprazole, Pantoprazole), Methoxsalen, Aminolevulinic acid (topical), Disopyramide, Idelalisib

Please refer to the package insert for other safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or publications and no confirmed mechanistic link. The safety profile of an EGFR-blocking oncology antibody also raises concerns for use in a non-cancer bone condition.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) to evaluate a link between EGFR blockade and bone metabolism
- Package insert warnings and contraindications from the India Pharma source (currently a blocking gap for safety screening)
- Preclinical or observational evidence on panitumumab's effect on bone, including whether it helps or harms
- Approved indication text for the India registration
- A risk-benefit assessment of using an oncology antibody in a non-cancer indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

