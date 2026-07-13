---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade (Anaesthesia) to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent (NMBA) widely used intraoperatively and in the ICU to facilitate endotracheal intubation and mechanical ventilation.
The TxGNN model assigns its highest repurposing score to **Cauda Equina Syndrome** (99.99%), yet no supporting clinical trials or published literature exist for this direction.
Across all 10 predicted indications reviewed, evidence consistently yields an **L5 or L4 level with a Hold recommendation**; high TxGNN scores most likely reflect surgical co-occurrence patterns rather than genuine therapeutic signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade to facilitate intubation and mechanical ventilation |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cisatracurium is a benzylisoquinolinium non-depolarizing NMBA that competitively antagonises nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction (NMJ), producing dose-dependent skeletal muscle relaxation. Detailed MOA data from DrugBank was not retrievable at the time of this report due to a data gap; however, this peripheral mechanism is firmly established in the anaesthesia pharmacology literature. Cisatracurium undergoes Hofmann elimination — a pH- and temperature-dependent spontaneous degradation — making it particularly favoured in patients with hepatic or renal impairment.

Cauda equina syndrome (CES) is caused by compression of the lumbosacral nerve roots within the spinal canal, producing a constellation of bladder and bowel dysfunction, saddle anaesthesia, and lower limb weakness. The definitive intervention is urgent surgical decompression; pharmacological muscle paralysis neither relieves nerve root compression nor modifies the underlying neurological injury. Crucially, Cisatracurium acts exclusively at peripheral NMJ sites on skeletal muscle fibres and does not cross the blood–brain barrier or penetrate central neural tissue.

The mechanistic gap is therefore fundamental. Blocking NMJ transmission cannot decompress the cauda equina, reduce epidural haematoma or disc herniation pressure, attenuate neuroinflammation, or restore axonal conductance. The TxGNN model's high score (global rank 308) is most plausibly an artefact of statistical co-occurrence: Cisatracurium is routinely administered as part of general anaesthesia for the very spinal surgeries performed to treat CES, creating a dataset association that carries no therapeutic implication whatsoever.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cisatracurium in Cauda Equina Syndrome.

---

## Literature Evidence

Currently no related literature available for Cisatracurium in Cauda Equina Syndrome.

---

## India Market Information

Cisatracurium currently has **no registered products** in India. Market status: Not Marketed (0 authorisations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data were not available at the time of this report (data gap). DDI database query returned no results due to a missing local database file. The official package insert (CDSCO/TFDA) should be consulted before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature support the use of Cisatracurium for cauda equina syndrome, and there is a fundamental mechanistic mismatch — peripheral NMJ blockade cannot address spinal nerve root compression. The same pattern holds across all 10 TxGNN-predicted indications (cauda equina syndrome, preeclampsia, neurogenic bladder, migraine, thrombotic disease, IBS, migraine with brainstem aura, mild/severe pre-eclampsia, and neurocirculatory asthenia): high model scores but no mechanistic link, with evidence limited to anaesthesia co-occurrence artefacts.

**To proceed, the following is needed:**

- **MOA data gap resolution:** Query DrugBank API (DB00565) for complete mechanism, targets, and pharmacology data
- **Safety data gap resolution:** Download and parse the official package insert PDF to extract warnings, contraindications, and special population precautions
- **DDI database repair:** Restore the missing `ddinter_code_A.csv` file to enable drug–drug interaction screening
- **Hypothesis re-scoping:** If repurposing is a genuine objective, the investigation should pivot away from all 10 current predictions — none demonstrate a plausible therapeutic mechanism — and instead explore pharmacological properties specific to Cisatracurium (e.g., Hofmann elimination in organ-impaired patients, histamine-sparing properties, ICU sedation protocols) as potential differentiation angles
- **India registration pathway:** Confirm whether Cisatracurium is available through import licensing or requires a new CDSCO submission before any clinical development in India can be planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

