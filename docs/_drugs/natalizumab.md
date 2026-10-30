---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 581
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Natalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Crohn's disease, inflammatory bowel disease, Crohn's colitis…"
monitor_inn: "Natalizumab"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Natalizumab: From Crohn's Disease and Multiple Sclerosis to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Natalizumab is a monoclonal antibody originally used to treat Crohn's disease, inflammatory bowel disease and multiple sclerosis.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.
Several other predicted indications (for example psoriasis) have some literature, but it is mostly case reports and shows signals of harm as well as benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, Crohn's colitis, multiple sclerosis (the India license record has no approved indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, natalizumab blocks alpha-4 integrin and limits the movement of white blood cells into inflamed tissue. This is how it helps in multiple sclerosis and Crohn's disease.

A theoretical link to airway inflammation exists, because excessive leukocyte infiltration is a feature of inflammatory lung conditions. However, no clinical or published evidence supports using natalizumab for bronchitis. The high TxGNN score is a model output only.

The safety profile also works against this use. Natalizumab carries a risk of serious infections, including progressive multifocal leukoencephalopathy (PML) and opportunistic infections. Using it for an infection-related or inflammatory airway condition is therefore unfavorable.

### Other Predicted Indications Reviewed

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Bronchitis | 0.9946 | L5 | No trials or literature; theoretical link only |
| Parapsoriasis | 0.9937 | L5 | Only one case report, describing an adverse event, not a benefit |
| Psoriasis | 0.9919 | L4 | Conflicting case reports; one small series reports improvement, others report induced or worsened psoriasis |
| Severe nonproliferative diabetic retinopathy | 0.9918 | L5 | No trials or literature; theoretical link only |
| Acute lichenoid pityriasis | 0.9904 | L5 | Only one case report, describing an adverse event, not a benefit |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (bronchitis), currently no related literature is available.

For comparison, the most relevant publications for the third-ranked prediction (psoriasis) are shown below. None is a randomized trial.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Observational / case series | Neurology(R) Neuroimmunology & Neuroinflammation | 18 MS patients with comorbid psoriasis treated with natalizumab; psoriasis improvement was reported |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case study with review | Case Reports in Neurology | Plaque psoriasis developed during natalizumab treatment; evidence of induction or aggravation is limited to case reports |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case report with review | Neurological Sciences | Arthritic psoriasis during natalizumab treatment |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case report | Dermatology Practical & Conceptual | Natalizumab-induced pustular psoriasis of palms and soles |
| [28765121](https://pubmed.ncbi.nlm.nih.gov/28765121/) | 2018 | Review | Annals of the Rheumatic Diseases | Novel therapies in immune-mediated inflammatory diseases, including psoriasis and Crohn's disease |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Deutsches Ärzteblatt International | Treatment options when MS occurs together with psoriasis, rheumatoid arthritis or inflammatory bowel disease |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacology & Therapeutics | Role of leukocyte integrins in leukocyte recruitment and as therapeutic targets in inflammatory disease |
| [18345706](https://pubmed.ncbi.nlm.nih.gov/18345706/) | 2008 | Review | BioDrugs | Cell adhesion antagonists and their therapeutic potential in asthma and COPD |
| [19647202](https://pubmed.ncbi.nlm.nih.gov/19647202/) | 2009 | Review | The Lancet Oncology | PML associated with rituximab, natalizumab and efalizumab |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Review | The Lancet Neurology | Clinical features and pathogenesis of JC virus disorders, including PML linked to natalizumab |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217331 | Tysabri 300mg Injection (Biogen Idec Biotech India Pvt Ltd) | Vial of 15 ml injection | Not stated in the available record |

---

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: progressive multifocal leukoencephalopathy (PML).
- **Drug Interactions**: 273 interactions were recorded. Major-level interactions include:
  - Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Other immunosuppressive or cytotoxic agents: mercaptopurine, trimetrexate, levamisole
  - Radiopharmaceuticals and radioimmunotherapies: ibritumomab tiuxetan, tositumomab, iobenguane (I-131)
- **Moderate and minor interactions**: naltrexone (moderate); zinc salts (minor).
- **PML and infection risk**: Multiple reviews in the literature link natalizumab with PML, a rare and often fatal brain infection caused by JC virus.

Please refer to the package insert for the full warnings and contraindications, as label-level data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication, bronchitis, rests only on a model score, with no clinical trials or literature, and natalizumab's infection risks (including PML) make this use unfavorable. The other predictions have either no evidence or only case reports, and some of those suggest the drug may cause the condition rather than treat it.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed product (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or clinical evidence in the predicted indication (for example airway inflammation models)
- A benefit-risk comparison against established therapies, such as IL-17, IL-23 and TNF inhibitors for psoriasis
- If psoriasis is pursued, prospective controlled data to resolve the conflicting signals of benefit and harm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

