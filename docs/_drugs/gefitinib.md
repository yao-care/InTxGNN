---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gefitinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: Non-small cell lung cancer / lung cancer"
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but this is a computational prediction only,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer / lung cancer (from the knowledge graph; the Indian licence records contain no indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, gefitinib is an oral EGFR tyrosine kinase inhibitor, its efficacy in EGFR-mutated non-small cell lung cancer is well established, and mechanistically it might be applicable to conditions driven by EGFR-mediated cell proliferation.

Gingival fibromatosis is a fibrotic overgrowth of gum tissue and is very different from lung cancer. The only link suggested is that EGFR signalling could contribute to fibroblast proliferation. This is speculative: no trial or publication in the data supports it, and the high TxGNN score is a model output alone.

Among the other top-ranked predictions, only a few have any literature, and that literature mostly concerns gefitinib's existing use in lung cancer, resistance mechanisms or adverse effects. It does not show a new therapeutic use. For example, the lung hilum carcinoma and pulmonary sulcus neoplasm predictions largely restate the approved NSCLC use, and some matches are plainly spurious (a formulation paper matched to "lung germ cell tumor" because of the word "germ").

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## India Market Information

Gefitinib has 20 valid single-ingredient registrations in India and no combination or cancelled registrations. The records contain no approved-indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 109077 | Iressa 250mg Tablet (AstraZeneca) | Box of 30 tablets | Not stated in the records |
| Registration No. 94713 | Gefticip Tablet (Cipla Ltd) | Strip of 30 tablets | Not stated in the records |
| Registration No. 99608 | Grexam 250mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 30 tablets | Not stated in the records |
| Registration No. 95429 | Geffy 250mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 66935 | Denrit 250mg Tablet (Pfizer Ltd) | Strip of 10 tablets | Not stated in the records |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function and respiratory symptoms (suggested by the contraindication-related disease associations and the case literature on pneumonitis); please also refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis, postinflammatory pulmonary fibrosis. Published case reports describe gefitinib-induced acute pneumonitis and interstitial lung disease, including a fatal case.
- **Other safety signals in the literature**: cutaneous toxicity (acneiform eruption, paronychia, xerosis), experimental evidence of QT prolongation, and a case report of recurrent myocardial infarction. The cutaneous toxicity is particularly relevant to any use in skin or mucosal disorders.
- **Drug Interactions**: 349 interactions were identified. The main moderate-level ones are:
  - Acid-suppressing drugs: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Clarithromycin
  - Aprepitant
  - Dexamethasone
  - Naltrexone
  - Azole antifungals (miconazole, clotrimazole)
  - Troglitazone

Package-insert warnings and contraindications were not available for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no clinical trials or literature and only a speculative mechanistic link. Gefitinib also carries known pulmonary, skin and liver safety concerns that would need to be weighed against any benefit in a non-malignant condition.

**To proceed, the following is needed:**
- Mechanism of action data (from DrugBank)
- Package insert warnings and contraindications (from the Indian regulatory source), which are required before safety screening can proceed
- Preclinical or mechanistic evidence that EGFR inhibition affects gingival fibroblast proliferation
- Review of the other top-ranked predictions: lung hilum carcinoma and pulmonary sulcus neoplasm have some indirect literature (Evidence Level L4) but mainly reflect the existing NSCLC use rather than a new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

