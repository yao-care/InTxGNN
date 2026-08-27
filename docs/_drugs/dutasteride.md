---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor (5-ARI) widely used to treat benign prostatic hyperplasia (BPH) and androgenetic alopecia by reducing dihydrotestosterone (DHT) levels.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** — a rare congenital hair disorder — with a prediction score of **99.998%**.
However, **no clinical trials or published literature** currently support this repurposing direction, placing the evidence at the lowest possible level (L5), and critical mechanistic analysis suggests this prediction is **biologically implausible**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) / Androgenetic Alopecia |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (recorded as a High-severity data gap). Based on established pharmacological knowledge, Dutasteride is a dual inhibitor of both Type 1 and Type 2 5α-reductase enzymes. These enzymes convert testosterone into dihydrotestosterone (DHT), which is a significantly more potent androgen. By suppressing DHT levels by approximately 90–95%, Dutasteride effectively reduces prostate volume in BPH and reverses androgen-driven miniaturisation of hair follicles in androgenetic alopecia (AGA).

Ambras type hypertrichosis universalis congenita is a rare X-linked genetic disorder caused by structural chromosomal rearrangements in the 8q22–q24 region, disrupting the regulatory environment of the TRPS1 gene. The pathological mechanism is a congenital developmental defect — the persistence and overgrowth of lanugo-type body hair — entirely driven by chromosomal architecture rather than androgen excess or DHT signalling. There is no known intersection between this disease pathway and the 5α-reductase / DHT axis that Dutasteride modulates.

In practical terms, the TxGNN model's very high prediction score (99.998%) for this indication is most likely an artefact of non-specific "hair follicle–related" node proximity within the knowledge graph, rather than a genuine biological signal. While both Dutasteride's target tissue (hair follicle in AGA) and the disease tissue (hair follicle in Ambras hypertrichosis) share the same anatomical structure, the underlying mechanisms are entirely different. This case illustrates an important limitation of graph-based drug repurposing: high topological proximity in the knowledge graph does not imply mechanistic or clinical relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Dutasteride has **122 recorded drug interactions** (source: DDInter). The most clinically significant are moderate-level CYP3A4-mediated interactions, which can increase Dutasteride plasma exposure:

| Interacting Drug | Level | Clinical Significance |
|-----------------|-------|-----------------------|
| Clarithromycin | Moderate | Strong CYP3A4 inhibitor; may meaningfully raise Dutasteride plasma levels |
| Aprepitant | Moderate | CYP3A4 inhibitor; potential for increased Dutasteride exposure |
| Cimetidine | Moderate | H2 receptor blocker with CYP inhibitory activity |
| Clotrimazole | Moderate | Azole antifungal; CYP3A4 inhibition |
| Miconazole | Moderate | Azole antifungal; CYP3A4 inhibition |

Additional interactions of currently unknown clinical significance have been recorded with Calcitriol, Pantoprazole, Glimepiride, Mesalazine, Doxycycline, Morphine, Metformin, Omeprazole, Rosiglitazone, Lansoprazole, Simvastatin, Prednisone, Hydrocortisone, and others (total: 122 interactions in database).

Please refer to the full package insert for complete warnings and contraindications — these data are currently not available in this Evidence Pack (Blocking-severity data gap: DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical trial evidence and zero published literature supporting Dutasteride's use in Ambras type hypertrichosis universalis congenita. More critically, mechanistic analysis strongly argues against biological plausibility: this condition is a chromosomal structural defect with no known dependence on DHT signalling, meaning Dutasteride's mechanism of action provides no rational therapeutic foothold for this indication.

**To proceed, any future investigation would require:**
- Preclinical evidence (in vitro or animal model) demonstrating a functional link between 5α-reductase / DHT pathways and Ambras-type hypertrichosis biology
- Expert consultation from dermatology geneticists to assess whether any androgen-related modifier pathway exists in this disease
- Full MOA data retrieved from DrugBank (data gap DG002) to confirm or rule out secondary pharmacological activities beyond CYP3A4 metabolism
- TFDA/package insert review (data gap DG001) to obtain complete warnings and contraindications before any safety profiling can proceed
- India regulatory pathway assessment if the drug were eventually to be considered for development — noting that Dutasteride currently has no registered products in India

> ⚠️ **Research Use Only**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. All predictions from TxGNN require prospective clinical verification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

