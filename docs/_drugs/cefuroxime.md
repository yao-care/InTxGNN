---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Respiratory Tract Infections to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic widely used for respiratory tract infections and other bacterial infections in markets where it is registered.
The TxGNN model predicts it may be effective for **Urinary Tract Infection** — a finding confirmed by the available evidence base,
with **17 clinical trials** and **20 publications** supporting this direction, including a completed real-world study of 973 patients with pyelonephritis.
Notably, this represents a validation of an established clinical use in other markets rather than a truly novel repurposing, making it a strong regulatory opportunity for India where Cefuroxime is not yet registered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory tract infections and other bacterial infections (not registered in India; approval basis derived from international labels and included literature) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on indication selection:** TxGNN's highest-ranked prediction for Cefuroxime is hyperamylasemia (score 99.76%, L5, Hold), which has no supporting evidence and reflects a spurious knowledge graph path. This report focuses on **Urinary Tract Infection** (TxGNN rank 6, score 99.62%), which carries the strongest evidence (L1) and the most actionable recommendation.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Cefuroxime is a second-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs). This disrupts the transpeptidation step required for peptidoglycan cross-linking, leading to cell lysis and death. Cefuroxime axetil, its oral prodrug form, is hydrolysed in the gut wall to release active Cefuroxime, achieving systemic bactericidal concentrations.

The bactericidal mechanism that makes Cefuroxime effective against respiratory pathogens (*Haemophilus influenzae*, *Streptococcus pneumoniae*, *Streptococcus pyogenes*) applies equally to the major uropathogens responsible for urinary tract infections: *Escherichia coli*, *Klebsiella pneumoniae*, and *Proteus mirabilis* are all within Cefuroxime's susceptibility spectrum. This shared Gram-negative and Gram-positive antibacterial coverage explains the TxGNN model's high confidence score and the strength of the supporting evidence.

Cefuroxime axetil has received formal regulatory approval for UTI in the United States (FDA), the European Union, and multiple Asian markets. Study NCT04616352 directly evaluated Cefuroxime in pyelonephritis (n=973, completed), while PMID 30234077 prospectively confirmed the safety and efficacy of oral cefuroxime-axetil in febrile paediatric UTI. The breadth and maturity of this evidence base places Cefuroxime well above the threshold for a regulatory submission in India.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Direct real-world evaluation of Cefuroxime in pyelonephritis (upper UTI); assesses mortality and morbidity risk when Cefuroxime is used against second-generation cephalosporin–resistant organisms |
| [NCT03221504](https://clinicaltrials.gov/study/NCT03221504) | N/A | Unknown | 221 | RCT comparing 7-day vs 10-day antibiotic therapy for febrile UTI in children; Cefuroxime among the commonly used agents; evaluates whether shorter courses maintain efficacy with fewer adverse events |
| [NCT05609240](https://clinicaltrials.gov/study/NCT05609240) | Phase 2 | Recruiting | 180 | Feasibility RCT comparing bolus vs bolus-plus-continuous infusion Cefuroxime prophylaxis for post-colorectal surgery infections including bladder/kidney infections; directly optimises Cefuroxime dosing |
| [NCT04146142](https://clinicaltrials.gov/study/NCT04146142) | N/A | Completed | 550 | RCT: antibiotic prophylaxis vs none before transperineal prostate biopsy; evaluates Cefuroxime for prevention of post-procedural UTI and sepsis |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Evaluates whether prophylactic antibiotics (including Cefuroxime) at urinary catheter removal prevent catheter-associated UTI; large real-world cohort |
| [NCT02072798](https://clinicaltrials.gov/study/NCT02072798) | Phase 4 | Completed | 42 | Phase 4 RCT of Cefuroxime prophylaxis for post-caesarean infections including UTI and endometritis; formally registered indication-level evidence |
| [NCT05337566](https://clinicaltrials.gov/study/NCT05337566) | N/A | Recruiting | 2278 | Placebo-controlled RCT: azithromycin + Cefuroxime vs Cefuroxime alone for post-hysterectomy infection prevention; Cefuroxime is the standard-of-care comparator arm; n=2278 |
| [NCT03020940](https://clinicaltrials.gov/study/NCT03020940) | N/A | Unknown | 100000 | Post-marketing real-world registry study of Cefuroxime axetil dispersible tablets; 100,000-case safety and efficacy re-evaluation across multiple indications including UTI |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotic treatment during puerperium for pregnant women with recurrent bacteriuria/UTI; Cefuroxime among agents evaluated; assesses reduction in UTI recurrence rate |
| [NCT05530174](https://clinicaltrials.gov/study/NCT05530174) | N/A | Active, not recruiting | 2000 | Cluster RCT comparing single vs multiple prophylactic antibiotic doses (Cefuroxime) after primary total hip arthroplasty in fracture patients; infection endpoints include UTI |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | The Lancet Infectious Diseases | Multicentre RCT: de-escalation from antipseudomonal β-lactams to narrow-spectrum agents including Cefuroxime in Enterobacterales bacteraemia — supports Cefuroxime as a safe de-escalation choice in urinary-source bacteraemia |
| [30234077](https://pubmed.ncbi.nlm.nih.gov/30234077/) | 2018 | Prospective Cohort | Frontiers in Pediatrics | 2-year prospective study: oral cefuroxime-axetil in children with first febrile UTI (n=82); confirmed fever resolution in most patients, good antibiotic tolerance, and low loss to follow-up |
| [40135203](https://pubmed.ncbi.nlm.nih.gov/40135203/) | 2025 | Multicenter Observational | IJID Regions | Klebsiella pneumoniae UTI susceptibility across 18 Indian centres (DASH study); directly maps Cefuroxime's real-world utility for UTI stewardship in India |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Prospective Cohort | Infectious Diseases & Clinical Microbiology | Community-acquired UTI causative organisms and risk factors for ESBL production; provides Cefuroxime susceptibility context against E. coli and Klebsiella |
| [35096675](https://pubmed.ncbi.nlm.nih.gov/35096675/) | 2021 | Retrospective Cohort | Germs | UTI microbiology and antibiotic resistance data from Romanian children; Cefuroxime susceptibility rates reported for E. coli |
| [35733866](https://pubmed.ncbi.nlm.nih.gov/35733866/) | 2022 | Propensity Score Analysis | Frontiers in Medicine | Carbapenem prophylaxis and risk of ESC-resistant Enterobacterales UTI in kidney transplant recipients; positions Cefuroxime within the hierarchy of UTI prophylaxis options |
| [26607682](https://pubmed.ncbi.nlm.nih.gov/26607682/) | 2016 | Cohort | Brazilian Journal of Infectious Diseases | Follow-up of infants <2 months with UTI; recurrence microbiological patterns inform appropriate antibiotic selection including Cefuroxime-class agents |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Narrative Review | International Journal of Antimicrobial Agents | Comprehensive pharmacological review of Cefuroxime axetil; confirms UTI as an approved indication alongside respiratory infections with pharmacokinetic data |
| [35069075](https://pubmed.ncbi.nlm.nih.gov/35069075/) | 2021 | Review | Menopause Review | Strategies to avoid antibiotic resistance in UTI treatment and prevention; Cefuroxime cited as second-line agent with relevant spectrum for E. coli and Gram-positive uropathogens |
| [30197697](https://pubmed.ncbi.nlm.nih.gov/30197697/) | 2018 | Case Report | Open Microbiology Journal | Non-typable *H. influenzae* UTI associated with renal stone disease; Cefuroxime active against this less common uropathogen, broadening the clinical relevance |

---

## India Market Information

Cefuroxime is currently **not registered** in India. There are **0** drug authorizations on record in the CDSCO database. This absence represents both a regulatory gap and a market opportunity, given the drug's widespread approval for UTI in the US, EU, and multiple Asian markets.

---

## Safety Considerations

**Drug Interactions:** 143 interactions documented (DDInter database). Key moderate-level interactions relevant to clinical use:

- **Acid-suppressing drugs** — H₂ blockers (Famotidine, Ranitidine, Cimetidine, Nizatidine) and PPIs (Omeprazole, Lansoprazole, Rabeprazole, Esomeprazole, Pantoprazole, Dexlansoprazole): Reduced gastric acidity decreases absorption of oral Cefuroxime axetil, which requires an acid environment for optimal bioavailability. Clinical recommendation: administer with food; avoid concurrent acid suppression if possible.
- **Antacids** (Aluminum hydroxide, Calcium carbonate, Magnesium hydroxide, Magnesium carbonate, Magnesium oxide, Magaldrate): Similar absorption impairment; stagger administration by at least 2 hours.
- **Aminoglycosides** (Kanamycin, Neomycin): Potential additive nephrotoxicity; monitor renal function in combination therapy.
- **Balsalazide**: Moderate interaction; potential for reduced antibiotic systemic exposure.

> Complete warnings and contraindications data were not available in this Evidence Pack. Please refer to an authorised package insert (e.g., FDA label or EMA SmPC) for full safety information pending CDSCO registration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefuroxime axetil has mature L1-level evidence for UTI across multiple completed trials and prospective cohort studies, and holds formal regulatory approval for this indication in the US, EU, and several Asian markets — making the path to CDSCO registration well-precedented. The primary guardrail is ensuring local antibiogram data supports sufficient susceptibility among India's prevalent uropathogens, particularly given rising ESBL rates documented in Indian centres (PMID 40135203).

**To proceed, the following is needed:**
- Obtain and review the FDA or EMA-approved Cefuroxime package insert to document warnings, contraindications, and pregnancy/paediatric dosing for submission to CDSCO
- Resolve the MOA data gap (DG002) via DrugBank API to support mechanistic narrative in regulatory dossier
- Commission or compile local Indian antibiogram data specific to UTI pathogens (E. coli, Klebsiella) to confirm adequate Cefuroxime susceptibility rates in the target market
- Define a drug interaction management protocol for patients on PPIs or antacids (high co-prescription probability in UTI populations)
- Conduct regulatory pathway assessment with CDSCO for a new drug registration — precedent from approvals in comparable markets (US, Japan, EU) should support an abbreviated dossier pathway
- Perform pharmacoeconomic analysis to position Cefuroxime axetil against existing registered UTI antibiotics in India (e.g., Nitrofurantoin, Norfloxacin, Fosfomycin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

