---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Invasive Candidiasis to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin-class antifungal agent with established clinical use in invasive candidiasis and invasive aspergillosis, currently not registered in India.
The TxGNN model ranks **Gastrin Secretion Abnormality** as its top predicted new indication,
with **0 clinical trials** and **0 publications** directly supporting this direction — suggesting a probable false positive from the knowledge graph.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis; invasive aspergillosis (known clinical use; no India registration on record) |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on information embedded in the evidence pack's repurposing rationale, Caspofungin belongs to the **echinocandin class** and exerts its antifungal effect by inhibiting **β-1,3-glucan synthase** (encoded by *FKS1* and *FKS2* genes) — an enzyme essential for fungal cell wall biosynthesis. Disruption of the cell wall leads to osmotic instability and fungal cell death. Its efficacy in invasive *Candida* and *Aspergillus* infections is well-established in international guidelines.

Gastrin secretion abnormality involves dysregulation of gastrin production by **G cells** in the gastric antrum, modulated through CCK-B (cholecystokinin B) receptors and neuroendocrine signalling. There is no known pharmacological bridge between β-1,3-glucan synthesis inhibition and this neuroendocrine pathway.

The TxGNN model's high score (99.44%) for this indication most likely reflects a **distant indirect node connection** in the knowledge graph — e.g., the path: *Candida* infection → gut microbiome disruption → gastrointestinal hormone dysregulation → gastrin abnormality. This is a low-specificity, multi-hop inference rather than a mechanistically grounded prediction, and carries a high probability of being a **false positive**. No preclinical or clinical data exists to elevate this beyond an algorithm-generated hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** (81 total interactions identified; selected highlights shown below):

| Interacting Drug | Severity |
|-----------------|----------|
| Dexamethasone | **Major** |
| Naltrexone | Moderate |
| Calcitriol | Unknown |
| Pantoprazole | Unknown |
| Doxycycline | Unknown |
| Morphine | Unknown |
| Omeprazole | Unknown |
| Lansoprazole | Unknown |
| Vancomycin | Unknown |
| Sucralfate | Unknown |
| Lactulose | Unknown |
| Prednisone | Unknown |
| Simvastatin | Unknown |
| Nystatin | Unknown |
| Epinephrine | Unknown |
| Amphotericin B | Unknown |
| Hydrocortisone | Unknown |
| Prednisolone | Unknown |

> The **Major** interaction with **Dexamethasone** is the most clinically significant finding. Caspofungin's plasma levels can be reduced by enzyme inducers; co-administration with systemic corticosteroids warrants dose review. The high count of Unknown-severity interactions (largely with common ICU medications — PPIs, corticosteroids, opioids, antibiotics) reflects incomplete DDI characterisation and should be evaluated systematically before any new indication study is designed.
>
> For complete warnings and contraindications, please refer to the originator package insert (Cancidas® / Merck), as formal CDSCO labelling data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no identified mechanistic link between caspofungin's β-1,3-glucan synthase inhibition and gastrin secretion pathways, and a complete absence of supporting clinical trials or literature makes this indication unsuitable for further development at this stage. The high TxGNN score most likely reflects knowledge-graph topology rather than true pharmacological relevance.

**To proceed with this specific indication, the following would be needed:**
- A plausible biological hypothesis connecting the echinocandin mechanism to G-cell / CCK-B receptor biology (e.g., via fungal-gut microbiome-gastrin axis)
- Preclinical evidence (in vitro or in vivo) demonstrating any effect on gastrin secretion
- Retrieval of full MOA data from DrugBank (DB00520) and CDSCO / originator package insert

---

**⚠️ Note on higher-priority indications in this evidence pack:**

While the top-ranked TxGNN prediction (Gastrin Secretion Abnormality, Rank 1) is a **Hold**, two additional indications within this same evidence pack carry meaningfully stronger evidence and merit separate evaluation:

| Rank | Indication | Evidence Level | Decision |
|------|-----------|---------------|----------|
| 8 | **Candida glabrata** infection | L2 | Proceed with Guardrails |
| 9 | **Neonatal Candidiasis** | L2 | Research Question |
| 10 | **Congenital Candidiasis** | L2 | Proceed with Guardrails |

Caspofungin is an IDSA-recommended first-line agent for invasive *C. glabrata* infections, with Phase 4 clinical trial data (NCT00839540), pharmacokinetic studies in neonates (NCT00330395), and a completed Phase 3 trial in Chinese adults supporting the congenital/neonatal candidiasis use case (NCT00635648). These indications represent the most clinically actionable repurposing opportunities in this evidence pack and should be prioritised for full report generation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

