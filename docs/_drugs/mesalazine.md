---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 529
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mesalazine: predicted new indication Congenital hypotrichosis with juvenile macular dystrophy (evidence level L5). Approved use: Ulcerative colitis, inflammatory bowel disease…"
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Mesalazine: From Ulcerative Colitis to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) was originally used to treat ulcerative colitis and other inflammatory bowel conditions.
The TxGNN model predicts it may be effective for **congenital hypotrichosis with juvenile macular dystrophy**, but **no clinical trials and no publications** support this prediction, so it rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease, ulcerative proctosigmoiditis (from the knowledge graph; no approved indication text was available in the licence records) |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mesalazine is an aminosalicylate anti-inflammatory agent. Its efficacy in ulcerative colitis is established, and its activity is generally attributed to reduced prostaglandin and leukotriene synthesis, PPAR-gamma activation and NF-kB modulation.

For this predicted indication, **no credible mechanistic link was identified**. Congenital hypotrichosis with juvenile macular dystrophy is an ultra-rare genetic disorder caused by CDH3 (cadherin-3) mutations that affect hair follicle and retinal development. Mesalazine's anti-inflammatory activity has no plausible connection to this structural defect.

The high TxGNN score reflects proximity in a knowledge graph and is not backed by any trial or publication. It should be treated as a hypothesis only.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Osteoarthritis | 99.63% | L5 | Theoretical anti-inflammatory rationale, but poor systemic absorption limits joint exposure. The only publication is a computational target-identification study, not clinical evidence. |
| 3 | Rheumatoid arthritis | 99.57% | L4 | Indirect rationale via sulfasalazine, which is metabolised to mesalazine. The antirheumatic effect is mainly attributed to sulfapyridine or the intact parent compound, and mesalazine alone has not shown comparable efficacy. |
| 4 | Seborrheic keratosis | 99.50% | L5 | No credible mechanistic link. |
| 5 | Osteoarthritis susceptibility | 99.35% | L5 | A genetic susceptibility phenotype, not an actionable indication. |
| 6 | Vulvar inverted follicular keratosis | 99.33% | L5 | No plausible mechanistic link. |
| 7 | Pseudoachondroplasia | 99.19% | L5 | COMP-mutation skeletal dysplasia, with no link to mesalazine's mechanism. |

Of the seven predictions, rheumatoid arthritis has the most (though still indirect) support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

## India Market Information

All 20 registrations are valid single-ingredient products. The licence records contain no approved indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 184427 | Rowasa 1gm Pellets (Abbott) | Packet of 1 gm pellets | Not stated in records |
| 133634 | Mesacol Tablet DR (Sun Pharmaceutical) | Strip of 15 delayed-release tablets | Not stated in records |
| 174418 | Pentasa 1gm Enema (Ferring) | Bottle of 100 ml enema | Not stated in records |
| 174017 | Pentasa 2gm Prolonged Release Granules (Ferring) | Sachet of 2 gm granules | Not stated in records |
| 133780 | Mesacol Suppository (Sun Pharmaceutical) | Strip of 5 suppositories | Not stated in records |

Available forms include oral tablets, granules and pellets, enemas and suppositories.

## Safety Considerations

- **Kidney and liver conditions:** The knowledge graph links mesalazine to contraindication or caution in kidney disease, interstitial nephritis, lipoid nephrosis, pyoureter, liver disease and gallbladder disease.
- **Blood disorders:** Neutropenia, agranulocytosis, anaemia and macrocytic anaemia are listed. These are knowledge-graph relationships, not label text.
- **Pyloric stenosis:** Also listed in the knowledge graph.
- **Drug interactions:** 291 interactions were identified. Major ones include cidofovir and human botulinum neurotoxin A/B immune globulin. Moderate ones include NSAIDs (ketorolac, ibuprofen, celecoxib, bromfenac), azathioprine, aminoglycosides (amikacin), amphotericin B formulations, acyclovir, cisplatin, capreomycin and sulfonylureas (chlorpropamide, acetohexamide). Many of these relate to additive kidney toxicity.
- **Reported adverse reactions in the literature:** Published case reports describe 5-ASA-induced colitis and DRESS syndrome with acute renal failure after mesalazine exposure.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests only on a graph-based score. It has no clinical trials or publications and no plausible mechanistic link to mesalazine's anti-inflammatory action. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For the top prediction, a mechanistic rationale linking mesalazine to CDH3-related pathology, plus any preclinical evidence
- If a more actionable direction is wanted, re-prioritise rheumatoid arthritis (L4) and review direct evidence for mesalazine, as opposed to sulfasalazine, in that condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

