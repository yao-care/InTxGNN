---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 20
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Acetic Acid: predicted new indication Post-bacterial disorder (evidence level L5). Approved use: Otitis externa, external ear disease"
monitor_inn: "Acetic acid"
predicted_indications: ["post-bacterial disorder", "postinfectious vasculitis", "post-infectious syndrome", "Chagas cardiomyopathy", "infective urethral stricture", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis", "pityriasis simplex", "tinea corporis"]
---

# Acetic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Acetic Acid: From Otitis Externa to Post-Bacterial Disorder
{: .text-alpha }

## One-Sentence Summary

Acetic acid is a topical acidifying and antimicrobial agent, originally used to treat otitis externa (external ear disease).
The TxGNN model's top-ranked prediction is **post-bacterial disorder**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.
The only prediction with any meaningful supporting literature is **tinea corporis** (rank 9), which has historical and indirect evidence only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa, external ear disease |
| Predicted New Indication | Post-bacterial disorder (top-ranked); tinea corporis is the only prediction with supporting literature |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetic acid is a topical acidifier with antibacterial and antifungal activity. Its efficacy in otitis externa is established, and mechanistically it may be applicable to some superficial infections.

For the top-ranked prediction, **post-bacterial disorder**, the link is weak. The term is a non-specific category (post-infectious sequelae), and there is no clear pharmacological connection to a topical antiseptic. The other high-scoring predictions (postinfectious vasculitis, post-infectious syndrome, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome, drug-induced osteoporosis) involve immune-mediated or systemic processes that a topical agent is unlikely to influence. Infective urethral stricture has only a very weak indirect rationale, because dilute acetic acid is used as an irrigant in some settings.

The most biologically plausible prediction is **tinea corporis** (score 0.9925). Acetic acid acidifies the skin surface and inhibits fungal growth, which is consistent with its use in fungal otitis externa. Historical reports describe dilute acetic acid for related dermatophyte infections. Pityriasis simplex (score 0.9933) is also loosely plausible through the same skin-acidifying effect, but no evidence was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked prediction (post-bacterial disorder). The table below covers the most relevant publications found for **tinea corporis** (rank 9), the only prediction with meaningful supporting literature. The evidence is dated, uncontrolled, and mostly concerns related dermatophytoses rather than tinea corporis itself.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical case series | Urol Cutaneous Rev | Larger series of tinea capitis patients treated with special iodine and dilute acetic acid |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical clinical report | JAMA | Treatment of tinea capitis with special iodine and dilute acetic acid |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical clinical report | Arch Dermatol Syphilol | Treatment of tinea capitis with special iodine and dilute acetic acid |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical clinical report | Vestn Dermatol Venerol | Foot epidermophytosis treated with increasing concentrations of acetic acid |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Case report/series | Skin Appendage Disord | Chemical peeling as an alternative to oral antifungals for onychomycosis in special circumstances |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | In vitro | Mycoses | Topical antifungal products evaluated in an in vitro onychomycosis model |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case series (safety) | Arch Plast Surg | Burns caused by Korean folk remedies, a safety concern for uncontrolled topical use |

For **post-infectious syndrome** (rank 3), the only item is a 2011 systematic review of animal models of post-infectious IBS ([20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/), J Gastroenterol). It does not show therapeutic benefit from acetic acid.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 805 | Acetik Ear Drop (NuLife Pharmaceuticals) | 10 ml bottle, ear drop | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals**: The TxGNN knowledge graph links acetic acid to contraindications in inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infectious disease, and geniculate herpes zoster. These come from graph edges rather than label text, so they should be verified against the product label.
- **Topical misuse risk**: A 2023 report describes burns caused by folk remedies, which raises a safety concern for uncontrolled topical use of acid-containing preparations.

No drug interaction data were found. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the TxGNN model (deep learning), with no clinical trials; the scores may reflect similarities the model learned between related diseases, not biological evidence. The top-ranked prediction (post-bacterial disorder) is non-specific and has no clear pharmacological link to a topical antiseptic. Tinea corporis is the most plausible research question (evidence level L4), but its support is limited to dated, uncontrolled reports on related dermatophytoses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed product (needed before any safety screening)
- Detailed mechanism of action data
- For tinea corporis: modern controlled studies comparing dilute acetic acid with standard topical antifungals, with a defined concentration and safety profile for skin use
- Confirmation of route compatibility, since the marketed product is an ear drop and skin use would need a different formulation
- Clarification of the post-bacterial disorder definition before any further assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

