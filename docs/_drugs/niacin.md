---
layout: default
title: Niacin
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 1
---

# Niacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Niacin: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Niacin (Vitamin B3) is a long-established lipid-lowering agent, historically used to treat dyslipidemia by reducing VLDL secretion and raising HDL-C levels.
The TxGNN model predicts it may be applicable to **Homozygous Familial Hypercholesterolemia (HoFH)**, with **2 registered clinical trials** (neither directly testing Niacin) and **20 publications** providing contextual support — most of which discuss Niacin as part of broader non-statin lipid-lowering strategies rather than as a primary HoFH intervention.
The mechanistic rationale is plausible but the clinical evidence base for this specific combination is weak, and large cardiovascular outcome trials have not demonstrated additive benefit from Niacin over statin therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyslipidemia / hyperlipidemia (VLDL and LDL cholesterol reduction, HDL raising) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 (observational studies, systematic reviews, narrative reviews; no direct Niacin RCT for HoFH) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Niacin exerts its lipid-lowering effect through a receptor-independent mechanism: it inhibits hepatic Diacylglycerol O-acyltransferase 2 (DGAT2) and suppresses adipose tissue lipolysis, thereby reducing free fatty acid flux to the liver and diminishing VLDL secretion. Because this pathway does not rely on functional LDL receptors, it is mechanistically plausible — at least in theory — that Niacin could offer some LDL-C reduction even in HoFH patients whose LDL receptors are completely non-functional or severely impaired.

HoFH and dyslipidemia share the same biochemical endpoint (elevated LDL-C and VLDL-C), which explains why the TxGNN knowledge graph model identifies an overlap. Historically, Niacin was indeed used as adjunctive therapy in severe hypercholesterolemia before PCSK9 inhibitors and lomitapide became available. Early case series and combination drug regimens from the 1980s–1990s included Niacin alongside bile acid sequestrants and statins for FH patients.

However, the clinical translation is limited. Niacin's LDL-C reduction effect is approximately 10–25%, which falls far short of the 50–80% reduction typically required in HoFH management. More critically, two large placebo-controlled RCTs — AIM-HIGH (2011) and HPS2-THRIVE (2013) — failed to demonstrate incremental cardiovascular benefit when Niacin was added to statin therapy in patients already at low LDL-C. This has substantially reduced clinical enthusiasm for Niacin as a serious lipid-lowering candidate, even in settings of residual hypercholesterolemia. The TxGNN prediction therefore reflects a mechanistic association that does not translate cleanly into clinical utility for HoFH.

---

## Clinical Trial Evidence

> **Note:** Neither trial below directly tests Niacin for HoFH. Both are included because they matched the disease query but evaluate other agents.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in children/adolescents aged 8–17 with HoFH; evaluated LDL-C reduction at 12, 24, and 48 weeks. **Not a Niacin trial.** |
| [NCT03110432](https://clinicaltrials.gov/study/NCT03110432) | N/A (Registry) | Completed | 1,695 | Prospective German registry of very high cardiovascular risk dyslipidemia patients; tracks real-world use of multiple lipid-lowering therapies including PCSK9 inhibitors. **Observational; no Niacin-specific efficacy data.** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Systematic Review | Expert Rev Cardiovasc Ther | Critical review of non-statin therapies for dyslipidemia; explicitly covers niacin as an adjunct option alongside fibrates, ezetimibe, and bile acid sequestrants. Discusses residual risk and statin intolerance contexts. |
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Clinical Practice Statement (AHA) | Arteriosclerosis Thromb Vasc Biol | ATVB Council statement on non-statin LDL-lowering therapy; confirms that niacin monotherapy reduces cardiovascular endpoints in placebo-controlled trials, but notes limited additive benefit on top of statins. |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Comprehensive review of pharmacotherapies beyond statins; positions niacin as an HDL-raising and VLDL-reducing agent with a role in mixed dyslipidemia and severe hypercholesterolemia. |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Detailed review of HoFH diagnosis and treatment landscape; highlights the therapeutic gap and the need for LDL receptor-independent approaches. |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern FH management review; discusses the difficulty of achieving 50% LDL-C reduction in HoFH and the emerging role of PCSK9 inhibitors and lomitapide over older agents like niacin. |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atherosclerosis Suppl | Examines unmet needs in HoFH; apheresis and combination lipid-lowering drugs discussed. Niacin is referenced as a historical adjunct with insufficient standalone efficacy for HoFH. |
| [7040850](https://pubmed.ncbi.nlm.nih.gov/7040850/) | 1982 | Historical Clinical Study | Med Clin North Am | Early clinical guidance on familial hypercholesterolemia drug therapy; includes combined regimens with niacin as a component for severe and homozygous cases. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK Interaction Study | Pharmacotherapy | Characterizes pharmacokinetic interactions of lomitapide (approved for HoFH) with multiple lipid-lowering agents **including niacin**; provides direct pharmacological data relevant to combination use in HoFH. |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Literature Review | Medicina (Kaunas) | Current review of FH diagnostics and treatment options covering LDLR/APOB/PCSK9 mutations, severity stratification, and evolving therapy landscape including newer agents. |
| [3548303](https://pubmed.ncbi.nlm.nih.gov/3548303/) | 1987 | Comparative Study | Am J Cardiol | Compares liver transplantation vs. medication and plasma exchange for HoFH cardiovascular disease; medication arm included multi-drug regimens that historically incorporated niacin. |

---

## India Market Information

Niacin (DB00627) currently has **no registered products** in the Indian market.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | — | — | — |

> Niacin is not currently approved or marketed in India. Any clinical use for HoFH would require a new regulatory filing or compassionate use pathway.

---

## Safety Considerations

**Drug Interactions (178 identified interactions; key moderate-level interactions listed):**

Niacin has a clinically significant pattern of **moderate interactions with antidiabetic agents**. Because Niacin can impair insulin sensitivity and raise blood glucose, co-administration with the following classes requires blood glucose monitoring and possible dose adjustment:

- **SGLT-2 inhibitors**: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin
- **GLP-1 receptor agonists**: Albiglutide, Dulaglutide, Exenatide
- **DPP-4 inhibitors**: Alogliptin
- **Biguanides**: Metformin
- **Sulfonylureas**: Glimepiride, Glipizide, Glyburide, Chlorpropamide, Acetohexamide
- **Insulins**: Insulin human, Insulin aspart, Insulin degludec
- **Alpha-glucosidase inhibitors**: Acarbose

**Minor interaction**: Acetylsalicylic acid (aspirin) — aspirin co-administration may reduce niacin-induced flushing, a common tolerability issue.

> Full prescribing warnings and contraindications are not available from the current data sources. Please refer to the package insert and TFDA/CDSCO label before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a mechanistically coherent link between Niacin's LDL receptor-independent VLDL-lowering mechanism and HoFH, where receptor-based therapies are partially ineffective. However, Niacin's LDL-C reduction potency (10–25%) is substantially below the treatment intensity needed for HoFH, and large cardiovascular outcome RCTs (AIM-HIGH, HPS2-THRIVE) failed to demonstrate incremental benefit over statin therapy — significantly weakening the clinical case for pursuing this indication. The drug is also not marketed in India, and no direct clinical trials testing Niacin specifically in HoFH patients were identified.

**To reconsider this decision, the following is needed:**

- **Direct clinical evidence**: Identify or commission a proof-of-concept study evaluating high-dose niacin as adjunctive therapy in HoFH patients on background statin/lomitapide regimens
- **MOA gap closure**: Obtain full DrugBank mechanistic data to confirm the DGAT2/VLDL pathway contribution specifically in LDL receptor-null phenotypes
- **Safety documentation**: Download and parse the full prescribing information (package insert) to complete the key warnings and contraindications profile (currently blocking safety evaluation — Data Gap DG001)
- **Regulatory pathway assessment**: If proceeding, map a regulatory filing strategy for India, as no existing licenses exist to build upon
- **Comparative positioning**: Evaluate Niacin's realistic adjunctive role versus lomitapide, evinacumab, or LDL apheresis — the current standard of care for HoFH — to determine if any clinical niche exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

