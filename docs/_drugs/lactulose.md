---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose: From Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a well-established non-absorbable disaccharide used clinically for hepatic encephalopathy and constipation, acting primarily by acidifying the colon and modulating gut microbiota to reduce systemic ammonia and endotoxin load.
The TxGNN model predicts it may be effective for **Acute Urate Nephropathy**, supported theoretically by the gut-kidney axis and lactulose's known anti-endotoxemia properties.
However, currently there are **no registered clinical trials** and **no supporting publications** for this specific indication, placing this prediction at the hypothesis-generation stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic encephalopathy; Constipation |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the queried data sources. Based on established clinical and pharmacological knowledge, Lactulose is a synthetic non-digestible disaccharide that is not absorbed in the small intestine. Upon reaching the colon, it is fermented by resident bacteria into short-chain organic acids (lactic acid, acetic acid), which acidify the colonic lumen, create an osmotic gradient that draws water into the bowel, and selectively reshape the gut microbial ecosystem. These properties drive its efficacy in hepatic encephalopathy — where the acidic environment protonates ammonia into non-absorbable ammonium (NH₄⁺) — and in constipation via its osmotic and pro-motility effects.

Acute urate nephropathy occurs when uric acid crystallises within renal tubules, most often triggered by rapid cell turnover (such as tumour lysis syndrome) or sustained hyperuricaemia leading to tubular obstruction and acute kidney injury. An emerging body of basic-science research points to a gut-kidney axis in uric acid homeostasis: gut bacteria, particularly *Lactobacillus* species, can degrade purines and uric acid in the intestinal lumen; when this microbial capacity is diminished, greater purine substrate reaches systemic circulation, potentially raising serum urate. Lactulose, by promoting a lactobacillus-enriched, low-pH colonic environment, may theoretically enhance gut-level degradation of uric acid precursors and reduce the intestinal reabsorption of urate, thereby lowering the systemic urate burden that drives tubular crystal deposition.

A further mechanistic thread is lactulose's well-documented ability to reduce systemic endotoxaemia — a property evidenced extensively in the obstructive jaundice literature contained within this Evidence Pack. Circulating endotoxin activates renal tubular inflammation, which can impair the tubular secretion of uric acid and worsen crystal-driven injury. By protecting gut barrier integrity and dampening portal endotoxin translocation, lactulose may indirectly preserve renal tubular function in states of hyperuricaemia. Taken together, these indirect mechanistic pathways offer a biologically plausible — though still speculative — rationale for the TxGNN prediction. Dedicated preclinical and clinical studies are needed before any causal claim can be made.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lactulose in Acute Urate Nephropathy.

---

## Literature Evidence

Currently no related literature available for Lactulose in Acute Urate Nephropathy.

---

## India Market Information

Lactulose currently holds no product registrations in India. No marketing authorisations, approved indications, or licensed dosage forms were identified in the regulatory database.

---

## Safety Considerations

**Drug Interactions**: The DDInter database records 533 known interactions for Lactulose. The following are representative entries; the full interaction list should be reviewed before clinical use.

| Interacting Drug | Severity | Source |
|------------------|----------|--------|
| Abiraterone | Moderate | DDInter |
| Amiodarone | Moderate | DDInter |
| Hydrochlorothiazide | Moderate | DDInter |
| Amiloride | Moderate | DDInter |
| Acetazolamide | Moderate | DDInter |
| Hydrocortisone | Moderate | DDInter |
| Tramadol | Moderate | DDInter |
| Propofol | Moderate | DDInter |
| Arsenic trioxide | Moderate | DDInter |
| Sodium citrate | Minor | DDInter |

Please refer to the package insert for complete warnings and contraindications, which were not available in the current data pull.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score of 99.89%, no clinical trials or supporting literature exist for Lactulose in acute urate nephropathy; the mechanistic link, while biologically plausible through gut microbiome modulation and anti-endotoxaemia effects, remains indirect and unvalidated. A Hold is appropriate until foundational preclinical and safety data confirm the hypothesis.

**To proceed, the following is needed:**
- Retrieval and review of the full Lactulose package insert to fill the blocking data gap on warnings and contraindications (DG001)
- DrugBank MOA data to formalise the mechanistic rationale (DG002)
- Preclinical studies (animal model) measuring lactulose's effect on serum and urinary uric acid levels and renal tubular urate handling
- Systematic literature review for any indirect evidence linking lactulose, gut microbiota, and uric acid metabolism
- Assessment of India regulatory pathway and data requirements for a new drug introduction, given zero existing registrations
- If preclinical data is supportive, design a Phase 2 proof-of-concept trial in patients at high risk for acute urate nephropathy (e.g., pre-chemotherapy tumour lysis prophylaxis setting)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

