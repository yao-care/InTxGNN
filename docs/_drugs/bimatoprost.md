---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma / Ocular Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component

---

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analog originally approved for reducing intraocular pressure in open-angle glaucoma and ocular hypertension, and subsequently for promoting eyelash growth (hypotrichosis).
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**,
with **0 clinical trials** and **20 publications** currently retrieved — however, all retrieved literature consists of general periodontology papers and none directly addresses bimatoprost in this context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (based on known pharmacology; India regulatory data unavailable) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Bimatoprost is a synthetic prostaglandin F2α (prostamide) analog that reduces intraocular pressure by increasing uveoscleral and trabecular outflow of aqueous humor. It is approved as an ophthalmic solution for glaucoma (Lumigan™) and as a cosmetic eyelash-enhancing agent (Latisse™), the latter leveraging its hair follicle-stimulating properties by extending the anagen phase of the hair cycle.

Prostaglandins and their analogs are known to participate in bone remodeling and inflammatory signaling — both relevant biological pathways in periodontal disease. Specifically, prostaglandin E2 (PGE2) and related prostanoids are implicated in alveolar bone resorption and periodontal ligament inflammation. It is conceivable that a prostamide analog such as bimatoprost could modulate prostaglandin receptor activity in periodontal tissues, potentially influencing tissue homeostasis or malformation-related defects in the odontal-periodontal complex.

However, this mechanistic extrapolation is entirely hypothetical at this stage. The TxGNN model's high prediction score likely reflects graph-based proximity in the knowledge graph between prostanoid signaling nodes and periodontal disease nodes — not established clinical or preclinical evidence. The 20 retrieved PubMed publications are standard periodontology references (guidelines, reviews, observational studies) with no mention of bimatoprost, confirming the absence of a direct evidence chain. This prediction warrants mechanistic investigation before any development resources are committed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bimatoprost in malformation syndrome with odontal and/or periodontal component.

---

## Literature Evidence

The following publications were retrieved for the combined query of Bimatoprost and periodontal/odontal malformation. **Important note:** None of these publications directly address bimatoprost; they represent general periodontology literature returned by the evidence pipeline. They are listed here for context on the target disease landscape.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guideline | J Clin Periodontology | EFP S3-level clinical practice guideline for Stage IV periodontitis — covers severity, functional sequelae, and treatment recommendations |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane Database | Periodontal treatment for glycaemic control in diabetes; evidence for bidirectional relationship between periodontitis and metabolic disease |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Systematic Review | Cochrane Database | Supportive periodontal therapy (SPT) reduces re-infection risk and maintains dentition following active treatment |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontology 2000 | Obstructive sleep apnea identified as emerging risk factor for periodontal health |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy as a novel direction in periodontitis treatment |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Cohort Study | J Dental Research | Periodontal therapy reduces oral-gut microbial dysbiosis in Stage III/IV periodontitis patients |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | Complications and treatment errors in regenerative periodontal surgery |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dental Research | Gingival fibroblasts act as innate immune sentinels in periodontitis pathogenesis |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Diabetes approximately triples susceptibility to periodontitis; two-way relationship well established |
| [20599785](https://pubmed.ncbi.nlm.nih.gov/20599785/) | 2010 | Review | Biochemical Pharmacology | Complement system overactivation linked to periodontal immunopathology — potential target for anti-inflammatory intervention |

---

## India Market Information

Bimatoprost is currently **not marketed in India**. No regulatory authorizations have been identified in the India drug registry. The drug is approved in other jurisdictions (e.g., US FDA approval for Lumigan™ and Latisse™; EU/EMA approval), meaning international reference data may be consulted for regulatory strategy, but a full India CDSCO registration process would be required.

---

## Safety Considerations

**Drug Interactions:** A total of **66 drug-drug interactions** have been identified via the DDinter database. All are currently classified as **Unknown** severity, indicating that interaction magnitudes are not yet quantified. Notable interacting drugs include:

- Metformin, Rosiglitazone (antidiabetics)
- Simvastatin (lipid-lowering)
- Prednisone, Prednisolone, Triamcinolone (corticosteroids)
- Morphine, Loperamide (opioid/opioid-related)
- Ondansetron, Palonosetron, Dolasetron (5-HT3 antagonists)
- Vancomycin (antibiotic)
- Omeprazole, Lansoprazole, Pantoprazole (proton pump inhibitors)

The clinical significance of these interactions in a topical or systemic repurposing context for periodontal disease would require dedicated pharmacovigilance review.

For key warnings and contraindications, please refer to the package insert, as these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN model prediction score (99.999%), there is no direct preclinical or clinical evidence linking bimatoprost to malformation syndromes involving odontal and/or periodontal tissues. All 20 retrieved publications are general periodontology literature with no mention of bimatoprost. The mechanistic rationale — based on prostanoid signaling in bone and periodontal inflammation — is biologically plausible but entirely speculative at this stage.

**To proceed, the following is needed:**

- **Mechanism of action verification:** Confirm whether bimatoprost's prostamide receptor activity (FP receptors, prostamide receptors) is expressed in periodontal ligament, gingival fibroblasts, or alveolar bone cells
- **Preclinical proof-of-concept:** In vitro or animal studies testing bimatoprost on periodontal tissue models or odontal malformation-related cell lines
- **Safety data:** Retrieve full package insert for Lumigan™/Latisse™ to document contraindications, key warnings, and systemic exposure risks
- **Drug interaction clarification:** Evaluate the 66 DDinter interactions of "Unknown" severity to identify any clinically significant risks in the target patient population
- **India regulatory pathway:** Assess CDSCO requirements for a new drug with zero existing India market presence — including whether a new drug application (NDA) or bridging studies would be required
- **Literature gap analysis:** Commission a systematic literature search specifically combining bimatoprost with prostaglandin receptor signaling in periodontal tissue to determine whether any indirect mechanistic evidence exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

