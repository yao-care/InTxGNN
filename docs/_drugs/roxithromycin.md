---
layout: default
title: Roxithromycin
parent: 僅模型預測 (L5)
nav_order: 750
evidence_level: L5
indication_count: 10
---

# Roxithromycin
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

# Roxithromycin: From Respiratory/Soft Tissue Infections to Leprosy

## One-Sentence Summary

> Roxithromycin is a macrolide antibiotic internationally used for respiratory tract, urinary tract, and soft tissue infections (not currently marketed in Taiwan/India).
> The TxGNN model predicts it may be effective for **Leprosy**,
> with **0 clinical trials** and **5 publications** — all preclinical/in vitro and animal studies — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local licensing data; internationally reported use is respiratory tract, urinary tract, and soft tissue infections |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (drug is not marketed locally, and DrugBank MOA lookup remains an open data gap). Based on known pharmacology, roxithromycin is a macrolide antibiotic — the same class as erythromycin and clarithromycin — with established activity against Gram-positive bacteria and some Gram-negative organisms such as *Legionella pneumophila*. Its efficacy in respiratory, urinary, and soft-tissue infections is well documented internationally.

Mechanistically, several macrolides (clarithromycin, roxithromycin, minocycline) have demonstrated anti-inflammatory and immunomodulatory activity in addition to direct antimycobacterial effects against *Mycobacterium leprae*. In vitro and mouse-footpad studies from the late 1980s and early 1990s showed that roxithromycin suppresses *M. leprae* growth and is bactericidal in animal models, providing biological plausibility for the TxGNN prediction. However, in head-to-head comparisons, clarithromycin — not roxithromycin — was found to be the more potent and clinically adopted macrolide for leprosy, and roxithromycin achieves lower drug levels at the infection site. No human clinical trial has evaluated roxithromycin specifically for leprosy treatment, so the current evidence base remains preclinical/mechanistic rather than clinical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Review | American Journal of Clinical Dermatology | General review of macrolide use in skin infections; notes macrolides inhibit bacterial protein synthesis via 23S ribosomal binding |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Review/Clinical commentary | Japanese Journal of Leprosy | Roxithromycin and clarithromycin show anti-inflammatory/immunomodulatory activity relevant to control of leprous peripheral neuropathy, alongside direct anti-*M. leprae* activity |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | In vitro/Animal | Antimicrobial Agents and Chemotherapy | Newer macrolides, including roxithromycin, assessed for in vitro/in vivo activity against *M. leprae*, building on erythromycin's known efficacy |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | In vitro (macrophage) | Antimicrobial Agents and Chemotherapy | Screening of >25 antimicrobials, including roxithromycin, using a macrophage-based phenolic glycolipid assay to evaluate antileprosy potential |
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | Animal (mouse model) | Antimicrobial Agents and Chemotherapy | Roxithromycin and clarithromycin were consistently active and bactericidal against *M. leprae* in mouse footpad infection; clarithromycin was superior, likely due to higher infection-site drug levels |

---

## Safety Considerations

- **Drug Interactions**: Pharmacology data indicate roxithromycin binds the motilin receptor (MLNR), a mechanism shared by macrolides that is associated with prokinetic gastrointestinal effects (e.g., nausea, GI motility stimulation). This is a pharmacological target interaction rather than a conventional drug-drug interaction, and no interaction severity level is documented.

Detailed TFDA-equivalent warnings and contraindications are not yet available (blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for the leprosy indication rests entirely on preclinical in vitro and mouse-model studies from the late 1980s–1990s plus narrative reviews (Evidence Level L4); no clinical trials exist, and a critical safety data gap (missing label warnings/contraindications) currently blocks entry into formal safety evaluation.

**To proceed, the following is needed:**
- Official product label / warnings & contraindications data (currently a Blocking data gap)
- Confirmed mechanism of action and original indication data from DrugBank
- Verification of India/Taiwan market and registration status
- Human pharmacokinetic and safety data specific to leprosy treatment populations
- Comparative efficacy data versus clarithromycin, the macrolide with stronger antileprosy evidence, to justify further investment in roxithromycin specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

