---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
---

# Pirfenidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Fibroblastic Neoplasm

## One-Sentence Summary

Pirfenidone is an antifibrotic small molecule whose approved use (per cited literature) is idiopathic pulmonary fibrosis. Among 10 TxGNN-predicted indications screened for this drug, only **fibroblastic neoplasm** (covering Dupuytren's disease and FAP-associated desmoid tumor) is supported by actual literature — **6 publications**, no clinical trials — while the other 9 candidates (mastocytosis, dermatofibrosarcoma protuberans, various fibrosarcomas, familial Mediterranean fever, hepatic infarction) returned **zero evidence** and remain at Hold. The evidence for fibroblastic neoplasm itself is mixed: preclinical/cohort support for antifibrotic benefit is counterbalanced by case reports of tumor emergence or aggravation after pirfenidone use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (per literature reference PMID 29702057; not separately recorded in drug-level regulatory data) |
| Predicted New Indication | Fibroblastic Neoplasm (Dupuytren's disease / FAP-associated desmoid tumor spectrum) |
| TxGNN Prediction Score | 99.23% (rank 9 of 10 screened candidates by score; rank 11,911 in full KG output) |
| Evidence Level | L3 (cohort pilot study + preclinical mechanistic studies; no RCTs) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A formal mechanism-of-action record is not available in DrugBank for this drug (data gap). However, the literature evidence collected for this candidate consistently describes pirfenidone as an inhibitor of TGF-β1 and PDGF signaling, which reduces fibroblast-to-myofibroblast transformation, collagen synthesis, and fibroblast proliferation — the pathway pirfenidone was designed to block in pulmonary fibrosis.

Fibroblastic neoplasm and fibroproliferative conditions such as Dupuytren's contracture share the same core biology: TGF-β1-driven myofibroblast activity causing progressive tissue contracture. FAP-associated desmoid tumors are similarly driven by fibroblast proliferation along related growth-factor pathways. This mechanistic overlap is why in vitro studies on Dupuytren's-derived fibroblasts and a pilot cohort in desmoid tumors were undertaken, and why the TxGNN embedding model surfaces this indication.

Importantly, the same anti-fibroblast mechanism that supports a therapeutic rationale also raises a safety question: two independent case reports describe new or worsening fibroblastic/mesenchymal tumors (undifferentiated pleomorphic sarcoma; multiple eruptive dermatofibromas) temporally associated with pirfenidone use. This suggests fibroblast-pathway modulation may not be uniformly protective and could, in some contexts, be associated with tumor promotion — a signal that must be resolved before advancing this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Cohort (pilot) | The American Journal of Gastroenterology | Pilot study of pirfenidone in FAP-associated desmoid tumors; described as a broad-spectrum, noncytotoxic oral antifibrotic blocking TGF-β1, PDGF, EGF, and FGF, aimed at preventing new fibrotic lesion formation |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | Preclinical (in vitro) | BMC Musculoskeletal Disorders | Pirfenidone inhibited TGF-β1-mediated myofibroblast activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | Preclinical (in vitro) | BMC Musculoskeletal Disorders | Pirfenidone modulated TGF-β1-stimulated non-SMAD signaling pathways in Dupuytren's-derived fibroblasts, supporting a mechanistic basis for antifibrotic effect beyond canonical SMAD signaling |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical (formulation) | Pharmaceutical Development and Technology | Local injectable pirfenidone formulation proposed to prevent nodule-to-cord progression in Dupuytren's disease, building on prior in vitro inhibition data |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report (adverse) | The Permanente Journal | Undifferentiated pleomorphic sarcoma reported following pirfenidone use for idiopathic pulmonary fibrosis; long-term oncogenic risk flagged as data-limited |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report (adverse) | Rheumatology (Oxford, England) | Multiple eruptive dermatofibromas aggravated by concurrent mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis |

## India Market Information

Pirfenidone is currently not marketed in India, and no registration/license records exist in the available regulatory data.

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-drug interaction data could not be retrieved (DDI database query failed due to a missing local reference file, and TFDA-equivalent label data is a documented Blocking data gap).

Separately, two literature case reports (not part of the formal safety database) describe new or aggravated fibroblastic/mesenchymal tumors temporally associated with pirfenidone use — this should be treated as an unresolved safety signal specific to any fibroproliferative-tumor indication, distinct from pirfenidone's known IPF-related tolerability profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for fibroblastic neoplasm rests on preclinical studies and one small human pilot cohort (no RCTs), and is counterbalanced by case reports suggesting a possible tumor-promoting signal in fibroblast-driven lesions — a direct conflict with the proposed antifibrotic rationale. Combined with the absence of basic label/safety data (Blocking gap) and no India market presence, the evidence base is not yet sufficient to proceed. The remaining 9 KG-predicted indications for this drug have no supporting evidence at all and should stay at Hold.

**To proceed, the following is needed:**
- TFDA-equivalent product label (warnings/contraindications) — currently a Blocking data gap
- Formal DrugBank-sourced mechanism-of-action record
- Repair of the local DDI reference dataset (ddinter file missing) to complete interaction screening
- Dedicated prospective study (not just retrospective case reports) resolving whether pirfenidone increases or decreases fibroblastic-neoplasm risk before any indication-specific trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

