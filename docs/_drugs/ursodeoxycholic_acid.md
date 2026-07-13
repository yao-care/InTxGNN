---
layout: default
title: Ursodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: From Cholestatic Liver Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a naturally occurring bile acid used primarily in the treatment of cholestatic liver diseases such as primary biliary cholangitis and gallstone dissolution.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
however this prediction is currently supported by **0 clinical trials** and **0 publications**, representing model-only evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (no registered licenses) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data sources queried. Based on known pharmacology, UDCA is a hydrophilic bile acid that modulates bile acid pool composition, hepatoprotection, and cholesterol homeostasis. Its indirect effects on cholesterol metabolism are mechanistically plausible as a starting point for the model's inference.

The predicted link to homozygous familial hypercholesterolemia (HoFH) likely arises from UDCA's multi-pronged influence on cholesterol pathways: it replaces toxic hydrophobic bile acids in the bile acid pool, inhibits HMG-CoA reductase to reduce hepatic cholesterol synthesis, activates the nuclear receptor FXR to upregulate the cholesterol transporters ABCG5/ABCG8 (increasing biliary cholesterol excretion), and reduces intestinal cholesterol absorption. These mechanisms collectively lower systemic cholesterol load.

However, the biological rationale for HoFH specifically is weak. HoFH is defined by biallelic loss-of-function mutations in the LDL receptor (LDLR), rendering the hepatic LDL-receptor clearance pathway non-functional. As a result, plasma LDL-C typically reaches 500–1,000 mg/dL—a severity that UDCA's incremental cholesterol-lowering effects cannot meaningfully address. The TxGNN high score most likely reflects topological overlap of cholesterol metabolism nodes within the knowledge graph rather than disease-specific therapeutic potential. This mismatch between mechanism magnitude and disease severity warrants caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Ursodeoxycholic acid is currently **not marketed in India** under any registered license. No authorization records are available in the India regulatory database.

---

## Safety Considerations

**Drug Interactions (272 total interactions identified):**

Notable interactions from available data:

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|------------------|---------------|
| Cyclosporine | Minor | Possible minor pharmacokinetic interaction |
| Aluminum hydroxide | Minor | Antacids may reduce UDCA absorption; separate dosing recommended |
| Magaldrate | Minor | Similar to aluminum hydroxide — may impair UDCA absorption |
| Pravastatin | Unknown | Interaction profile unclear; monitor if co-administered |
| Fluconazole | Unknown | Interaction profile unclear |
| Erythromycin | Unknown | Interaction profile unclear |
| Nelfinavir | Unknown | Interaction profile unclear |
| Indinavir | Unknown | Interaction profile unclear |

A total of 272 drug interactions have been identified in the DDI database. The majority (269) are classified as "Unknown" severity, indicating that interaction profiles have not been fully characterised. Please consult the package insert and a current drug interaction database for comprehensive review before initiating combination therapy.

Please refer to the package insert for full warnings and contraindication information, as those data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.86%), there is zero clinical or published evidence supporting the use of UDCA in homozygous familial hypercholesterolemia, and the mechanistic rationale is structurally weak — HoFH's core LDLR deficiency cannot be compensated by UDCA's bile acid–mediated cholesterol modulation. The score likely reflects knowledge graph topology artefacts rather than actionable biology.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank API to confirm or refute mechanistic plausibility
- Conduct targeted literature review using broader search terms (UDCA + dyslipidaemia, UDCA + familial hypercholesterolaemia, UDCA + LDL-C) to rule out any indirect evidence not captured in the current query
- Obtain India package insert to complete key warnings and contraindications (currently blocking safety evaluation at Stage S1)
- Evaluate whether TxGNN's high score for HoFH is a systematic false positive due to cholesterol pathway node over-representation in the knowledge graph — if so, consider down-weighting this class of predictions
- If UDCA is to be pursued for any lipid-related indication, heterozygous FH or non-familial hypercholesterolaemia would represent more biologically defensible targets than HoFH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

