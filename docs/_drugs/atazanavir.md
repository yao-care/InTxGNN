---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atazanavir: From HIV-1 Infection to Congenital Human Immunodeficiency Virus

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor widely used in combination antiretroviral therapy (cART) for adult HIV-1 infection.
The TxGNN model predicts it may also be effective for **Congenital Human Immunodeficiency Virus** (perinatally-acquired HIV),
with **33 clinical trials** and **7 publications** currently supporting this direction.

> **Note on ranking:** The top-ranked TxGNN predictions (ranks 1–3) identify non-human animal diseases (SIV infection, feline AIDS) and a rare neurodevelopmental disorder with no mechanistic link — none of which represent actionable human clinical targets. Rank 4 flags an obsolete ontology term for hyperlipidemia, a condition that Atazanavir is actually known to worsen as a side effect. This report therefore focuses on **rank 5 (Congenital Human Immunodeficiency Virus, score 99.71%)** as the most clinically meaningful and evidence-supported prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (combination antiretroviral therapy) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the system database (DG002). Based on known information, Atazanavir is an azapeptide-class HIV-1 protease inhibitor. It selectively blocks HIV-1 protease — the enzyme responsible for cleaving the viral gag and gag-pol polyproteins into functional structural and enzymatic proteins during viral maturation. Without this processing step, newly assembled viral particles remain immature and non-infectious. Atazanavir is typically co-administered with a pharmacokinetic booster (ritonavir or cobicistat) to enhance systemic exposure by inhibiting CYP3A4-mediated first-pass metabolism.

Congenital (perinatally-acquired) HIV infection occurs through vertical mother-to-child transmission during pregnancy, delivery, or breastfeeding. The underlying pathology is mechanistically identical to adult HIV-1 infection — the same viral protease targeted by Atazanavir drives replication in perinatally infected neonates and infants. This makes the mechanistic rationale direct and scientifically sound, not a speculative extrapolation. Furthermore, Atazanavir/ritonavir is already included in DHHS and WHO guidelines as an option for prevention of mother-to-child transmission (PMTCT) in pregnant women, establishing a clear biological and clinical continuum between adult and congenital HIV treatment.

What makes this prediction particularly strong is the existence of dedicated pediatric regulatory data. The PRINCE I study (NCT01099579) established pharmacokinetics and safety for children aged ≥3 months to <6 years using the powder formulation, and the PRINCE II study (NCT01335698) extended this to children 3 months to <11 years. A separate Phase IV study (NCT01691794) collected safety data in adolescents aged 6 to <18 years. This age-stratified evidence base is rare among antiretrovirals and directly supports use in congenital HIV cases across the full pediatric age spectrum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Atazanavir + ritonavir or saquinavir + TDF + nucleoside vs lopinavir/ritonavir in treatment-experienced HIV subjects; landmark efficacy comparison |
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | 96-week head-to-head comparison of atazanavir/ritonavir vs lopinavir/ritonavir + TDF-FTC in treatment-naive HIV adults |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | Dolutegravir/abacavir/lamivudine vs atazanavir + ritonavir + TDF/FTC once daily in HIV-naive women |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | Atazanavir powder + ritonavir safety, efficacy, and pharmacokinetics in pediatric HIV patients aged 3 months to <11 years (PRINCE II) |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | Atazanavir powder + ritonavir in pediatric HIV patients aged 3 months to <6 years (PRINCE I) |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | Atazanavir capsule + ritonavir long-term safety data in pediatric patients aged 6 to <18 years |
| [NCT00207142](https://clinicaltrials.gov/study/NCT00207142) | Phase 4 | Completed | 252 | Atazanavir boosted vs unboosted maintenance strategy after ATV/RTV induction in treatment-naive HIV adults (INDUMA study) |
| [NCT00135356](https://clinicaltrials.gov/study/NCT00135356) | Phase 4 | Completed | 219 | Atazanavir-based regimen switch for lipodystrophy management in HIV patients (REAL study) |
| [NCT01232127](https://clinicaltrials.gov/study/NCT01232127) | Phase 4 | Completed | 25 | Dedicated DDI study: effect of famotidine twice daily on atazanavir PK when co-administered with ritonavir and tenofovir |
| [NCT01003990](https://clinicaltrials.gov/study/NCT01003990) | Phase 3 | Completed | 710 | Atazanavir extended access study providing long-term safety and tolerability data across HIV clinical trial completers |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort | Frontiers in Immunology | PHACS SMARTT study: safety surveillance of in utero ARV exposure in >3,500 HIV-exposed uninfected children across 22 US sites; evaluates metabolic, cardiac, neurological, and neurodevelopmental domains |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort / PK Study | Antiviral Therapy | Atazanavir pharmacokinetic exposure remains therapeutically adequate during pregnancy regardless of tenofovir co-administration — directly supports PMTCT dosing guidance |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Assessment of congenital anomaly risk associated with in utero antiretroviral exposure in HIV-exposed uninfected infants; provides reassurance data for most agents |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case-Control | European Journal of Clinical Pharmacology | European congenital anomaly registry analysis of fetal ARV drug exposure; most recent large-scale safety evaluation using population-level data |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In Vitro Pharmacology | Reproductive Toxicology | Atazanavir and ritonavir interactions with placental ABC transporters (ABCB1, ABCG2, ABCC2) — characterizes factors affecting transplacental drug disposition in rats |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cross-Sectional | Journal of AIDS and Immune Research | Newborn hearing screening outcomes in 1,435 HIV-exposed uninfected infants with in utero ARV exposure from the SMARTT cohort; evaluates ototoxicity signal |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | Clinical Infectious Diseases | Multi-database pharmacovigilance analysis of antiretroviral safety signals in pregnancy; contextual reference for systematic ARV adverse event monitoring methodology |

---

## India Market Information

Atazanavir is currently **not registered in India**. No CDSCO authorizations are on record. The drug is marketed internationally as **Reyataz** (Bristol-Myers Squibb) in capsule and powder formulations. Generic versions are available in some markets. Any commercialization pathway in India would require a new drug application to CDSCO.

---

## Safety Considerations

**Drug Interactions:**

Atazanavir has **277 recorded drug interactions**. Two categories are clinically critical:

**Major interactions requiring clinical management:**

| Interacting Drug | Level | Clinical Concern |
|----------------|-------|----------------|
| Famotidine, Ranitidine | Major | H2-blockers raise gastric pH, significantly reducing Atazanavir absorption; confirmed by dedicated PK study NCT01232127 |
| Rabeprazole, Omeprazole | Major | PPIs substantially reduce Atazanavir bioavailability; concurrent use generally contraindicated without dose adjustment |
| Triamcinolone, Budesonide | Major | Atazanavir inhibits CYP3A4, causing corticosteroid overexposure; risk of iatrogenic Cushing's syndrome |
| Loperamide | Major | CYP3A4 inhibition increases loperamide plasma levels; cardiac risk |

**Moderate interactions (selected):**

Antidiabetic agents (Metformin, Pioglitazone, Alogliptin, Acarbose, Albiglutide), antacids (Aluminum hydroxide, Calcium carbonate), and several corticosteroids (Hydrocortisone, Betamethasone, nasal Budesonide) all carry moderate interaction flags.

Please refer to the full prescribing information for complete warnings, contraindications, and dose adjustment guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atazanavir's mechanism of action directly targets the HIV-1 protease enzyme, which drives viral replication equally in congenital/perinatally-acquired HIV and adult HIV-1 infection. Multiple completed Phase III trials establish efficacy in HIV, and dedicated pediatric pharmacokinetic and safety programs (PRINCE I & II) provide age-appropriate dosing data down to 3 months of age — evidence that directly addresses the congenital HIV clinical context. The L1 evidence level justifies clinical use, but India-specific regulatory and operational steps are required before market entry.

**To proceed, the following is needed:**

- **Regulatory pathway**: File a new drug application with CDSCO for India market authorization; reference international approvals (FDA, EMA) as supportive data
- **Safety documentation**: Download and review complete package insert (TFDA/FDA full prescribing information) to document all formal warnings and contraindications (DG001)
- **MOA documentation**: Query DrugBank API to retrieve formal mechanism of action data for completeness of mechanistic analysis (DG002)
- **Drug interaction management**: Develop clinical protocols for managing acid-suppressing agents (PPIs, H2-blockers), which are frequently co-prescribed in pediatric settings and significantly impair Atazanavir absorption
- **Guideline alignment**: Review current Indian pediatric HIV treatment guidelines and compare positioning of Atazanavir vs. integrase inhibitor-based first-line regimens (dolutegravir is increasingly preferred globally)
- **Pharmacoeconomics**: Assess cost-effectiveness and supply chain feasibility for the India market, including generic availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

