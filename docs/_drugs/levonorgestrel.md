---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levonorgestrel: From Contraception to Acne

## One-Sentence Summary

Levonorgestrel (LNG) is a synthetic progestin widely used as a hormonal contraceptive, available in combined oral contraceptives (COC), intrauterine devices (IUD), and emergency contraception formulations.
The TxGNN model predicts it may be effective for **Acne (Disease)**, with **5 clinical trials** and **20 publications** currently supporting this direction — though the mechanistic relationship is notably complex and bidirectional, requiring careful interpretation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception (no India regulatory records on file) |
| Predicted New Indication | Acne (Disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Levonorgestrel is a 19-nortestosterone-derived synthetic progestin with well-documented **androgenic activity**, classifying it among the more androgenic members of the progestin family (PMID 7825629). It functions primarily as a hormonal contraceptive — either as the progestin component of combined oral contraceptives (COC) paired with ethinylestradiol (EE), or as a standalone progestin in intrauterine devices and subdermal implants. Detailed MOA data is currently unavailable from the regulatory database; the mechanistic picture below is derived from the published literature.

The relationship between LNG and acne is **mechanistically bidirectional**. When used in combination with EE as a COC, the estrogen component raises sex hormone-binding globulin (SHBG), lowers circulating free testosterone, and suppresses sebaceous gland activity — all of which can improve acne. A placebo-controlled RCT (PMID 12196750) demonstrated that a low-dose COC containing 20 µg EE + 100 µg LNG significantly improved biochemical markers of androgenicity and was effective against moderate acne. This is the strongest signal supporting the TxGNN prediction.

However, LNG used **alone** exhibits partial androgen receptor (AR) agonist activity that can stimulate sebaceous glands and elevate free androgens — potentially **worsening** rather than treating acne. Comparative studies consistently show LNG-containing pills are less favorable for dermatological outcomes than COCs formulated with anti-androgenic progestins (e.g., drospirenone, chlormadinone acetate). In short, the beneficial acne signal belongs to the LNG+EE combination, not LNG as a standalone agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Evaluates doxycycline for reducing breakthrough bleeding during continuous LNG-containing COC use; acne is incidental context, not a primary endpoint |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large safety cohort comparing nomegestrol acetate/estradiol vs. LNG-containing COC; primary endpoints are cardiovascular and VTE safety, not acne efficacy |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | LNG intrauterine system for endometrial cancer prevention in obese women; oral progestin-associated acne cited as background rationale, no acne treatment endpoint |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Double-blind RCT of gestrinone subdermal implant for endometriosis-associated pelvic pain; study drug is gestrinone (not LNG), indirect relevance only |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | LNG-IUS (Mirena) vs. megestrol for atypical endometrial hyperplasia; no acne-related endpoints |

> ⚠️ **Important:** No registered trial directly evaluates LNG monotherapy for acne treatment. All acne-relevant signals derive from LNG+EE combination oral contraceptive studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | Placebo-controlled trial: low-dose COC (20 µg EE + 100 µg LNG) significantly improved moderate acne; effect attributed to EE-driven SHBG elevation and androgen suppression |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | Clinical Study | Acta Derm Venereol | LNG+EE OC raised SHBG and reduced free testosterone in female acne patients; pre-treatment androgen abnormalities found in 57% of subjects |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Medicine | LNG classified as a highly androgenic progestin (19-nortestosterone derivative); its androgenic activity is identified as an unfavorable property in acne management |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Comparative Review | Am J Clin Dermatol | EE/chlormadinone acetate superior to EE/LNG for acne, hirsutism, and seborrhea; anti-androgenic progestins preferred for pilosebaceous unit disorders |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | EE/CMA significantly more effective than EE/LNG 0.03/0.15 mg for mild-to-moderate papulopustular facial acne in a controlled comparison |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | Drospirenone-containing COC outperforms LNG-containing COC in reducing acne vulgaris and hirsutism due to antimineralocorticoid and antiandrogenic properties |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | LNG-IUS produces strong antiproliferative effect on endometrium; systemic LNG exposure via IUD is low — limited relevance to systemic acne treatment |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Cohort | Hum Reprod | LNG-IUS improved symptoms of endometriosis; primarily a local progestogenic effect with low systemic androgenic exposure |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Cochrane Review | Cochrane Database Syst Rev | LNG-IUS effective for endometrial hyperplasia treatment; no acne efficacy endpoints reported |
| [11091988](https://pubmed.ncbi.nlm.nih.gov/11091988/) | 2000 | Review | Obstet Gynecol Clin NA | LNG implants prevent pregnancy via ovulation inhibition, cervical mucus changes, and endometrial alteration; androgenic activity of LNG noted as a pharmacological property |

---

## India Market Information

Levonorgestrel currently has **no registered products** in India's drug regulatory database, with zero active licenses on record.

> *Note: This does not reflect global availability. LNG is widely marketed internationally under brand names including Mirena and Kyleena (hormonal IUDs), Plan B / Postinor (emergency contraception), and as the progestin component of numerous combined oral contraceptive formulations.*

---

## Safety Considerations

**Drug Interactions (162 interactions identified; representative moderate-level interactions shown):**

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Insulin aspart, lispro, degludec, isophane, zinc (multiple formulations) | Moderate | LNG may impair insulin sensitivity and compromise glycemic control |
| Canagliflozin, Dapagliflozin, Ertugliflozin (SGLT2 inhibitors) | Moderate | LNG may counteract glucose-lowering effects of SGLT2 inhibitors |
| Exenatide, Liraglutide (GLP-1 agonists) | Moderate | Risk of reduced antidiabetic efficacy |
| Linagliptin, Nateglinide | Moderate | Potential for compromised glycemic management |
| Aprepitant | Moderate | CYP3A4 induction may reduce LNG plasma concentrations |
| Clotrimazole | Moderate | CYP enzyme interaction; potential for altered LNG systemic exposure |
| Acarbose, Glycerol phenylbutyrate | Moderate | LNG's glucocorticoid-like metabolic effects may antagonize antidiabetic agents |

> ⚠️ The high concentration of interactions with antidiabetic drug classes reflects LNG's known effect on **glucose metabolism and insulin resistance** — a clinically important consideration in patients with diabetes or metabolic syndrome.

Please refer to the package insert for full warnings and contraindications (currently unavailable for India; data gap DG001 pending resolution).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical evidence for LNG in acne derives **entirely from LNG+EE combination oral contraceptives**, not from LNG monotherapy. LNG's intrinsic androgenic (AR partial agonist) activity means that, without an estrogenic counterpart to raise SHBG, LNG may actively **worsen** acne — making it fundamentally unsuitable as a standalone acne therapy. Comparative head-to-head data consistently rank LNG-containing regimens below anti-androgenic progestins for dermatological indications.

**To proceed, the following is needed:**
- **Formulation strategy clarification:** Determine whether the intended target is the LNG+EE combination (not LNG monotherapy); this changes the regulatory and clinical development pathway entirely
- **MOA data retrieval:** Complete DrugBank API query to formally document mechanism of action (Data Gap DG002)
- **Safety package completion:** Retrieve full TFDA/CDSCO package insert for warnings and contraindications (Data Gap DG001, Blocking severity)
- **Preclinical clarification:** Obtain data on LNG's net effect on sebaceous gland activity in the absence of exogenous estrogen, to resolve the bidirectionality concern
- **Comparative efficacy design:** If the combination indication is pursued, plan head-to-head trials against anti-androgenic COCs (drospirenone-EE, CMA-EE) to demonstrate non-inferiority or superiority
- **India regulatory pathway:** With zero existing registrations, any new indication would require a full new drug application to CDSCO
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

