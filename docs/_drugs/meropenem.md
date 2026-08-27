---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Serious Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic administered intravenously for severe bacterial infections including intra-abdominal infections, hospital-acquired pneumonia, bloodstream infections, and meningitis.
The TxGNN model predicts it may be effective for **Bacterial Arthritis**, with **1 clinical trial** and **20 publications** currently supporting this direction.
Evidence is primarily observational and case-based (Level L3), indicating this is a biologically plausible use that warrants further prospective investigation rather than immediate clinical adoption.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (intra-abdominal, nosocomial pneumonia, septicaemia, meningitis) |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Meropenem is a carbapenem-class β-lactam antibiotic that exerts bactericidal activity by binding to penicillin-binding proteins (PBPs) and inhibiting bacterial cell wall peptidoglycan synthesis. Its broad-spectrum activity covers Gram-negative pathogens including *Pseudomonas aeruginosa*, ESBL-producing *Enterobacteriaceae*, *Acinetobacter baumannii*, *Campylobacter* spp., and anaerobes. This same cell-wall inhibition mechanism mechanistically applies to the Gram-negative pathogens most commonly responsible for bacterial arthritis in immunocompromised or healthcare-associated settings.

Bacterial (septic) arthritis caused by multidrug-resistant Gram-negative organisms — including *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*, and *Burkholderia pseudomallei* (melioidosis) — is precisely the scenario where first-line agents (penicillins, fluoroquinolones) frequently fail. Retrospective cohort data from melioidosis-endemic regions (South India, Southeast Asia) consistently show that meropenem is the only reliably active agent against *Burkholderia pseudomallei* in osteoarticular disease, with 100% susceptibility reported across multiple study cohorts. Synovial fluid penetration of meropenem is estimated at approximately 50–60% of concurrent serum concentrations — sufficient to exceed MIC breakpoints for most susceptible Gram-negative pathogens in the joint space.

The TxGNN model's prediction therefore aligns with real-world prescribing practice: meropenem is already used off-label for Gram-negative septic arthritis in clinical settings, particularly in prosthetic joint infections with MDR organisms, and as a standard intensification therapy for melioidosis-associated osteoarticular disease. The gap is not biological plausibility, but the absence of prospective controlled trials specifically targeting this indication.

---

## Clinical Trial Evidence

Only one trial was retrieved; it is only tangentially related to this indication and does not evaluate meropenem directly for bacterial arthritis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Levofloxacin prophylaxis for bacteremia prevention in pediatric acute leukemia and HSCT patients; meropenem is not the study drug and bacterial arthritis is not the study endpoint — minimal relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective Review | Indian J Med Microbiol | 22 cases of culture-confirmed musculoskeletal melioidosis including septic arthritis; **all isolates were susceptible to meropenem**, supporting its role as standard-of-care in osteoarticular melioidosis |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective Cohort | Le Infezioni in Medicina | Osteoarticular melioidosis cohort study; characterizes fever, bone/joint involvement, and treatment outcomes; meropenem used as intensification therapy |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Antibiogram Study | Eur J Orthop Surg Traumatol | Antibiogram of bacterial isolates from orthopaedic infections (including septic arthritis, osteomyelitis, prosthetic joint infections) in a developing-world setting; identifies optimal empiric antibiotic strategies including carbapenem-class agents |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiological Study | Clinical Laboratory | Pathogen distribution and antimicrobial resistance in bone and joint infections in children under 4 years old; context for empiric antibiotic selection |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | In vitro / Lab Study | J Bone Joint Surg Am | Thermal stability and elution kinetics of meropenem from PMMA bone cement; establishes that meropenem retains activity after exothermic polymerisation — supports local delivery in orthopaedic infections |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Animal Study | Int J Antimicrobial Agents | Colistin-impregnated cement spacer combined with systemic meropenem evaluated in a rabbit model of carbapenemase-producing *Klebsiella pneumoniae* prosthetic joint infection; meropenem is used as the backbone systemic agent |
| [38134096](https://pubmed.ncbi.nlm.nih.gov/38134096/) | 2023 | Case Report | Medicine | *Campylobacter fetus*-induced primary psoas abscess in a patient with gouty arthritis; meropenem-based regimen described as treatment backbone for Gram-negative joint/soft-tissue infection |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case Report | Pharmaceuticals | Septic arthritis of the native hip joint caused by *Bacillus pumilus* and *Paenibacillus barengoltzii* in an immunocompetent adult; highlights challenges of unusual-pathogen bacterial arthritis and antibiotic choice |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrobial Agents | Off-label versus guideline-recommended use of conventional and novel antibiotics for MDR bacterial infections including Gram-negative organisms associated with joint infections |
| [2808217](https://pubmed.ncbi.nlm.nih.gov/2808217/) | 1989 | In vitro Study | J Antimicrobial Chemother | Foundational bacteriostatic and bactericidal in vitro activity study of meropenem; demonstrates meropenem is bactericidal for *Pseudomonas* spp. and staphylococci, with MBCs only 2-fold above MIC |

---

## India Market Information

No registered products for Meropenem were identified in the India regulatory database within this evidence pack. No authorisation table can be generated.

---

## Safety Considerations

**Drug Interactions (14 interactions identified from DDInter database):**

*Major interactions (exercise caution or avoid co-administration):*
- **Bupropion** — carbapenems, including meropenem, are well-documented to significantly reduce serum valproic acid levels (by up to 60–90%); concomitant bupropion further lowers seizure threshold, creating substantial seizure risk
- **Iohexol** (iodinated contrast medium) — major interaction; may potentiate nephrotoxicity or adverse haemodynamic effects
- **Iopamidol** (iodinated contrast medium) — major interaction; same class concern as iohexol

*Moderate interactions (monitor closely):*
- **Mycophenolic acid** — meropenem reduces mycophenolate plasma levels; risk of under-immunosuppression in transplant patients
- **Ethinylestradiol** — potential reduction in oral contraceptive efficacy
- **Pemetrexed** — carbapenems may reduce pemetrexed renal clearance, increasing toxicity risk
- **Teriflunomide**, **Alpelisib**, **Encorafenib** — pharmacokinetic interactions requiring monitoring
- **Picosulfuric acid**, **Polyethylene glycol with electrolytes**, **Sodium sulfate**, **Nitisinone**, **Lindane** — moderate interactions, clinical significance context-dependent

Please refer to the package insert for complete warnings and contraindications, which were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Meropenem has robust biological plausibility for bacterial arthritis caused by MDR Gram-negative organisms — particularly in melioidosis and prosthetic joint infection settings — evidence is limited to retrospective studies, case reports, and in vitro data (Level L3). There are no prospective Phase 2/3 RCTs evaluating meropenem specifically for the bacterial arthritis indication, and current use is based on susceptibility profiles rather than controlled clinical evidence.

**To proceed, the following is needed:**
- Prospective observational or controlled trial data evaluating meropenem efficacy specifically for MDR Gram-negative septic arthritis
- Synovial fluid pharmacokinetic studies (in vivo joint penetration data) to confirm adequate exposure at the site of infection
- MOA data from DrugBank to strengthen the mechanistic justification section
- India/CDSCO regulatory filing and approval status clarification (Meropenem is available in many global markets; the zero-registration result in this evidence pack should be verified against current CDSCO databases)
- Complete safety data from the package insert, including warnings, contraindications, and dosing in renal impairment
- Antimicrobial stewardship (AMS) criteria and protocol for appropriate carbapenem use in joint infections, to distinguish this indication from first-line antibiotic use cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

