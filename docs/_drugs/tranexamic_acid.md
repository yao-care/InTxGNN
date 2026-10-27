---
layout: default
title: Tranexamic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 854
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Tranexamic Acid: predicted new indication Amenorrhea (evidence level L4). Approved use: Endometriosis"
monitor_inn: "Tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Tranexamic Acid: From Endometriosis to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent; in the knowledge graph used for this analysis it is linked to endometriosis, and it is widely marketed in India.
The TxGNN model predicts it may be effective for **Amenorrhea**, but there are **0 clinical trials** and only **2 review articles** supporting this direction.
The prediction is best read as a computational signal, not a validated therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the marketed-product records compiled for this report contain no approved indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tranexamic acid is an antifibrinolytic (lysine analogue) that blocks plasminogen activation and reduces fibrinolysis, which lowers menstrual blood loss.

That mechanism plausibly supports use in heavy menstrual bleeding and in menses suppression or prophylaxis, for example in premenopausal haematology patients at risk of heavy bleeding. However, amenorrhea is the absence of menses. Tranexamic acid does not treat its underlying causes and does not induce menstruation, so the link to the predicted indication is indirect.

The high TxGNN score (0.99) probably reflects network proximity to menstrual disorders in the knowledge graph rather than a true therapeutic relationship. The lack of documented mechanism data further limits confidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of drug therapy for abnormal uterine bleeding; nonhormonal options reduce bleeding and selection depends on cause, bleeding amount, contraception needs and menopausal status |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in premenopausal haematologic cancer patients; notes little comparative data for these therapies |

Both publications address bleeding control or menses suppression, not treatment of amenorrhea itself.

---

## India Market Information

Twenty valid single-ingredient registrations were found. Five representative entries are shown below; no approved indication text is recorded for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 216788 | Tranfib 500mg Tablet | Strip of 10 tablets | Cipla Ltd |
| 214856 | Trapic 500mg Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 152402 | Nexamic 500mg Tablet | Strip of 10 tablets | Mac Millon Pharmaceuticals Pvt Ltd |
| 160047 | Naxic Injection | Ampoule of 5 ml injection | Rizpan Life Sciences Private Limited |
| 226120 | Tranguard Injection | Ampoule of 5 ml injection | Curador Healthcare Pvt Ltd |

Available routes are oral (tablets) and injectable (ampoules and vials).

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals (not label text)**: associations with hypertension, liver and gallbladder disease, diabetes and hyperglycaemia, hyperlipidaemia, coronary artery disease, stroke and cerebrovascular disorder, thrombophlebitis, migraine, porphyria, breast carcinoma and endometrial cancer. These resemble estrogen-class warnings and should be verified against the actual label.
- **Drug Interactions**: 35 interactions were identified, including 20 listed here. Most are Major, notably with estrogens and hormonal contraceptives (ethinylestradiol, estradiol, conjugated estrogens, norethisterone, drospirenone, etonogestrel, diethylstilbestrol), anti-inhibitor coagulant complex, Factor IX complex and carfilzomib. Moderate interactions include thrombolytics (alteplase, anistreplase). The main concern is additive thrombotic risk with hormonal and procoagulant agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no registered trials and only two general reviews that do not address amenorrhea. The mechanism (reducing bleeding) does not fit the disease (absence of menses), so the prediction is likely a network artefact. A more defensible direction would be heavy menstrual bleeding or menses suppression, rather than amenorrhea.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A clinical rationale for whether amenorrhea, rather than heavy menstrual bleeding or menses suppression, is the intended target
- Clinical studies or controlled data in the proposed use
- Assessment of thrombotic risk when combined with hormonal agents, as menses suppression often involves them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

