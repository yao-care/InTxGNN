---
layout: default
title: Capreomycin
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Capreomycin: predicted new indication Gout (evidence level L5). Approved use: Pulmonary tuberculosis"
monitor_inn: "Capreomycin"
predicted_indications: ["gout", "rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "sclerosing cholangitis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "meningococcal infection", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Capreomycin
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

# Capreomycin: From Pulmonary Tuberculosis to Gout

## One-Sentence Summary

Capreomycin is an injectable antibiotic originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **gout**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (from the knowledge graph; no approved indication text is available in the Indian licence records) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, capreomycin is a cyclic peptide antibiotic related to the aminoglycosides, and its efficacy in tuberculosis is established. It is thought to act by inhibiting bacterial protein synthesis at the ribosome.

Gout is driven by inflammation triggered by urate crystals, and there is no established connection between ribosomal inhibition and this process. The very high TxGNN score (99.91%) most likely reflects proximity in the knowledge graph rather than a biological rationale.

In addition, capreomycin's kidney toxicity and electrolyte disturbances would be unfavourable in a population where kidney problems are common. The prediction is therefore not mechanistically supported at present.

Other predictions in the same list (rheumatoid arthritis, osteoarthritis, sclerosing cholangitis, and several rare skeletal or developmental syndromes) share the same weaknesses: no trials, no literature, and no plausible mechanism. Meningococcal infection is the only one with an indirect, class-level rationale (an antibacterial for a bacterial infection), but well-established beta-lactams already treat it and capreomycin has no supporting data.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 51890 | Capreo 500mg Injection | Vial of 1 Injection | Not stated in the records |
| 117896 | Kapocin 500mg Injection | Vial of 1 Injection | Not stated in the records |
| 50929 | Ciprix 500mg Injection | Vial of 1 Injection | Not stated in the records |
| 51078 | Ciprix 1000mg Injection | Vial of 1 Injection | Not stated in the records |
| 117665 | Kapocin 1gm Injection | Vial of 1 Injection | Not stated in the records |

Seven valid single-ingredient registrations exist in total; the five above are shown. All are injectable products.

## Cytotoxicity

Capreomycin is an antibiotic, not an antineoplastic drug, so cytotoxic-drug handling requirements do not apply.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, potassium deficiency, hearing loss disorder, and X-linked mixed deafness with perilymphatic gusher.
- **Drug Interactions**: 58 interactions were identified in total. The two rated **Major** are **kanamycin** and **neomycin**, both aminoglycosides, so combining them risks additive toxicity. Many others are rated Moderate, including amphotericin B (all formulations), the corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone), the proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole), the mesalazine-related drugs (mesalazine, balsalazide, olsalazine), and exenatide.
- Kidney toxicity, hearing toxicity and electrolyte disturbances are the main concerns. Please refer to the package insert for full label warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or publications, no plausible mechanism linking capreomycin to gout, and the drug's toxicity and injection-only route make chronic use for gout implausible.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers, plus the approved indication text
- Mechanism of action data for capreomycin
- Any preclinical or clinical evidence linking capreomycin to urate-related inflammation
- A route and dosing feasibility assessment, since all marketed forms are injectable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

