---
layout: default
title: Flurbiprofen
parent: High Evidence (L1-L2)
nav_order: 368
evidence_level: L1
indication_count: 10
---

# Flurbiprofen
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Flurbiprofen: From NSAID Anti-Inflammatory Therapy to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen (DrugBank DB00712) is a conventional NSAID (COX-1/COX-2 inhibitor) historically used for inflammatory pain conditions such as rheumatoid arthritis and osteoarthritis. The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, and unlike the model's top-ranked prediction, this indication is backed by **20 published studies (including at least 8 randomized controlled trials)** from the 1970s–1980s, even though none are registered in modern clinical trial databases.

> **Note on indication selection:** TxGNN's raw ranking placed several ultra-rare genetic skeletal dysplasias (e.g., acromesomelic dysplasia, brachydactyly-syndactyly syndrome) above Ankylosing Spondylitis by score alone. Those top-ranked predictions have **zero clinical trials, zero literature, and no plausible mechanistic link** to an NSAID (scored L5/Hold in the evidence pack). Ankylosing Spondylitis (rank 8, score 99.97%) is the only prediction with substantive evidence and is therefore the focus of this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured TFDA licensing data (drug not currently marketed in Taiwan); historically used as an NSAID for rheumatoid arthritis, osteoarthritis, and related inflammatory pain per literature evidence |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank structured fields for this drug (data gap DG002). Based on the evidence pack's own repurposing rationale, however, Flurbiprofen is a conventional NSAID that inhibits cyclo-oxygenase (COX-1/COX-2), reducing prostaglandin synthesis and thereby producing analgesic and anti-inflammatory effects.

NSAIDs are a well-established first-line symptomatic treatment class for spondyloarthropathies, including ankylosing spondylitis — this is not a novel mechanistic hypothesis but a therapeutic use already documented in the older medical literature, predating modern clinical trial registries. The mechanistic link is direct: the same anti-inflammatory pathway that supports Flurbiprofen's traditional use in rheumatoid and degenerative joint disease extends naturally to axial spondyloarthritis.

A closely related prediction in the same evidence pack, "spondyloarthropathy, susceptibility to" (rank 7, L4, decision stage S1, "Research Question"), reinforces this signal — it sits in the same disease family as ankylosing spondylitis but currently lacks direct trial or literature support of its own.

## Clinical Trial Evidence

Currently no related clinical trials registered (all supporting evidence predates modern trial registries such as ClinicalTrials.gov and ICTRP; see Literature Evidence below).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT | British Medical Journal | Double-blind crossover in 35 AS patients: flurbiprofen (150mg/day) well tolerated, efficacy approaching phenylbutazone (300mg/day) |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT | Annals of the Rheumatic Diseases | Double-blind crossover comparing indomethacin, flurbiprofen, and placebo in AS |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT | Current Medical Research and Opinion | Parallel double-blind trial, 26 AS patients: flurbiprofen (150-200mg/day) equally effective as indomethacin, no withdrawals for lack of efficacy |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT | Southern Medical Journal | Companion report of the above trial: flurbiprofen and indomethacin equally effective relieving pain/tenderness in 26 active AS patients |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT | European Journal of Clinical Pharmacology | Double-blind parallel trial, 27 AS patients: flurbiprofen vs phenylbutazone equally effective; phenylbutazone favored on subjective improvement but not statistically significant |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT | The New Zealand Medical Journal | 4-week double-blind crossover, 30 AS patients: flurbiprofen 200mg/day vs naproxen 750mg/day, comparable efficacy; more side effects with flurbiprofen |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT | The American Journal of Medicine | Randomized double-blind study, 57 AS patients over 26 weeks: flurbiprofen 200mg/day effective for pain control, some patients controlled on 100mg/day |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT | The American Journal of Medicine | Randomized double-blind study, 90 AS patients over 26 weeks: flurbiprofen 200mg/day as effective as phenylbutazone 300mg/day |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Cohort | The American Journal of Medicine | Pooled safety data from 9 Phase III trials, 1,677 patients (AS, OA, RA): no clinically significant liver/kidney signal for flurbiprofen |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Pharmacological review: flurbiprofen 150-300mg/day comparable to aspirin/indomethacin in rheumatic diseases including AS, with fewer side effects than aspirin |

## Taiwan Market Information

Flurbiprofen is currently **not marketed in Taiwan** — 0 registered licenses are on file, so no product/dosage-form registration details are available.

## Safety Considerations

- **Drug Interactions**: DDI query returned 352 total interactions. Notable categories among the reviewed subset include: increased GI bleeding/ulcer risk when combined with corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone) or other NSAIDs/salicylates (Acetylsalicylic acid); potential altered glycemic control with sulfonylureas (Glimepiride, Chlorpropamide) and Metformin; and interactions with GI-active agents (Mesalazine, Balsalazide, H2-antagonists Famotidine/Cimetidine).
- Structured labeled warnings and contraindications are not yet available in this evidence pack (data gap DG001, Blocking severity) — please refer to the official package insert once obtained.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Eight-plus randomized controlled trials from 1974–1986 consistently demonstrate flurbiprofen's efficacy in ankylosing spondylitis, comparable to indomethacin, phenylbutazone, and naproxen — the drug class (NSAID) is already a validated first-line treatment for this disease, so the mechanistic and clinical rationale is strong (L1). However, the drug is not currently marketed in Taiwan and formal safety labeling data is missing, so the safety review cannot be finalized yet.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official TFDA/manufacturer package insert for warnings and contraindications
- Resolve DG002: confirm formal DrugBank MOA record
- Evaluate whether 1970s-80s trial data needs updating against current standard-of-care comparators (e.g., COX-2 selective NSAIDs, biologics) for a modern evidence assessment
- Assess feasibility/rationale for Taiwan market entry given current "not marketed" (0 licenses) status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

