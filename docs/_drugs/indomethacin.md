---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From Inflammatory Disease to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Indomethacin is a potent COX-1/COX-2 inhibitor (NSAID) with decades of clinical use in adult inflammatory conditions including arthritis, gout, and ankylosing spondylitis. The TxGNN model identifies **Juvenile Idiopathic Arthritis (JIA)** as the highest-evidence predicted indication among 10 candidates, with **0 registered clinical trials** but **20 supporting publications** — including a double-blind RCT directly comparing indomethacin in juvenile chronic arthritis, giving it an L2 evidence rating and an actionable "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current dataset |
| Predicted New Indication | Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** This is a multi-indication analysis (10 predictions total). Ranks #1–7 are rare genetic skeletal syndromes with no clinical or preclinical evidence (all L5/Hold). Juvenile Idiopathic Arthritis (rank #8) is the highest-evidence actionable indication and is the primary focus of this report.

---

## Why is This Prediction Reasonable?

Indomethacin inhibits both COX-1 and COX-2 enzymes, blocking the conversion of arachidonic acid into prostaglandins. The resulting reduction in prostaglandin E2 (PGE2) suppresses vasodilation, leukocyte recruitment, and the amplification of pro-inflammatory cytokine signals — producing both analgesic and anti-inflammatory effects. Detailed MOA data from DrugBank is currently unavailable (Data Gap DG002), but the pharmacological mechanism is well-established in the literature.

Juvenile Idiopathic Arthritis encompasses several subtypes of chronic inflammatory arthritis in children under 16, characterised by persistent joint inflammation, morning stiffness, and risk of progressive joint destruction. Its pathophysiology is driven by dysregulated immune activation involving IL-1β, IL-6, and TNF-α — all of which rely on prostaglandins as downstream amplifiers of the inflammatory cascade. NSAIDs targeting this prostaglandin axis are therefore first-line symptomatic agents in JIA management.

Historically, indomethacin was among the earliest NSAIDs used in juvenile chronic arthritis (JCA, the predecessor classification to JIA). A 1978 double-blind crossover trial in 30 children confirmed indomethacin as both a safe and effective anti-inflammatory and analgesic in JCA — and found it to be the preferred agent over ketoprofen. Multiple clinical reviews from the 1980s–1990s also list indomethacin alongside aspirin as the established NSAID backbone for systemic JIA fever control. The TxGNN knowledge graph prediction almost certainly reflects this mechanistic and historical connection captured as high-density edges in the drug–disease network.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Indomethacin in Juvenile Idiopathic Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT (double-blind crossover) | South African Medical Journal | Indomethacin vs ketoprofen in 30 children with JCA — both effective; indomethacin emerged as the preferred drug |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Review | Balkan Medical Journal | Comprehensive overview of JIA subtypes, clinical features, and current treatment modalities |
| [22573189](https://pubmed.ncbi.nlm.nih.gov/22573189/) | 2012 | Review | Swiss Medical Weekly | Systemic-onset JIA (Still's disease): orphan disease with chronic course, unique response profile to conventional immunosuppressants |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Clinical Review | Drugs | NSAIDs — including indomethacin — described as the foundation of pharmacotherapy for juvenile rheumatoid arthritis |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | British Journal of Rheumatology | NSAIDs in paediatric rheumatic disease; indomethacin specifically noted for systemic JCA fever control, though more toxic than alternatives |
| [28086918](https://pubmed.ncbi.nlm.nih.gov/28086918/) | 2017 | Observational | Pediatric Rheumatology Online Journal | Atypical monoarthritis presentation in oligoarticular JIA; clinical management context |
| [7417361](https://pubmed.ncbi.nlm.nih.gov/7417361/) | 1980 | Comparative Study | Arthritis and Rheumatism | JRA cohort comparison (USSR vs USA); documents therapeutic practices and NSAID reliance |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Clinical Review | Clinical Pharmacokinetics | Pharmacokinetics of NSAIDs including indomethacin in juvenile arthritis; dosing and clearance considerations |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | Clinical Study | Arzneimittel-Forschung | Long-term indomethacin therapy in juvenile rheumatoid arthritis and Still's disease — early efficacy data |
| [23312448](https://pubmed.ncbi.nlm.nih.gov/23312448/) | 2013 | Basic Research | Cytotherapy | Mesenchymal stromal cells in systemic JIA suppress immune responses; mechanistic context for combination approaches |

---

## India Market Information

Indomethacin has no recorded product registrations in the current dataset (0 licences on file). No approved indication text is available.

---

## Safety Considerations

**Drug Interactions (252 interactions on record; key interactions listed below):**

| Interacting Drug | Level | Clinical Relevance |
|----------------|-------|-------------------|
| Acetylsalicylic acid | Moderate | Concurrent NSAID use significantly increases GI bleeding and ulceration risk |
| Hydrocortisone | Moderate | Corticosteroid + NSAID combination raises GI ulceration risk; monitor closely |
| Dexamethasone | Moderate | As above; particularly relevant in JIA patients on steroid bridges |
| Betamethasone | Moderate | As above |
| Budesonide | Moderate | As above |
| Triamcinolone | Moderate | As above |
| Metformin | Moderate | NSAIDs may reduce renal clearance of metformin via prostaglandin-mediated renal effects |
| Mesalazine | Moderate | Risk of additive renal toxicity; monitor renal function |
| Balsalazide | Moderate | Monitor renal function with concurrent use |
| Glimepiride | Moderate | NSAIDs may potentiate hypoglycaemic effect of sulphonylureas |
| Famotidine | Minor | H2 blockers often co-prescribed for GI mucosal protection with NSAIDs |
| Ranitidine | Minor | As above |
| Cimetidine | Minor | As above |

Complete warnings and contraindications are not available in the current dataset (Data Gap DG001). Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Indomethacin has documented historical clinical use in juvenile chronic arthritis backed by a double-blind RCT and multiple clinical reviews spanning five decades. The COX inhibition → PGE2 reduction → joint inflammation control mechanism directly maps onto JIA pathophysiology. However, current paediatric rheumatology guidelines have shifted towards naproxen, ibuprofen, and diclofenac as preferred first-line NSAIDs due to indomethacin's comparatively higher GI and CNS toxicity burden; biologics (tocilizumab, etanercept) are now standard for refractory disease.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain CDSCO/TFDA package insert to fill DG001 — warnings and contraindications are currently unknown
- **MOA documentation (High):** Query DrugBank API for complete mechanism of action (DG002) to strengthen mechanistic rationale
- **Comparative benefit–risk review:** Head-to-head evidence against currently preferred NSAIDs in JIA (naproxen, ibuprofen, diclofenac) to establish whether indomethacin offers any advantage in specific JIA subtypes (e.g., systemic JIA fever)
- **Paediatric dosing review:** Confirm age-appropriate dosing, weight-based regimens, and paediatric pharmacokinetic data specific to JIA
- **Regulatory pathway assessment:** Evaluate feasibility of India registration for the JIA indication given current market status (not marketed, 0 registrations)
- **Subtype stratification:** Clarify which JIA subtypes (systemic, oligoarticular, polyarticular RF+/RF−) may benefit most, given the mechanistic literature is heterogeneous
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

