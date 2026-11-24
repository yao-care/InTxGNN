---
layout: default
title: Ribociclib
parent: Moderate Evidence (L3-L4)
nav_order: 737
evidence_level: L4
indication_count: 4
last_modified_at: 2026-11-24
description: "Ribociclib: predicted new indication Myeloid leukemia (evidence level L4). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Ribociclib"
predicted_indications: ["myeloid leukemia", "thrombocytopenia", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets"]
---

# Ribociclib
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

## Ribociclib: From Breast Cancer to Myeloid Leukemia
{: .text-alpha }

## One-Sentence Summary

Ribociclib is a CDK4/6 inhibitor, marketed in India as an oral tablet (Kryxana 200 mg).
The TxGNN model predicts it may be effective for **myeloid leukemia**, but this rests on a computational score and **one relevant preclinical publication**, with **no registered clinical trials** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the license record has no indication text) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L4 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ribociclib inhibits CDK4/6, which regulate progression from the G1 to the S phase of the cell cycle. These kinases are often dysregulated in myeloid malignancies. This reasoning relies on the known drug class. According to the Mechanism of Action section of the US FDA-approved prescribing information for ribociclib: "Ribociclib is an inhibitor of cyclin-dependent kinase (CDK) 4 and 6. These kinases are activated upon binding to D-cyclins and are downstream of signaling pathways which lead to cell cycle progression and cellular proliferation." ([DailyMed: Kisqali (ribociclib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8), label version 2026-07-01; accessed 2026-11-19.)

A 2020 preclinical report suggests CDK4/6 inhibitors can address pharmacokinetic drug resistance in acute myeloid leukemia (AML) cells, in which ABCB1 and ABCG2 transporters are overexpressed. This offers a plausible but indirect rationale. The high TxGNN score is a computational prediction only and is not backed by clinical data.

**Other predictions were not pursued.** The model also ranked thrombocytopenia and two rare thrombocytopenia-related conditions highly. Thrombocytopenia is a known adverse effect of ribociclib and other CDK4/6 inhibitors, caused by suppression of blood-cell progenitor growth. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of therapeutic benefit, and treating thrombocytopenia with ribociclib would be counterproductive. They are not valid repurposing candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical / in vitro | Cancers | CDK4/6 inhibitors may counter ABCB1/ABCG2-mediated pharmacokinetic drug resistance in AML cells |

Another publication retrieved for this indication (PMID 41641105, a vulvar adenocarcinoma case report) is unrelated to myeloid leukemia and is excluded.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 115741 | Kryxana 200mg Tablet | Strip of 21 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | Medium to high. Neutropenia, leukopenia and thrombocytopenia are well-documented in the literature, including pharmacovigilance analyses and meta-analyses |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential), liver function, ECG/QT interval and electrolytes. Other CDK4/6 inhibitor reports also describe pneumonitis |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 579 interactions were identified in the DDI screening, mostly Moderate. Major interactions in the listed results include **clarithromycin** and **dolasetron**. Moderate examples include corticosteroids (dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone), H2 blockers (famotidine, cimetidine), metformin, pioglitazone, saxagliptin, loperamide, aprepitant and alosetron.
- **Adverse events reported in the literature**: hematological toxicity (including thrombocytopenia), pneumonitis and visual hallucination (case reports).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to a computational prediction and a single preclinical study, with no registered clinical trials. Ribociclib's own myelosuppressive profile also calls for caution in a hematological malignancy setting.

**To proceed, the following is needed:**
- Mechanism of action data and a deeper mechanistic analysis for myeloid leukemia
- Package insert warnings and contraindications from the India license, plus the approved indication text
- Further preclinical validation in myeloid leukemia models, including myelosuppression risk
- A safety plan covering hematological monitoring and the major drug interactions above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Currently, detailed mechanism of action data is not available in the data compiled for this report, so this reasoning relies on the known drug class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Kisqali (ribociclib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

