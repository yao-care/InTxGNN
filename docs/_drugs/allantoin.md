---
layout: default
title: Allantoin
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 8
---

# Allantoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Allantoin: From Topical Wound Healing to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Allantoin is a naturally occurring compound widely used as a topical skin-conditioning and wound-healing agent in dermatological and cosmetic products, with no formally registered drug indication in India.

The TxGNN model has generated **8 novel indication predictions** across a range of dermatological and systemic diseases, with the top-ranked prediction being **Severe Nonproliferative Diabetic Retinopathy** (score: 99.56%). Among all predictions, **Acne Keloid** (rank 4) demonstrates the strongest mechanistic rationale, and **Exanthem** (rank 8) is the only indication with any supporting clinical trial data — **3 studies**, all providing indirect evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered drug indication (used as topical skin-conditioning agent) |
| Top Predicted Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 (top prediction) / L4 (Exanthem, rank 8) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (most indications) / Research Question (Acne Keloid, Exanthem) |

---

## Multi-Indication Prediction Overview

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------------|-------------|----------------|----------------|
| 1 | Severe Nonproliferative Diabetic Retinopathy | 99.56% | L5 | Hold |
| 2 | Acrodermatitis Chronica Atrophicans | 99.50% | L5 | Hold |
| 3 | Neonatal Dermatomyositis | 99.48% | L5 | Hold |
| 4 | Acne Keloid | 99.48% | L5 | Research Question |
| 5 | Secondary ILD (Childhood, CTD-associated) | 99.44% | L5 | Hold |
| 6 | Amyopathic Dermatomyositis | 99.43% | L5 | Hold |
| 7 | Hydroa Vacciniforme, Familial | 99.23% | L5 | Hold |
| 8 | Exanthem (Disease) | 99.10% | L4 | Research Question |

---

## Why Are These Predictions Reasonable?

Detailed mechanism of action data for Allantoin is not currently available in this Evidence Pack. Based on its well-established use in dermatological products, Allantoin is known to promote epithelial cell regeneration, exert keratolytic and anti-inflammatory effects, and strengthen the skin barrier. It is a metabolite of purine catabolism found naturally in many organisms and has been incorporated into scar-management, wound-healing, and moisturizing formulations for decades.

**Mechanistic plausibility varies considerably across the 8 predictions:**

- **Acne Keloid (Rank 4) — Strongest link.** Allantoin's keratolytic action can soften fibrotic scar tissue; its anti-inflammatory properties reduce the inflammation-driven fibrosis underlying keloid formation; and it may modulate abnormal fibroblast activity. It is already an active ingredient in commercially available scar-management products (e.g., Contractubex). This is the most biologically plausible repurposing candidate in this cohort.

- **Exanthem (Rank 8) — Moderate link.** Exanthem is a broad category of skin eruptions. Allantoin's anti-inflammatory and barrier-restoration properties support its use as a topical adjunct for symptomatic skin rash management. Three clinical trials — albeit indirect — provide minimal safety context for this route of administration.

- **Acrodermatitis Chronica Atrophicans (Rank 2) and Amyopathic Dermatomyositis (Rank 6) — Weak link.** These are autoimmune or infectious-origin skin diseases. Allantoin could offer adjunctive relief on skin lesions, but it cannot address the root pathology (Borrelia infection or autoimmune-mediated inflammation).

- **Severe Nonproliferative Diabetic Retinopathy (Rank 1), Neonatal Dermatomyositis (Rank 3), Secondary ILD-CTD (Rank 5), Hydroa Vacciniforme Familial (Rank 7) — Very weak or no link.** These are systemic or non-dermatological conditions. Allantoin's topical pharmacology has no credible therapeutic pathway to the retina, lung, or immune system. The KG model likely connected these through shared oxidative stress or inflammatory graph nodes, which does not constitute meaningful clinical evidence.

---

## Clinical Trial Evidence

*Only the Exanthem (Rank 8) indication has associated clinical trial data. No trials were identified for any other predicted indication.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT06122467](https://clinicaltrials.gov/study/NCT06122467) | NA | Completed | 36 | 12-week single-arm study evaluating an Allantoin-containing cosmetic product line for acne symptoms; no control group, Allantoin effect cannot be isolated from other ingredients |
| [NCT02241005](https://clinicaltrials.gov/study/NCT02241005) | NA | Completed | 159 | RCT of Theraworx bath wipes (Allantoin-containing) to reduce VRE skin colonization in pediatric HSCT patients; primary endpoint was infection prevention, not exanthem treatment |
| [NCT04101890](https://clinicaltrials.gov/study/NCT04101890) | Phase 4 | Terminated | 5 | Theraworx foam for prevention and treatment of diaper dermatitis in infants; terminated early with only 5 participants enrolled — no valid conclusions can be drawn |

> **Important caveat:** All three trials are indirect (Grade C relevance). None evaluated Allantoin as a monotherapy for exanthem, and all involve multi-ingredient formulations. These trials provide limited safety context for topical Allantoin use, not efficacy evidence for the predicted indication.

---

## Literature Evidence

Currently no related literature is available for any of the 8 predicted indications based on the Evidence Pack queries.

---

## India Market Information

Allantoin is **not currently marketed in India** as a registered drug product. No drug authorizations have been identified in the regulatory database.

| Status | Detail |
|--------|--------|
| Registered Drug Products | None |
| Total Licenses | 0 |
| Market Status | Not Marketed |

> Allantoin may be present as an excipient or active ingredient in cosmetic and OTC skin-care products in India, which are not captured by the drug regulatory database. Its regulatory classification as a pharmaceutical agent would need to be established before any development pathway is pursued.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug-drug interaction data, key warnings, or contraindication data were identified in this Evidence Pack. Allantoin has a long history of safe topical use in cosmetic and dermatological formulations, and its general tolerability via this route is well-established. However, formal pharmacological safety data for any systemic or non-topical route of administration is not currently available and would need to be generated if novel routes are considered.

---

## Conclusion and Next Steps

**Decision: Hold** (Ranks 1–3, 5–7) / **Research Question** (Rank 4: Acne Keloid; Rank 8: Exanthem)

**Rationale:**

The TxGNN model has generated high-scoring predictions for Allantoin, but the vast majority of these reflect the limitations of graph-based inference rather than genuine clinical opportunity. The top-ranked prediction (Severe Nonproliferative Diabetic Retinopathy) lacks both mechanistic plausibility and any clinical evidence — this is a likely false positive arising from shared oxidative stress nodes in the knowledge graph. The only indication with meaningful biological rationale is **Acne Keloid** (rank 4), where Allantoin's existing use in scar-management products already provides indirect real-world validation. **Exanthem** (rank 8) has the only clinical trial data, but all three studies are indirect, low-quality, and insufficient to support formal repurposing claims.

**To proceed with Research Question indications, the following is needed:**

- **Complete MOA data for Allantoin**: Retrieve full mechanism of action from DrugBank API to strengthen or refute mechanistic links across all 8 predictions (identified data gap DG002)
- **Acne Keloid targeted literature review**: Conduct a systematic PubMed search for Allantoin in keloid and hypertrophic scar management; evaluate whether existing scar products can anchor a drug-level indication claim
- **Exanthem evidence upgrade**: Search for published clinical or mechanistic studies in which Allantoin is evaluated as a standalone ingredient for skin inflammation or rash management
- **Route compatibility assessment**: Formally confirm that topical Allantoin can reach target tissue for each indication — systemic indications (retinopathy, lung disease) are almost certainly inaccessible via available routes
- **India regulatory classification**: Determine whether Allantoin requires new drug approval or can proceed under an existing OTC or cosmeceutical framework in India before any development pathway is initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

