---
layout: default
title: Interferon Beta-1A
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1A
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

# Interferon beta-1a: From Multiple Sclerosis to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Interferon beta-1a (IFN β-1a) is a recombinant cytokine biologic widely established for the treatment of relapsing-remitting multiple sclerosis (MS) — though no original indication is formally registered in India's regulatory database.
The TxGNN model ranks **Jeune syndrome situs inversus** as the top predicted new indication, with a score of **97.47%**.
However, **no clinical trials and no relevant literature** exist to support this prediction — the high score is assessed as a knowledge graph topology artifact, not a clinically actionable signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India (no approved licenses on record; known globally for relapsing-remitting MS) |
| Predicted New Indication | Jeune Syndrome Situs Inversus |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no detailed mechanism of action data is available in this Evidence Pack. Based on widely published pharmacology, Interferon beta-1a binds to the heterodimeric IFNAR1/IFNAR2 receptor complex on cell surfaces, activating the JAK1/TYK2 → STAT1/STAT2 → ISGF3 signalling cascade, which drives transcription of interferon-stimulated genes (ISGs). This pathway modulates innate and adaptive immunity — suppressing pro-inflammatory T-cell activity, reducing lymphocyte trafficking across the blood-brain barrier, and upregulating anti-inflammatory cytokines. Its clinical benefit in MS is rooted in immune dysregulation correction, not in structural tissue repair.

Jeune syndrome (asphyxiating thoracic dystrophy) with situs inversus is a ciliopathy — a congenital defect of primary cilia function — manifesting as skeletal dysplasia, restricted thoracic cage development, and, in some cases, situs inversus totalis due to defective cilia-driven left-right patterning in embryogenesis. This is a fixed structural malformation established before birth. The IFN β-1a immune-modulatory pathway has no known mechanism to correct or compensate for germline ciliopathy defects or to reverse situs inversus anatomy.

The TxGNN knowledge graph likely assigns a high score here because ciliary biology nodes (e.g., IFT genes, DNAI1) and immune regulation nodes share indirect edges in the graph topology — a structural artifact rather than a biologically meaningful therapeutic connection. All 10 top-ranked predictions in this Evidence Pack are congenital structural or chromosomal disorders, reinforcing the interpretation that these are systematic graph topology false signals for IFN β-1a, not genuine repurposing opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Interferon beta-1a in Jeune syndrome situs inversus.

---

## Literature Evidence

Currently no related literature available for Interferon beta-1a in Jeune syndrome situs inversus.

> **Note on apparent literature count:** The evidence pipeline retrieved 20 publications under the "disorder of fucoglycosan synthesis" query (rank #4). These have been reviewed and confirmed as false positives — all articles address IFN β-1a in multiple sclerosis, COVID-19, COPD, and ARDS, with zero semantic relevance to fucoglycosan metabolism or the ciliopathy spectrum that includes Jeune syndrome. They are not counted as supporting evidence for any indication in this report.

---

## India Market Information

Interferon beta-1a has **no registered products** in India's drug regulatory database. No authorization numbers, brand names, dosage forms, or approved indications are on record.

---

## Safety Considerations

**Drug Interactions:** A total of **284 drug-drug interactions** have been identified (DDInter database). Clinically notable interactions include:

- **Major severity:** Bupropion — risk of increased adverse effects; combination requires careful clinical assessment
- **Moderate severity (selected):** Rosuvastatin, Simvastatin (hepatotoxicity monitoring recommended); Clarithromycin, Levofloxacin, Minocycline (immunomodulatory overlap); Pioglitazone, Rosiglitazone, Acarbose (glucose metabolism effects in diabetic patients); Naltrexone; Orlistat; Anabolic steroids (Oxandrolone, Oxymetholone, Stanozolol — hepatotoxicity risk)

For complete warnings and contraindications, please refer to the approved package insert (SmPC/Prescribing Information). Formal TFDA labelling data was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no disease-relevant literature, and no mechanistic plausibility linking IFN β-1a to Jeune syndrome situs inversus. The TxGNN high score reflects a knowledge graph topology artifact — indirect cilia/immune node proximity — rather than a translatable therapeutic hypothesis. Additionally, IFN β-1a is not marketed in India, further limiting any near-term repurposing pathway.

**To proceed with any future evaluation of this drug, the following is needed:**

- Obtain the official prescribing information / SmPC for IFN β-1a (Avonex, Rebif, or equivalent) to fill the MOA and safety data gaps
- Run a targeted literature review across **all** ranked indications to identify whether any L3–L4 level mechanistic evidence exists (e.g., IFN pathway involvement in ciliopathies)
- Reassess whether TxGNN graph embeddings for IFN β-1a are over-indexing on immune/structural node co-occurrence — a calibration review of the knowledge graph edges is recommended before generating further candidates for this drug
- If repurposing is still of interest, pivot to indications where IFN β-1a has established biological rationale: autoimmune disorders, viral infections (COVID-19, COPD viral exacerbations), or neurodegenerative conditions with inflammatory components
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

