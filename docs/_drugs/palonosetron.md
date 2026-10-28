---
layout: default
title: Palonosetron
parent: Moderate Evidence (L3-L4)
nav_order: 639
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
description: "Palonosetron: predicted new indication Migraine disorder (evidence level L4). Approved use: Not recorded in the local data"
---

# Palonosetron
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Palonosetron: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Palonosetron is a second-generation 5-HT3 receptor antagonist, a class of drug used to prevent nausea and vomiting. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and the only directly relevant publication is a **case report describing palonosetron-induced migraine-type headache**, which points in the opposite direction of benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L4 |
| India Market Status | Marketed (valid licences: 12 of 12) |
| Number of Registrations | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, palonosetron is a second-generation 5-HT3 receptor antagonist. These receptors are found on trigeminal afferent nerves and in the brainstem circuits that control vomiting, which gives a theoretical link to migraine pathophysiology and to migraine-associated nausea.

However, this link is weak. The high TxGNN score (0.9974) reflects a network-based prediction, not clinical data. The only retrieved publication (PMID 21132477) reports that palonosetron **induced** migraine-type headache. That is a safety signal opposite to therapeutic benefit.

The other predicted indications are even less supported. Migraine with brainstem aura is a prediction driven only by its similarity to the general migraine node. Atrophoderma vermiculata and ulerythema ophryogenesis are rare skin disorders with no plausible 5-HT3 link and probably reflect TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case report | Can J Anaesth | Palonosetron-induced migraine-type headache; a safety signal, not evidence of efficacy |
| [42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/) | 2026 | Review | Eur Heart J Cardiovasc Pharmacother | Review of antiemetic-associated QT prolongation with a risk-stratified prescribing framework; relevant to cardiac safety, not migraine efficacy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 178921 | Palibout 0.25 Injection | Vial of 5 ml injection | Not specified |
| 8975 | Aloxy Capsule | Strip of 10 capsules | Not specified |
| 178192 | Palostar 0.25mg Injection | Vial of 5 ml injection | Not specified |
| 44732 | Chepatron 0.25mg Injection | Vial of 1 ml injection | Not specified |
| 76668 | Emecad 0.25mg Injection | Vial of 5 ml injection | Not specified |

Twelve valid single-ingredient registrations are listed in total. Both injectable and oral forms are marketed.

## Safety Considerations

- **Drug Interactions**: 398 interactions were recorded. Major-level interactions include:
  - Fentanyl, alfentanil, tramadol and dextromethorphan
  - Almotriptan and sumatriptan
  - Amiodarone, amisulpride, amitriptyline and anagrelide

  Moderate-level interactions include abiraterone, codeine, dihydrocodeine, famotidine, formoterol, adenosine, salbutamol, propofol and loperamide.
- **Cardiac safety**: A 2026 review indicates that antiemetics can prolong the QT interval. This is relevant given the QT-related interactions above (for example amiodarone and amisulpride).
- **Headache signal**: Palonosetron has been reported to induce migraine-type headache (PMID 21132477).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, and the only directly relevant report suggests palonosetron can trigger migraine-type headache rather than treat it. The remaining predicted indications have no supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence that 5-HT3 antagonism by palonosetron benefits migraine, which would need to address the reported headache-induction signal
- A QT-risk assessment if any development is considered, given the interacting QT-prolonging drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

