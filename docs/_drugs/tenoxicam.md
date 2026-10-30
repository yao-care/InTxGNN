---
layout: default
title: Tenoxicam
parent: Model Prediction Only (L5)
nav_order: 819
evidence_level: L5
indication_count: 8
monitor_inn: "Tenoxicam"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
last_modified_at: 2026-10-30
description: "Tenoxicam: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Tenoxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tenoxicam: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

The TxGNN model's top-ranked predictions are mostly rare congenital conditions with no support, and the only prediction with a direct study is **headache disorder**, backed by **1 clinical trial** (still active, no results) and **2 publications**, so the evidence is limited.

## Quick Overview

The table focuses on **headache disorder**, the only prediction with a direct clinical study. The top-ranked prediction (brachydactyly-syndactyly syndrome, score 0.9980) has no supporting evidence.

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note on the evidence level:** The trial (NCT06786650) studies tenoxicam directly in acute migraine, which falls under headache disorder. However, it is still active, has no results, and no published study of tenoxicam in headache is included. The two publications concern NSAIDs and triptans in general and are indirect. The evidence is therefore reported conservatively as L5 (prediction supported by a registered but unreported trial only) rather than the L3 shown in the compiled scoring data.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Tenoxicam belongs to the oxicam class of NSAIDs, which inhibit cyclooxygenase (COX-1 and COX-2) and reduce prostaglandin synthesis. Its use in arthritic joint disease is recorded in the knowledge graph and is consistent with this anti-inflammatory and analgesic action.

Headache disorders, especially migraine, involve prostaglandin-mediated neurogenic inflammation and sensitization of pain-sensing nerves. NSAIDs as a class are an established option for acute migraine, so the prediction is mechanistically plausible at the class level.

The evidence specific to tenoxicam is thin. One Phase 4 trial compares intravenous tenoxicam with intravenous ibuprofen in acute migraine, but it has not reported results. The supporting literature is indirect.

The other predictions are weaker:
- **Trigeminal autonomic cephalalgia (0.9961)**: biologically adjacent to headache, and indomethacin is a classic responsive agent in some forms, but there are no tenoxicam-specific studies.
- **Alopecia (0.9960)**: the only publication reports alopecia as an *adverse effect* of tenoxicam, which contradicts the prediction.
- **Diffuse alopecia areata (0.9961)**: an autoimmune condition for which NSAIDs are not an established treatment.
- **Brachydactyly-syndactyly syndrome (0.9980), colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9980), hypotrichosis simplex of the scalp (0.9966), congenital hypotrichosis milia (0.9966)**: congenital genetic disorders with no identifiable mechanistic link to COX inhibition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06786650](https://clinicaltrials.gov/study/NCT06786650) | Phase 4 | Active, not recruiting | 100 | Compares the pain-relieving effect and side effects of intravenous tenoxicam versus intravenous ibuprofen in acute migraine attacks; no results reported yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27813032](https://pubmed.ncbi.nlm.nih.gov/27813032/) | 2016 | Cohort | Agri | Compared triptans, NSAIDs and their combination in migraine attacks, including recurrence of headache within an attack |
| [18345416](https://pubmed.ncbi.nlm.nih.gov/18345416/) | 2007 | Review | Arquivos de Neuro-Psiquiatria | Review of 109 patients with acute primary headaches at a university hospital emergency centre; examines features, approach and treatment |
| [9303679](https://pubmed.ncbi.nlm.nih.gov/9303679/) | 1997 | Case report | Atención Primaria | Reports alopecia as a possible adverse effect of tenoxicam (relevant to the alopecia prediction, in the opposite direction) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217961 | Tobitil 20mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the licence record |

## Safety Considerations

Please refer to the package insert for safety information.

Note that one case report (PMID 9303679) describes alopecia as a possible adverse effect of tenoxicam. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only prediction with a direct study is headache disorder, and its single tenoxicam trial is still active with no results. The remaining high-scoring predictions have no clinical or literature support, and the alopecia prediction is contradicted by an adverse-effect report. The model scores alone are not enough to justify moving forward.

**To proceed, the following is needed:**
- Results of NCT06786650 (tenoxicam vs ibuprofen in acute migraine)
- Package insert warnings, contraindications and approved indications from the Indian licence
- Mechanism of action data from DrugBank
- Tenoxicam-specific studies in headache or trigeminal autonomic cephalalgia, if the headache direction is pursued
- No further work on the congenital syndromes, hypotrichosis conditions or alopecia unless new supporting data emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

