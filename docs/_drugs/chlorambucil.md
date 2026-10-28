---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 7
monitor_inn: "Chlorambucil"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
last_modified_at: 2026-10-23
description: "Chlorambucil: predicted new indication Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (evidence level L5). Approved use: Hodgkin lymphoma, follicular lymphoma, acute lymphobla…"
---

# Chlorambucil
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

## Chlorambucil: From Hodgkin Lymphoma and Other Lymphoid Malignancies to Pregerminal Center Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma
{: .text-alpha }

## One-Sentence Summary

Chlorambucil is an oral alkylating agent.
The TxGNN model ranks **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)** highest (score 0.9972).
No clinical trials are registered for this disease, and the only literature is **1 indirect review** (2003), so the evidence is prediction-level only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, follicular lymphoma, acute lymphoblastic leukemia, Richter syndrome and related lymphoid malignancies (relations recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 7 of 7) |
| Number of Registrations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorambucil is a nitrogen mustard-type alkylating agent, and its use in lymphoid malignancies is recorded in the knowledge graph. Mechanistically, DNA alkylation could plausibly act on the malignant B-cell clones of CLL/SLL.

The predicted disease is a molecular subtype of CLL/SLL (unmutated immunoglobulin heavy chain variable region genes). The high score probably reflects the association with the parent disease, CLL/SLL, rather than any evidence specific to this subtype. The one retrieved publication is a 2003 review arguing for a risk-adapted approach to CLL. It discusses the disease's biology and prognosis, and it does not test chlorambucil in this subtype. Modern practice has also moved toward targeted agents (BTK and BCL2 inhibitors) for high-risk or unmutated disease.

The other top-ranked predictions have no supporting data in the compiled material. They are the mutated-IGHV CLL/SLL subtype, ALK-positive large B-cell lymphoma, well-differentiated fetal adenocarcinoma of the lung and pulmonary blastoma (all L5). Primary pulmonary lymphoma (L3) and small cell lung carcinoma (L4 as rated in the data, but see the note below) are covered only briefly in the Conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Nederlands tijdschrift voor geneeskunde | CLL is not truly indolent. About 50% of Binet stage A patients need treatment, and two biological subtypes (pre-germinal center, unmutated, versus mutated) support a risk-adapted approach. Chlorambucil is not tested in this paper. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 40820 | Clokeran 2 Tablet | Strip of 30 tablets | Not stated in the licence record |
| 40553 | Celkeran 2 Tablet | Strip of 30 tablets | Not stated in the licence record |
| 185873 | Radix AQ 5mg Tablet | Strip of 30 tablets | Not stated in the licence record |
| 38855 | Clokeran 5mg Tablet | Strip of 30 tablets | Not stated in the licence record |
| 38241 | Celkeran 5mg Tablet | Strip of 30 tablets | Not stated in the licence record |

Seven valid single-ingredient licences are on record in total (the table lists five). No combination products are included.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. The knowledge graph lists neutropenia, thrombocytopenia, leukopenia, anemia and lymphopenia as contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function, renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindicated conditions recorded in the knowledge graph** (not label text): epilepsy, thrombocytopenia, neutropenia, agranulocytosis, anemia, leukopenia, lymphopenia, nephrotic syndrome, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, and acute leukemias (including mixed phenotype acute leukemia).
- **Drug interactions**: 167 interactions were identified in total. Major-level examples are deferiprone and samarium (153Sm) lexidronam, both of which add to myelosuppression risk. Moderate-level examples include amphotericin B (all formulations), mercaptopurine, chloramphenicol, roflumilast, palifermin and strontium-89 chloride. Others, such as warfarin, prednisone and omeprazole, are of unknown severity.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or study in the compiled material tests chlorambucil in this CLL/SLL subtype, so the evidence is limited to the model prediction (L5). The score likely reflects the parent-disease association, and current practice favours targeted agents for unmutated, high-risk disease.

Among the other predictions, primary pulmonary lymphoma has the most support (case reports, retrospective series and a small 1987 phase II study in mixed malignancies), but this is indirect and retrospective, so it is a research question rather than a candidate for action. For small cell lung carcinoma the retrieved material is mostly preclinical or old, and it includes negative results in other lung cancers. This is also weak, and chlorambucil is not part of current standard treatment.

**To proceed, the following is needed:**
- Subtype-specific clinical data (unmutated-IGHV CLL/SLL) comparing chlorambucil with current targeted therapies
- Confirmed approved-indication text from the Indian package inserts
- Mechanism of action data and package insert warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

