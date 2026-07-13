---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine: From Alzheimer's Disease to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist originally used for the treatment of moderate-to-severe Alzheimer's disease.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **0 clinical trials** and **2 publications** currently supporting this direction. The evidence base is primarily mechanistic and preclinical, placing this candidate at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease (moderate-to-severe) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Memantine is a non-competitive NMDA (N-methyl-D-aspartate) receptor antagonist. By blocking excessive calcium influx through over-activated NMDA channels, it reduces excitotoxic neuronal damage. This mechanism is well-validated in the context of Alzheimer's disease, where glutamate-mediated excitotoxicity plays a central pathological role.

The theoretical link to pulmonary hypertension rests on the observation that NMDA receptors are expressed not only in the central nervous system but also in peripheral vascular tissues, including pulmonary artery smooth muscle cells. In principle, blocking NMDA receptor-mediated calcium influx could attenuate smooth muscle cell proliferation and vascular remodeling — both hallmarks of pulmonary arterial hypertension (PAH). However, this mechanistic chain involves multiple indirect steps and has not been validated in dedicated PAH models.

The most relevant preclinical evidence (PMID 33500723) addresses NMDA receptor activation in the context of insulin resistance and lipid metabolism, not pulmonary vascular pathology. The only direct PAH-related study (PMID 41739394) involves MN-08, a nitrate *derivative* of memantine, in a Phase 1 pharmacokinetics trial — it does not evaluate memantine itself for PAH efficacy. Overall, biological plausibility is weak, and this prediction is likely driven by graph-level disease node proximity within the TxGNN knowledge graph rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/Safety | Clinical Drug Investigation | MN-08 (a nitrate derivative of memantine) evaluated in healthy Chinese volunteers for single/multiple ascending doses; aimed at PAH indication. Safety and PK data only — no efficacy data for memantine itself in PAH. |
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Basic/Mechanism | Theranostics | Investigated how NMDA receptor activation regulates insulin sensitivity and lipid metabolism. Mentions glutamate/NMDAR axis in pulmonary arterial hypertension and diabetes context, but does not study memantine's effect on PAH pathophysiology. |

---

## India Market Information

Memantine is currently **not marketed in India** and has **no registered product licenses** on record. No authorization table is available.

---

## Safety Considerations

**Drug Interactions** (100 total interactions on record; representative sample below):

| Interacting Drug | Interaction Level |
|-----------------|------------------|
| Hyoscyamine | Moderate |
| Atropine | Moderate |
| Glycopyrronium | Moderate |
| Clidinium | Moderate |
| Dicyclomine | Moderate |
| Methscopolamine | Moderate |
| Propantheline | Moderate |
| Scopolamine | Moderate |
| Trospium | Moderate |
| Mepenzolate | Moderate |
| Ranitidine | Minor |
| Metformin | Minor |
| Cimetidine | Minor |
| Potassium citrate | Minor |
| Glimepiride | Unknown |
| Doxycycline | Unknown |
| Lansoprazole | Unknown |
| Loperamide | Unknown |
| Famotidine | Unknown |
| Acetylsalicylic acid | Unknown |

> Note: The moderate-level interactions are predominantly with anticholinergic agents (atropine-class drugs). This is consistent with memantine's known pharmacology, as both drug classes affect cholinergic/glutamatergic neurotransmission pathways. Prescribers should exercise caution when co-administering memantine with any anticholinergic medication.
>
> Please refer to the package insert for full warnings and contraindications, as those data were not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score for pulmonary hypertension, but the underlying evidence is at L4 (preclinical/mechanistic only). No clinical trials of memantine for PAH exist, and the two available publications do not establish direct efficacy: one is a basic metabolic study with only tangential mention of PAH, and the other evaluates a distinct chemical derivative (MN-08) in a PK safety study. The mechanistic link involves multiple indirect inferential steps with no direct experimental validation in a PAH model.

**To proceed, the following is needed:**

- **Mechanistic validation**: Dedicated in vitro and in vivo studies confirming memantine's effect on pulmonary artery smooth muscle cell proliferation and vascular remodeling
- **Preclinical PAH model data**: Efficacy data in established animal models of PAH (e.g., monocrotaline or hypoxia-induced rat model) before any human study can be justified
- **MN-08 Phase 2/3 results**: Monitor progression of MN-08 trials; if this derivative demonstrates PAH efficacy, it would lend indirect biological support but would not substitute for memantine itself
- **MOA documentation**: Full mechanism of action data from DrugBank or primary sources to assess vascular target expression profiles
- **Safety package**: Download and parse the full prescribing information (package insert) to complete the key warnings and contraindications gap (DG001)
- **India regulatory pathway**: If pre-clinical data become supportive, consult CDSCO on requirements for a new indication investigational study, given the current zero-registration status in India

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

