---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol: From Gastric Ulcer Prevention & Medical Abortion to Amenorrhea

## One-Sentence Summary

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue well-established in clinical practice for NSAID-induced gastric ulcer prevention and obstetric/gynaecological applications including medical abortion and labour induction.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **0 registered clinical trials** and **7 publications** currently available — though none of the publications directly investigate amenorrhea as a primary therapeutic endpoint for Misoprostol.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastric ulcer prevention (NSAID-induced); obstetric/gynaecological use (medical abortion, labour induction) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacology, Misoprostol is a synthetic prostaglandin E1 analogue that activates EP2/EP3 receptors on uterine smooth muscle, producing a potent uterotonic effect — i.e., stimulating uterine contractions. This is the same mechanism exploited in medical abortion and labour induction protocols.

There is theoretical plausibility linking this mechanism to amenorrhea treatment. Secondary amenorrhea caused by intrauterine adhesions (Asherman's syndrome) or other structural uterine factors could theoretically benefit from Misoprostol's uterotonic and endometrial-stimulating properties — for example, by facilitating menstrual outflow or promoting endometrial regeneration following adhesiolysis. Misoprostol has been explored in this context post-hysteroscopic surgery to prevent re-adhesion and support endometrial recovery.

However, a critical limitation must be stated clearly: in all 7 identified publications, "amenorrhea" functions exclusively as a proxy for gestational age (e.g., "amenorrhea ≤35 days" to define ultra-early pregnancy) or appears as a presenting symptom in an unrelated case report — not as the condition being treated. No study in this dataset investigates Misoprostol as a therapeutic agent for amenorrhea. The mechanistic hypothesis is plausible, but clinical evidence is entirely absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | Dose-Ranging RCT | Reproductive Sciences | Dose-ranging study of mifepristone + misoprostol for ultra-early pregnancy termination (amenorrhea ≤35 days used as gestational age proxy, not treatment target). Complete abortion as primary endpoint. |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | Hospital vs. self-administered mifepristone + misoprostol for ultra-early medical abortion (n=744). Amenorrhea ≤35 days defines inclusion criterion only; not an outcome being treated. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Prospective Interventional Study | Human Reproduction | Feasibility of mifepristone + misoprostol administered before expected menstruation for unintended pregnancy prevention. Menstrual restoration is the pharmacological mechanism, not amenorrhea treatment. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Prospective Clinical Study | J Obstet Gynaecol Research | Safety and efficacy of low-dose mifepristone combined with self-administered misoprostol for early pregnancy termination. No amenorrhea-specific analysis. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Clinical Practice Guideline / Systematic Review | J Obstet Gynaecol Canada | Reviews endometrial ablation for abnormal uterine bleeding; post-ablation amenorrhea appears as a treatment outcome measure. Misoprostol is not featured as a primary intervention. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Prospective Clinical Study | BMJ | Early prospective study of misoprostol for medical management of missed abortion and anembryonic pregnancy. Foundational evidence for uterotonic use. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Case report of acute fatty liver of pregnancy (35-week gestation). Amenorrhea listed as a presenting symptom alongside nausea and fever; Misoprostol not mentioned as an intervention. |

---

## Safety Considerations

**Drug Interactions** (196 interactions identified in database; key examples listed below):

| Interacting Drug | Severity | Clinical Relevance |
|----------------|---------|-------------------|
| Dinoprostone (topical) | **Major** | Additive uterotonic effect — risk of uterine hyperstimulation and potential uterine rupture |
| Magnesium oxide | Moderate | Pharmacodynamic interaction; monitor |
| Magaldrate | Moderate | Pharmacodynamic interaction; monitor |
| Magnesium carbonate | Moderate | Pharmacodynamic interaction; monitor |
| Magnesium hydroxide | Moderate | Pharmacodynamic interaction; monitor |
| Quinapril | Moderate | ACE inhibitor — monitor blood pressure |
| Sodium citrate | Minor | Low clinical significance |
| Aluminum hydroxide | Minor | Low clinical significance |
| Calcium carbonate | Minor | Low clinical significance |
| Sodium bicarbonate | Minor | Low clinical significance |
| Naproxen | Minor | Low clinical significance |

Please refer to the package insert for complete warnings and contraindications, which could not be retrieved in this data pull (DG001: Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence sits at L4 (mechanistic plausibility only, no direct clinical studies). The 7 identified publications do not address amenorrhea as a therapeutic target — amenorrhea appears solely as a gestational age proxy or incidental symptom descriptor. No registered clinical trials exist for this indication, and the drug is not marketed in India.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve TFDA/CDSCO package insert to extract key warnings, contraindications, and approved label — required before any safety-based decision can be made
- **Resolve DG002 (High):** Obtain full MOA data from DrugBank to complete the mechanistic link analysis between PGE1 receptor activation and amenorrhea pathophysiology
- **Targeted literature search:** Commission a dedicated search for Misoprostol (or PGE1 analogues broadly) specifically in secondary amenorrhea, intrauterine adhesions (Asherman's syndrome), and post-ablation amenorrhea contexts
- **Mechanistic hypothesis refinement:** Clarify whether the intended use case is (a) promoting menstrual onset in hormone-primed endometrium, (b) post-surgical adhesion prevention, or (c) another specific amenorrhea subtype — each has a different evidence pathway
- **Expert consultation:** Engage a reproductive endocrinologist to assess clinical feasibility before investing in prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

