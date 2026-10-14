---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Metronidazole: From Anaerobic Bacterial and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis, and rosacea.
The TxGNN model predicts it may be effective for **pneumocystosis** (score 99.99%), but there are **0 clinical trials** and only **general reviews and case reports** to support this, and the literature does not show any metronidazole activity against Pneumocystis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis, rosacea, bacterial vaginosis, vulvovaginitis, intracranial abscess (the India label indication text is not available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metronidazole is a nitroimidazole antimicrobial. It is active against anaerobic bacteria and protozoa, because its nitro group is reduced in oxygen-poor organisms.

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

Metronidazole has 20 valid registrations in India, all single-ingredient products. The approved indication text is not available for the registrations listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 84136 | Flagyl 200 Tablet (Abbott) | Strip of 15 tablets | — |
| Registration No. 94564 | Gramogyl Suspension (Sun Pharmaceutical) | Bottle of 60 ml suspension | — |
| Registration No. 251435 | Zoacide 500mg Infusion (Wockhardt) | Bottle of 100 ml infusion | — |
| Registration No. 203188 | Septigard Ointment (Vanguard Therapeutics) | Tube of 10 gm ointment | — |
| Registration No. 26834 | Balgyl 400mg Tablet (Micro Labs) | Strip of 10 tablets | — |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

