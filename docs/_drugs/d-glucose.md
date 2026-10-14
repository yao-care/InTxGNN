---
layout: default
title: D-Glucose
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# D-Glucose
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

# D-glucose: From Intravenous Fluid and Nutrient Replacement to Non-syndromic Esophageal Malformation

## One-Sentence Summary

D-glucose (dextrose) is a basic metabolic substrate marketed in India as intravenous infusions, either alone or alongside electrolyte solutions. The TxGNN model ranks **non-syndromic esophageal malformation** as its top predicted new use, but **no clinical trials and no publications** support this prediction. The evidence is model-based only, and the prediction has no identified biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text is blank for all registrations) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 84.11% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. D-glucose is a ubiquitous metabolic substrate and an energy source. It is supplied in India as intravenous dextrose solutions (5%, 10%, 25%) and in combination with sodium chloride or other electrolytes. The data compiled for this report does not state a formal approved indication.

For the top prediction, **no mechanistic link could be identified**. Glucose has no known role in esophageal embryonic development or in correcting esophageal malformation, which is a structural developmental condition. The score comes from graph-based inference alone and has no supporting trials or literature, so it should be treated as a hypothesis-generating signal rather than a therapeutic lead.

The other highly ranked predictions show the same pattern:
- **Primary hereditary glaucoma and open-angle glaucoma**: Literature describes altered glycolysis and lactate metabolism in glaucoma. These are disease biomarkers, not a rationale for giving glucose as treatment.
- **Esophageal disease**: The literature is dominated by 18F-FDG PET imaging, in which a glucose analogue is used for diagnosis, not therapy.
- **Vitamin deficiency disorder**: Studies show that vitamin D status affects glucose metabolism, which is the reverse of the proposed direction.
- **Dermatitis**: An animal study found that 2-deoxy-D-glucose, a glycolysis inhibitor, was beneficial. This points away from glucose supplementation.
- **Biotin metabolic disease, neonatal dermatomyositis, acrodermatitis chronica atrophicans, familial hydroa vacciniforme**: No relevant evidence or plausible link.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication, non-syndromic esophageal malformation.

For reference, three trials were retrieved for the rank-4 prediction, esophageal disease. All were graded as not relevant, because D-glucose is not the studied intervention:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07118176](https://clinicaltrials.gov/study/NCT07118176) | Phase 1 | Active, not recruiting | 30 | 68Ga-FAPI-46 PET imaging tracer biodistribution in cancer patients; no D-glucose involvement |
| [NCT01129206](https://clinicaltrials.gov/study/NCT01129206) | Phase 2 | Completed | 6 | Pralatrexate plus docetaxel chemotherapy in advanced esophageal and gastroesophageal carcinoma |
| [NCT05775939](https://clinicaltrials.gov/study/NCT05775939) | N/A | Recruiting | 20 | PET functional imaging of cardiac radiation damage in lung or esophageal cancer patients |

---

## Literature Evidence

Currently no related literature is available for the top predicted indication. The table below shows the most relevant publications retrieved for lower-ranked predictions. All of them are indirect or diagnostic and do not demonstrate a therapeutic benefit of D-glucose.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41034373](https://pubmed.ncbi.nlm.nih.gov/41034373/) | 2025 | Cohort/Metabolomics | Scientific Reports | Dysregulated glycolytic flux and TCA cycle stalling in plasma of primary open-angle glaucoma patients (open-angle glaucoma) |
| [38355836](https://pubmed.ncbi.nlm.nih.gov/38355836/) | 2024 | Observational | Scientific Reports | Altered lactate metabolic balance in glaucoma, which could raise retinal glucose and glutamate (open-angle glaucoma) |
| [18212745](https://pubmed.ncbi.nlm.nih.gov/18212745/) | 2008 | Meta-analysis | British Journal of Cancer | Compares EUS, CT and FDG-PET for staging oesophageal cancer (esophageal disease) |
| [26271140](https://pubmed.ncbi.nlm.nih.gov/26271140/) | 2015 | Preclinical/Review | Metabolism | Inhibiting tumour energy pathways using the glucose analogue 2-deoxy-D-glucose for esophageal cancer |
| [18187309](https://pubmed.ncbi.nlm.nih.gov/18187309/) | 2008 | Review | Nutrition | Links between vitamin D deficiency and glucose and insulin metabolism (vitamin deficiency disorder) |
| [22673769](https://pubmed.ncbi.nlm.nih.gov/22673769/) | 2012 | Cohort | Nutr Metab Cardiovasc Dis | Vitamin D status and later changes in glucose metabolism in older adults (vitamin deficiency disorder) |
| [31991554](https://pubmed.ncbi.nlm.nih.gov/31991554/) | 2020 | Preclinical (animal) | Biomedicines | 2-deoxy-D-glucose, a glycolysis inhibitor, improved animal models of dermatitis (dermatitis) |

---

## India Market Information

D-glucose has 20 valid registrations in India, all single-ingredient products. The approved indication text is blank for every registration. The five main examples are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 59318 | D5 Infusion | 500 ml bottle, infusion | Not specified |
| Registration No. 72872 | Electrolyte P Infusion | 500 ml bottle, infusion | Not specified |
| Registration No. 7268 | Aculife 25% Infusion | 100 ml bottle, infusion | Not specified |
| Registration No. 58586 | Dextrose 25% Infusion | 100 ml bottle, infusion | Not specified |
| Registration No. 59116 | D 10% Infusion | 500 ml bottle, infusion | Not specified |

All products are injectable or infusion forms.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature, and no identified mechanistic link, so the evidence level is L5 (model prediction only). Across the top ten predictions, the available publications are diagnostic, biomarker-related, or inversely related to the proposed use, and none supports glucose as a therapy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products. Their absence currently blocks safety screening.
- Mechanism of action data for D-glucose.
- A biologically plausible hypothesis linking glucose administration to the predicted condition, with supporting preclinical evidence.
- Approved indication text for the Indian registrations, to define the original indication clearly.
- Evaluation of route compatibility and similarity to the original use, both currently pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

