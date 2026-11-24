---
layout: default
title: Capreomycin
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 9
monitor_inn: "Capreomycin"
predicted_indications: ["gout", "rheumatoid arthritis", "osteoarthritis", "sclerosing cholangitis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "meningococcal infection", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type"]
last_modified_at: 2026-11-24
description: "Capreomycin: predicted new indication gout (evidence level L5). In India: 7 listed products (7 not discontinued)"
---

# Capreomycin
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

## Capreomycin: Cyclic peptide antibiotic (ribosome-targeting) → Gout
{: .text-alpha }

## One-Sentence Summary

Capreomycin is an injectable cyclic peptide antibiotic used against mycobacterial infection.
The TxGNN model predicts it may be effective for **gout**, but **no clinical trials and no publications** were found in the data compiled for this report, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gout |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Capreomycin belongs to the cyclic peptide, aminoglycoside-like antibiotic class, which is understood to act by binding the bacterial ribosome and inhibiting protein synthesis.

Gout is driven by inflammation triggered by urate crystals in the joints. No established link connects ribosomal inhibition to urate metabolism or crystal-induced inflammation, so no clear mechanistic link was identified. The high score of 0.9991 is a model output only. It is not supported by any trial or publication.

Capreomycin's known kidney toxicity and electrolyte disturbances would also be unfavourable in gout patients, who often have kidney problems.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 48124 | Ciprix 750mg Injection | Vial of 1 Injection | Valid |
| 50929 | Ciprix 500mg Injection | Vial of 1 Injection | Valid |
| 51078 | Ciprix 1000mg Injection | Vial of 1 Injection | Valid |
| 51890 | Capreo 500mg Injection | Vial of 1 Injection | Valid |
| 117091 | Kapocin 750 Injection | Vial of 1 Powder for Injection | Valid |
| 117665 | Kapocin 1gm Injection | Vial of 1 Injection | Valid |
| 117896 | Kapocin 500mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 58 interactions were identified. Two are rated Major: **kanamycin** and **neomycin**. Both are aminoglycosides, so additive kidney and hearing toxicity is a concern. Many others are rated Moderate, including amphotericin B (several formulations), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone), proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, rabeprazole, dexlansoprazole), mesalazine-type drugs (mesalazine, balsalazide, olsalazine) and exenatide.

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, no plausible mechanism linking capreomycin to gout, and the toxicity profile and injection-only route make long-term use in gout impractical.

**To proceed, the following is needed:**
- Mechanism-of-action data and any biological rationale linking capreomycin to urate handling or crystal-induced inflammation
- Preclinical or in vitro evidence in a gout model
- Package insert warnings and contraindications, to assess kidney, hearing and electrolyte risks
- A comparison against existing gout therapies, which are oral and well established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

