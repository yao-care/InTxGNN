---
layout: default
title: Nalidixic Acid
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 4
---

# Nalidixic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Nalidixic Acid: From Urinary Tract Infection to Conjunctivitis

## One-Sentence Summary

Nalidixic acid is a first-generation quinolone antibiotic, historically used for the treatment of uncomplicated urinary tract infections caused by gram-negative bacteria.
The TxGNN model predicts it may be effective for **Conjunctivitis**, with **0 clinical trials** and **6 publications** currently available — though these publications only tangentially reference nalidixic acid in microbiological contexts.
Overall evidence support for this repurposing direction is limited, and the current recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urinary tract infections (first-generation quinolone antibiotic; no India registration data available) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 (preclinical/mechanism-level studies only) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, nalidixic acid is the prototypical first-generation quinolone antibiotic. Its antibacterial activity derives from inhibition of bacterial DNA gyrase (topoisomerase II), thereby blocking DNA replication in susceptible gram-negative organisms. It was among the first quinolones developed and laid the groundwork for modern fluoroquinolones.

The theoretical link to conjunctivitis rests on the quinolone class's established role in ophthalmic infections: later-generation fluoroquinolones such as ofloxacin and moxifloxacin are approved as topical eye drops for bacterial conjunctivitis, covering pathogens including *Haemophilus influenzae* and *Moraxella catarrhalis*. Nalidixic acid, as the ancestor molecule of this class, shares the same core mechanism against gram-negative pathogens.

However, this mechanistic bridge has significant practical limitations. Nalidixic acid's antibacterial spectrum is narrow (primarily gram-negative enteric organisms), offering no coverage for *Streptococcus pneumoniae* — one of the most common bacterial conjunctivitis pathogens. No ophthalmic formulation exists for nalidixic acid, and its tissue penetration into ocular tissues is considered poor. Modern fluoroquinolone eye drops have entirely superseded any theoretical role for nalidixic acid in this indication. The TxGNN prediction likely reflects a class-level signal rather than drug-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 6 retrieved publications do not directly study nalidixic acid for conjunctivitis treatment. Most reference nalidixic acid in passing — as a culture medium component (nalidixic agar), as a resistance marker in antimicrobial surveillance, or as a microbiological characterization tool. None constitute clinical evidence for this repurposing direction.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34151142](https://pubmed.ncbi.nlm.nih.gov/34151142/) | 2021 | Case Report | Access Microbiology | Two cases of *Tsukamurella pulmonis* conjunctivitis in patients with nasolacrimal duct obstruction; nalidixic agar used for bacterial isolation only |
| [15824427](https://pubmed.ncbi.nlm.nih.gov/15824427/) | 2005 | Microbiology Characterization | J Medical Microbiology | Characterization of provisional *Shigella boydii* serovar from diarrhoeal patients; nalidixic acid cited as resistance marker |
| [17446289](https://pubmed.ncbi.nlm.nih.gov/17446289/) | 2007 | Microbiology Characterization | J Medical Microbiology | Novel *Shigella dysenteriae* serovar characterization; nalidixic acid referenced as phenotypic marker |
| [9442487](https://pubmed.ncbi.nlm.nih.gov/9442487/) | 1997 | Molecular Microbiology | Microbial Drug Resistance | Plasmid-mediated drug resistance in epidemic *S. dysenteriae*; nalidixic acid sensitivity used for plasmid characterization |
| [16914657](https://pubmed.ncbi.nlm.nih.gov/16914657/) | 2006 | Surveillance Study | J Medical Microbiology | *Shigella sonnei* antibiotic resistance surveillance; >60% of isolates resistant to nalidixic acid |
| [3206956](https://pubmed.ncbi.nlm.nih.gov/3206956/) | 1988 | Animal/Microbiology Study | Zhurnal Mikrobiologii | *Yersinia* virulence and plasmid characterization; nalidixic acid resistance used as genetic marker |

---

## India Market Information

No marketing authorizations for nalidixic acid are registered in India at the time of data cutoff (2026-04-04).

---

## Safety Considerations

**Drug Interactions (156 interactions total; selected major interactions listed below):**

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Hydrocortisone | **Major** | Corticosteroid interaction — monitor closely |
| Dexamethasone | **Major** | Corticosteroid interaction — monitor closely |
| Betamethasone | **Major** | Corticosteroid interaction — monitor closely |
| Triamcinolone | **Major** | Corticosteroid interaction — monitor closely |
| Bupropion | **Major** | Lowered seizure threshold risk |
| Chlorpropamide | **Major** | Hypoglycaemia risk enhancement |
| Acarbose | Moderate | Glycaemic management interaction |
| Alogliptin | Moderate | Glycaemic management interaction |
| Canagliflozin | Moderate | Glycaemic management interaction |
| Dapagliflozin | Moderate | Glycaemic management interaction |

> Full prescribing warnings and contraindications are not available in the current dataset. Please refer to the package insert for complete safety information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials have evaluated nalidixic acid for conjunctivitis, and none of the 6 retrieved publications provide direct therapeutic evidence — they merely cite nalidixic acid as a microbiological reagent or resistance marker. Additionally, nalidixic acid lacks an ophthalmic formulation, has limited gram-positive coverage (a key gap for conjunctivitis pathogens), and has been clinically obsoleted by modern fluoroquinolone eye drops with proven ophthalmic safety profiles.

**To proceed, the following would be needed:**

- **Mechanism of Action data**: Retrieve full DrugBank MOA entry to formally assess whether any plausible ophthalmic pathway exists
- **Regulatory safety data**: Download and parse the official package insert to identify contraindications and boxed warnings (currently a blocking data gap)
- **Preclinical ocular studies**: At minimum, in vitro susceptibility data against major conjunctivitis pathogens (*S. pneumoniae*, *S. aureus*, *H. influenzae*) using nalidixic acid would be required to establish any biological basis
- **Formulation feasibility**: Assess whether an ophthalmic formulation of nalidixic acid is pharmacokinetically viable — current evidence strongly suggests it is not
- **Comparative positioning**: Given that ofloxacin and ciprofloxacin ophthalmic drops are generic, widely available, and have a superior spectrum, a clinical rationale for nalidixic acid over established alternatives would need to be articulated before any investment in this direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

