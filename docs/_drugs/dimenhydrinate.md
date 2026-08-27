---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is a first-generation antihistamine/antiemetic classically used for the prevention and treatment of motion sickness, nausea, and vomiting. The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 clinical trials** and **1 publication** currently supporting this direction. The mechanistic basis is plausible given that dimenhydrinate metabolises to diphenhydramine — a well-established H1 receptor antagonist — yet direct clinical evidence for this repurposing remains absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Motion sickness; nausea and vomiting |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dimenhydrinate is a salt composed of diphenhydramine and 8-chlorotheophylline. Upon oral or parenteral administration, it is rapidly metabolised to diphenhydramine — a classic first-generation H1 receptor antagonist. Diphenhydramine competitively blocks histamine H1 receptors, thereby suppressing the downstream cascade triggered by mast cell degranulation: vasodilation, increased vascular permeability, and pruritus. These are precisely the hallmark features of allergic urticaria, making the mechanistic link between dimenhydrinate (via its active metabolite) and this indication scientifically coherent.

Diphenhydramine itself carries Level 1 RCT evidence for allergic urticaria and is listed as a first-line agent in multiple international guidelines. The TxGNN model's high-confidence prediction therefore aligns with established pharmacology. However, dimenhydrinate as an independent drug entity has never been directly evaluated in allergic urticaria clinical trials — a critical evidence gap. The 8-chlorotheophylline moiety provides mild anticholinergic and bronchodilatory effects that are unlikely to enhance antihistaminic efficacy in urticaria but may contribute to additional adverse effects (e.g., CNS stimulation, tachycardia).

The distinction between diphenhydramine (well-evidenced for urticaria) and dimenhydrinate (zero direct clinical trial data) is the central challenge for this repurposing candidate. Regulatory and clinical acceptance would require bridging studies specifically using dimenhydrinate as the test agent, rather than extrapolating entirely from diphenhydramine data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dimenhydrinate in allergic urticaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic Study | Veterinary Dermatology | Compared oral dimenhydrinate vs. oral/IV diphenhydramine in healthy dogs; dimenhydrinate showed superior oral absorption of diphenhydramine and was evaluated for suppression of histamine-induced wheal formation, suggesting a pharmacodynamic basis for antiallergic activity |

---

## India Market Information

Dimenhydrinate currently has no registered products in India (0 authorisations on record).

---

## Safety Considerations

**Drug Interactions (67 interactions identified; selected key interactions listed below):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Potassium chloride | **Major** | Anticholinergic effects of dimenhydrinate may slow GI motility, increasing risk of potassium chloride-induced GI lesions |
| Potassium citrate | **Major** | Same mechanism as above; delayed gastric emptying increases mucosal exposure time |
| Scopolamine | Moderate | Additive anticholinergic effects; risk of urinary retention, dry mouth, confusion |
| Atropine | Moderate | Additive anticholinergic effects |
| Morphine | Moderate | Additive CNS and respiratory depression |
| Metoclopramide | Moderate | Dimenhydrinate's anticholinergic action may antagonise the prokinetic effect of metoclopramide |
| Hyoscyamine | Moderate | Additive anticholinergic toxicity |
| Glycopyrronium | Moderate | Additive anticholinergic toxicity |
| Loperamide | Moderate | Combined antimotility effect; risk of paralytic ileus |
| Nabilone | Moderate | Additive CNS depression and anticholinergic effects |

> The full interaction profile includes 67 interactions. Prescribers should review the complete DDI list before co-administration, particularly with any anticholinergic, CNS-depressant, or potassium-containing preparation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic hypothesis is sound — dimenhydrinate's active metabolite diphenhydramine is an established first-line H1 antihistamine for allergic urticaria — there are zero clinical trials and only one indirect pharmacokinetic study using dimenhydrinate as the test drug. The drug is also not marketed in India, meaning no local regulatory dossier exists. The current evidence base (L4) is insufficient to support a repurposing claim without further dedicated investigation.

**To proceed, the following is needed:**

- **MOA and package insert data**: Obtain full DrugBank MOA record and CDSCO/reference regulatory labelling (warnings, contraindications, special populations) to complete the S1 safety screen
- **Bridging PK/PD study**: Confirm that plasma diphenhydramine exposure from dimenhydrinate is equivalent to therapeutic diphenhydramine doses used in urticaria trials
- **Pilot clinical study**: A Phase 2 randomised controlled trial comparing dimenhydrinate to cetirizine or loratadine (second-generation standard-of-care) in mild-to-moderate allergic urticaria would define efficacy and tolerability
- **Regulatory strategy**: Evaluate whether a 505(b)(2)-equivalent pathway (or India's bridging submission route) can leverage existing diphenhydramine data to reduce the clinical development burden
- **Safety monitoring plan**: Given the 67 documented DDIs — including two Major-level interactions with potassium salts — a formal drug interaction management protocol must be developed before any clinical use
- **Patient population scoping**: Clarify whether the target population would be adults only, or whether paediatric use (a common population for urticaria) is intended, as this affects study design and dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

