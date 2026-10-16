---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glatiramer: predicted new indication Hemoglobinopathy (evidence level L5). Approved use: Not stated in the licence records (the literature indicates use in mu…"
monitor_inn: "Glatiramer"
predicted_indications: ["hemoglobinopathy", "plasma cell myeloma", "female breast carcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "indolent plasma cell myeloma", "gastric linitis plastica", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Glatiramer
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer is an immunomodulatory injectable that is marketed in India and is widely used in multiple sclerosis. The licence records compiled for this report do not state an approved indication, so multiple sclerosis here reflects the published literature rather than the licence text.
The TxGNN model predicts it may be effective for **hemoglobinopathy**, but there are currently **0 clinical trials** and only **1 loosely related publication**. This is a computational prediction only, with no direct supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (the literature indicates use in multiple sclerosis) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Glatiramer is generally described as an immunomodulator that shifts T-cell responses from Th1 toward Th2 and induces regulatory T cells. Its established use is in multiple sclerosis.

No plausible direct link between this mechanism and the pathophysiology of hemoglobinopathy has been established. These disorders mainly involve globin chain imbalance, ineffective erythropoiesis or red cell defects, which an immunomodulator would not be expected to correct. The only retrieved paper describes immune disorders after natalizumab discontinuation in a multiple sclerosis patient who also had beta thalassemia. It does not address treating hemoglobinopathy with glatiramer.

The high TxGNN score therefore reflects a pattern found by the computational model and should not be read as evidence of efficacy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Review/Commentary | Revue neurologique | Case of multiple immune disorders after natalizumab discontinuation in a woman with MS and a history of beta thalassemia; not about treating hemoglobinopathy |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 97885 | Glatirex Injection (Intas Pharmaceuticals Ltd) | Vial of 1 injection | Not stated |
| 98346 | Glataxone Injection (Abbott) | Vial of 1 ml injection | Not stated |
| 98005 | Glatimer 20mg Injection (Natco Pharma Ltd) | Packet of 1 injection | Not stated |
| 99022 | Glatrus 20mg Injection (Taj Pharma India Ltd) | Vial of 1 ml injection | Not stated |

---

## Safety Considerations

- **Drug Interactions**: One interaction is recorded. **Natalizumab** is classed as a **Major** interaction (DDInter).

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature, and there is no plausible mechanistic link between glatiramer's immunomodulatory action and hemoglobinopathy. The other nine predicted indications are also at L4 or L5 evidence, so none currently supports advancing.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications, and the approved indication text, from the India regulatory source
- Preclinical or mechanistic studies showing a rationale for glatiramer in hemoglobinopathy
- A review of the other predicted indications to see whether any has a stronger evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

