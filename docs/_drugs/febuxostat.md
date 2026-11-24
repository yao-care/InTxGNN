---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 340
evidence_level: L4
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Febuxostat"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
description: "Febuxostat: predicted new indication Hypouricemia, renal (evidence level L4). In India: at least 20 listed products"
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Febuxostat: Hypouricemia, renal
{: .text-alpha }

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat hyperuricemia (gout-related high uric acid).
The TxGNN model predicts it may be relevant for **renal hypouricemia**, but only **1 clinical trial** (with an unconfirmed link to this condition) and **2 publications** are available, so the support is weak.
The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a true therapeutic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L4 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for febuxostat: "ULORIC, a xanthine oxidase inhibitor, achieves its therapeutic effect by decreasing serum uric acid. ULORIC is not expected to inhibit other enzymes involved in purine and pyrimidine synthesis and metabolism at therapeutic concentrations." ([DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd), label version 2025-12-24; accessed 2026-11-19.) Febuxostat is known to be a non-purine, selective xanthine oxidase inhibitor that lowers serum uric acid. Its efficacy in hyperuricemia is established, but this does not make it a sensible treatment for the predicted condition.

Renal hypouricemia is a condition in which serum uric acid is already low because the kidney reabsorbs urate poorly (for example, loss of function in URAT1 or GLUT9). Lowering uric acid further has no clear therapeutic rationale and could be harmful. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a true therapeutic link.

The only possible rationale is indirect. Xanthine oxidase inhibition has been proposed to help prevent exercise-induced acute kidney injury, a complication of renal hypouricemia. A 2023 case report describes this idea in a young athlete with familial renal hypouricemia. This remains hypothesis-level.

Two other predictions were also generated: partial HPRT deficiency (Kelley-Seegmiller syndrome) and Lesch-Nyhan syndrome. In both, urate overproduction makes febuxostat plausible for symptom control only (gout and urate nephropathy). It would not address the neurological features. Xanthine accumulation (risk of xanthine nephropathy or stones) is a concern, and evidence is limited to case reports. These are better framed as research questions than as the lead indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with calculi and hyperuricemia. Its link to renal hypouricemia could not be confirmed, so it is likely unrelated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative update on hypouricemia (serum urate < 2 mg/dL) for rheumatologists, covering its causes |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (classified as Review) | Internal Medicine | A 16-year-old footballer with familial renal hypouricemia (URAT1 mutations) and recurrent exercise-induced acute kidney injury; a non-purine xanthine oxidase inhibitor (febuxostat) was considered as prophylaxis when hydration failed |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 68591 | Davstat 40 Tablet | Strip of 10 tablets | Valid |
| 76843 | Endeavours Furic 40mg Tablet | Strip of 10 tablets | Valid |
| 78762 | Ebuxo 120mg Tablet | Strip of 10 tablets | Valid |
| 84255 | Feboxa 40 Tablet | Strip of 10 tablets | Valid |
| 86019 | Febugenix 40mg Tablet | Strip of 10 tablets | Valid |
| 86025 | Febustar 40mg Tablet | Strip of 10 tablets | Valid |
| 87331 | Feboxit 40 Tablet | Strip of 10 tablets | Valid |
| 89118 | Fablen 40mg Tablet | Strip of 10 tablets | Valid |
| 89123 | Febuwin 80mg Tablet | Strip of 10 tablets | Valid |
| 89620 | Febumat 40mg Tablet | Strip of 10 tablets | Valid |
| 90110 | Fabnar 40mg Tablet | Strip of 10 tablets | Valid |
| 90669 | Febumed 40mg Tablet | Strip of 10 tablets | Valid |
| 91353 | Febunip 80mg Tablet | Strip of 10 tablets | Valid |
| 91492 | Febtac 40mg Tablet | Strip of 10 tablets | Valid |
| 91671 | Febuglob 40mg Tablet | Strip of 10 tablets | Valid |
| 119628 | Kinuxo 40mg Tablet | Strip of 10 tablets | Valid |
| 231672 | Uricrak 40mg Tablet | Strip of 10 tablets | Valid |
| 232083 | Uroxtat 40mg Tablet | Strip of 10 tablets | Valid |
| 232123 | Urifrain 40 Tablet | Strip of 10 tablets | Valid |
| 232920 | Uroxtat 80mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid single-ingredient oral tablets (40 mg, 80 mg and 120 mg strengths).

## Safety Considerations

- **Drug Interactions**: 22 interactions were identified. The major-level ones are:
  - Mercaptopurine
  - Azathioprine
  - Leflunomide
  - Teriflunomide

  Moderate-level interactions include theophylline and related xanthines (dyphylline, aminophylline, oxtriphylline), methotrexate, tioguanine, clofarabine, epirubicin, trabectedin, asparaginase and pegaspargase, brentuximab vedotin, naltrexone, and interferon beta products.
- **Knowledge-graph contraindication signals** (not label text): stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, and hemoglobinopathy. These cardiovascular and cerebrovascular signals should be checked against the official label.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic logic argues against further urate lowering in renal hypouricemia, the only trial found is probably unrelated, and the only supporting literature is a review and a single case report. The high TxGNN score is not backed by real evidence (Evidence Level L4).

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Clarification of whether the actual research question is exercise-induced acute kidney injury prevention in renal hypouricemia, or urate control in HPRT deficiency or Lesch-Nyhan syndrome (the latter two are better framed as research questions)
- Controlled data on febuxostat use in these conditions, including safety regarding xanthine accumulation and cardiovascular risk

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

