---
layout: default
title: Flupirtine
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flupirtine: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the available licence records (approved indication text…"
monitor_inn: "Flupirtine"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "hepatic porphyria", "pseudoachondroplasia", "gout", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "hepatoportal sclerosis", "primitive portal vein thrombosis"]
---

# Flupirtine
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

## Flupirtine: From Pain Management to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Flupirtine is a centrally acting, non-opioid analgesic (a selective neuronal potassium channel opener) marketed in India under many brand names, mainly for pain and muscle-relaxant use.
The TxGNN model predicts it may be useful for **osteoarthritis** with a very high score, but there are currently **0 registered clinical trials** and only **indirect or preclinical literature** supporting this direction.
The evidence is at the research-question stage, and the known liver safety risk weighs heavily on any repurposing decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence records (approved indication text is empty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 (preclinical and mechanistic evidence only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known pharmacology, flupirtine is a selective neuronal potassium channel (KCNQ/Kv7) opener with analgesic and muscle-relaxant activity.

A 2019 rat study (PMID 30759446) found that KCNQ/M channels in dorsal root ganglia neurons are suppressed in osteoarthritic pain, and that this is associated with hyperalgesic behaviour. Opening these channels is therefore a plausible way to relieve osteoarthritis pain.

This supports **symptomatic pain relief only**, not disease modification. Flupirtine has been withdrawn or restricted in Europe because of hepatotoxicity, which is a major concern for a chronic condition such as osteoarthritis.

### Other Predicted Indications (for reference)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Osteoarthritis susceptibility | 98.46% | L5 | Genetic susceptibility concept, not a treatable indication; likely reflects similarity to osteoarthritis |
| Rheumatoid arthritis | 98.43% | L4 | Possible symptomatic analgesia only; no anti-inflammatory or disease-modifying action; only a 1987 preliminary report |
| Gout | 97.83% | L4 | Preclinical animal data on gout arthritis pain; no human data; does not address urate or inflammation |
| Hepatic porphyria, hepatoportal sclerosis, primitive portal vein thrombosis | 97.5–97.9% | L5 | No rationale; likely graph artifacts; liver safety concern |
| Pseudoachondroplasia, brachyolmia, acromesomelic dysplasia (Hunter-Thompson type) | 97.6–97.9% | L5 | Rare skeletal dysplasias with no plausible mechanistic link |

---

## Literature Evidence

Currently no registered clinical trials are available for osteoarthritis. The literature below is indirect or preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30759446](https://pubmed.ncbi.nlm.nih.gov/30759446/) | 2019 | Preclinical (animal) | Pharmacology | Reduced KCNQ2/KCNQ3 expression and M-current in dorsal root ganglia neurons of osteoarthritic rats, associated with pain behaviour; supports the KCNQ-opening rationale |
| [25376546](https://pubmed.ncbi.nlm.nih.gov/25376546/) | 2015 | Systematic review | Schmerz | Opioids vs non-opioid analgesics in chronic non-cancer pain; indirect relevance |
| [28510996](https://pubmed.ncbi.nlm.nih.gov/28510996/) | 2017 | Systematic review | Cochrane Database Syst Rev | Tramadol for cancer pain; not relevant to osteoarthritis or flupirtine |
| [26977921](https://pubmed.ncbi.nlm.nih.gov/26977921/) | 2015 | Review | Zh Nevrol Psikhiatr Im S S Korsakova | Differential diagnosis and treatment of back pain (spinal osteoarthritis); indirect |

Related evidence for other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2451818](https://pubmed.ncbi.nlm.nih.gov/2451818/) | 1987 | Preliminary clinical report | Postgrad Med J | Long-term flupirtine in chronic pain from arthrosis or arthritis (104 patients reported, 12-month study); uncontrolled and dated |
| [32062659](https://pubmed.ncbi.nlm.nih.gov/32062659/) | 2020 | Preclinical (animal) | Pharmacology | Retigabine and flupirtine showed antinociceptive efficacy in a gout arthritis pain model |

---

## India Market Information

Flupirtine is widely registered in India: 20 valid single-ingredient registrations, with none cancelled. The approved indication text is not recorded in the licence data. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 174704 | Pirineu P 100mg/325mg Tablet | Strip of 10 tablets | Not recorded |
| 85535 | Flupride 100mg Tablet | Strip of 10 tablets | Not recorded |
| 175091 | Pirineu 100mg Capsule | Strip of 10 capsules | Not recorded |
| 233340 | Vasfree 100 Capsule (Intas) | Strip of 10 capsules | Not recorded |
| 115766 | Katadol Capsule (Lupin) | Strip of 10 capsules | Not recorded |

All products are oral (tablets, capsules, and one extended-release tablet).

---

## Safety Considerations

- **Hepatotoxicity:** Flupirtine has been withdrawn or restricted in Europe because of liver toxicity. This is a major concern for long-term use in chronic diseases such as osteoarthritis or rheumatoid arthritis, and it makes use in liver disease (for example hepatic porphyria, hepatoportal sclerosis, portal vein thrombosis) especially problematic.

Please refer to the package insert for further safety information, including warnings, contraindications and drug interactions. These were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for osteoarthritis is mechanistically plausible (KCNQ/Kv7 opening for pain relief), but there are no registered clinical trials and the supporting literature is preclinical or indirect. The known hepatotoxicity risk makes long-term use in a chronic condition hard to justify without stronger evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, to complete safety screening
- Confirmed approved indications for the registered Indian products
- Detailed mechanism-of-action data
- Controlled clinical evidence of efficacy in osteoarthritis pain, compared against current analgesic options
- A liver safety assessment and monitoring plan, including current European regulatory status and post-marketing hepatic safety data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

