---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

Using the **drug repurposing evaluation report** template supplied in the system instructions to generate this report from the given Evidence Pack.

A note before the report: the Evidence Pack's own annotations flag `predicted_indications[0]`–`[8]` (the 9 highest-scoring TxGNN predictions, all ≥99.99%) as `Hold`/`L5` **model-artifact false positives** — rare congenital/genetic disorders that co-occur with the drug in the knowledge graph but have zero mechanistic or literature support (the pack's own text calls this "偽陽性配對，而非真實藥理證據"). The only candidate with an actual mechanistic story, historical precedent, and real (if weak) literature is rank 10, "manic bipolar affective disorder" (L4, decision_stage S1, "Research Question"). Reporting on rank 1 (retinal dystrophy) as if it were a viable candidate would be actively misleading, so this report is built around rank 10, the only defensible signal in the pack. This deviation is documented below rather than silently made.

---

# Prochlorperazine: From Antiemetic/Antipsychotic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Prochlorperazine is a phenothiazine-class dopamine D2 receptor antagonist, classically used as an antiemetic and for psychotic symptoms.
> Of 10 indications TxGNN predicted for this drug, the model's top 9 (all ≥99.99% score) were internally flagged as knowledge-graph false positives with no mechanistic or literature support.
> The one candidate with a genuine (if limited) evidence trail is **Manic Bipolar Affective Disorder**, supported by **0 clinical trials** and **12 publications** — including one 1959 case report that directly documents prochlorperazine use in a manic-depressive patient — but no controlled efficacy studies exist.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local registry (drug is unmarketed here); internationally used as an antiemetic and for psychotic symptoms (phenothiazine class) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% (score 0.99979, rank 798 by TxGNN internal ranking) |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not supplied in this Evidence Pack (flagged as a data gap, DG002). However, the pack's own repurposing-rationale text establishes that prochlorperazine is a **phenothiazine-class dopamine D2 receptor antagonist**, acting centrally and at the chemoreceptor trigger zone (CTZ) — the pharmacological basis for its use as an antiemetic and antipsychotic.

Dopamine D2 antagonism is also the mechanistic backbone of conventional antipsychotics (e.g., chlorpromazine, haloperidol) used to control acute mania in bipolar affective disorder. Because prochlorperazine shares this class-level mechanism, a "class effect" rationale for antimanic activity is pharmacologically plausible, even though prochlorperazine itself was never developed or systematically studied for this purpose.

The literature evidence supports that this is more than a theoretical link: one case report (PMID 13617778, 1959) directly documents prochlorperazine being administered to a patient with mild manic-depressive illness. Critically, though, that report describes an **adverse reaction** (a confusional, dream-like episode), not a therapeutic response — so the existing direct evidence points to a real historical-use pattern, not to demonstrated efficacy. The remaining literature is dominated by general antipsychotic safety topics (seizures, hyperglycemia, tardive dyskinesia, use in pregnancy), reinforcing that the evidence base here is a risk profile inherited from the phenothiazine class, not an efficacy signal specific to bipolar mania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13617778](https://pubmed.ncbi.nlm.nih.gov/13617778/) | 1959 | Case Report (direct mention) | Annales medico-psychologiques | Confusional dream-like episode caused by prochlorperazine in a patient with mild manic-depressive illness — direct drug use in this population, but reported as an adverse event, not efficacy |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | Journal of Psychiatric Practice | Review of antipsychotic drug use and safety during pregnancy, including in mood/psychotic disorders |
| [26819726](https://pubmed.ncbi.nlm.nih.gov/26819726/) | 2015 | Pharmacovigilance/Cohort | Journal of Pharmaceutical Health Care and Sciences | FAERS analysis linking antipsychotics (dopamine antagonists) to hyperglycemic adverse events in schizophrenia/bipolar disorder patients |
| [4238455](https://pubmed.ncbi.nlm.nih.gov/4238455/) | 1969 | Review | Clinical Pharmacology and Therapeutics | General review of clinical use status of psychotherapeutic drugs |
| [14242542](https://pubmed.ncbi.nlm.nih.gov/14242542/) | 1965 | Review | Obstetrics and Gynecology | Recommended obstetric approach to severe puerperal psychological disorders |
| [14233737](https://pubmed.ncbi.nlm.nih.gov/14233737/) | 1964 | Review | The American Journal of Psychiatry | Survey of electroshock therapy combined with phenothiazines and reserpine |
| [14062306](https://pubmed.ncbi.nlm.nih.gov/14062306/) | 1963 | Review | La Tunisie Medicale | Emergency treatment approach to psychomotor agitation in general practice |
| [235013](https://pubmed.ncbi.nlm.nih.gov/235013/) | 1975 | Case Report | Journal of the Neurological Sciences | Tardive dyskinesia (induced by prolonged phenothiazine use) treated with pimozide |
| [6069087](https://pubmed.ncbi.nlm.nih.gov/6069087/) | 1967 | Case Series | Neurology | Spontaneous epileptic seizures and EEG changes during phenothiazine therapy |
| [15863814](https://pubmed.ncbi.nlm.nih.gov/15863814/) | 2005 | Case Report | The American Journal of Psychiatry | Discontinuation syndrome reported with an antipsychotic (quetiapine) |

---

## India Market Information

Prochlorperazine currently has **no registered marketing authorization** in this jurisdiction (0 licenses on file; market status recorded as "Not Marketed"). No product name, dosage form, or approved indication text is available to report.

---

## Safety Considerations

- **Drug Interactions**: 368 total interactions on file (source: DDInter). Two are flagged as **Major**:
  - Bupropion (Major)
  - Potassium citrate (Major)

  The remainder of the sampled interactions are Moderate, including with Acarbose, Famotidine, Epinephrine, Albiglutide, Alogliptin, Metformin, Pioglitazone, Hyoscyamine, Loperamide, Morphine, Atropine, Lorcaserin, Bisacodyl, Glycopyrronium, Canagliflozin, Chlorpropamide, Clarithromycin, and Picosulfuric acid.

No structured key-warning or contraindication text was available beyond this DDI data; please refer to the package insert for warnings and contraindications not captured here.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Among the 10 TxGNN-predicted indications for prochlorperazine, only "manic bipolar affective disorder" has any real mechanistic or historical grounding (dopamine D2 antagonism, a documented — if adverse — historical use case), yet there are zero clinical trials and no efficacy-oriented studies, only safety/adverse-event literature. The drug is also currently unmarketed in this jurisdiction, so there is no local product or label to anchor a repurposing pathway on. The other 9 higher-scoring predictions are model artifacts with no mechanistic plausibility and should not be pursued.

**To proceed, the following is needed:**
- TFDA/local regulatory label data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record — currently a high-severity data gap (DG002)
- Prospective or at minimum retrospective controlled efficacy data for prochlorperazine (or class-representative phenothiazines) in acute mania
- A formal safety review addressing the two Major DDIs (bupropion, potassium citrate) before any clinical use in a bipolar population, which often carries polypharmacy risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

