---
layout: default
title: Fluphenazine
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Fluphenazine
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

# Fluphenazine: From Psychotic Disorders to Manic Bipolar Affective Disorder

## One-Sentence Summary

Fluphenazine is a first-generation (typical) phenothiazine antipsychotic, primarily acting through D2 dopamine receptor antagonism to treat psychotic disorders such as schizophrenia. Among the 10 new indications predicted by the TxGNN model for this drug, only **manic bipolar affective disorder** is backed by actual clinical literature (20 publications, no dedicated RCTs), reaching evaluation stage S2 with a **Proceed with Guardrails** recommendation — the other 9 candidates (e.g., retinal dystrophy, syndromic myopia, various rare genetic disorders) have very high raw TxGNN embedding scores but no supporting mechanism or literature, and remain at Hold (S0).

> **Note on candidate selection**: This evidence pack ranks 10 predicted indications by TxGNN score. The top-ranked candidate ("retinal dystrophy with or without extraocular anomalies," score 99.99%) has no plausible mechanistic link to fluphenazine's pharmacology and no supporting evidence — the model itself flags this as likely embedding noise. This report focuses on **manic bipolar affective disorder** (rank 10, score 99.98%), the only candidate with real supporting evidence and an actionable decision stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorders (schizophrenia) — typical antipsychotic, phenothiazine class |
| Predicted New Indication | Manic bipolar affective disorder (bipolar mania) |
| TxGNN Prediction Score | 99.98% (rank 852 among all candidates) |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Fluphenazine is a first-generation phenothiazine antipsychotic whose primary mechanism is D2 dopamine receptor antagonism, with secondary activity at D1, α1-adrenergic, H1-histamine, and muscarinic acetylcholine receptors. D2 antagonism is the core pharmacological mechanism underlying acute treatment of manic episodes, and this mechanism is shared with other typical and atypical antipsychotics (e.g., haloperidol, risperidone) that are already approved for bipolar mania.

This prediction therefore represents a **class-effect extrapolation** rather than a novel mechanism specific to fluphenazine: because other D2-antagonist antipsychotics are established treatments for bipolar mania, and fluphenazine shares the same receptor pharmacology, its potential efficacy in this indication is biologically plausible. This is further supported by real-world literature showing off-label and long-acting injectable (LAI) fluphenazine use in bipolar disorder management, particularly for adherence-challenged or substance-use-comorbid patients.

By contrast, the other 9 TxGNN-predicted indications for fluphenazine (retinal dystrophies, syndromic/X-linked myopia, hydranencephaly, congenital glycosylation disorders, Charcot-Marie-Tooth disease, etc.) are structural, developmental, or metabolic genetic diseases with no known relationship to dopaminergic/adrenergic/cholinergic receptor pharmacology. The evidence pack's own rationale text for these explicitly notes "no known mechanistic link" — these should be treated as low-confidence knowledge-graph artifacts, not credible repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26243837](https://pubmed.ncbi.nlm.nih.gov/26243837/) | 2015 | Review | Clin Psychopharmacol Neurosci | Systematic review and expert consensus on long-acting injectable (LAI) antipsychotics, including fluphenazine decanoate, in bipolar disorder |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Cohort | J Affect Disord | Retrospective analysis: adding LAI antipsychotics during manic episodes reduces rehospitalization in bipolar disorder |
| [36779113](https://pubmed.ncbi.nlm.nih.gov/36779113/) | 2023 | Case Report | Cureus | Off-label use of fluphenazine in bipolar disorder with comorbid substance abuse history, two cases |
| [37345508](https://pubmed.ncbi.nlm.nih.gov/37345508/) | 2023 | Review | Expert Opin Pharmacother | Pharmacological considerations for switching to LAI antipsychotics, including fluphenazine, in severe mental illness |
| [22494448](https://pubmed.ncbi.nlm.nih.gov/22494448/) | 2012 | Review | CNS Drugs | Review of first- and second-generation depot antipsychotics for maintenance treatment of bipolar disorder |
| [30129771](https://pubmed.ncbi.nlm.nih.gov/30129771/) | 2018 | Observational | J Comp Eff Res | Initiating LAI antipsychotics associated with reduced hospitalization risk in bipolar I disorder |
| [34353834](https://pubmed.ncbi.nlm.nih.gov/34353834/) | 2021 | Case Report | BMJ Case Rep | Case of neuroleptic malignant syndrome in a bipolar patient maintained on fluphenazine decanoate — safety signal |
| [27028966](https://pubmed.ncbi.nlm.nih.gov/27028966/) | 2016 | Case Series | J Child Adolesc Psychopharmacol | Efficacy of LAI antipsychotics in adolescents, limited pediatric safety/efficacy data |

---

## Taiwan Market Information

Fluphenazine currently holds no TFDA license and is not marketed in Taiwan (未上市, 0 registrations). No local product, dosage form, or approved indication data is available.

---

## Safety Considerations

**Drug Interactions**: A total of 313 documented drug-drug interactions were identified. Notable interactions include:
- **Major**: Bupropion, Morphine
- **Moderate**: Acarbose, Famotidine, Epinephrine, Hydrocortisone, several antidiabetic agents (Albiglutide, Alogliptin, Metformin, Pioglitazone), Amphotericin B (conventional and lipid complex), Atropine/Hyoscyamine (anticholinergic burden), corticosteroids (Dexamethasone, Triamcinolone, Betamethasone), Lorcaserin, Loperamide
- **Minor**: Ascorbic acid

Detailed TFDA-specific warnings and contraindications are not currently available (this is a blocking data gap — see below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Manic bipolar affective disorder is supported by a class-effect mechanistic rationale (shared D2 antagonism with already-approved antipsychotics for bipolar mania) and multiple real-world/cohort/case-level publications, including fluphenazine-specific use cases — reaching evaluation stage S2. However, no fluphenazine-specific RCT exists for this indication, and the drug is not currently marketed in Taiwan, so guardrails (specialist oversight, off-label use documentation, safety monitoring) are warranted rather than unconditional advancement.

**To proceed, the following is needed:**
- TFDA product labeling (warnings/contraindications) — currently a **blocking** data gap (DG001); required before formal S1 safety assessment can begin
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source (DG002)
- A formal Taiwan market-entry or import pathway assessment, given current "未上市" status
- Consideration of a fluphenazine- or class-specific prospective study in bipolar mania, since existing evidence is largely LAI-formulation and class-level rather than drug-specific RCT data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

