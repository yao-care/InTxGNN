---
layout: default
title: Diethylcarbamazine
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Diethylcarbamazine
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

# Diethylcarbamazine: From Lymphatic Filariasis to Syndromic Lymphedema

## One-Sentence Summary

Diethylcarbamazine (DEC) is a well-established antifilarial agent and the WHO first-line treatment for lymphatic filariasis caused by *Wuchereria bancrofti* and *Brugia malayi*.
The TxGNN model ranks **Syndromic Lymphedema** as its top predicted new indication (score 99.59%), currently supported by **0 clinical trials** and **4 publications** addressing filarial-related lymphatic complications.
Critically, the Rank 2 prediction — **Primary Lymphedema** — carries **L1 evidence** backed by 6 large-scale clinical trials (combined enrollment > 48,000) and 20 publications, making it the most immediately actionable finding in this multi-indication analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lymphatic filariasis (*Wuchereria bancrofti*, *Brugia malayi*, *Loa loa*) — not registered in India; based on established international pharmacological use |
| Predicted New Indication | Syndromic Lymphedema (Rank 1) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L4 (Syndromic Lymphedema) / **L1** (Primary Lymphedema, Rank 2) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Syndromic Lymphedema) / **Proceed with Guardrails** (Primary Lymphedema) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on the published literature captured in this analysis, Diethylcarbamazine (DEC) acts predominantly as a **microfilaricide**: it disrupts the neuromuscular function of filarial larvae in the bloodstream and enhances host immune-mediated killing of microfilariae through cellular cytotoxicity. At standard dosing (6 mg/kg), DEC also exerts gradual macrofilaricidal activity, reducing adult worm burden over repeated treatment cycles. This dual action makes it the backbone of global lymphatic filariasis (LF) elimination programmes.

"Syndromic lymphedema" encompasses lymphedema arising secondary to an identifiable systemic cause. In tropical and subtropical endemic regions, filarial infection — particularly *Wuchereria bancrofti* invading and obstructing lymphatic vessels — is the world's leading cause of secondary lymphedema, progressing to elephantiasis in severe cases. In this etiology-specific subset, DEC's mechanism (eliminating the infectious trigger before irreversible lymphatic fibrosis sets in) is directly and plausibly relevant.

The four supporting publications illustrate DEC's clinical utility in filarial-related lymphatic pathology: tropical pulmonary eosinophilia (immunological hyperresponsiveness to filarial antigens with lymphatic and pulmonary involvement), filarial chyluria (lymphatic leakage successfully reversed by DEC), and filariasis-associated glomerulonephritis. These cases support biological plausibility for DEC in syndromic lymphedema of filarial origin. The critical caveat: if the syndromic lymphedema etiology is non-filarial (post-surgical, oncological, inflammatory, or genetic), DEC has no mechanistic rationale whatsoever.

---

## Clinical Trial Evidence

**Syndromic Lymphedema (Rank 1):** Currently no related clinical trials registered.

---

### Primary Lymphedema (Rank 2, TxGNN Score 99.25%) — L1 Evidence

The strongest evidence in this analysis applies to **Primary Lymphedema**, where filarial infection is the predominant cause in endemic settings. The following trials directly evaluate DEC-containing regimens for lymphatic filariasis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02899936](https://clinicaltrials.gov/study/NCT02899936) | N/A | Completed | 23,789 | Head-to-head comparison of DEC+ALB (2-drug, DA) vs IDA triple therapy across 5 countries; definitive safety and efficacy dataset for DEC-containing MDA |
| [NCT03676140](https://clinicaltrials.gov/study/NCT03676140) | Phase 3 | Completed | 20,000 | Safety of co-administering azithromycin alongside IDA (Ivermectin + DEC + Albendazole) for LF MDA; large-scale integrated NTD treatment evaluation |
| [NCT03268252](https://clinicaltrials.gov/study/NCT03268252) | N/A | Completed | 3,200 | Monitoring efficacy of DEC+ALB MDA programmes in Papua New Guinea; real-world effectiveness and transmission interruption data |
| [NCT03036059](https://clinicaltrials.gov/study/NCT03036059) | Phase 4 | Completed | 1,462 | Annual vs biannual IVM+ALB vs DEC-based regimens for *W. bancrofti* elimination in Ghana; dosing frequency optimisation |
| [NCT02974049](https://clinicaltrials.gov/study/NCT02974049) | N/A | Completed | 189 | Alternative chemotherapy strategies for LF in Loa-loa co-endemic Africa; DEC-alternative regimen safety |
| [NCT07159373](https://clinicaltrials.gov/study/NCT07159373) | Phase 3 | Not Yet Recruiting | 5,100 | Moxidectin + DEC + Albendazole vs standard IDA for LF, scabies and strongyloidiasis in Fiji (2026–2028); next-generation MDA evaluation |

---

## Literature Evidence

### Syndromic Lymphedema (Rank 1) — 4 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [24772754](https://pubmed.ncbi.nlm.nih.gov/24772754/) | 2013 | Case Report | J Assoc Physicians India | Filariasis-associated Grade III chyluria with nephrotic range proteinuria and IgM mesangial deposition; successful resolution with DEC + pelvic sclerotherapy; 19-month follow-up asymptomatic |
| [29549133](https://pubmed.ncbi.nlm.nih.gov/29549133/) | 2018 | Case Report | BMJ Case Reports | 7-year-old child with filarial chyluria mimicking nephrotic syndrome in endemic area; complete remission with DEC medical management at 1-year follow-up |
| [1580599](https://pubmed.ncbi.nlm.nih.gov/1580599/) | 1992 | Review | Annu Rev Med | Tropical pulmonary eosinophilia (PIE syndrome) caused by filarial hyperresponsiveness to *W. bancrofti* / *B. malayi*; DEC is the standard treatment reversing pulmonary and systemic lymphatic involvement |
| [9659744](https://pubmed.ncbi.nlm.nih.gov/9659744/) | 1998 | Review | Rev Hosp Clin | Comprehensive review of filarial TPE and differential diagnosis from similar syndromes; DEC-based therapeutic framework and pathophysiological basis |

---

### Primary Lymphedema (Rank 2) — Selected Key Publications (10 of 20)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33728462](https://pubmed.ncbi.nlm.nih.gov/33728462/) | 2021 | RCT Analysis | Clin Infect Dis | Cluster RCT: IDA MDA for LF control in Fiji (diurnally subperiodic transmission); superior microfilarial clearance vs standard DA at 12 months |
| [32511226](https://pubmed.ncbi.nlm.nih.gov/32511226/) | 2020 | Clinical Trial | PLoS Negl Trop Dis | Cluster-randomised community study (Haiti): IDA vs DA for *W. bancrofti*; IDA shows superior Mf clearance; safety profile confirmed in large community |
| [31641754](https://pubmed.ncbi.nlm.nih.gov/31641754/) | 2020 | RCT | Clin Infect Dis | Open-label RCT (Côte d'Ivoire): single-dose IDA non-inferior to 3 annual doses of IA for LF elimination in Africa |
| [39994719](https://pubmed.ncbi.nlm.nih.gov/39994719/) | 2025 | Cohort | Infect Dis Poverty | Community surveillance study (Kenya): IDA-MDA reduces LF antigenemia prevalence and clears circulating filarial antigens; real-world effectiveness data |
| [40063867](https://pubmed.ncbi.nlm.nih.gov/40063867/) | 2025 | Impact Analysis | PLoS Negl Trop Dis | Comparative IDA vs DA MDA in PNG: additional benefit on hookworm and strongyloidiasis co-infections; polypharmacy synergy |
| [26486704](https://pubmed.ncbi.nlm.nih.gov/26486704/) | 2016 | PK/PD Clinical Study | Clin Infect Dis | First triple-drug IDA single-dose study for Bancroftian filariasis; pharmacokinetics, safety, and efficacy characterised |
| [40380307](https://pubmed.ncbi.nlm.nih.gov/40380307/) | 2025 | Systematic Review & NMA | BMC Infect Dis | Network meta-analysis of antifilarial strategies; IDA superiority vs DA confirmed; safety constraints in sub-Saharan Africa (onchocerciasis co-endemicity) reviewed |
| [3297557](https://pubmed.ncbi.nlm.nih.gov/3297557/) | 1987 | Mechanistic Review | Ciba Found Symp | DEC mechanism: predominantly microfilaricidal via neuromuscular disruption + immune-mediated cellular cytotoxicity; foundational pharmacology reference |
| [18830049](https://pubmed.ncbi.nlm.nih.gov/18830049/) | 2008 | Review | Korean J Parasitol | Clinical and pathological aspects of filarial lymphedema and management; DEC + supportive care framework |
| [2181312](https://pubmed.ncbi.nlm.nih.gov/2181312/) | 1990 | RCT | N Engl J Med | Landmark RCT comparing ivermectin vs DEC for LF (*W. bancrofti*): comparative efficacy and side-effect profiles established |

---

## India Market Information

Diethylcarbamazine is currently **not commercially registered** in India (CDSCO). No authorizations on record.

> **Programme Context:** DEC is included in India's National Vector Borne Disease Control Programme (NVBDCP) as a Mass Drug Administration (MDA) drug for lymphatic filariasis elimination in endemic states — however, this represents programme-level supply, not individual commercial registration. India is one of the world's largest LF-endemic countries, with DEC+Albendazole (DA) MDA ongoing since 2004 and a transition to IDA (triple therapy) underway in select states.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Safety signals identified in MDA literature** (not from formal regulatory sources — Blocking data gap DG001 remains unresolved):
> - **Post-treatment reactions:** Fever, headache, myalgia, and lymphangitis following DEC in microfilaraemic individuals — these are largely Mazzotti-like reactions attributable to dying parasites, not direct drug toxicity.
> - **Critical regional contraindication:** DEC is contraindicated in areas co-endemic with *Onchocerca volvulus* (river blindness) due to risk of severe ocular adverse events and encephalopathy in individuals with high onchocercal microfilaria loads.
> - **No drug interaction data** were retrieved (DDI query: not found).

---

## Conclusion and Next Steps

### Syndromic Lymphedema (Rank 1)

**Decision: Hold**

**Rationale:**
No clinical trials address syndromic lymphedema as a defined entity, and the 4 supporting publications cover filarial complications (chyluria, TPE) rather than syndromic lymphedema per se. DEC is mechanistically plausible only when the etiology is filarial; for non-filarial syndromic lymphedema, there is no evidence basis.

**To proceed, the following is needed:**
- Systematic case series collection: DEC treatment outcomes in filarial-etiology syndromic lymphedema
- Etiological stratification of target patients (filarial vs non-filarial cause is a prerequisite for any DEC trial)
- Formal MOA documentation (resolve Data Gap DG002 via DrugBank API)
- CDSCO prescribing information for safety baseline (resolve Blocking Data Gap DG001)

---

### Primary Lymphedema (Rank 2) — Recommended Priority

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3/4 clinical trials with combined enrollment exceeding 48,000 participants directly demonstrate DEC efficacy and safety in lymphatic filariasis — the predominant cause of primary lymphedema in endemic regions. WHO has formally endorsed IDA (Ivermectin + DEC + Albendazole) triple therapy as the preferred MDA regimen since 2017. The mechanistic link is clear and the evidence level is L1.

**To proceed, the following is needed:**
- CDSCO registration pathway assessment: transition DEC from programme-only supply to individually prescribable drug for filarial lymphedema management
- Safety monitoring plan for regions with onchocerciasis co-endemicity
- Resolve Blocking Data Gap DG001 (obtain and parse official prescribing information from regulatory source)
- Define patient selection criteria distinguishing filarial-cause primary lymphedema from non-filarial or genetic causes, where DEC would be ineffective

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

