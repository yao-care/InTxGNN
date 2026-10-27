---
layout: default
title: Doripenem
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Doripenem: predicted new indication Idiopathic copper-associated cirrhosis (evidence level L5). Approved use: Cholecystitis"
monitor_inn: "Doripenem"
predicted_indications: ["idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatic porphyria", "genetic otorhinolaryngological malformation", "juvenile nasopharyngeal angiofibroma (disease)", "neonatal epileptic encephalopathy due to glutaminase deficiency", "familial nasal acilia"]
---

# Doripenem
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

## Doripenem: From Cholecystitis to Idiopathic Copper-Associated Cirrhosis
{: .text-alpha }

## One-Sentence Summary

Doripenem is a carbapenem antibiotic, originally associated with the treatment of cholecystitis, low phospholipid associated cholelithiasis and pyelonephritis.
The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cholecystitis; low phospholipid associated cholelithiasis; pyelonephritis (from the knowledge graph, as the approved indication text in the India licences is empty) |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Doripenem is a carbapenem beta-lactam antibiotic, which acts by inhibiting bacterial cell wall synthesis. Its efficacy in its original indications (biliary and kidney infections) is linked to this antibacterial action.

The predicted new indication does not follow from that mechanism. Idiopathic copper-associated cirrhosis is a disorder of copper metabolism with hepatic copper accumulation, not an infectious process. No plausible mechanistic link between doripenem and this disease has been identified.

The high score (99.00%) is most likely a result of proximity in the knowledge graph, as the original indications (cholecystitis, cholelithiasis) share a hepatobiliary context with the predicted disease. It should be read as a model signal only, not as a biological rationale. The other top-ranked predictions (hepatopulmonary syndrome, hepatoportal sclerosis, portal vein thrombosis, hepatic porphyria and others) show the same pattern: very similar scores, no supporting studies and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Doripenem is marketed in India as a single-ingredient injection with 20 valid registrations and none cancelled. The approved indication text is not available in the data compiled for this report. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 65614 | Dori 500mg Injection | Vial of 1 injection | Medilife Health Sciences Pvt Ltd |
| 69040 | Doriray 500mg Injection | Vial of 1 injection | Mylan Pharmaceuticals Pvt Ltd |
| 112816 | Inarem 250mg Injection | Vial of 1 injection | Emcure Pharmaceuticals Ltd |
| 62869 | Dorilon 500mg Injection | Vial of 1 injection | Zovilon Healthcare Private Limited |
| 70160 | Dpenem 500mg Injection | Vial of 1 injection | Bharat Serums & Vaccines Ltd |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: Clostridium difficile colitis, perinatal necrotizing enterocolitis, impaired renal function disease.
- **Drug Interactions**: Four moderate-level interactions were found: picosulfuric acid, ethinylestradiol, mycophenolic acid and pemetrexed.
- **Class-related concerns**: Carbapenems are known to carry a seizure risk and to interact with valproate. Safety in porphyria would also need separate assessment if hepatic porphyria were pursued.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanistic link between an antibacterial agent and copper-associated cirrhosis. The same holds for the other nine predicted indications reviewed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- A credible biological hypothesis linking doripenem to copper-associated cirrhosis, supported by preclinical or mechanistic studies
- Any clinical or observational evidence in this indication, none of which is currently identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

