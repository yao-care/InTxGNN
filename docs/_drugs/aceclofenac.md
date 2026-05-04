---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenac: From Musculoskeletal Inflammation to Inflammatory Spondylopathy

## One-Sentence Summary

Aceclofenac is an oral NSAID with established international use for musculoskeletal inflammatory conditions including osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis — though it is not currently registered in India.
The TxGNN model's top-ranked predictions are dominated by rare genetic skeletal dysplasias (Ranks 1–6, all L5/Hold); the most clinically actionable prediction is **Inflammatory Spondylopathy** (Rank 8),
with **3 clinical trials** and **17 publications** — including two direct RCTs in ankylosing spondylitis — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal inflammatory pain (OA, RA, AS — established in EU/Asian markets; not registered in India) |
| Predicted New Indication | Inflammatory Spondylopathy (Rank #8 — highest evidence among all predictions) |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on published literature, Aceclofenac is a phenylacetic acid derivative that inhibits both COX-1 and COX-2 enzymes, thereby reducing prostaglandin E2 (PGE₂) synthesis — the primary mediator of inflammation, pain sensitization, and synovial hyperemia in joint disease. This pharmacological profile is extensively documented across multiple decades of clinical trial publications.

Inflammatory spondylopathy encompasses ankylosing spondylitis (AS) and related seronegative spondyloarthropathies, all characterized by chronic immune-driven inflammation at spinal and sacroiliac entheses. Because PGE₂ drives the inflammatory cascade central to spondyloarthritis — including osteoclast activation, periosteal inflammation, and pain amplification via spinal sensitization — COX inhibition by aceclofenac addresses the pathological pathway directly. NSAIDs are internationally recognized as the first-line treatment for axial spondyloarthritis by ASAS and ACR guidelines, making this mechanistic link not merely theoretical but guideline-supported.

Critically, two multicenter comparative RCTs of aceclofenac in active ankylosing spondylitis were published as early as 1996 (PMID 8823692 vs. tenoxicam; PMID 8823693 vs. indomethacin), demonstrating comparable efficacy and tolerability. The TxGNN model's prediction therefore represents a confirmation of established clinical practice in markets where aceclofenac is approved — and an opportunity for India regulatory filing rather than first-in-disease clinical investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00647517](https://clinicaltrials.gov/study/NCT00647517) | Phase 4 | Completed | 60 | Taiwan 12-week RCT evaluating tramadol/APAP as add-on to COX-2 NSAID background therapy in patients with active ankylosing spondylitis or rheumatoid arthritis — directly confirms NSAID use as standard backbone therapy in inflammatory spondylopathy |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Multicenter prospective RCT comparing standard-dose vs. reduced-dose TNF inhibitor in stable AS patients — indirectly confirms AS as the primary clinical subtype of inflammatory spondylopathy under active investigation |
| [NCT02883569](https://clinicaltrials.gov/study/NCT02883569) | N/A | Completed | 1,102 | Large comparative effectiveness study of surgical vs. non-surgical management for low back pain (herniated disc and spinal stenosis) — limited relevance to aceclofenac pharmacotherapy; included for completeness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8823692](https://pubmed.ncbi.nlm.nih.gov/8823692/) | 1996 | RCT | J Rheumatology | Multicenter, double-blind, parallel 3-month RCT: Aceclofenac 100 mg BID vs tenoxicam 20 mg QD in active AS — comparable efficacy and safety profile |
| [8823693](https://pubmed.ncbi.nlm.nih.gov/8823693/) | 1996 | Clinical Trial | J Rheumatology | Multicenter controlled trial: Aceclofenac vs indomethacin in active ankylosing spondylitis — efficacy equivalence established |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | Review | J Pain Research | Comprehensive review of aceclofenac's analgesic and anti-inflammatory effects across musculoskeletal disorders including LBP, OA, RA, and AS; summarizes clinical trial evidence |
| [15163279](https://pubmed.ncbi.nlm.nih.gov/15163279/) | 2004 | Review | Expert Opin Pharmacother | Aceclofenac in inflammatory pain management — >75 million patients treated worldwide; confirms non-inferiority to indomethacin in AS, diclofenac in RA, naproxen in OA |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | Review | Drugs | Reappraisal of aceclofenac in pain and rheumatic disease — covers comparative trial data across OA, RA, and AS with emphasis on GI tolerability advantages |
| [8799688](https://pubmed.ncbi.nlm.nih.gov/8799688/) | 1996 | Review | Drugs | Pharmacodynamic and therapeutic potential review: efficacy equivalent to diclofenac/indomethacin in RA, OA, AS; preclinical data suggests lower GI damage potential than diclofenac |
| [11523298](https://pubmed.ncbi.nlm.nih.gov/11523298/) | 2001 | Review | Rev Med Liege | Critical review of aceclofenac's anti-inflammatory profile — covers COX inhibition, PGE₂ reduction, and cartilage remodeling effects relevant to spondyloarthritis |
| [10081315](https://pubmed.ncbi.nlm.nih.gov/10081315/) | 1999 | Review | Rev Med Liege | Drug profile: indicated for OA, RA, AS, abarticular inflammations, post-trauma inflammations; oral 100 mg BID; favorable GI safety profile |
| [11548913](https://pubmed.ncbi.nlm.nih.gov/11548913/) | 2001 | Cost-effectiveness | PharmacoEconomics | Economic modeling of aceclofenac vs other NSAIDs in OA, RA, and AS — demonstrates favorable cost-effectiveness including mild-to-moderate adverse event costs |
| [23192419](https://pubmed.ncbi.nlm.nih.gov/23192419/) | 2013 | RCT | Clin Rheumatology | Taiwan 12-week double-blind placebo-controlled RCT: tramadol/acetaminophen add-on to ongoing NSAID in 60 active AS patients (BASDAI >3); confirms NSAID as standard backbone in spondyloarthritis management |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal key warnings, contraindications, and drug-drug interaction data were not retrievable from the current data sources.

**Important note for reviewers:** As a member of the NSAID class, aceclofenac carries expected class-level risks including gastrointestinal toxicity (peptic ulceration, GI bleeding), cardiovascular risk (particularly with long-term use), renal impairment, and hypersensitivity reactions in aspirin-sensitive patients. One case report in the literature (PMID 16922973, *JEADV* 2006) documents aceclofenac as a precipitant of generalized pustular psoriasis — a rare but severe adverse event that warrants inclusion in prescriber guidance, particularly relevant given the dermatological overlap in spondyloarthritis patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct multicenter RCTs comparing aceclofenac to active comparators in ankylosing spondylitis (the core subtype of inflammatory spondylopathy) were published in 1996 and demonstrate comparable efficacy to established NSAIDs; this evidence, combined with multiple systematic reviews and a 2021 narrative review, supports an L2 classification. The prediction represents an India regulatory filing opportunity for a pharmacologically well-characterized drug, rather than a first-in-disease investigation.

**To proceed, the following is needed:**

- **Blocking — Regulatory filing strategy for India CDSCO:** Aceclofenac is not currently marketed in India; a regulatory dossier referencing EU and other Asian market approvals must be prepared before any India-specific clinical or commercial activity
- **Blocking — Full package insert safety data (DG001):** Key warnings and contraindications from the approved package insert must be obtained from the TFDA website (or equivalent approved markets) to complete the safety evaluation before S1 safety screening
- **High — Detailed MOA documentation (DG002):** DrugBank API query should be executed to obtain the complete mechanism of action, target profile (COX-1/COX-2 IC₅₀ ratio, metabolite activity), and pharmacokinetic data
- **Medium — Drug-drug interaction profile:** DDI query returned no results; a supplementary query via DrugBank DDI module or clinical pharmacology database is recommended given aceclofenac's broad use in elderly polypharmacy patients
- **Medium — Pediatric safety assessment:** If inflammatory spondylopathy indication includes juvenile-onset AS, pediatric dosing and safety data must be separately evaluated (no data currently available for this subpopulation)
- **Low — Clarify pustular psoriasis risk:** Investigate whether PMID 16922973 represents an isolated case or a known class-effect signal, and determine whether a specific warning is required for patients with concurrent psoriatic spondyloarthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

