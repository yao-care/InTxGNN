---
layout: default
title: Chlorzoxazone
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Chlorzoxazone
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

# Chlorzoxazone: From Skeletal Muscle Spasm to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is a centrally-acting skeletal muscle relaxant traditionally used for relief of discomfort associated with acute painful musculoskeletal conditions.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Skeletal muscle spasm and musculoskeletal pain (centrally-acting muscle relaxant; no India registration on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently unavailable (data gap pending resolution). However, based on existing pharmacological literature, chlorzoxazone is recognised as a **BK channel (KCa1.1/KCNMA1) activator** in addition to its classical central muscle relaxant properties. This ion-channel activity provides the key mechanistic bridge to migraine biology.

The biological rationale centres on the **CACNA1A gene**, which encodes the CaV2.1 voltage-gated calcium channel. Gain-of-function mutations in this gene are responsible for both Familial Hemiplegic Migraine Type 1 (FHM1) and spinocerebellar ataxia type 6 (SCA6), establishing CaV2.1 hyperactivation as a shared pathological basis across these neurological disorders. An animal study (PMID 23115190) demonstrated that BK channel activation can counteract neuronal hyperexcitability caused by enhanced CaV2.1 currents in Purkinje cells of CACNA1A-mutant mice — providing an indirect but biologically plausible mechanistic rationale for chlorzoxazone's potential relevance in migraine.

It is important to note that this inference remains at the preclinical and theoretical level. The three supporting publications are reviews and one animal study focused on vestibular/cerebellar disorders that share pathological pathways with migraine, rather than directly evaluating chlorzoxazone as a migraine treatment. No clinical trials have been conducted. The prediction is mechanistically credible but is not yet supported by direct efficacy evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Animal/Experimental Study | The Journal of Neuroscience | **Core mechanistic evidence:** BK channel (Ca²⁺-dependent K⁺ channel) activation alleviates cerebellar ataxia driven by enhanced CaV2.1 currents in CACNA1A (S218L) mutant mice — directly supports BK channel activation as a strategy against CaV2.1 hyperactivity that also underlies FHM1 |
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Narrative Review | Journal of Neurology | Overview of pharmacotherapy for central vestibular and cerebellar syndromes; highlights that ion channel modulators (potassium channel blockers/activators) are effective in disorders driven by aberrant neuronal firing — contextually relevant to migraine pathophysiology |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Narrative Review | Deutsches Ärzteblatt International | Reviews treatment and natural course of vestibular vertigo; identifies vestibular migraine as comprising 11.4% of cases, reinforcing the mechanistic and clinical overlap between cerebellar/vestibular disorders and migraine |

---

## India Market Information

Chlorzoxazone is currently **not marketed in India**. No approved product registrations were found (0 licenses on record). Any future development would require a full regulatory submission to CDSCO.

---

## Safety Considerations

**Drug Interactions (72 interactions identified; key interactions listed below):**

| Severity | Interacting Drug | Clinical Implication |
|----------|----------------|---------------------|
| **Major** | Morphine | Significant CNS/respiratory depression risk; avoid combination |
| **Major** | Morphine (liposomal) | Significant CNS/respiratory depression risk; avoid combination |
| **Moderate** | Ethanol | Additive CNS depression; advise patients to avoid alcohol |
| **Moderate** | Promethazine | Additive CNS sedation |
| **Moderate** | Opium | Additive CNS depression |
| **Moderate** | Dronabinol | Moderate interaction; monitor CNS effects |
| **Moderate** | Nabilone | Moderate interaction; monitor CNS effects |
| **Moderate** | Naltrexone | Moderate interaction |
| **Moderate** | Sibutramine | Moderate interaction |
| **Moderate** | Metoclopramide | Moderate interaction |

> **Note:** Formal prescribing information including warnings and contraindications is pending acquisition from the package insert (TFDA/CDSCO source). This is classified as a **Blocking** data gap and must be resolved before any safety evaluation can be completed. Please refer to the package insert for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.73%) and the mechanistic connection — BK channel activation opposing CaV2.1 hyperactivity via the CACNA1A/FHM1 pathway — is biologically plausible. However, there are no clinical trials and only 3 indirect supporting publications, none of which directly assess chlorzoxazone efficacy in migraine patients. The drug is not currently marketed in India, and critical safety data (package insert warnings and contraindications) remain unavailable. At evidence level L4, advancement to clinical evaluation is premature without foundational preclinical and regulatory groundwork.

**To proceed, the following is needed:**

- **Safety gap (Blocking):** Acquire and review the full package insert to extract official warnings and contraindications before any clinical evaluation can begin
- **MOA confirmation (High priority):** Retrieve and confirm detailed mechanism of action data from DrugBank to substantiate the BK channel activation hypothesis
- **Targeted preclinical studies:** Design and conduct studies specifically testing chlorzoxazone in validated migraine animal models (e.g., cortical spreading depression models, FHM1 CACNA1A knock-in mice)
- **PK/CNS penetration assessment:** Determine whether chlorzoxazone achieves therapeutically relevant CNS concentrations at standard clinical doses, as central BK channel engagement is essential to the proposed mechanism
- **Interaction risk review:** Given 2 major interactions (morphine class) and 8 moderate interactions, a full DDI risk assessment is needed before patient study design, particularly if migraine patients may be using concurrent analgesics or CNS-active agents
- **Regulatory pathway planning:** Since chlorzoxazone has no India registration, establish a regulatory development plan for any future IND/clinical trial application with CDSCO
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

