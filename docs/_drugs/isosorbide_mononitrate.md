---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina Pectoris to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate (ISMN) is a long-acting organic nitrate widely used for the prevention and management of angina pectoris, exerting its effects through nitric oxide (NO)-mediated vasodilation.
The TxGNN model predicts it may be effective for **Hypertrichosis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
However, biological plausibility analysis strongly indicates this is likely a false positive — ISMN's mechanism more plausibly *induces* excessive hair growth as a side effect, rather than treating it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris (prevention and acute management) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.9950% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, isosorbide mononitrate is an active metabolite of isosorbide dinitrate and — unlike the dinitrate — does not require hepatic biotransformation to exert its effect. It spontaneously releases nitric oxide (NO) after absorption, which activates soluble guanylate cyclase (sGC) in vascular smooth muscle cells. The resulting rise in cyclic GMP (cGMP) triggers smooth muscle relaxation and systemic vasodilation, reducing cardiac preload and afterload and relieving myocardial ischemia.

The TxGNN model appears to have captured a conceptual bridge between ISMN's vasodilatory action and hair follicle biology: NO-mediated increases in microcirculation could theoretically improve blood delivery to hair follicles, analogous to part of minoxidil's proposed mechanism for hair regrowth. This indirect mechanistic similarity may have elevated hypertrichosis as a high-score prediction.

**The critical problem is directionality.** Hypertrichosis (excessive, abnormal hair growth) is a well-documented **side effect** of minoxidil — not an indication for treatment. If ISMN shares overlapping NO/vasodilation mechanisms with minoxidil, it would more plausibly *cause* hypertrichosis than *treat* it. The simultaneous high-score prediction of both hypertrichosis (#1) and alopecia (#5) — physiologically opposite conditions — is a further signal of systematic model bias in the hair-follicle subgraph. Among all 10 analyzed predictions, **pulmonary arterial hypertension (PAH, rank #10)** carries the highest mechanistic plausibility: ISMN releases NO → activates pulmonary vascular sGC → elevates cGMP → relaxes pulmonary artery smooth muscle → reduces pulmonary arterial pressure. This pathway is the validated therapeutic core of PAH pharmacology (riociguat acts on sGC directly; sildenafil/tadalafil inhibit cGMP breakdown downstream).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Isosorbide mononitrate in hypertrichosis.

---

## Literature Evidence

Currently no related literature available for Isosorbide mononitrate in hypertrichosis.

---

## India Market Information

Isosorbide mononitrate is **not currently marketed in India** based on available regulatory data. No registered product authorizations are on file.

---

## Safety Considerations

**Drug Interactions** (189 total interactions identified; key interactions listed below):

| Interacting Drug | Level | Clinical Significance |
|-----------------|-------|-----------------------|
| Bupropion | Moderate | May potentiate hypotensive effects; monitor blood pressure |
| Morphine | Moderate | Opioids can amplify vasodilation; increased risk of orthostatic hypotension |
| Canagliflozin | Moderate | SGLT2 inhibitors combined with nitrates may increase hypotension risk |
| Dapagliflozin | Moderate | SGLT2 inhibitors combined with nitrates may increase hypotension risk |
| Empagliflozin | Moderate | SGLT2 inhibitors combined with nitrates may increase hypotension risk |
| Ertugliflozin | Moderate | SGLT2 inhibitors combined with nitrates may increase hypotension risk |
| Dronabinol | Moderate | Cannabinoids may enhance vasodilatory and hypotensive effects |
| Nabilone | Moderate | Cannabinoids may enhance vasodilatory and hypotensive effects |
| Rosiglitazone | Moderate | Thiazolidinediones may potentiate blood pressure lowering |
| Sapropterin | Moderate | BH4 cofactor enhances endogenous NO synthesis; additive vasodilation possible |
| Opium | Moderate | Opioid component may potentiate vasodilation and hypotension |
| Omeprazole | Minor | Minor pharmacokinetic interaction; clinical significance low |

> ⚠️ **Critical unlisted interaction**: ISMN is **absolutely contraindicated** with PDE5 inhibitors (sildenafil, tadalafil, vardenafil). Co-administration causes severe, potentially fatal hypotension. This is clinically decisive: PDE5 inhibitors are first-line agents for pulmonary arterial hypertension (the most mechanistically plausible predicted indication), making combination therapy in PAH patients categorically unsafe under current guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (hypertrichosis) carries zero clinical or literature evidence and fails the biological plausibility test — the mechanism points in the wrong direction. Across all 10 predictions, every indication is rated L5 (model prediction only) with the exception of PAH (L4, preclinical/mechanism data only), and PAH is itself blocked by a critical drug–drug interaction barrier with the current standard of care.

**To proceed, the following is needed:**
- MOA data from DrugBank API (flagged as High-severity data gap DG002) to formally confirm the NO-cGMP mechanism
- India package insert (CDSCO, flagged as Blocking data gap DG001) to establish approved indications, contraindications, and black-box warnings before any S1 safety evaluation
- Focused literature review specifically on ISMN monotherapy in PAH models (separate from hybrid molecule studies such as CDDO-NO)
- Pharmacological feasibility assessment: whether inhaled or intratracheal ISMN delivery could achieve selective pulmonary vasodilation while avoiding systemic hypotension and PDE5i contraindication
- Re-ranking of all 10 predicted indications by biological plausibility score to identify the strongest repurposing candidate for further development
- Nitrate tolerance risk assessment for any proposed chronic-use indication

---

*⚕️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

