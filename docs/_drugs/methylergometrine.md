---
layout: default
title: Methylergometrine
parent: Model Prediction Only (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methylergometrine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the licence data compiled for this report"
---

# Methylergometrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Methylergometrine: From Uterotonic Use to Hypertrichosis (Top Prediction), with Migraine as the Most Plausible Candidate

## One-Sentence Summary

Methylergometrine is an ergot-derived drug marketed in India as tablets and injections, with no approved-indication text recorded in the licence data compiled for this report. The TxGNN model's top prediction is **hypertrichosis**, but there are **0 clinical trials** and **0 publications** behind it. Of the ten predictions, only **migraine disorder** has any related literature (2 reviews), and these offer indirect and safety-oriented context rather than efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

The ten predictions all score between 99.57% and 99.87%. The table below shows how the evidence differs between them.

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Hypertrichosis | 99.87% | L5 | Hold |
| 2 | Pulmonary hypertension | 99.86% | L5 | Hold |
| 3 | Migraine disorder | 99.84% | L4 | Research Question |
| 4 | Ambras type hypertrichosis universalis congenita | 99.82% | L5 | Hold |
| 5 | Malformation syndrome with odontal/periodontal component | 99.81% | L5 | Hold |
| 6 | Syndrome with Dandy-Walker malformation as major feature | 99.81% | L5 | Hold |
| 7 | Isolated genetic hair shaft abnormality | 99.79% | L5 | Hold |
| 8 | Kyphoscoliotic heart disease | 99.77% | L5 | Hold |
| 9 | Migraine with brainstem aura | 99.77% | L5 | Hold |
| 10 | Nephrogenic syndrome of inappropriate antidiuresis | 99.57% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, methylergometrine is an ergot-derived uterotonic acting on serotonin, dopamine and alpha-adrenergic receptors.

**Hypertrichosis (rank 1):** No plausible mechanistic link was identified. Hypertrichosis is a hair growth disorder, and it is a known adverse effect of some other drugs (for example minoxidil). The high score may therefore reflect artifacts of the knowledge network rather than therapeutic potential.

**Pulmonary hypertension (rank 2):** The mechanistic direction argues against benefit. Ergot derivatives acting on 5-HT2B receptors are associated with pulmonary hypertension and valvulopathy, and methylergometrine has vasoconstrictive activity. This is a potential harm signal.

**Migraine disorder (rank 3):** This is the only prediction with a plausible, though indirect, link. Methylergometrine is the active metabolite of methysergide, a historical migraine preventive acting on 5-HT receptors. Ergot alkaloids such as ergotamine and dihydroergotamine are established migraine therapies. However, vasoconstriction and coronary risk, along with the fibrotic complications that led to methysergide's restriction, are major concerns.

**Other predictions (ranks 4–8, 10):** These are rare congenital or genetic conditions, structural malformations, or disorders with unrelated pathways (for example, a vasopressin V2 receptor gain-of-function disorder). None has a known mechanistic link, and the scores appear to reflect knowledge-graph proximity rather than pharmacology.

**Migraine with brainstem aura (rank 9):** A serotonergic rationale exists by extension from migraine, but vasoconstrictive agents such as ergots and triptans are generally cautioned or contraindicated in this subtype because of ischemic concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the ten predicted indications.

---

## Literature Evidence

Only the migraine disorder prediction has related literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Review | Cephalalgia | History of methysergide in migraine, from Wolff's vasodilation theory and the discovery of serotonin to the synthesis of methysergide from lysergic acid |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Review | Circulation | Compared the coronary vasoconstrictor potential of antimigraine drugs, including methylergometrine (the metabolite of methysergide); a safety-oriented study |

Neither paper provides direct efficacy evidence for methylergometrine in migraine. No literature is available for the other nine predictions.

---

## India Market Information

There are 20 valid single-ingredient registrations and no cancelled ones. The licence data contain no approved-indication text. Main authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 133630 | Methergin Injection (Novartis India Ltd) | Vial of 1 ml injection | Not recorded |
| 135150 | Methargo Tablet (Mankind Pharma Ltd) | Strip of 10 tablets | Not recorded |
| 129554 | Limitex 0.2mg Injection (Sun Pharmaceutical Industries Ltd) | Vial of 1 ml injection | Not recorded |
| 134492 | Methygene 0.125mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not recorded |
| 145497 | Metermin 0.2mg Injection (Cadila Pharmaceuticals Ltd) | Vial of 1 ml injection | Not recorded |

Products are available as oral tablets (0.125 mg) and injections (0.125 mg and 0.2 mg per ml).

---

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (not taken from label text): hypertensive disorder, hypertension, epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, arteriosclerosis obliterans, HELLP syndrome.
- **Drug interactions:** 92 known interactions were identified. Examples rated **Major**: isometheptene, epinephrine (including ophthalmic and topical forms), ephedrine (including nasal), lorcaserin, and clarithromycin. Examples rated **Moderate**: doxycycline, tetracycline, minocycline, aprepitant, dexamethasone, cimetidine, and the azoles clotrimazole and miconazole. CYP3A4 inhibitors raise the risk of ergotism.
- **Class concerns:** vasoconstriction, coronary risk, and pulmonary hypertension or valvulopathy (5-HT2B) are particular concerns for the predicted indications.

Package insert warnings and contraindications were not available for this report; please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Nine of the ten predictions rest on model scores alone, with no trials or literature, and several have a mechanistic direction that suggests harm (pulmonary hypertension, kidney disease, stroke risk). Migraine is the only candidate worth further study, and only as a research question, since its literature is indirect and focuses on safety.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory sources (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- For migraine: a focused literature review of direct efficacy data, and a cardiovascular and fibrosis risk assessment given the vasoconstrictive profile and the 92 interactions
- Approved indication text for the Indian licences, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

