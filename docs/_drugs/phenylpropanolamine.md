---
layout: default
title: Phenylpropanolamine
parent: Moderate Evidence (L3-L4)
nav_order: 659
evidence_level: L3
indication_count: 5
---

# Phenylpropanolamine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

# Phenylpropanolamine: From Nasal Decongestion to Nasal Cavity Disease

## One-Sentence Summary

Phenylpropanolamine (PPA, DrugBank DB00397) is a sympathomimetic amine historically used as a nasal decongestant and, in some markets, an appetite suppressant; it is not currently marketed in Taiwan and no TFDA license record exists in this evidence pack.
The TxGNN model's top prediction — **Nasal Cavity Disease** — largely restates this known original use rather than identifying a genuinely novel indication, and is currently supported by **1 clinical trial** (testing a different drug) and **3 publications** (1 direct human comparative study, 2 animal models).
Four additional lower-ranked predictions (acute laryngopharyngitis, rosacea conjunctivitis, faucial diphtheria, cervical disc degenerative disorder) have **no clinical or literature evidence** and are flagged in the source rationale as likely knowledge-graph noise or, at best, weak mechanistic analogy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Taiwan: not marketed, no license records). Mechanistic evidence indicates PPA's classic historical use is as a nasal decongestant. |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, regulatory-grade mechanism-of-action documentation for PPA is not available in this evidence pack (flagged as a data gap, DG002). Based on the mechanistic rationale collected alongside the top prediction, PPA is described as a direct-acting α-adrenergic receptor agonist that constricts nasal mucosal vascular smooth muscle — the classic pharmacological basis for a nasal decongestant.

Importantly, the evidence pack itself notes that this mechanism represents PPA's **historical original use category**, not a novel repurposing target: the "prediction" of nasal cavity disease is essentially a rediscovery of well-established pharmacology rather than new therapeutic ground. This should temper enthusiasm about the score despite its high magnitude (99.98%), since TxGNN is confirming known biology rather than surfacing an unexpected signal.

The remaining four predicted indications (laryngopharyngitis, rosacea conjunctivitis, faucial diphtheria, cervical disc degeneration) either rely on distant mechanistic analogy (e.g., comparison to brimonidine's use in rosacea) or have **no plausible pathophysiological link** to α-adrenergic vasoconstriction (faucial diphtheria is a bacterial infection; cervical disc degeneration is a structural orthopedic condition). The source rationale explicitly characterizes these as probable knowledge-graph artifacts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | Randomized, placebo-controlled pilot trial of oral **guaifenesin** (not PPA) for pediatric chronic rhinitis symptom relief. Relevance graded **C**: same disease domain but does not directly test PPA — contextual evidence only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Cohort/Comparative (Tier 1) | American Journal of Rhinology | Direct comparison of oral/topical decongestant effects of PPA vs. d-pseudoephedrine using acoustic rhinometry; establishes PPA's measurable effect on nasal cavity dimensions/architecture. |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | Animal model (feline), Tier 3 | American Journal of Rhinology | Characterizes nasal airway resistance changes in a compound 48/80-induced feline nasal congestion model; establishes the pharmacology platform later used to test decongestants. |
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | Animal model, Tier 3 | American Journal of Rhinology | Combined H1/H3 histamine receptor blockade produces nasal decongestion in the same experimental congestion model; mechanistic supporting context, not a direct PPA study. |

---

## Taiwan Market Information

Phenylpropanolamine currently holds no marketing authorization in Taiwan (market status: Not marketed / Not marketed; 0 registered licenses). No license or product data is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 176 documented interactions on file. Notable **Major**-severity interactions include Bupropion, Lorcaserin, Diethylpropion, and Phentermine (all sympathomimetic/CNS-active agents with additive pressor or serotonergic/adrenergic risk). Numerous **Moderate**-severity interactions were also identified with antidiabetic agents (e.g., Metformin, Acarbose, Alogliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Pioglitazone, Repaglinide, Chlorpropamide, Linagliptin, Dulaglutide, Albiglutide) and bowel-prep agents (Picosulfuric acid, PEG-electrolyte solutions), consistent with PPA's sympathomimetic/glycemic effects.

Detailed TFDA-sourced key warnings and contraindications are not available in this evidence pack (data gap DG001, severity: Blocking) — please refer to the package insert once available. Note also that PPA carries a well-established international regulatory history of hemorrhagic stroke risk that led to withdrawal in several markets; this should be independently verified against TFDA/regulatory sources before any further evaluation, as it is not captured in the structured safety data here.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (nasal cavity disease) mechanistically restates PPA's known original use rather than identifying novel therapeutic ground, is not supported by any completed trial directly testing PPA, and the drug is not currently marketed in Taiwan. A blocking data gap (missing TFDA warnings/contraindications) prevents even an initial safety screen (S1), and the four remaining predicted indications lack any supporting clinical or literature evidence, with two flagged as probable false positives.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert data: key warnings, contraindications (currently blocking)
- Formal DrugBank/MOA documentation to confirm mechanism-relevance claims
- A direct PPA (not guaifenesin) clinical trial or comparative study in a defined nasal cavity disease population
- Independent verification of PPA's historical cardiovascular/hemorrhagic stroke safety profile against current regulatory sources
- Re-evaluation of lower-ranked candidates (ranks 2–5) only if new clinical or literature evidence emerges — current mechanistic links are too weak to justify progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

