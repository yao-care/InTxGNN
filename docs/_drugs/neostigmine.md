---
layout: default
title: Neostigmine
parent: Model Prediction Only (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
---

# Neostigmine
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

# Neostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Neostigmine is a reversible acetylcholinesterase inhibitor, originally used to treat myasthenia gravis and other neuromuscular junction diseases.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**, but **no clinical trials and no publications** specific to this subtype were found.
This is essentially a model prediction that sits very close to the already approved indication, not a new repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myasthenia gravis (adult-onset myasthenia gravis; neuromuscular junction disease). Approved indication text is not stated on the Indian registrations compiled for this report |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, neostigmine inhibits acetylcholinesterase, which raises acetylcholine levels at the neuromuscular junction. This compensates for the loss of functional acetylcholine receptors in myasthenia gravis.

Thymic hyperplasia is a common pathological feature of autoimmune myasthenia gravis. The high TxGNN score therefore mainly reflects how close this subtype is to the approved myasthenia gravis indication. It does not point to a genuinely new therapeutic use.

**Other predictions in the top 10 (for context):**
- **Neonatal myasthenia gravis (score 99.97%, Level L4):** Mechanistically coherent, as anticholinesterases have historically been used for supportive care. The supporting literature consists of case reports and reviews with no controlled neostigmine data. It is classed as a research question, and neonatal dosing and safety would need separate review.
- **Limb-girdle autoimmune myasthenia and autoimmune disease of the peripheral nervous system (L4):** These are clinical variants or broad categories that overlap with approved myasthenia gravis. The literature is mostly mechanistic, animal or case-level work.
- **Bronchitis (L4):** Cholinesterase inhibition raises bronchial secretions and muscarinic tone, which is unfavourable in airway disease. The only support is a 1952 single case report.
- **Congenital myasthenia refractory to acetylcholinesterase inhibitors:** By definition these patients do not respond to such drugs, and some forms can worsen with them. This should be treated as a safety flag, not a candidate.
- **Hypersplenism, atypical haemolytic-uraemic syndrome, fetal akinesia sequence, and "disease of receptor activity":** No credible mechanistic link or only indirect or preclinical material was found. These are likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for myasthenia gravis with thymus hyperplasia.

For the neighbouring prediction of neonatal myasthenia gravis, the most relevant items supplied are below. They are indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40544117](https://pubmed.ncbi.nlm.nih.gov/40544117/) | 2025 | Review | Disease-a-month | Comprehensive overview of treatment options in myasthenia gravis |
| [9535308](https://pubmed.ncbi.nlm.nih.gov/9535308/) | 1998 | Case report | Pediatric Neurology | Preterm infant with transient neonatal MG treated with neostigmine, exchange transfusions and high-dose IVIG |
| [35103168](https://pubmed.ncbi.nlm.nih.gov/35103168/) | 2021 | Case report | Cureus | Transient neonatal MG in a newborn of a mother with MG |
| [37453109](https://pubmed.ncbi.nlm.nih.gov/37453109/) | 2023 | Case report | Prilozi | Transient neonatal MG with hypotonia and respiratory distress |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 153909 | Neotroy Injection | Vial of 1 ml injection | Not stated |
| 153984 | Neotroy 0.5mg Injection | Vial of 5 ml injection | Not stated |
| 134666 | Myostigmin 2.5mg Injection | Vial of 5 ml injection | Not stated |
| 152460 | Neomine 0.5mg Injection | Vial of 1 ml injection | Not stated |
| 215485 | Tilstigmin Tablet | Strip of 10 tablets | Not stated |

All 10 registrations are valid single-ingredient products. Nine are injections and one is an oral tablet (Tilstigmin, Tablets India Limited).

## Safety Considerations

- **Diseases linked to contraindication in the knowledge graph (not label text):** epilepsy, peptic ulcer disease, asthma (including intrinsic and allergic asthma), sudden cardiac arrest, heart conduction disease, peritonitis, hyperthyroidism (including Graves disease and thyrotoxicosis), urinary tract obstruction, and Hirschsprung disease and related syndromes (including Mowat-Wilson syndrome).
- **Drug interactions:** 47 interactions were recorded. The one rated **Major** is **bupropion**. The rest of those listed are rated Moderate, including:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide).
  - Anticholinergics and antispasmodics (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, clidinium, methscopolamine, mepenzolate), which may oppose neostigmine's effect.
  - Aminoglycosides (neomycin, kanamycin, paromomycin).
  - Bowel preparations (sodium sulfate, polyethylene glycol with electrolytes, picosulfuric acid).
- **Subtype-specific concern:** In congenital myasthenia refractory to acetylcholinesterase inhibitors, the drug may be ineffective or harmful.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a subtype of myasthenia gravis, which neostigmine already addresses. No trials or literature support it specifically, so the high score reflects model proximity to the approved indication. Of the other predictions, only neonatal myasthenia gravis is a plausible research question, and it needs separate safety review.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text from the Indian registrations (currently a blocking gap for safety screening).
- Detailed mechanism of action data.
- Clarification of whether myasthenia gravis with thymus hyperplasia is a clinically distinct target beyond the existing myasthenia gravis indication.
- For neonatal myasthenia gravis, a dedicated review of neonatal dosing, safety and any controlled evidence.
- Route compatibility assessment (not yet performed).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

