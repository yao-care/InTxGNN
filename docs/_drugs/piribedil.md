---
layout: default
title: Piribedil
parent: 僅模型預測 (L5)
nav_order: 672
evidence_level: L5
indication_count: 5
---

# Piribedil
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

# Piribedil: From Parkinsonian Motor Disorders to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Piribedil is a D2/D3 dopamine receptor agonist used internationally (including France, China, and Russia) for Parkinson's disease and related dopaminergic motor disorders, though it currently holds no market authorization in Taiwan. The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, a congenital ophthalmologic syndrome, but this candidate is supported by **zero clinical trials** and **15 tangentially-related publications**, none of which actually discuss Piribedil. The evidence pack's own mechanistic review flags this top prediction as a likely knowledge-graph embedding artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory records (drug not marketed, no license data). Contextually, Piribedil is documented elsewhere as a dopamine agonist approved for Parkinson's disease. |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, formally catalogued mechanism-of-action data for this candidate profile is currently a data gap. However, contextual information captured elsewhere in this evidence pack indicates Piribedil is a D2/D3 dopamine receptor agonist that crosses the blood-brain barrier to act on striatal dopaminergic pathways — the basis for its established use in Parkinson's disease in several countries.

The proposed link to retinal dystrophy with extraocular anomalies is considerably weaker. The retina does contain a small population of dopaminergic amacrine cells involved in light adaptation, which offers a theoretical, indirect connection to dopaminergic pharmacology. However, this predicted indication is a congenital, genetically-driven developmental disorder of the retina and extraocular structures — a fundamentally different disease category from Piribedil's striatal dopamine-replacement mechanism, with no established causal or therapeutic pathway between the two.

Taken together, the model's own mechanistic assessment in this pack characterizes the high TxGNN score as likely reflecting embedding-space similarity in the knowledge graph rather than genuine biological plausibility. Notably, other lower-ranked candidates in this same prediction set (juvenile Parkinsonism variants) show much stronger mechanistic coherence with Piribedil's known dopaminergic activity, but those carry zero clinical trial or literature support in the current dataset and are outside the scope of this report's headline prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections secondary to sinusitis; no drug relevance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia evaluation; no drug relevance |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis pathophysiology and workup; no drug relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies; no drug relevance |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome vitreoretinal degeneration; no drug relevance |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging classification of pediatric orbital/ocular pathologies; no drug relevance |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Case series of orbital arteriovenous malformations; no drug relevance |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia; no drug relevance |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Isolated congenital trochlear-oculomotor synkinesis case; no drug relevance |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case; no drug relevance |

**Note:** These 10 publications matched the search query on disease-term overlap only — none of them discuss Piribedil, dopaminergic therapy, or any pharmacological intervention. They should not be interpreted as supporting evidence for this repurposing candidate.

---

## India Market Information

Piribedil currently has no market authorization records in this dataset — market status is **Not Marketed**, with 0 registered licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this dataset; local label data acquisition is flagged as a blocking data gap — DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the underlying mechanistic link between Piribedil's striatal dopamine-agonist activity and this congenital retinal/extraocular developmental disorder is weak and plausibly a knowledge-graph artifact. No clinical trials and no drug-specific literature support this indication, and the drug has no current market presence or safety label data in Taiwan.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) — currently a blocking data gap (DG001)
- Verified original indication and mechanism-of-action data from DrugBank (DG002)
- If pursuing repurposing further, prioritize re-scoping evidence collection toward the mechanistically coherent Parkinsonism-related candidates in this same prediction set (e.g., juvenile Parkinson disease variants), which align with Piribedil's known dopaminergic pharmacology but currently lack any trial or literature evidence in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

