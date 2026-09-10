---
layout: default
title: Saquinavir
parent: 僅模型預測 (L5)
nav_order: 757
evidence_level: L5
indication_count: 6
---

# Saquinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Saquinavir: From HIV Protease Inhibition to AIDS-Related Complex (Extended Indication)

## One-Sentence Summary

> Saquinavir is an HIV-1 protease inhibitor already used to treat HIV infection.
> TxGNN's raw output ranks several very high-scoring but biologically implausible diseases at the top (e.g., feline AIDS, a rare pediatric neurodevelopmental disorder) — these are flagged as knowledge-graph artifacts.
> After screening, the only credible, actionable signal is extended use in **AIDS-Related Complex** (advanced/late-stage HIV disease), supported by **9 clinical trials (including two completed Phase 3 RCTs)** and mechanistic continuity with Saquinavir's established mode of action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (known drug class; not confirmed in India regulatory filings — see Data Gaps) |
| Predicted New Indication | AIDS-Related Complex |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently not available (Data Gap DG002). Based on known pharmacology, Saquinavir is a peptidomimetic HIV-1 **protease inhibitor**: it blocks cleavage of the Gag-Pol polyprotein, preventing maturation of infectious viral particles. This is Saquinavir's core, already-approved mechanism for HIV/AIDS treatment.

"AIDS-Related Complex" and "congenital HIV infection" are not truly novel diseases relative to Saquinavir's original indication — they represent **advanced-stage and special-population extensions of the same underlying HIV infection** the drug was designed to treat. The clinical trial record (Phase 1 dose-escalation through Phase 3 combination-therapy trials with AZT, ddC, and other protease inhibitors) directly supports use across this disease spectrum, including a dedicated pediatric/infant PK-safety study (NCT00623597) and a cohort study of ritonavir-boosted use in HIV-infected pregnant women (PMID 22938775), which is directly relevant to the congenital/perinatal-transmission indication.

In short, this is less a "repurposing hypothesis" and more a **confirmation that Saquinavir's established mechanism generalizes across HIV disease stages and populations** — which is why the internal evidence-scoring pipeline classifies it as L1/S3 (Proceed with Guardrails) rather than a speculative new use.

---

## TxGNN Predictions Screened Out (Not Recommended)

Four of the six raw TxGNN outputs scored equal or higher than the AIDS-Related Complex signal but were excluded as low-quality/spurious:

| Rank | Disease | Score | Evidence | Why Excluded |
|------|---------|-------|----------|---------------|
| 1 | Feline acquired immunodeficiency syndrome | 99.97% | None | Veterinary disease; FIV protease diverges substantially from HIV-1; likely embedding-space false positive from "retrovirus/protease inhibitor" proximity |
| 2 | Simian immunodeficiency virus infection | 99.97% | 4 in-vitro/animal studies | Real cross-reactivity exists, but SIV infection is an animal model, not a human disease — supports HIV mechanism, not an independent indication |
| 3 | Rare neurodevelopmental disorder (ataxic gait, absent speech) | 99.97% | None | No biological link to protease inhibition; zero trials/literature; likely knowledge-graph noise |
| 4 | Obsolete familial combined hyperlipidemia | 99.59% | None | Disease term is deprecated ontology; dyslipidemia is a known **adverse effect** of HIV protease inhibitors, not a treatment target — likely a reversed-causality artifact |

Rank 5 (AIDS-Related Complex) and Rank 6 (Congenital HIV) are the only signals with L1/S3 evidence grading and are the focus of this report.

---

## Clinical Trial Evidence

*(AIDS-Related Complex — Rank 5)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002333](https://clinicaltrials.gov/study/NCT00002333) | Phase 2 | Completed | 900 | Saquinavir vs. ddC vs. combination in advanced HIV (CD4 50–300) patients unable to take AZT |
| [NCT00002334](https://clinicaltrials.gov/study/NCT00002334) | Phase 3 | Completed | 3000 | Large parallel-group trial: AZT alone vs. AZT+ddC vs. AZT+Saquinavir vs. triple combination in early-stage HIV |
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Atazanavir+ritonavir/Saquinavir vs. lopinavir/ritonavir, both with tenofovir, in treatment-experienced HIV patients |
| [NCT00002347](https://clinicaltrials.gov/study/NCT00002347) | Phase 2 | Completed | 225 | Multidrug master protocol: AZT/ddC ± nevirapine or Saquinavir |
| [NCT00002162](https://clinicaltrials.gov/study/NCT00002162) | Phase 2 | Completed | 140 | Comparison of two Saquinavir formulations combined with nucleoside antiretrovirals |
| [NCT00000848](https://clinicaltrials.gov/study/NCT00000848) | Phase 2 | Completed | 144 | Switching hard-capsule to soft-gel Saquinavir vs. switching to indinavir after 1 year of use |
| [NCT00001040](https://clinicaltrials.gov/study/NCT00001040) | Phase 2 | Completed | 300 | Saquinavir+AZT vs. AZT+ddC vs. triple combination |
| [NCT00002111](https://clinicaltrials.gov/study/NCT00002111) | Phase 1 | Completed | 32 | Dose-escalation study of oral saquinavir mesylate — toxicity, antiviral activity, PK |

---

## Literature Evidence

*(AIDS-Related Complex — Rank 5)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32694416](https://pubmed.ncbi.nlm.nih.gov/32694416/) | 2020 | PK study | AIDS (London) | CNS antiretroviral penetration data relevant to HIV-related brain disease management |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | GI adverse events in HIV patients on antiretroviral treatment |
| [18256206](https://pubmed.ncbi.nlm.nih.gov/18256206/) | 2008 | Mechanistic/PK | Drug Metab Dispos | P-gp, MRP2 and CYP3A roles in saquinavir oral absorption (rat model) |
| [26944096](https://pubmed.ncbi.nlm.nih.gov/26944096/) | 2016 | Review | Adv Drug Deliv Rev | Nanotechnology approaches for CNS HIV reservoir management |
| [11363313](https://pubmed.ncbi.nlm.nih.gov/11363313/) | 1996 | Conference report | BETA | Conference summary, Retroviruses and Opportunistic Infections |
| [11362550](https://pubmed.ncbi.nlm.nih.gov/11362550/) | 1995 | Interview/Commentary | BETA | Pain management in AIDS |
| [15925431](https://pubmed.ncbi.nlm.nih.gov/15925431/) | 2005 | Case report | Rev Med Interne | Portal vein thrombosis in 4 HIV-infected patients |

---

## India Market Information

Saquinavir is **not currently registered or marketed in India** (0 authorizations on file). No license records are available to summarize.

---

## Safety Considerations

**Drug Interactions**: 313 documented interactions on file. The most significant flagged interactions include:

| Interacting Drug | Severity |
|---|---|
| Clarithromycin | Major |
| Budesonide (systemic) | Major |
| Triamcinolone | Major |
| Omeprazole, Rabeprazole, Famotidine | Moderate |
| Dexamethasone, Betamethasone, Hydrocortisone | Moderate |
| Metformin, Alogliptin, Canagliflozin, Chlorpropamide, Albiglutide | Moderate |

Given Saquinavir's CYP3A-dependent metabolism, interactions with corticosteroids and CYP3A inhibitors/inducers (e.g., clarithromycin) warrant particular attention.

No further warnings or contraindications are available at this time — please refer to the package insert once available (see Data Gap DG001, below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The AIDS-Related Complex / congenital HIV signal is backed by L1-grade evidence (multiple completed Phase 3 RCTs) and is mechanistically continuous with Saquinavir's already-established antiretroviral action — this is a low-risk, high-confidence extension rather than a novel repurposing bet. However, the drug is **not currently marketed in India**, and two blocking/high-severity data gaps remain.

**To proceed, the following is needed:**
- **TFDA/India label warnings and contraindications** (currently missing — flagged as a Blocking gap for safety review, DG001)
- **Confirmed mechanism of action from DrugBank API** (currently missing, DG002)
- Regulatory pathway assessment for India market entry (currently zero registrations)
- Pediatric/perinatal dosing and teratogenicity data review before pursuing the congenital-HIV population specifically
- Formal exclusion documentation for the four screened-out TxGNN signals (feline AIDS, SIV, rare neurodevelopmental disorder, hyperlipidemia) to prevent recurring false-positive triage effort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

