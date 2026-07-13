---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Lornoxicam
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

# Lornoxicam: From Pain and Inflammatory Conditions to Rheumatoid Arthritis

## One-Sentence Summary

Lornoxicam is an oxicam-class NSAID (non-steroidal anti-inflammatory drug) with analgesic, anti-inflammatory, and antipyretic properties, established for managing pain and inflammatory conditions.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** as its top-ranked indication (score 99.90%), supported by strong mechanistic rationale — COX-1/COX-2 inhibition reduces synovial PGE2, a core pathway targeted by approved oxicam-class drugs in RA.
However, **no dedicated clinical trials or publications** for this specific drug-indication pair were identified, placing current evidence at **Level L4 (mechanistic/class-analogy only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and inflammatory conditions (analgesic and anti-inflammatory use) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the queried data sources. Based on known pharmacological information, Lornoxicam (also known as chlortenoxicam) is a member of the oxicam subclass of NSAIDs. It inhibits both COX-1 and COX-2 cyclooxygenase enzymes, thereby suppressing prostaglandin synthesis — particularly PGE2 — which mediates pain sensitization and tissue inflammation. A notable pharmacokinetic feature is its relatively short elimination half-life of 3–5 hours, in contrast to longer-acting oxicams such as Piroxicam, which may offer tolerability advantages in chronic dosing scenarios.

Rheumatoid arthritis is a systemic autoimmune disease characterized by persistent synovial inflammation, in which PGE2 overproduction by activated macrophages and fibroblast-like synoviocytes drives joint swelling, pain, and structural damage. NSAIDs, including oxicam-class agents, are standard first-line symptomatic therapy in RA. Crucially, two structurally and mechanistically related oxicam drugs — **Meloxicam** (selective COX-2 preference) and **Piroxicam** (COX-1/2 non-selective) — carry regulatory approvals for RA in multiple markets, providing direct pharmacological class precedent for Lornoxicam's predicted activity in this indication.

The TxGNN prediction is therefore mechanistically well-grounded: the knowledge graph correctly identifies Lornoxicam as belonging to a drug class with established RA utility. The absence of dedicated Lornoxicam-RA clinical trial data most likely reflects historical commercial positioning — Lornoxicam has primarily been developed for acute pain settings (post-operative analgesia, musculoskeletal pain) in markets where it is approved, and long-term RA trials have not been pursued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lornoxicam currently has no registered products with CDSCO in India. The drug is not marketed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic connection between Lornoxicam and rheumatoid arthritis is pharmacologically coherent and supported by class-level analogy (Meloxicam, Piroxicam both oxicam-class, both RA-approved), but no Lornoxicam-specific clinical trial or publication evidence for RA was identified, and the drug carries zero registrations in India — making a go decision premature without foundational data collection.

**To proceed, the following is needed:**
- Retrieve full MOA details and safety profile from DrugBank (DB06725) to complete the mechanistic and safety assessment
- Obtain CDSCO-equivalent package insert or SmPC data for key warnings, contraindications, and drug-drug interactions (DDI file error noted in query log — DDInter database path missing)
- Conduct targeted literature search for Lornoxicam in rheumatoid arthritis and related inflammatory arthropathies (e.g., osteoarthritis, ankylosing spondylitis), as indexed studies may exist outside the current PubMed query scope
- Benchmark against approved oxicam comparators in RA (Meloxicam 7.5–15 mg, Piroxicam 20 mg) to assess whether Lornoxicam's shorter half-life (3–5 h) provides a clinical or safety differentiation rationale
- Map India CDSCO regulatory pathway for a new RA indication — assess whether a bridging study or bibliographic application is feasible given class-level precedent
- Note: Evidence Pack also captured **migraine disorder** (rank #3, L2 evidence, 1 completed Phase 2 RCT [NCT00293657, n=150]) as a higher-evidence repurposing candidate worth parallel evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

