---
layout: default
title: Rifabutin
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Rifabutin: From Mycobacterial Infection to HIV-Associated Opportunistic Infection

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic that acts against mycobacteria. It is marketed in India as Ributin Capsule, but the data compiled for this report contain no approved indication text.
The TxGNN model predicts it may be effective for **HIV infectious disease**, with **33 registered clinical trials** and **20 publications** linked to this direction.
Rifabutin has no activity against HIV itself. The evidence supports its use against **HIV-associated opportunistic infections** (Mycobacterium avium complex and tuberculosis) and as a rifamycin that is easier to combine with antiretroviral therapy than rifampicin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the India licence record) |
| Predicted New Indication | HIV infectious disease (best interpreted as HIV-associated opportunistic infection) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs, in MAC disease among HIV patients) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Rifabutin inhibits bacterial DNA-dependent RNA polymerase (the rpoB target). It does not act on HIV. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from the repurposing analysis.

The link to HIV is clinical rather than antiviral. People with advanced HIV are prone to Mycobacterium avium complex (MAC) disease and tuberculosis, and rifabutin has been studied for both treatment and prevention. It induces the liver enzyme CYP3A4 less strongly than rifampicin, which makes it a practical choice for patients on antiretroviral therapy. Substantial interactions with protease inhibitors, dolutegravir and long-acting cabotegravir/rilpivirine still require dose management.

The high TxGNN score therefore reflects a real clinical association, but the indication should be described as "HIV-associated opportunistic infection", not "HIV infection".

---

## Clinical Trial Evidence

The compiled data list 33 trials. The most relevant are shown below. Most are Phase 3 MAC trials, or pharmacokinetic and interaction studies. None tests rifabutin as an antiretroviral.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with placebo or rifabutin (two doses) for MAC bacteremia in AIDS |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Four regimens (clarithromycin, ethambutol, rifabutin or clofazimine) for disseminated MAC in AIDS |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Not labelled | Completed | 200 | Double-blind randomized trial of a rifabutin regimen for MAC bacteremia in AIDS |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Clarithromycin vs rifabutin vs combination to prevent MAC in HIV patients with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone and combined, for preventing disseminated MAC |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Not labelled | Completed | 750 | Rifabutin vs placebo for MAC prevention in AIDS (CD4 ≤200) |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | Completed | 246 | Clarithromycin combined with rifabutin, ethambutol or both for disseminated MAC |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (South Africa) |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Not labelled | Completed | 215 | Intermittent rifabutin-based regimen for HIV-related tuberculosis (failure and relapse rates) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir; treatment-limiting neutropenia seen in earlier work |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Pharmacokinetics and safety in TB/HIV children; earlier study stopped early for severe neutropenia |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Modeling | Clin Infect Dis | Managing interactions between long-acting cabotegravir/rilpivirine and inducers such as rifabutin |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK model | Br J Clin Pharmacol | Rifabutin as a less potent inducer alternative to rifampicin with dolutegravir |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | Practical therapeutic approach to TB/HIV co-infection |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectrum | Tuberculosis associated with HIV infection |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Review | Med Clin North Am | Non-tuberculous mycobacterial infections, with MAC as the most common systemic bacterial infection in AIDS |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Review | Arch Intern Med | Update on rifampin and rifabutin drug interactions |
| [31850816](https://pubmed.ncbi.nlm.nih.gov/31850816/) | 2020 | Review | Ocul Immunol Inflamm | Rifabutin strongly associated with drug-induced uveitis in HIV patients |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | PK review | Clin Pharmacokinet | Rifabutin pharmacokinetics; effective for MAC prophylaxis in HIV patients with low CD4 counts |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185256 | Ributin Capsule (Lupin Ltd) | Strip of 6 capsules (oral) | Not stated in the licence record |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Neutropenia in children**: published cohorts report treatment-limiting neutropenia with rifabutin plus lopinavir/ritonavir.
- **Uveitis**: rifabutin is strongly associated with drug-induced uveitis, particularly in HIV patients.
- **Drug interactions**: 163 interactions were recorded. Among the 20 listed, one is Major (eliglustat), most are Moderate and one is Minor. Moderate examples include doxycycline, clarithromycin, metronidazole, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), vitamin D analogues, morphine, aprepitant, and several antidiabetics (pioglitazone, saxagliptin, linagliptin, chlorpropamide, acetohexamide).
- **Antiretroviral interactions**: rifabutin lowers exposure to several antiretrovirals and its own levels change with protease inhibitors, so dose adjustment is needed (see the interaction studies above).

Package insert warnings and contraindications for the Indian product were not available. Please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 trials support rifabutin in preventing and treating MAC disease in HIV patients, and pharmacokinetic studies support its use alongside antiretroviral therapy. This evidence concerns HIV-associated opportunistic infections, not HIV itself, so the indication must be defined narrowly.

**To proceed, the following is needed:**
- Define the indication as HIV-associated MAC/TB, not "HIV infection"
- Obtain the Indian package insert (warnings, contraindications, approved indications)
- Obtain mechanism-of-action data from DrugBank
- Set up blood count monitoring (neutropenia, thrombocytopenia), uveitis surveillance and a protocol for antiretroviral interaction dosing
- Review current relevance, since the key MAC trials date from the 1990s and modern antiretroviral therapy has reduced MAC incidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

