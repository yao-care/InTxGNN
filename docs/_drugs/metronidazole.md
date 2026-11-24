---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

## Metronidazole: From Anaerobic Bacterial and Protozoal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis, and rosacea.
The TxGNN model predicts it may be effective for **pneumocystosis** (score 0.9999), but there are **0 clinical trials** and only **general reviews and case reports** to support this, and the literature does not show any metronidazole activity against Pneumocystis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis, rosacea, bacterial vaginosis, vulvovaginitis, intracranial abscess (the India label indication text is not available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metronidazole: "Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical." ([DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255), label version 2026-11-02; accessed 2026-11-19.) Based on known information, metronidazole is a nitroimidazole antimicrobial. It is active against anaerobic bacteria and protozoa, because its nitro group is reduced in oxygen-poor organisms.

Pneumocystis jirovecii is a fungus-like organism with no established nitroimidazole-sensitive pathway. The data compiled for this report do not support a mechanistic link. The very high TxGNN score most likely reflects network proximity to antiparasitic and anti-infective drugs, not a real pharmacological relationship.

The retrieved literature consists of general antiparasitic reviews and HIV opportunistic-infection case reports. In those reports metronidazole was given for a different infection, such as amoebiasis, in patients who also had Pneumocystis pneumonia. None shows that metronidazole treats pneumocystosis. Standard therapy is trimethoprim-sulfamethoxazole.

Other predictions with stronger indirect support are listed in the conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Overview of antiparasitic agents, including resistance and toxicity issues |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole is listed for amoebiasis and trichomoniasis; trimethoprim-sulfamethoxazole is listed for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Treatment of infectious complications of AIDS, including Pneumocystis pneumonia |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Pneumocystis and cytomegalovirus pneumonia in a patient previously treated with metronidazole for diarrhoea |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; metronidazole used for amoebic dysentery, with Pneumocystis pneumonia as a separate problem |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Colon perforation with peritonitis in an AIDS patient with CMV and amoebic colitis |

None of these publications reports metronidazole efficacy against Pneumocystis.

## India Market Information

Metronidazole has 20 valid registrations in India. The approved indication text is not available for the registrations listed.

<!-- review:begin in-lic-20261124-metronidazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Metronidazole has 20 valid registrations in India, all single-ingredient products." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-metronidazole-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 7617 | Ashmet 500mg Infusion | Bottle of 100 ml Infusion | Valid |
| 12276 | Aldezol 200mg Tablet | Strip of 10 tablets | Valid |
| 12568 | Anflox M Suspension | Bottle of 30 ml Suspension | Valid |
| 26834 | Balgyl 400mg Tablet | Strip of 10 tablets | Valid |
| 43345 | Combizol F Syrup | Bottle of 30 ml Syrup | Valid |
| 71273 | Denogyl N Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 84136 | Flagyl 200 Tablet | Strip of 15 tablets | Valid |
| 94564 | Gramogyl Suspension | Bottle of 60 ml Suspension | Valid |
| 96827 | Glomet 400mg Tablet | Strip of 10 tablets | Valid |
| 118125 | Klassak 100 mg/100 mg Suspension | Bottle of 30 ml Suspension | Valid |
| 123017 | Largyl N 100 mg/100 mg Suspension | Bottle of 60 ml Suspension | Valid |
| 125096 | Loc Syrup | Bottle of 30 ml Syrup | Valid |
| 135526 | Metron 100mg Suspension | Bottle of 30 ml Suspension | Valid |
| 140225 | Mebgyl 400mg Tablet | Strip of 10 tablets | Valid |
| 149566 | Metrokos 500mg Infusion | Bottle of 100 ml Infusion | Valid |
| 154033 | Normetrogyl 400mg/400mg Syrup | Bottle of 30 ml Syrup | Valid |
| 158456 | Normec M Syrup | Bottle of 30 ml Syrup | Valid |
| 203188 | Septigard Ointment | Tube of 10 gm Ointment | Valid |
| 229494 | Tosgyl Suspension | Bottle of 30 ml Suspension | Valid |
| 251435 | Zoacide 500mg Infusion | Bottle of 100 ml Infusion | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include oral tablets, syrups and suspensions, intravenous infusion, and topical ointment.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure and liver disease, epilepsy, kidney disease, haematological disease, neutropenia, agranulocytosis, leukopenia, blood coagulation disease, peripheral neuropathy and other peripheral nervous system disease, brain disease, optic nerve disease, diabetes mellitus, diabetic ketoacidosis, congestive heart failure, gout, gallbladder disease, substance abuse/dependence, and others.
- **Drug Interactions**: 620 interactions were recorded. The most important is **ethanol (Major)**. Moderate interactions include paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, amiodarone, celecoxib, butalbital, amobarbital, and loperamide.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model support (L5). There are no clinical trials, no mechanistic basis, and the retrieved literature does not show metronidazole activity against Pneumocystis. Standard therapy is already effective. The high score likely reflects network proximity to anti-infective drugs.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of metronidazole activity against Pneumocystis (none currently exists)
- Detailed mechanism of action data
- India package insert warnings and contraindications
- A safety plan for HIV or immunocompromised patients, including the ethanol interaction

**Other predictions to consider:**
Several lower-ranked predictions have more plausible indirect support and are rated "Research Question". These are not recommendations to proceed:
- **Cap polyposis**: case reports of remission after metronidazole-containing regimens; the mechanism may be antibiotic, anti-inflammatory, or both.
- **Ulceration of vulva**: used in vulvar Crohn's disease and genital amoebiasis, with indirect evidence from case reports and a 22-patient series.
- **Ulcerative proctosigmoiditis**: IBD reviews and a pouchitis cohort provide indirect support, and the evidence is weaker for ulcerative colitis than for Crohn's disease.
- **Myiasis**: metronidazole is used for odour control and as adjunct antibiotic coverage in infested wounds. Ivermectin and mechanical removal are the primary treatments.

The other predictions (punctate epithelial keratoconjunctivitis, nocardiosis, postmenopausal atrophic vaginitis, cryptococcal meningitis, papillary conjunctivitis) have no supporting evidence, and are rated Hold.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

