---
layout: default
title: Pitavastatin
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pitavastatin is a statin (HMG-CoA reductase inhibitor class) generally used for hypercholesterolemia/dyslipidemia; a specific local approved-indication record is not available in this evidence pack.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
but currently only **0 clinical trials** and **2 publications** support this specific direction, and the mechanistic case is weakened by HoFH's near-total loss of LDL receptor function.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (general statin-class use); no local approved-indication record available |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Pitavastatin belongs to the statin (HMG-CoA reductase inhibitor) class; its efficacy in hypercholesterolemia/dyslipidemia is well established, and mechanistically statins act by inhibiting hepatic cholesterol synthesis and upregulating LDL receptor expression.

In Homozygous Familial Hypercholesterolemia, patients have near-complete loss of functional LDL receptors (biallelic LDLR mutations, or equivalent defects such as autosomal recessive hypercholesterolemia via LDLRAP1). Because statins act primarily by increasing LDL receptor activity, their efficacy as monotherapy in HoFH is inherently limited — the mechanism is only partially applicable, working through residual receptor activity or minor non-receptor pathways rather than the primary mechanism used in more common hypercholesterolemia. Standard care for HoFH typically requires combination therapy (e.g., PCSK9 inhibitors, LDL apheresis), consistent with the evidence pack's own assessment that this is a "weakened, indirect mechanistic association."

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT | The Lancet HIV | INTREPID trial: pitavastatin vs. pravastatin in HIV-1-infected adults with dyslipidaemia — pitavastatin effective without CYP450-mediated interactions with antiretrovirals (population is HIV dyslipidaemia, not HoFH specifically) |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Case report | Journal of Clinical Lipidology | Rapid lipid-lowering response in two cases of autosomal recessive hypercholesterolemia (ARH), a condition clinically indistinguishable from HoFH |

## India Market Information

Not currently marketed; no local product registration records are available in this evidence pack.

## Safety Considerations

**Drug Interactions** (86 total interactions identified; key examples):

| Interacting Drug | Severity |
|---|---|
| Erythromycin | Major |
| Eluxadoline, Naltrexone, Metronidazole, Rosuvastatin, Simvastatin, Tinidazole, Ethanol, Cobicistat, Eltrombopag, Chloroquine, Disulfiram, Secnidazole, Benznidazole, Hydroxychloroquine, Zafirlukast, Chloramphenicol, Dapsone | Moderate |
| Warfarin, Dicoumarol | Minor |

No specific key-warning or contraindication data is available for this drug in the current evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for pitavastatin in HoFH is limited to two publications (no HoFH-specific RCTs and no registered clinical trials), and the mechanistic rationale itself is weak — HoFH's near-absent LDL receptor function limits statin monotherapy efficacy, with real-world management relying on combination therapy. The evidence level (L4) does not support proceeding beyond a research hypothesis at this time.

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) data
- HoFH-specific clinical evidence, ideally evaluating pitavastatin as combination/adjunct therapy rather than monotherapy
- Note: within the same evidence pack, the related indication **hyperlipoproteinemia** (rank 2) shows substantially stronger support (Evidence Level L1, 12 clinical trials including Phase 4 RCTs, 17 publications, recommendation "Proceed with Guardrails") and may warrant prioritization over HoFH as the lead repurposing candidate for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

