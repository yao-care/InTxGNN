---
layout: default
title: Diazoxide
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diazoxide is a potassium channel opener (KATP activator) with established use in treating hyperinsulinemic hypoglycemia and hypertensive emergencies, and is well-known to cause hypertrichosis (excessive hair growth) as a dose-related side effect.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, a hereditary hair-loss disorder affecting the scalp.
Currently, **no clinical trials** and **no supporting publications** exist for this specific indication, placing it at evidence level **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperinsulinemic hypoglycemia; hypertensive emergencies |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on well-established pharmacology, Diazoxide activates ATP-sensitive potassium channels (KATP) — specifically the SUR2B subtype expressed in hair follicle dermal papilla cells. This activation increases K⁺ efflux, causing membrane hyperpolarization, which in turn prolongs the anagen (active growth) phase of the hair cycle. This mechanism is functionally identical to that of minoxidil, whose active metabolite (minoxidil sulfate) is also a KATP opener. Critically, the hypertrichosis (dose-related excessive hair growth) routinely observed during systemic Diazoxide therapy for hyperinsulinism confirms that this KATP-mediated hair-growth mechanism is biologically active in humans — not merely theoretical.

Hypotrichosis simplex of the scalp, however, is a hereditary condition driven by loss-of-function mutations in LPAR6 or LIPH genes. These genes govern the lipid composition of the hair shaft itself, disrupting hair shaft structural integrity at the follicular level — a process distinct from the hair growth cycle modulated by KATP channels. Whether KATP activation in genetically defective follicles can meaningfully compensate for this structural defect is entirely unknown. The mechanistic connection is a plausible hypothesis (anagen-phase extension may partially offset hair loss), but has not been tested in any preclinical or clinical model of this specific condition.

The TxGNN prediction score of 99.96% most likely reflects the knowledge graph's strong established association between Diazoxide and hair biology (via the well-documented hypertrichosis adverse effect), which the model has re-interpreted as a potential therapeutic signal for hair loss disorders. While this is not an unreasonable extrapolation, careful disambiguation is needed: the drug causes excess hair growth systemically, but whether it can rescue genetically-impaired follicular function specifically in hypotrichosis simplex remains a pure open research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available specifically for hypotrichosis simplex of the scalp.

> **Mechanistic context from related predictions:** Relevant preclinical and observational evidence exists for the broader hair-biology prediction cluster. For alopecia (rank 4 in this Evidence Pack), 9 publications were retrieved — most notably a 1990 primate study ([PMID 2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/)) demonstrating that topical 5% Diazoxide significantly promoted hair regrowth in the bald scalp of stumptailed macaques (androgenetic alopecia model), and a 1993 comparative review ([PMID 8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/)) placing Diazoxide alongside minoxidil as a KATP-mediated hair growth promoter. These provide mechanistic plausibility but do not directly address hypotrichosis simplex.

---

## India Market Information

Diazoxide is currently **not registered or marketed in India**. No authorization records are available (total licenses: 0).

---

## Safety Considerations

**Drug Interactions**: Diazoxide has **209 documented drug interactions** (DDInter database). The majority reflect its core pharmacological effects — raising blood glucose (by suppressing insulin secretion) and causing vasodilation (hypotension, sodium retention). The most clinically significant moderate-severity interactions include:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Metformin | Moderate | Diazoxide raises blood glucose, opposing antidiabetic effect |
| Acarbose | Moderate | Diazoxide raises blood glucose, opposing antidiabetic effect |
| Alogliptin | Moderate | Diazoxide raises blood glucose, opposing DPP-4 inhibitor effect |
| Canagliflozin | Moderate | Diazoxide raises blood glucose, opposing SGLT2 inhibitor effect |
| Dapagliflozin | Moderate | Diazoxide raises blood glucose, opposing SGLT2 inhibitor effect |
| Empagliflozin | Moderate | Diazoxide raises blood glucose, opposing SGLT2 inhibitor effect |
| Pioglitazone | Moderate | Diazoxide raises blood glucose, opposing thiazolidinedione effect |
| Chlorpropamide | Moderate | Diazoxide raises blood glucose, opposing sulfonylurea effect |
| Hydrocortisone | Moderate | Additive hyperglycemic effect (corticosteroid + KATP opener) |
| Dexamethasone | Moderate | Additive hyperglycemic effect |
| Betamethasone | Moderate | Additive hyperglycemic effect |
| Budesonide | Moderate | Additive hyperglycemic effect |
| Triamcinolone | Moderate | Additive hyperglycemic effect |
| Morphine | Moderate | Cardiovascular and hemodynamic interactions |
| Bupropion | Moderate | CNS/cardiovascular interactions |

Please refer to the package insert for complete warnings and contraindications (formal safety data not yet available in this Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for hypotrichosis simplex of the scalp is mechanistically interesting but rests entirely on an inference from Diazoxide's known hypertrichosis side effect — there is no clinical trial, no human study, and no disease-specific preclinical model to validate efficacy. Additionally, systemic Diazoxide carries meaningful cardiovascular risks (hypotension, fluid retention) that make topical-only delivery the sole viable path for a hair indication, adding a significant formulation development burden.

**To proceed, the following is needed:**

- **Preclinical validation**: Test topical Diazoxide in LPAR6- or LIPH-deficient mouse models or hair follicle organoid systems to determine whether KATP activation can rescue structurally impaired follicle function
- **Topical formulation development**: Demonstrate that a topical formulation achieves adequate follicular penetration with negligible systemic absorption (to avoid cardiovascular adverse effects)
- **Mechanistic study**: Confirm that KATP channels in LPAR6/LIPH-deficient follicles are functionally intact and capable of responding to Diazoxide stimulation
- **Competitive analysis**: Evaluate whether topical Minoxidil (already approved, well-established safety profile) covers the same KATP mechanism sufficiently, and whether a Diazoxide formulation offers any differentiated benefit
- **MOA documentation**: Retrieve complete Diazoxide mechanism of action data from DrugBank API to support any future regulatory pre-consultation
- **Safety package completion**: Obtain CDSCO/TFDA package insert data to fill current data gaps in warnings and contraindications before initiating any human study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

