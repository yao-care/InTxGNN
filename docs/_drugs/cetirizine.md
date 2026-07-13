---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 6
---

# Cetirizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation H1 histamine receptor antagonist established for the treatment of allergic rhinitis and related IgE-mediated conditions.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **18 publications** — spanning systematic reviews, direct clinical studies, and pharmacological reviews — supporting this direction.
The mechanistic link is exceptionally strong, as histamine released by mast cells is the primary mediator of urticaria pathophysiology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis (no India registration data on file) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrieved in this evidence pack (DrugBank API query pending). Based on established pharmacological literature, cetirizine is a piperazine-class, second-generation H1 receptor antagonist and the carboxylated metabolite of hydroxyzine. It selectively and competitively blocks peripheral H1 receptors on skin mast cells and basophils, suppressing the IgE-mediated wheal-and-flare response. Critically, cetirizine also inhibits eosinophil chemotaxis during the secondary phase of the allergic cascade — a dual anti-allergic action that extends beyond simple antihistamine blockade (Campoli-Richards et al., *Drugs* 1990; Spencer et al., *Drugs* 1993).

Allergic urticaria and allergic rhinitis share an identical immunological driver: IgE-mediated mast cell degranulation with histamine as the primary effector. This is not a mechanistic leap across disease categories — it is the same H1-receptor axis applied to a different tissue compartment (skin versus nasal mucosa). Multiple landmark clinical studies have directly confirmed cetirizine's efficacy in chronic urticaria (Broide, *Allergy* 1995), and current international guidelines already position second-generation H1 antihistamines as first-line treatment for chronic spontaneous urticaria, with up-dosing to 4× the standard dose permitted if control is insufficient.

The TxGNN score of 99.99% reflects near-perfect mechanism-disease alignment. Rather than a speculative repurposing hypothesis, this prediction represents model confirmation of well-established pharmacology, validating the TxGNN model's ability to capture direct H1-receptor–urticaria mechanistic relationships.

---

## Clinical Trial Evidence

Currently no clinical trials for Cetirizine in Allergic Urticaria are registered in ClinicalTrials.gov or ICTRP in the evidence database.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Critical systematic review of up-dosing second-generation H1 antihistamines (including cetirizine) up to 4× licensed dose in chronic spontaneous urticaria; establishes antihistamine-first strategy per current guidelines |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Trial | Allergy | Direct clinical studies of cetirizine in allergic rhinitis and chronic urticaria — foundational efficacy evidence for this specific drug-disease pair |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Pharmacological Review | Drugs | Comprehensive cetirizine pharmacology review: potent H1 receptor antagonist inhibiting histamine release and eosinophil chemotaxis; controlled trials confirm efficacy in chronic idiopathic urticaria |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Clinical Review | Drugs | Reappraisal of cetirizine: effective and well-tolerated for seasonal/perennial allergic rhinitis and chronic idiopathic urticaria in both adults and children; 10 mg/day appears optimal |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Head-to-head comparison of second-generation antihistamines including cetirizine; evaluates sedation profile, CNS effects, and key clinical differentiators affecting drug choice |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | PK/PD Review | Clin Pharmacokinet | Comparative pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine, and levocetirizine (cetirizine's active R-enantiomer) for allergic rhinitis and chronic idiopathic urticaria |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety review of first- and second-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria; pharmacy-focused management framework |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Urticaria recognition, causes and treatment; nonsedating antihistamines are identified as the mainstay of treatment for chronic idiopathic urticaria |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1 antihistamines in children: Level 1 evidence confirmed for allergic rhinoconjunctivitis and urticaria; cetirizine among agents reviewed |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case Report | Cureus | Rebound pruritus and urticaria following discontinuation of chronic cetirizine use in an Asian patient — emerging safety signal for long-term use management in Asian populations |

---

## India Market Information

Cetirizine currently has **no active registrations** in India based on the regulatory data retrieved for this evidence pack (0 licenses, market status: Not Marketed).

> This finding likely reflects a data retrieval gap rather than true absence from the Indian market — cetirizine (sold globally as Zyrtec, Reactine, and numerous generics) is one of the most widely available OTC antihistamines worldwide and is expected to be marketed in India. Independent verification via the CDSCO drug database is strongly recommended before drawing conclusions about market access.

---

## Safety Considerations

**Drug Interactions**: Cetirizine has 570 known drug interactions on record. Clinically notable moderate-severity interactions include:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Bupropion | Moderate | CNS-related interaction potential |
| Dronabinol | Moderate | Additive CNS depression |
| Loperamide | Moderate | GI/CNS interaction |
| Metoclopramide | Moderate | CNS dopaminergic overlap |
| Morphine | Moderate | Additive CNS and respiratory depression |
| Morphine (liposomal) | Moderate | Additive CNS and respiratory depression |
| Nabilone | Moderate | Cannabinoid CNS additive effect |
| Opium | Moderate | Additive CNS depression |
| Sibutramine | Moderate | CNS serotonergic/adrenergic interaction |
| Difenoxin | Moderate | Antidiarrheal CNS interaction |
| Diphenoxylate | Moderate | Antidiarrheal CNS interaction |

Please refer to the package insert for full warnings and contraindications, as formal warning and contraindication data was not retrieved in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cetirizine's H1-receptor antagonism directly targets the primary pathological mechanism of allergic urticaria — mast cell histamine release — with L1-level systematic review evidence and multiple direct clinical studies confirming efficacy. This is a mechanism-confirmed indication, not a speculative leap, and current international urticaria guidelines already support second-generation antihistamine use as the standard of care.

**To proceed, the following is needed:**
- **CDSCO regulatory verification**: Confirm whether cetirizine is already registered in India (the 0-license finding is likely a data gap) and retrieve the approved indication text and package insert for safety completeness
- **Formal MOA documentation**: Query DrugBank API for DB00341 to complete the mechanistic analysis record
- **Clinical trial gap assessment**: No ClinicalTrials.gov or ICTRP trials for cetirizine + allergic urticaria were retrieved; a manual search of CTRI (Clinical Trials Registry–India) is recommended to identify India-specific evidence
- **Up-dosing safety protocol**: Confirm the 40 mg/day up-dosing threshold (4× standard dose) with appropriate hematological and hepatic monitoring plan for chronic use
- **Asian population safety flag**: Address the 2025 case report signal (PMID 41602253) on rebound pruritus following chronic cetirizine discontinuation, particularly relevant for the India patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

