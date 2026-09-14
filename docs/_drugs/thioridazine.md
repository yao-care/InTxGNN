---
layout: default
title: Thioridazine
parent: 僅模型預測 (L5)
nav_order: 825
evidence_level: L5
indication_count: 10
---

# Thioridazine
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

# Thioridazine: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Thioridazine is a phenothiazine-class antipsychotic historically used to treat schizophrenia.
> The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
> but this signal is currently supported only by **0 clinical trials** and **20 historical publications** (mostly case reports and reviews from before 2010), with a blocking safety data gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (based on known phenothiazine pharmacology; no Taiwan license/indication text available in this evidence pack) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (systematic review + case reports/observational literature; no clinical trials) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a drug-level gap (DG002) in this evidence pack, and `original_moa` is not populated. However, the pack's own downstream repurposing analyses for closely related candidates (ranks 2, 4, and 6) consistently describe thioridazine's pharmacology as **D2 dopamine receptor antagonism**, together with α1-adrenergic, M1-muscarinic, and H1-histaminergic antagonism — the classic phenothiazine antipsychotic profile.

The regulatory section shows no Taiwan license records (0 registrations, drug not marketed), so the original indication text cannot be sourced locally; based on known pharmacological class, thioridazine was historically developed and used for **schizophrenia**. Acute mania in bipolar disorder shares overlapping dopaminergic hyperactivity with psychotic states, and D2-antagonist antipsychotics (haloperidol, olanzapine, quetiapine, risperidone) are an established drug class for acute mania — making the mechanistic leap from schizophrenia to manic bipolar affective disorder biologically plausible.

This plausibility is echoed in the surfaced literature: a 1964 case series specifically describes thioridazine combined with pentobarbital/electroshock for "psychomotor excitation and manic reactions," and a 2002 pharmacokinetic study documents thioridazine coadministration in bipolar-disorder patients. However, the closely related "bipolar disorder" candidate (rank 6, score 99.69%) in this same evidence pack explicitly notes that thioridazine's well-known **QTc-prolongation risk** makes it unsuitable as first- or second-line therapy for bipolar-spectrum indications despite mechanistic plausibility — a caveat that should be carried over to this indication as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14252012](https://pubmed.ncbi.nlm.nih.gov/14252012/) | 1964 | Case Series | Annales medico-psychologiques | Combined thioridazine–pentobarbital and electroshock used to treat psychomotor excitation and manic reactions (French, historical) |
| [8448267](https://pubmed.ncbi.nlm.nih.gov/8448267/) | 1993 | Case Report | Biological Psychiatry | Circannual/menstrual rhythm tracking in a schizoaffective patient with mania on maintenance thioridazine |
| [106047](https://pubmed.ncbi.nlm.nih.gov/106047/) | 1979 | Case Report | J Clin Psychiatry | Severe neurotoxicity (delirium, seizures, EEG abnormalities) in 4 cases combining lithium and thioridazine — relevant given lithium's role in bipolar therapy |
| [11910256](https://pubmed.ncbi.nlm.nih.gov/11910256/) | 2002 | Pharmacokinetic Study | J Clin Psychopharmacol | RCT-design PK/safety study of quetiapine coadministered with thioridazine (among others) in schizophrenia/schizoaffective/bipolar patients |
| [3688291](https://pubmed.ncbi.nlm.nih.gov/3688291/) | 1987 | Commentary | Am J Psychiatry | Treatment approaches for rapid cycling bipolar patients (title-level relevance; no abstract) |
| [12676082](https://pubmed.ncbi.nlm.nih.gov/12676082/) | 2003 | Review (safety) | J Family Practice | Safety considerations in treating bipolar disorder (no abstract available) |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Systematic Review | J Clin Psychiatry | Review of typical/atypical antipsychotic efficacy for anxiety symptoms comorbid with bipolar disorder |
| [11336615](https://pubmed.ncbi.nlm.nih.gov/11336615/) | 2001 | Review | Expert Opin Pharmacother | Historical review of antipsychotic classes (chlorpromazine, thioridazine, haloperidol) in non-psychotic psychiatric disorders |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatric Practice | Safety of antipsychotic drug use during pregnancy, including bipolar-spectrum indications |
| [20859110](https://pubmed.ncbi.nlm.nih.gov/20859110/) | 2010 | Review (historical) | J Psychiatric Practice | History of CNS drug development, including early phenothiazine antipsychotics |

---

## Taiwan Market Information

Thioridazine currently holds **no Taiwan marketing authorization** (total registrations: 0; market status: 未上市 / Not Marketed). No license records, product names, or approved-indication text are available in this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: 282 total interactions on record. Notable **Major**-level interactions include **Bupropion**, **Morphine**, and **Lorcaserin**. Numerous **Moderate**-level interactions are also documented (e.g., Acarbose, Famotidine, Epinephrine, Hydrocortisone, Metformin, Amphotericin B, Atropine, Glycopyrronium, Canagliflozin, Chlorpropamide).
- **Class-level cardiac risk (contextual, not from official label data)**: This evidence pack's own analyses of related candidate indications repeatedly flag thioridazine's known **QTc-prolongation / cardiotoxicity** risk (e.g., rank 6 "bipolar disorder" and rank 8 "ADHD" rationale notes), and lithium co-administration case reports document severe neurotoxicity. This should be treated as a material safety signal pending official label confirmation.
- Official TFDA key warnings and contraindications are **not available** in this evidence pack (data gap DG001, severity: Blocking) — this must be resolved before any formal safety evaluation (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (manic bipolar affective disorder) has no supporting clinical trials, only historical case reports and reviews (evidence level L3), and thioridazine is not currently marketed in Taiwan (0 registrations). Most critically, TFDA warning/contraindication data is a **Blocking** gap, meaning formal safety evaluation (S1) cannot even begin — and cross-referenced analysis within this same evidence pack independently flags QTc-prolongation risk for closely related bipolar-spectrum indications.

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) — required before any S1 safety evaluation
- Confirmed original mechanism of action (MOA) from DrugBank, to validate the D2-antagonism rationale currently inferred indirectly
- Cardiac safety workup (QTc data) specific to the manic bipolar affective disorder population
- Updated/contemporary clinical evidence, since current literature predates 2010 for the most directly relevant articles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

