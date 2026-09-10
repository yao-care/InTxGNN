---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Rifabutin
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

# Rifabutin: From Antimycobacterial Therapy to HIV Infectious Disease

## One-Sentence Summary

> Rifabutin is a rifamycin-class antibiotic used to prevent and treat *Mycobacterium avium* complex (MAC) infection and tuberculosis, most often in HIV-infected patients.
> The TxGNN model predicts it may be effective for **HIV infectious disease**,
> with **38 clinical trials** and **20+ publications** currently supporting this direction — though the evidence base largely reflects rifabutin's *established* role in managing HIV-associated opportunistic infections rather than a genuinely novel antiviral mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antimycobacterial therapy (MAC prophylaxis/treatment, tuberculosis co-treatment) in HIV-infected patients — inferred from clinical trial/literature evidence; not a registered India indication (see Market Status below) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism of action (MOA) data is not available in the regulatory record. Based on the clinical trial and literature evidence collected, Rifabutin is a semisynthetic rifamycin that inhibits bacterial (mycobacterial) RNA polymerase, giving it potent activity against *Mycobacterium avium* complex and *M. tuberculosis*. It has long been used as an alternative to rifampicin in HIV-infected patients specifically because it is a weaker CYP3A4 inducer, causing fewer interactions with antiretroviral therapy (ART).

Importantly, the evidence pack's own repurposing rationale flags a key caveat: **Rifabutin has no direct antiviral activity against HIV itself.** Its strong TxGNN association with "HIV infectious disease" reflects its position in the knowledge graph as a *standard-of-care adjunct* for HIV patients — treating/preventing the opportunistic infections (MAC bacteremia, TB co-infection) that define advanced HIV disease — rather than a newly discovered antiretroviral mechanism. The dense clinical trial and pharmacokinetic literature confirms this well-established adjunctive role, not a novel repurposing hypothesis.

Given this, the practical interpretation of this prediction is: rifabutin should be evaluated (and positioned) as a component of HIV/TB and HIV/MAC co-management regimens, with emphasis on drug-drug interaction management with ART, rather than as a candidate for a standalone "HIV" indication label.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Daily vs. intermittent azithromycin/rifabutin (alone and combined) for prevention of disseminated MAC in HIV-infected patients |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Open-label RCT of 4 regimens (clarithromycin + ethambutol + rifabutin or clofazimine) for disseminated MAC disease in AIDS patients |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1,100 | Clarithromycin vs. rifabutin vs. combination for prevention of MAC bacteremia in HIV patients with CD4 ≤100 |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | NA | Completed | 750 | Double-blind, placebo-controlled trial of rifabutin monotherapy to prevent MAC bacteremia and prolong survival in AIDS patients (CD4 ≤200) |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm trial: clarithromycin/ethambutol + rifabutin (450mg or 300mg) vs. placebo for MAC bacteremia treatment |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | NA | Completed | 200 | Double-blind RCT of rifabutin-containing regimen for MAC bacteremia in AIDS patients |
| [NCT01663168](https://clinicaltrials.gov/study/NCT01663168) | Phase 2 | Unknown | 140 | Toxicity/PK of rifabutin doses in HIV adults/adolescents on lopinavir/ritonavir second-line ART (EARNEST substudy) |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | PK of rifabutin combined with ART for TB/HIV co-treatment in Vietnam |
| [NCT01259219](https://clinicaltrials.gov/study/NCT01259219) | Phase 1 | Unknown | 40 | Dosing/safety/PK of rifabutin in young HIV-infected children on Kaletra-based ART after completing TB treatment |
| [NCT01894776](https://clinicaltrials.gov/study/NCT01894776) | Phase 1 | Completed | 15 | DDI study of rifabutin's effect on maraviroc pharmacokinetics in healthy volunteers |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Cochrane Review | Cochrane Database Syst Rev | Rifamycins (incl. rifabutin) vs. isoniazid for TB prevention in HIV-negative at-risk individuals |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Review | Clin Pharmacokinet | Clinical pharmacokinetics of rifabutin; established efficacy for MAC prophylaxis in low-CD4 HIV patients |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | Bidirectional relationship between TB and HIV; rifabutin's role in co-infection management |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | Management of active TB in the HIV era, incl. rifamycin-ART interaction challenges |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin PK and safety in TB/HIV-coinfected children on LPV/r-based second-line ART |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety/efficacy of rifabutin in HIV/TB-coinfected children on LPV/r-based ART |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | PK/Safety Study | J Antimicrob Chemother | PK and short-term safety of rifabutin + LPV/r in young HIV-infected children |
| [32979587](https://pubmed.ncbi.nlm.nih.gov/32979587/) | 2020 | Retrospective Observational | Int J Infect Dis | Tenofovir alafenamide + rifabutin co-administration does not compromise HIV-1 suppression |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | Population PK Pooled Analysis | J Antimicrob Chemother | Pooled DDI analysis for rifabutin dosing with HIV protease inhibitors |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK Model | Br J Clin Pharmacol | DDI model characterizing rifabutin-dolutegravir co-administration |

---

## India Market Information

Rifabutin currently has **no marketing authorization registered in India** (0 licenses on file; market status: Not Marketed). No product-level dosage form or approved indication text is available from local regulatory sources.

---

## Safety Considerations

**Drug Interactions**: A DDI query returned **163 total interactions**. Notable examples include:
- **Major**: Eliglustat
- **Moderate**: Doxycycline, Clarithromycin, Metronidazole, Aprepitant, corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone), vitamin D analogs (Cholecalciferol, Calcifediol, Calcitriol), oral hypoglycemics (Pioglitazone, Saxagliptin, Linagliptin, Chlorpropamide, Acetohexamide), Morphine, Picosulfuric acid
- **Minor**: Dolasetron

Given rifabutin's role as a moderate CYP3A4 inducer, interactions with ART (protease inhibitors, integrase inhibitors) and corticosteroids/hypoglycemics should be actively managed in any HIV co-treatment protocol. Package insert–level warnings and contraindications are not currently available in the evidence pack (data gap DG001) — please refer to the official product label once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (n=400–1,100) robustly support rifabutin's efficacy in preventing/treating MAC bacteremia in HIV-infected patients, and extensive PK/DDI literature supports its safe co-administration with modern ART. However, this predicted indication should be reframed as **adjunctive management of HIV-associated opportunistic infections**, not a direct antiretroviral indication — rifabutin has no intrinsic anti-HIV activity.

**To proceed, the following is needed:**
- TFDA/India-equivalent package insert warnings and contraindications (DG001, blocking)
- Structured mechanism of action documentation (DG002)
- Clarification of the intended indication label (OI prophylaxis/treatment in HIV patients vs. standalone "HIV infectious disease") before advancing past S3
- Confirmation of India registration pathway, given current "Not Marketed" status and zero existing licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

