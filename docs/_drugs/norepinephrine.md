---
layout: default
title: Norepinephrine
parent: Moderate Evidence (L3-L4)
nav_order: 606
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Norepinephrine: predicted new indication Obstructive lung disease (evidence level L4). Approved use: Asthma, intrinsic asthma, allergic asthma, bronchitis…"
---

# Norepinephrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Norepinephrine: From Asthma and Hypotensive Disorders to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine is an adrenergic vasopressor, originally listed for conditions such as asthma, bronchitis, emphysema, bronchiectasis and hypotensive disorders.
The TxGNN model predicts it may be effective for **obstructive lung disease**, but the supporting evidence is thin: **1 clinical trial** (indirectly related) and **19 publications**, mostly mechanistic reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, intrinsic asthma, allergic asthma, bronchitis, hypotensive disorder, pulmonary emphysema, bronchiectasis (the indication text in the local licences is blank; these come from the knowledge graph) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Norepinephrine is an adrenergic agonist with alpha-1, alpha-2 and beta-1 activity, and weak beta-2 activity. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on general pharmacological knowledge.

Asthma, bronchitis, emphysema and bronchiectasis already appear among its original indications. Obstructive lung disease (such as COPD and asthma) overlaps heavily with these conditions, which is why the model links them. The literature supports a role for adrenergic and neuroimmune signalling in airway disease, but this is mechanistic and review-level evidence.

There are important limits. Norepinephrine's beta-2 bronchodilator activity is weak, and no modern evidence shows it improves outcomes in obstructive lung disease. Its vasoconstrictor, tachycardic and arrhythmic effects are a concern in COPD patients who also have heart disease or hypoxaemia.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function, exercise and skeletal muscle feedback in hypertension. Not designed to test norepinephrine in obstructive lung disease; the link is indirect (relevance grade C). |

## Literature Evidence

No randomised trials were found. The most relevant items are reviews and physiology studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Review | Front Immunol | Adrenergic signalling at the interface of allergic asthma and viral infections |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Review | Ann Med | Neuroimmune circuits in respiratory disease and potential therapeutic targets |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Airway innervation in asthma and COPD, including the role of norepinephrine in sympathetic nerves |
| [2003685](https://pubmed.ncbi.nlm.nih.gov/2003685/) | 1991 | Review | Am Rev Respir Dis | Neural control of airway blood vessels and oedema; sympathetic norepinephrine acts as a constrictor |
| [10951892](https://pubmed.ncbi.nlm.nih.gov/10951892/) | 2000 | Review | Allergy Asthma Proc | Stress, immune regulation and asthma; lymphocytes carry norepinephrine receptors |
| [28539203](https://pubmed.ncbi.nlm.nih.gov/28539203/) | 2018 | Review | Allergol Int | Neuroendocrine activity and stress-induced worsening of allergic asthma |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Physiology study | Am J Physiol Heart Circ Physiol | Muscle alpha-adrenergic responsiveness during exercise in COPD patients |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Panel study | Environ Pollut | Stress hormones and air pollution exposure in people with and without COPD |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Clinical study | Am J Med | Mechanisms of hypertension in COPD with acute respiratory failure, including norepinephrine levels |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | Catecholamines in critical care |

## India Market Information

Twenty single-ingredient injectable licences are valid in India, with none cancelled. The approved indication text is blank for all of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152051 | Norbit Injection | Vial of 2 ml injection | Not stated |
| 153832 | N-Adrin 4mg Injection | Vial of 2 ml injection | Not stated |
| 157407 | Nordyx Injection | Ampoule of 2 ml injection | Not stated |
| 1359 | Adrenor 4mg Injection | Vial of 2 ml injection | Not stated |
| 150671 | Norad 4mg Injection | Vial of 4 ml injection | Not stated |

All products are injections; no inhaled or oral forms are registered, which matters for a respiratory indication.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: hypertensive disorder, hypertension, thrombotic disease.
- **Drug Interactions**: 70 interactions were identified, all of those listed rated Moderate. They are mainly with antidiabetic drugs (e.g., metformin, pioglitazone, sitagliptin, semaglutide, insulins, SGLT2 inhibitors) and with the anorectics phentermine and diethylpropion.

Package-insert warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.84%) is not backed by direct clinical evidence: the only trial is an indirect Phase 1 hypertension study, and the literature is mechanistic. Norepinephrine's cardiovascular effects add risk in COPD patients, and the registered products are injections only.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data
- Controlled clinical data in obstructive lung disease, or a clear rationale for an appropriate route and setting
- A cardiovascular risk assessment for patients with COPD and comorbid heart disease or hypoxaemia

*Other predictions, not recommended for further work at this stage:*
- **Respiratory malformation** (score 99.84%, L5): no clinical trials, and the literature is physiological or safety-related. A vasopressor has no clear therapeutic role.
- **Rienhoff syndrome** (score 99.83%, L5): no trials or literature; this is a computational hypothesis only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

