---
layout: default
title: Amodiaquine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Amodiaquine
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

# Amodiaquine: From Malaria to Pulmonary Hypertension

## One-Sentence Summary

Amodiaquine is a 4-aminoquinoline antimalarial drug, widely used for decades in the treatment and prevention of malaria caused by *Plasmodium falciparum*, particularly in sub-Saharan Africa as part of artemisinin-based combination therapy (ASAQ).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a high prediction confidence score of 99.25%.
However, currently **no clinical trials** and **no publications** specifically supporting this repurposing direction have been identified, making the evidence base extremely limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (*Plasmodium falciparum* infection) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Amodiaquine belongs to the 4-aminoquinoline class of antimalarial drugs — the same structural family as chloroquine and hydroxychloroquine. Its primary antimalarial activity is attributed to accumulation in parasite food vacuoles and inhibition of heme polymerization, thereby disrupting the parasite's ability to detoxify heme. Beyond its antiparasitic action, amodiaquine has well-documented anti-inflammatory properties: studies in the rheumatoid arthritis literature confirm that it suppresses T cell proliferation and Th1 cell differentiation through p21-mediated pathways, and inhibits PPARγ activity, reducing pro-inflammatory responses.

The mechanistic bridge to pulmonary hypertension is plausible but speculative. Pulmonary arterial hypertension (PAH) is increasingly understood as a disease with significant inflammatory and autoimmune components — vascular remodelling driven by inflammatory cytokines, T cell infiltration, and dysregulated immune signalling are central pathophysiological features. Chloroquine and hydroxychloroquine, structurally related to amodiaquine, have been studied in PAH and systemic autoimmune diseases complicated by PAH, lending indirect mechanistic support. Additionally, the 4-aminoquinolines are known to modulate lysosomal function and autophagy, pathways implicated in pulmonary vascular smooth muscle cell proliferation.

That said, the TxGNN knowledge graph prediction may be capturing network-level relationships (shared protein targets, pathway proximity) rather than direct mechanistic evidence. Without primary experimental data or clinical observation linking amodiaquine specifically to pulmonary haemodynamics, this prediction remains hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amodiaquine in Pulmonary Hypertension.

---

## Literature Evidence

Currently no related literature available for Amodiaquine in Pulmonary Hypertension.

---

## India Market Information

Amodiaquine is not currently registered or marketed in India. No authorizations on record.

> **Note:** Amodiaquine is listed on the WHO Essential Medicines List for malaria treatment (as ASAQ fixed-dose combination) and is widely used in Africa under WHO/UNICEF programs, but it does not hold an approved marketing authorization in India as of the data cut-off (2026-04-05).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data specific to amodiaquine — including package insert warnings, contraindications, and drug-drug interaction profiles — were not available in this Evidence Pack. Key known concerns from the pharmacological literature include: risk of agranulocytosis with prolonged use (historically limiting its prophylactic use), hepatotoxicity, and potential QT interval prolongation (a class effect of aminoquinolines relevant to any cardiac indication such as PAH). These require formal evaluation before any repurposing programme is initiated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.25%) to amodiaquine for pulmonary hypertension, suggesting strong network-level associations in the knowledge graph; however, zero clinical trials and zero directly relevant publications have been identified, placing this at Evidence Level L5 — model prediction only, with no empirical validation. The drug is also not marketed in India, eliminating any regulatory shortcut. A Hold decision is appropriate until foundational evidence is established.

**To proceed, the following is needed:**

- **MOA clarification**: Obtain full DrugBank mechanism-of-action data for amodiaquine (DrugBank DB00613) to confirm whether known molecular targets overlap with PAH pathophysiology (e.g., PDGFR, BMPR2 pathway, inflammatory cytokine suppression)
- **Safety dossier**: Retrieve CDSCO/TFDA/EMA package insert for complete warnings, contraindications, and QT-prolongation risk profile — critical for any cardiac/pulmonary indication
- **Preclinical evidence search**: Conduct a systematic search in PubMed using broader queries (e.g., "amodiaquine vascular", "4-aminoquinoline pulmonary hypertension", "chloroquine PAH") to identify any indirect preclinical support
- **DDI database access**: Restore the DDinter dataset (file path error logged in query log) to assess drug interaction risks, particularly with current PAH pharmacotherapy (sildenafil, bosentan, prostanoids)
- **Expert review**: Engage a pulmonary hypertension specialist to assess biological plausibility before committing to preclinical studies
- **India regulatory pathway assessment**: Confirm whether amodiaquine would require a full NDA or could leverage existing WHO/international data packages if clinical evidence supports advancement

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

