---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tipiracil: predicted new indication Cecum villous adenoma (evidence level L5). Approved use: Colorectal cancer (malignant colon neoplasm, colonic neoplasm…"
monitor_inn: "Tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
---

# Tipiracil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tipiracil: From Colorectal Cancer to Cecum Villous Adenoma
{: .text-alpha }

## One-Sentence Summary

Tipiracil is a component of the trifluridine/tipiracil combination, originally used to treat colorectal cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but there are currently **0 clinical trials** and **0 related publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (malignant colon neoplasm, colonic neoplasm, squamous cell carcinoma of colon) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tipiracil is a thymidine phosphorylase inhibitor that is marketed only in combination with trifluridine (trifluridine/tipiracil). It prevents the breakdown of trifluridine, a cytotoxic nucleoside analogue, and so raises the drug's exposure. Tipiracil itself is not known to have a direct antitumour effect.

A villous adenoma of the cecum is a benign precursor lesion in the same organ as colorectal cancer. The link between the two is therefore anatomical and prediction-based. The model score is very high, but it likely reflects shared colon-tissue neighbours in the knowledge graph rather than a biological reason.

There is also little clinical rationale for cytotoxic therapy in a benign lesion that can usually be removed endoscopically. No clinical, preclinical or literature evidence supports a benefit in this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for cecum villous adenoma.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228143 | Tipanat 8.19mg/20mg Tablet (Natco Pharma Ltd) | Bottle of 20 tablets (oral) | Not specified in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Not a cytotoxic agent itself. It is the enzyme-inhibitor component of a conventional cytotoxic combination (trifluridine, a nucleoside analogue) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The published case reports for the combination mention leukopenia and neutropenia |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, plus liver and renal function, as is standard for the combination |
| Handling Protection | Please refer to the package insert; follow cytotoxic drug handling regulations when handling the combination product |

## Safety Considerations

- **Drug Interactions**: 14 interaction records were found. Thirteen are rated Moderate (DDInter). Those listed are:
  - Cimetidine
  - Tafenoquine
  - Ketoconazole
  - Brigatinib
  - Crizotinib
  - Encorafenib
  - Ethinylestradiol
  - Lenvatinib
  - Medroxyprogesterone acetate
  - Megestrol acetate
  - Ribociclib
  - Rucaparib
  - Vandetanib

  The fourteenth is a pharmacology record linking tipiracil to the SARS-CoV-2 non-structural protein 15, which is not a clinical drug interaction.
- **Adverse event report**: A case report describes leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura after trifluridine/tipiracil treatment. Other reported effects of the combination include leukopenia, neutropenia, fatigue, diarrhoea and vomiting.

Warnings and contraindications from the package insert are not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cecum villous adenoma is supported only by the model score, with no trials, no literature and no mechanistic basis. Cytotoxic combination therapy is also hard to justify for a benign lesion that can be resected endoscopically. The other nine predicted indications are likewise Hold. Most are benign colon lesions or re-labellings of the approved colorectal cancer indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian product, which block safety screening.
- Mechanism of action data, for example from DrugBank.
- Any preclinical or clinical evidence specific to cecal villous adenoma. If none exists, consider redirecting effort to malignant colorectal subsets such as rectosigmoid junction neoplasm, where the approved indication may already apply.
- A benefit-risk argument for cytotoxic therapy over endoscopic resection in a benign lesion.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

