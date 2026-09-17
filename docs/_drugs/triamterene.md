---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 855
evidence_level: L5
indication_count: 6
---

# Triamterene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Triamterene: From Potassium-Sparing Diuretic Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Triamterene is pharmacologically a potassium-sparing diuretic that inhibits the epithelial sodium channel (ENaC) in the distal nephron; no formal original-indication or MOA record is present in this evidence pack.
> The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
> but **zero clinical trials** and **zero publications** currently support this specific direction — the prediction is model-derived only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (drug not marketed in Taiwan/reference market; no approved indication text on file) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed DrugBank mechanism-of-action (MOA) data is not available for Triamterene. Based on the pharmacological description captured in the model's reasoning notes, Triamterene is a potassium-sparing diuretic that inhibits ENaC in the distal tubule/collecting duct, reducing sodium and water reabsorption while sparing potassium excretion. Diuretics as a class are used adjunctively for blood-pressure control, which is the superficial rationale the model likely picked up on.

However, the mechanistic fit to this specific candidate is weak and potentially counter-indicated. Malignant hypertensive renal disease involves acute vascular endothelial injury and a rapid drop in glomerular filtration rate — a physiological state in which a potassium-sparing agent carries meaningful risk of inducing or worsening hyperkalemia, which runs *against* the clinical management goal rather than supporting it.

No clinical trial or literature evidence accompanies this prediction, and the model's own rationale flags the mechanistic link as tenuous. This should be treated as a hypothesis generated purely from knowledge-graph embedding proximity (L5), not as a clinically supported signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

No registration or license records are currently available. Triamterene is not marketed in the reference jurisdiction (market status: Not Marketed; total licenses: 0), so no product/indication table can be produced.

---

## Safety Considerations

- **Drug Interactions**: 104 total interactions on file (20 detailed entries reviewed). Notable findings:
  - **Major**: Potassium citrate — combined use raises hyperkalemia risk, directly relevant to the mechanistic concern above.
  - **Moderate**: Hydrocortisone, Metformin, Bupropion, Triamcinolone, Morphine, Dexamethasone, Betamethasone, Bisacodyl, Budesonide, Canagliflozin, Dapagliflozin, Dronabinol, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes) — includes two SGLT2 inhibitors (canagliflozin, dapagliflozin), which independently carry a hyperkalemia signal when paired with potassium-sparing diuretics.
  - **Minor**: Famotidine, Ranitidine, Doxycycline, Cimetidine, Minocycline.

Formal key warnings and contraindications (e.g., from a product label) are not currently available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5, model prediction only), and the drug's own potassium-sparing mechanism plausibly conflicts with the pathophysiology of malignant hypertensive renal disease (hyperkalemia risk in a setting of acute renal impairment). There is no basis to advance this indication at this time.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (currently blocking — flagged as DG001)
- Confirmed DrugBank mechanism-of-action data (flagged as DG002)
- Original approved indication(s) for Triamterene, to establish a baseline for mechanistic comparison
- Targeted literature/trial search specific to diuretic use in malignant hypertension or hypertensive nephropathy, with explicit assessment of hyperkalemia risk
- Note: other TxGNN candidates for this drug (e.g., chronic pulmonary heart disease, pulmonary hypertension due to lung disease/hypoxia) carry marginally more literature context — though still weak (L4, Research Question stage) — and may warrant parallel review before further prioritization.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

