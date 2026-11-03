---
layout: default
title: Rifabutin
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-03
monitor_inn: "Rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
description: "Rifabutin: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Rifabutin
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

## Rifabutin: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic that works against mycobacteria by blocking bacterial RNA polymerase.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with a score of **0.9988**.
The compiled studies are mostly about mycobacterial infections in people with HIV and drug interactions with antiretrovirals. None tests rifabutin as a treatment for HIV infection itself, so the evidence level is **L5**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. From what is known, rifabutin is a rifamycin that inhibits bacterial DNA-dependent RNA polymerase (rpoB). It has no direct activity against HIV.

The link to HIV is indirect. People with advanced HIV are prone to mycobacterial infections such as Mycobacterium avium complex (MAC) and tuberculosis. Rifabutin is used in that setting, and many of the compiled trials cover MAC prevention and treatment in AIDS patients. Rifabutin is also a weaker CYP3A4 inducer than rifampicin. That makes it a practical rifamycin choice for patients on antiretroviral therapy, although dose adjustments are still needed with protease inhibitors, dolutegravir and long-acting cabotegravir/rilpivirine.

The model's score therefore most likely reflects how often rifabutin appears alongside HIV in the literature, not an effect on the virus. The more accurate description is "HIV-associated opportunistic infection", not "HIV infection" itself. Because none of the cited studies treats HIV infection directly, the evidence level is capped at L5.

---

## Clinical Trial Evidence

The listed trials were run in people with HIV. They study opportunistic mycobacterial infections or drug interactions, not HIV infection itself.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Four regimens for disseminated MAC in AIDS: clarithromycin at two doses plus ethambutol with either rifabutin or clofazimine |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with rifabutin (two doses) or placebo for MAC bacteremia in AIDS |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Not specified | Completed | 200 | Double-blind randomized trial of a rifabutin regimen for MAC bacteremia in AIDS |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Clarithromycin vs rifabutin vs the combination to prevent MAC in HIV patients with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone and combined, for preventing disseminated MAC in HIV |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Not specified | Completed | 750 | Placebo-controlled trial of rifabutin to prevent MAC bacteremia in AIDS with CD4 ≤200 |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | Completed | 246 | Clarithromycin combined with rifabutin, ethambutol or both for disseminated MAC in AIDS |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (South Africa) |
| [NCT00000877](https://clinicaltrials.gov/study/NCT00000877) | Phase 1 | Completed | 31 | Steady-state interaction between indinavir and rifabutin given together or staggered |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin pharmacokinetics and safety in TB/HIV-coinfected children on lopinavir/ritonavir-based ART; an earlier pediatric study was stopped for severe neutropenia |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir; neutropenia is a concern |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK model | Br J Clin Pharmacol | Models how rifabutin affects dolutegravir exposure, as a less potent inducer than rifampicin |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Modeling study | Clin Infect Dis | Modeled management of interactions between long-acting cabotegravir/rilpivirine and inducers such as rifabutin |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectrum | Overview of tuberculosis associated with HIV infection |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | Practical approach to TB/HIV co-infection treatment, including rifamycin and antiretroviral interactions |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Review | Med Clin North Am | Nontuberculous mycobacterial infections, with MAC as the most common systemic bacterial infection in AIDS |
| [31850816](https://pubmed.ncbi.nlm.nih.gov/31850816/) | 2020 | Review | Ocul Immunol Inflamm | Rifabutin is strongly associated with drug-induced uveitis in HIV patients |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Review | Arch Intern Med | Update on rifampin and rifabutin drug interactions, including with HIV protease inhibitors |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | PK article | Clin Pharmacokinet | Pharmacokinetics of rifabutin and its value for MAC prophylaxis in HIV-positive patients with low CD4 counts |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185256 | Ributin Capsule (Lupin Ltd) | Strip of 6 capsules (oral) | Not stated in the licence record |

India market status: Marketed (1 valid single-ingredient licence).

---

## Safety Considerations

- **Drug Interactions**: The compiled data list 163 recorded interactions.
  - Major: eliglustat.
  - Moderate, among others: clarithromycin, doxycycline, metronidazole, dexamethasone, hydrocortisone, betamethasone, triamcinolone, morphine, aprepitant, pioglitazone, saxagliptin, linagliptin and calcitriol.
  - Minor: dolasetron.
- **Antiretroviral interactions**: The trials and literature above show that rifabutin levels and antiretroviral exposure can both change when the drugs are combined. Examples are protease inhibitors, nevirapine, efavirenz, dolutegravir, maraviroc and cabotegravir. Dose management is needed.
- **Haematological and ocular effects**: The cited studies report treatment-limiting neutropenia in children given rifabutin with lopinavir/ritonavir, and uveitis, especially when combined with interacting drugs.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The cited studies address mycobacterial infections in people with HIV and antiretroviral drug interactions, not treatment of HIV infection. Rifabutin has no antiretroviral activity. The high model score probably reflects how often the drug and HIV appear together in the literature. No cited study directly supports the predicted indication, so the evidence level is L5.

**To proceed, the following is needed:**
- A clear redefinition of the target indication, such as prevention or treatment of HIV-associated opportunistic mycobacterial infection, with direct evidence for that use
- Label warnings and contraindications from the Indian package insert
- Detailed mechanism-of-action data
- A drug-interaction management plan for patients on antiretroviral therapy, including monitoring for neutropenia and uveitis

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

