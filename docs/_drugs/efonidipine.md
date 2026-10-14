---
layout: default
title: Efonidipine
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 4
---

# Efonidipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Efonidipine: From Hypertension to Pulmonary Hypertension

## One-Sentence Summary

Efonidipine is a calcium channel blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension (with unclear multifactorial mechanism)**,
but **no clinical trials** and **no directly relevant publications** currently support this direction, so the prediction remains model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, efonidipine is a dual L-type/T-type calcium channel blocker with vasodilatory activity, and its blood-pressure-lowering efficacy in systemic hypertension is established (it is authorised for this use in Japan and India). Mechanistically, it may be applicable to pulmonary hypertension, because pulmonary vascular tone and smooth muscle proliferation also depend on calcium signalling.

Other predictions from the model follow a similar pattern:
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.14%): hypoxia-driven pulmonary vasoconstriction and remodelling involve calcium signalling and the HIF-1 pathway. The only related publication is an in vitro study of a different drug, cilnidipine, which is class-level hint at best.
- **Malignant hypertensive renal disease** and **malignant renovascular hypertension** (both 99.04%): these are close to the approved use. Efonidipine's vasodilation of glomerular arterioles gives a rationale for renal protection. However, these are more severe disease forms than the labelled use, and no trials or literature were found.

The mechanistic rationale is therefore plausible but speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications directly support efonidipine in pulmonary hypertension. Two indirect publications were found for the hypoxia-related prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19374868](https://pubmed.ncbi.nlm.nih.gov/19374868/) | 2009 | Preclinical (in vitro) | European Journal of Pharmacology | Compared several L-type calcium channel blockers (including efonidipine) on HIF-1 activity in vascular cells; the title highlights selective suppression by cilnidipine, a different drug |
| [7557732](https://pubmed.ncbi.nlm.nih.gov/7557732/) | 1995 | Preclinical (animal) | Nihon Yakurigaku Zasshi | Efonidipine showed protective effects in mouse and rat models of cerebral ischaemia and anoxia; not related to pulmonary hypertension |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72675 | Efnocar 20 Tablet | Strip of 10 tablets | Not stated |
| 73173 | Efonta 20 Tablet | Strip of 15 tablets | Not stated |
| 76085 | Efnocar 10mg Tablet | Strip of 10 tablets | Not stated |
| 72455 | Efnocar 40 Tablet | Strip of 10 tablets | Not stated |
| 72983 | Efonta 40mg Tablet | Strip of 15 tablets | Not stated |

Seven valid single-ingredient registrations exist in total (the two not shown are Efnocar-MX 40/25 Tablet MR and Efonta T 20mg/40mg Tablet).

## Safety Considerations

Please refer to the package insert for safety information.

One pharmacology record indicates that efonidipine acts on the Cav3.2 (T-type calcium channel, CACNA1H) target; no specific drug–drug interactions were identified in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.14%), but there are no clinical trials and no efonidipine-specific publications for pulmonary hypertension, so the evidence is at the model-prediction level only (L5). The mechanistic rationale is plausible but unverified, and the key safety information is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India market (currently blocking for safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical studies of efonidipine in pulmonary hypertension models (e.g., hypoxia-induced or monocrotaline models)
- A literature search focused on efonidipine and pulmonary vascular effects
- Safety assessment for pulmonary hypertension populations, including haemodynamic effects of systemic vasodilation
- Review of the closer-to-label predictions (malignant hypertensive renal disease, malignant renovascular hypertension) as possibly lower-risk alternatives to explore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

