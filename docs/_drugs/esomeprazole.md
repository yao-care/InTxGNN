---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 3
---

# Esomeprazole
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

# Esomeprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole (Nexium) is the S-isomer of omeprazole — a proton pump inhibitor (PPI) with established efficacy in gastro-oesophageal reflux disease (GERD), reflux esophagitis, and Helicobacter pylori eradication.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux** with a score of 99.53%, currently supported by **0 clinical trials** and **1 narrative review** specifically for this indication.
Notably, the closely related indication of **duodenal ulcer** (TxGNN rank 3) carries robust **L1 evidence** from multiple completed Phase 3 RCTs, reflecting the drug's well-established acid-suppression pharmacology across the gastroduodenal spectrum.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | GERD, reflux esophagitis, H. pylori eradication, NSAID-associated ulcer prevention (no registered product found in India market) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on published literature, Esomeprazole is a proton pump inhibitor (PPI) that irreversibly blocks the H⁺/K⁺-ATPase enzyme on gastric parietal cells, dramatically reducing acid secretion and prolonging intragastric pH above 4. As the S-isomer of omeprazole, it achieves more consistent pharmacokinetic exposure than its racemate, which translates to superior acid control in head-to-head trials.

The mechanistic connection to duodenogastric reflux is **indirect and only partially plausible**. Duodenogastric reflux is characterised by the retrograde movement of bile and duodenal contents into the stomach — the primary pathological agent here is bile, not acid. PPI therapy has no direct pharmacological mechanism to block bile reflux. However, in mixed-reflux scenarios where acid and bile act synergistically to damage the gastric mucosa, reducing acid may attenuate the co-injury effect, providing some clinical benefit.

The TxGNN model's very high prediction score (99.53%) most likely reflects the dense knowledge-graph connections between esomeprazole and the broader family of acid-related gastroduodenal diseases — including GERD, peptic ulcer, and reflux esophagitis — rather than a validated mechanistic pathway specific to duodenogastric reflux. This prediction should therefore be interpreted with caution and treated as a hypothesis-generating signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Esomeprazole in duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Narrative Review | European Journal of Clinical Pharmacology | Comprehensive PPI update confirming esomeprazole as first-line for peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome; duodenogastric reflux is not addressed as a distinct indication |

---

## India Market Information

No registered products found. Esomeprazole holds no approved licenses on record in the India market within this dataset.

---

## Safety Considerations

**Drug Interactions (168 total identified; key interactions listed below):**

| Interacting Drug | Severity |
|-----------------|---------|
| Acalabrutinib | Major |
| Atazanavir | Major |
| Abametapir (topical) | Moderate |
| Apalutamide | Moderate |
| Armodafinil | Moderate |
| Bosutinib | Moderate |
| Atorvastatin | Moderate |
| Amphotericin B | Moderate |
| Hydrochlorothiazide | Moderate |
| Acetylsalicylic acid | Minor |

> Key warnings and contraindications data are not available in this evidence pack. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Esomeprazole's TxGNN prediction score for duodenogastric reflux is extremely high (99.53%), the mechanistic link is indirect (acid suppression does not directly address bile reflux), there are no dedicated clinical trials for this indication, and the sole supporting publication is a general PPI narrative review with no specific duodenogastric reflux data. The evidence is insufficient to advance beyond hypothesis generation at this stage.

**To proceed, the following is needed:**
- Dedicated prospective clinical studies or RCTs evaluating esomeprazole specifically in duodenogastric (bile) reflux populations
- Mechanistic studies clarifying whether acid suppression meaningfully modifies outcomes in isolated versus mixed (acid + bile) reflux
- Complete MOA data from DrugBank (DG002 remediation) to support or challenge the mechanistic rationale
- TFDA/CDSCO package insert review to fill the warning and contraindication data gap (DG001 remediation)
- Consider whether the L1-evidence duodenal ulcer indication (TxGNN rank 3) represents a higher-priority repurposing opportunity that warrants a separate regulatory evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

