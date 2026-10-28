---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Iohexol: predicted new indication insomnia (disease) (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
monitor_inn: "Iohexol"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Iohexol: From Iodinated Contrast Imaging Agent to insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Iohexol is a non-ionic iodinated radiographic contrast agent that is marketed in India under several brand names. The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials and no supporting publications** exist for this use. The prediction is most likely a computational artifact rather than a real pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (iohexol is used as a radiographic contrast agent) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 6 of 6) |
| Number of Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iohexol is a non-ionic, water-soluble iodinated contrast medium that is cleared by the kidneys. It is used to visualize blood vessels, the spinal canal, joints and other structures during imaging.

Iohexol is pharmacologically inert and has no known activity on sleep-regulating pathways. There is no plausible mechanistic link between a contrast agent and insomnia. The very high TxGNN score (0.9987) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions were also reviewed: anxiety, rheumatoid arthritis, antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, fibromyalgia, conjunctivitis and tendinitis. None has a supporting mechanism or therapeutic evidence. Where literature exists, iohexol appears only as a diagnostic or imaging tool, or as the cause of adverse reactions. It never appears as a treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for insomnia.

For reference, literature retrieved for the second-ranked prediction (anxiety) concerns iohexol only as a contrast agent. It does not support any anxiolytic effect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Double-blind comparison of iodixanol and iohexol in extremity phlebography. This is a contrast agent comparison unrelated to anxiety treatment. |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohort | Neuroradiology | Side effects (headache, nausea, minor mental symptoms such as anxiety) in 200 patients after lumbar iohexol myelography. |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Clinical physiological study | Acta Neurochirurgica | Cerebral haemodynamics monitored with transcranial Doppler during cerebral angiography. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 162067 | Omnipaque 350mg Infusion (Pfizer Ltd) | Bottle of 50 ml infusion | Not available |
| Registration No. 46263 | Contrapaque 300mg Infusion (J B Chemicals and Pharmaceuticals Ltd) | Bottle of 100 ml infusion | Not available |
| Registration No. 36166 | Contrapaque 350mg Infusion (J B Chemicals and Pharmaceuticals Ltd) | Bottle of 100 ml infusion | Not available |
| Registration No. 43072 | Contrapaque 240mg Infusion (J B Chemicals and Pharmaceuticals Ltd) | Bottle of 50 ml infusion | Not available |
| Registration No. 36885 | Contrapaque 300mg Injection (J B Chemicals and Pharmaceuticals Ltd) | Vial of 20 ml injection | Not available |

A sixth registration, Omnipaque 300mg Injection (Pfizer Ltd, Registration No. 162140, 10 ml vial), is also valid. All six registrations are valid single-ingredient products in injectable form.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The main Major-level interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Metformin
  - Amphotericin B, including the lipid complex
  - Aminoglycosides and glycopeptides: kanamycin, neomycin, vancomycin
  - Levofloxacin
  - Bupropion
  - Morphine
  - Metoclopramide
  - Mesalazine and balsalazide
  - Appetite suppressants and cannabinoids: phentermine, diethylpropion, dronabinol

  Mannitol is a Moderate-level interaction.

- **Literature signals (contrast use)**: The retrieved publications describe hypersensitivity reactions requiring desensitization. They also describe a fatal multiorgan dysfunction case after repeated iodinated contrast injection in a patient on low-dose methotrexate.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or supporting publications for insomnia, and no plausible mechanism for an inert contrast agent. The other top predictions also lack therapeutic evidence.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, supported by mechanism of action data from DrugBank
- Preclinical evidence of an effect on sleep-related pathways
- The package insert warnings and contraindications from the India regulatory source, which are needed for safety screening
- Confirmation of the approved indications for the registered products
- Review of route and formulation compatibility. The current products are injectable contrast formulations and may not suit chronic insomnia treatment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

