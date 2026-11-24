---
layout: default
title: Triptorelin
parent: Model Prediction Only (L5)
nav_order: 870
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Triptorelin"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "allergic urticaria", "familial male-limited precocious puberty", "familial isolated trichomegaly", "aromatase excess syndrome"]
description: "Triptorelin: predicted new indication Hypertrichosis (disease) (evidence level L5). In India: 6 listed products (6 not discontinued)"
---

# Triptorelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Triptorelin: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Triptorelin is a gonadotropin-releasing hormone (GnRH) agonist that suppresses sex hormone production.
The TxGNN model predicts it may be useful for **hypertrichosis (disease)**, but **no clinical trials** and **only 1 publication** were found.
That publication is a case report of a drug side effect, not evidence that triptorelin treats the condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for triptorelin: "Triptorelin is a synthetic decapeptide agonist analog of gonadotropin releasing hormone (GnRH). Comparative in vitro studies showed that triptorelin was 100-fold more active than native GnRH in stimulating luteinizing hormone release from monolayers of dispersed rat pituitary cells in culture and 20-fold more active than native GnRH in displacing 125 I-GnRH from pituitary receptor sites." ([DailyMed: Trelstar (triptorelin pamoate) prescribing information, Verity Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b84d62-a369-a4b7-5c41-dd1f553a18f3), label version 2026-06-30; accessed 2026-11-19.) Triptorelin belongs to the GnRH agonist class. With continuous exposure, these drugs desensitise the pituitary and lower LH, FSH and sex-steroid levels. In theory, lowering androgen levels could matter for some hair-growth disorders.

In practice, the link to hypertrichosis is weak. Hypertrichosis is most often drug-induced or genetic, and it is not typically driven by gonadotropin-mediated androgen excess. No credible mechanism was identified by which triptorelin would treat it. The high model score most likely reflects proximity between the drug and the disease in the model's data rather than a true therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report | Cureus | Ciclosporin-induced generalised hypertrichosis in a transgender woman with psoriasis who was also taking estradiol and triptorelin. It describes a side effect of ciclosporin and does not show a benefit of triptorelin. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 58621 | Decapeptyl 0.1mg Injection | Vial of 1 ml Injection | Valid |
| 59940 | Decapeptyl Depot Injection | Vial of 1 Injection | Valid |
| 174365 | Pamorelin LA 11.25mg Powder for Injection | Vial of 1 Powder for Injection | Valid |
| 175170 | Pamorelin LA 3.75mg Injection | Vial of 1 Injection | Valid |
| 175479 | Pamorelin LA 22.5mg Injection | Vial of 1 Injection | Valid |
| 222576 | Tryplog Injection | Vial of 5 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All licences are for single-ingredient injectable products and are currently valid. A sixth valid licence (Tryplog Injection, Life Medicare & Biotech Pvt Ltd) is also on record.

## Safety Considerations

- **Drug Interactions**: 262 interactions were recorded. One is rated Major: dolasetron. Many others are rated Moderate, including:
  - antidiabetic drugs (acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide, dulaglutide)
  - clarithromycin
  - famotidine
  - loperamide
  - palonosetron
  - bowel-preparation and laxative agents (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials, and the only publication is a case report of a side effect of another drug. No plausible mechanism links GnRH agonism to treating hypertrichosis, so the evidence level is L5.

**To proceed, the following is needed:**
- A defined mechanistic hypothesis for how lowering sex hormones would affect hypertrichosis
- Controlled or observational clinical data on triptorelin in this condition
- Package insert warnings and contraindications for the marketed products
- Detailed mechanism-of-action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Trelstar (triptorelin pamoate) prescribing information, Verity Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b84d62-a369-a4b7-5c41-dd1f553a18f3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

