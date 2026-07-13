---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a third-generation progestin used as a progestin-only contraceptive pill (75 mcg/day), indicated for pregnancy prevention in women of reproductive age.
The TxGNN model predicts it may be effective for **Amenorrhea**,
with **2 clinical trials** and **16 publications** currently supporting this direction — though the mechanistic relationship is complex and paradoxical, warranting caution before advancing to clinical development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (progestin-only oral contraceptive) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Desogestrel in this evidence pack. Based on known pharmacological information, Desogestrel is a third-generation progestin belonging to the gonane family and is classified as a prohormone — it must first be metabolised into its biologically active form (etonogestrel) in the liver. As a progestin-only pill (POP, Cerazette 75 mcg/day), it suppresses the LH surge and inhibits ovulation in approximately 97% of cycles, more consistently than first- and second-generation POPs. Through HPO (hypothalamic-pituitary-ovarian) axis modulation, it alters follicular development, cervical mucus viscosity, and endometrial receptivity without the estrogen component present in combined oral contraceptives.

The mechanistic relationship with amenorrhea is notably **bidirectional and paradoxical** for repurposing purposes. Clinically, 20–30% of Desogestrel POP users develop amenorrhea as a recognised side effect — meaning the drug is well-documented to suppress, not restore, menstruation. The TxGNN model likely identified the HPO axis interaction node shared between Desogestrel's pharmacology and amenorrhea pathophysiology as a knowledge graph connection. However, using Desogestrel to *treat* amenorrhea (e.g., hypothalamic amenorrhea caused by energy deficiency, or primary amenorrhea from ovarian insufficiency) lacks mechanistic justification: these conditions already involve insufficient gonadotropin drive or ovarian reserve, which progestin monotherapy does not address and may exacerbate.

Both identified clinical trials confirm this concern — amenorrhea appears as an **observed outcome or safety measure**, not as a treatment target. The prediction therefore captures a real biological relationship, but in the wrong direction for a therapeutic claim. A narrower sub-indication (e.g., progestin-challenge test for anovulatory oligoamenorrhea, or cyclical withdrawal bleeding in PCOS-associated amenorrhea) might offer a more defensible pathway, but would require substantial evidence development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Investigates fat-mediated modulation of reproductive/endocrine function in young athletes with exercise-induced amenorrhea; compares transdermal vs oral estrogen for bone density restoration. Desogestrel is not the primary intervention — amenorrhea is the patient population criterion, not the treatment target. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | Compares hormonal contraceptive pill vs vaginal ring on androgen secretion, insulin/glucose metabolism, lipid profile, and SHBG in women with PCOS over 59 weeks. Amenorrhea is an observational outcome, not a therapeutic endpoint. Small sample and unknown completion status limit data reliability. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Systematic Review / Meta-analysis | Cochrane Database of Systematic Reviews | Compares 20 µg vs >20 µg estrogen COCs; lower estrogen doses associated with higher rates of amenorrhea and unscheduled bleeding — relevant background on dose-response relationship |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Systematic Review | Cochrane Database of Systematic Reviews | Updated Cochrane review confirming lower-dose estrogen formulations (including Desogestrel-containing pills) produce more irregular bleeding and amenorrhea |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Observational Study | Gynecological Endocrinology | Head-to-head comparison of Drospirenone 4 mg vs Desogestrel 75 mcg on bleeding patterns in women with cardiovascular risk factors; Desogestrel showed poor cycle control with amenorrhea in a significant proportion of users |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstetricia et Gynecologica Scandinavica | Seminal pharmacodynamic evaluation of Desogestrel's androgenicity compared to other progestogens; low androgenic profile documented; discusses PCO-related amenorrhea as comparative context |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Study | Journal of Reproductive Medicine | Evaluates different EE doses on bone mineral density in hypothalamic oligoamenorrhea; provides clinical context for OCP management of amenorrhea subtypes |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative Trial | British Journal of Obstetrics and Gynaecology | RCT comparing Desogestrel 150 µg with 20 µg vs 30 µg EE (Mercilon vs Marvelon); higher amenorrhea and spotting rates with lower estrogen formulation |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstetrical & Gynecological Survey | Overview of three new progestogens (Desogestrel, norgestimate, gestodene); Desogestrel described as a prohormone metabolised to etonogestrel, with lower androgenic activity than earlier-generation agents |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Review | American Journal of Obstetrics and Gynecology | Comprehensive tolerability profile of Desogestrel/EE combination; documents non-contraceptive benefits (dysmenorrhea, endometriosis, PID reduction) and menstrual pattern changes including amenorrhea |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Review | British Medical Bulletin | Reviews COC safety and efficacy in 60 million+ users; discusses clinical management based on dose, potency, and biological activity — relevant safety background |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Study | Georgian Medical News | Examines central genesis of dysfunctional menstrual disorders including oligomenorrhea and amenorrhea in infertile women (n=159); compares pathogenesis-directed management vs standard hormone therapy — provides context for hypothalamic amenorrhea treatment approaches |

---

## India Market Information

Desogestrel is currently **not marketed in India**. No drug registrations were identified in the regulatory database (total licenses = 0). This means there is no existing regulatory approval, pricing precedent, or distribution infrastructure to leverage for a repurposing pathway in the Indian market.

---

## Safety Considerations

**Drug Interactions (43 total interactions documented; representative moderate-level interactions shown below):**

A notable clustering of interactions involves antidiabetic agents, reflecting Desogestrel's known effect on glucose tolerance and insulin sensitivity. All listed interactions are **Moderate** severity (source: DDInter).

| Interacting Drug | Level | Class / Clinical Relevance |
|-----------------|-------|---------------------------|
| Metformin | Moderate | Biguanide; progestins may impair glucose tolerance — monitor glycemic control |
| Insulin aspart, Insulin detemir, Insulin degludec, Insulin glulisine, Insulin lispro (protamine), Insulin human (zinc) | Moderate | Multiple insulin formulations; Desogestrel may reduce insulin sensitivity — dose adjustment may be needed |
| Liraglutide, Albiglutide, Lixisenatide | Moderate | GLP-1 receptor agonists; pharmacodynamic interaction via metabolic/hormonal axis |
| Dapagliflozin, Ertugliflozin | Moderate | SGLT2 inhibitors; monitor for changes in glycemic control during co-administration |
| Alogliptin, Linagliptin | Moderate | DPP-4 inhibitors; antidiabetic efficacy may be altered |
| Nateglinide | Moderate | Meglitinide; glucose-lowering effect may be diminished |
| Rosiglitazone | Moderate | Thiazolidinedione; monitor insulin sensitivity markers |
| Aprepitant | Moderate | NK1 receptor antagonist / CYP3A4 inducer; may reduce Desogestrel plasma concentrations, potentially reducing contraceptive efficacy |
| Glycerol phenylbutyrate | Moderate | Nitrogen scavenger; hormonal interaction pathway |
| Metreleptin | Moderate | Leptin analogue; potential interaction at the metabolic-reproductive hormonal axis |

Please refer to the package insert for complete warnings and contraindications (TFDA prescribing information currently unavailable in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction connecting Desogestrel to amenorrhea reflects a pharmacologically real but therapeutically inverted relationship — clinical data consistently shows Desogestrel *induces* amenorrhea in 20–30% of users as an adverse effect, and neither of the identified clinical trials tests it as a therapy *for* amenorrhea. Combined with zero India market registrations and absent regulatory documentation, there is no viable near-term repurposing pathway for this indication as currently framed.

**To proceed, the following is needed:**
- **Indication refinement**: Clarify whether a specific subtype of amenorrhea is hypothesised to benefit (e.g., progestin challenge-responsive anovulatory amenorrhea in PCOS, or cyclical withdrawal bleeding protocols) rather than amenorrhea as a broad category
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB00304) to support or refute any therapeutic — rather than side-effect — rationale for the amenorrhea linkage
- **Regulatory data gap resolution**: Download and parse the TFDA/CDSCO package insert PDF to obtain warnings, contraindications, and approved indication text (identified as a blocking data gap: DG001)
- **Targeted literature review**: Conduct a focused search on progestin-only pills in the *treatment* of specific amenorrhea subtypes (hypothalamic, PCOS-associated, post-pill) to distinguish from the existing evidence base documenting amenorrhea as a POP side effect
- **Mechanistic plausibility workshop**: If a specific subtype rationale is identified, a scientific advisory panel review is recommended before committing to any prospective study design
- **India regulatory pathway assessment**: Given zero current registrations, a market entry strategy would need to be developed in parallel with any clinical development plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

