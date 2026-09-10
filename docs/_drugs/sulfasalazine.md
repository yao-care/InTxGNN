---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using no additional skills — this is a direct content-generation task with a fully specified template; I'll follow it exactly.

---

# Sulfasalazine: From Rheumatoid Arthritis to Osteoarthritis

## One-Sentence Summary

Sulfasalazine is a long-established disease-modifying antirheumatic drug (DMARD), traditionally used for rheumatoid arthritis and inflammatory bowel disease. The TxGNN model predicts it may also be effective for **Osteoarthritis**, and this is currently the only prediction among the top 10 TxGNN hits that is supported by actual evidence — **2 clinical trials** and **20 publications** (mostly preclinical/mechanistic), rather than raw model score alone.

> **Note on candidate selection**: The raw top-ranked TxGNN prediction for sulfasalazine (score 99.94%, "brachydactyly-syndactyly syndrome") and several others in the top 10 (ranks 1–4, 6, 7, 9, 10) have **zero clinical trials or literature support** and are flagged in the evidence pack itself as likely knowledge-graph embedding artifacts with no plausible biological link. This report instead focuses on **osteoarthritis (rank 5)**, the highest-ranked prediction that is actually corroborated by mechanistic and preclinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / Ulcerative colitis (established pharmacological use; not provided in evidence pack — original_indications field empty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, sulfasalazine is a prodrug combining sulfapyridine and 5-aminosalicylic acid (5-ASA), classified as a DMARD and 5-ASA compound. Its efficacy in rheumatoid arthritis and inflammatory bowel disease is well established, and mechanistically it may extend to osteoarthritis, a condition increasingly recognized as having a significant inflammatory (not purely mechanical) component.

Per the repurposing rationale in the evidence pack: sulfasalazine inhibits the NF-κB pathway, reducing pro-inflammatory cytokines (TNF-α, IL-1, IL-6). Preclinical literature shows this can reduce cytokine-induced cartilage degradation and proteoglycan/collagen release, and an ACL-transection animal model demonstrated attenuated cartilage destruction with sulfasalazine treatment via inhibition of the cystine/glutamate antiporter system. This gives biological plausibility to the OA hypothesis.

However, the currently available clinical trials (NCT00551707, NCT03975790) are primarily conducted in rheumatoid arthritis populations, not osteoarthritis specifically, and neither directly tests sulfasalazine as the primary intervention in an OA population. The evidence is therefore mechanistic/preclinical rather than confirmatory clinical evidence, consistent with the assigned L3 evidence level.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | Completed | 51 | RCT of CRx-102 (dipyridamole + low-dose prednisolone) in active rheumatoid arthritis; anti-inflammatory synergy mechanism relevant to arthritis but not a direct sulfasalazine/OA study (relevance grade B) |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Completed | 479 | Retrospective claims-database study comparing tofacitinib+MTX continuation vs. MTX withdrawal in RA patients; population is RA, not OA, and does not evaluate sulfasalazine directly (relevance grade C) |

*No clinical trial in this evidence pack directly evaluates sulfasalazine in an osteoarthritis population.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical/In vivo | Int J Biol Macromol | Sulfasalazine-loaded hyaluronic acid reduced inflammation and cartilage degradation in an MIA-induced rat OA model |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical/Animal model | J Orthop Res | Sulfasalazine attenuated cartilage destruction in ACL-transection/menisectomy OA model via cystine/glutamate antiporter inhibition |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | In vitro | Mod Rheumatol | Sulfasalazine and tofacitinib alter protein profile of articular chondrocytes |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | In vitro | Rheumatology (Oxford) | Sulfasalazine blocked cytokine-stimulated release of proteoglycan/collagen from cartilage and down-regulated metalloproteinases |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Basic pharmacology | Wien Klin Wochenschr | Sulfasalazine and metabolites reduced leukotriene/prostaglandin release from synovial tissue of OA, RA, and chondrocalcinosis patients |
| [12205730](https://pubmed.ncbi.nlm.nih.gov/12205730/) | 2002 | Clinical (RA cohort) | Yonsei Med J | Sulphasalazine treatment reduced urinary collagen crosslink excretion, a marker of joint connective tissue turnover, in RA patients |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Review of ferroptosis in inflammatory arthritis including osteoarthritis pathogenesis |
| [11478054](https://pubmed.ncbi.nlm.nih.gov/11478054/) | 2001 | Review | Hand Clin | Review of pharmacologic treatment options for OA and RA |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | Review of clinical trials across rheumatic diseases including OA |

## India Market Information

Sulfasalazine is currently **not marketed in India**; the evidence pack contains no registration records (total_licenses = 0).

## Safety Considerations

**Drug Interactions**: The evidence pack records 404 total drug-drug interactions. Notable **Major**-level interactions include:
- Prilocaine (topical)
- Human immunoglobulin G (intravenous)
- Methenamine

Common **Moderate**-level interactions include NSAIDs (ketorolac, ibuprofen, celecoxib), aminoglycosides (amikacin), amphotericin B, azathioprine, and hormonal agents (ethinylestradiol, estradiol). A **Minor** interaction is noted with folic acid (relevant given sulfasalazine's known effect on folate absorption).

*Key warnings and contraindications data are not available in this evidence pack (Blocking-severity data gap — TFDA/regulatory label not yet obtained).*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the osteoarthritis indication is limited to preclinical, in vitro, and mechanistic studies (L3) — no completed trial has evaluated sulfasalazine directly and primarily in an OA population. Combined with a Blocking-severity data gap on the drug's safety label (contraindications/warnings) and its unmarketed status in India, the current evidence does not support progression beyond a research question.

**To proceed, the following is needed:**
- TFDA/reference-agency package insert (warnings, contraindications) to complete the S1 safety pre-assessment
- Confirmed mechanism of action data from DrugBank
- A dedicated Phase 2/3 RCT of sulfasalazine specifically in an osteoarthritis population (current trials are RA-focused)
- Clarification of the drug's original approved indications, which are absent from the current evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

