---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Aflibercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aflibercept: From Neovascular Ocular Disease to Esotropia

## One-Sentence Summary

Aflibercept (Eylea) is a recombinant anti-VEGF fusion protein approved globally for neovascular (wet) age-related macular degeneration, diabetic macular edema, and retinal vein occlusion, with an IV formulation (Zaltrap) also approved for metastatic colorectal cancer.
The TxGNN model predicts it may be relevant to **Esotropia** with a prediction score of **99.38%**,
however **no supporting clinical trials or publications** were identified across all 10 predicted indications — the current evidence base is **Level L5** (model inference only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular (wet) AMD, diabetic macular edema, retinal vein occlusion (global approvals; no India registration on record) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Aflibercept is a recombinant fusion protein that functions as a "VEGF trap" — it binds VEGF-A, VEGF-B, and placental growth factor (PlGF) with high affinity, preventing their interaction with endogenous VEGF receptors. This suppresses pathological angiogenesis and vascular permeability, which is the basis for its established use in retinal neovascular diseases.

Regarding the esotropia prediction specifically: VEGF signaling participates in ocular neurovascular development, which gives Aflibercept and esotropia shared nodes in the ophthalmology subgraph of the TxGNN knowledge graph. However, the mechanistic logic here is inverted — published observational data suggests that anti-VEGF treatment in premature infants (e.g., for retinopathy of prematurity) is *associated with a higher incidence* of esotropia, positioning it as a potential adverse effect rather than a therapeutic target. The TxGNN model's high score is most likely driven by topological proximity within the ophthalmic disease cluster, not a true therapeutic relationship.

This is a recognized limitation of graph neural network-based prediction: high connectivity within a disease domain can inflate scores for conditions that share anatomical or biological context without implying a treatment benefit. For this reason, no further development of the esotropia indication is warranted at this stage.

---

## All 10 Predicted Indications — Overview

The following table summarizes all TxGNN predictions included in this evidence pack:

| Rank | Disease | Score | Evidence Level | Decision | Mechanistic Assessment |
|------|---------|-------|----------------|----------|----------------------|
| 1 | Esotropia | 99.38% | L5 | Hold | Likely adverse-effect artifact; esotropia rate increased by anti-VEGF treatment |
| 2 | Esophageal varices without bleeding | 97.56% | L5 | Hold | Theoretical: portal hypertension drives VEGF-mediated collateral angiogenesis; no preclinical validation |
| 3 | Esophageal varices with bleeding | 97.56% | L5 | Hold | Same as above; acute hemorrhage adds hemostatic safety concern |
| 4 | Varicose disease | 96.95% | L5 | Hold | VEGF linked to venous wall remodeling, but core pathology is mechanical; indirect link |
| 5 | Urethral calculus | 95.97% | L5 | Hold | No credible mechanistic link to VEGF; assessed as graph artifact |
| 6 | Adenosine deaminase deficiency | 95.76% | L5 | Hold | No mechanistic link; assessed as knowledge-graph false positive |
| 7 | Hemorrhagic disease of newborn | 95.56% | L5 | Hold | Pathology is vitamin K-dependent; anti-VEGF may worsen bleeding tendency — safety concern |
| 8 | Ectomesenchymoma | 94.52% | L5 | Research Question | Rare malignancy; VEGF overexpression in soft tissue tumors plausible; class-extension hypothesis |
| 9 | Malignant cutaneous granular cell skin tumor | 94.51% | L5 | Hold | Schwann cell origin; VEGF as driver is weakly supported |
| 10 | Middle ear neuroendocrine tumor | 94.42% | L5 | Research Question | NETs are typically hypervascular; anti-angiogenic class-extension hypothesis reasonable |

---

## Clinical Trial Evidence

No clinical trials were identified for the top-ranked indication (esotropia) or for 8 of the 10 predicted indications.

One trial was retrieved under "Hemorrhagic Disease of Newborn" but is **not relevant**:

| Trial Number | Phase | Status | Enrollment | Assessment |
|-------------|-------|--------|------------|------------|
| [NCT02537054](https://clinicaltrials.gov/study/NCT02537054) | Phase 2 | Completed | 15 | Study of intravitreal Aflibercept for choroidal neovascularization in pseudoxanthoma elasticum — an ophthalmic disease entirely unrelated to neonatal hemorrhagic disease. Retrieval is a classification error; does not support the predicted indication. |

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## India Market Information

Aflibercept currently has **no registered products** in India. No authorization numbers, brand names, dosage forms, or approved indications are on record.

---

## Cytotoxicity

Aflibercept meets criteria for inclusion of this section: one of its approved global formulations (ziv-aflibercept / Zaltrap) is indicated for metastatic colorectal cancer, and its anti-angiogenic mechanism is shared with multiple recognized antineoplastic agents. Several predicted indications in this report also involve malignant conditions.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Anti-angiogenic (VEGF inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low for intravitreal (ophthalmic) use; Moderate for IV oncology formulation (ziv-aflibercept) — neutropenia reported |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure, proteinuria, wound healing, arterial thromboembolic events (IV use); intraocular pressure, endophthalmitis risk (intravitreal use) |
| Handling Protection | Standard biological agent precautions; cytotoxic drug handling regulations apply to IV oncology formulation |

---

## Safety Considerations

**Drug Interactions:** 78 interactions identified. Major interactions include:

| Interacting Drug | Severity |
|-----------------|----------|
| Deferiprone | Major |
| Adalimumab | Major |
| Baricitinib | Major |
| Certolizumab pegol | Major |
| Cladribine | Major |
| Clozapine | Major |
| Samarium (153Sm) lexidronam | Major |
| Roflumilast | Moderate |
| Chloramphenicol / Chloramphenicol (ophthalmic) | Moderate |
| Zidovudine | Moderate |
| Azathioprine | Moderate |
| Anakinra | Moderate |
| Alemtuzumab | Moderate |
| Alefacept | Moderate |
| Canakinumab | Moderate |

> The high number of Major-level interactions predominantly involving immunosuppressants and biological agents reflects Aflibercept's immunomodulatory profile and the additive risk of infection or immunosuppression when combined with these agents.

Full key warnings and contraindications are not available in this Evidence Pack. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are Evidence Level L5 — model inference with no supporting clinical trials or published literature. The highest-ranked prediction (esotropia, 99.38%) is likely a knowledge-graph artifact: the mechanistic evidence suggests esotropia is an *adverse consequence* of anti-VEGF therapy in premature infants, not a therapeutic target. The remaining predictions either lack plausible mechanistic links (urethral calculus, ADA deficiency) or carry active safety concerns (hemorrhagic disease of newborn, esophageal varices with bleeding). Two indications (ectomesenchymoma and middle ear neuroendocrine tumor) have theoretical anti-angiogenic rationale and merit further exploratory investigation but not drug development at this stage.

**To proceed, the following is needed:**

- **Regulatory data gap (Blocking):** Obtain the full package insert (EMA/FDA/CDSCO) to document approved indications, key warnings, and contraindications — required before any safety evaluation can proceed
- **MOA gap (High):** Retrieve complete mechanism of action data from DrugBank API (DB08885) to enable proper mechanistic-link analysis
- **For esotropia (Rank 1):** Conduct targeted literature review of anti-VEGF-associated esotropia to formally classify this as an adverse effect and close out this prediction
- **For ectomesenchymoma and middle ear NET (Research Question):** Perform targeted PubMed search for anti-VEGF / anti-angiogenic therapy in soft tissue sarcomas and ear NETs; obtain tumor VEGF expression data from case reports or pathology registries
- **India market assessment:** Evaluate pathway for Aflibercept introduction in India if any indication advances to a higher evidence level — currently no registered formulation exists
- **Interaction risk review:** Clinical pharmacist review of the 7 Major-level DDIs is recommended before any prospective use in patients on immunosuppressive regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

