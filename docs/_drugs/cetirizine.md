---
layout: default
title: Cetirizine
parent: Model Prediction Only (L5)
nav_order: 166
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Cetirizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis (other listed indications: vasomotor rhinitis…"
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation antihistamine, originally used for allergic rhinitis, conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **1 clinical trial** and **18 publications** currently supporting this direction. This is better viewed as an extension within the same disease family than as true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other listed indications: vasomotor rhinitis, pharyngitis, common cold, atopic/papillary/vernal conjunctivitis, nasopharyngitis, idiopathic urticaria) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (conditional, see below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cetirizine is a second-generation H1-receptor antagonist. Its efficacy in allergic rhinitis and idiopathic urticaria is well established, and mechanistically it is applicable to allergic urticaria.

Histamine released from mast cells drives wheal and flare formation in allergic urticaria, so H1 blockade directly addresses the underlying pathophysiology. The predicted indication is closely related to idiopathic urticaria, which is already an original indication.

The literature also describes cetirizine as inhibiting eosinophil chemotaxis and histamine release during the allergic response. Reviews describe antihistamines as the mainstay of urticaria treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Randomized, double-blind pilot study of IV cetirizine (10 mg) vs IV diphenhydramine (50 mg) in acute urticaria in emergency departments, urgent care and allergy clinics. It assessed feasibility of a larger Phase 3 trial rather than definitive efficacy. |

The L1 rating is conditional. This is a small pilot study using an IV route, so it does not by itself establish Phase 3 RCT-level efficacy. The rating rests mainly on the broader antihistamine literature and the existing urticaria indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Cetirizine is effective and well tolerated in seasonal/perennial allergic rhinitis and chronic idiopathic urticaria in adults |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Pharmacology and clinical potential in allergic rhinitis, pollen-induced asthma and chronic urticaria; no CNS depressant effects at 10 mg |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of oral antihistamines in allergic rhinitis and chronic idiopathic urticaria |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Non-sedating antihistamines are the mainstay of treatment for most chronic idiopathic urticaria |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Review | Allergy | Clinical studies of cetirizine in allergic rhinitis and chronic urticaria |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Levocetirizine (the R-enantiomer of cetirizine) in allergic rhinitis and chronic idiopathic urticaria |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine in allergic rhinitis and chronic idiopathic urticaria in adults and children |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Case of cetirizine-induced cholestasis; transient transaminase elevations in <2% of patients in US trials |

The evidence is mostly reviews, including several on related antihistamines (levocetirizine and others), rather than direct trials in allergic urticaria.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12883 | Acrecet 10mg Tablet | Strip of 10 tablets | Not specified |
| 205627 | Stencold Syrup | Bottle of 30 ml syrup | Not specified |
| 116914 | Kolcare Tablet | Strip of 10 tablets | Not specified |
| 51370 | Cetrish 10mg Tablet | Strip of 10 tablets | Not specified |
| 52831 | Cetnir Syrup | Bottle of 60 ml syrup | Not specified |

There are 20 valid single-ingredient registrations in total. Dosage forms include tablets, dispersible tablets, capsules and syrups.

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (not label text): the drug-disease contraindication edges list hypertension, kidney disease (including chronic and end-stage), liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (including Graves disease). These should be verified against the package insert.
- **Drug interactions**: 570 interactions were identified. Those rated moderate include bupropion, dronabinol, loperamide, metoclopramide, morphine, nabilone, opium, sibutramine, difenoxin and diphenoxylate. Several others have an unknown severity level (for example calcitriol, pantoprazole, glimepiride and doxycycline).
- **Literature signal**: a case report describes cetirizine-induced cholestasis, and transient transaminase elevations have been reported in under 2% of trial patients.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is directly relevant, and cetirizine is already approved for closely related urticaria. However, the only trial is a small IV pilot study, and the supporting literature is largely review-based, so the L1 rating is conditional.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (currently missing and blocking for safety screening)
- Detailed mechanism of action data
- Approved indication text for the Indian registrations
- Confirmation of efficacy in allergic urticaria from oral-route RCTs, or from the pivotal results of the IV cetirizine program
- A safety monitoring plan for patients with liver or kidney impairment and for those on interacting CNS-active drugs

### Other Predicted Indications (for reference)

| Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|
| Cold urticaria | 99.95% | L3 | Proceed with Guardrails |
| Nasal cavity disease | 99.77% | L4 | Research question (term too broad) |
| Acute laryngopharyngitis | 99.72% | L5 | Hold |
| Rosacea conjunctivitis | 99.41% | L5 | Hold |
| Recalcitrant atopic dermatitis | 99.19% | L5 | Hold |

Cold urticaria has the strongest secondary signal: clinical studies show cetirizine reduced cold-induced wheals (by about 50% in one small study), and antihistamines are first-line therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

