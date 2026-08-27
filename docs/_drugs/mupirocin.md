---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: From Bacterial Skin Infection to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic with well-established use against *Staphylococcus aureus* skin infections, including impetigo and MRSA nasal decolonization.
The TxGNN model predicts it may be effective for **Pleural Empyema**, achieving a prediction confidence of **99.49%**; however, **no clinical trials or supporting publications** currently exist for this specific application, placing it at the lowest evidence tier (L5) and warranting a **Hold** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial skin infections (*S. aureus* / MRSA) |
| Predicted New Indication | Pleural Empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record system. Based on established pharmacological knowledge, Mupirocin is a pseudomonic acid antibiotic that selectively inhibits bacterial isoleucyl-tRNA synthetase, blocking protein synthesis in susceptible Gram-positive organisms. It is particularly potent against *Staphylococcus aureus* (including MRSA) and *Streptococcus pyogenes* — two of the most clinically important skin pathogens.

Pleural empyema is a serious purulent infection of the pleural space, and *S. aureus* is a recognized causative organism. This shared pathogen forms the basis of the TxGNN model's prediction: the knowledge graph identifies a direct biological link between Mupirocin's established antibacterial profile and the microbial etiology of pleural empyema, which is a mechanistically coherent starting point.

However, a critical pharmacokinetic barrier fundamentally undermines this prediction. Mupirocin is formulated exclusively for topical application, with negligible systemic absorption following cutaneous use. It does not achieve measurable plasma concentrations sufficient to distribute to the pleural cavity. Without a radically different delivery strategy — such as direct intrapleural instillation — this prediction cannot be clinically translated in its current form. Route-of-administration incompatibility is the primary reason this candidate is rated Hold at L5 despite the high TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Mupirocin is currently not registered or marketed in India. No approved product authorizations are on record (0 licenses). No tabulation of authorization data is possible at this time.

---

## Safety Considerations

**Drug Interactions**: A total of 118 potential drug interactions have been identified (source: DDInter). All interactions are classified as "Unknown" severity, indicating limited clinical characterization data is available for this topical agent when considered in systemic co-medication contexts. Representative interactions include:

| Interacting Drug | Level | Clinical Context |
|-----------------|-------|-----------------|
| Vancomycin | Unknown | Both are anti-staphylococcal agents; concurrent use is clinically plausible in severe MRSA infections |
| Morphine | Unknown | Common analgesic co-administration in wound-care or post-surgical settings |
| Prednisone / Prednisolone / Triamcinolone | Unknown | Corticosteroid co-use may modulate local immune and inflammatory response |
| Metformin | Unknown | Frequent co-medication in diabetic patients with skin infections |
| Simvastatin / Rosuvastatin | Unknown | Common co-medications in cardiovascular risk patients |
| Pantoprazole / Omeprazole | Unknown | Common GI prophylaxis agents during concurrent systemic antibiotic therapy |

Please refer to the package insert for comprehensive safety, contraindication, and warning information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.49%), the prediction for pleural empyema is undermined by a fundamental pharmacokinetic barrier — Mupirocin is a topical-only formulation with no clinically meaningful systemic bioavailability and cannot reach the pleural cavity through any standard route of administration. Without resolving this delivery challenge, clinical development for this indication is not feasible.

**To proceed, the following is needed:**
- Evaluate whether novel delivery modalities (e.g., direct intrapleural irrigation formulation) could achieve therapeutic concentrations in the pleural space
- Obtain the Mupirocin package insert to resolve **DG001** (safety warnings and contraindications) and **DG002** (mechanism of action) — both currently blocking full evaluation
- **Strongly consider redirecting focus** to **Staphylococcal Scalded Skin Syndrome (SSSS)** (TxGNN Rank 9, Evidence Level **L3**, 14 supporting publications including retrospective cohort data and treatment reviews) — this candidate has a direct, route-compatible mechanistic rationale and represents the strongest repurposing opportunity identified in this Evidence Pack
- Evaluate **Cutaneous Candidiasis** (Rank 4, L4, 2 publications) and **MRSA Vaginosis** (Rank 10, L4, 1 publication) as secondary research questions with existing early-stage literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

