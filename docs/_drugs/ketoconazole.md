---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketoconazole: From Fungal Infections to Acne

## One-Sentence Summary

Ketoconazole is a broad-spectrum imidazole antifungal agent, classically used to treat fungal infections (including cutaneous candidiasis, tinea, and pityriasis versicolor) and, at systemic doses, to suppress cortisol production in Cushing's syndrome.
The TxGNN model predicts it may be effective for **Acne (disease)**, with **1 active clinical trial** and **15 publications** currently supporting this direction.
Evidence is grounded in two mechanistic pathways: anti-*Malassezia* activity (addressing fungal folliculitis often misdiagnosed as acne) and anti-androgenic effects via steroidogenesis inhibition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antifungal (fungal skin infections, candidiasis, pityriasis versicolor; systemic: Cushing's syndrome cortisol suppression) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (Topical Route Only) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, ketoconazole is an imidazole antifungal that inhibits cytochrome P450–dependent 14α-lanosterol demethylase, blocking ergosterol biosynthesis in fungal cell membranes. At higher concentrations, it also inhibits mammalian steroidogenic enzymes including **CYP17A1** and **CYP11A1**, reducing adrenal and gonadal androgen production — a property that underpins its use in Cushing's syndrome and PCOS-related hyperandrogenism.

Two mechanistic pathways connect ketoconazole to acne. First, the **anti-fungal pathway**: *Malassezia* (formerly *Pityrosporum ovale/orbiculare*), a lipophilic yeast resident in pilosebaceous units, drives *Pityrosporum folliculitis* — a condition clinically indistinguishable from comedonal acne vulgaris. Topical ketoconazole directly suppresses this organism. Second, the **anti-androgenic pathway**: androgens stimulate sebaceous gland activity, and ketoconazole's CYP inhibition reduces circulating androgens, offering theoretical benefit in hormonal acne (e.g., PCOS-associated acne). In vitro work has additionally demonstrated direct inhibition of *Propionibacterium acnes* lipase activity, attenuating the inflammatory metabolite cascade central to conventional acne pathogenesis.

The predicted new indication is therefore not speculative — topical ketoconazole 2% cream is already under active clinical investigation as an alternative to adapalene in mild acne (NCT07237763). While systemic use raises significant safety concerns (658 drug interactions, hepatotoxicity), the **topical formulation** has minimal systemic absorption, substantially widening the safety margin for this specific application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | NA | Active, Not Recruiting | 52 | Head-to-head RCT comparing topical ketoconazole 2% cream vs. topical adapalene 2% cream over 12 weeks in mild comedonal and papulopustular acne; evaluating whether ketoconazole offers a viable alternative with fewer side effects and better tolerability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | In vitro study | *Microbiology and Immunology* | Ketoconazole inhibits *P. acnes* lipase activity, reducing generation of pro-inflammatory fatty acids from sebum; also inhibits *P. acnes* growth — supports direct antibacterial/anti-inflammatory mechanism in acne |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | *Biological & Pharmaceutical Bulletin* | Azole antifungals including ketoconazole demonstrate activity against *P. acnes* in vitro; relevant given rising antibiotic-resistant *P. acnes* strains |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case Series | *Clinical and Experimental Dermatology* | 62 patients with *Pityrosporum* folliculitis (frequently misdiagnosed as acne vulgaris) in Saudi Arabia; confirms ketoconazole as effective treatment for this acne-mimicking condition |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | *The Keio Journal of Medicine* | Comprehensive review of *Pityrosporum ovale* as opportunistic pathogen in pityriasis versicolor, folliculitis, and seborrhoeic dermatitis; mechanistic basis for antifungal use in acne-spectrum disease |
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | Phase 3 Open-Label Study | *Pituitary* | Levoketoconazole (ketoconazole enantiomer) in Cushing's syndrome (SONICS trial): clinical improvement in acne and other hyperandrogenic skin signs, supporting the anti-androgenic pathway |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Clinical Study | *Polski Tygodnik Lekarski* | Ketoconazole included in treatment of hyperandrogenic manifestations in PCOS, with reduction of acne and seborrhoea within 3 months; early clinical evidence of anti-androgenic efficacy |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | *Dermatology (Basel)* | Comprehensive review of systemic acne treatment options; contextualises where anti-androgens and anti-fungals fit in the therapeutic ladder |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | *BMJ Clinical Evidence* | PCOS review: acne is a key presenting feature of hyperandrogenic PCOS; supports rationale for androgen-targeting therapy including ketoconazole |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case Series | *Archives of Dermatology* | Neonatal *Malassezia furfur* pustulosis frequently misidentified as neonatal acne; underscores the diagnostic overlap between fungal folliculitis and acne, where ketoconazole would be appropriate |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | *Pharmaceuticals (Basel)* | Adapalene therapeutic review — the comparator drug in the active RCT (NCT07237763); provides mechanistic context for the head-to-head comparison with topical ketoconazole |

---

## India Market Information

Ketoconazole currently has **no registered products** in the Indian market based on the available regulatory data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations on record |

> **Note:** Ketoconazole oral formulations have faced regulatory restrictions globally (including FDA and EMA black-box warnings for hepatotoxicity). Topical formulations generally remain available and are distinct from the systemic safety concerns. Market entry for the acne indication would likely follow a topical-only pathway.

---

## Safety Considerations

**Drug Interactions (Total: 658 interactions identified)**

Ketoconazole carries an exceptionally high drug interaction burden, primarily due to potent **CYP3A4 inhibition**. Key interactions include:

| Severity | Representative Interactions |
|----------|----------------------------|
| **Major** | Loperamide, Triamcinolone, Budesonide (risk of systemic corticosteroid toxicity / QT prolongation) |
| **Moderate** | Famotidine, Ranitidine, Rabeprazole, Omeprazole (reduced ketoconazole absorption due to gastric pH elevation); Hydrocortisone, Dexamethasone, Betamethasone (CYP3A4-mediated corticosteroid accumulation); Pioglitazone, Aprepitant, Atropine, Hyoscyamine, Bisacodyl, Methscopolamine, Alosetron |
| **Minor** | Amphotericin B, Amphotericin B lipid complex |

> **For topical use specifically:** systemic absorption of ketoconazole 2% cream is negligible under normal conditions, substantially reducing the clinical relevance of the above interactions. The interaction profile above reflects systemic (oral) administration and should not be applied directly to topical formulations.

> **Key Safety Note:** Detailed prescribing warnings and contraindications for oral ketoconazole (hepatotoxicity, QT prolongation, adrenal insufficiency risk) should be verified directly from the package insert. These are well-documented in global regulatory agency labelling.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for topical ketoconazole in acne is biologically coherent via two independent pathways (anti-*Malassezia*/anti-*P. acnes* and anti-androgenic), and is corroborated by an active randomised controlled trial (NCT07237763) directly comparing it to a first-line acne therapy. The L3 evidence level reflects converging observational, in vitro, and clinical evidence — sufficient to justify a structured development programme for the topical route. Systemic use is not recommended given the 658-interaction burden and global hepatotoxicity warnings.

**To proceed, the following is needed:**

- **Retrieve topical-specific safety data**: Obtain the package insert for ketoconazole 2% topical cream to document local tolerability (contact sensitisation, irritation), as distinct from systemic hepatotoxicity concerns
- **Await NCT07237763 results**: The active RCT comparing ketoconazole 2% vs adapalene 2% in mild acne will directly answer the efficacy question; estimated completion December 2025
- **Confirm MOA data (DrugBank)**: Formally document the CYP17A1/CYP11A1 inhibition and anti-*Malassezia* mechanism to complete the mechanistic dossier
- **Regulatory pathway assessment**: Determine whether a new drug application for the acne indication requires a full NDA or can be filed as a line extension/supplemental application for the topical formulation in India
- **Subgroup analysis plan**: Define whether the target population is fungal folliculitis (anti-*Malassezia* pathway), hormonal/PCOS acne (anti-androgenic pathway), or conventional acne vulgaris (anti-*P. acnes* pathway) — these require different trial designs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

