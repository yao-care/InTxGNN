---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: From Iron Overload to Hepatic Porphyria

## One-Sentence Summary

Deferiprone is an oral iron chelator widely used for transfusional iron overload in patients with hemoglobinopathies, particularly beta-thalassemia.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Transfusional iron overload (beta-thalassemia and other hemoglobinopathies) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Deferiprone is an oral bidentate hydroxypyridinone iron chelator that forms stable 3:1 complexes with iron(III), enabling urinary and fecal excretion of excess iron. It is particularly notable for its superior ability to remove iron from cardiac tissue compared to deferoxamine, making it valuable in preventing iron-induced cardiomyopathy in chronically transfused patients.

The predicted link to hepatic porphyria is mechanistically plausible. In porphyria disorders — particularly Porphyria Cutanea Tarda (PCT) and Congenital Erythropoietic Porphyria (CEP) — free iron acts as a catalyst for reactive oxygen species (ROS) generation, which in turn amplifies the accumulation of phototoxic porphyrin metabolites in the liver and skin. Reducing hepatic iron burden is therefore a recognized therapeutic strategy: phlebotomy (iron depletion) is already a standard treatment for PCT.

Deferiprone's oral iron chelation could theoretically replicate the iron-depleting benefit of phlebotomy for patients who are not candidates for venesection. Animal model studies (PCT mouse model using Hfe⁻/⁻ mice) and a human case series in CEP patients have demonstrated reductions in porphyrin accumulation and improvement in photosensitivity following iron chelation. The mechanistic rationale is considered **moderate** — real but not yet validated in prospective human trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Clinical Case Series / Animal Model | *Blood* | Iron chelation (including deferiprone) rescued hemolytic anemia and skin photosensitivity in CEP patients and mouse models; demonstrates iron-reduction as a therapeutic pathway in erythropoietic porphyria |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal Model (Mouse) | *Hepatology* | In PCT mouse model (Hfe⁻/⁻), deferiprone (L1) reduced hepatic uroporphyrin accumulation comparably to iron-deficient diet, suggesting oral chelation as an alternative to phlebotomy for hepatic iron-driven porphyria |

---

## India Market Information

Deferiprone currently has **no registered products** in India. No authorization records are available.

---

## Safety Considerations

Detailed warnings and contraindications from the product insert are not available in this Evidence Pack. Please refer to the package insert for complete safety information.

**Drug Interactions (246 interactions identified):**

The following moderate-level interactions were identified — all share a common mechanism: Deferiprone's metal-chelating activity is impaired when co-administered with polyvalent cation-containing products, as they competitively bind to the chelator and reduce its systemic availability.

| Interacting Drug | Severity | Clinical Implication |
|-----------------|----------|---------------------|
| Iron (oral supplements) | Moderate | Mutual chelation reduces both efficacy; separate by ≥2 hours |
| Calcium Phosphate / Carbonate / Acetate / Citrate / Gluconate / Lactate / Glubionate | Moderate | Calcium ions bind deferiprone; separate administration by ≥2 hours |
| Magnesium Oxide / Carbonate / Chloride / Citrate / Gluconate / Hydroxide / Sulfate | Moderate | Magnesium ions compete with iron binding; separate by ≥2 hours |
| Aluminum Hydroxide | Moderate | Trivalent aluminum chelated preferentially; reduces iron chelation efficacy |
| Sucralfate | Moderate | Contains aluminum; same mechanism as above |
| Magaldrate / Kaolin / Attapulgite | Moderate | Polyvalent metal antacids; separate by ≥2 hours |

> **Key principle:** All moderate interactions share the same mechanism — polyvalent metal cations competitively occupy the chelation site. The clinical management is consistent: **separate dosing by at least 2 hours**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Deferiprone in hepatic porphyria is scientifically coherent — hepatic iron reduction is an established strategy in PCT and has shown signals of benefit in CEP — but available evidence is limited to animal models and a single case series. No prospective human clinical trials have been registered or completed for this indication, and Deferiprone is not currently marketed in India, meaning there is no local regulatory pathway to build upon.

**To proceed, the following is needed:**

- **MOA data gap closure**: Retrieve full mechanism of action and pharmacological profile from DrugBank (DB08826) to strengthen the mechanistic narrative
- **Package insert safety review**: Download and parse the TFDA/EMA/FDA product insert to complete the Blocking data gap (DG001) on key warnings and contraindications — currently essential for any S1 safety evaluation
- **Porphyria subtype clarification**: Differentiate between PCT (hepatic iron-driven, most likely target), CEP (erythropoietic), and other porphyria subtypes — each has distinct pathophysiology and therapeutic relevance
- **Proof-of-concept human study**: A Phase 2 pilot study in PCT patients ineligible for phlebotomy (e.g., anaemia, poor venous access) would be the logical next step if mechanistic review is supportive
- **Comparator context**: Evaluate against low-dose hydroxychloroquine, which is another established second-line option for PCT, to position Deferiprone's potential niche
- **India-specific regulatory pathway**: Since Deferiprone is not marketed in India, explore whether existing global approvals (EU: Ferriprox; US: FDA-approved) can support a new indication filing via an expedited or orphan disease pathway, given porphyria's rare disease status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

