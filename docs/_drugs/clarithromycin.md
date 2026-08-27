---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 5
---

# Clarithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Clarithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin (DrugBank ID: DB01211) is a well-known macrolide antibiotic; however, this evidence pack does not contain specific original indication or mechanism-of-action (MOA) data (both flagged as data gaps). The TxGNN model predicts a possible association with **Hyperamylasemia**, but this is currently supported by only **1 case report** and **0 clinical trials**, and the underlying rationale suggests the signal is likely a knowledge-graph co-occurrence artifact rather than a genuine treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (Clarithromycin is generally known as a macrolide antibiotic; `original_indications` field is empty) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Clarithromycin in this evidence pack (flagged as a High-severity data gap). Based on general knowledge, Clarithromycin is a macrolide antibiotic, and its efficacy against susceptible bacterial infections is well established; mechanistically, macrolides also carry secondary anti-inflammatory and immunomodulatory properties, which is the basis some repurposing predictions rely on.

However, in this specific case, Hyperamylasemia is a laboratory finding (elevated serum amylase) rather than an independent disease entity — it is typically seen in the context of pancreatitis, salivary gland disorders, or as a drug-related side effect. The only supporting literature is a 2004 case report describing a patient with *Mycobacterium abscessus* lung infection complicated by primary macroamylasemia, in which clarithromycin was used as an anti-mycobacterial agent — not as a treatment directed at hyperamylasemia itself.

Given this, the repurposing rationale explicitly flags this prediction as **highly suspected to be a false positive** arising from co-occurrence patterns in the knowledge graph (i.e., the drug and the lab abnormality appearing together in the same clinical record/literature), rather than a mechanistically grounded therapeutic signal. This should be treated as a hypothesis-generating observation only, not a validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case Report | Nihon Kokyuki Gakkai zasshi (Journal of the Japanese Respiratory Society) | Case of *M. abscessus* lung infection complicated by primary macroamylasemia in a 76-year-old man with prior tuberculosis; clarithromycin was part of anti-mycobacterial treatment, not directed at the hyperamylasemia finding itself. |

---

## India Market Information

No registration/licensing data available — Clarithromycin currently has **0 registered licenses** and is marked as **not marketed** in this jurisdiction (`total_licenses: 0`, `licenses: []`).

---

## Safety Considerations

**Drug Interactions**: A total of **822 documented interactions** were identified for Clarithromycin. Notable **Major**-severity interactions include:
- **Abemaciclib** (Major)
- **Fentanyl** (Major)
- **Acalabrutinib** (Major)

Several **Moderate**-severity interactions were also identified, including Abiraterone, Paclitaxel, Acarbose, Tramadol, Famotidine, Formoterol, Nifedipine, Adenosine, Trastuzumab emtansine, Flunisolide, Afatinib, Ethinylestradiol, and Hydrocortisone, among others.

Detailed key warnings and contraindications from the product label (TFDA-equivalent source) are not currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety-stage (S1) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for the Clarithromycin–Hyperamylasemia association is a single low-tier case report describing an unrelated primary treatment context, with no clinical trials and no mechanistic data to substantiate a direct therapeutic link. The repurposing rationale itself flags this as a likely knowledge-graph co-occurrence artifact rather than a genuine signal, and evidence strength (L4) does not meet the bar for advancing to a research question or pilot stage.

**To proceed, the following is needed:**
- Resolution of Blocking data gap DG001 (TFDA/product label warnings and contraindications) before any safety-stage (S1) review is possible
- Resolution of High-priority data gap DG002 (confirmed mechanism of action) to assess biological plausibility
- Independent mechanistic or preclinical studies specifically linking clarithromycin to amylase regulation or pancreatic/salivary pathophysiology (not just co-occurrence in unrelated case reports)
- Note: four additional lower-ranked candidates (polyclonal hyperviscosity syndrome, congenital analbuminemia, punctate epithelial keratoconjunctivitis, blood group incompatibility) were also screened in this evidence pack; all were rated L5/Hold except punctate epithelial keratoconjunctivitis (L3, "Research Question" stage via class-effect extrapolation from azithromycin literature), and none currently support progression beyond exploratory review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

