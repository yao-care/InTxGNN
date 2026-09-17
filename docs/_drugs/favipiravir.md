---
layout: default
title: Favipiravir
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 3
---

# Favipiravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Favipiravir: From Influenza to Infection-Associated Hemophagocytic Syndrome

## One-Sentence Summary

Favipiravir is an RNA-dependent RNA polymerase (RdRp) inhibitor originally developed as an antiviral for novel and re-emerging influenza virus infections. The TxGNN model predicts a possible role in **hemophagocytic syndrome associated with an infection**, but this is currently supported only by **2 review-type publications** and **no clinical trials**, and a blocking data gap in TFDA label safety information prevents full evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (novel/re-emerging influenza virus infection) — not present in current Taiwan regulatory data; based on general drug knowledge |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 (mechanism/review-level literature only, no clinical trials) |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for favipiravir is not available in this evidence pack. Based on known information, favipiravir is an RdRp inhibitor with established antiviral activity against RNA viruses, including bunyaviruses such as SFTS virus (SFTSV) and Heartland virus (HRTV).

The mechanistic rationale is indirect rather than direct: SFTSV and HRTV infections are known to trigger secondary (infection-associated) hemophagocytic lymphohistiocytosis (HLH) through virus-driven immune hyperactivation. The proposed pathway is "suppress viral replication → reduce the infectious trigger → reduce secondary immune hyperactivation," not a direct immunomodulatory effect of favipiravir on macrophage/lymphocyte activation. The high TxGNN score (99.41%) most likely reflects a drug–disease co-occurrence pattern in the knowledge graph (antiviral drugs linked to infection-triggered HLH) rather than direct pharmacological evidence.

It is worth noting that TxGNN generated two additional candidates for favipiravir — "acquired HLH associated with malignant disease" and "fatal infantile cardioencephalomyopathy due to cytochrome c oxidase deficiency" — both scored similarly high but have no supporting literature or trials and no plausible mechanistic link to favipiravir's antiviral activity. These were excluded from further consideration as likely model noise, leaving infection-associated HLH as the only candidate with any supporting rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30098914](https://pubmed.ncbi.nlm.nih.gov/30098914/) | 2018 | Review | Journal of Infection and Chemotherapy | Reviews pathophysiology of severe fever with thrombocytopenia syndrome (SFTS), a tick-borne bunyavirus infection that can progress to hemophagocytic syndrome, and discusses development of specific antiviral therapy |
| [38399689](https://pubmed.ncbi.nlm.nih.gov/38399689/) | 2024 | Review | Microorganisms | Reviews Heartland virus disease, a related tick-borne bunyavirus infection presenting with fever, leukopenia and thrombocytopenia consistent with a hemophagocytic-syndrome-like picture |

Note: neither publication directly studies favipiravir treatment of hemophagocytic syndrome — both are background reviews of the underlying viral infections that can trigger it.

---

## Taiwan Market Information

Favipiravir is not currently marketed in Taiwan (0 registrations); no license information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

(Note: TFDA label warnings/contraindications for favipiravir are a **blocking data gap** — this has not yet undergone S1 safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature evidence consists of two background reviews on related viral infections (SFTS, Heartland virus disease), not direct studies of favipiravir in hemophagocytic syndrome, and no clinical trials exist for this indication. In addition, TFDA label safety data (warnings/contraindications) is missing and is flagged as a blocking gap, which prevents the candidate from proceeding to initial safety evaluation (S1).

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action data (DG002)
- Preclinical or case-level evidence directly linking favipiravir treatment to resolution of infection-associated HLH (e.g., in SFTS or Heartland virus disease patients)
- Clarification of favipiravir's original approved indication and licensing status, since no Taiwan regulatory record currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

