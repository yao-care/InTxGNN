---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 2
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-30
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Not recorded in the local data"
---

# Colchicine
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

## Colchicine: Microtubule-polymerization inhibitor → Plasmodium falciparum malaria
{: .text-alpha }

## One-Sentence Summary

Colchicine is a microtubule-polymerization inhibitor that is marketed in India as single-ingredient tablets.
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**,
but there are currently **no clinical trials** and only **2 indirect publications** (preclinical, neither testing colchicine against malaria), so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. Colchicine is generally known as a microtubule-polymerization inhibitor. Plasmodium parasites depend on microtubules for cell division and for the structure of their parasite stages, so a mechanistic rationale for antimalarial activity exists.

The two supplied papers are only indirect. One studies how curcumin (not colchicine) disrupts microtubules in *P. falciparum*. The other examines expression of the parasite's *pfmdr1* gene in mammalian cells and its link to chloroquine susceptibility, which is a multidrug-resistance transporter context. Neither shows that colchicine works against malaria in cells, animals or patients.

The high score of 0.9960 is a computational ranking only. Colchicine's narrow therapeutic index and its 127 recorded drug interactions would complicate any use, particularly alongside antimalarials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro / preclinical | PloS one | Curcumin (not colchicine) disrupts microtubules in *P. falciparum*; supports microtubules as a parasite target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / preclinical | Molecular and cellular biology | Expressing the parasite *pfmdr1* gene in mammalian cells increased chloroquine susceptibility; relates to drug-resistance transporters, not colchicine efficacy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 94225 | Goutnil 0.5mg Tablet | Strip of 10 tablets | Not recorded |
| 97772 | Gountnil 0.5mg Tablet | Strip of 10 tablets | Not recorded |
| 246411 | Zycolchin Tablet | Strip of 10 tablets | Not recorded |
| 37782 | Colchicindon 0.5mg Tablet | Strip of 10 tablets | Not recorded |
| 37532 | Coljoy 0.5mg Tablet | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Drug Interactions**: 127 interactions are recorded. Major-level examples include aprepitant, clarithromycin, eliglustat, rolapitant, rosuvastatin, simvastatin, cobicistat and deferiprone. Moderate-level examples include chloroquine, metronidazole, cimetidine, ticagrelor and deferasirox. The chloroquine interaction is directly relevant to any antimalarial setting.
- Colchicine has a narrow therapeutic index, so dose-related toxicity is a concern.

Please also refer to the package insert for label warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a plausible microtubule-based rationale. No study directly tests colchicine against *P. falciparum* malaria, so the evidence level is L5. Safety margins and interactions with antimalarials add further concern.

**To proceed, the following is needed:**
- In vitro activity data for colchicine against *P. falciparum* (including chloroquine-resistant strains)
- A comparison of antiparasitic concentrations with tolerable human exposure, given the narrow therapeutic index
- Package insert warnings and contraindications from the India label
- Detailed mechanism of action data
- An interaction assessment against standard antimalarial regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

