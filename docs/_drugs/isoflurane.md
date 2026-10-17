---
layout: default
title: Isoflurane
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Isoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the available licence data (isoflurane is an inhaled ge…"
monitor_inn: "Isoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
---

# Isoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Isoflurane: From General Anaesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is a volatile inhaled general anaesthetic that is widely marketed in India.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.
Evidence is stronger for other predicted indications (for example, migraine disorder with 12 publications, mostly preclinical or case reports), but none is supported by clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data (isoflurane is an inhaled general anaesthetic) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isoflurane is a volatile halogenated ether anaesthetic, and its efficacy in producing general anaesthesia is established. Mechanistically, it may be applicable to **Prinzmetal angina** only through an indirect link.

Volatile anaesthetics have vasodilatory effects and modulate vascular smooth muscle calcium handling, which could theoretically relate to coronary vasospasm. However, isoflurane can also cause coronary vasodilation and, in some settings, coronary steal, so this link is speculative and may carry safety concerns rather than benefit. No clinical evidence supports this use.

The prediction score is very high (99.67%), but the score reflects knowledge-graph patterns and not clinical proof.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For context, the other predicted indications with literature were:

- **Migraine disorder (rank 7, score 99.06%, Evidence Level L4):** 12 publications, with no clinical trials.
- **Manic bipolar affective disorder (rank 3, score 99.57%, Evidence Level L4):** 3 publications, with no clinical trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Preclinical | Cephalalgia | Inhalational anaesthetics inhibit cortical spreading depression, the experimental correlate of migraine aura (migraine) |
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case report | Braz J Anesthesiol | Status migrainosus treated with general anaesthesia (propofol and isoflurane act on GABA-A receptors); the same case is also published in Portuguese as [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) (migraine) |
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | Open-label study | Eur J Anaesthesiol | Burst-suppression isoflurane anaesthesia compared with ECT in 12 patients with severe depression; marked improvement was seen after both (bipolar/mood disorders, indirect) |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | Case report | AANA J | Malignant hyperthermia differential diagnosis in a patient with manic-depressive psychosis; not efficacy evidence (bipolar) |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | Animal study | Psychiatry Res | FDG-PET in a rat model of mania; isoflurane used as the anaesthetic, not as the tested therapy (bipolar) |

The remaining migraine records are preclinical studies of CGRP, NMDA and spreading-depolarization models, where isoflurane is probably used only as the anaesthetic.

---

## India Market Information

Isoflurane has 13 valid single-ingredient registrations, with no cancelled licences. The approved indication text is not recorded in the licence data. Main authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 87759 | Forane Solution (Abbott) | Bottle of 250 ml solution for inhalation | Not recorded |
| 88227 | Forane Solution (Abbott) | Bottle of 100 ml solution for inhalation | Not recorded |
| 109317 | Isotroy Solution for inhalation (Troikaa) | Packet of 100 ml solution for inhalation | Not recorded |
| 202634 | Sosrane Liquid For Inhalation (Neon Laboratories) | Bottle of 30 ml solution for inhalation | Not recorded |
| 108228 | Isoflurane USP Liquid For Inhalation (Baxter India) | Bottle of 100 ml solution for inhalation | Not recorded |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver disease, gallbladder disease, hypotensive disorder, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, Duchenne muscular dystrophy, Becker muscular dystrophy and muscular dystrophy. These come from TxGNN knowledge-graph edges and must be confirmed against the package insert.
- **Drug Interactions:** 38 interactions were identified. The main ones are:
  - **Major:** Epinephrine
  - **Moderate:** Morphine, Opium
  - Many others (for example atropine, hydrocortisone, omeprazole, ondansetron, dexamethasone) have an unclassified severity level.
- **Indication-specific concern:** Isoflurane can cause coronary vasodilation and coronary steal, which is a potential risk rather than a benefit in coronary vasospastic disease.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on a model score alone, with no clinical trials or literature, and the proposed mechanism may even imply harm (coronary steal). A chronic, inhaled general anaesthetic is also impractical for a chronic cardiac condition.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the India-registered products
- Mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies of isoflurane in coronary vasospasm, including a coronary steal safety assessment
- Route and setting feasibility assessment, since the available forms are inhaled anaesthetics for hospital use
- Consideration of **migraine disorder** as a research question instead. It has the most supporting material (anaesthetic inhibition of spreading depression, plus anecdotal status migrainosus case reports), but it still lacks clinical trials, and use would be limited to refractory, hospitalised settings.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

