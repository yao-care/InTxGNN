---
layout: default
title: Primaquine
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 8
---

# Primaquine
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

Using the Evidence Pack as provided (no additional tools needed — this is a direct report-writing task from structured JSON data already supplied). I want to flag one data-quality issue before the report: `predicted_indications[0]` (myiasis) has **zero** supporting trials/literature, while several *lower-ranked* candidates in this same pack (malaria, pneumocystosis, toxoplasmosis) have substantial evidence — and "malaria" is actually Primaquine's own established indication reappearing as a "prediction." I followed the template's literal instruction to use `predicted_indications[0]` as the headline candidate, but I've noted this context in the Conclusion so it isn't lost.

---

# Primaquine: From Malaria to Myiasis

## One-Sentence Summary

Primaquine is a well-established 8-aminoquinoline antimalarial, historically used for the radical cure of *Plasmodium vivax* and as a gametocytocidal agent against *Plasmodium falciparum*. The TxGNN model predicts it may be effective for **Myiasis**, but this specific link is currently supported by **0 clinical trials** and **0 publications**, making it a purely computational hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (established antimalarial use — radical cure of *P. vivax*, gametocytocidal against *P. falciparum*); no India label text available since the drug is not locally registered |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no supporting studies identified) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Primaquine in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological information corroborated elsewhere in this same pack — the drug's own "malaria" entry cites 50 clinical trials describing it as "the only drug commercially available that kills mature transmission stage" of *P. falciparum* and the standard radical-cure agent for *P. vivax* hypnozoites — Primaquine's proven efficacy lies squarely in antiprotozoal, blood- and liver-stage antimalarial activity, primarily attributed to oxidative-stress-mediated parasite killing.

Myiasis, in contrast, is a parasitic infestation caused by dipteran fly larvae (not a protozoan), and its established treatments are mechanical larval removal, occlusive therapy, or ivermectin — none of which share Primaquine's known mechanism. The repurposing rationale field for this specific candidate is marked "pending" with no mechanistic-link data populated, meaning the model's score is not yet backed by any documented biological hypothesis in this evidence pack.

Given the absence of both a documented mechanistic rationale and any real-world evidence (trials or literature), this candidate should currently be treated as a **graph-based signal only** — worth flagging for expert review, but not yet supported by pharmacological or clinical reasoning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Primaquine currently holds **no registrations** in the India market data on file (0 licenses; market status: Not Marketed). No product/dosage-form information is available for extraction.

---

## Safety Considerations

**Drug Interactions**: The evidence pack identifies 278 total documented interactions for Primaquine (source: DDInter). Notable entries include:

| Interacting Drug | Severity Level |
|---|---|
| Dolasetron | Major |
| Famotidine | Moderate |
| Alosetron | Moderate |
| Loperamide | Moderate |
| Clarithromycin | Moderate |
| Levofloxacin | Moderate |
| Ondansetron, Granisetron, Palonosetron | Moderate |
| Metronidazole | Minor |

(20 of 278 total interactions shown; most flagged entries relate to QT-interval-affecting or serotonergic agents, with Dolasetron as the sole Major-level interaction in this sample.)

Separately, literature captured elsewhere in this evidence pack (e.g., PMID 36160421, and multiple malaria/PCP trials such as NCT03337152 and NCT02216123) repeatedly documents **hemolytic risk in G6PD-deficient patients** as a defining safety concern for Primaquine. This is not part of the structured `safety.key_warnings` field (which is a blocking data gap in this pack) but is worth flagging as a known class-level risk pending confirmation from official labeling.

Official warning and contraindication text is a **blocking data gap** in this evidence pack — please refer to the package insert once available for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for Primaquine → Myiasis is high (99.76%), but there is no corroborating clinical trial, literature, or mechanistic-link evidence in this pack, placing it at Evidence Level L5. Compounding this, the drug-level safety data needed for even a preliminary S1 safety screen (TFDA/label warnings and contraindications) is a **Blocking** data gap, so this candidate cannot currently advance past S0.

**To proceed, the following is needed:**
- Official label safety data (warnings/contraindications) to clear the Blocking data gap (DG001)
- Mechanism of action data from DrugBank to support or refute biological plausibility (DG002)
- A targeted literature/trial search specifically for "Primaquine AND myiasis" (or related antiparasitic/larvicidal activity) beyond what this pack currently captures
- Expert (entomology/parasitology) review of biological plausibility, since Primaquine's known antiprotozoal mechanism has no established link to dipteran larvae
- Consideration of re-scoping this evaluation toward better-evidenced candidates already present in this same pack — notably **pneumocystosis** (6 trials + 20 publications, including a Phase 3 RCT) and **toxoplasmosis** (L4, 7 publications) — which have materially stronger evidentiary support than the current rank-1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

