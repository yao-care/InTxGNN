---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib: From Multiple Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib (Kyprolis®) is an irreversible proteasome inhibitor originally approved for relapsed/refractory multiple myeloma, where it selectively blocks the chymotrypsin-like activity of the 20S proteasome. The TxGNN model predicts it may be effective across multiple **melanoma subtypes** — led by CMM7 (Cutaneous Malignant Melanoma 7) with a prediction score of 99.37% — supported by **5 preclinical publications** demonstrating proteasome inhibition-induced apoptosis in melanoma cell lines. No clinical trials have been registered for any of these melanoma indications, placing the overall evidence at the **L4–L5 (preclinical/model-only)** level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma (relapsed/refractory) |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma 7) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (CMM7-specific) / L4 (melanoma broadly) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, Carfilzomib is a selective, irreversible epoxyketone proteasome inhibitor that covalently binds and inhibits the β5 (chymotrypsin-like) subunit of the 20S proteasome. This causes the accumulation of poly-ubiquitinated proteins, triggering endoplasmic reticulum (ER) stress, activation of the unfolded protein response (UPR), and ultimately caspase-dependent apoptosis — the same mechanism underpinning its efficacy in multiple myeloma.

Melanoma cells share a key vulnerability with myeloma cells: they exhibit high protein synthesis and turnover rates, and frequently overexpress anti-apoptotic proteins such as Mcl-1 and Bcl-2. This creates a theoretical sensitivity to proteasome blockade. Direct in vitro support is provided by PMID 33671902, which showed that Carfilzomib combined with bortezomib synergistically enhanced apoptosis in B16-F1 melanoma cells through simultaneous activation of caspases 3, 8, 9, and 12. Additional computational work (PMID 36134605) identified Carfilzomib as a candidate kinase-targeting agent across multiple cancer types including melanoma.

CMM7 is a genetic locus designation (OMIM) for a melanoma susceptibility gene cluster, representing a genetically defined subtype rather than a distinct clinical disease. The TxGNN model ranks it highest among all five predicted indications (99.37%), but its mechanistic rationale overlaps almost entirely with the broader melanoma category. Among the five melanoma-related predictions in this pack — CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma, and melanoma (general) — only the general melanoma category carries any published evidence, and each subtype has meaningful biological and anatomical differences that would need to be addressed individually before any clinical development is pursued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted melanoma indications (CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma, or melanoma).

---

## Literature Evidence

All available publications are linked to the **melanoma** indication (TxGNN rank 5). No literature was found for the four higher-ranked melanoma subtypes.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical | Biology | Carfilzomib + Bortezomib synergistically induced apoptosis in B16-F1 melanoma cells via caspase 3, 8, 9, and 12 activation; most directly relevant study |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational / in silico | J Biomol Struct Dyn | Molecular docking and dynamics screening of repurposed clinical drugs against 18 cancer kinase targets including melanoma; Carfilzomib identified as a candidate |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Basic science | Mol Cancer Res | AIRAP/AIRAPL proteasome-related gene regulation in human melanoma cell survival; identifies E3-ligase cIAP2 as a mediator of proteasome inhibitor sensitivity in melanoma |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical | Leukemia | BRD4-targeting PROTACs drive proteasomal degradation in myeloma models; provides cross-context evidence for ubiquitin-proteasome pathway exploitation in haematologic malignancy |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical | Matrix Biology | Carfilzomib activates NF-κB to upregulate heparanase in myeloma cells; highlights a potential off-target resistance mechanism relevant to solid tumour translation |

---

## India Market Information

Carfilzomib is **not registered in India**. No marketing authorizations have been issued as of the data cutoff (June 21, 2026). Any future development would require a fresh regulatory submission to CDSCO.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor class).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Irreversible proteasome inhibitor (epoxyketone class); not classical cytotoxic chemotherapy |
| Myelosuppression Risk | High — thrombocytopenia and neutropenia are well-documented; the 227 identified DDIs include multiple agents that augment haematologic toxicity (anabolic steroids, radioactive isotopes, coagulation factor products) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelets (baseline and each cycle), serum creatinine and electrolytes, cardiac function (ECG and echocardiogram — cardiac toxicity is a known class concern), liver function tests |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV formulation requires preparation by trained oncology pharmacy personnel under appropriate containment |

---

## Safety Considerations

**Drug Interactions**: 227 drug-drug interactions identified (DDInter database). Notable interactions include:

- **Major interactions**: Oxandrolone, Oxymetholone, Stanozolol (anabolic steroids — risk of augmented haematologic toxicity); Deferiprone (additive myelosuppression); Samarium (¹⁵³Sm) lexidronam (additive bone marrow suppression); Aminocaproic acid, Von Willebrand Factor Human, Antihemophilic factor (human recombinant), Coagulation factor VIIa (Recombinant Human), Coagulation factor X human, Avatrombopag, Human C1-esterase inhibitor, Conestat alfa (coagulation cascade interference)
- **Moderate interactions**: Metronidazole, Tinidazole (nitroimidazoles); Naltrexone; Rosuvastatin, Simvastatin (statin-related myopathy risk); Palifermin; Strontium chloride Sr-89

Formal prescribing information (warnings, contraindications) was not available in the evidence pack. Please refer to the Kyprolis® SmPC / package insert for the complete safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The four highest-ranked TxGNN predictions (CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma) are all L5 — model prediction only, with zero clinical trials or published literature for these specific subtypes. Even the broadest category (melanoma general, rank 5) reaches only L4 with five preclinical/computational publications, none of which are clinical trials. Compounding this, Carfilzomib carries no India market registration, has 227 documented DDIs (including multiple major interactions with haematologic agents), and has formal safety data unavailable in the current evidence pack — making a risk-benefit assessment impossible at this stage.

**To proceed, the following is needed:**

- Obtain the full Kyprolis® prescribing information / SmPC to populate warnings, contraindications, and dose-adjustment guidance
- Commission a structured literature review for Carfilzomib in solid tumour models, with focus on in vivo melanoma data (xenograft or syngeneic models)
- Evaluate blood-brain barrier penetration data before any consideration of pediatric leptomeningeal melanoma
- Characterise mutation-subtype context (BRAF/NRAS/GNAQ/GNA11 status) to determine whether proteasome inhibition has differential efficacy across melanoma subtypes
- Explore rational combination hypotheses (e.g., Carfilzomib + PD-1/PD-L1 checkpoint inhibitors or BRAF/MEK inhibitors) to build a translatable clinical rationale
- Conduct a regulatory feasibility assessment for India (CDSCO) if evidence matures to support a development programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

