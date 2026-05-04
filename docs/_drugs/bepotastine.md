---
layout: default
title: Bepotastine
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 1
---

# Bepotastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Bepotastine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Bepotastine is a second-generation selective H1 receptor antagonist, originally approved in Japan and Korea for allergic rhinitis, urticaria, and pruritus, but currently not marketed in India.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **1 registered clinical trial** and **12 publications** currently supporting this direction.
Given that its primary pharmacological mechanism directly targets the pathophysiology of allergic urticaria, this prediction carries strong mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, urticaria, and pruritus (approved in Japan/Korea; not registered in India) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available as a formal data gap. However, based on published literature, Bepotastine is a second-generation selective histamine H1 receptor antagonist. It competitively blocks histamine from binding to H1 receptors following mast cell degranulation, and additionally inhibits eosinophil chemotaxis and platelet-activating factor (PAF), providing ancillary anti-inflammatory benefits beyond simple histamine blockade.

The core pathophysiology of allergic urticaria is IgE-mediated mast cell activation leading to histamine release, which causes increased vascular permeability and the characteristic wheals and flares of the skin. H1 receptor blockade is therefore a direct and pharmacologically well-founded treatment mechanism. This is not a repurposing in the traditional sense — it is an extension of a primary drug action to a closely related allergic condition driven by an identical molecular target.

Beyond the mechanism, bepotastine has already obtained approved indications for urticaria in Japan and Korea, and multiple RCTs and surveillance studies have directly investigated its efficacy in chronic urticaria. The TxGNN model score of 99.62% is consistent with this strong mechanistic and clinical alignment. The key opportunity here is India market entry, where no regulatory authorization currently exists.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01897428](https://clinicaltrials.gov/study/NCT01897428) | Phase 1 | Completed | 26 | Randomized, open-label, 2-sequence crossover PK study comparing bepotastine salicylate (Belion, a new formulation) vs. conventional bepotastine besilate in healthy subjects. Established bioavailability equivalence and characterised PK parameters (Cmax, AUC, t½). Supports formulation safety and systemic exposure, but does not directly assess urticaria efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37067147](https://pubmed.ncbi.nlm.nih.gov/37067147/) | 2023 | RCT | Indian Journal of Dermatology, Venereology and Leprology | Head-to-head randomised open-label trial comparing bepotastine besilate vs. levocetirizine in chronic spontaneous urticaria; assessed efficacy and safety in parallel groups. Directly supports the use of bepotastine in urticaria with active comparator evidence. |
| [20687621](https://pubmed.ncbi.nlm.nih.gov/20687621/) | 2010 | Drug Evaluation / Systematic Review | Drugs | Comprehensive review of bepotastine across multiple allergic disorders including chronic urticaria. Concludes that twice-daily bepotastine (20 mg/day) is effective and generally well-tolerated for urticaria, with results from numerous short- and long-term clinical trials. |
| [24191914](https://pubmed.ncbi.nlm.nih.gov/24191914/) | 2013 | Clinical Review | Expert Opinion on Pharmacotherapy | Reviews bepotastine besilate across indications. Notes Japanese oral approval for urticaria and pruritus management, and discusses the anti-pruritic and anti-allergic profile relevant to urticarial presentations. |
| [30208284](https://pubmed.ncbi.nlm.nih.gov/30208284/) | 2018 | Clinical Review | Expert Opinion on Pharmacotherapy | Reviews bepotastine besilate as an H1-antihistamine; documents widespread use for allergic rhinitis and urticaria in multiple countries with efficacy comparable to other second-generation agents. |
| [22035879](https://pubmed.ncbi.nlm.nih.gov/22035879/) | 2011 | Historical Review | Journal of Allergy and Clinical Immunology | Landmark centenary review of histamine and H1-antihistamines. Frames H1-antihistamines as inverse agonists with immunoregulatory effects, providing mechanistic context for bepotastine's action in IgE-mediated conditions including urticaria. |
| [38543228](https://pubmed.ncbi.nlm.nih.gov/38543228/) | 2024 | PK Modelling Study | Pharmaceutics | Population PK and PBPK modelling to determine optimal dosing for paediatric patients with allergic rhinitis or urticaria. Highlights evidence gap in paediatric dosing and proposes weight-based regimens, confirming bepotastine's paediatric utility in urticaria. |
| [24105252](https://pubmed.ncbi.nlm.nih.gov/24105252/) | 2013 | PK Comparative Study | Clinical Drug Investigation | Compares bepotastine besilate vs. bepotastine salicylate PK profiles to support regulatory bioequivalence in a population indicated for allergic rhinitis, urticaria, and pruritus. |
| [27803886](https://pubmed.ncbi.nlm.nih.gov/27803886/) | 2016 | Case Report | Asia Pacific Allergy | Documents a rare case of bepotastine-induced urticaria in a patient originally treated for urticarial symptoms, confirmed by oral provocation. Clinically relevant safety signal: paradoxical antihistamine hypersensitivity should be considered. |
| [19348661](https://pubmed.ncbi.nlm.nih.gov/19348661/) | 2009 | Case Series | The Journal of Dermatology | Reports multiple H1-antihistamine-induced urticaria cases, providing safety context for antihistamine use in chronic urticaria; highlights the rare but real risk of antihistamine hypersensitivity reactions. |
| [32173321](https://pubmed.ncbi.nlm.nih.gov/32173321/) | 2020 | Stability / In Silico Study | Journal of Pharmaceutical Sciences | Forced degradation study of bepotastine besilate with in silico ADMET evaluation of photodegradation products. Relevant for formulation stability and quality control in pharmaceutical development contexts. |

---

## India Market Information

Bepotastine (DB04890) currently has **no registered product licenses in India**. There are no authorized products, dosage forms, or approved indications on record.

This represents a regulatory whitespace opportunity. Bepotastine is commercially available in Japan (as Talion®) and Korea (as Belion®) for allergic rhinitis, urticaria, and pruritus, but a formal New Drug Application (NDA) or regulatory filing with CDSCO would be required before any commercial activity in India.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug-drug interaction records) was not retrievable during evidence collection. No DDI records were found in the queried database.

Based on published clinical literature, the following general safety profile is known:

- **Class-level precautions**: As a second-generation antihistamine, bepotastine has low sedation potential compared to first-generation agents; however, surveillance data indicate some degree of sleepiness may occur in certain patient subgroups.
- **Rare hypersensitivity**: Case reports document paradoxical antihistamine-induced urticaria with bepotastine (PMID 27803886) — a rare but clinically significant safety signal.
- **Paediatric dosing**: No established paediatric dosing guidelines are currently approved; off-label use is common (PMID 38543228).

> Please refer to the originator package insert (Talion® or Belion®) and CDSCO prescribing guidance for complete warnings, contraindications, and precautions before any clinical or regulatory use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of bepotastine for allergic urticaria is mechanistically direct — H1 receptor blockade is the established first-line treatment for urticaria, and bepotastine is already approved for this exact indication in Japan and Korea. An RCT conducted in India (PMID 37067147) directly comparing bepotastine vs. levocetirizine in chronic spontaneous urticaria further strengthens the evidence base. The primary barrier is regulatory, not scientific: bepotastine is not yet registered in India.

**To proceed, the following is needed:**

- **CDSCO regulatory filing**: Prepare a New Drug Application (NDA) for bepotastine besilate, leveraging existing Japanese/Korean regulatory dossiers as reference data packages.
- **India-specific clinical data**: The 2023 RCT (PMID 37067147) was conducted in India — this should be formally incorporated into a regulatory submission to demonstrate local efficacy and safety data.
- **Complete safety dossier**: Retrieve and review the full originator package insert (Talion®/Belion®) to document warnings, contraindications, and drug interactions for CDSCO submission.
- **MOA documentation**: Retrieve DrugBank MOA records for the full mechanistic justification section required in regulatory filings.
- **Paediatric dosing strategy**: Define whether the product will seek a paediatric indication, given the data gap noted in PMID 38543228.
- **Post-marketing surveillance plan**: Given the rare risk of antihistamine-induced urticaria (PMID 27803886), include a pharmacovigilance protocol for hypersensitivity monitoring.

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All findings should be interpreted in the context of formal regulatory and clinical review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

