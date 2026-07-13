---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From Anti-inflammatory / Pain to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a well-established non-steroidal anti-inflammatory drug (NSAID) widely used for pain relief and inflammatory conditions, acting principally through inhibition of the COX-1 and COX-2 enzymes to suppress prostaglandin synthesis.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The evidence base consists entirely of computational prediction (Evidence Level L5), and the mechanistic rationale is highly indirect, warranting a **Hold** recommendation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NSAID / anti-inflammatory and analgesic use (no India regulatory registration on file) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this evidence pack. Based on widely accepted pharmacology, Diclofenac is a non-selective COX-1/COX-2 inhibitor that suppresses the arachidonic acid cascade, reducing the synthesis of prostaglandins — notably PGE2 and PGD2. Its efficacy across pain, inflammation, and musculoskeletal conditions has been extensively documented in clinical practice.

The proposed mechanistic link to hypotrichosis simplex of the scalp rests on the role of the prostaglandin axis in hair follicle biology. PGD2 is known to inhibit hair follicle cycling (acting through DP2/CRTH2 receptors), while PGE2 is thought to promote hair growth. Theoretically, COX inhibition by Diclofenac could shift the PGD2/PGE2 balance toward growth-promoting signalling in the scalp microenvironment.

However, hypotrichosis simplex of the scalp is primarily a hereditary structural disorder driven by mutations in genes such as *LPAR6*, *LIPH*, and *CDSN* — genes governing lipid metabolism and corneodesmosome integrity in the hair follicle. Inflammatory prostaglandin signalling is not the principal pathological mechanism. The mechanistic connection between systemic COX inhibition and the correction of a genetic hair follicle structural defect is therefore extremely weak, and this TxGNN prediction most likely reflects a loose pathway co-occurrence in the knowledge graph rather than a therapeutically actionable relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Diclofenac has **641 documented drug interactions**. Key interactions of clinical significance are listed below:

| Severity | Interacting Drug | Clinical Relevance |
|----------|-----------------|-------------------|
| Moderate | Hydrocortisone | Combined use increases risk of gastrointestinal adverse effects (ulceration, bleeding) |
| Moderate | Dexamethasone | Combined use increases GI risk; monitor for GI symptoms |
| Moderate | Betamethasone | Additive GI mucosal risk with concurrent corticosteroid |
| Moderate | Budesonide | Additive GI mucosal risk with concurrent corticosteroid |
| Moderate | Triamcinolone | Additive GI mucosal risk with concurrent corticosteroid |
| Moderate | Acetylsalicylic acid | May reduce cardioprotective effect of aspirin; increases GI bleeding risk |
| Moderate | Metformin | NSAIDs may impair renal function, reducing metformin clearance and increasing lactic acidosis risk |
| Moderate | Glimepiride | NSAIDs may potentiate hypoglycaemic effect of sulfonylureas |
| Moderate | Glipizide | NSAIDs may potentiate hypoglycaemic effect of sulfonylureas |
| Moderate | Mesalazine | Potential additive nephrotoxicity; renal monitoring advised |
| Moderate | Balsalazide | Potential additive nephrotoxicity |
| Moderate | Aprepitant | Possible pharmacokinetic interaction via CYP3A4 modulation |
| Minor | Famotidine | Minor interaction; generally well tolerated |
| Minor | Ranitidine | Minor interaction; generally well tolerated |
| Minor | Cimetidine | May slightly increase diclofenac plasma concentrations |

Please refer to the package insert for complete key warnings and contraindications, which were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (99.69%), hypotrichosis simplex of the scalp is a genetically determined structural hair disorder for which COX/prostaglandin inhibition has no established or direct pathological relevance; no clinical trial or published literature evidence exists to support this repurposing direction.

**To proceed, the following is needed:**
- Preclinical validation (cell or animal model) demonstrating any phenotypic effect of Diclofenac or COX inhibition on hair follicle structural defects caused by *LPAR6*, *LIPH*, or *CDSN* mutations
- Mechanistic studies clarifying whether prostaglandin pathway modulation can compensate for lipid metabolism or corneodesmosome defects in affected follicles
- India (CDSCO) package insert to complete the safety assessment for key warnings and contraindications (currently a blocking data gap)
- Consideration of whether a more clinically proximate TxGNN-predicted indication — such as juvenile idiopathic arthritis (Rank 9, L4 evidence, NSAIDs are ACR/EULAR first-line) — represents a higher-priority repurposing candidate for this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

