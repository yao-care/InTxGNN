---
layout: default
title: Amodiaquine
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amodiaquine: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not stated in the India license data"
monitor_inn: "Amodiaquine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "kyphoscoliotic heart disease", "migraine with or without aura, susceptibility to", "migraine with brainstem aura", "rheumatoid arthritis", "leprosy", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Amodiaquine
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

# Amodiaquine: From Malaria to Pulmonary Hypertension

## One-Sentence Summary

Amodiaquine is a 4-aminoquinoline drug that is marketed in India as a single-ingredient product, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The only indication in the ranked list with meaningful supporting literature is **rheumatoid arthritis** (8 publications, mostly historical), which is covered as an additional finding below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amodiaquine is a 4-aminoquinoline antimalarial, related to chloroquine and hydroxychloroquine. Its original indication is not recorded in the license data compiled for this report.

For pulmonary hypertension, no mechanistic rationale is evident from the available data. The score reflects the model's graph-based prediction only, with no trials or literature to back it. The other top-ranked predictions are similar: several migraine entries (migraine disorder, susceptibility, brainstem aura) probably come from the same graph neighbourhood and should not be counted as independent evidence. The rare conditions (nephrogenic syndrome of inappropriate antidiuresis, kyphoscoliotic heart disease, atrophoderma vermiculata, ulerythema ophryogenesis) likewise have no supporting data.

### Additional Finding: Rheumatoid Arthritis (Rank 7, score 98.65%, Evidence Level L3)

Rheumatoid arthritis is the best-supported alternative direction. Amodiaquine is structurally and pharmacologically related to chloroquine and hydroxychloroquine, which are established disease-modifying drugs for this condition. Preclinical work suggests anti-inflammatory activity through suppression of T cell proliferation and Th1 differentiation. A 2025 computational study also points to possible PAD4 inhibitor repositioning potential, which is relevant to citrullination biology in rheumatoid arthritis. Historical clinical reports from 1959 to 1964 exist, but their methodological quality cannot be verified from the data available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension, nor for any of the other top-ten predicted indications.

---

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

For the additional rheumatoid arthritis direction, the following publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13799077](https://pubmed.ncbi.nlm.nih.gov/13799077/) | 1959 | Controlled clinical study (historical) | Arthritis and Rheumatism | 15-month controlled study of amodiaquine (Camoquin) in rheumatoid arthritis; no abstract available |
| [14408648](https://pubmed.ncbi.nlm.nih.gov/14408648/) | 1959 | Clinical study (historical) | Lancet | Amodiaquine and hydroxychloroquine in rheumatoid arthritis; no abstract available |
| [27109480](https://pubmed.ncbi.nlm.nih.gov/27109480/) | 2016 | Preclinical | Biochem Biophys Res Commun | Chloroquine and amodiaquine reduce T cell proliferation and Th1 differentiation via p21 |
| [40697620](https://pubmed.ncbi.nlm.nih.gov/40697620/) | 2025 | Computational/in vitro | RSC Med Chem | Virtual screening for repositioned PAD4 inhibitors, relevant to rheumatoid arthritis |
| [29071567](https://pubmed.ncbi.nlm.nih.gov/29071567/) | 2017 | Preclinical | Arch Pharm Res | Anti-adipogenic activity through PPARγ suppression; rheumatoid arthritis mentioned as a therapeutic area of interest |
| [13939082](https://pubmed.ncbi.nlm.nih.gov/13939082/) | 1962 | Review (historical) | Hospital (Rio de Janeiro) | Evaluation of antimalarials for rheumatoid arthritis |
| [13975794](https://pubmed.ncbi.nlm.nih.gov/13975794/) | 1962 | Clinical report (historical) | Vie Medicale | Treatment of rheumatoid polyarthritis with synthetic antimalarials |
| [14203311](https://pubmed.ncbi.nlm.nih.gov/14203311/) | 1964 | Clinical commentary (historical) | Gazette Medicale de France | Reflections on a corticoid-aspirin-antimalarial combination |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 79388 | Eriquin 200mg Tablet | Strip of 10 tablets | Not stated |
| 28083 | Basoquin Suspension | Bottle of 30 ml suspension | Not stated |

---

## Safety Considerations

Please refer to the package insert for safety information.

Note that the literature reviewed for the rheumatoid arthritis direction flags hepatotoxicity and agranulocytosis as risks associated with amodiaquine that would need careful weighing against hydroxychloroquine, which has a better-established safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction rests on the model score alone (Evidence Level L5), with no trials, no literature and no identifiable mechanistic link. The rheumatoid arthritis direction (L3) is more plausible, but its human evidence is historical and of unverified quality, and it would have to compete with hydroxychloroquine.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data for amodiaquine
- The approved indication text for the Indian licenses
- Any mechanistic or preclinical evidence linking amodiaquine to pulmonary hypertension
- For rheumatoid arthritis: a critical review of the 1959 controlled study, and a comparison of benefit and risk against hydroxychloroquine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

