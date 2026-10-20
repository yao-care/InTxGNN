---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal, staphylococcal, pneumonia…"
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibacterial, originally used for infections such as streptococcal and staphylococcal infections, bacterial pneumonia, anthrax, sinusitis, conjunctivitis and pyelonephritis.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but the best-supported candidate in the data compiled for this report is **monoclonal gammopathy**, with **1 published phase 3 randomised trial (TEAMM, reported in two publications)** and about 18 other publications.
That evidence supports infection *prevention* in myeloma patients, not treatment of the gammopathy itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal, pneumonia, anthrax, sinusitis, conjunctivitis, pyelonephritis, etc.) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (TxGNN rank 1); monoclonal gammopathy (rank 7) is the best-evidenced candidate and is the focus of the evidence sections below |
| TxGNN Prediction Score | 99.92% (punctate epithelial keratoconjunctivitis); 99.81% (monoclonal gammopathy) |
| Evidence Level | L5 for the top-ranked prediction; L1 for monoclonal gammopathy (infection prophylaxis in myeloma only); L3 for septicemic plague (preclinical) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (top prediction); Proceed with Guardrails as a research question for infection prophylaxis in myeloma |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, levofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy against a wide range of bacterial infections is established.

**Top-ranked prediction (punctate epithelial keratoconjunctivitis).** Levofloxacin is already used for bacterial conjunctivitis, so ocular surface use is plausible. However, the only paper retrieved describes a microsporidial keratoconjunctivitis outbreak. Microsporidia are fungi-related intracellular parasites that fluoroquinolones do not reliably treat, so the paper gives no support for efficacy. The high score likely reflects network proximity to conjunctivitis indications.

**Monoclonal gammopathy.** The link is indirect. In the TEAMM trial, levofloxacin prevented infections in newly diagnosed symptomatic myeloma through its antibacterial action, not by treating the plasma cell disorder. The studied population was symptomatic myeloma, not MGUS or premalignant gammopathy, so applicability is only partial.

**Septicemic plague.** Levofloxacin is bactericidal against *Yersinia pestis*. Support comes from African green monkey models of pneumonic plague, which underpin FDA approval under the Animal Rule. Data on septicemic plague specifically are not provided, and no human trials were retrieved.

The remaining predictions (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant hematological disease, hematological disease with acquired peripheral neuropathy, congenital hematological disorder) have no supporting evidence and no plausible mechanism. They appear to be computational artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction or for the other predictions in the data compiled for this report.

The most relevant controlled study for monoclonal gammopathy is the TEAMM trial, which appears in the literature table below.

---

## Literature Evidence

**Monoclonal gammopathy (selected from 19 publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (phase 3, double-blind, placebo-controlled) | Lancet Oncol | TEAMM: levofloxacin prophylaxis in newly diagnosed myeloma, assessing infection prevention and antibiotic-resistant organism carriage |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT | Health Technol Assess | Full TEAMM report: prophylactic levofloxacin to prevent infections in symptomatic myeloma, with attention to healthcare-associated infections such as *C. difficile* |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Supportive care in multiple myeloma, including infection management |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transpl Infect Dis | Infectious complications after autologous transplant in myeloma, with or without levofloxacin prophylaxis (developing-country data) |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Cohort | Clin Transplant | Ciprofloxacin vs levofloxacin prophylaxis in autologous transplant for myeloma (297 patients) |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biol Blood Marrow Transplant | Levofloxacin prophylaxis and bloodstream infection/fever rates in neutropenic myeloma patients |
| [25212681](https://pubmed.ncbi.nlm.nih.gov/25212681/) | 2014 | Study | Int J Hematol | Oral levofloxacin prophylaxis to prevent severe infections in myeloma patients on bortezomib regimens |
| [32007199](https://pubmed.ncbi.nlm.nih.gov/32007199/) | 2020 | Commentary | Lancet Oncol | Correspondence on TEAMM (authors' reply: [32007200](https://pubmed.ncbi.nlm.nih.gov/32007200/)) |
| [25591868](https://pubmed.ncbi.nlm.nih.gov/25591868/) | 2016 | Case report | J Oncol Pharm Pract | Acute kidney injury from crystal nephropathy with pomalidomide and levofloxacin |

**Septicemic plague (selected from 16 publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal study (non-human primate) | PLoS Negl Trop Dis | Levofloxacin cured experimental pneumonic plague in African green monkeys |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal study (non-human primate) | Clin Infect Dis | Effect of delaying treatment on ciprofloxacin and levofloxacin efficacy in pneumonic plague |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review/Regulatory | Clin Infect Dis | The monkey model and FDA approval of antimicrobials under the Animal Rule |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | Animal study (in vitro model) | Antimicrob Agents Chemother | Streptomycin vs levofloxacin for plague, with resistance selection and mutant fitness |
| [21574421](https://pubmed.ncbi.nlm.nih.gov/21574421/) | 2010 | Animal study (mouse) | Antibiot Khimioter | Lack of levofloxacin efficacy against nalidixic acid-resistant plague strains |

**Other predictions with literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Microsporidial keratoconjunctivitis outbreak linked to swimming pool water in Taiwan (does not support levofloxacin efficacy) |
| [40350274](https://pubmed.ncbi.nlm.nih.gov/40350274/) | 2025 | Case report | Rinsho Ketsueki | *Campylobacter lari* bacteremia after ABO-mismatched transplantation (indirect, anecdotal) |

---

## India Market Information

Twenty valid single-ingredient registrations are on file, all oral tablets. Approved indication text is not available. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 122062 | Lquin 750 Tablet (Cipla Ltd) | Strip of 5 tablets | Not stated |
| 192687 | R-Levo 250 Tablet (R.B. Remedies Pvt Ltd) | Strip of 10 tablets | Not stated |
| 11175 | Avulox 500mg Tablet (Avunu Life Sciences) | Strip of 10 tablets | Not stated |
| 128899 | Livopen 250mg Tablet (Morepen Laboratories Ltd) | Strip of 10 tablets | Not stated |
| 82302 | Elvox 500mg Tablet (Elder Pharmaceuticals Ltd) | Strip of 5 tablets | Not stated |

---

## Safety Considerations

- **Contraindications / high-risk conditions (from knowledge-graph associations, not label text):** long QT syndrome, torsades de pointes, epilepsy, liver disease, tendinitis and other tendon disorders, diabetes mellitus and diabetic ketoacidosis, peripheral neuropathy, rhabdomyolysis, myasthenia gravis, impaired renal function, *Clostridium difficile* colitis, thrombocytopenia, leukopenia, pancytopenia, anemia, coronary artery disease, and others.
- **Drug Interactions:** 434 interacting drugs are recorded. Major-level examples include **tramadol** and **hydrocortisone**. Moderate-level examples include abiraterone, acarbose, famotidine, formoterol, ketorolac, adenosine, ibuprofen, ethinylestradiol, salbutamol, alfuzosin, alogliptin, metformin, pioglitazone and amifampridine. Minor-level examples include paclitaxel, aldesleukin and altretamine.
- **Context-specific concerns:** fluoroquinolone-associated peripheral neuropathy argues against the prediction for hematological disease with acquired peripheral neuropathy. In myeloma, resistance selection and healthcare-associated infections (e.g. *C. difficile*) are concerns, and one case report links levofloxacin with pomalidomide to crystal nephropathy.

Please also refer to the package insert for formal warnings, as label text was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (punctate epithelial keratoconjunctivitis) and for the other predictions without evidence.
**Proceed with Guardrails** only as a research question for infection prophylaxis in myeloma and for plague.

**Rationale:**
- The top-ranked prediction has L5 evidence, and its only paper describes a pathogen that levofloxacin is not expected to treat.
- The strongest evidence (TEAMM phase 3 RCT, L1) concerns preventing infection in symptomatic myeloma, a related but distinct use from treating monoclonal gammopathy.
- Plague support is preclinical, from animal models (L3).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A critical appraisal of the TEAMM results (infection outcomes, resistance, *C. difficile*) and their applicability to non-myeloma or premalignant gammopathy populations
- Review of the large interaction burden (434 drugs), including QT-prolonging and tramadol or corticosteroid combinations
- For ocular use, clinical or microbiological evidence in non-microsporidial punctate keratoconjunctivitis, and a check of route compatibility (ocular vs. oral formulations; only oral tablets are registered in India)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

