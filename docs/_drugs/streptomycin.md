---
layout: default
title: Streptomycin
parent: 僅模型預測 (L5)
nav_order: 785
evidence_level: L5
indication_count: 10
---

# Streptomycin
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

# Streptomycin: From Bacterial Infections to Conjunctivitis

## One-Sentence Summary

> Streptomycin is one of the earliest aminoglycoside antibacterials, historically used against bacterial infections such as tuberculosis and other susceptible organisms.
> The TxGNN model predicts it may be effective for **Conjunctivitis**,
> but this is currently supported by **0 clinical trials** and **20 publications**, most of which are historical case reports/cohort studies from the 1940s–1950s, with several entries only tangentially related (different drugs or unrelated organisms).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No India registration data available; historically used as a broad-spectrum antibacterial (e.g., tuberculosis, other bacterial infections) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Streptomycin is an aminoglycoside antibacterial that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit. It has no current marketed product or registration in India, and no original indication text could be extracted from regulatory records.

Mechanistically, this antibacterial action could plausibly extend to **bacterial conjunctivitis** and its more specific historical forms — tuberculous conjunctivitis, brucella-related keratoconjunctivitis, and trachoma (chlamydial). However, the disease label "conjunctivitis" as predicted by TxGNN is non-specific: the large majority of real-world conjunctivitis cases are viral or allergic in etiology, for which an antibacterial mechanism does not apply. The supporting literature reflects this ambiguity — several papers concern unrelated drugs (e.g., tobramycin) or unrelated species (dogs, cats), and the most directly relevant evidence (1947–1953 case series and prophylaxis cohorts) predates modern trial standards and modern topical antibiotic alternatives.

In short, the prediction is biologically plausible **only for the bacterial subtype of conjunctivitis**, and the current evidence base, while historically supportive, does not meet a modern evidentiary bar for repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13075256](https://pubmed.ncbi.nlm.nih.gov/13075256/) | 1953 | Cohort/Prophylaxis trial | Rev Int Trachome | Streptomycin eye instillations compared with chloramine for prevention/treatment of seasonal conjunctivitis in rural Morocco |
| [13075257](https://pubmed.ncbi.nlm.nih.gov/13075257/) | 1953 | Cohort/Prophylaxis trial | Rev Int Trachome | Streptomycin eye-wash vs. aureomycin salve for prevention of seasonal conjunctivitis in southern Morocco |
| [15442493](https://pubmed.ncbi.nlm.nih.gov/15442493/) | 1950 | Case report | La Semana Medica | Primary tuberculous conjunctivitis with fistulized adenopathies treated with systemic and local streptomycin |
| [18132879](https://pubmed.ncbi.nlm.nih.gov/18132879/) | 1949 | Case series | Am J Ophthalmol | Effectiveness of streptomycin in experimental conjunctivitis caused by *Hemophilus* sp. |
| [38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/) | 2024 | Case report | Am J Case Rep | Parinaud oculoglandular syndrome (conjunctivitis + lymphadenopathy) due to *Francisella tularensis* |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Observational/microbiology | J Ophthalmic Inflamm Infect | Bacteriologic survey of conjunctivitis pathogens and antibiotic susceptibility in Lagos, Nigeria |
| [5289718](https://pubmed.ncbi.nlm.nih.gov/5289718/) | 1971 | Laboratory study | J Hygiene | Susceptibility of trachoma (TRIC) agent to streptomycin and related antibiotics in culture |
| [6789462](https://pubmed.ncbi.nlm.nih.gov/6789462/) | 1981 | Case report | S Afr Med J | Brucella keratoconjunctivitis treated with systemic tetracycline/co-trimoxazole/streptomycin plus topical therapy |
| [38298538](https://pubmed.ncbi.nlm.nih.gov/38298538/) | 2023 | Review | Front Microbiol | Review of tularemia treatment, including its oculoglandular/conjunctival presentation |
| [3317953](https://pubmed.ncbi.nlm.nih.gov/3317953/) | 1987 | Review (different drug: tobramycin) | Surv Ophthalmol | Historical note on streptomycin's discovery (1943); main content concerns tobramycin, not streptomycin, in ophthalmology |

---

## India Market Information

Streptomycin currently has **no valid drug registration in India** (0 licenses on file). No marketed product, dosage form, or approved indication text is available from regulatory records.

---

## Safety Considerations

- **Drug Interactions**: Among 177 recorded interactions, several are rated **Major**, including:
  - Botulinum toxin type A — Major (risk of potentiated neuromuscular blockade)
  - Human immunoglobulin G (intravenous) — Major
  - Bacitracin — Major
  - Additional **Moderate**-level interactions include Amikacin, Amphotericin B (and lipid complex), NSAIDs (Ibuprofen, Ketorolac, Celecoxib, Acetylsalicylic acid), bisphosphonates (Alendronic acid, Risedronic acid, Ibandronate), estrogens (Ethinylestradiol, Estradiol), Rabeprazole, Mesalazine, Balsalazide, and topical Neomycin.

No product-label warnings or contraindications are currently available for this drug (data gap, see below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking**-severity data gap exists on the product label warnings/contraindications, which prevents completion of the S1 safety pre-assessment required before advancing this candidate.
- The supporting evidence for conjunctivitis specifically is limited to **L3** (historical case series/cohort studies from 1947–1953 and isolated case reports), with **no clinical trials** and no modern comparative data; several cited papers are only tangentially relevant (different drugs, unrelated species).
- The drug has **no current market registration in India**, and the target indication ("conjunctivitis") as predicted is too broad — the plausible mechanistic link only applies to the bacterial subtype (tuberculous, brucella, trachoma), not the majority viral/allergic cases.

**To proceed, the following is needed:**
- Product label warnings/contraindications (DG001) to complete the S1 safety pre-assessment
- Detailed mechanism of action data (DG002) to substantiate mechanistic relevance
- Narrowing of the target indication to a specific bacterial conjunctivitis subtype, aligned with existing evidence
- Confirmation of an appropriate ophthalmic route/formulation, given known aminoglycoside ototoxicity/nephrotoxicity concerns and the current lack of route-compatibility data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

