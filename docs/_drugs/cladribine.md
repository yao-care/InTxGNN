---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cladribine: predicted new indication Parameningeal embryonal rhabdomyosarcoma (evidence level L5). Approved use: Hairy cell leukemia, hairy cell leukemia variant…"
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog originally used for hairy cell leukemia (including its variant) and relapsing-remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
but **no clinical trials and no directly relevant publications** currently support this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukemia, hairy cell leukemia variant, relapsing-remitting multiple sclerosis (from the knowledge graph; the India license text has no indication recorded) |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cladribine is a purine nucleoside analog. It is cytotoxic to lymphocytes through activation by deoxycytidine kinase, which disrupts DNA synthesis. Its efficacy in hairy cell leukemia, a lymphoid malignancy, is established.

The link to rhabdomyosarcoma is weak. Rhabdomyosarcoma is a solid tumor of soft tissue, and no mechanistic rationale for a lymphocyte-directed purine analog in this setting is documented. The high score most likely reflects proximity in the knowledge graph to the broader rhabdomyosarcoma/sarcoma disease nodes rather than a specific biological mechanism. The same pattern appears in the other top predictions: prostate, vaginal (botryoid), and bile duct embryonal subtypes, the parent term "rhabdomyosarcoma", and liver sarcoma. These all score between 99.7% and 99.8% and probably share one ontology-driven signal. Any further work would need preclinical validation first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead predicted indication.

For the seventh-ranked prediction (liver sarcoma), one paper was retrieved: [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) (2004, case report, *Der Hautarzt*). It describes successful cladribine therapy in smoldering systemic mastocytosis, a hematologic neoplasm. It is most likely a retrieval mismatch and does not support liver sarcoma or rhabdomyosarcoma.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 37767 | Cladrim 10mg Injection (Fresenius Kabi India Pvt Ltd) | Vial of 1 injection | Not recorded in the available data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | High. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anemia among its contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function; neurological assessment given the peripheral neuropathy signal |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindicated conditions (knowledge-graph associations, not label text)**: kidney disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, anemia (including macrocytic anemia), peripheral nervous system disease, peripheral neuropathy, hyperuricemia.
- **Drug Interactions**: 344 interactions were found. Major interactions include:
  - Corticosteroids: hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone, prednisone
  - Deferiprone
  - Radiopharmaceuticals and radioimmunotherapies: ibritumomab tiuxetan, iobenguane (I-131), tositumomab (with and without I-131), samarium (153Sm) lexidronam, strontium chloride Sr-89

  Moderate interactions include palifermin, dipyridamole, cilostazol and eltrombopag.

Package insert warnings and contraindications for the India product were not available. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5), with no clinical trials and no relevant literature. There is no demonstrated mechanistic link between cladribine and rhabdomyosarcoma, and the drug carries substantial myelosuppression and neurotoxicity concerns.

**To proceed, the following is needed:**
- Preclinical evidence (cell-line or xenograft data) of cladribine activity in rhabdomyosarcoma models
- Detailed mechanism of action data, to assess whether deoxycytidine kinase-dependent activity is relevant in this tumor type
- India package insert warnings and contraindications, which are required before any safety screening
- Confirmation of the approved indication text for the India license
- A systematic literature search targeted at rhabdomyosarcoma and nucleoside analogs, since the one retrieved paper is off-target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

