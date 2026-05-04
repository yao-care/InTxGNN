---
layout: default
title: Monobenzone
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Monobenzone
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

# Monobenzone: From Depigmentation (Vitiligo) to Dentinogenesis Imperfecta

## One-Sentence Summary

Monobenzone is a melanocyte-selective cytotoxin historically used as a topical depigmenting agent for permanent depigmentation in patients with extensive vitiligo.
The TxGNN model predicts it may be effective for **Dentinogenesis Imperfecta** with a score of **92.18%**,
however **no clinical trials and no published literature** currently support this direction — evidence is limited to model prediction alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Depigmentation in extensive vitiligo |
| Predicted New Indication | Dentinogenesis Imperfecta |
| TxGNN Prediction Score | 92.18% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Monobenzone from this Evidence Pack. Based on known pharmacology, Monobenzone (monobenzyl ether of hydroquinone) is a melanocyte-selective cytotoxin that irreversibly destroys melanocytes by generating reactive quinone metabolites that disrupt tyrosinase activity and induce oxidative stress selectively within pigment-producing cells. Its established clinical use is permanent depigmentation in patients with widespread vitiligo.

Dentinogenesis imperfecta (DI) is a hereditary disorder of dentin formation caused by mutations in the *DSPP* (dentin sialophosphoprotein) or *DMP1* genes, resulting in defective dentin mineralization, discoloured teeth, and increased fracture susceptibility. There is no obvious pharmacological bridge between Monobenzone's tyrosinase-pathway mechanism and the DSPP/DMP1 signalling cascade that governs odontoblast differentiation and dentin matrix production.

The TxGNN system likely arrived at this prediction via an indirect graph-traversal pathway: melanocytes and odontoblasts both originate from neural crest cells, and tyrosinase-related proteins (TRP-1, TRP-2) have documented, albeit peripheral, roles in enamel and dentin mineralisation biology. This shared embryological ancestry creates graph-level proximity in the knowledge graph, but it does not constitute a direct mechanistic link. The prediction should therefore be regarded as a hypothesis-generating signal rather than actionable evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Monobenzone (DrugBank ID: DB00600) is **not currently marketed in India**. No approved product licenses were identified. The drug has no registered dosage forms on the Indian market at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindications data are unavailable in this Evidence Pack. Drug–drug interaction data could not be retrieved (DDInter database file not found). Before any clinical use or study initiation, a full safety assessment from the originator label or a regulatory-grade dossier is mandatory.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a mathematically high score (92.18%) for Monobenzone in dentinogenesis imperfecta, but this likely reflects knowledge-graph topological clustering through shared neural crest cell biology rather than a direct pharmacological mechanism. There are zero clinical trials and zero published studies supporting this repurposing hypothesis, and all safety data are absent — this combination places the candidate firmly at evidence level L5, which is insufficient to justify any development investment without further validation.

**To proceed, the following is needed:**

- **Mechanistic validation**: Conduct in vitro experiments testing whether Monobenzone or its quinone metabolites modulate DSPP/DMP1 expression or odontoblast differentiation in dental pulp stem cell models.
- **MOA data retrieval**: Obtain full mechanism-of-action data from DrugBank API (DG002) to confirm or refute any plausible biological linkage.
- **Safety dossier**: Retrieve CDSCO/FDA label warnings, contraindications, and a complete DDI profile (DG001) before any in vivo or human study design can be considered.
- **Animal/preclinical study**: Establish at least one in vivo model (e.g., *Dspp*-knockout mouse) to assess whether systemic or local Monobenzone administration has any effect on dentin quality or tooth structure.
- **Re-evaluate prediction cluster**: The nearly identical TxGNN scores across ranks 2–10 (all 0.915–0.922) strongly suggest a graph clustering artefact. A broader mechanistic review of this cluster is recommended before prioritising any single indication from this list.

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All findings should be verified against current regulatory-approved labelling.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

