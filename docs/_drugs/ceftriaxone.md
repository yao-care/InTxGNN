---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 161
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Ceftriaxone: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections (pneumonia, meningitis, gonorrhea, salmonellosis…"
monitor_inn: "Ceftriaxone"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ceftriaxone: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, meningitis, gonorrhea and salmonellosis.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support it, so it is a model prediction only.
The better-supported predictions are in otitis media (infectious, suppurative and chronic), which are largely extensions of existing antibacterial use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (pneumonia, meningitis, gonorrhea, salmonellosis, bacterial arthritis, among others); no approved indication text is available from the India licences |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, ceftriaxone is a third-generation cephalosporin that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is well established.

**For the top-ranked prediction, the rationale is weak.** Polyclonal hyperviscosity syndrome is a haematologic/immunologic condition driven by elevated immunoglobulins, and an antibacterial would not be expected to address it. The high score (0.994) is a knowledge-graph prediction with no supporting trials or literature. Other top-ranked predictions are similarly unsupported: hyperamylasemia (a laboratory finding), congenital analbuminemia (a genetic albumin synthesis disorder, where ceftriaxone's high albumin binding is only a dosing consideration) and blood group incompatibility (an immune-mediated process).

**The otitis media predictions are biologically plausible.** Ceftriaxone is active against the main otitis media pathogens (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*).

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Infectious otitis media | 99.26% | L3 | Strong plausibility; likely already an established use (single-dose intramuscular ceftriaxone), so label-adjacent rather than true repurposing |
| Suppurative otitis media | 99.02% | L3 | Plausible, but chronic cases often involve *Pseudomonas aeruginosa* and biofilm producers, against which ceftriaxone has limited activity; evidence is largely descriptive or dated |
| Chronic otitis media | 99.01% | L3 | Partially plausible; the literature is mostly susceptibility surveys, and topical therapy is generally preferred |

---

## Clinical Trial Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), no related clinical trials are currently registered.

For the best-supported prediction, infectious otitis media, one trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | Not applicable | Completed | 250 | Tympanostomy tubes versus non-surgical management in children with recurrent acute otitis media; ceftriaxone is not the studied intervention, so it gives disease context only |

---

## Literature Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), no related literature is currently available.

For infectious otitis media (the best-supported prediction), the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | Pediatrics | Single intramuscular dose of ceftriaxone compared with 10 days of oral trimethoprim-sulfamethoxazole for acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical study | Pediatr Infect Dis J | Bacteriologic and clinical efficacy of one-day versus three-day intramuscular ceftriaxone in nonresponsive acute otitis media |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical study | Pediatr Infect Dis J | Bacteriologic efficacy of a three-day intramuscular ceftriaxone regimen in nonresponsive acute otitis media |
| [2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) | 1989 | Clinical efficacy evaluation | Jpn J Antibiot | Once-daily ceftriaxone 1 g versus cefotiam in acute suppurative otitis media and acute exacerbation of chronic suppurative otitis media (efficacy 71% vs 86%) |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus recommendations | Clin Pediatr | Consensus recommendations for the management of acute otitis media |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clin Ther | Review of treatment recommendations for antimicrobial therapy of acute otitis media |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | Int J Pediatr Otorhinolaryngol | Factors associated with ceftriaxone use for acute otitis media in a large U.S. primary care population |
| [39376426](https://pubmed.ncbi.nlm.nih.gov/39376426/) | 2024 | Microbiology study | Indian J Otolaryngol Head Neck Surg | Biofilm-producing organisms and their antibiotic sensitivity in chronic suppurative otitis media |

For hyperamylasemia, three papers were found, but none supports ceftriaxone as a treatment. One 1999 study ([PMID 10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/)) looked at ceftriaxone prophylaxis after endoscopic papillosphincterotomy, which is only an indirect association.

---

## India Market Information

Ceftriaxone is marketed in India with 20 valid single-ingredient registrations, all as injectable vials. The approved indication text is not available in the compiled data. Main authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 54887 | Cefset-TX 1000mg/125mg Injection | Powder for injection (vial) | Not available |
| Registration No. 117657 | Keftragard 250mg/125mg Injection | Injection (vial, 5 ml) | Not available |
| Registration No. 146757 | Micef TZ 1000mg/125mg Injection | Injection (vial) | Not available |
| Registration No. 245340 | Xonejet 500mg Injection | Injection (vial) | Not available |
| Registration No. 57118 | Colticef 250mg Injection | Injection (vial) | Not available |

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** liver disease, gallbladder disease, neonatal jaundice, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and hemolytic anemia.

**Drug Interactions:** 164 interactions were identified. The main ones are:
- **Major:** calcium chloride, calcium glucoheptonate, calcium gluconate
- **Moderate:** kanamycin, neomycin, streptomycin, picosulfuric acid

Many other listed interactions have an unknown severity level.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (polyclonal hyperviscosity syndrome) has no mechanistic link and no trials or literature, so it rests on model output alone (L5). The otitis media predictions are better supported (L3) but largely reflect existing antibacterial use rather than new repurposing, and the only registered trial does not test ceftriaxone. The compiled data also lack package insert safety information, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-registered products (approved indication text is also missing)
- Detailed mechanism of action data
- If otitis media is pursued, confirmation of whether it is already a labelled use, plus current comparative efficacy data, particularly for chronic disease where *Pseudomonas* and biofilms limit activity
- For the other top-ranked predictions, a plausible mechanistic hypothesis before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

