---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide (Xtandi) is a second-generation androgen receptor (AR) inhibitor with established clinical approval in multiple markets for castration-resistant and castration-sensitive prostate cancer.
The TxGNN model predicts it may be relevant for **Prostate Cancer/Brain Cancer Susceptibility** conditions,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (castration-resistant and castration-sensitive) |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Enzalutamide is a potent, second-generation androgen receptor (AR) antagonist. Unlike first-generation agents such as bicalutamide, it exerts a triple-blockade mechanism: (1) competitive inhibition of androgen binding to the AR, (2) suppression of AR nuclear translocation, and (3) inhibition of AR–DNA binding and co-activator recruitment. This comprehensive AR axis blockade is the basis for its remarkable efficacy in castration-resistant prostate cancer (CRPC), validated across landmark Phase 3 trials including AFFIRM, PREVAIL, PROSPER, and ARCHES.

The prediction for "prostate cancer/brain cancer susceptibility" likely reflects a hereditary cancer predisposition context — for example, germline mutations in BRCA2, CHEK2, or ATM that simultaneously elevate lifetime risk for both prostate and certain brain tumors (e.g., glioblastoma). Biological plausibility exists in this space: in BRCA2-deficient prostate cancers, the AR signaling axis remains a key growth driver, and preclinical work suggests that AR activity may modulate expression of homologous recombination repair genes, potentially creating a vulnerability exploitable by AR inhibition. The TxGNN model's high score (rank 5603 of all disease nodes) reflects this strong topological proximity between Enzalutamide and prostate cancer–related nodes in the knowledge graph.

However, a critical conceptual distinction must be made: "susceptibility" refers to a risk state, not an established malignancy. Chemoprevention of hereditary cancer syndromes using AR inhibitors has not been clinically investigated. The absence of any supporting trial or literature data, combined with the unusual disease framing (susceptibility rather than active disease), suggests this prediction captures a graph topology signal rather than a clinically actionable treatment hypothesis in its current form.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication (prostate cancer/brain cancer susceptibility).

---

## Literature Evidence

Currently no related literature available for the predicted indication (prostate cancer/brain cancer susceptibility).

---

## India Market Information

Enzalutamide currently holds no approved registrations in India. No license records are available.

---

## Cytotoxicity

Enzalutamide is classified as an antineoplastic agent (prostate cancer treatment) and meets the criteria for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation androgen receptor antagonist (non-steroidal) |
| Myelosuppression Risk | Low (AR antagonists do not exert direct bone marrow toxicity; neutropenia is uncommon) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs), complete blood count (CBC), blood pressure, neurological status (seizure risk — known class effect), cardiovascular assessment |
| Handling Protection | Standard oral antineoplastic handling precautions recommended; avoid crushing/splitting capsules |

---

## Safety Considerations

**Drug Interactions**: Enzalutamide has 571 documented drug interactions in the DDInter database. Clinically significant interactions include:

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|-----------------|
| **Major** | Bupropion | Seizure threshold lowering — additive risk with Enzalutamide's known seizure potential |
| **Major** | Dolasetron | QT interval prolongation risk |
| **Major** | Eliglustat | Enzalutamide induces CYP3A4/CYP2D6, significantly altering Eliglustat exposure |
| Moderate | Clarithromycin | CYP3A4 inhibition may increase Enzalutamide plasma levels |
| Moderate | Dexamethasone / Hydrocortisone | CYP3A4 induction interactions; frequent combination in prostate cancer — dosing review required |
| Moderate | Famotidine / Omeprazole / Rabeprazole | Acid-suppressive agents may affect absorption; gastric pH considerations |
| Moderate | Saxagliptin / Linagliptin / Empagliflozin | Diabetes medications — CYP3A4 induction by Enzalutamide may reduce DPP-4 inhibitor exposure |

> Note: Formal package insert warnings and contraindications for this market have not yet been retrieved (Data Gap DG001). Please refer to the current prescribing information (FDA/EMA label) for complete safety data before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN prediction score (99.71%) reflects strong graph-level proximity to prostate-related pathways, but the "susceptibility" framing of the indication is a fundamentally different clinical context from therapeutic treatment — and zero supporting clinical trials or published literature leaves this at L5 evidence, insufficient for clinical development planning.

**To proceed, the following is needed:**

- **Disease phenotype clarification**: Precisely define what "prostate cancer/brain cancer susceptibility" represents in the knowledge graph (ICD-10/OMIM mapping) — is this a specific hereditary syndrome (e.g., BRCA2-associated, Lynch syndrome)?
- **Mechanistic validation**: Conduct a targeted literature review on AR's role in hereditary cancer susceptibility and chemoprevention — does AR inhibition reduce incident cancer risk in germline mutation carriers?
- **Safety data completion**: Retrieve TFDA/FDA package insert for full warnings and contraindications (resolve Data Gap DG001)
- **MOA data retrieval**: Obtain DrugBank API data for formal MOA documentation (resolve Data Gap DG002)
- **Pivot consideration**: Rank 9 of this same prediction set — **Prostate Neoplasm** — carries L1 evidence with a "Proceed with Guardrails" recommendation and represents a far more immediately actionable repurposing signal for India market strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

