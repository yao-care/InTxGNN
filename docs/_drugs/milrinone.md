---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Milrinone
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

# Milrinone: From Congestive Heart Failure to Alopecia

## One-Sentence Summary

Milrinone is a phosphodiesterase type 3 (PDE3) inhibitor widely used for the short-term intravenous management of congestive heart failure, with documented clinical use across multiple countries.
The TxGNN model predicts it may be effective for **Alopecia**, ranking it as the highest-scoring novel indication.
Currently, **0 clinical trials** and **0 publications** directly support this repurposing direction, placing the evidence at Level 5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congestive heart failure (short-term IV inotropic support) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Milrinone is a bipyridine-class selective PDE3 inhibitor. By preventing PDE3 from breaking down cyclic AMP (cAMP) within cardiac myocytes and vascular smooth muscle cells, it produces both a positive inotropic effect (enhanced heart contractility) and systemic vasodilation. Pharmacological data confirms that its binding targets include PDE2A, PDE3A, PDE3B, and PDE5A, all expressed in human tissue.

The connection to alopecia rests on an indirect biological hypothesis: cAMP signaling pathways do participate in hair follicle biology, particularly in regulating the Wnt/β-catenin cascade that governs the anagen (growth) phase of the hair cycle. In theory, elevating intracellular cAMP via PDE3 inhibition could influence dermal papilla cell activity. However, this mechanistic chain remains entirely unvalidated for Milrinone specifically, and no published in vitro or in vivo experiment has explored PDE3 inhibition as a hair follicle target.

The TxGNN model's high score most likely reflects knowledge graph topological proximity — shared pathway nodes or common molecular associations between Milrinone and alopecia-related diseases — rather than a direct causal mechanism. This prediction should be treated as a hypothesis-generating signal, not a clinically actionable finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Milrinone is not currently marketed in India. No product authorizations, registered brands, or approved dosage forms are on record with the regulatory authority.

---

## Safety Considerations

**Drug Interactions** (5 clinically graded interactions identified from DDInter):

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|------------------|-------------------|
| Amifostine | Moderate | Additive hypotensive effect possible |
| Diatrizoate | Moderate | Contrast media; cardiovascular monitoring advised |
| Anagrelide | Moderate | Both inhibit PDE; additive cardiovascular effects |
| Ozanimod | Moderate | Risk of additive heart rate or blood pressure effects |
| Procarbazine | Moderate | Potential cardiovascular interaction |

**Pharmacological Targets** (from Guide to Pharmacology): Milrinone acts on PDE3A (gene: PDE3A, ENSG00000172572), PDE3B (gene: PDE3B, ENSG00000152270), and also shows activity at PDE2A and PDE5A. This broad PDE binding profile should be considered when co-administering other vasoactive agents.

Please refer to the package insert for full warnings and contraindications, as detailed safety labelling data was not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite TxGNN assigning the highest novel-indication score to alopecia (99.91%), the evidence base is entirely absent — no clinical trials, no observational data, and no published mechanistic studies link Milrinone's PDE3 inhibition to hair follicle biology. Proceeding without any preclinical foundation would not be scientifically justifiable.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro studies testing whether PDE3 inhibition (using Milrinone or selective PDE3 inhibitors) affects human dermal papilla cell proliferation or keratinocyte behaviour
- **Mechanistic proof of concept**: Establish whether cAMP elevation via PDE3 inhibition influences the Wnt/β-catenin pathway in hair follicle models
- **MOA clarification**: Full DrugBank mechanism-of-action data for Milrinone to better map downstream pathway interactions
- **Route of administration feasibility**: Assess whether a topical or localised delivery route is feasible to avoid systemic cardiovascular effects (hypotension, arrhythmia risk) that would preclude systemic use for a cosmetic/dermatological indication
- **India regulatory gap**: Obtain full CDSCO/India labelling data for safety labelling review before any IND-stage planning

> **Note for reviewers**: Among all predicted indications in this Evidence Pack, **congestive heart failure** (Rank 6, TxGNN score 99.45%, Evidence Level L2) carries substantially stronger support — with over 50 registered clinical trials, 20 published studies, and a completed Phase 1/2 oral slow-release milrinone trial. If the goal is identifying the most actionable repurposing opportunity from this dataset, congestive heart failure warrants a dedicated higher-priority report, as it represents confirmation of Milrinone's established pharmacological role with emerging evidence for novel formulations (oral extended-release, inhaled nebulised).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

