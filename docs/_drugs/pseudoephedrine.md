---
layout: default
title: Pseudoephedrine
parent: High Evidence (L1-L2)
nav_order: 705
evidence_level: L2
indication_count: 3
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Pseudoephedrine: From Nasal Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

Pseudoephedrine is an oral alpha-adrenergic agonist long used worldwide as a nasal decongestant, though it currently holds no marketing authorization in India. The TxGNN model assigns its highest prediction score to **Nasal Cavity Disease**, but the supporting evidence indicates this largely reflects the drug's well-established core pharmacology rather than a novel repurposing signal, with **19 clinical trials** and **7 publications** identified in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (drug not marketed in India); internationally known as an oral nasal decongestant |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (DrugBank MOA field) is currently a data gap. However, the evidence pack's repurposing rationale describes pseudoephedrine as a classic **α-adrenergic agonist** that indirectly promotes norepinephrine release, acting on α1-receptors in nasal mucosal vascular smooth muscle to produce vasoconstriction and reduce mucosal congestion and swelling.

This is worth flagging directly: the analysis in the evidence pack itself notes that this α1-adrenergic decongestant action is **textbook-level, well-established pharmacology for pseudoephedrine — not a newly discovered mechanistic link**. TxGNN's very high score (99.75%) for "Nasal Cavity Disease" is therefore best read as the model correctly recovering a known drug-disease relationship rather than surfacing a novel repurposing hypothesis.

That said, because pseudoephedrine has no current marketing authorization in India, formal recognition of this indication would still represent a genuine regulatory gap to close, even though the underlying pharmacology is not new. Supporting clinical evidence (e.g., a Phase 2 trial directly comparing pseudoephedrine to placebo in allergic rhinitis) is consistent with this established decongestant role.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomized, double-dummy, placebo-controlled crossover directly comparing JNJ-39220675 and pseudoephedrine for allergic rhinitis in an environmental exposure chamber |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | H3-receptor antagonist tested against nasal allergen challenge; acoustic rhinometry used to measure congestion, the same endpoint model used for decongestant efficacy |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Evaluated topical anesthesia and/or decongestant pretreatment for reducing discomfort during fiberoptic nasal pharyngoscopy/laryngoscopy |

*Note: 16 additional registered trials returned for this indication (e.g., endoscopic sinus surgery, balloon sinuplasty, nasal spray devices, probiotics) were excluded as they evaluate surgical, device, or unrelated-drug interventions rather than pseudoephedrine itself.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Cohort | American Journal of Rhinology | Direct comparison of oral/topical decongestant effects of phenylpropanolamine and d-pseudoephedrine using acoustic rhinometry |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy and Asthma Proceedings | Overview of nonallergic rhinitis subtypes and their shared congestion/rhinorrhea symptomatology |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Other (animal model) | American Journal of Rhinology & Allergy | Feline model showing decongestant effects of D-pseudoephedrine alone and combined with desloratadine |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Other (animal model) | J Pharmacol Exp Ther | Pharmacological evaluation of α2c-adrenergic agonists in animal models of nasal congestion (mechanistic comparator class) |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Other (animal model) | J Pharmacol Toxicol Methods | Development of a chronic dog model for characterizing nasal decongestant drug mechanisms |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Other (animal model) | American Journal of Rhinology | Acoustic rhinometry validated in a dog model of nasal congestion via mast cell degranulation |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Other (animal model) | American Journal of Rhinology | Ragweed-sensitized dog model of allergic nasal congestion using acoustic rhinometry |

---

## India Market Information

Pseudoephedrine currently holds no marketing authorization in India (0 registered products; market status: Not Marketed). No license records are available for review.

---

## Safety Considerations

**Drug Interactions**: 150 documented interactions on record. Of the sample reviewed, the large majority are **Moderate**-severity interactions with antidiabetic agents — including insulins (human, aspart, degludec), sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), GLP-1 receptor agonists (albiglutide, dulaglutide, exenatide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), alogliptin, and acarbose — consistent with pseudoephedrine's sympathomimetic effect counteracting glycemic control. One **Minor** interaction was noted with ascorbic acid.

Detailed prescribing warnings and contraindications are not currently available in this evidence pack; please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (Nasal Cavity Disease) is supported by a completed Phase 2 RCT directly involving pseudoephedrine and corroborating decongestant-mechanism literature (L2), but the evidence pack itself flags that this reflects known pharmacology rather than a novel signal. Two lower-ranked candidates — acute laryngopharyngitis (L5, Hold, no clinical or literature evidence) and allergic urticaria (L4, Hold, mechanistically weak link) — do not currently meet the bar to proceed.

**To proceed, the following is needed:**
- Formal mechanism-of-action (MOA) documentation from DrugBank (currently a data gap, DG002)
- Package insert warnings/contraindications, particularly given the extensive antidiabetic drug interaction profile (currently a Blocking data gap, DG001)
- Clarification on whether "Nasal Cavity Disease" is intended as a new India regulatory indication or simply confirmation of existing decongestant use, since no original indication is currently on file for India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

