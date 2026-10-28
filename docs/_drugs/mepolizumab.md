---
layout: default
title: Mepolizumab
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "Mepolizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Mepolizumab: Thrombocytopenia due to immune destruction
{: .text-alpha }

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but the evidence is very limited: **0 clinical trials** and **1 publication** (a single case report) are available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, mepolizumab is an anti-IL-5 antibody that depletes eosinophils. Its use in eosinophil-driven conditions such as eosinophilic pneumonia and hypereosinophilic syndromes is consistent with this action.

The link to immune-mediated thrombocytopenia is indirect at best. The only supporting report describes a patient with a steroid-resistant hypereosinophilic immune disorder and thrombotic microangiopathy who improved on mepolizumab. This suggests eosinophil-driven immune dysregulation might contribute to some immune-mediated cytopenias in selected hypereosinophilic patients.

There is no evidence that IL-5 blockade acts on the core mechanisms of primary immune thrombocytopenia (autoantibody-mediated platelet destruction and T-cell dysregulation). The high TxGNN score is a computational prediction only and has not been corroborated clinically.

Other predictions from the model show the same pattern, with no supporting evidence:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Primary release disorder of platelets | 0.9961 | L5 | Only a review of hypereosinophilic syndrome that mentions mepolizumab; it does not address platelet function defects |
| Pseudo-von Willebrand disease | 0.9944 | L5 | No plausible link to IL-5 inhibition; no studies |
| Autoimmune thrombocytopenic | 0.9933 | L5 | Likely overlaps with the lead prediction; no direct evidence |
| Glanzmann thrombasthenia | 0.9928 | L5 | An inherited integrin αIIbβ3 defect with no known relationship to IL-5; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells, Molecules & Diseases | A steroid-resistant hypereosinophilic immune disorder, with mixed thrombotic microangiopathy linked to complement activation, resolved with mepolizumab. This is a single case and does not involve primary immune thrombocytopenia. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152267 | Nucala 100mg Injection | Vial of 1 injection | Not available |
| 157788 | Nucala Injection | Pre-filled pen of 1 injection | Not available |

Both licences are valid single-ingredient registrations held by Glaxo SmithKline Pharmaceuticals Ltd.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and one case report in a different disease context (hypereosinophilic disorder with thrombotic microangiopathy). There are no registered trials and no mechanistic rationale for primary immune thrombocytopenia. Evidence is insufficient to justify further investment at this time.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences, since safety screening cannot proceed without them
- Detailed mechanism of action data (for example, from DrugBank)
- Evidence on whether eosinophils or IL-5 play a role in immune thrombocytopenia, such as translational studies or additional case series
- A targeted literature search for mepolizumab in immune-mediated cytopenias, to see whether any clinical signal exists
- Approved indication text for the India licences, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

