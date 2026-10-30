---
layout: default
title: Nicergoline
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Nicergoline"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "benign prostatic hyperplasia (disease)", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
description: "Nicergoline: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Nicergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Nicergoline: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Nicergoline is an ergot-derived vasodilator and alpha-1 adrenergic antagonist marketed in India as single-ingredient tablets. The India license records compiled for this report do not list an approved indication.
Among the eight predicted indications, only **migraine disorder** has supporting literature (**6 publications, 0 registered trials**, mostly preclinical).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 (hypertrichosis); L4 (migraine disorder) |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold (hypertrichosis); migraine flagged as a research question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, nicergoline is an ergot derivative with vasodilating, alpha-1 adrenergic blocking and serotonin-modulating properties.

**Hypertrichosis (rank 1):** No plausible mechanistic path from nicergoline to hair growth regulation is evident. The same applies to the related predictions (Ambras-type congenital hypertrichosis, isolated genetic hair shaft abnormality), which are genetic conditions that a vasoactive drug is unlikely to correct.

**Other low-plausibility predictions:** Malformation syndromes (odontal/periodontal, Dandy-Walker) are structural developmental conditions, and nephrogenic syndrome of inappropriate antidiuresis arises from vasopressin V2 receptor signalling. None has a link to nicergoline's pharmacology in the data supplied.

**Benign prostatic hyperplasia (rank 5):** Alpha-1 blockade is the mechanism of established BPH drugs such as tamsulosin, so the rationale is plausible. However, no evidence was supplied, and uroselectivity and blood-pressure effects would need to be compared with existing alternatives.

**Migraine (rank 8):** This is the most coherent candidate. Nicergoline's vasoactive, alpha-blocking and serotonergic properties fit migraine pathophysiology. Preclinical work shows effects on cerebrovascular resistance, 5-HT-induced vasoconstriction and serotonin transport in rat brain synaptosomes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

The literature below relates to migraine disorder, the only predicted indication with publications. No literature was available for the other seven predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6385484](https://pubmed.ncbi.nlm.nih.gov/6385484/) | 1984 | Clinical report (design unclear) | Wiadomosci Lekarskie | Describes use of nicergoline (Sermion) in migraine treatment; no abstract available, apparently uncontrolled |
| [2622296](https://pubmed.ncbi.nlm.nih.gov/2622296/) | 1989 | Preclinical | Methods Find Exp Clin Pharmacol | Nicergoline reduced cerebrovascular resistance and affected 5-HT-induced vessel constriction and 5-HT transport in rat brain synaptosomes in migraine-related models |
| [2625145](https://pubmed.ncbi.nlm.nih.gov/2625145/) | 1989 | Preclinical (animal) | Farmakol Toksikol | Nicergoline and methysergide competitively inhibited serotonin uptake in rat brain synaptosomes |
| [8374139](https://pubmed.ncbi.nlm.nih.gov/8374139/) | 1993 | Preclinical/mechanistic | Biull Eksp Biol Med | Compared the effect of antimigraine drugs, including nicergoline, on serotonin transport in platelets |
| [12924226](https://pubmed.ncbi.nlm.nih.gov/12924226/) | 2003 | Preclinical/mechanistic | Eksp Klin Farmakol | Compared the antiserotonin cerebrovascular effects of tropoxin with other antimigraine drugs |
| [2684591](https://pubmed.ncbi.nlm.nih.gov/2684591/) | 1989 | Review (flunarizine, not nicergoline-specific) | Drugs | Review of flunarizine as migraine prophylaxis; indirect context only |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 35705 | Cholergol Tablet | Strip of 10 tablets | Not stated |
| 151877 | Nicer 30mg Tablet | Strip of 10 tablets | Not stated |
| 200864 | Sermion 30mg Tablet | Strip of 10 tablets | Not stated |
| 150520 | Nicerbium Tablet | Strip of 10 tablets | Not stated |
| 154136 | Nicerwin V Tablet | Strip of 10 tablets | Not stated |

All five licences are valid single-ingredient oral products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (for hypertrichosis and the other six non-migraine predictions). Migraine disorder is flagged as a research question rather than a Go.

**Rationale:**
- The top-ranked prediction has no clinical or literature support and no plausible mechanism, so the score is likely a TxGNN model (deep learning) artefact.
- Migraine has a coherent mechanism, but its evidence is mostly preclinical, with one old, low-grade clinical report. BPH is mechanistically plausible but entirely unsupported by evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which are required before any safety screening
- Approved indication text for the India licences, to establish the original indication
- Mechanism of action data for nicergoline (for example, from DrugBank)
- For migraine: a systematic search for controlled clinical trials of nicergoline, and comparison with established prophylaxis options
- For BPH: a literature search and a comparison of alpha-1 selectivity and blood-pressure effects against existing alpha-blockers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

