---
layout: default
title: Valdecoxib
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 2
---

# Valdecoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Valdecoxib: From Arthritis Pain Relief to Osteoarthritis Susceptibility

## One-Sentence Summary

Valdecoxib (Bextra®) is a selective COX-2 inhibitor approved in the early 2000s for osteoarthritis, rheumatoid arthritis, and primary dysmenorrhea, but voluntarily withdrawn from global markets in 2005 due to cardiovascular and severe skin reaction safety concerns.
The TxGNN model predicts it may be effective for **Osteoarthritis Susceptibility** (score 99.45%), with **0 clinical trials** and **0 publications** directly supporting this specific predicted indication — placing it at model-prediction-only evidence level.
A closely related rank-2 prediction, **Rheumatoid Arthritis**, carries substantially stronger support with **1 clinical trial** and **20 publications**; however, the pre-existing withdrawal history means safety must be addressed before any repurposing pathway can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory data (drug withdrawn globally in 2005; historically approved for osteoarthritis, rheumatoid arthritis, and dysmenorrhea) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only — 0 clinical trials, 0 publications for this specific indication) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured data fields. Based on information consistently described across the retrieved literature, Valdecoxib is a highly selective inhibitor of cyclooxygenase-2 (COX-2) — the inducible enzyme responsible for prostaglandin synthesis at sites of inflammation, injury, and pain. By selectively blocking COX-2 without suppressing COX-1, it reduces prostaglandin-mediated joint inflammation and pain sensitization while sparing the gastroprotective prostaglandins that COX-1 maintains.

Osteoarthritis susceptibility is mechanistically linked to chronic, low-grade inflammatory activity in synovial joints, where COX-2-derived prostaglandins drive cartilage degradation and pain chronification. The pharmacological rationale for a COX-2 inhibitor in this setting is well-established — Valdecoxib was in fact originally approved for osteoarthritis management. The TxGNN prediction is therefore a biologically coherent re-identification of its known therapeutic target. The "susceptibility" framing may reflect the model identifying an early-intervention or disease-modification opportunity in at-risk populations, which is mechanistically plausible given that COX-2 activity has been implicated in early cartilage loss.

It is critical to note that Valdecoxib's 2005 market withdrawal was driven not by lack of efficacy but by confirmed post-marketing safety signals: increased cardiovascular thrombotic event risk (myocardial infarction, stroke) and rare but life-threatening skin reactions (Stevens-Johnson syndrome / toxic epidermal necrolysis). Any repurposing pathway must directly address these liabilities before clinical re-evaluation can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis susceptibility.

> **Supporting context (Rank-2 prediction — Rheumatoid Arthritis):** One completed Phase 4 trial (NCT00650455) evaluated Valdecoxib in rheumatoid arthritis; see table below for reference.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00650455](https://clinicaltrials.gov/study/NCT00650455) | Phase 4 | Completed | 489 | Multicenter RCT comparing Valdecoxib 10 mg QD vs. Naproxen 500 mg BID vs. placebo in severe RA; evaluated efficacy, safety, and tolerability |

---

## Literature Evidence

Currently no related literature available specifically queried for osteoarthritis susceptibility.

> **Supporting context (Rank-2 prediction — Rheumatoid Arthritis):** 20 publications were retrieved; the 10 most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15363872](https://pubmed.ncbi.nlm.nih.gov/15363872/) | 2004 | Systematic Review / Meta-analysis | *Pain* | Meta-analysis of RCTs: Valdecoxib 10–20 mg was significantly more effective than placebo and comparable to NSAIDs in OA and RA, with better upper GI tolerability |
| [18405470](https://pubmed.ncbi.nlm.nih.gov/18405470/) | 2008 | Systematic Review / HTA | *Health Technology Assessment* | Comprehensive systematic review and economic evaluation of COX-2 selective NSAIDs (including valdecoxib) for OA and RA; assessed clinical effectiveness and cost-effectiveness |
| [15740543](https://pubmed.ncbi.nlm.nih.gov/15740543/) | 2005 | Meta-analysis | *Alimentary Pharmacology & Therapeutics* | Meta-analysis comparing upper GI tolerability of valdecoxib vs. nonselective NSAIDs in OA/RA patients; valdecoxib showed significantly lower abdominal pain, dyspepsia, and nausea |
| [17692722](https://pubmed.ncbi.nlm.nih.gov/17692722/) | 2007 | RCT | *Clinical Therapeutics* | 12-week multicenter double-blind RCT in severe RA: valdecoxib significantly improved signs and symptoms vs. placebo; safety profile compared with naproxen |
| [12209034](https://pubmed.ncbi.nlm.nih.gov/12209034/) | 2002 | RCT | *Rheumatology (Oxford)* | Randomized controlled trial in RA patients: valdecoxib was significantly more effective than placebo and non-inferior to naproxen in symptom reduction |
| [16678642](https://pubmed.ncbi.nlm.nih.gov/16678642/) | 2006 | RCT | *Clinical Therapeutics* | Dose-comparison RCT (10, 20, 40 mg QD) vs. naproxen 500 mg BID vs. placebo in RA; all valdecoxib doses demonstrated significant efficacy improvement |
| [15266215](https://pubmed.ncbi.nlm.nih.gov/15266215/) | 2004 | Pooled Analysis | *American Journal of Therapeutics* | Cardiovascular thrombotic event data pooled from ~8,000 OA/RA patients; quantified the cardiovascular risk that ultimately led to market withdrawal |
| [15161329](https://pubmed.ncbi.nlm.nih.gov/15161329/) | 2004 | Review | *Drugs* | Comprehensive clinical review covering OA, RA, dysmenorrhea, and acute pain; summarizes efficacy as dose-dependent up to 40 mg/day |
| [23517091](https://pubmed.ncbi.nlm.nih.gov/23517091/) | 2013 | Review | *Expert Opinion on Pharmacotherapy* | Historical analysis of valdecoxib's regulatory trajectory: effective for rheumatological disease, withdrawn due to GI and cardiovascular risk profile |
| [40311381](https://pubmed.ncbi.nlm.nih.gov/40311381/) | 2025 | Original Research | *Archives of Medical Research* | Recent study showing valdecoxib ameliorates apoptosis and ferroptosis in tenocytes via SIRT6/NRF2-mediated suppression of oxidative stress — suggests novel cytoprotective mechanisms beyond classical COX-2 inhibition |

---

## India Market Information

No authorized products found. Valdecoxib currently holds **0 registrations** and is classified as **not marketed** in India.

---

## Safety Considerations

**Drug Interactions (222 total interactions identified; representative sample below):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Acetylsalicylic acid | Moderate | Combination increases GI toxicity; may blunt antiplatelet effect of aspirin |
| Hydrocortisone / Dexamethasone / Betamethasone / Triamcinolone / Budesonide | Moderate | NSAID + corticosteroid combinations significantly increase GI bleeding and ulceration risk |
| Metformin / Glimepiride / Chlorpropamide | Moderate | NSAIDs may impair renal clearance and potentiate hypoglycaemic effects |
| Clarithromycin | Moderate | CYP3A4 inhibition can raise valdecoxib plasma concentrations |
| Cimetidine | Moderate | Inhibits hepatic metabolism; potential for elevated drug exposure |
| Vancomycin | Moderate | Combined nephrotoxicity risk; renal monitoring warranted |
| Mesalazine / Balsalazide | Moderate | Additive GI mucosal injury risk |
| Metronidazole | Moderate | Interaction mechanism requires clinical monitoring |
| Omeprazole | Minor | May alter absorption or metabolic profile |

> **Critical Historical Safety Context:** Valdecoxib was voluntarily withdrawn worldwide in April 2005 following post-marketing evidence of (1) increased cardiovascular thrombotic events (MI, stroke) compared to placebo, particularly in post-CABG surgical patients, and (2) disproportionate reports of Stevens-Johnson syndrome and toxic epidermal necrolysis. These represent confirmed, mechanism-linked safety signals — not theoretical risks — and constitute the primary barrier to any repurposing effort.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Valdecoxib's withdrawal from global markets due to confirmed cardiovascular thrombotic risk and life-threatening cutaneous reactions represents a blocking safety liability that cannot be bypassed without a formal risk reassessment and risk-mitigation strategy; additionally, the rank-1 predicted indication (osteoarthritis susceptibility) has zero supporting clinical or literature evidence, placing confidence solely in the TxGNN model prediction at this stage.

**To proceed, the following is needed:**

- **Safety re-evaluation**: Obtain and review original FDA/EMA withdrawal documentation to precisely characterize the at-risk populations and dose/duration thresholds associated with cardiovascular and skin toxicity
- **Risk stratification strategy**: Define a patient subgroup (e.g., low baseline cardiovascular risk, short-term use) where the benefit-risk balance may be acceptable for osteoarthritis susceptibility
- **MOA characterization**: Retrieve full mechanism of action data from DrugBank API (DG002 remediation); the recent 2025 finding on SIRT6/NRF2-mediated cytoprotection in tenocytes warrants further investigation
- **Evidence gap for specific indication**: Commission a targeted literature search specifically for "valdecoxib AND osteoarthritis susceptibility / early osteoarthritis / OA prevention" to determine if L5 is truly the ceiling
- **India regulatory feasibility assessment**: Clarify whether a drug withdrawn from major markets (US, EU) can be re-submitted under a new indication in India, and what the regulatory pathway would require
- **Package insert recovery**: Retrieve pre-withdrawal prescribing information (PDF parsing from archived TFDA/FDA sources) to populate formal contraindications and black-box warnings (DG001 remediation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

