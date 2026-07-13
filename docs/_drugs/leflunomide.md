---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide is a disease-modifying antirheumatic drug (DMARD) primarily used to treat rheumatoid arthritis, acting via inhibition of the DHODH enzyme to suppress immune-mediated inflammation.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**,
however **0 clinical trials** and **0 publications** currently support this direction — the prediction rests entirely on model inference with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (DMARD) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Leflunomide is an immunomodulatory DMARD whose active metabolite **teriflunomide** inhibits **dihydroorotate dehydrogenase (DHODH)** — a key enzyme in the de novo pyrimidine synthesis pathway. By blocking this pathway, Leflunomide suppresses proliferation of activated T and B lymphocytes, reducing autoimmune-driven joint inflammation. It has additionally been noted to possess weak inhibitory activity against fibroblast growth factor receptors (FGFRs) as a secondary effect.

The putative connection to brachydactyly-syndactyly syndrome is speculative. Certain brachydactyly subtypes — most notably Type A2 (BDA2) — are caused by gain-of-function mutations in **FGFR2**. TxGNN may have assigned a high probability score based on the hypothesis that Leflunomide's weak FGFR inhibitory activity could modulate this pathway. However, confidence in this mechanistic bridge is **low** for two fundamental reasons: (1) Leflunomide's FGFR inhibition is a minor, indirect effect rather than its primary pharmacological action; and (2) there is currently no direct evidence linking the DHODH/pyrimidine synthesis pathway to human limb morphogenesis.

Most critically, brachydactyly-syndactyly syndrome is a **congenital structural anomaly** resulting from mutations affecting embryonic limb development. Drug administration after birth cannot reverse established skeletal malformations. Unless the hypothesis is reframed toward prenatal intervention or management of associated systemic features, this repurposing rationale faces a fundamental feasibility barrier.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Leflunomide is currently **not marketed** in India, with no registered product authorizations on record (0 licenses).

---

## Safety Considerations

**Drug Interactions**: Leflunomide has an extensive interaction profile with **677 known interactions** identified. The following represent a subset of flagged interactions:

| Interacting Drug | Level | Class / Note |
|-----------------|-------|--------------|
| Acarbose | Major | Antidiabetic (alpha-glucosidase inhibitor) |
| Pioglitazone | Major | Antidiabetic (thiazolidinedione) |
| Chlorpropamide | Moderate | Antidiabetic (sulfonylurea) |
| Acetohexamide | Moderate | Antidiabetic (sulfonylurea) |
| Hydrocortisone | Major | Corticosteroid |
| Dexamethasone | Major | Corticosteroid |
| Betamethasone | Major | Corticosteroid |
| Triamcinolone | Major | Corticosteroid |
| Budesonide | Major | Corticosteroid |
| Clarithromycin | Major | Macrolide antibiotic |
| Minocycline | Major | Tetracycline antibiotic |
| Metronidazole | Moderate | Antiprotozoal/antibiotic |
| Bupropion | Major | Antidepressant / Smoking cessation |
| Naltrexone | Major | Opioid antagonist |
| Oxandrolone | Major | Anabolic steroid |
| Oxymetholone | Major | Anabolic steroid |
| Chenodeoxycholic acid | Major | Bile acid |
| Acetylsalicylic acid | Major | NSAID / Antiplatelet |
| Zinc sulfate | Minor | Mineral supplement |
| Zinc acetate | Minor | Mineral supplement |

> Please refer to the package insert for complete warnings and contraindications (currently a data gap requiring remediation via the CDSCO/TFDA package insert PDF).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Brachydactyly-syndactyly syndrome is a congenital structural malformation — post-natal pharmacological intervention cannot reverse established skeletal anomalies, and there is zero supporting clinical or preclinical evidence for Leflunomide in this indication despite a high TxGNN score (99.93%).

**To proceed, the following is needed:**

- **Reframe the hypothesis**: Clarify whether the target use case is (a) prenatal FGFR-modulating intervention, or (b) management of associated non-skeletal features (e.g., immune or connective tissue phenotypes), as this fundamentally determines feasibility
- **Preclinical mechanistic evidence**: Studies demonstrating a functional link between DHODH inhibition or weak FGFR modulation and limb patterning during embryogenesis
- **Genetic subtype stratification**: Identify which brachydactyly subtypes (if any) carry FGFR gain-of-function mutations and assess whether these are druggable by weak FGFR inhibitors
- **MOA data gap remediation**: Obtain full target profile from DrugBank (DG002) to assess off-target activities beyond DHODH
- **Safety data gap remediation**: Download and parse the package insert PDF to populate key warnings and contraindications (DG001 — currently Blocking severity)
- **India regulatory pathway assessment**: Since Leflunomide is not currently marketed in India, a full regulatory filing would be required if development proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

