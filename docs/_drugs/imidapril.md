---
layout: default
title: Imidapril
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 5
---

# Imidapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imidapril: From Hypertension/Heart Failure to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Imidapril is an ACE (Angiotensin-Converting Enzyme) inhibitor used internationally — most notably approved in Japan — to treat hypertension and chronic heart failure, but currently holds no marketing authorisation in India (CDSCO).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension with Unclear Multifactorial Mechanism (WHO Group 5)**, with a prediction score of 99.78%.
However, **0 clinical trials** and **0 directly relevant publications** currently support this specific repurposing direction, making this a model-only prediction with no clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Chronic Heart Failure (pharmacological use in Japan; PMDA-approved; no India CDSCO record) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism (WHO Group 5) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Imidapril is a prodrug ACE inhibitor. After oral administration, it is hydrolysed to its active diacid metabolite imidaprilat, which competitively inhibits the Angiotensin-Converting Enzyme (ACE, gene: *ACE*, ENSEMBL: ENSG00000159640). By preventing the conversion of Angiotensin I to Angiotensin II, imidapril reduces systemic vascular resistance, lowers blood pressure, and decreases cardiac afterload — forming the mechanistic basis for its use in hypertension and heart failure. Detailed MOA documentation is not yet retrieved from DrugBank for this candidate; the above is inferred from pharmacology database data included in this Evidence Pack.

From a theoretical standpoint, reduced Angiotensin II could attenuate pulmonary vasoconstriction, since the RAAS pathway contributes to pulmonary vascular tone and remodelling. This theoretical overlap may explain why the TxGNN knowledge-graph model, which encodes biological pathway relationships, generates a high prediction score for imidapril in pulmonary hypertension.

However, the top-ranked prediction targets **WHO Group 5 PH** — "pulmonary hypertension with unclear multifactorial mechanisms" — a heterogeneous category encompassing sarcoidosis, Langerhans cell histiocytosis, and myeloproliferative disorders. Guidelines for Group 5 PH recommend treating the underlying cause; there is no established or emerging role for ACE inhibitors in this subgroup. The model's score almost certainly reflects the drug's cardiovascular network topology rather than any validated mechanism in this disease. It should be read as a hypothesis-generation signal, not clinical endorsement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Imidapril in pulmonary hypertension with unclear multifactorial mechanism.

---

## Literature Evidence

Currently no related literature directly linking Imidapril to pulmonary hypertension with unclear multifactorial mechanism.

> **Contextual note:** For the closely related prediction (Rank 2 — WHO Group 3 PH: pulmonary hypertension due to lung disease and/or hypoxia), 20 PubMed records were retrieved. However, none of these papers study imidapril or ACE inhibitors in pulmonary hypertension. They are general hypoxia biology reviews and basic-science studies spanning neurology, oncology, and cell signalling (e.g., HIF-1α regulation, keloid fibroblasts, brain hypoxia). These are **not** considered supporting evidence for this repurposing candidate.

---

## India Market Information

Imidapril is currently **not approved** for marketing in India. The CDSCO database returns no registered licenses, product authorisations, or dosage-form records for this drug.

> **Reference point:** Imidapril holds PMDA approval in Japan under the brand name **Tanatril** (5 mg, 10 mg tablets) for essential hypertension and renal parenchymal hypertension. No equivalent approval pathway has been initiated in India. Any development path for this drug in India would begin from zero regulatory history.

---

## Safety Considerations

**Drug-Target Interaction (Pharmacology Source):**
Imidapril acts as a selective inhibitor of human Angiotensin-Converting Enzyme (ACE). CAS: 89371-37-9. SMILES confirms it is a synthetic organic compound with a chiral imidazolinone scaffold. One pharmacological interaction was identified in this Evidence Pack.

**Class-Level Safety Signals (from known ACE inhibitor pharmacology):**

- **Renovascular Hypertension — Known Contraindication:** One of the five TxGNN predictions for imidapril is *malignant renovascular hypertension* (Rank 4, score 99.76%). This is a recognised contraindication for ACE inhibitors. In renal artery stenosis, GFR on the affected side depends on Angiotensin II to maintain efferent arteriolar tone; ACE inhibition removes this compensation and can precipitate **acute kidney injury (AKI)**. This prediction is assessed as a false positive (TxGNN confusing the "hypertension" node), and serves as a safety red flag that warrants scrutiny of all five predictions before any further development step.

- **Hypotension Risk in PH Patients:** Pulmonary hypertension patients frequently have low systemic blood pressure and reduced right ventricular reserve. ACE inhibitors carry intrinsic risk of systemic hypotension in this population, which could worsen haemodynamic status.

- **Full Package Insert Not Available:** Warnings, contraindications, and monitoring requirements from the PMDA-approved Tanatril prescribing information were not retrieved in this Evidence Pack. Please consult the PMDA SmPC directly before any clinical assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.78%), the top indication — WHO Group 5 pulmonary hypertension — has zero clinical trial evidence, zero directly relevant literature, and no guideline-supported mechanistic basis for ACE inhibitor use. Concurrently, one prediction in this five-candidate cluster (malignant renovascular hypertension) represents an established contraindication for this drug class, raising concerns about model reliability in this particular region of the disease graph. With no India CDSCO regulatory history and no safety documentation in hand, proceeding without further evidence gathering would be premature.

**To proceed, the following is needed:**
- Retrieve and parse the full PMDA Tanatril prescribing information (warnings, contraindications, dose adjustments) before any safety stage can be entered
- Obtain DrugBank API data for imidapril MOA, categories, and toxicity profile
- Conduct a targeted literature search for ACE inhibitors (class-level) in WHO Group 5 PH specifically — if class evidence exists, Imidapril may be eligible for indirect L4 upgrading
- Evaluate haemodynamic feasibility: assess whether ACE inhibitor use is safe in PH patients with low baseline systemic pressure
- Confirm the Rank 3 indication (malignant hypertensive renal disease, L4) as the more actionable near-term candidate — it has stronger mechanistic grounding via established ACE inhibitor renoprotection, and should be prioritised over Group 5 PH in any development roadmap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

