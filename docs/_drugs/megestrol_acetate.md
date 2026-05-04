---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Cancer Cachexia / Hormonal Cancer Therapy to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestational agent with established global use in breast cancer, endometrial cancer, and cancer-related anorexia-cachexia, though it is currently not registered in India.
The TxGNN model predicts it may be effective for **Uterine Corpus Endometrial Carcinoma** with a prediction score of **99.94%**, supported by **3 clinical trials** and a mechanistically well-established rationale as a progesterone receptor agonist that directly opposes estrogen-driven endometrial tumourigenesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; globally approved for palliative treatment of advanced breast carcinoma, advanced endometrial carcinoma, and cancer anorexia-cachexia |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. However, Megestrol acetate is a well-characterized synthetic progestin (progesterone receptor agonist) whose antitumour mechanism in the endometrium is thoroughly documented in international literature. By competitively binding progesterone receptors in uterine epithelium, megestrol acetate opposes estrogen-driven cell proliferation, induces differentiation of neoplastic endometrial cells, and suppresses tumour growth — particularly in PR-positive, Grade 1–2 endometrioid-type carcinoma where receptor expression is highest (>70%).

Uterine corpus endometrial carcinoma is the most common gynaecological malignancy in developed countries, and in its early stages it is strongly estrogen-dependent. This makes progestational therapy a biologically rational intervention. The mechanistic link between progesterone receptor agonism and endometrial cancer suppression is one of the most established in gynaecologic oncology, and megestrol acetate has been a cornerstone of fertility-sparing treatment protocols for young women with Stage IA, Grade 1 disease for decades.

The TxGNN score of 99.94% is fully consistent with this mechanistic plausibility. The evidence package further reinforces this with a completed Phase 2 randomised trial directly incorporating megestrol acetate in endometrial carcinoma (NCT00729586), underscoring that this prediction reflects a real clinical use case rather than purely model speculation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomised Phase 2 trial comparing temsirolimus (mTOR inhibitor) alone versus megestrol acetate + tamoxifen + temsirolimus in advanced, persistent, or recurrent endometrial carcinoma; completed 2017; represents the highest-quality direct evidence in this pack |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Randomised Phase 2 comparing continuous versus sequential megestrol in endometrial intraepithelial neoplasia (EIN) / atypical endometrial hyperplasia in patients desiring uterine preservation; terminated early due to recruitment difficulty with only 9 participants enrolled; provides design rationale but no efficacy conclusions |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor combined with progesterone versus progesterone alone in early-stage endometrial cancer (fertility-sparing); uses progesterone rather than megestrol acetate directly; indirectly supports the broader progestin-in-endometrial-cancer concept |

---

## Literature Evidence

Currently no related literature is available for uterine corpus endometrial carcinoma in this Evidence Pack.

---

## India Market Information

Megestrol acetate is currently not registered or marketed in India. No authorisation records are available for this drug under CDSCO.

---

## Cytotoxicity

Megestrol acetate is classified as an antineoplastic hormonal agent with established use in gynaecological and breast cancers.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal therapy — Progestin class (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (progestins do not cause significant bone marrow suppression) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood glucose (high-dose megestrol exhibits glucocorticoid-like activity and can elevate glucose significantly), body weight and oedema, signs of adrenal suppression with prolonged high-dose use (≥160 mg/day), haemostatic parameters (increased thromboembolism risk at high doses) |
| Handling Protection | Standard pharmaceutical handling; dedicated cytotoxic drug handling protocols generally not required for oral progestins |

---

## Safety Considerations

**Drug Interactions (134 interactions identified; selected key examples below):**

The most clinically prominent interaction pattern involves widespread moderate-level interactions with virtually all major antidiabetic drug classes, reflecting megestrol acetate's glucocorticoid-like activity at high doses (≥160 mg/day), which can antagonise glycaemic control:

| Interaction Category | Representative Drugs | Level |
|---------------------|---------------------|-------|
| Insulin analogues | Insulin aspart, Insulin degludec | Moderate |
| GLP-1 receptor agonists | Albiglutide, Dulaglutide, Semaglutide | Moderate |
| DPP-4 inhibitors | Alogliptin, Linagliptin, Saxagliptin, Sitagliptin | Moderate |
| SGLT-2 inhibitors | Canagliflozin, Dapagliflozin, Empagliflozin | Moderate |
| Biguanides | Metformin | Moderate |
| Sulfonylureas | Glimepiride, Chlorpropamide | Moderate |
| Thiazolidinediones | Pioglitazone | Moderate |
| Meglitinides | Repaglinide | Moderate |
| Alpha-glucosidase inhibitors | Acarbose | Moderate |
| Antibiotics / antiemetics | Clarithromycin, Aprepitant | Moderate |

*Clinical implication: High-dose megestrol can induce new-onset hyperglycaemia or worsen existing diabetes. All antidiabetic regimens should be closely monitored and adjusted when co-administering.*

For complete warnings and contraindications, please refer to the package insert, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Megestrol acetate's progesterone receptor agonist mechanism is directly and mechanistically applicable to PR-positive endometrial carcinoma, a completed Phase 2 randomised trial (NCT00729586, n=73) provides clinically meaningful supporting evidence at L2 level, and the drug carries decades of global clinical use for this indication — making the TxGNN prediction both biologically and clinically credible for regulatory consideration in India.

**To proceed, the following is needed:**

- **Regulatory pathway**: Assess CDSCO import licence / New Drug Application requirements for a drug not currently marketed in India
- **Full package insert review**: Obtain and parse TFDA or FDA prescribing information to document complete warnings and contraindications (Data Gap DG001 — currently blocking S1 safety evaluation)
- **MOA documentation**: Retrieve complete DrugBank entry to formalise pharmacological mechanism data (Data Gap DG002)
- **Patient selection criteria**: Define PR/ER receptor testing protocol to identify the target population most likely to benefit (Grade 1–2, PR-positive endometrioid carcinoma; fertility-sparing indication in young patients)
- **Blood glucose monitoring plan**: Establish baseline and on-treatment glycaemic monitoring given high-dose megestrol's glucocorticoid-like activity and its moderate interaction with all major antidiabetic classes
- **Thromboembolism risk protocol**: Define risk stratification and prophylaxis strategy for high-dose use (LMWH consideration in cancer patients with additional VTE risk factors)
- **Comparator benchmarking**: Compare against medroxyprogesterone acetate (MPA), which may be available in India, to determine clinical and market differentiation for endometrial indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

