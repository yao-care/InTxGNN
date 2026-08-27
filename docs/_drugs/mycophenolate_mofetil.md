---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Organ Transplant Rejection to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF) is a selective immunosuppressant used internationally for prevention of acute rejection in solid organ transplantation, though it currently holds no market authorization in India.
The TxGNN model predicts it may be effective for **HIV infectious disease**,
with **10 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prophylaxis (not registered in India; based on international use) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mycophenolate mofetil (MMF) is a prodrug hydrolyzed in vivo to mycophenolic acid (MPA), a potent and selective inhibitor of inosine monophosphate dehydrogenase (IMPDH). By blocking IMPDH, MMF depletes the intracellular deoxyguanosine triphosphate (dGTP) nucleotide pool preferentially in lymphocytes. Because HIV reverse transcriptase depends on dGTP to synthesize viral DNA, this depletion directly impairs viral replication — and has been shown in clinical studies to synergize with nucleoside analog antiretrovirals (NRTIs) such as abacavir and didanosine. Simultaneously, MMF reduces the proliferation of activated CD4⁺ T cells, which are the primary host cells permissive to HIV replication, thereby restricting the available viral reservoir.

HIV chronic infection is characterized by persistent immune hyperactivation, which paradoxically accelerates CD4⁺ T-cell depletion and disease progression. MMF's ability to dampen this hyperactivation — independent of its direct antiviral effect — represents a second mechanistic rationale. Early clinical studies, including a Phase 4 study (MAN2) in ART-naïve patients and several Phase 2 trials in treatment-experienced patients, found that MMF was generally tolerable in HIV-infected individuals and modestly reduced viral markers when used alongside specific NRTIs.

However, a fundamental tension limits this repurposing opportunity: MMF is an immunosuppressant, and using it in a population already immunocompromised by HIV raises serious safety concerns. Adding further immunosuppression could increase the risk of opportunistic infections and impair HIV-specific immune surveillance. No clinical consensus on a minimum safe CD4⁺ threshold for MMF use in HIV has been established. Until this safety paradox is resolved with adequately powered trials, the mechanistic rationale — though compelling — cannot justify routine clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Multicenter prospective trial of renal transplantation in HIV-1 infected patients on Raltegravir-based ART; evaluated acute graft rejection at 6 months and immunological outcomes |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 Study: randomized MMF vs. no treatment in ART-naïve HIV-1 patients; assessed whether MMF reduces chronic immune hyperactivation and CD4⁺ T-cell decline |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Randomized double-blind placebo-controlled study of DAPD vs. DAPD+MMF in treatment-experienced HIV patients; explored synergistic antiretroviral activity via dGTP depletion |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | Sub-study of MAN2: assessed effect of MMF on cardiovascular and metabolic surrogate markers in HIV-1 infected patients not receiving ART |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT to induce mixed hematopoietic chimerism in HIV-positive patients using non-myeloablative conditioning; MMF used as post-transplant immunosuppression |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Safety and efficacy of renal transplantation in HIV-infected patients with end-stage renal disease; confirmed MMF tolerability within the HIV immunosuppressive context |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Planned study of MMF safety, tolerability, and antiretroviral activity as adjunct to abacavir in heavily treatment-experienced patients; withdrawn prior to enrollment — no data generated |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Clinical Trial | J Acquir Immune Defic Syndr | MMF added to abacavir-based ART depleted intracellular dGTP and reduced plasma HIV-1 RNA in 5 patients with multidrug-resistant HIV; proof-of-concept for IMPDH inhibition as adjunctive strategy |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Clinical Trial | J Acquir Immune Defic Syndr | Randomized pilot (n=17) of MMF during HAART interruption in chronic HIV-1 patients; assessed viral load rebound kinetics and lymphatic tissue reservoir changes |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD Study | Clin Pharmacokinet | Low-dose MMF PK/PD profile in HIV patients on abacavir+efavirenz+nelfinavir; recommended therapeutic drug monitoring given pharmacokinetic interactions |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK/PD Study | Clin Pharmacokinet | MMF's effects on intracellular dCTP/dGTP pools and lamivudine triphosphate concentrations; demonstrated mechanistic rationale for NRTI synergy |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Clinical Study | AIDS Res Hum Retroviruses | MMF+HAART in treatment-naïve acute and chronic HIV-1 patients showed no detrimental immunological effects; longitudinal T-cell proliferation analysis |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Comprehensive mechanistic review of immunosuppressive drugs in HIV; details how IMPDH inhibition addresses chronic immune hyperactivation as a disease driver |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot Study | J Acquir Immune Defic Syndr | Open-label pilot (n=7) of MMF+ABC+ddI+APV±EFV in patients with AIDS and ≥8 failed ART regimens; well-tolerated but no sustained viral load decline |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical Study | AIDS | DAPD (amdoxovir) with or without MMF in drug-resistant HIV after extensive ART; evaluated safety and antiretroviral activity in treatment-experienced patients |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Experimental | J Clin Invest | Antiproliferative drugs selectively target HIV-infected CD4⁺ T-cell clones; provides contemporary mechanistic support for MMF's role in reducing the clonally expanded HIV reservoir |
| [39515757](https://pubmed.ncbi.nlm.nih.gov/39515757/) | 2025 | Cohort Study | Am J Transplant | Long-term kidney transplant outcomes in HIV recipients on tacrolimus/MMF; compared r-ATG vs. IL-2 receptor antagonist induction — real-world safety data for MMF in HIV patients |

---

## India Market Information

Mycophenolate mofetil currently has **no authorized products registered in India** (0 licenses, market status: not marketed). No approved indication text is available from CDSCO records.

---

## Safety Considerations

**Drug Interactions** (92 total interactions identified; key interactions listed below):

| Severity | Interacting Drug(s) | Clinical Relevance |
|----------|--------------------|--------------------|
| **Major** | Activated charcoal | Dramatically reduces MMF absorption; avoid concurrent use |
| **Moderate** | Proton pump inhibitors (Omeprazole, Esomeprazole, Rabeprazole, Lansoprazole, Dexlansoprazole) | Reduce MPA systemic exposure; monitor drug levels and immunosuppressive efficacy |
| **Moderate** | Antibiotics (Amoxicillin, Doxycycline, Tetracycline, Clarithromycin, Minocycline, Vancomycin, Kanamycin, Paromomycin) | Disruption of gut flora may impair enterohepatic recirculation of MPA, potentially reducing MMF efficacy — particularly relevant given frequent antibiotic use in HIV patients |
| **Moderate** | Antacids (Aluminum hydroxide, Calcium carbonate, Magnesium oxide) | Chelation reduces MMF absorption; separate administration by at least 2 hours |
| **Minor** | Zinc sulfate, Zinc acetate, Iron | Minor reduction in MMF absorption |

Please refer to the package insert for complete warnings and contraindications, as key warnings and contraindication data are not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although MMF's IMPDH inhibition mechanism provides a plausible and experimentally supported rationale for use in HIV, the fundamental safety paradox — deploying an immunosuppressant in an already immunocompromised population — combined with consistently small trial sizes (n=5 to 90), absence of a Phase 3 superiority trial specifically for HIV treatment, and zero India regulatory footprint, makes advancing this candidate premature without further targeted evidence generation.

**To proceed, the following is needed:**
- Retrieve complete MOA and pharmacology data from DrugBank (DB00688) to fill the current data gap and support mechanistic analysis
- Obtain full prescribing information (package insert) from an international regulatory source (FDA/EMA) to document warnings, contraindications, and pregnancy/infection risk categories
- Define a minimum safe CD4⁺ T-cell threshold below which MMF use in HIV is contraindicated — this is the central unresolved safety question
- Commission or identify a well-powered prospective RCT with pre-specified primary endpoints (e.g., viral reservoir size, ART-free viral suppression duration) in a defined HIV subpopulation (e.g., multidrug-resistant HIV, HIV with autoimmune complications, HIV transplant recipients)
- Conduct a drug-drug interaction review specifically for MMF combined with current first-line ART regimens (INSTI-based regimens), given that 92 DDIs are already documented and antibiotic co-administration is common in HIV patients
- Evaluate regulatory pathway feasibility in India through CDSCO for a potential orphan or investigational new drug application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

