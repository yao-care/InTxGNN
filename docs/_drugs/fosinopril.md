---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Fosinopril is an ACE inhibitor generally used for hypertension and related cardiovascular indications, though no India-specific approved indication text is available in this evidence pack. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but this prediction is currently supported by **no clinical trials and no literature** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Fosinopril is not registered in India (no license/indication text in this evidence pack); generically an ACE inhibitor class drug |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Fosinopril in this evidence pack. Based on known pharmacological classification, Fosinopril is an angiotensin-converting enzyme (ACE) inhibitor that acts on the renin-angiotensin-aldosterone system (RAAS) to lower blood pressure and provide renal-protective effects — this is a well-established class effect of ACE inhibitors.

Malignant hypertensive renal disease involves severe, rapidly progressive hypertension with renal damage, mechanistically connected to RAAS dysregulation. The generic "ACEi → hypertension/renal disease" pharmacological link in the knowledge graph likely drives this prediction, but it has not been specialized to the malignant subtype with any direct clinical or literature evidence.

Because no clinical trials, ICTRP registrations, or PubMed literature were found for this specific drug-disease pairing, the mechanistic rationale should be treated as generic class-level plausibility rather than validated evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Fosinopril is currently not marketed in India — there are no product license records available (0 registrations).

---

## Safety Considerations

**Drug Interactions**: Fosinopril has 183 recorded interactions in the DDI database. Notable interactions include:
- **Major**: Potassium bicarbonate, Potassium citrate (potassium-elevating agents — combined with an ACE inhibitor, this raises hyperkalemia risk consistent with known ACEi pharmacology)
- **Moderate**: multiple corticosteroids (Hydrocortisone, Betamethasone, Budesonide, Triamcinolone, Dexamethasone), antidiabetic agents (Alogliptin, Canagliflozin, Chlorpropamide, Dapagliflozin, Empagliflozin, Metformin, Saxagliptin), Acetylsalicylic acid, Dronabinol, Bupropion, Morphine, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes)

No TFDA/label-level key warnings or contraindications data are currently available for this drug (see Data Gap DG001 below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials or literature), and a blocking data gap on TFDA label warnings/contraindications (DG001) prevents any S1 safety pre-assessment. Fosinopril is also not currently marketed in India, and MOA confirmation is missing (DG002).

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA label warnings and contraindications to enable safety pre-assessment
- Resolve DG002: confirm mechanism of action via DrugBank query
- Independent clinical or preclinical evidence specific to malignant hypertensive renal disease (current dataset has zero trials/literature)
- Clarify original approved indication and any India market entry pathway, since no license records currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

