---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "Flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "ankylosing spondylitis", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Flurbiprofen
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

## Flurbiprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Flurbiprofen is a nonsteroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and related joint disorders.
The TxGNN model's top-ranked prediction is **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder, but **no clinical trials and no publications** support it, so it rests on the model score alone.
A different, lower-ranked prediction, **ankylosing spondylitis**, has much stronger support and is discussed in the conclusion.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (model prediction only) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available for this report. Flurbiprofen belongs to the NSAID class, which reduces prostaglandin-mediated inflammation and pain by inhibiting the COX-1 and COX-2 enzymes. Its efficacy in inflammatory and degenerative joint disease is well established.

The predicted disease is a rare genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway, which governs bone and cartilage development. A symptomatic anti-inflammatory drug has no clear way to alter this pathway. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related skeletal and joint diseases, not biological evidence.

Several other top-ranked predictions have the same weakness. They include brachydactyly-syndactyly syndrome, brachyolmia, pseudoachondroplasia and other rare developmental disorders. They also have no trials or literature, and no plausible disease-modifying mechanism for an NSAID.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Flurbiprofen has 20 valid single-ingredient registrations and none cancelled. Only two are oral tablets (Migrid); the other 18 are ophthalmic products (eye drops, solution or ointment). The licence entries do not list approved-indication text. Five representative registrations:

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| 136158 | Migrid 10mg Tablet | Strip of 10 tablets (oral) |
| 139138 | Migrid 5mg Tablet | Strip of 10 tablets (oral) |
| 97660 | Gatidrops FP Eye Drop | Bottle of 5 ml eye drop |
| 164804 | Ocuflur Eye Ointment | Tube of 5 gm eye ointment |
| 84289 | Flur Ophthalmic Solution | Packet of 10 ml ophthalmic solution |

The marketed products are mostly ophthalmic, so a systemic skeletal indication would need an oral product. Route compatibility with any new indication has not yet been assessed.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): hypertension, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction and coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, and substance abuse/dependence.
- **Drug interactions:** 352 interactions are recorded, a heavy burden. Most of the interactions listed are Moderate; only famotidine, cimetidine and linaclotide are Minor. They include:
  - acetylsalicylic acid
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - metformin
  - sulfonylureas (glimepiride, chlorpropamide)
  - mesalazine and balsalazide
  - aprepitant
  - potassium citrate and bicarbonate
  - bowel-preparation laxatives (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)

Please refer to the package insert for label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, acromesomelic dysplasia, Hunter-Thompson type, has only a score from the TxGNN model (deep learning). It has no trials, no publications and no plausible mechanism, so it does not justify further investment.

**Better-supported alternative:** The same analysis ranks **ankylosing spondylitis** eighth, with about 20 publications. These include several double-blind randomized comparisons from 1974 to 1986 against indomethacin, phenylbutazone and naproxen, which found comparable pain relief (for example [PMID 3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) and [PMID 3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/)). This is a drug-class effect, so it is not a novel repurposing, and no disease-modifying benefit has been shown. It is rated L2 and **Proceed with Guardrails**. These trials are small and old, and their phase and design should be verified.

**To proceed, the following is needed:**
- Mechanism-of-action data for flurbiprofen
- Package insert warnings and contraindications for the India products (currently a blocking gap for safety screening)
- Verification of the trial design and phase for the ankylosing spondylitis literature
- A safety plan covering gastrointestinal, cardiovascular and renal risk, gastroprotection, and the high drug-interaction burden
- Assessment of whether an oral product is available for any systemic indication, since most India registrations are ophthalmic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

