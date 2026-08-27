---
layout: default
title: Etizolam
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 1
---

# Etizolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Etizolam: From Anxiolytic/Sedative to Insomnia

## One-Sentence Summary

Etizolam is a thienodiazepine compound, primarily recognized as an anxiolytic and sedative-hypnotic agent used in select Asian markets (notably Japan and India), acting as a positive allosteric modulator of the GABA-A receptor.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **99.94%**,
supported by **0 clinical trials** and **4 publications** — primarily preclinical and pharmacokinetic in nature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders / sedation (thienodiazepine class; no Taiwan/India regulatory record available) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Etizolam belongs to the **thienodiazepine** class and acts as a **positive allosteric modulator (PAM) of the GABA-A receptor** — a mechanism essentially identical to classical benzodiazepines, but with a thienyl ring replacing the benzene ring in the chemical scaffold. By enhancing GABAergic inhibitory neurotransmission, it produces sedative, hypnotic, anxiolytic, and muscle-relaxant effects. Its half-life of approximately 6 hours (with an active metabolite, α-hydroxy-etizolam, of ~8 hours) is pharmacokinetically suitable for both sleep-onset and sleep-maintenance indications.

The mechanistic link between Etizolam and insomnia is therefore highly plausible. GABA-A receptor modulation is the shared mechanism of virtually all approved benzodiazepine and Z-drug hypnotics (e.g., triazolam, zolpidem, eszopiclone). The very high TxGNN score (0.9994) reflects a strong graph-level association between the GABA pathway nodes and the insomnia disease node in the knowledge graph. Furthermore, a preclinical study (PMID 18789918) directly demonstrated that Etizolam shortened sleep latency and increased non-REM sleep time in rats — consistent with clinical utility for insomnia.

However, mechanistic plausibility does not substitute for clinical evidence. The major safety concern is the well-established class risk of **tolerance, dependence, and rebound insomnia** upon withdrawal, which is documented even in the limited preclinical literature available for Etizolam specifically. This risk substantially limits the drug's profile as a long-term insomnia treatment and must be addressed before any clinical development pathway can be recommended.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18789918](https://pubmed.ncbi.nlm.nih.gov/18789918/) | 2008 | Animal Study (Preclinical) | European Journal of Pharmacology | Etizolam shortened sleep latency and increased non-REM sleep time in rats in a dose-dependent manner; abrupt withdrawal caused significant rebound insomnia (prolonged sleep latency), paralleling triazolam behavior |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review (PK) | Expert Opinion on Drug Metabolism & Toxicology | Reviewed pharmacokinetics of anxiolytic drugs including thienodiazepines; anxiety disorders represent the most common mental disorders with high comorbidity burden, supporting rational for GABAergic agents |
| [23553148](https://pubmed.ncbi.nlm.nih.gov/23553148/) | 2013 | Case Report | Journal of Anesthesia | Case of neuroleptic malignant syndrome-like symptoms with fever and insomnia emerging on postoperative day 1 following abrupt withdrawal of oral etizolam, highlighting withdrawal-related insomnia risk |
| [29105206](https://pubmed.ncbi.nlm.nih.gov/29105206/) | 2018 | Observational / Cross-sectional | Journal of Paediatrics and Child Health | Identified risk factors for psychological and psychosomatic symptoms (including sleep disturbance) in hospitalised children with malignancies; Etizolam mentioned among medications used for symptom management |

---

## India Market Information

Etizolam currently has **no registered products** in India (or Taiwan) according to the regulatory data in this Evidence Pack. No authorisation table can be generated.

> **Note:** Etizolam is approved and marketed in Japan (as Depas®) and has a complex regulatory status internationally — classified as a controlled/scheduled substance in several jurisdictions including the EU and US. This regulatory landscape is a material consideration for any development strategy in India.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, drug–drug interactions) were not available in this Evidence Pack. Based on class-level knowledge:

- **Withdrawal / Rebound Insomnia**: Directly documented in preclinical data (PMID 18789918); abrupt cessation after sustained use causes significant rebound sleep disturbance — a major concern for an insomnia indication.
- **Dependence and Tolerance**: As a GABAergic PAM, Etizolam carries the standard benzodiazepine class risk of physical dependence, tolerance, and abuse potential.
- **Controlled Substance Status**: Etizolam is classified as a scheduled/controlled substance in multiple jurisdictions; this has direct implications for development pathway, prescribing restrictions, and regulatory strategy in India.

Please refer to the package insert and applicable national controlled substance regulations for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to preclinical animal studies and pharmacokinetic reviews with no registered clinical trials for the insomnia indication; the L4 evidence level, combined with the drug's controlled substance status and known rebound insomnia risk, does not support advancing to feasibility analysis without first resolving the data gaps and regulatory constraints.

**To proceed, the following is needed:**

- **Regulatory classification clarification**: Determine Etizolam's current legal/scheduling status in India — whether it is permissible to develop, import, or study for new indications under the Narcotic Drugs and Psychotropic Substances Act or equivalent regulation.
- **MOA documentation**: Obtain full DrugBank mechanism-of-action data and pharmacodynamic profile to complete the mechanistic link analysis (Data Gap DG002).
- **Safety data retrieval**: Download and parse the Japanese PMDA package insert (Depas®) or equivalent source for full warnings, contraindications, and DDI profile (Data Gap DG001).
- **Comparative landscape review**: Assess whether Etizolam offers any meaningful clinical advantage over already-approved hypnotics (zolpidem, eszopiclone) for insomnia, given the identical GABA-A mechanism and a worse dependence/rebound profile vs. Z-drugs.
- **Clinical evidence search**: Conduct a targeted systematic search in Japanese literature databases (Ichushi-Web / J-STAGE) where Etizolam has been used clinically, to identify any human sleep data not captured by PubMed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

