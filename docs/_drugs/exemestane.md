---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 335
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal, irreversible aromatase inhibitor that lowers estrogen levels. It is marketed in India under several brand names.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.
Evidence is therefore at the model-prediction level, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data compiled for this report (the approved indication text is empty for all licences) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, exemestane is a steroidal irreversible aromatase inhibitor that lowers circulating estrogen. It is generally used in hormone-receptor-positive breast cancer in postmenopausal women.

Antithrombin deficiency type 2 is a hereditary defect in the function of the SERPINC1 gene product. Estrogen lowering is not expected to correct this defect. Any effect on thrombotic risk would be indirect and speculative. The high TxGNN score appears to reflect network proximity in the knowledge graph rather than a biological rationale.

Other predictions in the list show the same pattern:

- **Amenorrhea:** The literature (cohort studies and reviews, mostly in breast cancer) treats amenorrhea as a marker of ovarian function after chemotherapy or ovarian suppression. It is not a condition treated by exemestane, and aromatase inhibition would not be expected to treat it.
- **Thrombophilia-related conditions** (factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, thrombophilia): There are no trials or literature. Aromatase inhibitors have shown lower venous thromboembolism rates than tamoxifen in breast cancer, but this is a different context and does not address inherited thrombophilia.
- **Migraine disorder and migraine with brainstem aura:** There is no clinical evidence. Estrogen lowering could theoretically influence estrogen-withdrawal-sensitive migraine, but the direction of effect is uncertain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication, antithrombin deficiency type 2.

For the second-ranked prediction (amenorrhea), five indirect publications were retrieved. They are not evidence for a therapeutic indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort | Annals of Oncology | Ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhea who switched from tamoxifen to exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone-receptor-positive early breast cancer |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review | Journal of Clinical Oncology | Whether estradiol monitoring is necessary during ovarian suppression for breast cancer |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Progressi in Medicina | Current role of LHRH analogues in premenopausal breast cancer |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klinicka Onkologie | Aromatase inhibitor treatment in postmenopausal breast cancer and management of side effects |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 243847 | Xtane Tablet (Natco Pharma Ltd) | Bottle of 30 tablets | Not specified |
| 16628 | Aromasin 25mg Tablet (Pfizer Ltd) | Strip of 15 tablets | Not specified |
| 244021 | Xemasin 25mg Tablet (Zee Laboratories) | Strip of 10 tablets | Not specified |
| 74595 | Exeget 25mg Tablet (GLS Pharma Ltd.) | Strip of 10 tablets | Not specified |
| 75614 | Exmasin 25mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 5 tablets | Not specified |

Two further valid single-ingredient licences (76776 Exetraz, Alkem; 244202 Xmalon, Celon) are not shown. All 7 registrations are valid, with none cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, not a conventional cytotoxic agent |
| Myelosuppression Risk | Low |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions:** 203 interactions were recorded. Two are rated Moderate: dexamethasone and troglitazone. The rest have no severity rating, and include pantoprazole, omeprazole, metformin, simvastatin, morphine, and aspirin (acetylsalicylic acid).
- **Contraindications:** The literature notes that aromatase inhibitors are contraindicated in women with functional ovaries, so premenopausal use requires concurrent ovarian suppression.

Please also refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only a high model score. There are no clinical trials or literature, and no plausible mechanistic link between estrogen suppression and correcting an antithrombin functional defect. None of the other six predicted indications has direct supporting evidence either.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indication text from the India regulatory source, which are currently missing and block safety screening
- Mechanism of action data from DrugBank to allow a proper mechanistic-link analysis
- Preclinical or mechanistic evidence connecting aromatase inhibition to antithrombin or other coagulation pathways, if the prediction is to be pursued
- Re-evaluation of the predictions with more plausible biology, since the thrombophilia and migraine predictions are likewise unsupported
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

