---
layout: default
title: Zidovudine
parent: Model Prediction Only (L5)
nav_order: 903
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Zidovudine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Zidovudine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Zidovudine: From HIV Infection / AIDS to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Zidovudine is a nucleoside reverse transcriptase inhibitor (NRTI) originally used to treat HIV infection and AIDS.
The TxGNN model's top-ranked prediction is **simian immunodeficiency virus (SIV) infection**, an animal model of HIV, supported by **0 clinical trials** and **about 20 publications** (almost all non-human primate studies).
Among the other predictions, **congenital HIV** and **AIDS related complex** have Phase 3 trial support, but both fall within the drug's established HIV use rather than representing new repurposing opportunities.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the registration records compiled for this report contain no approved-indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical studies only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, zidovudine is a thymidine analogue NRTI. It is phosphorylated in cells and blocks reverse transcription, the step lentiviruses need to replicate. Its efficacy in HIV/AIDS is well established.

SIV is a lentivirus closely related to HIV and uses the same reverse transcriptase target, so the mechanistic link is strong. However, SIV infection is an animal model of HIV rather than a distinct human disease. The prediction is essentially a restatement of the approved HIV use, not a new human indication.

The other predictions follow a similar pattern:
- **Feline acquired immunodeficiency syndrome (FIV/FeLV):** a veterinary indication, mechanistically plausible but not relevant to human repurposing.
- **AIDS related complex** and **congenital HIV:** historical or perinatal stages of HIV disease, already covered by the drug's established use.
- **A rare neurodevelopmental disorder** and **obsolete familial combined hyperlipidemia:** high model scores but no trials, no literature, and no identifiable mechanistic rationale. The second is likely an ontology artifact, and NRTIs are associated with lipid disturbances, which argues against benefit.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (SIV infection). The most relevant human trials were found for the related HIV-stage predictions:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001011](https://clinicaltrials.gov/study/NCT00001011) | Phase 3 | Completed | 538 | Safety and efficacy of zidovudine in early AIDS related complex |
| [NCT00001104](https://clinicaltrials.gov/study/NCT00001104) | Phase 3 | Completed | 538 | Placebo-controlled zidovudine in HIV-infected hemophilic patients |
| [NCT00000960](https://clinicaltrials.gov/study/NCT00000960) | Phase 3 | Completed | 1496 | Oral zidovudine in pregnant HIV-infected women and their infants to reduce mother-to-child transmission |
| [NCT00000736](https://clinicaltrials.gov/study/NCT00000736) | Phase 3 | Completed | 3200 | Zidovudine in asymptomatic HIV-infected individuals; delay of AIDS/ARC onset |
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Strategies for antiretroviral therapy in infants infected at birth |
| [NCT00001022](https://clinicaltrials.gov/study/NCT00001022) | Phase 3 | Completed | 1200 | AZT alone vs AZT + didanosine vs AZT + zalcitabine |
| [NCT00002124](https://clinicaltrials.gov/study/NCT00002124) | Phase 3 | Completed | 1250 | Delavirdine plus zidovudine vs zidovudine alone |
| [NCT00002436](https://clinicaltrials.gov/study/NCT00002436) | Phase 3 | Completed | 325 | Lamivudine or zalcitabine added to AZT in AZT-experienced patients |
| [NCT00002238](https://clinicaltrials.gov/study/NCT00002238) | Phase 3 | Completed | Not reported | Interferon beta in AIDS/advanced ARC patients on reduced-dose AZT |
| [NCT00000803](https://clinicaltrials.gov/study/NCT00000803) | Phase 2 | Completed | 471 | Delavirdine with AZT and/or ddI vs AZT/ddI |

## Literature Evidence

**SIV infection (top prediction):** all studies are non-human primate or in vitro work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Preclinical (macaque) | AIDS | Post-exposure prophylaxis with zidovudine, lamivudine and indinavir after vaginal SIV exposure |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Preclinical (newborn macaque) | Antimicrob Agents Chemother | Immediate oral zidovudine prevented infection or reduced virus load and AIDS onset |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | Preclinical (macaque) | J Infect Dis | Effect of starting zidovudine at different times after SIV inoculation |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Preclinical (rhesus macaque) | J Infect Dis | Zidovudine prolonged survival and lowered CNS viral burden |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | Non-occupational HIV post-exposure prophylaxis; animal studies provide indirect support |

**Related HIV-stage indications (human evidence):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2677429](https://pubmed.ncbi.nlm.nih.gov/2677429/) | 1989 | Clinical cohort | JAMA | Prolonged zidovudine therapy in 229 patients with AIDS and advanced ARC |
| [1777174](https://pubmed.ncbi.nlm.nih.gov/1777174/) | 1991 | Double-blind trial | AIDS | Zidovudine with or without acyclovir in ARC (n=199) |
| [7913986](https://pubmed.ncbi.nlm.nih.gov/7913986/) | 1994 | Guideline | MMWR | U.S. Public Health Service recommendations on zidovudine to reduce perinatal HIV transmission |
| [29912896](https://pubmed.ncbi.nlm.nih.gov/29912896/) | 2018 | Systematic review / network meta-analysis | PLoS One | Comparative safety and effectiveness of perinatal antiretroviral therapies |
| [28537936](https://pubmed.ncbi.nlm.nih.gov/28537936/) | 2017 | Cohort | AIDS | Zidovudine use in pregnancy and congenital malformations; evidence inconsistent |

## India Market Information

Zidovudine is marketed in India with 19 valid single-ingredient registrations (no combination or cancelled registrations). The records compiled for this report do not include approved-indication text. Main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 250241 | Zido H 100mg Capsule | Strip of 10 capsules | Not available |
| 251540 | Zidomax 100mg Capsule | Strip of 10 capsules | Not available |
| 251471 | Zidohope 100mg Tablet | Bottle of 100 tablets | Not available |
| 248526 | Zidine 300mg Tablet | Bottle of 60 tablets | Not available |
| 247170 | Zidovir 300mg Tablet | Strip of 10 tablets | Not available |

All products are oral forms (capsules and tablets) from manufacturers including Cipla, Sun Pharma, Alkem, Macleods and Emcure.

## Safety Considerations

**Contraindication-related disease associations (from a drug-disease knowledge graph, not label text):** liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, myopathy and myositis (including dermatomyositis), neutropenia, agranulocytosis, anemia (including macrocytic anemia), hypertriglyceridemia, fatty liver disease and non-alcoholic steatohepatitis, lactic acidosis, obesity, and familial periodic paralysis.

**Drug Interactions:** 235 interactions were recorded. Those listed include:
- **Moderate:** amphotericin B (including lipid formulations), systemic corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), naltrexone, rosuvastatin, simvastatin, orlistat
- **Minor:** cimetidine, clarithromycin
- **Level unknown:** pantoprazole, omeprazole, morphine, metformin

Veterinary studies also report zidovudine toxicity in cats. For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) is supported only by non-human primate studies and is essentially a restatement of the approved HIV use, so it offers no new human repurposing value. The Phase 3 evidence for AIDS related complex and congenital HIV is strong (L1), but those uses are already established. The remaining high-scoring predictions have no trials, no literature and no plausible mechanism.

**To proceed, the following is needed:**
- Mechanism of action data to support mechanistic-link analysis
- Package insert warnings and contraindications for India-marketed products (currently missing, and a blocker for safety screening)
- Approved-indication text for the registered products
- Identification of a genuinely non-HIV indication with human evidence, since the current predictions are within the existing HIV use or are non-human diseases
- For perinatal use, a guardrail review covering congenital malformation risk, neonatal hematologic toxicity, and the current preference for combination regimens over zidovudine alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

