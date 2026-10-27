---
layout: default
title: Levosalbutamol
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levosalbutamol: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Asthma, bronchial disease"
monitor_inn: "Levosalbutamol"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "bronchitis", "anorectal stricture", "proctitis", "anal polyp", "tracheal disease", "allergic urticaria", "obstructive lung disease"]
---

# Levosalbutamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Levosalbutamol: From Asthma to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Levosalbutamol is the active (R)-enantiomer of salbutamol, a bronchodilator originally used to treat asthma and bronchial disease.
The TxGNN model's top-ranked prediction is **Nasal Cavity Disease**, but this prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.
The best-supported direction among the predictions is **Obstructive Lung Disease** (1 withdrawn trial and 15 publications), which largely overlaps with the existing indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchial disease (approved indication text is not listed in the registration records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, levosalbutamol is the (R)-enantiomer of salbutamol and a selective beta-2 adrenergic agonist. Its efficacy in asthma is established, because it relaxes airway smooth muscle and relieves bronchoconstriction.

For nasal cavity disease, the link is speculative. Any benefit would have to come from effects such as mucosal vasoconstriction or decongestion, and no study supports this. The high score probably reflects the drug's network proximity to other respiratory tract diseases rather than a demonstrated mechanism.

The other predictions follow the same pattern. Pharyngitis, acute laryngopharyngitis, anorectal stricture, proctitis, anal polyp and allergic urticaria have no trials or publications, and no plausible mechanism. Some of these, such as anorectal stricture, are likely model artifacts. Two predictions have more support:
- **Bronchitis** (score 99.97%): bronchodilation is plausible, and one 2023 publication studied a fixed-dose combination of ambroxol, guaifenesin and levosalbutamol for productive cough in acute bronchitis. The contribution of levosalbutamol alone cannot be separated out (Evidence Level L4).
- **Obstructive lung disease** (score 99.85%): this has a strong mechanistic fit, but it is mostly an extension of the existing asthma and bronchial indication rather than true repurposing (Evidence Level L3).

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, nasal cavity disease. The only registered trial in the data compiled for this report relates to the best-supported prediction, obstructive lung disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Phase 3 | Withdrawn | 0 | Ipratropium/levosalbutamol fixed-dose combination (pMDI) versus salbutamol plus ipratropium for acute bronchodilator effects in stable moderate-to-very-severe COPD. No participants were enrolled, so there are no outcome data. |

---

## Literature Evidence

No literature is available for nasal cavity disease. The table below shows selected publications for obstructive lung disease and bronchitis, the better-supported predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41405824](https://pubmed.ncbi.nlm.nih.gov/41405824/) | 2026 | RCT | Indian J Pediatr | Budesonide-formoterol SMART versus budesonide plus as-needed levosalbutamol in children with persistent asthma. The specific role of levosalbutamol is unconfirmed. |
| [17276051](https://pubmed.ncbi.nlm.nih.gov/17276051/) | 2007 | Randomized, double-blind, crossover | Respir Med | Bronchodilator response of levosalbutamol versus salbutamol via pMDI. |
| [36594293](https://pubmed.ncbi.nlm.nih.gov/36594293/) | 2023 | Comparative study | Mymensingh Med J | Levosalbutamol versus racemic salbutamol in acute asthma exacerbation. |
| [20012785](https://pubmed.ncbi.nlm.nih.gov/20012785/) | 2009 | Comparative study | Indian J Pediatr | Efficacy and tolerability of levosalbutamol versus racemic salbutamol in acute asthma exacerbation in children aged 5 to 18 years. |
| [22364295](https://pubmed.ncbi.nlm.nih.gov/22364295/) | 2012 | Review | Expert Opin Pharmacother | Treatment evaluation of levosalbutamol in COPD. |
| [21453221](https://pubmed.ncbi.nlm.nih.gov/21453221/) | 2011 | Review | Expert Opin Pharmacother | (R)-salbutamol in asthma and chronic obstructive airways disease. |
| [17337829](https://pubmed.ncbi.nlm.nih.gov/17337829/) | 2007 | Review | Indian J Pediatr | Evidence-based review of levosalbutamol. |
| [37167145](https://pubmed.ncbi.nlm.nih.gov/37167145/) | 2023 | Combination-product evaluation | Ter Arkh | Ambroxol/guaifenesin/levosalbutamol versus bromhexine/guaifenesin/salbutamol for productive cough in acute bronchitis. |
| [27762515](https://pubmed.ncbi.nlm.nih.gov/27762515/) | 2016 | Cross-sectional cohort | J Assoc Physicians India | Response to levosalbutamol bronchodilatory cough formulations in Indian outpatient settings. |
| [11236808](https://pubmed.ncbi.nlm.nih.gov/11236808/) | 2001 | Review | Clin Pharmacokinet | Pharmacokinetics of levosalbutamol and its clinical implications. |

---

## India Market Information

Levosalbutamol is marketed in India as a single-ingredient product with 20 valid registrations. The approved indication text is not listed in the registration records. The main registrations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121411 | Levolin Synchrobreathe Inhaler (Cipla Ltd) | Box of 120 MDI inhaler | Not listed |
| 120835 | Levolin 50mcg Inhaler (Cipla Ltd) | Packet of 200 MDI inhaler | Not listed |
| 199887 | Salbair 50mcg Transhaler (Lupin Ltd) | Packet of 250 MDI Transhaler | Not listed |
| 151733 | Nebulair Respules 2ml (Dr Reddy's Laboratories Ltd) | Strip of 7 respules | Not listed |
| 224595 | Tiecuf L Syrup (Indica Biolife Sciences) | Bottle of 100 ml syrup | Not listed |

Other registered forms include oral syrups, oral drops and nebulizer respules.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** Disease associations include hypertension and hypertensive disorder, long QT syndrome, heart conduction disease, sudden cardiac arrest, coronary artery disease, epilepsy, potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease and thyrotoxicosis.
- **Drug Interactions:** 146 interactions were identified. Examples include:
  - Moderate: epinephrine, ephedrine, isometheptene, famotidine, clarithromycin, cisapride, dolasetron, palonosetron, phentermine, diethylpropion, and inhaled rapid-acting insulin.
  - Minor: corticosteroids such as hydrocortisone, dexamethasone, budesonide, beclomethasone, betamethasone and triamcinolone.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, nasal cavity disease, rests on the model score alone, with no trials, no literature and no established mechanism. The best-supported prediction, obstructive lung disease, is largely an extension of the existing asthma and bronchial indication rather than a new one. Its only registered trial was withdrawn with no participants, so no completed Phase 3 trial confirms it.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which are required for safety screening
- Detailed mechanism of action data (MOA)
- Any preclinical or clinical evidence for nasal cavity disease, such as mucosal decongestion studies
- Full-text review of the comparative trials (PMIDs 36594293, 20012785, 17276051), which could support an upgrade of the obstructive lung disease evidence level to L2 or L1
- Confirmation of levosalbutamol's role in the 2026 SMART trial (PMID 41405824)
- Assessment of route compatibility, since the available routes (inhaled, oral, nebulized) have not been matched to the routes required for the predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

