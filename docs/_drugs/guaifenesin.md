---
layout: default
title: Guaifenesin
parent: High Evidence (L1-L2)
nav_order: 400
evidence_level: L2
indication_count: 5
---

# Guaifenesin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **5** 
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

# Guaifenesin: From Cough/Chest Congestion (Expectorant) to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is a mucolytic/expectorant traditionally used to thin and loosen respiratory mucus secretions (chest congestion, productive cough). The TxGNN model predicts it may also be effective for **Nasal Cavity Disease** (e.g., chronic rhinitis/sinusitis), currently supported by **1 completed Phase 2 pilot trial** and **2 supporting review articles**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan (no TFDA approved-indication text on file); internationally recognized as an over-the-counter expectorant for productive cough |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Guaifenesin is not available in this evidence pack ([Data Gap] on `original_moa`). Based on the repurposing rationale accompanying the prediction, Guaifenesin is a mucolytic/expectorant that reduces the viscosity of mucus secretions and promotes ciliary clearance — its established pharmacological effect in the respiratory tract.

Nasal cavity disease (e.g., chronic rhinitis/sinusitis) shares the same underlying problem of thick, poorly-cleared mucus, just in the upper rather than lower airway. Since Guaifenesin's action is symptomatic mucus-rheology modulation rather than disease-specific, it is mechanistically plausible that the same mucolytic effect could relieve nasal congestion and thick nasal secretions — this is the basis of the TxGNN prediction, and it is echoed by the one existing pediatric pilot trial testing oral Guaifenesin specifically for chronic rhinitis symptoms.

Note that this is a symptomatic/adjunctive mechanism, not a disease-modifying one — it does not address the underlying inflammatory or infectious cause of nasal cavity disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | 14-day randomized, placebo-controlled, masked pilot study of oral Guaifenesin in pediatric chronic rhinitis (ages 7–18), assessing nasal symptom relief (SN-5 survey) vs. nasal airway volume and secretion biophysical properties. Small pilot scale (n=30); provides feasibility/preliminary signal, not definitive efficacy evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review | American Journal of Rhinology | Management review of chronic sinusitis in adult cystic fibrosis patients; discusses medical/surgical management context relevant to mucus-clearance therapy. |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Review on hidden respiratory allergies in voice users; notes decongestant/Guaifenesin combinations as a treatment strategy alongside antihistamines and steroids. |

---

## Taiwan Market Information

Currently not registered in Taiwan (0 licenses on file; market status: Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug-interaction data are currently unavailable — this is flagged as a **Blocking** data gap (DG001) that prevents progression to the S1 safety initial-review stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 indication (Nasal Cavity Disease) has only a single small pediatric pilot trial (n=30) plus two indirectly-related review articles — sufficient to justify further investigation (L2) but not to support progression.
- A **Blocking** data gap (TFDA label/warnings unavailable) prevents entry into the S1 safety review stage, and the drug has no current Taiwan market registration to anchor a local safety profile.
- The four other predicted indications (acute laryngopharyngitis, faucial diphtheria, cervical disc degenerative disorder, papillary conjunctivitis) are all L5 (model prediction only, no trials or literature) and are separately recommended for Hold.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (source: TFDA official site, PDF parsing) — resolves DG001
- DrugBank-sourced mechanism-of-action detail (resolves DG002)
- Confirmation of Taiwan registration/import status for Guaifenesin-containing products
- A larger, adequately powered RCT in adult or broader pediatric chronic rhinitis/nasal cavity disease populations to move beyond pilot-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

