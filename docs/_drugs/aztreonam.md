---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, Pseudomonas aeruginosa infection…"
monitor_inn: "Aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Aztreonam: From Urinary Tract Infection to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic originally used for gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection, peritonitis and *E. coli* infection.
The TxGNN model's top-ranked prediction is **Hyperamylasemia**, but **no clinical trials and no publications** support it, and the link appears to be a graph-based artifact.
The most credible lead among the top 10 predictions is **gonococcal urethritis**, which has **6 publications** (mostly older, non-randomized studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, rhinoscleroma, *E. coli* infection, endometritis (from the knowledge graph; no approved indication text is available from the India licences) |
| Predicted New Indication | Hyperamylasemia (top-ranked); gonococcal urethritis is the best-supported among the top 10 |
| TxGNN Prediction Score | 99.73% (hyperamylasemia) |
| Evidence Level | L5 (hyperamylasemia); L3 for gonococcal urethritis |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (hyperamylasemia); gonococcal urethritis is a research question only |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, aztreonam is a monobactam antibiotic that inhibits bacterial cell wall synthesis by binding penicillin-binding protein 3 (PBP3) in gram-negative aerobes. Its efficacy in gram-negative infections such as urinary tract infection is established.

**For the top-ranked prediction, hyperamylasemia,** no plausible mechanistic link was identified. Hyperamylasemia is a laboratory finding, not an infectious process, and the high score looks like a graph-based artifact. The same is true of polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility and premalignant hematological system disease. None of these is a bacterial infection, and an antibacterial acting on PBP3 has no known effect on them.

**The more plausible predictions are infectious ones:**
- **Gonococcal urethritis:** *Neisseria gonorrhoeae* is a gram-negative diplococcus whose PBP3 aztreonam binds, so activity is plausible. Historical single-dose studies from the 1980s and a 2020 single-arm trial support this.
- **Epiglottitis:** It is often caused by *Haemophilus influenzae* type b, a gram-negative organism within aztreonam's spectrum. The evidence is only indirect.
- **Xanthogranulomatous pyelonephritis:** It is often associated with *E. coli*, *Proteus* or *Pseudomonas*, which aztreonam covers, and aztreonam is already used for urinary tract infections. Management is mainly surgical, so extrapolation is plausible but unsupported by direct data.
- **Ureaplasma urethritis:** The mechanism contradicts the prediction. Ureaplasma has no cell wall, so beta-lactams including aztreonam are intrinsically ineffective.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the predicted indications.

---

## Literature Evidence

No literature is available for the top-ranked prediction, hyperamylasemia. The table below lists the most relevant publications for the best-supported prediction, **gonococcal urethritis**.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Evaluated single-dose intramuscular aztreonam 2 g in men with *N. gonorrhoeae*, motivated by the threat of ceftriaxone-resistant gonorrhea |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical effectiveness study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM for uncomplicated gonorrhea: no failures with either drug |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Single-dose clinical study | Genitourin Med | Single 1 g IM dose cleared infection at all sites in 61 men and 26 women, except one pharyngeal infection; effective against penicillin-sensitive and resistant strains |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic and therapeutic study | Hinyokika Kiyo | Single-dose aztreonam therapy for gonorrheal infections, with an accompanying epidemiologic analysis |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro / clinical effectiveness | J Infect Dis | Aztreonam was effective against penicillinase-producing gonococci |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance surveillance | J Infect Chemother | Reported emergence of cephem- and aztreonam-high-resistant gonococci that do not produce beta-lactamase |

Indirect evidence for other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Case series (epiglottitis) | Am J Dis Child | Open trial of aztreonam in 59 children with serious gram-negative infections; epiglottitis was one of several diagnoses, so the evidence is not specific |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Clinical study (monoclonal gammopathy) | Jpn J Antibiot | Among 90 evaluable patients with infections complicating hematologic disorders, the efficacy rate was 51.1%. This shows infection control in immunocompromised patients, not treatment of the gammopathy itself |

One further paper retrieved for blood group incompatibility (PMID 34956120) is a microbial genomics study unrelated to that indication, so it is not counted as evidence.

---

## India Market Information

Aztreonam is marketed in India with 20 valid single-ingredient registrations (no combination products, none cancelled). All are injectable vials. Approved indication text is not available for these licences. The first five are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12233 | Azinox 500mg Injection (Kritikos Care) | Vial of 1 injection | Not available |
| 7051 | Azotum 2gm Injection (Venus Remedies Ltd) | Vial of 1 injection | Not available |
| 1376 | Azom 1gm Injection (United Biotech Pvt Ltd) | Vial of 1 injection | Not available |
| 36994 | Cromobact Injection (Fusion Healthcare Pvt Ltd) | Vial of 1 injection | Not available |
| 7396 | Aztrone 2gm Injection (Neon Laboratories Ltd) | Vial of 1 injection | Not available |

---

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (not taken from label text): kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and bronchial disease.
- **Drug interactions:** 27 interactions were identified. Those rated **Moderate** are:
  - Picosulfuric acid
  - Dicoumarol
  - Warfarin

  The others are of unknown severity and include vancomycin, amikacin, amphotericin B, acyclovir, tacrolimus, heparin, acetylsalicylic acid, fluconazole, metronidazole, morphine and several proton pump inhibitors (omeprazole, pantoprazole, lansoprazole). Anticoagulant use warrants particular attention.

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia) have no clinical evidence and no plausible mechanism, and are likely knowledge-graph artifacts. The only prediction with a credible mechanism and some clinical data is gonococcal urethritis (evidence level L3). That evidence consists of non-randomized studies, one report of high-level aztreonam-resistant gonococci, and a current standard of care based on ceftriaxone. It is therefore a research question, possibly a niche option for resistant or allergic cases, rather than a candidate to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences (currently a blocking data gap for safety screening)
- Detailed mechanism of action data (from DrugBank)
- For gonococcal urethritis: current resistance and susceptibility data, plus results and follow-up of the 2020 single-arm trial, including pharyngeal efficacy
- Approved indication text for the India licences, to confirm the original indications
- A dosing and route-compatibility assessment for any pursued indication
- A review of the interaction profile, especially with warfarin and dicoumarol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

