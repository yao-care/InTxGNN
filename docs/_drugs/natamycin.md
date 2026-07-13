---
layout: default
title: Natamycin
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Natamycin
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

# Natamycin: From Fungal Keratitis to Vulvovaginal Candidiasis

## One-Sentence Summary

Natamycin is a polyene macrolide antifungal agent, globally established for treating ophthalmic fungal infections (fungal keratitis) and topical candidiasis, but currently not registered in India.
The TxGNN model predicts it may be highly effective for **Vulvovaginal Candidiasis (VVC)**, with **1 completed Phase 3 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration; globally used for fungal keratitis and topical candidiasis |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Natamycin is a polyene macrolide antifungal that binds with high affinity to ergosterol — the principal sterol in fungal cell membranes. This binding forms transmembrane channels that disrupt ionic gradients, ultimately causing fungal cell death. Because ergosterol is absent in mammalian cells (which use cholesterol instead), this mechanism confers high selectivity for fungi with a favourable systemic safety profile.

Vulvovaginal candidiasis is caused predominantly by *Candida albicans* (accounting for 85–90% of cases), whose cell membrane is rich in ergosterol — precisely the molecular target of natamycin. The mechanistic link is therefore direct, specific, and biologically well-established. Furthermore, vaginal topical delivery achieves high local drug concentrations while systemic absorption remains negligible, making this route particularly well-suited to VVC treatment.

Globally, natamycin vaginal suppositories (marketed as Pimafucin®) have been used for vaginal candidiasis in Europe and other regions for over five decades. A recently completed Phase 3 RCT (NCT06411314, 2023, n=218) confirmed the efficacy of the natamycin/lactulose combination — with results published in 2025 (PMID 39979898). The TxGNN prediction therefore aligns closely with established international clinical evidence; the primary objective for India is market entry rather than de novo mechanistic repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | Completed | 218 | International RCT comparing Natamycin 100 mg + Lactulose 300 mg vaginal suppositories vs. Natamycin 100 mg alone (Pimafucin) vs. Lactulose 300 mg alone in non-pregnant adult females with VVC. The combination arm demonstrated superior efficacy; safety also assessed. Results published in BMC Women's Health (2025). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT (Phase 3) | BMC Women's Health | Natamycin + Lactulose vaginal suppositories assessed for efficacy and safety in adult females with VVC; direct highest-level evidence for natamycin-based vaginal formulation |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | RCT | Medical Journal of Australia | Comparative trial of natamycin pessaries vs. amphotericin B pessaries in vaginal candidiasis; established early head-to-head clinical efficacy of natamycin |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Clinical Trial | Acta Obstetricia et Gynecologica Scandinavica | 33 patients treated with natamycin vaginal tablets for 10 days; cure rate 88–94% at 1-month follow-up; partner co-treatment did not significantly improve outcomes |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | Clinical Trial | ANZ Journal of Obstetrics and Gynaecology | Controlled trial (n=120) comparing lytic enzyme preparation (Elase) plus natamycin vs. natamycin alone in monilial vulvovaginitis; combination improved both symptom alleviation and organism eradication |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Clinical Trial | Zentralblatt für Gynäkologie | Combination of oral metronidazole and vaginal natamycin tablets in mixed urogenital infections; Candida vaginal mycoses cured clinically in 89% of patients after the first treatment course |
| [6972554](https://pubmed.ncbi.nlm.nih.gov/6972554/) | 1981 | Clinical Study | Przeglad Dermatologiczny | Multiple natamycin formulations evaluated in cutaneous and mucosal multifocal candidiasis including vaginal sites; supports broad-spectrum mucosal antifungal activity |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | Clinical Study | New Zealand Medical Journal | 50 women with vaginal *C. albicans* treated with natamycin vaginal tablets twice nightly for 10 days; 76% cure rate at 2 weeks, maintained at 4-week follow-up |
| [4545913](https://pubmed.ncbi.nlm.nih.gov/4545913/) | 1972 | Clinical Observation | Sbor. Věd. Pr. LF UK Hradec Králové | Clinical experience treating gynaecological candidiasis and trichomoniasis with natamycin; supports gynaecological antifungal use |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Česká Gynekologie | Review of diagnostics and treatment of chronic vaginal candidiasis; direct comparison of natamycin vs. clotrimazole, supporting natamycin as a clinically effective option |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Survey | Česká a Slovenská Farmacie | Survey of VVC management in Ukraine (n=408); lifetime VVC prevalence 72.6%; vaginal itching and cottage cheese-like discharge were the most common symptoms; contextualises current clinical practice and natamycin's role |

---

## India Market Information

Natamycin currently has **no registered products** in India. There are no approved licenses, authorised formulations, or recorded market history in the Indian regulatory system as of the data cut-off date (2026-04-04). A de novo CDSCO market authorisation application will be required before commercial use is possible.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT06411314, n=218, published 2025) directly demonstrates natamycin's efficacy in vulvovaginal candidiasis, and the drug has a decades-long international safety and efficacy record under the brand Pimafucin®. The mechanistic basis (selective ergosterol-binding against *Candida* species) is well-characterised and directly applicable to VVC, and local vaginal delivery minimises systemic exposure. The primary barrier to use in India is the absence of local registration, not a lack of clinical evidence.

**To proceed, the following is needed:**
- Preparation and submission of a full regulatory dossier to CDSCO (Central Drugs Standard Control Organisation) for market authorisation in India
- Download and parsing of full package insert to complete mandatory safety assessment (key warnings, contraindications — Data Gap DG001)
- Retrieval of detailed mechanism of action data via DrugBank API (Data Gap DG002)
- Design of a local pharmacovigilance plan aligned with CDSCO requirements
- Clarification of appropriate dosage form strategy for the Indian market (vaginal suppositories vs. tablets) and assessment of import/local manufacturing pathway
- Consideration of special population data (pregnancy safety: case-control evidence available, PMID 12849848) for labelling purposes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

