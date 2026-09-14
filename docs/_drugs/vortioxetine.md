---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 888
evidence_level: L5
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

> Vortioxetine is a multimodal serotonergic antidepressant globally approved for the treatment of **Major Depressive Disorder (MDD)**.
> The TxGNN model predicts it may also be effective for **Neurotic Disorder**,
> currently supported by **1 clinical trial** and **1 publication** — with the caveat that "neurotic disorder" is an older diagnostic term that may substantially overlap with the drug's existing depression indication rather than representing a truly independent new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — per included literature evidence (structured license data not available for India) |
| Predicted New Indication | Neurotic Disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured DrugBank mechanism-of-action data is a documented gap in this evidence pack (`original_moa: [Data Gap]`). However, the literature evidence included in this pack (Sanchez et al., 2015, PMID 25016186) describes Vortioxetine as a multimodal serotonergic agent: a 5-HT3, 5-HT7, and 5-HT1D receptor antagonist, 5-HT1B receptor partial agonist, 5-HT1A receptor agonist, and serotonin transporter (SERT) inhibitor. This multi-receptor profile enhances serotonergic, noradrenergic, dopaminergic, cholinergic, histaminergic, and glutamatergic neurotransmission in brain regions implicated in mood and cognition.

"Neurotic disorder" is a legacy psychiatric classification term that historically overlapped with the depressive and anxiety spectrum. The TxGNN knowledge graph appears to have linked it closely to MDD-related nodes, which is consistent with Vortioxetine's established mechanism. However, the evidence pack's own mechanistic assessment for this candidate is explicit that this is likely **not a genuinely new indication**, but rather a terminology variant of the drug's existing depression indication.

This interpretation is reinforced by two closely related, higher-confidence candidates also returned by the model: "neurotic depression" (L1 evidence, 1 large real-world cohort + 20 publications including a Lancet network meta-analysis of 21 antidepressants) and "melancholia" (L1 evidence, **6 completed Phase 3 RCTs** — the original MDD registration trials for Vortioxetine). Both are essentially confirmatory of the known MDD indication rather than novel repurposing signals. By contrast, a fourth candidate in this batch ("benign paroxysmal torticollis of infancy") had zero supporting evidence and was flagged Hold — illustrating that not all high TxGNN scores reflect a plausible mechanistic link.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completed | 370,212 | Large nationwide claims-database retrospective cohort comparing medication utilization patterns and adverse outcomes across commonly used antidepressants, to assess real-world clinical benefit of antidepressant therapy. Not a dedicated neurotic-disorder trial; graded "B" (indirect evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review (case report) | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case report on "neurotic depression" discussing predisposing personality factors and clinical features; notes benefit of combined antidepressant + CBT approach. |

---

## India Market Information

Vortioxetine is not currently marketed in India — no license registrations are recorded in this evidence pack (`total_licenses: 0`, `market_status: 未上市`).

---

## Safety Considerations

**Key Warnings / Contraindications**: No official India label data available (Blocking data gap — see below).

**Drug Interactions**: 151 total interactions identified. Selected clinically significant (Major-level) interactions:

| Interacting Drug | Level | Source |
|---|---|---|
| Bupropion | Major | ddinter |
| Lorcaserin | Major | ddinter |
| Diethylpropion | Major | ddinter |
| Dolasetron | Major | ddinter |
| Palonosetron | Major | ddinter |
| Phentermine | Major | ddinter |

Additional Moderate-level interactions include morphine, acetylsalicylic acid, dexamethasone, chlorpropamide, glimepiride, and several insulin formulations (full list of 151 available in source data).

**Data Gap (Blocking):** Official India label warnings/contraindications (`DG001`) are not yet retrieved, which prevents this candidate from clearing the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Vortioxetine's mechanism plausibly extends to the broader depression/neurotic spectrum — and closely related candidates ("neurotic depression," "melancholia") are backed by L1 evidence including 6 completed Phase 3 RCTs — the top-ranked candidate "neurotic disorder" itself has only indirect evidence (1 real-world cohort, 1 case report) and likely represents terminology overlap with the drug's existing MDD indication rather than a genuinely novel use. Critically, the missing India label data (`DG001`, Blocking severity) prevents this candidate from clearing the S1 safety pre-screening stage regardless of indication-level evidence strength.

**To proceed, the following is needed:**
- Official India-approved label (warnings/contraindications) — resolve Blocking gap DG001
- Structured DrugBank MOA data — resolve High-severity gap DG002
- Clinical clarification of whether "neurotic disorder" represents a distinct target population or is synonymous with the drug's existing MDD indication
- If India market entry is pursued, formal registration/licensing application status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

