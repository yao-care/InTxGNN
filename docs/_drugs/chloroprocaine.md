---
layout: default
title: Chloroprocaine
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 1
---

# Chloroprocaine
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

# Chloroprocaine: From Local Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Chloroprocaine is a short-acting ester-type local anesthetic used primarily for spinal and epidural anesthesia procedures. The TxGNN model assigned it a high score for **Cauda Equina Syndrome (CES)**, with **1 clinical trial** and **4 publications** found — however, this evidence describes CES as an *adverse event* caused by chloroprocaine, not as a condition it treats. This prediction is a known false-positive driven by adverse-event co-mention in the literature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local / spinal anesthesia (short surgical procedures) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known clinical pharmacology, Chloroprocaine is a short-acting ester-type local anesthetic that blocks voltage-gated Na⁺ channels on neuronal membranes, preventing action potential propagation. It has an exceptionally short duration of action due to rapid hydrolysis by plasma pseudocholinesterase, making it suitable for brief surgical procedures under spinal or epidural anesthesia.

**The core problem: this is a false-positive prediction.** The TxGNN model scored Chloroprocaine highly for Cauda Equina Syndrome because these two terms co-appear frequently in the medical literature — but that co-occurrence reflects a *causative/adverse relationship*, not a *therapeutic one*. High-dose or repeated intrathecal injection of chloroprocaine (particularly older formulations containing bisulfite preservatives) is a documented cause of cauda equina syndrome through direct neurotoxic injury to the lumbosacral nerve roots.

In other words, Chloroprocaine does not treat CES; it can *induce* CES under certain conditions. The single clinical trial retrieved (NCT02067806) monitors CES as a safety endpoint, and all four literature articles describe CES as a complication or adverse event. There is no mechanistic or clinical rationale for repurposing Chloroprocaine to treat CES.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02067806](https://clinicaltrials.gov/study/NCT02067806) | N/A | Completed | 394 | Prospective safety study evaluating 1% 2-chloroprocaine HCl for intrathecal anesthesia; Cauda Equina Syndrome monitored as a neurological adverse event endpoint, not a treatment target |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiologica Scandinavica | RCT comparing chloroprocaine vs lidocaine for selective spinal anesthesia in outpatient TURP; CES not a treatment target |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiologica Scandinavica | Review of 2-chloroprocaine for spinal anesthesia; discusses TNS and CES as neurological complications of intrathecal use |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Review of regional anesthesia complications; chloroprocaine, lidocaine, and procaine implicated in CES etiology |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case Report | Regional Anesthesia | Two cases of CES following spinal-epidural anesthesia; chloroprocaine identified as one of the causative agents alongside lidocaine and procaine |

---

## India Market Information

Chloroprocaine currently has no approved registrations in India (0 licenses on record). This section cannot be populated further.

---

## Safety Considerations

**Drug Interactions** (12 interactions identified):

| Severity | Interacting Drug |
|----------|-----------------|
| **Major** | Nitrous acid |
| **Moderate** | Sulfasalazine, Lidocaine (topical), Benzocaine (topical), Cocaine (nasal), Cocaine (topical), Lidocaine (ophthalmic), Tetracaine (ophthalmic), Oxybuprocaine (ophthalmic), Cinchocaine (topical), Tetracaine (topical) |
| **Minor** | Hyaluronidase |

The major interaction with Nitrous acid and the multiple moderate interactions with other local anesthetics (lidocaine, tetracaine, benzocaine, etc.) reflect additive CNS/cardiovascular toxicity risk when local anesthetics are combined — a clinically important consideration for any spinal anesthesia protocol.

For key warnings and contraindications, please refer to the package insert, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 99.01% for Cauda Equina Syndrome is a **textbook false positive** caused by adverse-event co-mention in the literature. All retrieved evidence — 1 clinical trial and 4 publications — documents CES as a potential *complication* of intrathecal chloroprocaine administration, not as a condition for which the drug has therapeutic benefit. Proceeding with repurposing development would be clinically irrational.

**To convert this Hold, the following would be needed:**
- Identification of a plausible therapeutic mechanism by which chloroprocaine could *treat* CES (currently none exists)
- Preclinical evidence of benefit in a CES animal model (none found)
- A clear biological rationale distinguishing therapeutic use from neurotoxic risk at equivalent or lower doses

**Recommended action:** Flag this candidate as a false positive in the TxGNN pipeline and consider filtering adverse-event co-mentions from the scoring signal to prevent similar artifacts in future predictions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

