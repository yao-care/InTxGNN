---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 5
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a selective β1-adrenergic receptor blocker widely used in clinical practice for hypertension, chronic heart failure, and angina pectoris.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction score of **99.94%**.
However, **no supporting clinical trials or literature** specific to this indication were identified; the current evidence level is model prediction only (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, chronic stable heart failure, angina pectoris |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question (Hold) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from the structured data source. Based on established pharmacology, Bisoprolol is a highly cardioselective β1-adrenergic receptor antagonist. By blocking β1 receptors in the heart, it reduces heart rate and cardiac output, thereby lowering systemic blood pressure. In addition, β1 blockade at the juxtaglomerular apparatus suppresses renin secretion, dampening activity of the renin–angiotensin–aldosterone system (RAAS).

Malignant hypertensive renal disease (malignant nephrosclerosis) is an acute, severe form of hypertensive end-organ damage characterised by markedly elevated blood pressure causing direct vascular injury to the glomeruli and arterioles. The mechanistic link to Bisoprolol is indirect: by reducing cardiac output and suppressing renin release, the drug lowers blood pressure and may theoretically reduce ongoing renal haemodynamic injury. However, this is a second-order mechanism — standard first-line therapy for malignant hypertension prioritises intravenous antihypertensives for acute blood pressure reduction, while long-term renoprotection is managed primarily with ACE inhibitors or ARBs.

The TxGNN model likely captures the general anti-hypertensive network connectivity of Bisoprolol within the knowledge graph, which spans multiple hypertensive end-organ disease nodes. While the mechanistic link is biologically plausible, Bisoprolol plays a supporting rather than primary role in this clinical scenario, and no direct renal endpoint evidence exists to substantiate a repurposing claim at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bisoprolol in malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available for Bisoprolol in malignant hypertensive renal disease.

---

## India Market Information

Bisoprolol is currently **not marketed** in India under any registered authorisation. No CDSCO licence records were identified in the dataset.

---

## Safety Considerations

**Drug Interactions (226 interactions identified; selected key interactions shown):**

| Interacting Drug | Interaction Level | Notes |
|-----------------|------------------|-------|
| Epinephrine | Moderate | β-blockade may blunt epinephrine-mediated bronchodilation and vasopressor response; risk of paradoxical hypertension |
| Dexamethasone | Moderate | Corticosteroids may antagonise antihypertensive effects |
| Betamethasone | Moderate | Same class as dexamethasone; similar mechanism of antagonism |
| Budesonide | Moderate | Inhaled corticosteroid; potential attenuation of antihypertensive effect |
| Hydrocortisone | Moderate | Systemic corticosteroid interaction; blood pressure antagonism |
| Triamcinolone | Moderate | Corticosteroid; similar to above |
| Bupropion | Moderate | May increase bisoprolol plasma levels via CYP2D6 inhibition |
| Morphine | Moderate | Additive hypotensive and CNS depressant effects possible |
| Atropine | Moderate | Anticholinergic drugs may counteract bradycardic effects |
| Calcium carbonate / acetate / citrate / gluconate | Moderate | Calcium salts may reduce absorption or efficacy |
| Acetylsalicylic acid | Minor | NSAIDs may blunt antihypertensive effect with regular use |
| Aluminum hydroxide | Minor | May reduce oral bisoprolol absorption |

> **Note:** A total of 226 drug interactions were identified in the database. Only a representative selection is shown above. For a complete interaction profile, consult a full DDI reference source or clinical pharmacist.

For warnings and contraindications, please refer to the approved package insert, as structured safety data were not available in this Evidence Pack (CDSCO/TFDA SmPC data pending retrieval).

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The TxGNN model assigns a high prediction score for Bisoprolol in malignant hypertensive renal disease based on knowledge graph connectivity, and a biologically plausible indirect mechanism exists (blood pressure reduction → reduced renal haemodynamic stress). However, the evidence level is L5 — no clinical trials, no published literature, and no India regulatory precedent — which is insufficient to justify any clinical development or repurposing pathway at this time.

**To proceed, the following is needed:**

- **Retrieve formal MOA data** from DrugBank API (DG002) to complete mechanistic analysis
- **Retrieve CDSCO / TFDA package insert warnings and contraindications** (DG001, currently blocking safety screening)
- **Conduct targeted literature review** focused specifically on: (1) β-blockers in malignant hypertension, (2) renal outcomes in β-blocker trials, and (3) comparative efficacy vs. ACEi/ARB in hypertensive nephrosclerosis
- **Assess clinical positioning**: determine whether Bisoprolol can be meaningfully differentiated from existing standard-of-care (IV labetalol, ACEi/ARB) in this indication
- **Consider preclinical feasibility study** to explore direct renal protective effects of β1 blockade in malignant hypertension animal models before any clinical hypothesis formation
- **India regulatory pathway review**: since Bisoprolol has 0 registered products in India, a full new drug application pathway or import licence would be required before any clinical study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

