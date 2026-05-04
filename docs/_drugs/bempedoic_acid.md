---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor approved in the US and EU for lowering LDL-cholesterol in adults with hypercholesterolemia or mixed dyslipidemia.
Among the 10 TxGNN-predicted new indications evaluated, **Homozygous Familial Hypercholesterolemia (HoFH)** emerges as the most actionable candidate—it sits within the same lipid-lowering pathway as the drug's established indication and is the only prediction with real clinical evidence.
**17 publications** support this direction, including a **2026 real-world retrospective cohort** specifically evaluating bempedoic acid in HoFH patients.

> **Note on prediction selection**: TxGNN's highest-scored prediction (hyperthyroidism, score 99.61%) lacks any established mechanistic link to ACL inhibition and has only one tangentially related publication. Several other top predictions (e.g., infectious bovine rhinotracheitis, malignant catarrh) refer to veterinary diseases with no human relevance. HoFH (TxGNN score 99.48%) is selected as the primary focus of this report because it is the only prediction with substantive human clinical evidence (L3) and a coherent pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / LDL-C reduction (not registered in India) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (global rank 8,682) |
| Evidence Level | L3 – Observational study + multiple systematic reviews |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bempedoic acid is a liver-targeted prodrug. After oral absorption, it is activated exclusively in hepatocytes by the enzyme very-long-chain acyl-CoA synthetase-1 (ACSVL1) into its active form, ETC-1002-CoA. This active metabolite inhibits ATP-citrate lyase (ACL), an enzyme that sits one step upstream of HMG-CoA reductase in the cholesterol biosynthesis pathway. By blocking ACL, bempedoic acid reduces the liver's internal cholesterol production, which triggers a compensatory upregulation of LDL receptor (LDLR) expression on hepatocyte surfaces—leading to increased removal of LDL particles from the bloodstream.

HoFH is caused by biallelic mutations in the LDLR gene, resulting in severely impaired or essentially absent LDL receptor function. This presents an important mechanistic caveat: because bempedoic acid's LDL-lowering effect partly depends on functional LDLR to clear circulating LDL-C, the benefit in HoFH patients with complete receptor loss will be attenuated. However, in patients with residual LDLR activity—particularly in compound heterozygotes rather than true null-null genotypes—meaningful LDL-C reduction remains plausible. Additionally, when bempedoic acid is added to LDLR-independent agents such as evinacumab (an ANGPTL3 inhibitor) or lomitapide (an MTP inhibitor), it may contribute a complementary reduction on top of an already aggressive regimen.

This prediction is best understood as a pharmacologically logical label extension along the familial hypercholesterolemia spectrum. Bempedoic acid already holds approval for heterozygous FH (HeFH)—the same disease at a less severe degree. HoFH sits at the extreme end of that same LDL-pathway disorder. A 2026 real-world study (Warden & Duell, PMID 41274797) published in the *Journal of Clinical Lipidology* directly evaluated bempedoic acid use in HoFH patients, confirming that clinical practice is already exploring this extension ahead of formal regulatory approval.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for bempedoic acid specifically in homozygous familial hypercholesterolemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-world retrospective cohort | Journal of Clinical Lipidology | Direct evaluation of bempedoic acid efficacy and tolerability in HoFH patients; the only study focused specifically on this population |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Clinical consensus | Journal of Clinical Lipidology | National Lipid Association expert consensus on FH; addresses HoFH management including adjunct role of bempedoic acid |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Experimental and Molecular Pathology | Comprehensive review of novel therapies for HoFH, including ACL inhibition; discusses LDL-receptor–independent mechanisms |
| [39070027](https://pubmed.ncbi.nlm.nih.gov/39070027/) | 2024 | Review | American Journal of Preventive Cardiology | LDL-C targeting beyond PCSK9 inhibitors; positions bempedoic acid within the broader lipid-lowering landscape |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | American Journal of Preventive Cardiology | Cumulative lifetime LDL-C exposure and ASCVD prevention; emphasises early, aggressive LDL lowering relevant to HoFH |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Drug review / approval | Cardiology in Review | Evinacumab approval review for HoFH; contextualises bempedoic acid as a potential add-on therapy in combination regimens |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Non-statin lipid-lowering drugs including bempedoic acid; directly relevant to India clinical practice context |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | Journal of Atherosclerosis and Thrombosis | Advances in HoFH treatment; discusses bempedoic acid as adjunct alongside lomitapide, evinacumab, and LDL apheresis |
| [35754818](https://pubmed.ncbi.nlm.nih.gov/35754818/) | 2022 | Review | Frontiers in Genetics | Refractory hypercholesterolemia and emerging gene therapies; bempedoic acid discussed as a bridging/combination agent |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical (animal model) | Arteriosclerosis, Thrombosis, and Vascular Biology | Bempedoic acid significantly lowered LDL-C and reduced atherosclerotic burden in LDLR-deficient Yucatan miniature pigs—a direct large-animal model of HoFH |

---

## India Market Information

Bempedoic acid is not currently registered in India. No CDSCO-approved products are on record. This means that any development pathway toward HoFH would first require establishing the base hypercholesterolemia/HeFH indication in India before pursuing a label extension to HoFH.

---

## Safety Considerations

Detailed safety data from the Indian package insert were not available in this Evidence Pack.

**Pregnancy safety concern**: Bempedoic acid has demonstrated fetal toxicity in animal reproductive studies and is contraindicated during pregnancy. This is a critical consideration that immediately eliminates the separately TxGNN-predicted indication of "pregnancy-associated osteoporosis" (TxGNN rank 10) from further evaluation—not only does the prediction lack mechanistic support, but it carries an absolute safety contraindication.

Please refer to the approved prescribing information (US/EU labels are publicly available) for complete warnings, contraindications, and drug interaction data pending full India package insert retrieval.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
HoFH shares the same lipid metabolic pathway as bempedoic acid's established indication, making this a scientifically coherent label extension. A 2026 real-world cohort provides the first direct clinical evidence in HoFH patients, and multiple expert reviews already position bempedoic acid within HoFH combination regimens. The key pharmacological limitation—LDLR dependency—is real but does not eliminate all patient subgroups from potential benefit.

**To proceed, the following is needed:**

- **Retrieve full MOA and safety data**: Query DrugBank API for complete mechanistic details; download the CDSCO/FDA package insert to fill the safety data gap (currently blocking S1 evaluation)
- **India regulatory pathway**: Bempedoic acid has zero registrations in India; establishing a base hypercholesterolemia indication with CDSCO is a prerequisite before any HoFH label extension can be pursued
- **Patient subgroup definition**: Prioritise HoFH patients with residual LDLR activity (compound heterozygotes, missense mutations) over complete null-null genotypes, where the pharmacological rationale is strongest
- **Evidence upgrade**: No clinical trials exist; a prospective registry study or Phase 2 pilot in Indian HoFH patients would significantly strengthen the evidence base (India's consanguineous population structure may produce a higher-than-average HoFH prevalence in certain communities)
- **Combination strategy design**: Evaluate bempedoic acid as add-on to LDLR-independent agents (evinacumab, lomitapide) rather than as monotherapy in HoFH
- **Uric acid monitoring**: Bempedoic acid is known to raise serum urate; gout risk monitoring should be incorporated into any HoFH treatment protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

