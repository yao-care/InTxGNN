---
layout: default
title: Dicyclomine
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 2
---

# Dicyclomine
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

# Dicyclomine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an anticholinergic and direct smooth muscle relaxant, classically used for the symptomatic relief of functional bowel disorders such as irritable bowel syndrome (IBS).
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
with **0 clinical trials** and **0 publications** currently identified to support this direction — making this a model-only prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Irritable bowel syndrome / functional gastrointestinal spasm (FDA-approved; not registered in India) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological information, Dicyclomine belongs to the anticholinergic (antimuscarinic) drug class and also exerts a direct relaxant effect on smooth muscle — a dual mechanism that distinguishes it from purely receptor-selective agents such as oxybutynin. Its established efficacy is in gastrointestinal smooth muscle spasm, particularly in IBS.

Cauda equina syndrome (CES) is a rare but serious neurological emergency caused by compression or ischaemia of the lumbosacral nerve roots within the spinal canal. One downstream complication of CES is neurogenic bladder, particularly detrusor overactivity, for which anticholinergic agents are a recognised symptomatic intervention. The TxGNN model appears to have inferred the link via the knowledge-graph path: **Dicyclomine → [muscarinic antagonist] → bladder smooth muscle → neurogenic bladder component of CES**.

However, this mechanistic connection is indirect and weak. The primary pathology of CES — nerve root compression or ischaemia — is entirely outside Dicyclomine's pharmacological scope. Definitive treatment is surgical decompression. Dicyclomine lacks bladder selectivity compared to purpose-designed urological antimuscarinics, and its systemic anticholinergic burden may be poorly tolerated in the neurological patient population. This prediction is likely an artefact of graph traversal rather than a clinically meaningful repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Dicyclomine is **not currently marketed in India**. No regulatory licenses or approved product registrations were identified.

---

## Safety Considerations

**Drug Interactions (344 interactions identified; selected examples below):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Botulinum toxin type A | Moderate | Additive anticholinergic effect; risk of enhanced neuromuscular blockade |
| Hyoscyamine | Moderate | Additive anticholinergic toxicity |
| Aclidinium | Moderate | Additive anticholinergic effects |
| Amantadine | Moderate | Enhanced anticholinergic side effects |
| Amitriptyline | Moderate | Additive anticholinergic and CNS depressant effects |
| Fentanyl | Moderate | Additive CNS/respiratory depression; reduced GI motility |
| Codeine | Moderate | Additive CNS depression and constipation risk |
| Tramadol | Moderate | Additive anticholinergic and CNS effects |
| Dihydrocodeine | Moderate | Similar to codeine interaction |
| Alfentanil | Moderate | Additive opioid–anticholinergic effects |
| Galantamine | Moderate | Pharmacodynamic antagonism (cholinergic vs. anticholinergic) |
| Ethanol | Moderate | Enhanced CNS depression |
| Chlorpheniramine | Moderate | Additive anticholinergic effects |
| Acrivastine | Moderate | Additive anticholinergic and sedative effects |
| Phenyltoloxamine | Moderate | Additive anticholinergic effects |
| Loperamide | Moderate | Additive reduction in GI motility |
| Acebutolol | Moderate | Possible pharmacodynamic interaction |
| Acetaminophen | Minor | Delayed gastric emptying may alter absorption |
| Hydrochlorothiazide | Minor | Possible additive heat stroke risk via decreased sweating |

> Key warnings and contraindications data are not available from the current evidence pack. Please refer to the approved package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates an indirect mechanistic link via neurogenic bladder, but CES is a surgical emergency and there is zero supporting clinical or preclinical evidence for Dicyclomine in this indication; the prediction does not constitute a viable repurposing hypothesis at this stage.

**To proceed, the following is needed:**

- Obtain and review the full package insert (SmPC/PIL) to document approved indications, key warnings, and contraindications (currently classified as a blocking data gap)
- Obtain MOA data from DrugBank API (DB00804) to enable formal mechanistic plausibility analysis
- Clarify whether the clinical target is the **neurogenic bladder complication of CES** (a more plausible sub-indication) rather than CES itself — if so, rerun evidence search under "neurogenic bladder" as the primary indication
- Review second-ranked prediction (Neurogenic Bladder, TxGNN score 99.50%) as a potentially more tractable repurposing candidate before advancing any CES-specific investigation
- If investigation of the neurogenic bladder indication proceeds, conduct a comparative efficacy assessment against approved bladder-selective antimuscarinics (e.g., solifenacin, tolterodine) to determine whether Dicyclomine's dual mechanism offers a clinically meaningful differentiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

