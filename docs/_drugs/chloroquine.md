---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 4
---

# Chloroquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Chloroquine: From Rheumatoid Arthritis and Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is an established antimalarial that is also used for rheumatoid arthritis and lupus.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis**,
but the data compiled for this report contain **no clinical trials** and only **1 publication**, which does not study chloroquine. This is a model-based prediction with very little direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, systemic lupus erythematosus, malaria (Plasmodium vivax, falciparum, ovale, malariae), discoid and chronic cutaneous lupus erythematosus (from the knowledge graph; no approved-indication text in the India licences) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chloroquine is an antimalarial that is also used as a slow-acting, DMARD-like agent in rheumatoid arthritis. It is thought to act through immunomodulation: raising lysosomal pH and inhibiting autophagy, reducing antigen presentation, and lowering pro-inflammatory cytokine production.

RF-positive polyarticular JIA closely resembles adult seropositive rheumatoid arthritis, so the same immunomodulatory effects may plausibly apply. The very high TxGNN score most likely reflects this network proximity to the approved RA indication rather than direct clinical evidence in JIA.

Related predictions in the same disease family (rheumatoid nodulosis, juvenile chronic polyarthritis and juvenile idiopathic arthritis overall) also show scores of about 99%. They rest on the same reasoning and are likewise not supported by chloroquine-specific trials in the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort (prospective, real-life) | The Journal of Rheumatology | Describes long-term clinical experience with leflunomide in JIA. It does not evaluate chloroquine, so it is indirect evidence only. |

Across the broader JIA predictions, historical literature is also available, such as 1970s dosing studies of chloroquine and hydroxychloroquine in juvenile rheumatoid arthritis (PMIDs 4608161, 5574957) and older therapy reviews (PMID 2047820). The abstracts for these were not available, and none provides modern controlled efficacy data.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 144057 | Malaquin 250mg Suspension | Bottle of 60 ml suspension | Not stated |
| 184408 | Resochin Tablet | Strip of 10 tablets | Not stated |
| 18912 | Amoquin 50mg Syrup | Bottle of 60 ml syrup | Not stated |
| 147598 | Malswift 40mg Injection | Vial of 30 ml injection | Not stated |
| 148233 | Malgo 250mg Tablet | Strip of 10 tablets | Not stated |

There are 20 valid single-ingredient registrations in total, covering tablets, syrups, suspensions, drops and injections. Paediatric-friendly forms (syrup, suspension, drops) are available.

## Safety Considerations

- **Contraindications / conditions flagged in the knowledge graph** (not taken from label text): epilepsy, porphyria, liver disease, eye and retinal disease, vision and hearing disorders, psoriasis, neutropenia, agranulocytosis, leukopenia, anaemia, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia and substance abuse/dependence.
- **Drug interactions**: 467 interactions were recorded. Major ones include bupropion, cisapride, clarithromycin, dolasetron, granisetron and agalsidase beta. Moderate ones include antacids (aluminium hydroxide, calcium carbonate), cimetidine, famotidine, metronidazole, and antidiabetic agents (glimepiride, glipizide, glyburide, chlorpropamide, insulin).
- **Literature safety signals**: A case report describes third-degree atrioventricular block under chloroquine therapy (PMID 9523387), and another describes chloroquine-induced vitiligo in juvenile-onset rheumatoid arthritis (PMID 1450810). These call for caution in paediatric use.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score and mechanistic plausibility alone (Evidence Level L5). No clinical trials exist, and the only retrieved publication concerns a different drug. Documented cardiac conduction toxicity and the ocular and haematological risks raise the bar for paediatric use.

**To proceed, the following is needed:**
- Chloroquine-specific (or hydroxychloroquine) efficacy data in JIA, such as controlled trials or well-designed cohorts
- Detailed mechanism of action data
- India package insert warnings and contraindications, which are required for safety screening
- A paediatric dosing and monitoring plan covering retinal, cardiac and haematological surveillance
- Comparison against current standard JIA therapies, since modern practice relies on methotrexate and biologics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

