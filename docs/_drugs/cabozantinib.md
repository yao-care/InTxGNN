---
layout: default
title: Cabozantinib
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 5
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
last_modified_at: 2026-10-27
description: "Cabozantinib: predicted new indication liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Cabozantinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cabozantinib: multikinase inhibitor (VEGFR2, MET, AXL) → liposarcoma
{: .text-alpha }

## One-Sentence Summary

Cabozantinib is an oral multikinase inhibitor that blocks VEGFR2, MET and AXL, and it is marketed in India as single-ingredient tablets.
The TxGNN model predicts it may be effective for **liposarcoma**, but the support is indirect: **1 clinical trial** and **1 publication** are listed, and both study soft tissue sarcoma in general rather than liposarcoma specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | liposarcoma |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cabozantinib inhibits VEGFR2, MET and AXL. These pathways are involved in tumour angiogenesis and progression, including in soft tissue sarcomas.

Liposarcoma is a soft tissue sarcoma, so activity in this group of tumours is biologically plausible. However, liposarcoma-specific data are limited. The listed studies cover mixed sarcoma subtypes, so they do not show that cabozantinib works in liposarcoma itself.

Because no listed study directly addresses liposarcoma, the evidence level is L5 (model prediction with no direct study), even though related sarcoma studies exist.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomised trial of ipilimumab + nivolumab with or without cabozantinib in advanced soft tissue sarcoma. It is not liposarcoma-specific and has not reported results. The combination design makes it hard to isolate cabozantinib's own contribution. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | American Journal of Clinical Oncology | Evaluated the safety of neoadjuvant cabozantinib given with radiation therapy in extremity soft tissue sarcoma. Cabozantinib has shown activity in several sarcoma subtypes, and the study addressed concern about fistula or perforation with concurrent radiation. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38313 | Cabolong Tablet | Bottle of 30 tablets | Not recorded |
| 36242 | Cabotib 40 Tablet | Bottle of 30 tablets | Not recorded |
| 40996 | Cabotib 20 Tablet | Bottle of 30 tablets | Not recorded |
| 36088 | Cabotres 20 Tablet | Bottle of 30 tablets | Not recorded |
| 35518 | Cabotres 40 Tablet | Bottle of 30 tablets | Not recorded |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interactions, of which the first 20 are shown here. Major-level interactions include acetylsalicylic acid, cisapride, clarithromycin, dolasetron, granisetron and levofloxacin. Moderate-level interactions include loperamide, aprepitant, dexamethasone, bisacodyl and several laxatives (castor oil, glycerin, lactitol, lactulose, magnesium citrate). Fidaxomicin is Minor.
- **Other safety notes**: A phase 1 study flagged concern about fistula or perforation when cabozantinib is combined with radiation therapy.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for liposarcoma is high (0.9983), but no listed study directly examines liposarcoma. The only supporting studies are in mixed soft tissue sarcoma, one of them a combination with checkpoint inhibitors.

**To proceed, the following is needed:**
- Liposarcoma-specific clinical data, or sarcoma trials reporting results by subtype
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India licence holders
- A safety plan covering the interaction profile and the fistula/perforation risk seen with radiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

