---
layout: default
title: Ticarcillin
parent: Model Prediction Only (L5)
nav_order: 836
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Ticarcillin: predicted new indication Lymph node palisaded myofibroblastoma (evidence level L5). Approved use: Bacterial infections (urinary tract infection, bacterial pneumonia…"
monitor_inn: "Ticarcillin"
predicted_indications: ["lymph node palisaded myofibroblastoma", "abdominal cystic lymphangioma", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "sacrum chordoma", "disease of retroperitoneum", "urethral disease", "disease of uterine broad ligament", "disease of peritoneum", "pelvic varices"]
---

# Ticarcillin
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

## Ticarcillin: From Bacterial Infections to Lymph Node Palisaded Myofibroblastoma
{: .text-alpha }

## One-Sentence Summary

Ticarcillin is a beta-lactam (penicillin-class) antibiotic, originally used to treat bacterial infections such as urinary tract infection, bacterial pneumonia, and pelvic inflammatory disease.
The TxGNN model's top-ranked prediction is **lymph node palisaded myofibroblastoma**, which has no supporting evidence. The best-supported candidate is **disease of peritoneum** (rank 9), with **0 clinical trials** and **20 publications**, mostly older, small, or non-randomized studies, many on the ticarcillin/clavulanate combination.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, bacterial pneumonia, staphylococcal infection, pelvic inflammatory disease, etc.) |
| Predicted New Indication | Lymph node palisaded myofibroblastoma (rank 1); disease of peritoneum (rank 9) is the only candidate with literature support |
| TxGNN Prediction Score | 0.9982 (rank 1); 0.9981 (disease of peritoneum) |
| Evidence Level | L5 (rank 1); L3 (disease of peritoneum) |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Registrations | 15 (valid: 15) |
| Recommended Decision | Hold (rank 1); Hold overall, with disease of peritoneum as a research question |

The India approved-indication text was not available in the data compiled for this report, so the original indication above is not drawn from an India-specific approved-indication text.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ticarcillin is a beta-lactam antibacterial that acts on bacterial cell wall synthesis. Its efficacy in bacterial infections is established.

**Rank 1 (lymph node palisaded myofibroblastoma):** This is a benign mesenchymal neoplasm, and no mechanistic link to an antibacterial was identified. The high score is a computational prediction only, with no trial or literature support.

**Disease of peritoneum (rank 9):** This is the only prediction with some plausibility. Ticarcillin, usually combined with clavulanate, has broad Gram-negative and anaerobic coverage relevant to polymicrobial peritonitis and intra-abdominal sepsis. Several clinical reports describe the combination in intra-abdominal infection. However, this is an extension of the existing antibacterial class use rather than a novel mechanism. The evidence is mostly for the combination product rather than ticarcillin alone, and the combination has been largely superseded by newer agents.

**Other predictions:** Most of the remaining top-10 candidates (ectopic pregnancy, cystic lymphangioma, celiac trunk compression syndrome, sacrum chordoma, pelvic varices) are non-infectious conditions with no plausible antibacterial mechanism. Urethral disease and disease of uterine broad ligament are conceptually adjacent to existing infectious indications but are nonspecific categories without direct evidence. Urethral disease largely overlaps with the existing urinary tract infection indication rather than being true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table below covers the best-supported candidate, disease of peritoneum. The other nine predicted indications have no literature. Studies are ordered by clinical relevance, and study types follow the classification in the compiled data.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2691475](https://pubmed.ncbi.nlm.nih.gov/2691475/) | 1989 | Prospective clinical study | J Antimicrob Chemother | 50 consecutive patients with secondary peritonitis received ticarcillin/clavulanate 5.2 g three times daily as initial therapy |
| [2024225](https://pubmed.ncbi.nlm.nih.gov/2024225/) | 1991 | Clinical study | Surg Gynecol Obstet | Ticarcillin/clavulanate as an alternative to aminoglycoside-containing regimens for intra-abdominal sepsis in the elderly, given the nephrotoxicity risk of aminoglycosides |
| [3302345](https://pubmed.ncbi.nlm.nih.gov/3302345/) | 1987 | Clinical study | Jpn J Antibiot | Clavulanic acid/ticarcillin in 76 cases of intraperitoneal and biliary tract infections, 10-day drip infusion |
| [3499526](https://pubmed.ncbi.nlm.nih.gov/3499526/) | 1987 | Clinical study | Jpn J Antibiot | Clavulanic acid/ticarcillin in pelvioperitonitis (14 patients) and Douglas' abscess (4 patients) |
| [10768063](https://pubmed.ncbi.nlm.nih.gov/10768063/) | 2000 | Clinical study | Antibiot Khimioter | Ticarcillin/clavulanate in 19 patients with peritonitis and abdominal sepsis; clinical and bacteriological effects in 84.2% and 87.5% of cases |
| [367159](https://pubmed.ncbi.nlm.nih.gov/367159/) | 1978 | Clinical and laboratory study | Am J Med Sci | Eleven patients with serious anaerobic infections treated with carbenicillin or ticarcillin were all cured |
| [9451930](https://pubmed.ncbi.nlm.nih.gov/9451930/) | 1998 | Review | World J Surg | Antibiotic therapy for abdominal infection, with coverage of E. coli and Bacteroides species as the key principle |
| [1734854](https://pubmed.ncbi.nlm.nih.gov/1734854/) | 1992 | Guideline | Arch Surg | Surgical Infection Society guidelines for anti-infective selection in intra-abdominal infection |
| [3112102](https://pubmed.ncbi.nlm.nih.gov/3112102/) | 1987 | Animal study | J Antimicrob Chemother | Pseudomonas peritonitis in neutropenic rats treated with amikacin, ceftazidime and ticarcillin, alone and in combination |
| [3536827](https://pubmed.ncbi.nlm.nih.gov/3536827/) | 1986 | In vitro study | J Antibiot | Ticarcillin/clavulanic acid was active against ticarcillin-resistant S. aureus, E. coli and K. pneumoniae |

None of these are randomized controlled trials. Some are indirect (for example, a review on temocillin, a different drug, and observational data on dialysis patients).

## India Market Information

Fifteen valid single-ingredient registrations were found. Approved indication text was not available for any of them. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228363 | Ticwise 3000mg/100mg Injection | Vial of 1 injection | Not available |
| 216070 | Ticarnic 3.1 Injection | Vial of 1 injection | Not available |
| 224103 | Ticar C 3000mg/100mg Injection | Vial of 1 injection | Not available |
| 217640 | Timentin 3.1 Injection (GlaxoSmithKline) | Vial of 1 injection | Not available |
| 222573 | Timcyn 3000 mg/100 mg Injection | Vial of 1 injection | Not available |

All products are injectables.

## Safety Considerations

- **Contraindication-related conditions (knowledge graph):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome. These come from drug-disease relationships in the knowledge graph, not from package insert text.
- **Drug Interactions:** 23 interactions were recorded. Most are Moderate:
  - Tetracyclines: doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline
  - Aminoglycosides: kanamycin, streptomycin, amikacin (including liposomal), gentamicin
  - Anticoagulants: warfarin, dicoumarol (Moderate); heparin (Minor)
  - Others (Moderate): chloramphenicol, picosulfuric acid, ethinylestradiol, iodide I-123, iodide I-131
  - Minor: clarithromycin, erythromycin
- **Renal function:** A pharmacokinetic study (PMID 1107435) showed ticarcillin half-life rising from about 71 minutes with normal renal function to about 14.8 hours when creatinine clearance is below 10 mL/min, so dose adjustment is relevant in renal impairment.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (lymph node palisaded myofibroblastoma) has no mechanistic link and no trial or literature evidence, so it is a computational artifact. Disease of peritoneum has L3-level literature, but it consists of older, small, mostly non-randomized studies on the ticarcillin/clavulanate combination, and it largely represents existing antibacterial use rather than genuine repurposing. It is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-registered products (currently a blocking gap for safety screening)
- Approved indication text for the India registrations
- Detailed mechanism of action data (MOA)
- For disease of peritoneum: a comparison against current standard intra-abdominal infection regimens and evidence specific to ticarcillin rather than the combination product
- Route compatibility and similarity-to-original assessment for any candidate that advances
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

