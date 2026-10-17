---
layout: default
title: Chromium
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chromium: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the available licence records"
monitor_inn: "Chromium"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "hepatic porphyria", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Chromium
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

# Chromium: From an Unspecified Original Indication to Rheumatoid Arthritis

## One-Sentence Summary

Chromium is a trace-element injection marketed in India, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts several new indications. The best-supported one is **Rheumatoid Arthritis**, with **1 completed Phase 2/3 trial** and **1 randomized trial publication** on trivalent chromium.
The top-ranked prediction (osteoarthritis, 98.68%) is not supported: the retrieved studies concern cobalt-chromium implant alloys, not chromium as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence records |
| Predicted New Indication | Rheumatoid arthritis (the best-supported of the 10 predictions; the top-ranked prediction by score is osteoarthritis) |
| TxGNN Prediction Score | 98.54% (rheumatoid arthritis); osteoarthritis, rank 1: 98.68% |
| Evidence Level | L2 (rheumatoid arthritis) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold (research question for rheumatoid arthritis) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Chromium is marketed in India as an injectable trace-element product. Because no approved indication text is available, its original therapeutic use cannot be described here.

For **rheumatoid arthritis**, there is a plausible rationale. A rat adjuvant-induced arthritis study found that trivalent chromium reduced inflammation, with up-regulation of FOXP3 and lower synovial Cathepsin G expression. Insulin-sensitizing and anti-inflammatory effects have also been proposed. These findings were then taken into a human randomized trial against baricitinib. The mechanism is still not established in the data compiled for this report.

For **osteoarthritis** and **osteoarthritis susceptibility**, the high scores likely reflect a knowledge-graph link through cobalt-chromium joint implants. The implant literature points to potential harm (metallosis, metal ion release, adverse tissue reactions), not benefit. Gout, hepatic porphyria and the rare skeletal dysplasias (pseudoachondroplasia, brachyolmia and others) have no supporting mechanism or only unrelated literature. Those predictions are purely computational.

## Clinical Trial Evidence

Rheumatoid arthritis (the best-supported prediction):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05545020](https://clinicaltrials.gov/study/NCT05545020) | Phase 2/3 | Completed | 60 | Trivalent chromium supplementation in rheumatoid arthritis patients, with a published randomized comparison against baricitinib |

The other trials retrieved (NCT00120952, NCT03681639) are hip implant device studies. They do not test chromium as a drug and are excluded from the evidence count.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39030450](https://pubmed.ncbi.nlm.nih.gov/39030450/) | 2024 | RCT | Inflammopharmacology | First Phase 2/3 randomized trial of trivalent chromium vs baricitinib in rheumatoid arthritis, assessing effect and safety |
| [35829940](https://pubmed.ncbi.nlm.nih.gov/35829940/) | 2022 | Preclinical (rat model) | Inflammopharmacology | Trivalent chromium reduced adjuvant-induced arthritis, with FOXP3 up-regulation and lower synovial Cathepsin G; compared with prednisolone |
| [39881936](https://pubmed.ncbi.nlm.nih.gov/39881936/) | 2024 | Review | Cureus | Metallosis from metal-on-metal joint implants is a serious complication (osteoarthritis context; a harm signal) |
| [41231919](https://pubmed.ncbi.nlm.nih.gov/41231919/) | 2025 | RCT (implant bearing) | J Bone Joint Surg Am | Serum metal levels after conventional vs modular dual-mobility hip bearings; not a chromium therapy |
| [34232144](https://pubmed.ncbi.nlm.nih.gov/34232144/) | 2021 | Cohort | Clin Orthop Relat Res | Adverse local tissue reactions are common after hip resurfacing, including in asymptomatic patients |
| [41379985](https://pubmed.ncbi.nlm.nih.gov/41379985/) | 2025 | Systematic review / meta-analysis | JBJS Reviews | Hip resurfacing has lower metal ion levels and revision risk than large-head metal-on-metal total hip arthroplasty |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 161947 | Otski Injection | Vial of 3 ml injection | Not stated |
| 219156 | Trace I.V. Injection | Ampoule of 3 ml injection | Not stated |
| 35624 | Celecel Injection | Vial of 3 ml injection | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

Published implant literature on cobalt-chromium alloys reports metal ion release, metallosis, adverse local tissue reactions and metal hypersensitivity. That exposure is different from a chromium injection, but it is a reminder to monitor for toxicity and hypersensitivity if chromium is studied further.

## Conclusion and Next Steps

**Decision: Hold** (rheumatoid arthritis may advance as a research question)

**Rationale:**
Only rheumatoid arthritis has direct human evidence: one small completed Phase 2/3 trial (n=60) and one preclinical study. It has not been independently replicated. The other predictions rest on model scores or on implant-alloy confounding, and the original indication and mechanism of action are unknown.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the Indian regulatory source (a blocking gap for safety screening)
- Mechanism of action data
- Independent replication of the rheumatoid arthritis trial, with a larger sample and longer follow-up
- A dose, route and safety assessment for chronic use in rheumatoid arthritis, since current products are trace-element injections
- Drug-interaction information (none was found in the data compiled)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

