---
layout: default
title: Romiplostim
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Romiplostim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Idiopathic aplastic anemia, aplastic anemia…"
monitor_inn: "Romiplostim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
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

## Romiplostim: From Immune Thrombocytopenia and Aplastic Anemia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Romiplostim is a thrombopoietin receptor (MPL) agonist, originally used for autoimmune thrombocytopenia (immune thrombocytopenic purpura, ITP) and listed in the knowledge graph for aplastic anemia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are currently **0 clinical trials** and **1 publication** (basic in vitro research on ITP, not directly on this condition), so this prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic aplastic anemia, aplastic anemia, autoimmune thrombocytopenia (from the knowledge graph; the Indian license records contain no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, romiplostim is a peptide that binds the thrombopoietin receptor (MPL) and stimulates megakaryocyte proliferation and platelet production. It is used to raise platelet counts in chronic ITP, a disease in which platelets are destroyed by autoantibodies.

The predicted indication is a platelet *function* disorder, in which the defect lies in platelet release or activity rather than in low production. Raising platelet count would therefore be unlikely to correct the underlying defect. The single retrieved paper (PMID 25682608) shows that ITP autoantibodies inhibit proplatelet formation, which is relevant to ITP, not to this condition. The very high score most likely reflects network proximity to thrombocytopenia-related nodes in the knowledge graph rather than a true mechanistic fit.

### Other Top-Ranked Predictions (for context)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Pseudo-von Willebrand disease | 99.9998% | L5 | No data; benefit-risk uncertain with hyper-reactive platelets |
| 3 | Glanzmann thrombasthenia | 99.9995% | L5 | Qualitative defect with normal counts; weak rationale |
| 4 | Fetal and neonatal alloimmune thrombocytopenia | 99.9873% | L4 | Only indirect evidence from ITP; Research Question |
| 5 | Scott syndrome | 99.9666% | L5 | Procoagulant defect with normal counts; weak rationale |
| 6 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.9529% | L5 | Plausible but subtype-dependent; Research Question |
| 7 | Bleeding diathesis due to a collagen receptor defect | 99.9508% | L5 | Function defect; weak rationale |
| 8 | Platelet-type bleeding disorder | 99.9319% | L5 | Too non-specific to assess |
| 9 | Autosomal dominant macrothrombocytopenia | 99.8807% | L5 | Plausible in selected patients; Research Question |
| 10 | Ehlers-Danlos syndrome, fibronectinemic type | 99.8452% | L5 | No plausible link; likely graph artifact |

Among these, the constitutional thrombocytopenias, autosomal dominant macrothrombocytopenia, and fetal/neonatal alloimmune thrombocytopenia are mechanistically more plausible than the top-ranked prediction, but none has direct supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (primary release disorder of platelets):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic research (in vitro) | Haematologica | Antiplatelet autoantibodies from ITP patients inhibit proplatelet formation by megakaryocytes and impair platelet production; relevant to ITP, not to platelet release disorders |

For the fourth-ranked prediction (fetal and neonatal alloimmune thrombocytopenia), only indirect evidence from related immune thrombocytopenias is available:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31239245](https://pubmed.ncbi.nlm.nih.gov/31239245/) | 2019 | Review | Blood Advances | Romiplostim in pediatric ITP: drug development and current practice; FDA approved use in children ≥1 year in December 2018 |
| [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/) | 2021 | Case report | BMJ Case Reports | Management of refractory ITP in pregnancy |
| [20410910](https://pubmed.ncbi.nlm.nih.gov/20410910/) | 2010 | Review | J Perinatol | Whether novel thrombopoietic agents could reduce platelet transfusions in neonates |
| [23257464](https://pubmed.ncbi.nlm.nih.gov/23257464/) | 2012 | Review | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Advances in thrombopoietic drugs for childhood immune thrombocytopenia |
| [23822831](https://pubmed.ncbi.nlm.nih.gov/23822831/) | 2013 | Case report | Eur J Haematol | Complete remission of refractory ITP after a short course of romiplostim |
| [27605856](https://pubmed.ncbi.nlm.nih.gov/27605856/) | 2016 | Case report | Asian J Transfus Sci | Refractory ITP in pregnancy managed with eltrombopag (a different TPO-RA) |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 184222 | Romy Injection (Intas Pharmaceuticals Ltd) | Vial of 0.5 ml injection | Not stated in the records |
| 185412 | Romiset 125mcg Injection (Alkem Laboratories Ltd) | Vial of 1 injection | Not stated in the records |
| 836 | Augplat 250mcg Injection (Zydus Cadila) | Vial of 1 injection | Not stated in the records |
| 184776 | Romiset Injection (Alkem Laboratories Ltd) | Vial of 1 injection | Not stated in the records |
| 185051 | Romiset 500mcg Injection (Alkem Laboratories Ltd) | Vial of 1 injection | Not stated in the records |

All five registrations are valid single-ingredient injectable products.

---

## Safety Considerations

- **Drug Interactions**: Carfilzomib (Major severity, per DDInter). Romiplostim also acts on its pharmacological target, the thrombopoietin receptor (MPL).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, primary release disorder of platelets, has no clinical trials and no directly relevant literature. A drug that increases platelet number is unlikely to fix a platelet function defect. The high TxGNN score appears to reflect graph proximity rather than biological fit.

**To proceed, the following is needed:**
- Mechanism of action data to support a mechanistic-link analysis
- Package insert warnings and contraindications from the Indian regulatory sources (a blocking gap for safety screening)
- Approved indication text for the Indian registrations
- If pursuing the area, prioritize subtype-specific investigation of constitutional thrombocytopenias, autosomal dominant macrothrombocytopenia, and fetal/neonatal alloimmune thrombocytopenia (all flagged as Research Questions), rather than platelet function disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

