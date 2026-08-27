---
layout: default
title: Climbazole
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Climbazole
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

Using judgment on data selection: among the 10 TxGNN-predicted indications, only rank #3 ("dermatitis," specifically evidenced as seborrheic dermatitis) has actual clinical/literature support (L2, decision stage S2, "Proceed with Guardrails"). The nominal top-scored candidate (rank #1, "acne keloid") and 7 others are explicitly flagged in the evidence pack's own rationale as zero-evidence "model noise" with Hold recommendations. I built the report around the only substantiated candidate rather than the raw highest-score entry, and noted this explicitly for transparency.

---

# Climbazole: From Topical Antifungal (Anti-Dandruff) Use to Dermatitis (Seborrheic Dermatitis)

## One-Sentence Summary

> Climbazole is an imidazole antifungal agent long used as an active ingredient in anti-dandruff shampoos and topical antifungal creams, though it holds no formal drug marketing authorization in India (0 registrations, "Not Marketed" status).
> Among 10 TxGNN-predicted indications, only **Dermatitis (specifically Seborrheic Dermatitis)** is backed by real-world evidence — the model's higher-scoring candidates (e.g., acne keloid, amyopathic dermatomyositis) returned **zero clinical trials and zero literature hits** and are annotated in the evidence pack itself as likely embedding artifacts.
> For Dermatitis, there are currently **0 registered clinical trials** but **14 relevant publications**, including 3 RCTs directly testing climbazole-containing shampoos/creams against seborrheic dermatitis and dandruff.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in India/Taiwan; internationally marketed as a topical antifungal active in anti-dandruff shampoos and antimycotic creams |
| Predicted New Indication | Dermatitis (evidence specifically supports the seborrheic dermatitis subtype) |
| TxGNN Prediction Score | 95.05% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's single highest-scoring prediction ("acne keloid," 95.32%) and several others (amyopathic dermatomyositis, neonatal dermatomyositis, newborn respiratory distress syndrome, etc.) returned zero clinical trials and zero literature across all queried sources, and are explicitly flagged in the model rationale as mechanistically implausible or likely model noise (all scored L5/Hold). This report instead focuses on the one candidate with real supporting evidence.

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data for climbazole was not available in this evidence pack (flagged as a Blocking/High-severity data gap — see Conclusion). Based on the supporting literature and repurposing rationale collected, climbazole is an **imidazole-class antifungal** that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol biosynthesis in the fungal cell membrane. This is the same mechanism shared by other topical azole antifungals.

Its established, long-standing use is in anti-dandruff shampoos and scalp/skin antifungal products, where it suppresses *Malassezia* species (*M. furfur*, *M. globosa*, *M. restricta*) — the yeast implicated as the principal pathogenic driver of dandruff and seborrheic dermatitis. Since seborrheic dermatitis pathology is directly dependent on *Malassezia* overgrowth, the mechanistic link between climbazole's known antifungal activity and this indication is direct and well-established, rather than a novel hypothesis.

Two important caveats apply. First, "Dermatitis" as scored by TxGNN is a broad, unspecific term; the actual literature retrieved supports only the **seborrheic dermatitis** subtype — it should not be extrapolated to other dermatitis types (e.g., contact dermatitis, atopic dermatitis), which have different underlying pathophysiology and were separately scored by TxGNN (rank #9, "dermatitis, atopic") with **zero** supporting evidence. Second, since climbazole-containing anti-dandruff/anti-seborrheic products are already commercially available worldwide (predominantly as cosmetic/OTC shampoo actives rather than as a formally registered pharmaceutical), this finding is best understood as a **formalization of an existing, already-marketed use** rather than a genuinely novel repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27904273](https://pubmed.ncbi.nlm.nih.gov/27904273/) | 2016 | RCT | Annals of Dermatology | Split-face RCT: climbazole/piroctone olamine cream was effective and well-tolerated for facial seborrheic dermatitis |
| [11534318](https://pubmed.ncbi.nlm.nih.gov/11534318/) | 2001 | RCT | Praxis | Climbazole 0.65% shampoo improved clinical signs of moderate-to-severe scalp seborrheic dermatitis after a 4-week treatment period |
| [21272039](https://pubmed.ncbi.nlm.nih.gov/21272039/) | 2011 | RCT | International Journal of Cosmetic Science | Piroctone olamine 0.5%/climbazole 0.45% shampoo showed efficacy comparable to a 1% zinc pyrithione shampoo in moderate-severe dandruff |
| [31190937](https://pubmed.ncbi.nlm.nih.gov/31190937/) | 2019 | Cohort/Clinical Study | Clinical, Cosmetic and Investigational Dermatology | Assessor-blinded 6-week study: hyaluronic acid cream containing climbazole improved signs, symptoms, and skin microbiota in facial seborrheic dermatitis |
| [38331330](https://pubmed.ncbi.nlm.nih.gov/38331330/) | 2024 | Review/Formulation | International Journal of Pharmaceutics | Characterizes climbazole skin permeation and rational formulation development for dandruff/seborrheic scalp conditions |
| [38544350](https://pubmed.ncbi.nlm.nih.gov/38544350/) | 2024 | In vitro/Preclinical | Journal of Cosmetic Dermatology | Novel shampoo formulations containing climbazole tested against *Malassezia* species amid emerging azole resistance concerns |
| [26397749](https://pubmed.ncbi.nlm.nih.gov/26397749/) | 2015 | PK/Analytical | Journal of Chromatography B | Validated UHPLC-MS/MS method quantifying climbazole and zinc pyrithione deposition on human scalp from anti-dandruff shampoos |
| [28550716](https://pubmed.ncbi.nlm.nih.gov/28550716/) | 2017 | PK/Ex-vivo | Journal of Pharmaceutical and Biomedical Analysis | Measured climbazole delivery into the scalp follicular infundibulum, relevant to anti-dandruff efficacy |
| [28599021](https://pubmed.ncbi.nlm.nih.gov/28599021/) | 2017 | PK/Imaging | Journal of Biomedical Optics | Stimulated Raman scattering imaging mapped cutaneous distribution of climbazole in dandruff treatment |
| [12858225](https://pubmed.ncbi.nlm.nih.gov/12858225/) | 2003 | Methodology | Journal of Cosmetic Science | Developed the "hair strand test" for evaluating antifungal (antimycotic) efficacy of anti-dandruff preparations |

---

## India Market Information

No market authorization records found. Climbazole currently has no registered pharmaceutical license in India (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three RCTs and multiple supporting studies directly demonstrate that climbazole-containing topical formulations reduce signs and symptoms of seborrheic dermatitis via well-understood anti-*Malassezia* activity, giving this candidate L2 evidence — the strongest of all 10 predictions in this pack. However, the guardrail is necessary because evidence supports only the seborrheic dermatitis subtype (not "dermatitis" broadly), the drug has zero market authorization in India, and formal safety/label data is entirely absent.

**To proceed, the following is needed:**
- India-specific regulatory/label safety data (key warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or another authoritative source — currently a High-severity data gap (DG002)
- Drug-drug interaction data (DDI query previously failed due to a missing local data file and returned no results)
- Clarification that any future indication claim is scoped specifically to seborrheic dermatitis, not generalized "dermatitis"
- A regulatory pathway assessment, since climbazole is not currently a registered pharmaceutical product in India (cosmetic/OTC shampoo use ≠ approved drug indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

