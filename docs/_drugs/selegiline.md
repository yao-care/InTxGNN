---
layout: default
title: Selegiline
parent: High Evidence (L1-L2)
nav_order: 759
evidence_level: L2
indication_count: 4
---

# Selegiline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

# Selegiline: From Parkinson's Disease to Schizophrenia (Negative Symptom Augmentation)

## One-Sentence Summary

> Selegiline is a selective, irreversible MAO-B inhibitor originally approved for **Parkinson's disease (oral)** and **major depressive disorder (transdermal, in other jurisdictions)**.
> The TxGNN model predicts it may be useful as an **augmentation therapy for schizophrenia negative symptoms**,
> with **1 completed clinical trial** and **20 publications** (including two placebo-controlled RCTs) currently supporting this direction.
>
> Note: TxGNN's top-ranked candidate ("polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis") and two other high-scoring candidates (a congenital glycosylation disorder, and a retinal dystrophy syndrome) were screened out — they have no supporting clinical/literature evidence and no plausible mechanistic link to MAO-B inhibition. They are flagged in the evidence pack itself as likely knowledge-graph topology artifacts ("noise matches"), not real repurposing signals. This report therefore focuses on the schizophrenia candidate, the only one with actual evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in India; per literature (PMID 37087864), approved elsewhere for Parkinson's disease (oral) and major depressive disorder (transdermal) |
| Predicted New Indication | Schizophrenia (negative symptom augmentation of antipsychotics) |
| TxGNN Prediction Score | 99.14% (rank 12,910) |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not available in the source registry for this evaluation. Based on evidence within the pack (systematic review, PMID 37087864), Selegiline is an irreversible, selective MAO-B inhibitor, approved for Parkinson's disease (oral) and major depressive disorder (transdermal). At low oral doses it remains MAO-B selective, sparing peripheral MAO-A and reducing tyramine-reaction risk relative to non-selective MAOIs; at higher oral doses (≥20 mg/day) selectivity is lost.

Schizophrenia negative symptoms (avolition, blunted affect, anhedonia) are hypothesized to reflect regionally deficient prefrontal cortical dopaminergic activity — a mechanism distinct from the mesolimbic dopamine excess targeted by antipsychotics. Selegiline's MAO-B inhibition increases synaptic dopamine (and to a lesser extent norepinephrine), providing a biologically plausible rationale for its use as an **add-on/augmentation** agent to antipsychotics, rather than monotherapy.

This mechanistic link is directly supported by multiple published trials in the evidence pack testing selegiline augmentation of antipsychotics (haloperidol, risperidone) specifically for negative symptoms — this is not a purely computational prediction but an area with an existing, if inconclusive, clinical research literature spanning 1993–2023.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | RCT of selegiline augmentation of antipsychotics vs. placebo for negative symptoms in chronic inpatient schizophrenia; primary endpoint was reduction in negative symptoms |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT (double-blind, placebo-controlled, multicenter) | Am J Psychiatry | Tested selegiline augmentation of antipsychotics in outpatients with moderate-or-greater negative symptoms |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT (add-on, double-blind, placebo-controlled) | Hum Psychopharmacol | Selegiline add-on to risperidone, 8-week RCT, for negative symptoms |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | RCT/pilot (open-label augmentation) | J Nerv Ment Dis | Low-dose selegiline (5 mg BID) augmentation tested against dopamine-deficiency hypothesis of negative symptoms in 21 patients |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic Review/Meta-analysis | Eur Neuropsychopharmacol | Pooled efficacy/safety of oral and transdermal selegiline across psychiatric disorders, including schizophrenia |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case series | Compr Psychiatry | 3 patients showed improved negative symptoms and functioning after selegiline addition, no adverse effects observed |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Evaluates the evidence base for selegiline in schizophrenia negative symptoms |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT (placebo-controlled) | Biol Psychiatry | Selegiline 10 mg/day vs. placebo for neuroleptic-induced tardive dyskinesia in 33 patients |
| [7901857](https://pubmed.ncbi.nlm.nih.gov/7901857/) | 1993 | Clinical study | Pharmacopsychiatry | Selegiline evaluated for neuroleptic-induced parkinsonism |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic Review | Schizophr Res | Reviews pharmacological treatments (including selegiline) for primary negative symptoms |
| [36561338](https://pubmed.ncbi.nlm.nih.gov/36561338/) | 2022 | Historical Review | Front Pharmacol | Historical role of MAO inhibitors, including selegiline, in psychopharmacology |

---

## India Market Information

Selegiline currently has **no marketing authorization** on record in the India regulatory dataset used for this evaluation (`market_status: Not marketed`, 0 registrations). No product listing table is available.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 123 total interactions on file; representative Major-severity interactions shown):

| Interacting Drug | Severity |
|---|---|
| Isometheptene | Major |
| Bupropion | Major |
| Diethylpropion | Major |
| Phentermine | Major |
| Dexfenfluramine | Major |

These reflect the expected pharmacology of a MAO-B inhibitor: sympathomimetic amines, other MAOIs/antidepressants, and appetite suppressants carry risk of hypertensive crisis or serotonin syndrome and should be reviewed case-by-case. In addition, multiple Moderate-severity interactions exist with sulfonylureas and insulins (e.g., Glimepiride, Repaglinide, Insulin glargine), suggesting glucose-lowering potentiation risk warranting monitoring.

Detailed key warnings and contraindications were not available in this evidence pack; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Existing RCTs of selegiline augmentation for schizophrenia negative symptoms span three decades but are small, methodologically heterogeneous, and yield inconsistent effect sizes; the only registered trial (NCT00456976) was Early Phase 1. Evidence level is L2 (a completed RCT exists) but effect is not robustly established, and this is add-on rather than monotherapy positioning.

**To proceed, the following is needed:**
- Official TFDA/regulatory-sourced package insert (warnings, contraindications) — currently a blocking data gap
- Verified original MOA and indication data from DrugBank/regulatory source (currently unavailable)
- An updated, adequately powered RCT (Phase 2/3) specifically in negative-symptom-predominant schizophrenia
- Formal DDI risk assessment against concomitant antipsychotic and antidepressant regimens typical in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

