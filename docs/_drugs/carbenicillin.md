---
layout: default
title: Carbenicillin
parent: Moderate Evidence (L3-L4)
nav_order: 143
evidence_level: L3
indication_count: 7
last_modified_at: 2026-10-14
description: "Carbenicillin: predicted new indication Gonococcal urethritis (evidence level L3). Approved use: Urinary tract infection"
---

# Carbenicillin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Carbenicillin: From Urinary Tract Infection to Gonococcal Urethritis

## One-Sentence Summary

Carbenicillin is an extended-spectrum penicillin, originally used to treat urinary tract infection and prostatitis.
The TxGNN model predicts it may be effective for **gonococcal urethritis** (the most evidence-supported of its predictions), but there are **no registered clinical trials** and only **4 publications**, mostly from the 1970s, behind this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection; prostatitis (the approved indication text on the Indian licences is blank, so this comes from the knowledge graph) |
| Predicted New Indication | Gonococcal urethritis (the top-ranked prediction, Ureaplasma urethritis, was set aside because it is not mechanistically supported; see below) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (treat as a research question only) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, carbenicillin is a beta-lactam penicillin. It inhibits penicillin-binding proteins and blocks bacterial cell wall synthesis. It is active against many Gram-negative organisms, including *Pseudomonas* and *Proteus*, which explains its use in urinary tract infections.

Urinary tract infection and gonococcal urethritis are both infections of the lower urogenital tract, and *Neisseria gonorrhoeae* is a cell-wall-containing bacterium that penicillins can plausibly target. Two 1970s clinical reports (carbenicillin and carbenicillin indanyl sodium in gonorrhoea) suggest historical activity.

This link has serious limits today. Penicillin resistance in *N. gonorrhoeae* is widespread, and current guidelines use ceftriaxone. The old reports were small and uncontrolled and have not been checked against modern standards.

**Other predictions reviewed (all rated Hold):**
- **Ureaplasma urethritis (rank 1):** *Ureaplasma* has no cell wall, so beta-lactams are expected to be ineffective. The high score is probably a network artifact.
- **Urogenital tuberculosis:** *M. tuberculosis* is intrinsically resistant to most penicillins, so the prediction is not mechanistically supported.
- **Uterine inflammatory disease, xanthogranulomatous pyelonephritis, epiglottitis:** Coverage is plausible in principle, but there is no supporting evidence.
- **Laryngitis:** Only indirect literature exists (topical antibiotics for post-laryngectomy wound infection; necrotizing otitis externa). Laryngitis is mostly viral.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4638000](https://pubmed.ncbi.nlm.nih.gov/4638000/) | 1972 | Clinical study | Health Services Reports | Carbenicillin in the treatment of gonorrhoea in males (no abstract available) |
| [4841541](https://pubmed.ncbi.nlm.nih.gov/4841541/) | 1974 | Clinical study | Singapore Medical Journal | Carbenicillin indanyl sodium in the treatment of gonorrhoea (no abstract available) |
| [6224627](https://pubmed.ncbi.nlm.nih.gov/6224627/) | 1982 | Review | Clinical Pharmacy | Comparison of mezlocillin and piperacillin; indirect relevance only |
| [12002087](https://pubmed.ncbi.nlm.nih.gov/12002087/) | 2001 | Susceptibility survey | East African Medical Journal | Antimicrobial susceptibility of *N. gonorrhoeae* in Gondar, Ethiopia |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 50906 | CARBELIN 5GM INJECTION (Lyka Labs) | Vial of 1 injection | Not stated |
| 42088 | CARBELIN 1GM INJECTION (Lyka Labs) | Vial of 1 injection | Not stated |

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions:** 18 interactions were found.
  - **Major:** methotrexate.
  - **Moderate:** warfarin, dicoumarol, tetracyclines (doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline), chloramphenicol, ethinylestradiol, mycophenolic acid, pemetrexed, balsalazide, picosulfuric acid, iodide I-131 and I-123.
  - **Minor:** clarithromycin, erythromycin.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gonococcal urethritis has the best support of the predicted indications, but that support is two small 1970s reports with no registered trials. Widespread penicillin resistance and the current use of ceftriaxone make a modern role unlikely. The other predictions have no evidence, and two (Ureaplasma urethritis and urogenital tuberculosis) contradict known mechanisms.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Current *N. gonorrhoeae* resistance data for penicillins, including carbenicillin, in India
- Full-text review of the two 1970s gonorrhoea studies to judge cure rates and study quality
- A comparison with current standard-of-care regimens before any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

