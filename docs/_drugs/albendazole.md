---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Albendazole
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

# Albendazole: From Intestinal Helminthiasis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole antiparasitic agent, originally established as the WHO first-line treatment for intestinal helminthiasis and soil-transmitted helminth infections.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis**,
with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Intestinal helminthiasis (soil-transmitted helminth infections) |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed (0 registrations in dataset) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on known pharmacological information, Albendazole is a benzimidazole compound whose active metabolite — **albendazole sulfoxide** — selectively binds to parasite β-tubulin with approximately 1,000-fold greater affinity than mammalian tubulin, inhibiting microtubule polymerization and disrupting cyst wall cytoskeletal integrity. It simultaneously blocks parasite glucose uptake via GLUT inhibition, exploiting a critical vulnerability: *Echinococcus multilocularis* larvae cannot perform gluconeogenesis and rely entirely on external glucose, leading to ATP depletion and eventual parasite death or stasis. Albendazole sulfoxide penetrates the metacestode cyst wall to achieve therapeutic concentrations at the target site.

Alveolar echinococcosis (AE) is a severe, potentially fatal zoonosis caused by the larval stage of *Echinococcus multilocularis*, a cestode tapeworm. The same β-tubulin inhibition pathway that governs albendazole's efficacy in intestinal helminthiasis applies directly to cestode larval stages — the key difference is that in AE the drug acts **parasitostatic** rather than parasiticidal, halting disease progression rather than eliminating the parasite outright. This means long-term or lifelong treatment is often required, particularly when surgical resection is not feasible (approximately 60–70% of cases).

The WHO-IWGE Expert Consensus (PMID 19931502) formally lists albendazole as the first-line continuous pharmaceutical treatment for AE, supported by a Phase 2 trial with 194 patients (NCT07182305), multiple observational cohort studies, and an extensive review literature. The 99.97% TxGNN prediction score reflects genuine clinical and biological evidence rather than a network artefact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Direct AE Phase 2 trial in Kyrgyzstan (2017–2023); the largest prospective trial to date evaluating albendazole as parasitostatic treatment for early-stage alveolar echinococcosis caused by *E. multilocularis*. High relevance (Grade A). |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completed | 50 | EchinoVISTA prospective study (2012–2021); defines improved management of hepatic AE patients on albendazole by identifying biological and imaging markers of parasite viability to guide treatment withdrawal decisions. Observational design (Grade B). |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Unknown | 24 | Randomised controlled trial evaluating adjuvant albendazole after pulmonary hydatid cyst (cystic echinococcosis, CE) resection vs placebo for 6-month recurrence reduction. Targets CE rather than AE; small sample size (Grade B). |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | NA | Recruiting | 43 | Evaluation of a multiplex quantitative PCR technique for echinococcosis diagnosis; albendazole referenced as the treatment backbone. Diagnostic study without direct efficacy assessment (Grade C). |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Case report of a misdiagnosed primary intramuscular hydatid cyst treated with albendazole; narrative reference only, no statistical power (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Consensus Guideline | *Acta Tropica* | WHO-IWGE expert consensus on diagnosis and treatment of cystic and alveolar echinococcosis; recommends albendazole as the first-line pharmacological agent for AE |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Comprehensive Review | *Clinical Microbiology Reviews* | Major 21st-century advances in echinococcosis covering genetics, molecular epidemiology, diagnostic tools, and treatment; confirms albendazole central role |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | *Parasite (Paris)* | Current status of benzimidazole chemotherapy for AE; characterises parasitostatic limitations, liver toxicity risks, and the urgent need for alternative agents |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Clinical Review | *World Journal of Gastroenterology* | Management of liver echinococcosis; albendazole positioned as essential perioperative and long-term adjunct to surgical treatment |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | *Parasite (Paris)* | Novel therapeutic options for AE and CE beyond albendazole/mebendazole; large-scale drug screening strategies and albendazole as the reference comparator |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | *Chinese Journal of Schistosomiasis Control* | Progress of albendazole research specifically for AE treatment; reviews evidence for parasitostatic effects and recent clinical studies |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacology Study | *Antimicrobial Agents and Chemotherapy* | Metabolic mechanism and pharmacological study of albendazole in a secondary hepatic AE rat model; evaluates enhanced-solubility formulations (ABZ-CSD, TABZ-HCl-H) to overcome poor oral bioavailability |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | *Acta Tropica* | Status and prospects of novel treatments for AE and CE; confirms albendazole and mebendazole remain the only two licensed non-surgical treatment options globally |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Clinical Review | *Seminars in Liver Disease* | Hepatic alveolar echinococcosis review; documents the pseudotumoral presentation and role of lifelong albendazole in non-resectable cases |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | *Tidsskrift for den Norske laegeforening* | Current clinical overview of AE in a non-endemic European setting; highlights prolonged albendazole therapy as standard management combined with surgery |

---

## India Market Information

No registrations for Albendazole were found in this dataset for the Indian market (CDSCO). This likely reflects a data collection gap rather than the actual availability of the drug: Albendazole is included in the WHO Model List of Essential Medicines and is widely used in global mass drug administration programmes.

> **Note:** It is strongly recommended to verify current CDSCO approval status directly via the Indian drug regulatory authority database before proceeding with any clinical or procurement activities.

---

## Safety Considerations

**Drug Interactions:** Albendazole has 96 documented interactions in the DDInter database. Key interactions to monitor:

| Interacting Drug | Level | Potential Clinical Impact |
|----------------|-------|--------------------------|
| Aprepitant | Moderate | CYP3A4/CYP2C19 modulation may alter albendazole sulfoxide plasma exposure |
| Cobicistat | Moderate | CYP enzyme inhibition may increase active metabolite levels |
| Apalutamide | Moderate | CYP3A4 induction may reduce albendazole efficacy |
| Bosentan | Moderate | Potential additive hepatotoxicity risk |
| Boceprevir | Moderate | CYP3A4 inhibition may elevate albendazole metabolite concentrations |
| Bendamustine | Moderate | Possible additive hepatotoxic effects |
| Fostamatinib | Moderate | Pharmacokinetic interaction via CYP pathways |
| Deferasirox | Moderate | Potential drug-drug interaction affecting systemic exposure |
| Dexamethasone | Minor | May increase albendazole sulfoxide levels — notably relevant in AE treatment protocols where corticosteroids are co-administered |
| Cimetidine | Minor | May increase albendazole plasma concentrations via CYP inhibition |

> Please refer to the package insert for complete safety information including key warnings and contraindications, as TFDA/CDSCO prescribing information was not available in this data pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is supported by WHO expert consensus guidelines and a completed Phase 2 prospective trial with 194 patients (NCT07182305) as the primary pharmacological treatment for alveolar echinococcosis — making this prediction a genuine clinical application rather than speculative repurposing. The biological mechanism is well-characterised, the drug is already used off-label for AE in multiple countries, and the evidence base is substantial enough to justify continued development under a structured oversight framework.

**To proceed, the following is needed:**

- **Regulatory data (Blocking):** Obtain CDSCO prescribing information to assess key warnings and contraindications (Data Gap DG001 — currently blocking Safety Stage 1 evaluation)
- **Mechanism documentation:** Retrieve formal MOA data from DrugBank API to complete mechanistic link analysis (Data Gap DG002)
- **India regulatory pathway:** Verify current CDSCO registration status; determine whether import authorization, named-patient supply, or new registration is required given 0 licenses found in dataset
- **Long-term monitoring protocol:** Establish hepatotoxicity monitoring plan (ALT/AST, bilirubin, alkaline phosphatase at baseline and every 4–8 weeks) given documented risk of liver dysfunction during prolonged albendazole therapy
- **Formulation optimization assessment:** Evaluate enhanced bioavailability formulations (e.g., albendazole crystal dispersion systems) given known poor and erratic oral absorption due to low aqueous solubility — this is particularly critical for achieving therapeutic concentrations within echinococcal cysts
- **Surgical candidacy criteria:** Define patient selection criteria distinguishing resectable from non-resectable AE to position albendazole correctly as definitive therapy vs. perioperative adjunct

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Results generated by the TxGNN model are computational predictions and must be interpreted in conjunction with clinical expertise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

