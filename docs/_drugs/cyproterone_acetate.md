---
layout: default
title: Cyproterone Acetate
parent: Moderate Evidence (L3-L4)
nav_order: 222
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-30
description: "Cyproterone Acetate: predicted new indication Migraine disorder (evidence level L4). Approved use: Not stated in the India license records (the drug's general clinical…"
monitor_inn: "Cyproterone acetate"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "amenorrhea (disease)", "breast fibrocystic disease", "thrombophilia"]
---

# Cyproterone Acetate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Cyproterone Acetate: From Androgen-Dependent Conditions to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Cyproterone acetate is a progestogen and antiandrogen, used in androgen-dependent conditions such as prostate cancer, acne and hirsutism in women, and in combined oral contraceptives.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and **3 publications**, none of which show that the drug treats migraine.
This prediction is a computational signal only and should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license records (the drug's general clinical use is androgen-dependent conditions, acne and hirsutism in women, and contraception) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L4 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyproterone acetate is a progestogen and androgen receptor antagonist, widely used in androgen-dependent diseases and in combined contraceptives (often with ethinylestradiol). Its efficacy in these hormone-related conditions is established.

Migraine, particularly menstrual and hormone-related migraine, is plausibly sensitive to sex-steroid fluctuation. A review of progestin effects on the brain notes that progestins interact with GABA-A receptors and dopamine and opioid systems, and that cyproterone acetate increases dopaminergic responses and binds opiate receptors independently of its classical action. This offers a loose biological link.

However, no retrieved paper shows that cyproterone acetate treats migraine. Estrogen-containing cyproterone products carry migraine-related vascular warnings, so the direction of effect is uncertain and could be harmful. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Two related predictions, *migraine with brainstem aura* and *migraine with or without aura, susceptibility to*, rest on the same weak basis. The literature for them concerns thrombotic and vascular risk of hormonal contraception, which is a safety signal rather than evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review | Maturitas | Progestins interact with GABA-A receptors and dopamine and opioid systems; cyproterone acetate increases dopaminergic responses and binds opiate receptors. Mechanistic background only. |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral hormone replacement schemes and their effects on migraine in postmenopausal women; not specific to cyproterone acetate. |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Review | Zentralblatt fur Gynakologie | Long-term side effects of cyproterone acetate-containing therapy in gynecology, including discussion of mutagenic potential; no migraine efficacy data. |

---

## India Market Information

Cyproterone acetate has 20 valid single-ingredient registrations; the license records provide no approved indication text. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 40795 | Carrol Tablet | Strip of 10 tablets | Not stated |
| Registration No. 35019 | Carpela Tablet | Strip of 21 tablets | Not stated |
| Registration No. 59882 | Dianette 2mg/0.035mg Tablet | Strip of 21 tablets | Not stated |
| Registration No. 74045 | Estranon Tablet | Strip of 21 tablets | Not stated |
| Registration No. 94234 | Ginette 35 Tablet | Strip of 21 tablets | Not stated |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal antiandrogen (not a conventional cytotoxic); used in prostate cancer palliation |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (liver function is commonly monitored with this drug) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry, the drug's own target, the androgen receptor (an antagonist action rather than a drug-drug interaction). No other drug-drug interactions were found.
- **Thrombosis signal from the literature**: Retrieved papers consistently link cyproterone acetate-containing products, mainly combined with ethinylestradiol, to increased venous thromboembolism risk and prothrombotic changes, with larger effects in factor V Leiden carriers.
- **Migraine-specific concern**: Migraine with aura is a recognised risk factor and contraindication for estrogen-containing hormonal products, so use in migraine may be harmful.
- Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. No trials exist, and the literature offers only loose mechanistic background and safety signals. Because estrogen-containing cyproterone products carry vascular and migraine-related warnings, the risk could outweigh any benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source
- Mechanism of action data (for example from DrugBank)
- Evidence on cyproterone acetate alone (without estrogen) in hormone-related migraine
- A benefit-risk assessment addressing thrombotic and stroke risk in people with migraine, especially with aura

**Other predictions in this run:**
- *Amenorrhea (irregular cycles of hyperandrogenic origin)* is the best supported (L3), with one Phase 4 trial (NCT01103518, 100 participants, status unknown) and older hirsutism and hyperandrogenism studies. It is better viewed as a symptom of an already established use than as a new target.
- *Breast fibrocystic disease* has limited, old evidence (L3) and remains on Hold.
- The thrombosis-related predictions (thrombophilia, antithrombin deficiency type 2, heparin cofactor 2 deficiency, factor 5 excess, Prinzmetal angina) reflect harm or no evidence, and should not be pursued as therapeutic targets.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

