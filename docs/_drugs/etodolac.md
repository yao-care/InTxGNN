---
layout: default
title: Etodolac
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etodolac: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
---

# Etodolac
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

# Etodolac: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Etodolac is a nonsteroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and related joint disorders.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare inherited skeletal disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (from the knowledge-graph indication list; the India licence records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for etodolac is not available in the data compiled for this report. It is known to be an NSAID that inhibits cyclooxygenase (COX), with a preferential effect on COX-2. This reduces prostaglandin-driven inflammation and pain in joint disease.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by mutations in the CDMP1/GDF5 gene. The defect lies in growth-factor signalling during bone and cartilage development. Etodolac's COX inhibition does not act on this pathway, and no plausible mechanistic link is evident.

The high score (99.97%) most likely reflects the disease's closeness to other musculoskeletal disease nodes in the knowledge graph, not a true pharmacological connection. At best, an NSAID might relieve joint pain symptomatically. It would not be expected to change the underlying developmental defect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Etodolac has 20 valid registrations in India, all single-entity listings. Several products combine etodolac with other actives such as thiocolchicoside, paracetamol or tramadol. The licence records contain no approved-indication text. Five main plain-etodolac products are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 72346 | Etova 400 Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |
| 73022 | Etova 200 Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |
| 75459 | Edonix 600mg Tablet ER | Strip of 10 extended-release tablets | Ajanta Pharma Ltd |
| 72861 | Etornext-ER Tablet | Strip of 10 extended-release tablets | Alembic Pharmaceuticals Ltd |
| 73477 | Etosafe ER Tablet | Strip of 10 extended-release tablets | Wanbury Ltd |

All products are oral formulations.

---

## Safety Considerations

- **Disease-level contraindication signals** (from the knowledge graph, not package insert text): hypertension and hypertensive disorders, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active ulcer), blood coagulation disease, myocardial infarction and coronary thrombosis, hemoglobinopathy, and cardiovascular and heart disease.
- **Drug Interactions**: 221 interactions were identified in total. Those listed below are a sample of 20, and most carry a Moderate rating.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide (Moderate)
  - Acetylsalicylic acid (Moderate)
  - Mesalazine and balsalazide (Moderate)
  - Metformin, glimepiride, chlorpropamide, repaglinide (Moderate)
  - Potassium citrate and potassium bicarbonate (Moderate)
  - Picosulfuric acid and polyethylene glycol with electrolytes (Moderate)
  - Famotidine, ranitidine, cimetidine, linaclotide (Minor)

Please refer to the package insert for the full set of warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it. The target is a genetic developmental disorder, and etodolac's COX-inhibiting mechanism has no apparent link to the GDF5 signalling defect. The score is likely a network-proximity artefact.

Among the other predictions evaluated for etodolac, **ankylosing spondylitis** has more support. It is backed by reviews, open-label studies and postmarketing surveillance (Evidence Level L3, Proceed with Guardrails). It is largely an extension of the existing spondyloarthropathy indication, not a new mechanism.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking etodolac to GDF5-related skeletal dysplasia
- Detailed mechanism-of-action data for etodolac
- Package insert warnings and contraindications from the India regulatory source
- A clear case that symptomatic NSAID use would help this rare population, with cardiovascular, gastrointestinal and renal risks assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

