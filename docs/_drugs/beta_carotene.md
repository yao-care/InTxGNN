---
layout: default
title: Beta Carotene
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Beta Carotene
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

# Beta Carotene: From Vitamin A Precursor to Acne Treatment

## One-Sentence Summary

Beta carotene is a provitamin A carotenoid found naturally in fruits and vegetables, widely used as a dietary supplement and precursor to vitamin A (retinol); it has no formally registered drug indication in India.
The TxGNN model predicts it may be effective for **Acne (Disease)**, with **0 clinical trials** and **7 publications** currently available to support this direction.
The mechanistic rationale is biologically plausible but indirect — retinoid derivatives converted from vitamin A are established acne treatments, yet the conversion efficiency from beta carotene to the active form varies greatly between individuals, and no study has directly tested beta carotene as an acne therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal drug registration in India; used as a dietary supplement / provitamin A precursor |
| Predicted New Indication | Acne (Disease) |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank. Based on established pharmacology, beta carotene is a fat-soluble carotenoid that the body enzymatically cleaves (via BCO1/BCMO1) into retinol (vitamin A) and subsequently into retinoic acid. This conversion pathway is the key to understanding the predicted association with acne.

Retinoids — the active vitamin A derivatives — are among the most effective treatments for acne vulgaris. Isotretinoin (13-cis-retinoic acid) reduces sebaceous gland size and secretion, normalises keratinocyte differentiation within hair follicles, and suppresses *Cutibacterium acnes*–driven inflammation. Topical tretinoin follows similar mechanisms. If beta carotene could serve as a reliable upstream source of these active retinoids, a comparable therapeutic effect in acne might be expected.

The critical limitation is conversion efficiency. The conversion of beta carotene to retinol is tightly regulated and highly variable — BCO1 gene polymorphisms, fat-malabsorption states, and baseline vitamin A status can all reduce conversion by more than an order of magnitude. Current published literature does not include any study that has directly administered beta carotene as a treatment for acne; the existing evidence links oxidant/antioxidant imbalance to acne pathophysiology and documents retinoid use downstream. The TxGNN model likely captures this indirect retinoid pathway, but the mechanistic connection remains inferential at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7618499](https://pubmed.ncbi.nlm.nih.gov/7618499/) | 1995 | Narrative Review | J Am Board Fam Pract | Broad review of vitamins as therapeutic agents; covers retinoid derivatives (vitamin A analogues) in dermatology, including their established role in acne management |
| [20049267](https://pubmed.ncbi.nlm.nih.gov/20049267/) | 2009 | Cross-sectional | Indian J Dermatol | Oxidant/antioxidant imbalance identified in obese adolescent females with acne vulgaris; supports the hypothesis that antioxidant status (including carotenoids) may modulate acne severity |
| [22517509](https://pubmed.ncbi.nlm.nih.gov/22517509/) | 2012 | Clinical Observational | Cell Biochem Funct | Isotretinoin therapy in acne patients induced oxidative toxicity and depleted plasma antioxidant vitamins including beta carotene; highlights the inverse relationship between retinoid treatment and circulating carotenoid levels |
| [2073211](https://pubmed.ncbi.nlm.nih.gov/2073211/) | 1990 | Case Series | Australas J Dermatol | In anorexia nervosa patients, elevated serum beta carotene was observed alongside acne development in a subset; suggests complex relationship between carotenoid accumulation and skin status rather than a clear therapeutic benefit |
| [4230169](https://pubmed.ncbi.nlm.nih.gov/4230169/) | 1967 | Cross-sectional | Dermatol Wochenschr | Early observational study comparing serum vitamin A and beta carotene levels between patients with and without various skin diseases; provides background on carotenoid status in dermatology |
| [39459015](https://pubmed.ncbi.nlm.nih.gov/39459015/) | 2024 | Phytochemical / In vitro | Pharmaceuticals | Chemical characterisation and antibacterial/antioxidant activity of ylang-ylang essential oil for dermatological use; beta carotene cited as one of several bioactive antioxidant components relevant to skin disease |
| [23625436](https://pubmed.ncbi.nlm.nih.gov/23625436/) | 2013 | Phytochemical | Pak J Pharm Sci | Antioxidant and antibacterial characterisation of *Helichrysum oligocephalum*; plant extract noted to contain beta carotene among active components with potential in acne, asthma, and circulatory conditions |

---

## India Market Information

Beta carotene (DB06755) currently has no registered drug products in India. There are no approved authorizations, licenses, or recorded formulations on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction is mechanistically grounded in the vitamin A/retinoid pathway, but the entire evidence base for beta carotene in acne consists of indirect observational studies and mechanistic reviews (Evidence Level L4). No clinical trial has directly evaluated beta carotene supplementation as an acne treatment, and the highly variable conversion efficiency to active retinoids represents a fundamental pharmacological barrier.

**To proceed, the following is needed:**
- A Phase 2 proof-of-concept RCT directly evaluating oral beta carotene supplementation in acne patients, with serum retinol and retinoic acid levels as secondary endpoints
- Mechanistic studies confirming adequate conversion of supplemental beta carotene to retinoic acid in sebaceous gland tissue at standard doses
- Pharmacokinetic characterisation of beta carotene bioavailability and BCO1-mediated conversion across target patient subgroups (including genotyping for common BCO1 polymorphisms)
- MOA data retrieval from DrugBank (data gap DG002) to formally document the retinoid pathway linkage
- Safety data from the package insert (data gap DG001) to allow standard safety screening before clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

