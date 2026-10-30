---
layout: default
title: Lornoxicam
parent: High Evidence (L1-L2)
nav_order: 503
evidence_level: L2
indication_count: 8
monitor_inn: "Lornoxicam"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "tendinitis", "myositis fibrosa"]
last_modified_at: 2026-10-30
description: "Lornoxicam: predicted new indication Migraine disorder (evidence level L2). Approved use: Not stated in the licence records compiled for this report (the liter…"
---

# Lornoxicam
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

## Lornoxicam: From Pain and Inflammatory Conditions to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Lornoxicam is a nonsteroidal anti-inflammatory drug (NSAID) of the oxicam class, marketed in India as oral tablets. The TxGNN model predicts it may be effective for **migraine disorder**, supported by **1 Phase 2 clinical trial** and **2 review publications**. The trial studied intravenous lornoxicam, which is a different route from the oral products currently marketed in India.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (the literature describes painful and inflammatory conditions) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L2 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 (the list may be partial) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lornoxicam is not available in the data compiled for this report. Based on general pharmacology, lornoxicam is a potent NSAID that inhibits COX-1 and COX-2, which reduces prostaglandin synthesis. A 1996 review describes it as having analgesic, anti-inflammatory and antipyretic properties, with a relatively short elimination half-life of 3 to 5 hours.

Prostaglandins contribute to neurogenic inflammation and trigeminovascular sensitization in migraine. NSAIDs are an established class of acute migraine therapy, so the mechanism is biologically plausible. A 1992 review of controlled NSAID studies in migraine lists lornoxicam among the NSAIDs tested.

Other predictions from the model are weaker. Migraine with brainstem aura is a subtype of migraine and likely reflects ontology proximity. Headache disorder is a parent category covered by the same trial and literature. Trigeminal autonomic cephalalgia has only a weak rationale. Tendinitis has one study that found lornoxicam inferior to betamethasone. Brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome and myositis fibrosa have no supporting evidence, and the first two appear to be model artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00293657](https://clinicaltrials.gov/study/NCT00293657) | Phase 2 | Completed | 150 | Randomized, double-blind, placebo-controlled single-dose study of intravenous lornoxicam (8 mg or 16 mg) versus placebo for moderate or severe headache of an acute migraine attack. Results are not included in the data compiled for this report. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1495823](https://pubmed.ncbi.nlm.nih.gov/1495823/) | 1992 | Review | Pathologie-biologie | Reviews controlled studies of NSAIDs for acute migraine attacks and long-term prophylaxis. Lornoxicam is among the many NSAIDs tested. |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Review | Drugs | Reviews the pharmacology and therapeutic potential of lornoxicam in painful and inflammatory conditions. This is a general review, not specific to migraine. |

## India Market Information

At least 20 licences are recorded (the list may be partial), all for single-ingredient products in oral tablet form. The licence records contain no approved indication text. Five examples are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 132637 | Lormyp 8mg/325mg Tablet | Strip of 10 tablets | Not stated in the records |
| Registration No. 126438 | Lodol 4mg Tablet | Strip of 10 tablets | Not stated in the records |
| Registration No. 250889 | Zoloxy 8mg Tablet | Strip of 10 tablets | Not stated in the records |
| Registration No. 131888 | Lornok 8mg Tablet | Strip of 10 tablets | Not stated in the records |
| Registration No. 232371 | Univer 4mg Tablet | Strip of 10 tablets | Not stated in the records |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 randomized, placebo-controlled trial directly studies lornoxicam in acute migraine headache, and the NSAID mechanism is plausible. However, there is only one Phase 2 trial, its results are not available here, and it used an intravenous formulation, whereas the products marketed in India are oral tablets.

**To proceed, the following is needed:**
- Results of NCT00293657 (primary endpoint, effect size and safety), and confirmation of its design
- Package insert warnings and contraindications from the India Pharma website, which are currently missing and block safety screening
- Mechanism-of-action data from DrugBank
- A route and dose assessment for oral lornoxicam in acute migraine, since the trial tested the intravenous route
- Confirmatory Phase 3 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

