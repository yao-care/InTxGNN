---
layout: default
title: Tinidazole
parent: Model Prediction Only (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tinidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis…"
monitor_inn: "Tinidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "blunt duct adenosis of breast", "apocrine adenosis of breast", "congenital human immunodeficiency virus", "AIDS related complex", "benign mammary dysplasia"]
---

# Tinidazole
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

# Tinidazole: From Giardiasis and Trichomoniasis to Postmenopausal Atrophic Vaginitis

## One-Sentence Summary

Tinidazole is an antimicrobial originally used to treat protozoal and anaerobic infections such as giardiasis, amoebiasis, trichomoniasis and bacterial vaginosis.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **no clinical trials and no publications** currently support this specific prediction.
The result is a model-only prediction that should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis, amoebiasis due to *Entamoeba histolytica*, trichomoniasis |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tinidazole is a 5-nitroimidazole antimicrobial. Its efficacy in vaginal infections such as bacterial vaginosis and trichomoniasis is established, and the model appears to link it to vaginitis in general.

The prediction is probably driven by graph proximity to the approved vaginitis, vulvitis and vulvovaginitis indications rather than by a shared disease mechanism. Atrophic vaginitis after menopause is caused mainly by estrogen deficiency, not infection. An antimicrobial would therefore not be expected to treat the underlying condition. At most it might help with a secondary infection.

Other high-scoring predictions point the same way. The ulceration of vulva, vulvar neoplasm, benign breast conditions (fibrocystic disease, blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) and HIV-related conditions all have weak or no plausible mechanistic rationale. Their scores most likely reflect graph neighbourhood effects.

## Clinical Trial Evidence

Currently no related clinical trials are registered for postmenopausal atrophic vaginitis.

For reference, the only registered trial among the other predicted indications (AIDS) is below. It is indirectly relevant at best.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03412071](https://clinicaltrials.gov/study/NCT03412071) | Not applicable | Unknown | 125 | Pilot study of four antimicrobial products (3 topical, 1 systemic) on the foreskin microbiome and HIV susceptibility in Ugandan men. It does not test tinidazole for AIDS treatment, and no efficacy data are available. |

## Literature Evidence

Currently no related literature is available for postmenopausal atrophic vaginitis.

Literature was retrieved only for the AIDS prediction. It mostly concerns tinidazole's established uses and does not show benefit in HIV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21931875](https://pubmed.ncbi.nlm.nih.gov/21931875/) | 2011 | Cohort | PLoS Negl Trop Dis | Retrospective analysis of 170 HIV-1-infected Japanese men with invasive amoebiasis: clinical features and response to therapy |
| [8442923](https://pubmed.ncbi.nlm.nih.gov/8442923/) | 1993 | Preliminary study | AIDS | Combined tinidazole, thiabendazole and cotrimoxazole versus placebo for AIDS diarrhoea in Zambia |
| [34794678](https://pubmed.ncbi.nlm.nih.gov/34794678/) | 2022 | Review | Pediatr Clin North Am | Amoebiasis and amoebic liver abscess in children, including higher risk in people with HIV/AIDS |
| [19632225](https://pubmed.ncbi.nlm.nih.gov/19632225/) | 2010 | Review | Exp Parasitol | Treatment options and prospects for new drugs against *Cryptosporidium* and *Giardia* |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In vitro | Microbiol Spectrum | In vitro activity of 5-nitroimidazole drugs against *T. vaginalis* clinical isolates |
| [31324206](https://pubmed.ncbi.nlm.nih.gov/31324206/) | 2019 | Trial protocol | Trials | Randomized trial protocol on antimicrobial effects on penile microbiota and HIV susceptibility in Ugandan men |
| [21097745](https://pubmed.ncbi.nlm.nih.gov/21097745/) | 2010 | Case report | Int J STD AIDS | Trichomoniasis presenting as vulval ulceration, fully resolved after oral tinidazole |
| [33121364](https://pubmed.ncbi.nlm.nih.gov/33121364/) | 2021 | Case report | Int J STD AIDS | Successful tinidazole desensitization in a patient with trichomoniasis allergic to metronidazole |

## India Market Information

Twenty valid single-ingredient registrations are on record. The approved indication text is not available for any of them. Five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 84533 | Fasigyn 500mg Tablet | Strip of 4 tablets | Pfizer Ltd |
| 84516 | Fasigyn DS 1000mg Tablet | Strip of 2 tablets | Pfizer Ltd |
| 222759 | Tinibid DS 1000mg Tablet | Strip of 6 tablets | Sun Pharmaceutical Industries Ltd |
| 218212 | Tinifas 500mg Tablet | Strip of 10 tablets | Cipla Ltd |
| 215735 | Tiniba 800mg Infusion | Bottle of 400 ml infusion | Zydus Cadila |

Available forms are oral tablets and intravenous infusions. No vaginal formulation appears in the registration data.

## Safety Considerations

- **Contraindication-related conditions (knowledge graph):** epilepsy, neutropenia, agranulocytosis, peripheral nervous system disease and peripheral neuropathy. These come from graph associations, not from label text.
- **Drug Interactions:** 161 interactions are recorded, and the 20 listed in the data compiled for this report are all of moderate severity. They include paclitaxel, cabazitaxel, capecitabine, bortezomib, brentuximab vedotin, trastuzumab emtansine, amiodarone, atorvastatin, ethinylestradiol, estradiol, levodopa and ethanol. Alcohol is a well-known concern with nitroimidazoles.

Please refer to the package insert for other warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no clinical trials or literature. The disease is estrogen-deficiency driven, so an antimicrobial mechanism is unlikely to be relevant. Other top-ranked predictions are similarly unsupported, and the AIDS-related evidence reflects treatment of co-infections, not of HIV.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source
- Detailed mechanism of action data
- Evidence that a secondary infectious component is clinically relevant in atrophic vaginitis, before any trial is designed
- Assessment of route compatibility, since no vaginal formulation is currently registered
- Review of the neuropathy, neutropenia and epilepsy signals for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

