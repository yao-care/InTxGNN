---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Topical Antifungal Therapy to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal historically used to treat candidal (fungal) infections of the skin and mucosa. The TxGNN model's top prediction — **Vulvovaginitis** (Candida-driven) — is supported by a **99.92% prediction score**, **20 publications**, but **no registered clinical trials**, and the underlying evidence itself indicates this is largely a reaffirmation of nystatin's long-established, pre-azole-era role in vulvovaginal candidiasis rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (Data Gap) — nystatin is a polyene antifungal; literature evidence (PMID 1436934) indicates it was the original first-line topical/vaginal antifungal for candidiasis before azoles superseded it |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset (Data Gap, flagged High severity for downstream mechanistic analysis). Based on the information present in the supporting evidence, however, nystatin is a polyene antifungal that binds directly to ergosterol in fungal cell membranes, forming pores that lead to cell lysis and death.

Vulvovaginitis is predominantly caused by *Candida albicans* (85–90% of cases per the cited literature), making nystatin's antifungal mechanism directly applicable to the pathogen rather than a speculative cross-indication link. Indeed, the evidence pack's own rationale notes this is essentially "reaffirmation of a known indication" — nystatin vaginal formulations were the original standard of care for vulvovaginal candidiasis in the 1950s–1970s before imidazole/triazole agents became first-line. This context matters for interpretation: the high TxGNN score here reflects rediscovery of an established pharmacological relationship rather than a new repurposing opportunity, which should temper enthusiasm relative to a true novel signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Reviews management of fluconazole-resistant vulvovaginal candidiasis, noting nystatin among alternative agents alongside boric acid and newer antifungals |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis after bacterial vaginosis; *C. albicans* accounts for 85–90% of cases |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Recurrent VVC remains difficult to manage; non-albicans species show increasing azole resistance |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | Confirms VVC epidemiology and *C. albicans* predominance |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clinical Evidence | Reiterates VVC as second most common vaginitis cause |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | General review of vulvovaginal candidiasis diagnosis and management |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287 *Candida* isolates from 283 patients tested for fluconazole/nystatin susceptibility; correlated in vitro sensitivity with clinical outcomes in complicated VVC |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska Gynekologie | Evaluated combined vaginal nystatin + nifuratel products for mixed/miscellaneous vulvovaginal infections |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical | BMC Microbiology | Rat model: nystatin enhanced mucosal immune response against *C. albicans* and protected vaginal epithelial ultrastructure |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | Preclinical | Infection and Drug Resistance | Compared ZnO nanoparticles and nystatin effects on virulence gene (SAP1-3) expression in fluconazole-resistant *C. albicans* from VVC patients |

---

## Safety Considerations

- **Drug Interactions**: A completed DDI query identified **347 total documented interactions**. Severity levels are currently unclassified ("Unknown") for all entries, including with commonly co-prescribed agents such as cyclosporine, fluconazole, erythromycin, azithromycin, pravastatin, valsartan, ramipril, tramadol, and pantoprazole. Given the sheer volume and lack of severity grading, individual interaction review is needed before clinical use.

Formal warnings, contraindications, and local package-insert safety data are not currently available — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between nystatin and vulvovaginitis is strong and biologically direct (Evidence Level L2), but the supporting evidence consists entirely of observational/review literature with no clinical trials, and largely confirms an already-known historical use rather than a novel repurposing signal. Combined with a Blocking-severity gap in local safety/label data, this indication should not proceed to full evaluation without additional safeguards.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, Blocking)
- Formal mechanism of action documentation from DrugBank (DG002, High)
- Severity classification for the 347 identified drug-drug interactions
- Confirmation of India market/registration intent, given the drug is currently not marketed there

**Note on other candidates:** Ranks 2–7, 9, and 10 (disease of orbital region, disease of orbital part of eye adnexa, cystic teratoma, spinal cord dermoid cyst, postmenopausal atrophic vaginitis, biotin metabolic disease, commissural lip fistula, osteoradionecrosis of the mandible) all scored L5/S0 with no clinical or mechanistic support and are recommended **Hold** — these appear to be embedding-similarity artifacts rather than credible repurposing leads. Rank 8 (vulvitis) shares the same evidentiary profile and rationale as vulvovaginitis (L2, Proceed with Guardrails) and should be evaluated jointly with it rather than as a separate candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

