---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Colistin: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Escherichia coli infection, otitis externa, external ear disease"
monitor_inn: "colistin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
---

# Colistin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Colistin: From Escherichia coli Infection to Postinfectious Vasculitis

## One-Sentence Summary

Colistin is a polymyxin antibiotic, originally used to treat Gram-negative infections such as Escherichia coli infection and otitis externa.
The TxGNN model's top-ranked prediction is **postinfectious vasculitis**, but **no clinical trials and no publications** support it. Among lower-ranked predictions, **sinusitis** and **chronic rhinosinusitis** have indirect literature (12 and 3 publications respectively, mostly reviews, preclinical work, and a case report) and are the most plausible research directions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Escherichia coli infection, otitis externa, external ear disease (from the knowledge graph; no approved indication text is available in the India license records) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, colistin is a polymyxin antibiotic that disrupts the outer membrane of Gram-negative bacteria. Its efficacy against Gram-negative infections is established, but it is mainly used as a last-resort agent against multidrug-resistant organisms.

For the top prediction, **postinfectious vasculitis**, no mechanistic rationale is evident. This condition is immune-mediated, so an antibacterial agent would not be expected to treat it. The high TxGNN score (99.91%) is a graph-based prediction without supporting data. Colistin's nephrotoxicity and neurotoxicity are additional concerns. The other top-ranked predictions have similar problems:

- **Post-bacterial disorder and post-infectious syndrome** are vague umbrella categories. The links likely reflect knowledge-graph connections to bacterial infection rather than a defined pathophysiology.
- **Chagas cardiomyopathy** is caused by a protozoan (*Trypanosoma cruzi*), and colistin has no known relevant antiprotozoal activity.
- **Infection-related hemolytic uremic syndrome** is typically toxin-mediated. Antibiotics are generally avoided because they may increase toxin release, and colistin's nephrotoxicity is a serious concern in acute kidney injury.
- **Infective urethral stricture** is a fibrotic, structural condition, and antibacterial therapy would at most address a concurrent infection.

The more biologically plausible candidates are the sinus conditions. **Sinusitis** and **chronic rhinosinusitis**, particularly in cystic fibrosis or immunocompromised patients, are often colonised by *Pseudomonas aeruginosa* and other multidrug-resistant Gram-negative bacteria and biofilms, which colistin can target. This is also close to the original ear and upper-airway indication (otitis externa). Topical or nebulised delivery is a plausible route. **Paratyphoid fever** has a theoretical in vitro rationale (a Gram-negative pathogen), but colistin is not an established treatment, and agents such as azithromycin, ceftriaxone, and fluoroquinolones are preferred. **Chronic ethmoidal sinusitis** is a subtype of chronic sinusitis, and the rationale is extrapolated from the broader sinusitis indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

## Literature Evidence

No publications support the top-ranked prediction (postinfectious vasculitis). The table below covers the most relevant literature for the best-supported candidates, **sinusitis** and **chronic rhinosinusitis**, plus paratyphoid fever. Most items are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Case report | Int J Hematol | IV colistin successfully treated maxillary sinusitis, orbital cellulitis, and pneumonia caused by multidrug-resistant, metallo-beta-lactamase-producing *P. aeruginosa* in a patient with acute myeloid leukaemia |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | Pharmacokinetic study | J Antimicrob Chemother | Studied systemic absorption of nasally administered tobramycin and colistin (as colistin sulfomethate) in cystic fibrosis patients, using absorption as a surrogate for safety |
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | Reviews therapeutic options for chronic rhinosinusitis in cystic fibrosis, a condition that is often refractory to standard therapy |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | In vitro / preclinical | Int J Antimicrob Agents | Colistin's bactericidal effect on planktonic *P. aeruginosa* is independent of hydroxyl radical formation |
| [33155505](https://pubmed.ncbi.nlm.nih.gov/33155505/) | 2021 | Preclinical (drug delivery) | Acta Otolaryngol | Autologous fibrin sealant co-delivered with antibiotics as a topical antibiotic approach after sinus surgery |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Cohort (indirect) | Int Forum Allergy Rhinol | Sinus surgery improved quality of life, lung infections, and lung function in primary ciliary dyskinesia |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | In vitro / preclinical | Pharmaceutics | Ceragenins plus ivacaftor prevented biofilm formation by rhinosinusitis bacteria (not colistin-specific) |
| [14126225](https://pubmed.ncbi.nlm.nih.gov/14126225/) | 1964 | Clinical observation (historical) | Iryo | General observations on typhoid and paratyphoid fever; no demonstrated colistin efficacy |

## India Market Information

Colistin is marketed in India, with 20 valid single-ingredient registrations. Approved indication text is not recorded for these licenses. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 104503 | Hopstin 1Million IU Injection | Vial of 1 ml injection | Not specified |
| 244243 | Xylomonas 3Million IU Injection | Vial of 1 injection | Not specified |
| 19505 | Acostin 4.5Million IU Injection | Vial of 1 ml injection | Not specified |
| 117887 | Kallistro 2Million IU Powder for Injection | Vial of 1 powder for injection | Not specified |
| 44467 | Colizin Oral Suspension | Bottle of 30 ml oral suspension | Not specified |

Other registered forms include syrups, dry syrups, and suspensions.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Colistin is linked to contraindication or caution signals for kidney disease, pyoureter, herpes simplex infection, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, myasthenia gravis (including adult-onset), neuromuscular junction disease, geniculate herpes zoster, and myringitis bullosa hemorrhagica.
- **Nephrotoxicity and neurotoxicity**: These are known concerns with colistin and are particularly relevant to conditions involving acute kidney injury, such as infection-related hemolytic uremic syndrome.
- **Systemic absorption with nasal use**: Nasal administration in cystic fibrosis patients showed systemic absorption, so safety of topical sinus use must be established.

Please refer to the package insert for full warnings, contraindications, and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (postinfectious vasculitis and related non-specific categories) are graph-based predictions with no clinical or literature support and no plausible mechanism. Sinusitis and chronic rhinosinusitis are the most credible directions, but the evidence is indirect (a case report, a pharmacokinetic study, reviews, and preclinical work), with no trials. They are best treated as research questions rather than candidates ready to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's records (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- For sinusitis and chronic rhinosinusitis: clinical studies of topical or nebulised colistin, with formulation, dosing, and mucosal safety defined
- A systemic exposure and nephrotoxicity or neurotoxicity assessment for any non-systemic route
- Route compatibility assessment, since the marketed forms are injectable and oral, and no topical sinus product is among them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

