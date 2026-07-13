---
layout: default
title: Cefprozil
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

# Cefprozil: From Respiratory Tract Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an orally active second-generation cephalosporin antibiotic, originally used to treat upper and lower respiratory tract infections and skin/soft tissue infections.
The TxGNN model predicts it may be effective for **Urinary Tract Infection**, with **no registered clinical trials** but **9 publications** (including 3 dedicated RCTs) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Upper/lower respiratory tract infections; skin and soft tissue infections |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on known pharmacological information, Cefprozil is an oral second-generation cephalosporin β-lactam antibiotic. β-lactam drugs inhibit bacterial cell wall synthesis by binding to and inactivating penicillin-binding proteins (PBPs), blocking peptidoglycan cross-linking and ultimately causing cell lysis. Cefprozil is particularly active against gram-positive organisms (*Streptococcus pyogenes*, *S. pneumoniae*, methicillin-susceptible *S. aureus*) and has moderate activity against gram-negative pathogens (*Haemophilus influenzae*, *Moraxella catarrhalis*, Enterobacteriaceae).

The rationale for UTI is mechanistically straightforward: the most common UTI pathogens — *Escherichia coli*, *Klebsiella pneumoniae*, and *Proteus mirabilis* — fall squarely within Cefprozil's antibacterial spectrum via PBP inhibition. Following oral administration, Cefprozil achieves high urinary concentrations, reaching therapeutic levels that exceed the MICs of susceptible uropathogens. In vitro data from clinical isolates in Taiwan (Liu et al., 1995) confirmed inhibition of >80% of *E. coli* and *Klebsiella* at 8 mg/L. This profile is mechanistically consistent with approved second-generation cephalosporins already used in UTI management guidelines.

Crucially, three randomized controlled trials conducted specifically for acute uncomplicated UTIs in the early 1990s demonstrated clinical and bacteriological cure rates of 93–94% with Cefprozil 500 mg once daily — comparable to Cefaclor as the active comparator. These trials provide direct clinical evidence rather than mere inference from spectrum data, elevating the confidence in this prediction to L1.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cefprozil in urinary tract infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | RCT | J Antimicrobial Chemotherapy | Open randomized trial in 102 adults: Cefprozil 500 mg QD vs Cefaclor 250 mg TID for 10 days in acute uncomplicated UTI; comparable clinical and bacteriological cure rates |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | RCT | Clinical Therapeutics | Multicenter randomized study in patients ≥2 years old: Cefprozil QD vs Cefaclor TID for 10 days; satisfactory clinical response rates comparable between groups |
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | RCT | Antimicrobial Agents & Chemotherapy | 108 college women with acute UTI; Cefprozil 500 mg QD vs Cefaclor 250 mg TID — clinical cure 94% and bacterial cure 93% for Cefprozil, not significantly different from Cefaclor |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Systematic Review | Drugs | Comprehensive review confirming Cefprozil's broad antibacterial activity including against common UTI pathogens (*E. coli*, *Klebsiella*, Enterobacteriaceae); MRSA and some gram-negatives not susceptible |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Drug Review | Pediatric Annals | Overview of Cefprozil's role in respiratory, skin, and UTI infections; favorable GI and dermatological side effect profile highlighted; once/twice daily dosing feasible |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Comparative Review | American Family Physician | Cefprozil among newer oral cephalosporins positioned as an effective, convenient twice-daily option for skin, respiratory, and urinary tract infections |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In Vitro Study | Chemotherapy | In vitro activity against 637 clinical isolates from Kaohsiung VGH, Taiwan: Cefprozil inhibited >80% of *E. coli* and *Klebsiella pneumoniae* at 8 mg/L; comparable to other oral cephalosporins |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Pediatric Clinical Study | Japanese J Antibiotics | PK/PD characterized in children after oral Cefprozil; urinary concentrations and recovery rates measured; relevant for pediatric UTI dosing |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Pediatric Clinical Study | Japanese J Antibiotics | 21 children with bacterial infections including 3 UTI cases; good to excellent clinical responses in 19/21 patients; all 11 bacterial strains eradicated |

---

## India Market Information

Cefprozil currently has **no product registrations in India**. No authorization records are available in the CDSCO database.

---

## Safety Considerations

**Drug Interactions** (55 interactions identified in DDInter database; notable interactions listed below):

*Moderate-level interactions:*

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Kanamycin | Moderate | Concurrent aminoglycoside use may increase nephrotoxicity risk |
| Neomycin | Moderate | Potential additive renal effects; monitor renal function |
| Streptomycin | Moderate | Caution with combined aminoglycoside use |
| Balsalazide | Moderate | Cephalosporins may alter gut microbiome, affecting balsalazide metabolism |
| Picosulfuric acid | Moderate | Antibiotics may reduce efficacy of gut-acting laxatives |

*Unknown-level interactions (selected notable agents):*

Acetylsalicylic acid, Amoxicillin, Pantoprazole, Omeprazole, Lansoprazole, Cimetidine, Prednisone, Prednisolone, Metformin, Simvastatin — interaction profiles with Cefprozil are not fully characterized in available databases.

For complete warnings and contraindications, please refer to the full package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three dedicated RCTs from the 1990s directly demonstrated Cefprozil's efficacy in acute uncomplicated UTIs with cure rates of ~93–94%, and the mechanistic basis — broad-spectrum β-lactam PBP inhibition combined with high urinary drug concentrations — is well-established. However, Cefprozil is not currently marketed in India, and the supporting trials are over 30 years old, predating the current era of widespread ESBL and fluoroquinolone-resistant uropathogens.

**To proceed, the following is needed:**
- **Current local resistance data**: Obtain contemporary antibiogram data for UTI pathogens in India; assess ESBL prevalence and resistance patterns among *E. coli* and *Klebsiella*, which may substantially reduce the drug's clinical utility compared to the 1990s trial data
- **Regulatory pathway**: Initiate CDSCO market authorization application; define the target indication scope (uncomplicated lower UTI only, or broader)
- **Package insert retrieval**: Download and review the full prescribing information for approved warnings, contraindications, and special population guidance (renal dosing adjustments, pregnancy category)
- **MOA data**: Resolve the DrugBank data gap to complete the mechanistic risk assessment
- **Bridging evidence plan**: Consider a locally-relevant PK/PD study or prospective observational study in Indian patients to establish contemporary clinical evidence, particularly given changes in regional pathogen susceptibility profiles since the original registration trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

