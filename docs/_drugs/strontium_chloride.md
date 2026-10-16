---
layout: default
title: Strontium Chloride
parent: Model Prediction Only (L5)
nav_order: 793
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Strontium Chloride: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not recorded in the India license data"
monitor_inn: "Strontium chloride"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "hepatic porphyria", "gout", "pseudoachondroplasia", "hepatoportal sclerosis", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension"]
---

# Strontium Chloride
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

# Strontium Chloride: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Strontium chloride is marketed in India as a topical dental gel (Bentoform Dental Gel), but no approved indication text is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **osteoarthritis**, supported by **1 Phase 3 clinical trial** (status unknown) and **no indexed publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the India license data |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.28% |
| Evidence Level | L1 (nominal; see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note: The L1 label comes from the data compiled for this report, but the evidence is weaker than L1 normally implies. Only one Phase 3 trial is registered, its status is unknown, and no verified results are available. By the strict definition (two or more completed Phase 3 RCTs), the evidence would be lower.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for strontium chloride. Based on known information, strontium has dual effects on bone remodeling: it stimulates osteoblast-mediated bone formation and inhibits osteoclast-mediated resorption. It has also been reported to influence chondrocyte activity and cartilage matrix synthesis.

This gives a plausible link to osteoarthritis, a joint disease involving cartilage degeneration and changes in the underlying bone. The mechanism could therefore support structure-modifying or pain-relieving effects.

There are important caveats. The registered trial studied a topical strontium chloride hexahydrate product (2PX), but the registry record has no verified outcome. The available mechanistic reasoning may rely partly on strontium ranelate data, so extrapolating to strontium chloride is unconfirmed. The original indication of the marketed product is also not stated, so the relationship between original and new use cannot be assessed.

Other predictions have much weaker support, with no trials or literature and mechanistic links that appear to be graph artifacts. They are:
- Osteoarthritis susceptibility
- Rheumatoid arthritis
- Hepatic porphyria
- Gout
- Pseudoachondroplasia
- Several rare hepatic and portal conditions

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00954629](https://clinicaltrials.gov/study/NCT00954629) | Phase 3 | Unknown | 300 | 26-week, placebo-controlled, randomised, double-blind study of topical strontium chloride hexahydrate (2PX) for knee osteoarthritis pain. It aims to show superiority over vehicle in reducing pain intensity and improving physical function (2009-06 to 2010-05). No results verified. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 29556 | Bentoform Dental Gel (JK Biochem Healthcare Pvt Ltd) | Dental gel, tube of 50 gm | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

One point from the data is worth noting. Strontium ranelate, a different strontium salt, has been associated with venous thromboembolism risk. Whether this applies to topical strontium chloride is unknown.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single Phase 3 placebo-controlled trial of topical strontium chloride in knee osteoarthritis offers a reasonable signal. However, the trial status is unknown, no results or publications are available, and the mechanistic reasoning is partly extrapolated from another strontium salt. This supports further investigation, not a full "Go".

**To proceed, the following is needed:**
- Retrieve published or registry results for NCT00954629 and confirm its final status
- Confirm the exact salt form and formulation tested in the trial
- Obtain the package insert for Bentoform Dental Gel to clarify its approved indication, warnings and contraindications
- Obtain mechanism of action data for strontium chloride (for example from DrugBank)
- Assess route compatibility between the existing dental gel and a topical osteoarthritis product
- Review the safety profile of topical strontium, including the thromboembolism signal seen with strontium ranelate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

