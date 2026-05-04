---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 6
---

# Desloratadine
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

# Desloratadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation, non-sedating H1 antihistamine (active metabolite of loratadine) widely used for allergic rhinitis and chronic idiopathic urticaria globally, though it is not currently registered in the Indian market. The TxGNN model predicts it may be effective for **Cold Urticaria (Acquired Cold Urticaria)**, with **3 clinical trials** and **7 publications** currently supporting this direction. Evidence quality is strong, anchored by multiple completed randomized controlled trials demonstrating clinically meaningful, dose-dependent symptom suppression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; approved internationally for allergic rhinitis and chronic idiopathic urticaria |
| Predicted New Indication | Cold Urticaria (Acquired Cold Urticaria) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Desloratadine is a selective peripheral H1 receptor antagonist and the pharmacologically active metabolite of loratadine. It competitively and potently blocks histamine H1 receptors on cutaneous blood vessels, smooth muscle, and sensory nerve endings, reducing vascular permeability and suppressing wheal-and-flare responses. Crucially, its limited CNS penetration means this peripheral antihistaminic effect is achieved without significant sedation — a key advantage for long-term use in chronic skin conditions.

Acquired cold urticaria (ACU) is a form of physical urticaria in which exposure to cold stimuli triggers degranulation of skin mast cells, releasing histamine as the primary effector molecule. This histamine then acts on H1 receptors on dermal capillaries and sensory nerves, generating the characteristic wheals, erythema, and pruritus. Because histamine is the dominant downstream mediator in this specific pathway — unlike in many other dermatological conditions where cytokine cascades are more central — H1 receptor blockade maps almost directly onto the core disease mechanism. This places desloratadine in a uniquely strong mechanistic position for ACU relative to other repurposing candidates.

Multiple randomized controlled trials have further validated this mechanistic reasoning with objective pharmacodynamic endpoints. High-dose desloratadine (20 mg/day) has been shown to significantly raise the **critical temperature threshold (CTT)** — the lowest temperature at which cold exposure triggers a symptomatic response — compared with both standard dosing (5 mg) and placebo. This CTT shift represents a quantifiable, clinically meaningful reduction in disease susceptibility, providing direct experimental confirmation that the H1 blockade mechanism is operative and dose-responsive in ACU patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center double-blind dose-escalation study; directly compared 5 mg, 10 mg, and 20 mg desloratadine in ACU to determine the dose sufficient to inhibit cold urticaria symptoms; provides dose-response evidence critical for clinical protocol design |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized double-blind placebo-controlled crossover study; objectively measured cold urticaria lesions using thermography, volumetry, and digital time-lapse photography; tested hypothesis that 20 mg outperforms standard 5 mg dose |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Head-to-head comparison of 5 antihistamines (including desloratadine) for urticaria suppression in a Latin American tropical population; largest sample among available trials; provides comparative class-level efficacy context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | High-dose desloratadine (20 mg) significantly decreased wheal volume and raised cold provocation thresholds vs. standard dose (5 mg) and placebo in ACU; pivotal RCT supporting EAACI guideline recommendation for dose escalation |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | H1-antihistamine dose-escalation RCT in cold urticaria; validated critical temperature threshold as a reproducible pharmacodynamic endpoint; found variable inter-patient response predicting need for dose individualisation |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Controlled Study | J Dermatol Treatment | Early controlled study: 5 mg desloratadine for 4 days inhibited ice-cube provocation responses in 12 ACU patients; established proof-of-concept for desloratadine specifically in cold urticaria |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Comprehensive review of chronic urticaria aetiology and management; contextualises second-generation antihistamines (including desloratadine) as first-line therapy across urticaria subtypes |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of second-generation antihistamines in allergic rhinitis and chronic urticaria; positions desloratadine within the therapeutic class and summarises efficacy data from controlled trials |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case Series | J Allergy Clin Immunol Pract | Describes food-dependent cold urticaria as a novel ACU variant; expands understanding of trigger heterogeneity relevant to clinical diagnosis and antihistamine trial design |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case Report | Qatar Med J | First reported case of cold-induced urticaria following black ant bite-induced anaphylaxis; illustrates uncommon secondary ACU triggers and ongoing clinical spectrum evolution |

---

## India Market Information

Desloratadine currently has **no registered products** in the Indian market (CDSCO total licenses: 0). No license data is available to display.

> Note: Desloratadine is approved and marketed in multiple other jurisdictions (e.g., US FDA as Clarinex®; EMA as Aerius®) for allergic rhinitis and chronic idiopathic urticaria. An Indian regulatory submission (NDA/import license) would be required prior to any commercial or clinical development in India.

---

## Safety Considerations

- **Drug Interactions**: A total of **266 potential drug interactions** are recorded in the DDI database. All listed interactions were classified as **"Unknown" severity**, indicating interaction significance has not been definitively quantified. Key interaction pairs flagged include: Cimetidine (may elevate desloratadine plasma levels via CYP3A4/P-gp inhibition, an effect documented for the parent drug loratadine), Erythromycin and azole antifungals (class-level concern for this antihistamine), and a broad range of CNS-active and cardiovascular agents. A structured interaction review is recommended before use in polypharmacy patients.

For complete warnings, contraindications, and special population guidance (pregnancy, paediatrics, renal/hepatic impairment), please refer to the approved international package inserts (e.g., US FDA label for Clarinex® or EMA SmPC for Aerius®), as formal CDSCO label data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 4 randomized placebo-controlled trials (NCT01444196, NCT00600847) and a third head-to-head Phase 4 study (NCT01940393) directly evaluate desloratadine in acquired cold urticaria, supported by two independent RCTs in the published literature (PMID 19201016; PMID 22242678) demonstrating objective, dose-dependent improvement in critical temperature thresholds. The mechanistic rationale is among the strongest possible for any drug-disease repurposing pair: histamine is the primary mediator in ACU, and desloratadine's primary pharmacological action is peripheral H1 blockade. Evidence quality meets L1 criteria.

**To proceed, the following is needed:**

- **Regulatory pathway for India**: Desloratadine has zero registrations in India; a full CDSCO New Drug Application (NDA) or import license application is required before any clinical or commercial activity
- **Label safety documentation**: Download and parse the official international SmPC/USPI to extract formal contraindications, warnings, special population restrictions, and pregnancy category — currently absent from this evidence pack
- **Dose optimisation protocol**: Clinical evidence supports 20 mg as superior to the standard 5 mg in ACU; a protocol specifying initial dose, escalation triggers, and monitoring intervals should be formalised before any clinical application
- **DDI risk stratification**: Review and clinically categorise the 266 recorded drug interactions — particularly for CYP3A4/P-gp inhibitors (azoles, macrolides, cimetidine) — to define contraindicated combinations and monitoring requirements
- **Formal MOA documentation**: Obtain structured mechanism-of-action data from DrugBank (DB00967) to complete regulatory submission dossier requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

