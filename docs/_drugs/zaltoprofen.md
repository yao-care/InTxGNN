---
layout: default
title: Zaltoprofen
parent: Model Prediction Only (L5)
nav_order: 902
evidence_level: L5
indication_count: 8
monitor_inn: "Zaltoprofen"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "tendinitis", "idiopathic granulomatous myositis"]
last_modified_at: 2026-10-23
description: "Zaltoprofen: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the licence record"
---

# Zaltoprofen
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

## Zaltoprofen: From an NSAID with No Recorded Indication Text to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Zaltoprofen is a nonsteroidal anti-inflammatory drug (NSAID) with one valid single-ingredient registration in India, though the licence record contains no approved-indication text.
The TxGNN model predicts it may be useful for **migraine disorder**, but **no clinical trials and no publications** directly study this use.
The prediction rests on drug-class reasoning and model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence record |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Zaltoprofen is classed as an NSAID. It is reported to inhibit cyclooxygenase (COX), with a preference for COX-2, and to have bradykinin-related analgesic activity. These properties are inferred from the drug class rather than from supplied label data.

Reducing prostaglandin-driven inflammation and pain could plausibly ease headache pain, including neurogenic inflammation in migraine. This is the main basis for the prediction. It is a class-level argument, not evidence that zaltoprofen works in migraine.

Several other top-ranked predictions look like TxGNN model (deep learning) artifacts rather than real signals. Brachydactyly-syndactyly syndrome and colobomatous microphthalmia-rhizomelic dysplasia syndrome are congenital developmental conditions with no apparent link to NSAID pharmacology. Related headache predictions (migraine with brainstem aura, headache disorder, trigeminal autonomic cephalalgia) share the same weak, class-based reasoning. For trigeminal autonomic cephalalgia, NSAIDs generally have limited efficacy apart from indomethacin-responsive variants.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for migraine disorder.

Across the lower-ranked predictions, one publication was supplied, listed under tendinitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30738433](https://pubmed.ncbi.nlm.nih.gov/30738433/) | 2019 | RCT protocol | BMC Musculoskelet Disord | Protocol for a randomized, placebo-controlled, double-blind phase II study of zaltoprofen in diffuse-type and unresectable localized tenosynovial giant cell tumors. It does not directly address tendinitis or migraine. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 248794 | ZP 80mg Tablet (Wezen Chemicals Pvt Ltd) | Strip of 10 tablets | Not stated in the licence record |

This is a single-ingredient oral product. The only registration is valid.

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found, and the knowledge graph lists no contraindicated diseases for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication directly studies zaltoprofen in migraine disorder, so the evidence level is L5. The prediction is supported only by NSAID class reasoning and a high model score. Safety data and mechanism data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registration (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Approved-indication text for the Indian product
- A targeted search for studies of zaltoprofen in migraine or headache
- Clarification of the migraine-versus-NSAID-class question, including comparison with established migraine NSAIDs
- Review of PMID 30738433 only as an indirect lead, since it concerns tenosynovial giant cell tumor rather than tendinitis or migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

