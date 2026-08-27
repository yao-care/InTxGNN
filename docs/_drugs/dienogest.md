---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest (Visanne®) is a fourth-generation progestin approved and widely used internationally for the treatment of endometriosis, where it suppresses endometrial tissue growth through hypoestrogenic and anti-inflammatory mechanisms.
The TxGNN model predicts it may be applicable to **Amenorrhea**, with **4 clinical trials** and **6 publications** currently available — though the majority relate to endometriosis contexts where amenorrhea emerges as a pharmacological effect rather than a primary treatment target.
This distinction critically limits the repurposing value, and the overall evidence requires careful interpretation before any clinical development decision can be made.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis (based on clinical trial and literature context; no approved indication listed in India regulatory data) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dienogest is a fourth-generation progestin with high selectivity for progesterone receptors and minimal androgenic activity. Its primary mechanism in endometriosis involves suppressing ovarian estradiol production (creating a hypoestrogenic environment), inhibiting endometrial cell proliferation, promoting apoptosis of ectopic endometrial tissue, and reducing local inflammation via downregulation of inflammatory cytokines. It does not bind significantly to androgen, glucocorticoid, or mineralocorticoid receptors, giving it a relatively clean pharmacological profile.

The mechanistic connection between dienogest and amenorrhea is real but directionally reversed from a classic repurposing scenario: dienogest does not *treat* amenorrhea — it *induces* it as a pharmacological effect. In 60–80% of women treated with dienogest for endometriosis, menstruation is suppressed (drug-induced amenorrhea). This effect is intentional and considered therapeutically desirable in endometriosis management, as it reduces retrograde menstruation and lesion stimulation.

Where limited biological plausibility exists for repurposing is in *secondary amenorrhea* — specifically cases arising from PCOS or endometriosis-related hormonal dysregulation, where cyclic progestin therapy can help reset uterine bleeding patterns. However, this is a very different clinical scenario from primary amenorrhea, which has distinct anatomical or genetic etiologies that progestins cannot address. The TxGNN model's high score likely reflects topological proximity in the knowledge graph between "progestins" and "amenorrhea" nodes, rather than a direct therapeutic relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Non-inferiority RCT comparing Indinol Forto® 200 mg vs. Visanne® (dienogest 2 mg) in endometriosis; menstrual suppression likely a secondary endpoint |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Compares transdermal estradiol + dienogest vs. estradiol + drospirenone in endometriosis; evaluates patient satisfaction with estradiol add-back regimens |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completed | 968 | Real-world observational study of Visanne® in endometriosis; amenorrhea captured as a safety/efficacy outcome, not the primary endpoint |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completed | 895 | Prospective observational cohort in Asian women with endometriosis; focuses on quality of life and long-term safety; menstrual suppression is a secondary observation |

> **Note:** None of the identified trials study amenorrhea as a primary treatment target. Amenorrhea appears as a pharmacological effect or safety observation within endometriosis trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review + Bayesian Analysis | BMC Pharmacology & Toxicology | Comprehensive analysis of adverse events associated with dienogest; amenorrhea identified as a frequent, mechanism-driven effect during treatment of endometriosis and adenomyosis |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical Pharmacology Study | European Journal of Contraception & Reproductive Health Care | Confirms dienogest's high inhibition ratio and transformation index; its pharmacological properties deliberately induce amenorrhea as part of endometriosis management |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Reviews hormonal treatment landscape for endometriosis; estrogen-dependency and progesterone-resistance are key pathogenic drivers; progestins including dienogest are first-line options |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospective Clinical Study | Reproductive Sciences | Retrospective cohort (n=514) assessing long-term efficacy and safety of dienogest beyond 12 months in ovarian endometrioma; amenorrhea rates documented as a treatment effect |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Clinical Report | Journal of Pediatric and Adolescent Gynecology | Case series on obstructive Müllerian anomalies using 3D/VR imaging; dienogest used for medical management during diagnostic workup; marginal relevance to amenorrhea repurposing |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | Case of ovarian granulosa cell tumor in PCOS context; PCOS-related secondary amenorrhea provides indirect contextual link; low direct evidence value |

---

## India Market Information

Dienogest is currently **not approved or marketed in India**. No drug licenses, registrations, or approved indications are on record in the CDSCO database for this compound.

> This represents a significant regulatory gap. Any repurposing effort would require a de novo regulatory submission in India, including clinical data from the target indication.

---

## Safety Considerations

**Drug Interactions (37 interactions identified via DDInter):**

*Major interactions (exercise caution; consider alternatives):*

| Interacting Drug | Level | Clinical Concern |
|---------|------|------|
| Sugammadex | Major | Possible reduced effectiveness of hormonal agents (steroidal reversal competition) |
| Griseofulvin | Major | CYP induction may accelerate dienogest metabolism, reducing efficacy |
| Bexarotene | Major | Hormonal contraceptive/progestin efficacy may be compromised |
| Brigatinib | Major | CYP3A4 induction risk; progestin exposure may be reduced |
| Dabrafenib | Major | CYP3A4 induction; may decrease dienogest plasma levels |
| Encorafenib | Major | CYP-mediated interaction; hormonal drug efficacy may be affected |

*Selected moderate interactions:*

| Interacting Drug | Level |
|---------|------|
| Adalimumab | Moderate |
| Anakinra | Moderate |
| Canakinumab | Moderate |
| Certolizumab pegol | Moderate |
| Cladribine | Moderate |
| Linaclotide | Moderate |
| Miltefosine | Moderate |
| Metreleptin | Moderate |

*Minor interactions:*
- Ethanol (minor; monitoring advised)

Please refer to the full package insert for complete safety information, including pregnancy contraindication (Category X), venous thromboembolism risk, and hepatic function requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction that dienogest could be used for amenorrhea reflects a pharmacological reality — dienogest reliably induces amenorrhea — but this is a drug-induced *effect*, not a treatment of the underlying condition. For primary amenorrhea (structural/genetic causes), dienogest has no mechanistic basis. For secondary amenorrhea from PCOS or endometriosis, progestin therapy has some clinical logic, but dienogest's strong ovarian-suppressive profile may be inappropriate. Additionally, dienogest is not marketed in India (0 registrations), and key safety data (package insert warnings, contraindications) are unavailable for this evaluation.

**To proceed, the following is needed:**

- **Clarify the amenorrhea subtype:** Distinguish primary vs. secondary amenorrhea; the latter (PCOS-related or endometriosis-related) carries more biological plausibility for progestin intervention
- **Retrieve the full package insert** from the EMA/MHRA (Visanne® is approved in Europe) to complete the mandatory safety assessment, including warnings, contraindications, and pregnancy category
- **Confirm MOA data from DrugBank** (DB09123) to strengthen the mechanistic analysis
- **Conduct a dedicated literature search** specifically for "progestin" + "secondary amenorrhea" + "PCOS" to identify any direct evidence base, separate from the endometriosis literature retrieved here
- **Assess regulatory pathway in India:** Since the drug has no CDSCO registration, a regulatory strategy review is essential before any clinical program can be designed
- **Evaluate benefit-risk for the secondary amenorrhea niche:** If the target population is defined as PCOS-related or endometriosis-related secondary amenorrhea, a small proof-of-concept study with amenorrhea restoration (not induction) as the primary endpoint would be the minimum needed to move this to L2 evidence

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

