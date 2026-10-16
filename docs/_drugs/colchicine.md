---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an established anti-inflammatory drug, originally used to treat gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**,
but there are currently **0 clinical trials** and only **2 indirect preclinical publications**, so this is essentially a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (from the knowledge-graph indication list, since the India licence records contain no indication text) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Colchicine inhibits microtubule polymerization. Plasmodium parasites depend on microtubules for cell division and for the structure of their different life-cycle stages, so a mechanistic rationale for antimalarial activity exists. Detailed mechanism of action data is not otherwise available in the data compiled for this report.

The link between the original and new indications is weak. Gout and FMF are inflammatory conditions treated by dampening neutrophil activity, whereas malaria is a parasitic infection. The connection is therefore based on the shared target (microtubules) rather than on similar disease biology.

The two publications supplied are indirect. One studies curcumin, not colchicine, and its effects on P. falciparum microtubules. The other examines expression of the parasite pfmdr1 gene in mammalian cells and chloroquine susceptibility, a multidrug-resistance transporter context that may be relevant to colchicine as a P-glycoprotein substrate. Neither shows that colchicine works against malaria.

Two other predictions were also generated:
- **Familial Mediterranean fever, autosomal dominant** (score 99.38%): This largely reflects colchicine's existing first-line use in FMF, and is likely an ontology label-mapping case rather than a true repurposing opportunity. Supporting literature consists of review articles, with no trials supplied. The evidence level is L4 and the decision is Hold.
- **Dermatofibrosarcoma protuberans** (score 99.37%): No trials or literature were supplied. The disease is driven by the COL1A1-PDGFB fusion and is treated with surgery and imatinib, so the link to colchicine is unsupported. The evidence level is L5 and the decision is Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro / preclinical | PLoS One | Curcumin (not colchicine) disrupts P. falciparum microtubules, supporting microtubules as a parasite target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / preclinical | Mol Cell Biol | Expression of the parasite pfmdr1 gene in mammalian cells increased chloroquine susceptibility; relevant to multidrug-resistance transporters |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 94225 | Goutnil 0.5mg Tablet | Strip of 10 tablets | Not stated |
| 97772 | Gountnil 0.5mg Tablet | Strip of 10 tablets | Not stated |
| 246411 | Zycolchin Tablet | Strip of 10 tablets | Not stated |
| 37782 | Colchicindon 0.5mg Tablet | Strip of 10 tablets | Not stated |
| 37532 | Coljoy 0.5mg Tablet | Strip of 10 tablets | Not stated |

Seven valid single-ingredient registrations exist in total; all are oral tablets.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver failure, renal impairment, hematologic disease (including thrombocytopenia, leukopenia, agranulocytosis, neutropenia, aplastic anemia), peptic ulcer disease, diarrheal disease, myopathy and rhabdomyolysis, and acute urate nephropathy.
- **Drug Interactions**: 127 interactions are recorded. Major ones include:
  - Clarithromycin and cobicistat (CYP3A4/P-gp inhibitors)
  - Aprepitant and rolapitant
  - Rosuvastatin and simvastatin (myopathy risk)
  - Eliglustat and deferiprone

  Moderate ones include metronidazole, cimetidine, chloroquine, ticagrelor and miconazole.
- Colchicine has a narrow therapeutic index. Its interactions with CYP3A4/P-gp substrates and with antimalarials would complicate any use in malaria.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.60%) is a model prediction only. No clinical trials exist, and the two publications are indirect and preclinical. Colchicine's narrow therapeutic index and extensive interaction profile add further concern.

**To proceed, the following is needed:**
- Direct in vitro and in vivo data on colchicine's activity against P. falciparum
- Mechanism of action data
- Package insert warnings and contraindications from the India regulatory source (currently missing)
- Assessment of whether tolerable doses can reach antiparasitic concentrations
- Interaction assessment with standard antimalarial regimens
- Confirmation of whether the autosomal dominant FMF prediction should be treated as an on-label mapping
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

