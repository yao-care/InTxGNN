---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting recombinant insulin analog widely used for basal glycemic control in Type 1 and Type 2 diabetes mellitus.
The TxGNN model predicts it may have a role in **Autoimmune Oophoritis**, achieving a prediction score of **99.88%**;
however, **zero clinical trials and zero published literature** currently support this direction — all 10 predicted indications remain at the hypothesis stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes mellitus (Type 1 & Type 2; standard clinical use) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, insulin glargine is a modified long-acting human insulin analog that provides a peakless, 24-hour basal insulin profile. It binds to insulin receptors (IR) and cross-reacts with IGF-1 receptors (IGF-1R), activating the PI3K–Akt and MAPK signaling cascades that govern glucose uptake, protein synthesis, lipid metabolism, and cell survival.

The connection to autoimmune oophoritis is indirect and most likely reflects knowledge graph topology rather than a direct therapeutic mechanism. Insulin and IGF-1R signaling do influence ovarian granulosa cell steroidogenesis — a relationship best studied in the context of polycystic ovary syndrome (PCOS) and hyperinsulinemia. However, autoimmune oophoritis is a T-cell–mediated immune destruction of ovarian follicles, a pathophysiology that insulin signaling does not directly modulate. The TxGNN model's high score almost certainly arises from the close proximity of Type 1 Diabetes Mellitus (T1DM) and autoimmune oophoritis nodes in the knowledge graph: both are classic organ-specific autoimmune diseases that share immune regulatory axes (e.g., regulatory T-cell dysfunction, HLA susceptibility loci), making them graph neighbors without implying a pharmacological bridge.

Among all 10 predicted indications, the most biologically grounded signal is **opsismodysplasia** (Rank 5), caused by loss-of-function mutations in *INPPL1* (SHIP2) — a phosphatase that is a direct negative regulator of the insulin PI3K–Akt pathway. SHIP2 deficiency would theoretically amplify insulin downstream signaling, making this the one candidate with a genuine mechanistic hypothesis worth exploring preclinically. All other predictions, including the lipodystrophy cluster, either reflect reverse causation (insulin injections *cause* lipodystrophy) or comorbidity association rather than actionable repurposing targets.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## India Market Information

Insulin glargine is currently **not registered or marketed in India**. No product licenses were found in the CDSCO database.

---

## Safety Considerations

**Drug Interactions (352 interactions identified; key examples below):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Metformin | Moderate | Additive glucose-lowering; monitor for hypoglycemia |
| Pioglitazone | Moderate | Enhanced hypoglycemic effect; dose adjustment may be needed |
| Alogliptin | Moderate | Additive antidiabetic effect; blood glucose monitoring required |
| Albiglutide | Moderate | Additive glucose-lowering; titrate insulin accordingly |
| Hydrocortisone | Moderate | Corticosteroids antagonize insulin; may substantially increase insulin requirements |
| Hydrochlorothiazide | Moderate | Thiazide diuretics may reduce insulin efficacy and raise blood glucose |
| Ethanol | Moderate | Potentiates hypoglycemia; unpredictable glycemic response; patient counseling required |
| Epinephrine | Moderate | Catecholamines elevate blood glucose and blunt hypoglycemia awareness |
| Acebutolol | Moderate | Beta-blockers may mask tachycardia as a hypoglycemia warning sign |
| Formoterol | Moderate | Beta-2 agonists may impair hypoglycemia recognition and raise blood glucose |
| Salbutamol | Moderate | Same mechanism as formoterol; monitor glycemia during acute bronchospasm treatment |
| Pseudoephedrine | Moderate | Sympathomimetic; may increase blood glucose |
| Phenylephrine | Moderate | Sympathomimetic; may increase blood glucose |
| Ethinylestradiol | Moderate | Estrogens alter insulin sensitivity; requirements may change |
| Estradiol | Moderate | Same class effect as ethinylestradiol |
| Alpelisib | Moderate | PI3K inhibitor causes hyperglycemia; insulin dose escalation often required |
| Acetazolamide | Moderate | Carbonic anhydrase inhibition may alter glycemic control |
| Doxycycline | Moderate | Tetracyclines reported to affect blood glucose; monitor glycemia |
| Hydrocortisone (topical) | Minor | Minimal systemic absorption; low glycemic impact under normal use |
| Alclometasone (topical) | Minor | Topical corticosteroid; systemic effect negligible at standard doses |

Please refer to the package insert for complete warnings and contraindications (currently not retrieved in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 10 TxGNN-predicted indications for insulin glargine returned zero supporting clinical trials and zero published literature, placing all candidates at L5 (model prediction only). The top-ranked prediction — autoimmune oophoritis — reflects knowledge graph co-clustering of autoimmune diseases rather than a mechanistically actionable insulin–ovarian immunity link. Proceeding without at least preclinical or mechanistic evidence would not meet a credible repurposing threshold.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001**: Retrieve CDSCO or global package insert to populate key warnings and contraindications — this is classified as Blocking for any safety review
- **Resolve Data Gap DG002**: Query the DrugBank API to confirm the official MOA and original approved indications — the absence of `original_indications` likely causes system misclassification of "pancreatic agenesis" (a standard insulin indication) as a novel repurposing candidate
- **Prioritize opsismodysplasia for hypothesis exploration**: This is the only candidate among the 10 with a direct mechanistic rationale (SHIP2/INPPL1 as a negative insulin-pathway regulator); a targeted scoping review of INPPL1 knockout model data would clarify feasibility
- **Exclude reverse-causation candidates**: Drug-induced localized lipodystrophy should be removed from the candidate list — insulin glargine is an established *cause* of this condition, not a treatment
- **Confirm pancreatic agenesis status**: If insulin replacement is already standard-of-care for pancreatic agenesis, this indication should be reclassified as an existing use rather than a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

