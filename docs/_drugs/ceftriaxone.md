---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic broadly used to treat serious bacterial infections including meningitis, pneumonia, and sepsis.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **3 clinical trials** and **19 publications** currently supporting this direction — including multiple RCTs directly evaluating ceftriaxone in acute otitis media (AOM) treatment protocols.

> **Note on report scope:** The TxGNN model produced 7 predictions for ceftriaxone. The highest-ranked prediction by model score (polyclonal hyperviscosity syndrome, score 99.39%) carries no supporting clinical evidence (L5, Hold). This report focuses on **Infectious Otitis Media** (TxGNN rank 4), which is the strongest actionable prediction with Level L2 evidence and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (meningitis, sepsis, pneumonia, gonorrhoea) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| India Market Status | ⚠️ Registry shows "Not Marketed" — likely a data gap; ceftriaxone is on the WHO Essential Medicines List and widely available in India under brand names (Monocef, Oframax, etc.) |
| Number of Registrations | 0 (registry data incomplete) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Ceftriaxone is a third-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), blocking peptidoglycan cross-linking and triggering bacterial lysis. Its defining pharmacokinetic advantages include a long half-life (~8 hours) enabling once-daily dosing, high serum protein binding (~95%), and excellent penetration into middle ear fluid.

Ceftriaxone's antibacterial spectrum directly covers all three major pathogens responsible for acute otitis media: *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. This is the same mechanistic basis underlying its use in meningitis and community-acquired pneumonia — pathogen overlap across respiratory and ear-nose-throat infections means the pharmacological bridge is direct, not inferential. As a parenteral (IM/IV) agent, ceftriaxone fills a specific clinical gap in AOM management: patients who fail first-line oral amoxicillin, cannot take oral medications, carry penicillin-resistant *S. pneumoniae*, or belong to high-risk groups such as cochlear implant recipients.

Multiple international paediatric guidelines — including those from the American Academy of Pediatrics (AAP) and the Infectious Diseases Society of America (IDSA) — explicitly recommend intramuscular ceftriaxone as a second-line or salvage therapy for AOM. This is therefore not a speculative repurposing signal: the TxGNN model has identified a clinically established but under-formalised use case in the India regulatory context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study assessing Prevnar 13 impact on otitis media in children; independently confirms *S. pneumoniae* as the primary AOM pathogen and validates the bacteriological rationale for ceftriaxone use |
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Multicentre double-blind RCT comparing 5-day vs. 10-day antibiotic therapy for AOM in children aged 6–23 months; addresses antimicrobial resistance as primary endpoint; early termination requires review of cause before weight can be assigned |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | RCT evaluating tympanostomy tube placement vs. non-surgical management for recurrent AOM over 2 years; establishes recurrent AOM severity and the high unmet need for effective salvage antibiotics |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective randomised single-blind trial: single IM dose of ceftriaxone vs. 10-day TMP-SMZ for AOM; assessed clinical cure rates in children — foundational head-to-head comparison |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | 1-day vs. 3-day IM ceftriaxone in non-responsive AOM; 3-day regimen showed superior bacteriologic eradication, particularly for resistant *S. pneumoniae* |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical Trial | *Pediatric Infectious Disease Journal* | Bacteriologic efficacy of 3-day IM ceftriaxone in children with non-responsive AOM; demonstrated effective eradication of penicillin-resistant pneumococcal strains |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Clinical Trial | *Pediatric Infectious Disease Journal* | Compared 1- vs. 3-day ceftriaxone on nasopharyngeal *S. pneumoniae* carriage; 3-day regimen reduced resistant-strain carriage more effectively |
| [12750572](https://pubmed.ncbi.nlm.nih.gov/12750572/) | 1998 | Clinical Trial | *Le Infezioni in Medicina* | Three-arm study (amoxicillin / cefuroxime axetil / single-dose IM ceftriaxone) for AOM in 75 children aged 6 months–6 years; no statistically significant difference in clinical efficacy |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *International Journal of Pediatric Otorhinolaryngology* | Large US primary care database study; documents rising IM ceftriaxone use for AOM, particularly for otitis-conjunctivitis syndrome, as a proxy signal for increasing antimicrobial resistance |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus Guideline | *Clinical Pediatrics* | Expert consensus for AOM management in paediatric practice; IM ceftriaxone explicitly recommended for treatment-failure scenarios |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | *Clinical Therapeutics* | Synthesises three major AOM treatment guideline publications; provides revised recommendations including ceftriaxone positioning |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review/Guideline | *Otology & Neurotology* | Guidelines for AOM and meningitis prevention and treatment in children with cochlear implants; highlights ceftriaxone as preferred parenteral agent in this high-risk population |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review/Guideline | *JAMA Network Open* | Optimal paediatric outpatient antibiotic prescribing; addresses appropriateness of ceftriaxone use in AOM, contextualising stewardship considerations |

---

## India Market Information

The Evidence Pack indicates 0 registered licenses for Ceftriaxone in India. This is almost certainly a data retrieval gap rather than a true absence — ceftriaxone is a WHO Essential Medicine, appears on India's National List of Essential Medicines (NLEM), and is widely manufactured and marketed in India under numerous brand names (Monocef, Oframax, Emcef, Biotrakson, and others). A direct CDSCO database query is required to confirm registered formulations and approved indications.

---

## Safety Considerations

**Drug Interactions (from 164 documented interactions; key clinical alerts shown):**

| Interacting Drug | Severity | Clinical Implication |
|------|------|------|
| Calcium chloride | **Major** | Ceftriaxone-calcium complex forms insoluble precipitates in IV lines; potentially fatal in neonates — concurrent IV administration contraindicated |
| Calcium glucoheptonate | **Major** | Same precipitation mechanism; avoid concurrent IV use |
| Calcium gluconate | **Major** | Same precipitation mechanism; neonates at highest risk |
| Kanamycin | Moderate | Additive nephrotoxicity risk; monitor renal function |
| Neomycin | Moderate | Additive nephrotoxicity risk |
| Streptomycin | Moderate | Additive nephrotoxicity risk |
| Picosulfuric acid | Moderate | Potential pharmacokinetic interaction; monitor clinical response |

Please refer to the package insert for full prescribing information, including complete warnings, contraindications, and dosing guidance. CDSCO-approved labelling should be obtained to complete the safety profile for the India market context.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs (1997–2002) and consistent international paediatric guidelines establish ceftriaxone's efficacy in acute otitis media, particularly for resistant *S. pneumoniae* and treatment-failure cases. The mechanistic link is direct and well-characterised. The primary barrier is not clinical evidence but regulatory formalisation in the India market context and the need for an antimicrobial stewardship framework to govern use.

**To proceed, the following is needed:**

- **Regulatory confirmation:** Conduct a direct CDSCO database query to identify existing registered formulations and approved indications; clarify whether otitis media is already an approved or commonly recognised off-label indication
- **Safety data completion:** Retrieve CDSCO-approved prescribing information (package insert) including full contraindications and warnings (currently a Blocking data gap)
- **MOA documentation:** Pull complete mechanistic and pharmacokinetic profile from DrugBank API (DB01212) to formally complete the mechanistic analysis
- **Patient selection criteria:** Define target population for India (treatment-failure AOM, penicillin allergy, cochlear implant recipients, resistant *S. pneumoniae* endemic areas)
- **Stewardship protocol:** Develop antimicrobial stewardship guidelines governing indications, duration, and resistance monitoring to prevent inappropriate use of a critically important antibiotic
- **Pharmacoeconomic review:** Assess cost-effectiveness of IM ceftriaxone vs. standard oral AOM therapy in Indian outpatient and paediatric settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

