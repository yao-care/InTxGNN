---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Febuxostat: From Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a non-purine selective xanthine oxidase inhibitor (XOI) internationally used to lower serum uric acid in hyperuricemia and gout. The TxGNN model predicts a possible new role in **Renal Hypouricemia** — not as a treatment for the low uric acid itself, but as a candidate for preventing exercise-induced acute kidney injury (EIAKI) in these patients. Evidence is currently limited: **1 clinical trial** (relevance unconfirmed) and **2 review-level publications** support this direction, with no completed RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack — no India license records exist (drug is not marketed). Internationally, Febuxostat is approved as a xanthine oxidase inhibitor for hyperuricemia/gout. |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. Based on known pharmacology referenced in the repurposing rationale, Febuxostat is a non-purine selective xanthine oxidase inhibitor (XOI) whose established efficacy is in lowering uric acid production for hyperuricemia and gout.

Renal hypouricemia (RHUC) is, mechanistically, the opposite clinical picture — patients carry defects in urate transporters (e.g., URAT1) that cause abnormally *low* serum uric acid. The connection to Febuxostat is not through uric-acid lowering, but through a secondary consequence of RHUC: patients are prone to exercise-induced acute kidney injury (EIAKI), a phenomenon thought to involve a post-exercise surge in xanthine oxidase activity and associated reactive oxygen species generation. By inhibiting xanthine oxidase, Febuxostat may blunt this oxidative pathway and protect renal function during strenuous exercise.

This is therefore a "enzyme-inhibition protection" hypothesis rather than a direct extension of the uric-acid-lowering indication — mechanistically plausible given Febuxostat's known XOI activity, but still at the case-report/mechanistic-reasoning stage rather than a validated indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study (Dept. of Urology, Shanghai Xu-hui Central Hospital) exploring effects of uric acid control on stone recurrence and renal function in hyperuricemic patients with calculi; relevance to Febuxostat in renal hypouricemia/EIAKI is unconfirmed — trial title does not clarify intervention design and requires manual verification. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review | Internal Medicine (Tokyo) | Case of a 16-year-old athlete with familial renal hypouricemia (compound heterozygous URAT1 mutations) and recurrent EIAKI; discusses possible use of non-purine selective XOIs, including febuxostat, for EIAKI prevention when hydration prophylaxis fails. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate < 2 mg/dL), covering etiology and clinical management relevant to rheumatologists. |

---

## India Market Information

Febuxostat currently has no India registration or marketing authorization on file (0 licenses recorded).

---

## Safety Considerations

- **Drug Interactions**: 22 documented interactions on file. Notable **Major**-level interactions include: Mercaptopurine, Azathioprine, Leflunomide, and Teriflunomide (source: DDInter). **Moderate**-level interactions include theophylline-class agents (Theophylline, Aminophylline, Oxtriphylline, Dyphylline), Methotrexate, Naltrexone, and several immunomodulators/antineoplastics (Brentuximab vedotin, Clofarabine, Pegaspargase, Trabectedin, Epirubicin, Interferon beta-1a/1b, Peginterferon beta-1a, Asparaginase E. coli, Tioguanine).

Detailed prescribing warnings and contraindications are not yet available (blocking data gap — see below) and must be obtained from the official India/TFDA label before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the renal-hypouricemia/EIAKI-prevention hypothesis rests on two review articles and one clinical trial of unconfirmed relevance — no completed RCTs exist, and the mechanistic link, while plausible, is inferred rather than directly demonstrated (Evidence Level L4, Decision Stage S0). Two related but even lower-evidence candidates (HPRT partial deficiency, Lesch-Nyhan syndrome) were also identified, both also rated Hold, supported only by case reports.

**To proceed, the following is needed:**
- Official India/TFDA label data (key warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank — currently a **High**-severity data gap (DG002)
- Manual verification of NCT04398251's actual relevance to renal hypouricemia/EIAKI (title alone is inconclusive)
- Prospective or case-series data specifically evaluating Febuxostat for EIAKI prevention in confirmed RHUC patients, rather than extrapolation from single case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

