---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a broad-spectrum triazole antifungal agent widely used to treat systemic and superficial fungal infections including aspergillosis, histoplasmosis, and onychomycosis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (infection caused by *Pneumocystis jirovecii*),
with **0 clinical trials** and **20 publications** identified — however, critical mechanistic evidence strongly contradicts this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic and superficial fungal infections (aspergillosis, histoplasmosis, onychomycosis, etc.) |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* pneumonia, PCP) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Itraconazole belongs to the triazole antifungal class and exerts its effect by inhibiting **lanosterol 14α-demethylase (CYP51/Erg11)**, a key enzyme in the ergosterol biosynthesis pathway. By blocking ergosterol production, itraconazole disrupts fungal cell membrane integrity and function. This mechanism is highly effective against organisms whose cell membranes depend on ergosterol, such as *Aspergillus*, *Histoplasma*, and *Candida* species.

However, there is a **fundamental mechanistic contradiction** with this prediction: *Pneumocystis jirovecii* is a unique atypical fungus whose cell membrane **lacks ergosterol entirely** — it substitutes cholesterol instead. Because itraconazole's target enzyme (Erg11) requires ergosterol as the downstream product, all azole antifungals and polyene antifungals (which also target ergosterol) are **intrinsically ineffective** against *P. jirovecii*. This is corroborated by the molecular study (PMID 12606318), which confirmed that the *P. carinii* Erg11 protein shares key amino acid substitutions associated with azole resistance.

The co-occurrence of itraconazole and pneumocystosis in the literature most likely reflects **ecological association rather than therapeutic relevance**: both conditions frequently arise in the same immunocompromised patient populations (HIV/AIDS, organ transplant recipients, patients on corticosteroids), not because itraconazole treats PCP. The first-line treatment for PCP remains TMP-SMX, with alternatives including pentamidine, atovaquone, and clindamycin + primaquine. This prediction is therefore considered a likely **ecological fallacy** in the TxGNN model output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT (double-blind, placebo-controlled) | HIV Medicine | Phase III trial of itraconazole prophylaxis in HIV-infected patients; evaluated prevention of **deep fungal infections** (not PCP specifically) |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Clinical Guideline / Review | BMJ Clinical Evidence | HIV opportunistic infection prophylaxis guidelines; PCP prophylaxis centres on TMP-SMX, not azoles |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Review of protozoan infection therapy including *P. carinii*; azoles not listed as treatment options |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Lung transplant infections; PCP prophylaxis discussed without mention of itraconazole |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Bone marrow transplant antimicrobial prophylaxis; itraconazole mentioned for fungal coverage, not PCP |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Basic Science | Am J Respir Cell Mol Biol | Characterised *P. carinii* Erg11; confirmed inherent resistance to azoles due to specific amino acid substitutions — **key mechanistic evidence against this repurposing** |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Retrospective Cohort | Transplantation Proceedings | Invasive fungal infections post-kidney transplant; itraconazole used for mould coverage, PCP treated separately with TMP-SMX |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational Study | Indian Journal of Medical Microbiology | Respiratory fungal pathogens in immunocompromised vs. immunocompetent hosts; PCP and azole-susceptible fungi co-occur in same population |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | *Talaromyces marneffei* + *P. jirovecii* co-infection in a child with STAT1 mutation; itraconazole used for talaromycosis, not PCP |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case Report | Annals of Internal Medicine | Uveitis associated with rifabutin prophylaxis and itraconazole therapy in an HIV patient; highlights itraconazole DDI risk in this population |

---

## Safety Considerations

**Drug Interactions (295 interactions identified; selected major and clinically significant interactions listed below):**

| Severity | Interacting Drug | Clinical Relevance |
|----------|----------------|--------------------|
| **Major** | Loperamide | Risk of serious cardiac events (QT prolongation / torsades de pointes) |
| **Major** | Triamcinolone | Itraconazole inhibits CYP3A4, markedly increasing corticosteroid exposure; risk of Cushing's syndrome and adrenal suppression |
| **Major** | Budesonide | Same mechanism as triamcinolone; systemic budesonide levels can increase dramatically |
| Moderate | Omeprazole, Rabeprazole | Proton pump inhibitors reduce gastric acid → impaired absorption of itraconazole capsules |
| Moderate | Famotidine, Ranitidine, Cimetidine | H2 blockers reduce gastric acid → impaired itraconazole capsule absorption |
| Moderate | Dexamethasone, Hydrocortisone, Betamethasone | CYP3A4 inhibition increases corticosteroid exposure |
| Moderate | Aprepitant | Mutual CYP3A4 interaction; increased plasma levels of both agents |
| Moderate | Alosetron | Increased alosetron exposure via CYP3A4 inhibition |
| Moderate | Budesonide (nasal) | Systemic absorption risk via CYP3A4 inhibition |
| Minor | Metformin, Pioglitazone | Minor pharmacokinetic interactions; clinical significance generally low |
| Minor | Amphotericin B / Amphotericin B (lipid complex) | Potential antagonism; itraconazole may reduce ergosterol availability needed for amphotericin B binding |

> For complete warnings, contraindications, and special population guidance, please refer to the approved package insert, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.34%), but this is a case where the model appears to have learned **co-occurrence in immunocompromised populations** rather than a genuine therapeutic relationship. The fundamental mechanistic barrier — *P. jirovecii* lacks ergosterol, the molecular target of all azole antifungals — makes itraconazole pharmacologically inactive against PCP. No clinical trials support this indication, and the existing literature does not contain evidence of itraconazole being used or studied as a PCP treatment.

**To proceed (if further investigation is deemed warranted), the following is needed:**

- **Mechanistic rebuttal investigation**: Confirm whether any novel mechanism (e.g., host-directed therapy, immunomodulatory effects, or inhibition of cholesterol pathway in *P. jirovecii*) could theoretically justify activity independent of ergosterol targeting
- **Full package insert data**: Retrieve TFDA/EMA/FDA prescribing information to complete safety assessment (key warnings, contraindications)
- **DrugBank MOA data**: Formally confirm mechanism of action via DrugBank API to support or refute the mechanistic analysis above
- **Expert consultation**: Obtain infectious disease specialist review before any further investment in this repurposing hypothesis
- **India regulatory pathway**: If evidence were to emerge, note that itraconazole is currently not registered in India (0 licenses), requiring a full regulatory submission

> ⚠️ **Research Note**: This result is provided for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

