---
layout: default
title: Butenafine
parent: Model Prediction Only (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Butenafine: predicted new indication Superficial mycosis (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection, pityriasis versicolor…"
monitor_inn: "Butenafine"
predicted_indications: ["endothrix infectious disease", "Majocchi granuloma", "ectothrix infectious disease"]
---

# Butenafine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Butenafine: From Superficial Fungal Skin Infections (Tinea) to Superficial Mycosis

## One-Sentence Summary

Butenafine is a topical benzylamine antifungal, originally used for tinea pedis, tinea corporis, other tinea infections, pityriasis versicolor, and dermatophytosis of the groin and perianal area.
The TxGNN model predicts it may be effective for **superficial mycosis** (the top-ranked prediction, cutaneous candidiasis, has much weaker support), with **no registered clinical trials** but **11 publications**, including a vehicle-controlled RCT, supporting this direction.
Note that this is largely a relabeling of existing uses rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, pityriasis versicolor, dermatophytosis of groin and perianal area (from the knowledge graph; the Indian license records contain no indication text) |
| Predicted New Indication | Superficial mycosis (the strongest-supported of the five predictions; the rank-1 prediction is cutaneous candidiasis) |
| TxGNN Prediction Score | 99.02% for superficial mycosis (cutaneous candidiasis: 99.33%) |
| Evidence Level | L1 for superficial mycosis (L4 for cutaneous candidiasis; L5 for the other three predictions) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails (superficial mycosis); Hold for the other four predictions |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available for this drug. Based on known pharmacology, butenafine is a benzylamine antifungal that inhibits squalene epoxidase. This blocks ergosterol synthesis, depletes ergosterol in the fungal cell membrane, and causes squalene to accumulate, which is fungicidal against susceptible organisms such as dermatophytes.

Superficial mycoses (dermatophytoses, pityriasis versicolor) are the established territory of this drug. The prediction is therefore consistent with its approved class of use, and is closer to relabeling than to genuine repurposing. The published literature includes a vehicle-controlled RCT in tinea pedis, a randomized comparison against bifonazole, and a multicentre efficacy and safety study in tinea pedis, cruris and corporis.

The other predictions are weaker:
- **Cutaneous candidiasis**: Candida also depends on ergosterol, so a mechanistic link is plausible. However, benzylamine and allylamine activity against Candida is generally weaker and more variable than against dermatophytes. The supplied literature consists of antifungal reviews and an in vitro study of a different drug (KP-103), with no direct clinical data on butenafine.
- **Endothrix infection, ectothrix infection, Majocchi granuloma**: The organisms are plausibly susceptible, but topical butenafine penetrates poorly into hair follicles, hair shafts and the dermis. These conditions are conventionally treated with systemic therapy. There are no trials or literature, so support is a model prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table covers the superficial mycosis prediction, which has the most relevant literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9039200](https://pubmed.ncbi.nlm.nih.gov/9039200/) | 1997 | RCT (vehicle-controlled) | J Am Acad Dermatol | One-week twice-daily butenafine 1% cream versus vehicle in tinea pedis (multicenter, double-blind) |
| [23283047](https://pubmed.ncbi.nlm.nih.gov/23283047/) | 2012 | Randomized, double-blind comparative study | Global Journal of Health Science | Butenafine versus bifonazole cream for 2 weeks in 96 patients with superficial mycosis; safety and efficacy compared |
| [11676116](https://pubmed.ncbi.nlm.nih.gov/11676116/) | 2001 | Clinical study | J Indian Med Assoc | Butenafine 1% cream in 111 patients with tinea pedis (4 weeks), tinea cruris and tinea corporis (2 weeks); efficacy and safety assessed (non-comparative) |
| [18624686](https://pubmed.ncbi.nlm.nih.gov/18624686/) | 2008 | Review | Expert Opin Drug Metab Toxicol | Butenafine is a benzylamine with potent fungicidal activity, particularly against dermatophytes |
| [12432425](https://pubmed.ncbi.nlm.nih.gov/12432425/) | 2002 | Review | Skin Therapy Letter | Effective and safe in interdigital tinea pedis, tinea corporis/cruris and pityriasis versicolor; effect persists at least 4 weeks after stopping |
| [9039197](https://pubmed.ncbi.nlm.nih.gov/9039197/) | 1997 | Review | J Am Acad Dermatol | Update on topical therapy for superficial fungal infections with a focus on butenafine |
| [24898980](https://pubmed.ncbi.nlm.nih.gov/24898980/) | 2014 | Case report | Am J Trop Med Hyg | Tinea nigra treated with butenafine 1% for 30 days, with complete remission and no recurrence at 12 months |
| [10357864](https://pubmed.ncbi.nlm.nih.gov/10357864/) | 1999 | RCT (combination) | Trop Med Int Health | 2% butenafine plus 5% tea tree oil in toenail onychomycosis; the effect of butenafine alone cannot be isolated |
| [11893219](https://pubmed.ncbi.nlm.nih.gov/11893219/) | 2002 | Review | Am J Clin Dermatol | Review of six new antimycotics, including butenafine (cited for cutaneous candidiasis; no direct butenafine candidiasis data) |

Other supplied publications provide only background or supportive context: a review of topical naftifine (PMID 24196340), a review of antifungal-resistant dermatophytosis in Japan (PMID 42219346), an in vitro dermatophyte susceptibility study from Turkey (PMID 38567576), a tinea nigra case report (PMID 41378809), and an animal study of a different drug, KP-103 (PMID 11302816).

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28571 | Butenaskin Cream | Cream, tube of 15 gm | Not stated in the records |
| 116998 | Kutica Cream | Cream, tube of 15 gm | Not stated in the records |
| 221459 | Tenafin Cream | Cream, tube of 10 gm | Not stated in the records |
| 77405 | Exebute Cream | Cream, tube of 15 gm | Not stated in the records |

All four licenses are valid single-ingredient topical products.

---

## Safety Considerations

Please refer to the package insert for safety information. The data compiled for this report contain no drug-interaction records and no knowledge-graph contraindications for butenafine.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (superficial mycosis). **Hold** for cutaneous candidiasis, endothrix infection, Majocchi granuloma and ectothrix infection.

**Rationale:**
- Superficial mycosis is supported by a vehicle-controlled RCT, a randomized comparison against bifonazole, and several reviews. It falls within butenafine's established use in dermatophyte infections and pityriasis versicolor, so it is closer to relabeling than to new repurposing.
- The remaining predictions rest on model scores alone or on indirect literature. Hair-follicle and deep dermal infections are also poorly suited to a topical cream.

**To proceed, the following is needed:**
- The package insert for the four Indian products, to confirm approved indications and obtain warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Guardrail: limit any claim to superficial dermatophyte infections and pityriasis versicolor. Claims for onychomycosis or antifungal-resistant dermatophytosis need separate evidence.
- For cutaneous candidiasis: direct clinical or in vitro data on butenafine against Candida species
- For the hair-follicle and deep infections: evidence of adequate follicular penetration and efficacy, or a decision to exclude topical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

