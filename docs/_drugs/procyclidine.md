---
layout: default
title: Procyclidine
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
---

# Procyclidine
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

Using the txgnn-pipeline skill's context confirmed no additional report-format requirements apply here (it covers training/deployment, not report authoring), so I'm following the v5 report prompt exactly as specified.

A few honesty notes before the report: `original_indications` and `taiwan_regulatory.licenses` are empty in this Evidence Pack, so I've used Procyclidine's well-established public drug classification (antimuscarinic/anticholinergic, historically used for Parkinsonism) only where the template's own fallback rule requires it — flagged explicitly as not sourced from this Evidence Pack. I also did not soften the rank-1 candidate's own rationale text, which states there is no mechanistic basis for it.

---

# Procyclidine: From Parkinsonism to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Procyclidine is an antimuscarinic (anticholinergic) agent historically used to manage Parkinson's disease and drug-induced extrapyramidal symptoms.
> The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**,
> but this direction currently has **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states there is no known biological link between the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinsonism / drug-induced extrapyramidal symptoms (based on known drug classification — not provided in this Evidence Pack; `original_indications` is empty) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Procyclidine in this Evidence Pack (flagged as data gap DG002, High severity). Based on generally known pharmacological classification, Procyclidine is an antimuscarinic anticholinergic that antagonizes central M1 acetylcholine receptors, and has been used clinically to reduce tremor and rigidity in Parkinsonism and drug-induced extrapyramidal symptoms.

Rasmussen subacute encephalitis, the model's top-ranked candidate, is a unilateral autoimmune inflammatory encephalitis in which T-cell–mediated neuronal destruction drives intractable focal epilepsy. This is mechanistically unrelated to antimuscarinic receptor blockade. The Evidence Pack's own repurposing rationale for this candidate is explicit on this point: it states there is "no association with anticholinergic drug mechanism" and "no evidentiary basis" for the link. A prediction score of 99.7% should not be read as clinical confidence here — TxGNN scores are frequently compressed near the top of the range across many drug-disease pairs, and this candidate's ordinal rank (5,111th) and empty evidence base both indicate a low-quality signal despite the high raw score.

It is worth noting that other candidates further down this drug's Top-10 list are mechanistically more coherent with Procyclidine's known pharmacology — for example, rank 7 (progressive supranuclear palsy–corticobasal syndrome) and rank 8 (juvenile parkinsonism, "Hunt's paralysis agitans") both involve parkinsonian rigidity/dystonia where anticholinergics are occasionally used symptomatically. However, these too returned zero clinical trials, zero ICTRP registrations, and zero PubMed literature in the queries performed, so none of the ten candidates currently rise above a model-only (L5) evidence level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Procyclidine is not currently marketed in India — `taiwan_regulatory.total_licenses` = 0 and no license records are present in this Evidence Pack.

---

## Safety Considerations

- **Drug Interactions**: 70 interactions on file. Two are classified **Major**: co-administration with **Potassium citrate** and **Potassium chloride** (risk relates to anticholinergic-mediated slowing of GI transit, which can increase mucosal contact time/ulcerogenic potential of oral potassium salts). The remainder are classified **Moderate**, predominantly other antimuscarinic/anticholinergic agents (e.g., Atropine, Glycopyrronium, Dicyclomine, Trospium, Mepenzolate, Methscopolamine, Clidinium — additive anticholinergic burden), opioids (Morphine, Opium, Loperamide — additive constipation/CNS effects), and agents sensitive to altered GI motility (Metoclopramide, Pramlintide, Eluxadoline, Dronabinol, Nabilone).

Key warnings and contraindications could not be assessed — this Evidence Pack reports a **Blocking**-severity data gap (DG001: TFDA/label warnings and contraindications not yet retrieved), which by definition prevents this candidate from entering the S1 safety initial-screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Rasmussen subacute encephalitis) has no supporting clinical trials or literature and, per the model's own rationale, no plausible mechanistic link to Procyclidine's anticholinergic action — this is an L5, model-only signal. Independently, a **Blocking**-severity data gap (missing label warnings/contraindications, DG001) means the candidate cannot yet pass the S1 safety initial evaluation regardless of indication evidence, and the drug has no existing India market presence to leverage.

**To proceed, the following is needed:**
- Retrieve TFDA/official product label warnings and contraindications (resolves DG001, currently Blocking)
- Retrieve confirmed mechanism-of-action documentation from DrugBank (resolves DG002)
- If pursuing repurposing further, prioritize mechanistically coherent candidates from this drug's list (e.g., PSP-CBS, juvenile parkinsonism) over the current top-ranked candidate, and commission targeted literature/preclinical searches, since all 10 predicted indications currently return zero hits across ClinicalTrials.gov, ICTRP, and PubMed
- Pharmacology/clinical expert review of the Rasmussen-encephalitis prediction specifically, given the model rationale itself disputes the mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

