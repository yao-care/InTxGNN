---
layout: default
title: Caffeine
parent: Moderate Evidence (L3-L4)
nav_order: 130
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis…"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Caffeine: From Allergic Rhinitis and Headache Disorders to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a long-established stimulant and analgesic adjuvant, originally used in products for allergic rhinitis, the common cold, pharyngitis and headache disorders such as migraine and cluster headache.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **3 publications**, none of which directly tests caffeine in a nasal disease.
The evidence supports this direction only weakly, and the prediction partly overlaps with existing labeled uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis, common cold, headache disorders (the data compiled for this report contains no approved indication text from the product licences, so this reflects knowledge-graph indications) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, caffeine is an adenosine receptor antagonist and phosphodiesterase inhibitor. It is mainly used in combination products for colds and rhinitis, and its efficacy as an analgesic adjuvant is well established.

Nasal cavity disease is closely related to the existing indications (allergic rhinitis, vasomotor rhinitis, common cold, nasopharyngitis). The high TxGNN score likely reflects this proximity in the knowledge graph rather than a truly new therapeutic signal. A review of bitter taste receptors suggests these receptors are expressed in human airway and nasal tissue and may modulate innate defence, which offers a plausible but speculative mechanistic link.

The only nasal-specific paper concerns an intranasal caffeine gel for cognition after sleep deprivation. That is a drug-delivery study and not a nasal disease indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in airway and nasal tissue and may play a role in airway defence |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical/formulation study | Current Drug Delivery | Thermo-sensitive intranasal caffeine gel for cognition after sleep deprivation; not a nasal disease treatment |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited lung tumours in rats; not relevant to nasal disease |

---

## India Market Information

Caffeine is marketed in India as 20 valid single-ingredient registrations, all oral tablets (strips of 10). The data compiled for this report contains no approved indication text for these products. Most product names suggest cold and allergy preparations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 209998 | Snokey Cold Plus Tablet | Strip of 10 tablets | Not available |
| 202438 | Signcold Tablet | Strip of 10 tablets | Not available |
| 150830 | NT Grain Tablet | Strip of 10 tablets | Not available |
| 235665 | Vinoryl Tablet | Strip of 10 tablets | Not available |
| 144331 | Makzine P Tablet | Strip of 10 tablets | Not available |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text): hypertension, orthostatic hypotension, long QT syndrome, postural orthostatic tachycardia syndrome, multiple system atrophy, epilepsy, insomnia, anxiety disorder, liver disease and liver failure, kidney disease, peptic or gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, COPD, hypothyroidism, porphyria, and thrombocytopenia.
- **Drug Interactions**: 75 interactions were identified. The main ones listed are:
  - **Major**: nasal cocaine and topical cocaine
  - **Moderate**: alosetron, obeticholic acid, abametapir (topical), adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole, duloxetine
  - **Minor**: acetylsalicylic acid, cimetidine, atazanavir, disulfiram
- **Other cautions from the literature**: caffeine can contribute to medication-overuse headache and sleep disruption, and its cardiovascular effects need care.

Package insert warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on the TxGNN score, with no clinical trials and no literature directly testing caffeine in nasal cavity disease. The indication also largely overlaps with existing labeled uses (rhinitis and the common cold), so it is not a clear new repurposing signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, which is a blocking gap for safety screening
- Detailed mechanism of action data
- Approved indication text for the registered products, to clarify the overlap with nasal cavity disease
- Clear definition of which nasal conditions are targeted beyond rhinitis and the common cold
- Direct clinical or mechanistic evidence for caffeine in nasal disease

---

### Other Predicted Indications Noted (for reference)

Among the other predictions, **hypnic headache** (L4, score 99.17%) has the most supportive evidence, including reviews describing caffeine as a first-line option based on case reports and series. It is flagged as a research question and needs guardrails because of medication-overuse headache and sleep disruption. **Neuralgia** (L4) has only preclinical support for caffeine as an analgesic adjuvant. Thrombotic disease and vein disease have indirect, inconsistent evidence and raise cardiovascular safety concerns. The remaining predictions (acute laryngopharyngitis, papillary conjunctivitis, glossodynia, coccygodynia) rest on model prediction alone (L5).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

