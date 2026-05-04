---
layout: default
title: Luliconazole
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 7
---

# Luliconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Luliconazole: From Dermatophytosis to Pityriasis Versicolor

## One-Sentence Summary

Luliconazole is a topical imidazole antifungal agent used in multiple countries for the treatment of dermatophytosis (tinea infections), exerting potent fungicidal activity by disrupting fungal cell membrane ergosterol synthesis.
The TxGNN model predicts it may be effective for **Pityriasis Versicolor**,
with **1 clinical trial** (Phase 4, not yet recruiting) and **3 publications** currently supporting this direction.
Notably, a broader indication of **Superficial Mycosis** (Rank 2) carries even stronger evidence, including a completed Phase 3 RCT (L1 level).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dermatophytosis (tinea pedis, tinea corporis, tinea cruris) |
| Predicted New Indication | Pityriasis Versicolor |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not captured in this dataset. Based on published literature, luliconazole is a novel imidazole antifungal that inhibits **lanosterol 14α-demethylase (CYP51)**, a rate-limiting enzyme in fungal ergosterol biosynthesis. By depleting ergosterol, luliconazole disrupts cell membrane integrity and kills susceptible fungi. Luliconazole has among the lowest minimum inhibitory concentrations (MICs) reported for any topical azole, particularly against *Trichophyton* species.

Pityriasis versicolor is caused by lipophilic yeasts of the *Malassezia* genus (*M. furfur*, *M. globosa*, *M. sympodialis*), which — like dermatophytes — rely on ergosterol for cell membrane function. The CYP51 inhibition pathway is therefore equally applicable. In vitro work as early as 2003 (PMID 12636984) confirmed that luliconazole (then designated NND-502) achieves potent activity against all three major *Malassezia* species, with geometric mean MICs substantially lower than comparator agents lanoconazole, bifonazole, and terbinafine. A 2018 study (PMID 29198426) further confirmed broad-spectrum activity encompassing *Malassezia*, dermatophytes, and *Candida* species through the same CYP51 mechanism.

Clinically, a prospective open-label randomized comparative trial conducted in eastern India (PMID 27559523) directly evaluated topical luliconazole versus ketoconazole in pityriasis versicolor, indicating real-world clinical applicability. A forthcoming Phase 4 head-to-head RCT (NCT07333170, target completion November 2026) is designed to provide further confirmatory data. The TxGNN score of 99.13% reflects the tight biological link between the drug's established dermatophyte target and the *Malassezia* organisms driving pityriasis versicolor.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07333170](https://clinicaltrials.gov/study/NCT07333170) | Phase 4 | Not Yet Recruiting | 86 | Randomized controlled comparison of luliconazole 2% cream vs ketoconazole 1% cream for pityriasis versicolor; expected start February 2026, completion November 2026. No results available yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | Clinical Comparative Study (Open-label RCT) | Indian Dermatology Online Journal | Prospective, open, randomized controlled trial comparing topical ketoconazole and topical luliconazole in pityriasis versicolor patients at a tertiary care hospital in eastern India; directly relevant to the Indian market context |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In Vitro | Journal de Mycologie Médicale | Confirmed luliconazole as a broad-spectrum CYP51 inhibitor with activity against *Malassezia* species, *Candida albicans*, dermatophytes, and other clinically relevant fungi; notes prior clinical use in pityriasis versicolor |
| [12636984](https://pubmed.ncbi.nlm.nih.gov/12636984/) | 2003 | In Vitro | International Journal of Antimicrobial Agents | NND-502 (luliconazole) demonstrated potent in vitro activity against *M. furfur* (GM-MIC ~1.4 mg/L), *M. sympodialis* (~0.1 mg/L), and *M. slooffiae* (~1.0 mg/L), comparing favourably to lanoconazole, bifonazole, and terbinafine |

---

## India Market Information

Luliconazole is currently **not registered** in India. No CDSCO product authorizations are on record as of the data cut-off (April 4, 2026).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registrations found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Luliconazole's CYP51 inhibitory mechanism directly targets the ergosterol biosynthesis pathway of *Malassezia* spp., the causative organisms of pityriasis versicolor; an Indian-based clinical comparison study (PMID 27559523) has already demonstrated head-to-head efficacy against the standard-of-care ketoconazole, and a confirmatory Phase 4 RCT is actively planned. Broader superficial mycosis indications (Rank 2) are supported by a completed Phase 3 RCT (PMID 24385117, L1 evidence), further strengthening confidence in the drug class's efficacy in this space. The primary barriers are regulatory (no India registration) and data gaps in safety documentation.

**To proceed, the following is needed:**

- **MOA documentation**: Query DrugBank API for DB08933 to formally record the mechanism of action and pharmacological category
- **Package insert review**: Download and parse the TFDA, FDA, or EMA prescribing information PDF to extract key warnings, contraindications, and known drug interactions (currently blocking safety pre-screening)
- **Trial monitoring**: Track completion of NCT07333170 (expected November 2026) for Phase 4 head-to-head efficacy and safety data specific to pityriasis versicolor
- **Regulatory pathway assessment**: Evaluate CDSCO new drug application requirements for a topical antifungal not previously registered in India
- **Formulation confirmation**: Verify appropriate topical concentration (1% vs 2% cream) and delivery vehicle for the Indian climate and patient population, informed by approved specifications in Japan and the United States
- **Consider broadened indication**: Given L1 evidence for **Superficial Mycosis** (Rank 2, including tinea cruris Phase 3 RCT), a composite indication filing covering multiple superficial fungal infections may offer a stronger regulatory package than a pityriasis-only claim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

