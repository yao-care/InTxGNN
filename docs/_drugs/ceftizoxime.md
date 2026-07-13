---
layout: default
title: Ceftizoxime
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 6
---

# Ceftizoxime
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

# Ceftizoxime: From Broad-Spectrum Antibacterial Therapy to Gonococcal Urethritis

## One-Sentence Summary

Ceftizoxime is a third-generation cephalosporin antibiotic with established broad-spectrum antibacterial activity, originally developed for treatment of serious gram-negative bacterial infections.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis**,
with **0 registered clinical trials** and **11 publications** (including 1 direct head-to-head RCT vs. ceftriaxone) currently supporting this direction.
This prediction is strongly mechanistically grounded, as ceftizoxime's beta-lactam mechanism directly targets the cell wall synthesis pathway of *Neisseria gonorrhoeae*, including penicillinase-producing strains (PPNG).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (third-generation cephalosporin) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ceftizoxime is a third-generation cephalosporin antibiotic that exerts its bactericidal effect by binding to penicillin-binding proteins (PBPs), thereby inhibiting the final transpeptidation step of bacterial cell wall peptidoglycan synthesis. Critically, ceftizoxime is highly stable against beta-lactamase hydrolysis, which gives it activity against penicillinase-producing strains of *Neisseria gonorrhoeae* (PPNG) — strains that have rendered traditional penicillin therapy ineffective.

*Neisseria gonorrhoeae*, the causative organism of gonococcal urethritis, is a gram-negative diplococcus whose susceptibility to beta-lactam antibiotics is entirely dependent on the drug's affinity for gonococcal PBP2 and its resistance to beta-lactamase degradation. In vitro studies show ceftizoxime achieves an MIC₉₀ of 0.004 µg/mL against *N. gonorrhoeae* — well below clinically achievable serum concentrations following intramuscular injection. This places ceftizoxime pharmacodynamically on par with ceftriaxone, the current CDC-recommended agent.

The prediction is therefore not a speculative repurposing but a mechanistically direct extension: ceftizoxime's structural features that confer beta-lactamase stability and high PBP affinity are exactly the pharmacological properties required to treat PPNG-associated urethritis. The available clinical literature, including a direct head-to-head RCT comparing ceftizoxime with ceftriaxone (PMID 1948517), further validates this rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1948517](https://pubmed.ncbi.nlm.nih.gov/1948517/) | 1991 | RCT | Sexually Transmitted Diseases | Head-to-head comparison of single-dose ceftizoxime vs. ceftriaxone for uncomplicated urethral gonorrhea; both agents showed equivalent efficacy including against PPNG strains |
| [2264006](https://pubmed.ncbi.nlm.nih.gov/2264006/) | 1990 | Prospective Clinical Study | Sexually Transmitted Diseases | 175 male patients with confirmed gonococcal urethritis treated with single-dose ceftizoxime in LA (area with >1% PPNG prevalence); demonstrated efficacy as alternative to ceftriaxone |
| [6324399](https://pubmed.ncbi.nlm.nih.gov/6324399/) | 1984 | Prospective Clinical Study | Sexually Transmitted Diseases | 55 men with culture-confirmed gonococcal urethritis (including 47% PPNG) treated with 1 g IM ceftizoxime; 100% cure rate with no local or systemic adverse effects |
| [6092006](https://pubmed.ncbi.nlm.nih.gov/6092006/) | 1984 | In vitro/In vivo Susceptibility Study | Chemotherapy | Tested 102 freshly isolated *N. gonorrhoeae* strains (>50% partially/fully penicillin-resistant); MIC₉₀ of ceftizoxime = 0.004 µg/mL, demonstrating superior activity vs. penicillin |
| [6325750](https://pubmed.ncbi.nlm.nih.gov/6325750/) | 1983 | Clinical Evaluation | Japanese Journal of Antibiotics | 41 male patients with gonorrheal urethritis (15% PPNG) treated with ceftizoxime + probenecid; bacteriological and clinical evaluation of PPNG vs. non-PPNG strains |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance Surveillance | Journal of Infection and Chemotherapy | Reports emergence of cephem/aztreonam-resistant *N. gonorrhoeae* that does not produce beta-lactamase; raises alert regarding monitoring for ceftizoxime resistance development |
| [23416957](https://pubmed.ncbi.nlm.nih.gov/23416957/) | 2013 | Case Report / Phenotypic Characterization | Journal of Antimicrobial Chemotherapy | First two ESC-resistant *N. gonorrhoeae* cases in South Africa associated with cefixime treatment failure; relevant context for monitoring extended-spectrum cephalosporin resistance |
| [2122657](https://pubmed.ncbi.nlm.nih.gov/2122657/) | 1990 | Clinical Efficacy Study (comparator) | Acta Urologica Japonica | Epidemiological study of 109 gonococcal infections; evaluates cefetamet pivoxil as alternative agent — provides indirect evidence for third-generation cephalosporin class effect |
| [1416861](https://pubmed.ncbi.nlm.nih.gov/1416861/) | 1992 | Clinical Study (comparator) | Antimicrobial Agents and Chemotherapy | Dose-response study of oral cefpodoxime proxetil in male gonococcal urethritis; 100% eradication across all doses — supports third-generation cephalosporin class efficacy |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Large Cohort (comparator) | Current Medical Research and Opinion | 1,000-patient trial of cefetamet pivoxil showing single-dose efficacy in gonorrhea; comparative data reinforces class-level evidence |

---

## India Market Information

Ceftizoxime currently has **no registered products** in India (market status: not marketed). There are no authorization records to display.

---

## Safety Considerations

**Drug Interactions** (12 moderate-level interactions identified, source: DDInter):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Kanamycin | Moderate | Aminoglycoside combination — monitor for additive nephrotoxicity/ototoxicity |
| Neomycin | Moderate | Aminoglycoside combination — monitor renal function |
| Streptomycin | Moderate | Aminoglycoside combination — monitor renal function |
| Amikacin | Moderate | Aminoglycoside combination — monitor renal function |
| Amikacin (liposomal) | Moderate | Aminoglycoside combination — monitor renal function |
| Gentamicin | Moderate | Aminoglycoside combination — monitor renal function |
| Warfarin | Moderate | Beta-lactams may enhance anticoagulant effect; monitor INR |
| Chloramphenicol | Moderate | Potential antagonism with bacteriostatic agents against bactericidal cephalosporins |
| Ethinylestradiol | Moderate | Antibiotic may reduce enterohepatic recirculation of estrogen; advise additional contraceptive precautions |
| Mycophenolic acid | Moderate | Antibiotics may reduce mycophenolate exposure via gut flora disruption |
| Pemetrexed | Moderate | NSAIDs/renally cleared drugs may increase pemetrexed toxicity — monitor if co-administered |
| Picosulfuric acid | Moderate | Antibiotic may reduce bowel preparation efficacy |

> Note: Detailed prescribing warnings and contraindications were not available in this Evidence Pack. Please refer to the package insert for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for ceftizoxime in gonococcal urethritis is exceptionally strong — its beta-lactamase stability and high PBP affinity directly address both sensitive and PPNG strains of *N. gonorrhoeae*, and this is supported by multiple prospective clinical studies and one head-to-head RCT against the current standard of care (ceftriaxone). The TxGNN prediction reflects genuine pharmacological alignment rather than statistical artifact.

**To proceed, the following is needed:**

- **Formal India regulatory filing**: No current licenses exist; pathway assessment under CDSCO (Central Drugs Standard Control Organisation) required for market entry
- **Current resistance surveillance data**: The most recent literature (2001, 2013) raises concerns about emerging cephalosporin-resistant *N. gonorrhoeae* strains; updated local/regional MIC data for Indian gonococcal isolates is essential before recommending as first-line therapy
- **Mechanism of action documentation**: Retrieve full DrugBank MOA entry (DB01332) and CDSCO/WHO prescribing data to complete the pharmacological dossier
- **Safety package completion**: Obtain and parse the full prescribing information (package insert) for key warnings, contraindications, and special population data (renal impairment dosing, pregnancy category)
- **Formulation and route assessment**: Ceftizoxime is administered IM/IV — confirm that a single-dose IM formulation consistent with STI clinic workflows is available or developable for the India market
- **Comparison with current Indian STI treatment guidelines**: Confirm whether ceftizoxime offers advantages over ceftriaxone (already likely available) in the Indian gonorrhea treatment landscape, particularly regarding drug supply and cost
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

