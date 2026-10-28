---
layout: default
title: Clioquinol
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
monitor_inn: "Clioquinol"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-23
description: "Clioquinol: predicted new indication Ectothrix infectious disease (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection…"
---

# Clioquinol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Clioquinol: From Tinea Infections to Ectothrix Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Clioquinol is a topical agent used for superficial fungal skin infections such as tinea pedis and tinea corporis.
The TxGNN model predicts it may be effective for **ectothrix infectious disease** (a dermatophyte infection of the hair shaft), but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, dermatophytosis of groin and perianal area (relations recorded in the knowledge graph; the licence records contain no indication text) |
| Predicted New Indication | Ectothrix infectious disease |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, clioquinol is a topical antifungal and antimicrobial agent. Its activity is plausibly related to chelation of metal ions such as copper, zinc and iron, which may disrupt fungal enzyme function. This remains a hypothesis and not a confirmed mechanism.

Ectothrix infection is a dermatophyte infection in which fungal arthroconidia form a sheath on the outside of the hair shaft (for example *Microsporum* and some *Trichophyton* species). It belongs to the same disease family as the tinea infections linked to clioquinol. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction is therefore mainly an extension within the same disease family and not a distinct new use.

A key limitation is that hair-shaft infections usually need systemic therapy, because topical agents penetrate the hair follicle poorly. Topical clioquinol may therefore be insufficient.

A second predicted indication, endothrix infectious disease (score 0.9919, also L5, Hold), follows the same reasoning. Spores grow inside the hair shaft, as in tinea capitis, and standard care relies on systemic antifungals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 59852 | Dermoquinol 8% Cream | Tube of 25 gm cream | Not stated in the records |
| Registration No. 64513 | Dermoquinol 4% Ointment | Tube of 15 gm ointment | Not stated in the records |
| Registration No. 61339 | Dermoquinol 4% Cream | Tube of 25 gm cream | Not stated in the records |
| Registration No. 64362 | Dermoquinol 8% Ointment | Tube of 15 gm ointment | Not stated in the records |
| Registration No. 61594 | Dermi-Zio 6 Cream | Tube of 15 gm cream | Not stated in the records |

All five registrations are valid single-ingredient topical products (creams and ointments).

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists contraindication relations with adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication and peripheral arterial disease. These come from the graph and have not been verified against product labelling.
- **Neurotoxicity history:** Oral clioquinol has been associated with subacute myelo-optic neuropathy (SMON). Any systemic exposure therefore calls for caution, which is especially relevant if systemic delivery were considered for hair-shaft infections.

No drug interaction data were found. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model scoring and similarity to existing tinea indications. No clinical trial or publication studies ectothrix infection directly, so the evidence level is L5. Poor follicular penetration of topical products further limits the likelihood of benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products (currently a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Evidence of follicular or hair-shaft penetration for topical clioquinol, plus in vitro activity against ectothrix pathogens
- Clinical or observational data in hair-shaft dermatophytosis
- A route and exposure assessment that takes the SMON history into account
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

