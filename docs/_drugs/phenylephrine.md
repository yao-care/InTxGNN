---
layout: default
title: Phenylephrine
parent: Model Prediction Only (L5)
nav_order: 665
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Phenylephrine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
---

# Phenylephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Phenylephrine: From Allergic Rhinitis and Nasal Decongestion to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is an alpha-1 adrenergic agonist originally used to relieve nasal congestion and related conditions such as allergic rhinitis, the common cold and pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the support is limited: **no registered clinical trials** and **5 publications** (mostly indirect or low-tier) are available.
The prediction overlaps heavily with existing indications, so it is best treated as a research question rather than a new repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, conjunctivitis (atopic, papillary, vernal), headache disorder, hemorrhoid, proctitis (the India licence records contain no approved-indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (L5 would apply to model prediction alone; indirect literature exists, but no completed trials) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, phenylephrine is an alpha-1 adrenergic agonist. It constricts the blood vessels of the nasal mucosa, which reduces swelling, congestion and mucosal bleeding.

This is closely aligned with its established uses in rhinitis, nasopharyngitis and the common cold. "Nasal cavity disease" is a broad category that largely overlaps with these existing indications, which likely explains the very high TxGNN score. It therefore adds little repurposing novelty.

The literature does point to a few niche uses: a topical vasoconstrictor to improve the surgical field in endoscopic sinus surgery, and a component of combination nasal sprays (for example, Polydexa with phenylephrine). The evidence for these is indirect or consists of small clinical or experimental reports.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental and clinical evaluation | Vestnik otorinolaringologii | Safety and efficacy evaluation of Polydexa spray with phenylephrine (a combination with an aminoglycoside antibiotic) in acute rhinosinusitis; aims to support reduced systemic antibiotic use |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Pathogenesis-based approach to treating inflammatory diseases of the nose and paranasal sinuses, including reduction of mucosal hyperaemia and swelling |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Clinical diagnostic article | Vestnik otorinolaringologii | Endoscopic assessment of the nasal mucosa after topical anti-inflammatory and antibacterial therapy, including Polydexa with phenylephrine |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT (triple-blind) | PLoS One | Topical tranexamic acid and bleeding during endoscopic sinus surgery in chronic rhinosinusitis; phenylephrine relevance is indirect |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Arch Ophthalmol | Toxic reactions after intranasal cocaine, with one patient also reacting to intranasal phenylephrine; a safety signal in hypertensive or sympathomimetic-treated patients |

## India Market Information

All 20 registrations are valid single-ingredient licences. The records contain no approved-indication text. The table lists 5 of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 64687 | Dexcare Syrup | Syrup, 100 ml bottle | Not stated in the records |
| 252407 | Zuricof DX Syrup | Syrup, 60 ml bottle | Not stated in the records |
| 117227 | Korf D Syrup | Syrup, 100 ml bottle | Not stated in the records |
| 116618 | Koffrio Tablet DT | Dispersible tablet, strip of 10 | Not stated in the records |
| 117200 | Kofno-Plus Softgel Capsule | Soft gelatin capsule, strip of 10 | Not stated in the records |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** the TxGNN knowledge graph links phenylephrine to contraindications in several disease groups:
  - Cardiovascular: hypertension and hypertensive disorder
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Respiratory: COPD
  - Neurological and psychiatric: epilepsy, insomnia, psychotic disorders including schizophreniform and schizoaffective disorder
  - Endocrine: hypothyroidism, myxedema, Addison disease, adrenocortical insufficiency
  - Gastrointestinal: gastric ulcer, peptic ulcer disease, gastritis, inflammatory bowel disease, pancreatitis, gallbladder disease
  - Other: porphyria, thrombocytopenia, dermatitis herpetiformis
- **Drug Interactions:** 180 interactions were identified, all of the ones listed are rated Moderate. The main groups are:
  - Antidiabetic agents: acarbose, glimepiride, glipizide, glyburide, insulin, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), GLP-1 agonists (exenatide, dulaglutide)
  - Anticholinergics: atropine (ophthalmic), hyoscyamine, clidinium
  - Sympathomimetic anorectic: diethylpropion
- **Literature safety signal:** a 1980 case report describes reactions to intranasal phenylephrine, and the sympathomimetic effect is a concern in patients with hypertensive cardiovascular disease.

Please refer to the package insert for label warnings and contraindications, as these were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication largely overlaps with phenylephrine's existing nasal decongestant uses, so it offers little novelty. The supporting evidence is indirect or low-tier, with no registered trials. Label safety data are also missing. Two other predictions (acute laryngopharyngitis, trigeminal autonomic cephalalgia) are weaker: the first has no evidence at all, and the second rests on diagnostic pupillometry studies, not therapeutic benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved-indication text for the India licences
- Prospective or controlled clinical data in specific nasal cavity diseases (for example, use during endoscopic sinus surgery) that goes beyond current approved uses
- Cardiovascular safety assessment for hypertensive and other at-risk populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

