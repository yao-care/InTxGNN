---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Paliperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

> Paliperidone (9-hydroxyrisperidone, the active metabolite of risperidone) is an atypical antipsychotic already established for schizophrenia. Among the 10 candidate indications TxGNN returned, the nine highest-scoring ones (retinal/genetic/developmental disorders) have **zero clinical trials, zero literature, and no mechanistic link** — they are treated as model noise and excluded. The only evidence-backed candidate is **Treatment-Refractory Schizophrenia**, supported by **4 clinical trials** and **2 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this regulatory dataset (drug not registered/marketed); known pharmacological indication: Schizophrenia / Schizoaffective Disorder |
| Predicted New Indication | Treatment-Refractory Schizophrenia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is a flagged data gap (DG002). Based on known pharmacological classification, paliperidone is a D2/5-HT2A receptor antagonist and the major active metabolite of risperidone, belonging to the atypical (second-generation) antipsychotic class already indicated for schizophrenia.

Unlike a typical cross-disease repurposing case, this prediction is a **within-indication refinement**: the drug's proven efficacy in general schizophrenia is being extended to a treatment-refractory subpopulation, rather than to an unrelated disease. Mechanistically this is plausible on its face, since refractory patients still have the same dopaminergic/serotonergic pathology — but "treatment-refractory" is conventionally defined as failure of ≥2 adequate antipsychotic trials, for which clozapine remains the guideline reference standard, not paliperidone.

The supporting evidence reflects this gap: available trials are either general first-episode/schizoaffective populations, comparator arms in other drugs' trials, or a real-world naturalistic case series of paliperidone palmitate (N=30, completed, Phase 4) that was not restricted to a formally defined refractory population. No randomized trial specifically enrolling refractory patients was identified. This is why the evidence pack assigns L2/S2 rather than a stronger level, and "Proceed with Guardrails" rather than "Go."

*Note on excluded candidates:* the nine higher-scoring predictions (retinal dystrophy with extraocular anomalies, X-linked myopia, syndromic myopia, hydranencephaly, a congenital glycosylation disorder, X-linked myopia 26, a perisylvian polymicrogyria syndrome, CMT type 1G, and atypical glycine encephalopathy) are all rare congenital/genetic/developmental disorders with no clinical trials, no literature, and no plausible connection to a central D2/5-HT2A antagonist. Their own rationale text explicitly labels them as knowledge-graph embedding noise, and they are held at L5/S0/Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating effectiveness of paliperidone palmitate across three schizophrenia patient groups; the most directly relevant trial but not an RCT and not refractory-specific |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | "SchizOMICS": RCT comparing aripiprazole vs. paliperidone/risperidone using multi-omics data in first-episode psychosis; paliperidone appears as a comparator arm |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates pharmacotherapy combined with new recovery-oriented psychosocial programs for treatment-resistant schizophrenia and bipolar disorder; specific antipsychotic not isolated |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared clozapine vs. non-clozapine antipsychotics on inflammatory markers in treatment-resistant schizophrenia; terminated early, low enrollment, indirect relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Review of psychopharmacology evidence for schizoaffective disorder; notes the lack of disorder-specific treatment guidelines |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Review of evidence-informed pharmacological approaches for early-onset schizophrenia spectrum disorders in adolescents |

---

## India Market Information

Paliperidone currently has **no registered licenses** in this dataset (0 of 0 total registrations; market status: Not Marketed).

---

## Safety Considerations

**Drug Interactions**: 235 documented interactions on record. Notable **Major**-level interactions include **Bupropion** and **Morphine** (increased risk of CNS/seizure-related and opioid-related adverse effects). A larger set of **Moderate**-level interactions is also on record, including antidiabetic agents (Metformin, Pioglitazone, Alogliptin, Canagliflozin, Chlorpropamide, Albiglutide), anticholinergics (Atropine, Hyoscyamine, Glycopyrronium), H2-blockers/antacid-related agents (Famotidine), and others (Epinephrine, Hydrocortisone, Amphotericin B, Loperamide, Bisacodyl, Lorcaserin, Acarbose).

Detailed key warnings and contraindications (from labeling) are not yet available in this dataset (DG001, blocking gap) — full safety review (S1) cannot proceed until label data is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paliperidone's efficacy in general schizophrenia is well-established, and mechanistic extrapolation to a refractory subpopulation is biologically plausible, but current evidence consists only of a real-world case series and indirect comparator-arm trials — no RCT specifically targeting a formally defined treatment-refractory population exists yet. The nine other TxGNN candidates in this evidence pack lack any supporting evidence and are excluded from consideration (Hold).

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (DG001) — currently blocking formal safety pre-assessment (S1)
- Formal mechanism-of-action documentation (DG002)
- A prospective trial specifically enrolling patients meeting standard treatment-refractory criteria (failure of ≥2 adequate antipsychotic trials), ideally benchmarked against clozapine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

