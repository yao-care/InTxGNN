---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 739
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV/AIDS Treatment to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Ritonavir is a well-established HIV-1 protease inhibitor, originally used in antiretroviral combination therapy for HIV/AIDS.
> The TxGNN model's top prediction points to **Simian Immunodeficiency Virus (SIV) Infection** — a lentivirus that infects non-human primates, not humans.
> Supporting evidence consists solely of **12 preclinical/mechanistic publications** and **no clinical trials**, reflecting cross-reactivity of protease inhibitors across lentivirus species rather than a viable human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS (inferred from known mechanism as HIV-1 protease inhibitor; no formal Taiwan label text available — drug not marketed) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale confirms Ritonavir acts as an **HIV-1 protease inhibitor**. SIV and HIV both belong to the *Lentivirus* genus, and their viral proteases share substantial sequence homology, which explains why in vitro assays show cross-susceptibility of SIV to several HIV protease inhibitors, including Ritonavir (PMID 12709355, PMID 15040537).

However, this mechanistic overlap does not translate into a human clinical indication. SIV is a primate-specific pathogen and does not infect humans; the supporting literature consists entirely of animal-model and in vitro studies used to validate SIV/macaque systems as surrogate models for HIV/AIDS research — not evidence of therapeutic benefit in a human disease. In effect, this candidate reflects TxGNN's inability to distinguish "biologically related pathogen" from "clinically actionable human indication."

It is also worth noting that ranks #2 and #3 in this prediction set share similar issues: rank #2 ("feline acquired immunodeficiency syndrome") is a cat-specific viral disease with its single associated clinical trial appearing to be a mismatched HIV-in-humans study, and rank #3 (a rare neurodevelopmental disorder) has no mechanistic, trial, or literature support at all (L5, model score only). None of the three top-ranked candidates constitute a credible human repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro drug susceptibility | Antimicrob Agents Chemother | Ritonavir inhibited SIVmac239 with EC50 ~13 nM, comparable to its inhibition of HIV-1 (~25 nM), directly demonstrating cross-species protease inhibition. |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro drug susceptibility | Antivir Ther | Evaluated 16 approved anti-HIV-1 drugs (incl. Ritonavir) against HIV-2, SIV, and SHIV strains to inform treatment/post-exposure prophylaxis guidance. |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Macaque animal model | J Virol | Studied viral decay kinetics in SIV-infected macaques receiving quadruple antiretroviral therapy (mathematical modeling of lentivirus dynamics). |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Macaque/CNS animal model | mBio | Found lentiviral reservoirs persist in brain tissue despite effective ART, using SIV/macaque models to study HIV CNS persistence. |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro mechanism study | Antivir Chem Chemother | Characterized broad-spectrum antiviral activity of a fluoroquinolone derivative against HIV-1 (including Ritonavir-resistant strains), HIV-2, and SIV. |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Macaque animal model | PLoS One | Evaluated combination ART plus HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques as an HIV reservoir model. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | SHIV construct/animal model | Microbes Infect | Constructed a novel SHIV bearing HIV-1 protease for in vivo efficacy testing of protease inhibitors in rhesus macaques. |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Mechanism study (Vif/protease) | J Virol | Demonstrated viral protease-dependent processing of the HIV-1 Vif protein, relevant to protease inhibitor mechanism of action. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Macaque animal model | J Virol Methods | Assessed oral HAART (including Lopinavir/Ritonavir) impact on CD8 T-cell subsets in SHIV-infected macaques. |
| [11364629](https://pubmed.ncbi.nlm.nih.gov/11364629/) | 1997 | Commentary/mechanism hypothesis | J Int Assoc Physicians AIDS Care | Brief commentary on chemokine receptor-targeted antiviral strategies. |

---

## Taiwan Market Information

Ritonavir is currently **not marketed in Taiwan** — no active product licenses are on record (0 registrations).

---

## Safety Considerations

- **Drug Interactions**: Ritonavir has an extensive drug interaction profile, with **343 documented interactions** overall (primarily via strong CYP3A4 inhibition). Notable **Major-severity** interactions from the available data include:

| Interacting Drug | Level | Source |
|---|---|---|
| Loperamide | Major | ddinter |
| Triamcinolone | Major | ddinter |
| Budesonide | Major | ddinter |

Additional **Moderate-level** interactions are documented with corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Budesonide nasal), diabetes medications (Acarbose, Metformin, Alogliptin, Canagliflozin, Chlorpropamide, Albiglutide), and other agents (Bupropion, Aprepitant, Metronidazole, Clarithromycin, Alosetron, Lorcaserin).

Key warnings and contraindications could not be assessed — the official TFDA label/package insert has not yet been obtained (Blocking-severity data gap), so no formal warning or contraindication data is available at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, SIV infection, is a non-human primate disease with no human clinical relevance; all supporting evidence is preclinical (in vitro assays and macaque models), corresponding to Evidence Level L4 with no clinical trials. Combined with a Blocking-severity data gap on TFDA label safety information, this candidate cannot proceed past initial safety screening (S1). The next two ranked candidates (feline AIDS, a rare neurodevelopmental disorder) are similarly non-actionable due to species mismatch or absence of any supporting evidence (L5).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required before any S1 safety screening
- Confirmed mechanism-of-action record via DrugBank API
- Re-screening of the TxGNN candidate list for indications with plausible human clinical applicability (current top-3 ranked candidates are not suitable for advancement)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

