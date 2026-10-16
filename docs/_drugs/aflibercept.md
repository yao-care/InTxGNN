---
layout: default
title: Aflibercept
parent: Model Prediction Only (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aflibercept: predicted new indication Esotropia (evidence level L5). Approved use: Metastasis from malignant tumor of colon"
monitor_inn: "Aflibercept"
predicted_indications: ["esotropia", "esophageal varices without bleeding", "esophageal varices with bleeding", "varicose disease", "urethral calculus", "adenosine deaminase deficiency", "hemorrhagic disease of newborn", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "middle ear neuroendocrine tumor"]
---

# Aflibercept
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

# Aflibercept: From Metastatic Colon Cancer and Retinal Disease to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF-A/VEGF-B/PlGF trap, originally used for metastatic colorectal cancer and retinal vascular diseases such as macular degeneration, retinal artery occlusion and diabetic macular edema.
The TxGNN model predicts it may be effective for **esotropia**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastasis from malignant tumor of colon; macular degeneration; retinal artery occlusion; diabetic macular edema (from the knowledge graph; the approved indication text in the India license is blank) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, aflibercept is a recombinant fusion protein that traps VEGF-A, VEGF-B and placental growth factor (PlGF). Its efficacy in neovascular and edematous retinal disease, and in metastatic colorectal cancer, rests on blocking VEGF-driven angiogenesis and vascular permeability.

Esotropia is an ocular motor alignment disorder (inward deviation of the eye). No plausible direct mechanism links VEGF blockade to it. The very high TxGNN score (0.994) is a model prediction, probably reflecting the drug's many ocular associations in the knowledge graph rather than a true therapeutic signal. The prediction should be treated as a hypothesis only.

Other predictions for this drug are also unsupported. These include esophageal varices (a theoretical link via VEGF-driven portal hypertension), varicose disease, and several rare tumours (a generic anti-angiogenic rationale). All have no trials or literature. For hemorrhagic disease of the newborn, the one linked trial (NCT02537054) studies choroidal neovascularization and is a spurious match.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for esotropia.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 72924 | Eylea 40mg/ml Injection (Bayer Zydus Pharma Pvt Ltd) | Vial of 1 ml injection | Not stated in the available record |

---

## Safety Considerations

- **Drug Interactions**: 78 interactions were identified. Major-level interactions listed include deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine and clozapine. Moderate-level interactions include strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab and several vaccines (tetanus toxoid, anthrax, live cholera).
- **Bleeding risk**: Aflibercept carries a bleeding and hemorrhage warning, which is a particular concern for any predicted indication involving active bleeding (for example, bleeding esophageal varices).

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). No clinical trials or publications support it, and there is no plausible mechanism linking VEGF blockade to esotropia. The same holds for the other nine predicted indications, which should not advance on the current evidence.

**To proceed, the following is needed:**
- Mechanism of action data for aflibercept (for example, from DrugBank), to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from the India Pharma source, which are required before safety screening
- Preclinical or mechanistic evidence for VEGF involvement in esotropia or extraocular muscle disease
- Route compatibility assessment, since the only available form is an intravitreal/injectable vial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

