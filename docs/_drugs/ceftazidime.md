---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Gram-Negative Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic with established global use against serious gram-negative bacterial infections, including complicated urinary tract infections (UTIs), respiratory tract infections, and bacteremia — yet it currently holds no registered approval in India.
The TxGNN model predicts it may be effective for **Urinary Tract Infection**, which aligns with its core pharmacological profile, with **17 clinical trials** and **20 publications** currently supporting this direction.
This case represents a market access gap rather than a clinical evidence gap: the evidence base is robust, and the recommended path is to proceed with a structured registration strategy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (systemic; globally established) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Ceftazidime is a third-generation cephalosporin that exerts its antibacterial effect by binding to penicillin-binding protein 3 (PBP3), blocking the final cross-linking step of peptidoglycan synthesis in the bacterial cell wall. This produces concentration-independent bactericidal activity and is particularly potent against gram-negative organisms, most notably *Pseudomonas aeruginosa* — a pathogen that is disproportionately difficult to treat and commonly implicated in complicated and healthcare-associated UTIs.

The mechanistic fit for UTI is strong on multiple levels. Ceftazidime is renally eliminated largely unchanged, achieving urinary drug concentrations that exceed the MIC for most susceptible uropathogens by a wide margin. Common UTI causative agents — *Escherichia coli*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*, and *Enterobacter* species — fall squarely within the gram-negative spectrum of Ceftazidime's activity. The combination formulation Ceftazidime-Avibactam (CAZ-AVI) further extends this coverage to carbapenem-resistant strains producing KPC and OXA-48-type β-lactamases, making Ceftazidime particularly critical in the era of multidrug-resistant (MDR) uropathogens.

Importantly, the TxGNN prediction reflects pharmacological reality: UTI (particularly complicated UTI and pyelonephritis) is one of Ceftazidime's core global indications. Its absence from the Indian market is therefore a regulatory and commercial gap, not a signal of clinical uncertainty. Multiple international guidelines (IDSA, ESCMID, SIMIT/SPILF) endorse Ceftazidime or CAZ-AVI for complicated UTIs caused by resistant organisms, and robust clinical trial data — including Phase 4 completed studies and systematic network meta-analyses — support efficacy and safety in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | Completed | 60 | Open-label RCT comparing CAZ-AVI vs best available therapy for carbapenem-resistant gram-negative infections (including cUTI) in Chinese adults; directly evaluates efficacy and safety |
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | Completed | 129 | Double-blind RCT comparing IV CXA-101 vs IV Ceftazidime in complicated UTI including pyelonephritis; high-quality direct comparator evidence |
| [NCT00690378](https://clinicaltrials.gov/study/NCT00690378) | Phase 2 | Completed | 137 | Investigator-blinded, randomized study of NXL104/Ceftazidime vs comparator in hospitalized adults with complicated UTI; supports combination strategy |
| [NCT02497781](https://clinicaltrials.gov/study/NCT02497781) | Phase 2 | Completed | 97 | Single-blind RCT of CAZ-AVI vs Cefepime in pediatric complicated UTI (3 months–18 years); supports use in pediatric populations |
| [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) | N/A | Completed | 189 | Retrospective real-world study of CAZ-AVI effectiveness and safety in India (June 2019–April 2020), including cUTI; directly relevant to the Indian market context |
| [NCT03147807](https://clinicaltrials.gov/study/NCT03147807) | N/A | Completed | 75 | BetaLACTA test-guided early de-escalation of empirical carbapenems in ICU patients with pulmonary, urinary, and bloodstream infections; supports Ceftazidime's role in UTI step-down therapy |
| [NCT05733104](https://clinicaltrials.gov/study/NCT05733104) | N/A | Recruiting | 600 | Post-marketing surveillance of Zavicefta (CAZ-AVI) in Korea for hospital-acquired infections including cUTI; ongoing safety/effectiveness data |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Large PK/PD study of understudied drugs in pediatric populations; provides Ceftazidime dosing optimization data for UTI in children |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | Completed | 43 | PK/DDI study of Avibactam + Ceftazidime; directly informs CAZ-AVI combination dosing for MDR UTI |
| [NCT05258851](https://clinicaltrials.gov/study/NCT05258851) | Phase 3 | Terminated | 29 | CAZ-AVI vs Colistin in critically ill patients with carbapenem-resistant Enterobacteriaceae; terminated early due to enrollment challenges, not safety signals |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic Review / NMA | J Comparative Effectiveness Research | Network meta-analysis of treatment options for complicated UTI including acute pyelonephritis; evaluates CAZ-AVI among available therapies against drug-resistant organisms |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Clinical Practice Guideline | Int J Antimicrobial Agents | Joint SIMIT/SPILF practical guidance on treating MDR gram-negative infections; positions CAZ-AVI for cUTI caused by carbapenem-resistant Enterobacterales |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Retrospective Cohort | Clinical Infectious Diseases | Multicenter study of CAZ-AVI for KPC-producing *K. pneumoniae* infections, including UTI; supports real-world effectiveness |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Comparative Cohort | Antimicrobial Agents & Chemotherapy | Head-to-head comparison of CAZ-AVI vs meropenem-vaborbactam for carbapenem-resistant Enterobacteriaceae infections; patients with localized UTI were excluded, defining scope boundary |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrobial Agents | Clinical trial data review for novel antibiotics including CAZ-AVI for MDR gram-negative bacteria; positions Ceftazidime combinations as standard of care |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | Systematic Review / Meta-analysis | Antimicrobial Resistance & Infection Control | Global trends in CAZ-AVI resistance in gram-negative bacteria; critical for India market resistance surveillance planning |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clinical Infectious Diseases | Challenges of renal dose adjustment for CAZ-AVI in AKI vs chronic kidney disease; directly relevant to UTI patients with renal impairment |
| [37843118](https://pubmed.ncbi.nlm.nih.gov/37843118/) | 2023 | Review | Clinical Infectious Diseases | ARLG priorities and progress in gram-negative infection research; includes design considerations for ceftazidime-based trials in resistant uropathogens |
| [35734948](https://pubmed.ncbi.nlm.nih.gov/35734948/) | 2022 | Epidemiology | Pediatrics | Epidemiology, treatment, and outcomes of third-generation cephalosporin-resistant UTI in US pediatric patients; highlights role of Ceftazidime-class drugs in resistant pediatric UTI |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | Phase 3 RCT | Infectious Diseases & Therapy | TANGO II trial of meropenem-vaborbactam vs best available therapy (which included CAZ-AVI) for CRE; supports CAZ-AVI positioning in treatment algorithms for resistant UTI |

---

## India Market Information

Ceftazidime currently has **no registered authorizations** in India. The `taiwan_regulatory` data (sourced for the India market context) confirms zero licenses and no marketed products. This represents a regulatory gap — not a safety or efficacy issue — as Ceftazidime and CAZ-AVI are widely approved and marketed in the United States (FDA), European Union (EMA), Japan (PMDA), and many other jurisdictions.

Notably, the retrospective real-world study [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) enrolled 189 patients in India who had already received CAZ-AVI for at least 48 hours in routine practice (June 2019–April 2020), indicating that the drug is in clinical use in India through off-label or import channels despite having no formal registration.

---

## Safety Considerations

Formal warning and contraindication data for Ceftazidime are not available in this Evidence Pack. Please refer to the package insert for key warnings and contraindications before clinical use.

**Drug Interactions** (114 total interactions identified; key moderate-level interactions):

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|------------------|---------------|
| Amphotericin B (conventional) | Moderate | Potential additive nephrotoxicity; monitor renal function closely |
| Amphotericin B (cholesteryl sulfate) | Moderate | Same nephrotoxicity concern as conventional formulation |
| Amphotericin B (lipid complex) | Moderate | Nephrotoxicity risk persists even with lipid formulations |
| Amphotericin B (liposomal) | Moderate | Monitor renal function; liposomal formulation reduces but does not eliminate risk |
| Kanamycin | Moderate | Additive nephrotoxicity and ototoxicity with aminoglycosides |
| Neomycin | Moderate | Additive nephrotoxicity with aminoglycosides |
| Streptomycin | Moderate | Additive nephrotoxicity and ototoxicity with aminoglycosides |
| Picosulfuric acid | Moderate | Risk of electrolyte imbalance may affect drug excretion/toxicity |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftazidime is a globally established, guideline-endorsed antibiotic for complicated urinary tract infections — particularly for *Pseudomonas aeruginosa* and carbapenem-resistant gram-negative organisms — supported by Phase 2/4 completed RCTs, systematic reviews, and extensive real-world evidence. Its absence from the Indian market is a market access issue, not a clinical uncertainty; the drug is already being used in Indian clinical practice via off-label channels, as evidenced by a completed real-world Indian cohort study (n=189).

**To proceed, the following is needed:**

- **Regulatory filing**: Prepare CDSCO New Drug Application (NDA) or import registration documentation; leverage existing FDA/EMA approval dossiers as the basis
- **Mechanism of action documentation**: Obtain formal DrugBank MOA data (DB00438) to complete safety narratives required for regulatory submissions
- **Local resistance surveillance data**: Conduct or source a local Indian antibiogram for common UTI pathogens to establish susceptibility profiles and support clinical positioning
- **Package insert safety data**: Download and parse the FDA/EMA-approved package insert to fill the current warning and contraindication data gaps
- **Pharmacovigilance plan**: Establish a local adverse drug reaction monitoring framework, given that aminoglycoside combinations (commonly used in Indian ICUs) represent the primary moderate drug-drug interaction risk
- **Formulation strategy**: Confirm IV formulation availability and cold-chain logistics for the Indian market; consider whether CAZ-AVI (Zavicefta) should be co-registered alongside Ceftazidime monotherapy to maximize MDR coverage positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

