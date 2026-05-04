---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) used as a cornerstone component of combination antiretroviral therapy (cART) for HIV-1 infection in humans, included in widely-used formulations such as Truvada and Descovy.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection in cats)**, with **4 clinical trials** (indirect, all in human HIV-1) and **1 direct experimental publication** in FIV-infected cats currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (human; inferred from clinical trial context — no India market approval on record) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Emtricitabine (FTC) is a fluorinated cytidine analogue. After intracellular phosphorylation to its active triphosphate form (FTC-TP), it competes with natural deoxycytidine triphosphate for incorporation into the nascent viral DNA strand, acting as an obligate chain terminator of reverse transcriptase (RT) — thereby blocking viral RNA-to-DNA conversion. This mechanism is definitively established for HIV-1 in humans.

Feline Immunodeficiency Virus (FIV) belongs to the *Lentivirus* genus, the same viral family as HIV-1 and HIV-2. FIV and HIV-1 share structural homology in their reverse transcriptase enzymes, which is the mechanistic basis for this repurposing prediction. Importantly, a 2023 experimental study (PMID 37112803) directly tested a cART regimen including Emtricitabine (40 mg/kg) alongside Dolutegravir and Tenofovir in FIV-infected domestic cats, providing the first in-species pharmacokinetic and immunophenotypic data. Additionally, the M184V resistance mutation — through which FTC resistance emerges in HIV — has been documented in SIV primate models treated with emtricitabine (PMID 12021341), demonstrating cross-lentiviral conservation of the drug-target interaction mechanism.

However, several critical unknowns limit immediate translation. Feline-specific pharmacokinetics (oral bioavailability, tissue distribution, hepatic metabolism) differ substantially from humans; cats are known to have limited glucuronidation capacity. The sequence divergence between FIV RT and HIV-1 RT may affect binding affinity and chain-termination efficiency. These gaps require dedicated feline pharmacology studies before any clinical recommendation can be made.

---

## Clinical Trial Evidence

> **Important context:** No registered clinical trials directly study Emtricitabine in feline AIDS. The four trials below evaluated Emtricitabine as a backbone component of human HIV-1 combination regimens. They are listed here as indirect mechanistic support, confirming the drug's antiviral activity and safety profile via its RT-inhibiting mechanism — the same mechanism proposed for FIV.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Non-inferiority of dolutegravir vs raltegravir, both combined with TDF/FTC or ABC/3TC, over 96 weeks in ART-naïve HIV-1 adults; establishes FTC-containing backbone efficacy at scale |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs Efavirenz/Emtricitabine/TDF (Atripla) over 96 weeks in ART-naïve HIV-1 adults; long-term safety and resistance data for FTC confirmed |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study for dolutegravir administered with TDF/FTC or ABC/3TC; provides safety and tolerability data for FTC as part of combination regimens |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs boosted darunavir + TDF/FTC in ART-naïve HIV-1 patients; comparative safety profile of FTC-containing dual-NRTI backbone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Experimental Animal Study (FIV cat model) | *Viruses* | cART (Dolutegravir 2.5 mg/kg + Tenofovir 20 mg/kg + **Emtricitabine 40 mg/kg**) administered to FIV-infected domestic cats; evaluated pharmacokinetics and immunophenotype — the only direct in-species study available for this indication |

---

## India Market Information

Emtricitabine currently has **no approved or registered products in India** as of the data cutoff (April 2026). No license records are available for review.

---

## Safety Considerations

**Drug Interactions** (20 interactions identified; source: DDInter):

| Severity | Interacting Drugs |
|----------|------------------|
| **Major** | Leflunomide, Teriflunomide |
| **Moderate** | Orlistat, Naltrexone, Cobicistat, Asparaginase *Escherichia coli*, Interferon beta-1a, Interferon beta-1b, Brentuximab vedotin, Cabozantinib, Cladribine, Clofarabine, Epirubicin, Idelalisib, Methotrexate, Pegaspargase, Peginterferon beta-1a, Tioguanine, Trabectedin |
| **Minor** | Eribulin |

For key warnings and contraindications, please refer to the full package insert, as this information was not captured in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Emtricitabine in feline acquired immunodeficiency syndrome remains at **L4** (a single experimental cat study published in 2023), with no dedicated clinical trials and no regulatory precedent in veterinary medicine for this species-indication pair. While the mechanistic case is scientifically coherent — FIV shares lentiviral RT homology with HIV — species-specific pharmacology has not been adequately characterized to support advancement.

> **Note on secondary predictions:** The second-ranked TxGNN prediction — **Simian Immunodeficiency Virus (SIV) infection** (score 99.92%, **L3** evidence, recommendation: *Proceed with Guardrails*) — carries a meaningfully stronger evidence base, with 20 macaque studies (SHIV/SIV challenge models) demonstrating Emtricitabine's efficacy in pre-exposure prophylaxis and treatment. If the research goal is lentiviral disease modeling or primate translational research, SIV infection represents a more immediately actionable avenue.

**To proceed with feline AIDS indication, the following is needed:**

- **Species-specific PK/PD study** in cats: oral bioavailability, plasma half-life, renal and hepatic clearance, target tissue (lymphoid) penetration
- **In vitro FIV RT inhibition assay** with FTC-TP to confirm susceptibility and determine IC₅₀ vs HIV-1 RT
- **FIV challenge model study** with defined virological endpoints (plasma viral load, CD4⁺ T-cell counts, clinical scoring)
- **Feline safety and tolerability study** including renal, hepatic, and haematological monitoring (cats are at particular risk with certain NRTIs)
- **Full mechanism of action documentation** via DrugBank API or package insert review
- **Regulatory pathway scoping** for veterinary drug approval in India (CDSCO veterinary division) or international reference (e.g., EMA veterinary procedures)

---

*This report is for research reference only and does not constitute medical or veterinary advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

