---
layout: default
title: Metaxalone
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 3
---

# Metaxalone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Metaxalone: From Skeletal Muscle Relaxant to Infectious Otitis Media

## One-Sentence Summary

Metaxalone (DrugBank: DB00660) is a centrally acting skeletal muscle relaxant, approved in the United States for relief of discomfort associated with acute, painful musculoskeletal conditions.
The TxGNN model predicts it may be effective for **Infectious Otitis Media** (rank #1 among predicted indications, score 99.06%),
however **no clinical trials and no publications** currently support this direction, and the mechanistic rationale analysis strongly suggests this is a model artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal pain / skeletal muscle spasm (centrally acting muscle relaxant; not registered in India) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Metaxalone in this evidence pack. Based on known pharmacological information, Metaxalone is a CNS depressant that acts centrally to produce skeletal muscle relaxation; it is widely used in the United States for acute musculoskeletal pain. Its precise molecular mechanism remains incompletely characterized, with no established antimicrobial, antiviral, or local anti-inflammatory activity in the ear.

Infectious otitis media is a bacterial or viral infection of the middle ear that requires antimicrobial treatment or symptomatic management targeting infectious pathogenesis. There is no known pharmacological bridge between central muscle relaxation and the resolution of middle-ear infection—neither antibacterial activity, anti-biofilm properties, nor relevant immunomodulatory effects have been reported for Metaxalone.

The high TxGNN score (0.9906) is most likely a **graph shortcut artifact**: when MOA-related nodes are absent or sparse in the knowledge graph, graph neural networks can generate spurious high-confidence links between pharmacologically unrelated drug–disease pairs. The fact that all three top-ranked predicted indications (otitis media, endocarditis, endocardial fibroelastosis) fall into structurally dissimilar disease categories with zero supporting evidence strongly reinforces this interpretation. This prediction should not be taken as a genuine repurposing signal without further mechanistic investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Metaxalone has **no registered products** in India. No authorization records are available.

---

## Safety Considerations

**Drug Interactions (53 interactions identified; selected key interactions shown below):**

| Interacting Drug | Severity | Clinical Significance |
|-----------------|----------|-----------------------|
| Morphine | **Major** | Additive CNS depression; risk of respiratory depression and sedation |
| Morphine (liposomal) | **Major** | Same as morphine; additive CNS depressant effects |
| Codeine | **Major** | Additive CNS and respiratory depression |
| Hydrocodone | **Major** | Additive CNS and respiratory depression |
| Dronabinol | Moderate | Enhanced CNS depression |
| Nabilone | Moderate | Enhanced CNS depression |
| Naltrexone | Moderate | May reduce analgesic efficacy of opioids used concomitantly |
| Metoclopramide | Moderate | Additive CNS effects |
| Ethanol | Moderate | Enhanced CNS depression; avoid concomitant use |
| Promethazine | Moderate | Additive sedation and CNS depression |
| Chlorpheniramine | Moderate | Additive sedation |
| Cetirizine | Moderate | Additive sedation |
| Dextromethorphan | Moderate | Additive CNS depression |
| Sibutramine | Moderate | CNS interaction risk |
| Doxylamine | Moderate | Additive sedation and anticholinergic effects |

> **Note:** Key warnings and contraindications data are not available in the current evidence pack. Please refer to the US FDA package insert (Skelaxin®) or applicable prescribing information for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction carries L5 evidence (model prediction only, zero supporting clinical or literature evidence) and the mechanistic rationale analysis identifies it as a probable graph neural network artifact driven by missing MOA nodes in the knowledge graph. Metaxalone's CNS muscle-relaxant profile has no plausible pharmacological connection to infectious otitis media, endocarditis, or endocardial fibroelastosis—the three top-ranked predictions all point toward the same systematic bias in the model output.

**To proceed, the following is needed:**

- **MOA clarification**: Retrieve complete DrugBank mechanism-of-action data to determine whether any secondary pharmacological activity could support anti-infective or anti-inflammatory applications
- **Knowledge graph audit**: Review TxGNN KG edges connecting Metaxalone to infection-related disease nodes to identify and correct the graph shortcut artifact
- **CDSCO/India package insert**: Obtain official prescribing information to document warnings, contraindications, and approved indications if/when India registration is sought
- **Re-prediction with updated KG**: Re-run TxGNN after patching missing MOA nodes; if the high scores persist after correction, escalate to L4 mechanistic investigation; otherwise, deprioritize this candidate
- **Consideration of alternative indications**: If Metaxalone repurposing is a priority, explore evidence-backed directions (e.g., neuropathic pain, spasticity in neurological conditions) rather than the current model-flagged infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

