---
layout: default
title: Potassium Citrate
parent: High Evidence (L1-L2)
nav_order: 683
evidence_level: L1
indication_count: 10
---

# Potassium Citrate
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Potassium Citrate: From Data-Gap Original Indication to Nephrolithiasis

## One-Sentence Summary

Potassium citrate is an electrolyte / urinary alkalinizing agent (DrugBank DB09125); its original indication and detailed mechanism-of-action documentation are currently a **data gap** in this evidence pack (DG001, DG002). Among 10 TxGNN-predicted indications, only **Nephrolithiasis (kidney stones)** reaches actionable evidence strength, with **36 registered clinical trials** identified — this reflects potassium citrate's well-established real-world role in kidney stone prevention rather than a purely novel repurposing hypothesis. The remaining 9 predicted indications are TxGNN-only signals (L4–L5) with no or minimal literature/trial support and are not actionable at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — data gap (TFDA label not yet obtained, DG001) |
| Predicted New Indication | Nephrolithiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for potassium citrate is currently a data gap (DG002 — High severity). Based on the pharmacological rationale documented across the linked clinical trials, potassium citrate's citrate moiety is metabolized to bicarbonate, which alkalinizes urine and raises urinary citrate concentration. Elevated urinary citrate inhibits calcium oxalate and calcium phosphate crystal nucleation and aggregation, while citrate also chelates free calcium ions, further reducing crystallization risk.

This is not a distant, purely graph-derived TxGNN inference — it is a mechanism-level relationship consistent with an already-established standard-of-care use in urology (urinary alkalinization for stone prevention/dissolution). The evidence pack's `original_indications` field is empty due to a data gap rather than reflecting an actual absence of prior approved use, so this candidate should be read as "confirming an established use with strong trial support" rather than "speculative repurposing."

Several trials also probe genetically- or metabolically-defined stone subtypes (e.g., calcium phosphate stone formers, absorptive hypercalciuria, cystinuria-related alkalinization), reinforcing that the mechanism generalizes across multiple stone-forming etiologies, not just a single narrow population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | Completed | 300 | Direct RCT comparing potassium phosphate vs. potassium citrate for absorptive hypercalciuria and stone recurrence prevention |
| [NCT01329042](https://clinicaltrials.gov/study/NCT01329042) | Phase 4 | Completed | 80 | Potassium sodium hydrogen citrate reduces stone recurrence/residual fragments after ESWL and PCNL in calcium oxalate urolithiasis |
| [NCT03258190](https://clinicaltrials.gov/study/NCT03258190) | Phase 2 | Completed | 137 | Lime powder regimen (citrate/potassium-enriched) corrects urinary metabolic abnormalities to prevent urolithiasis recurrence |
| [NCT03984409](https://clinicaltrials.gov/study/NCT03984409) | N/A | Completed | 22 | Dietary citrate source achieves comparable urine alkalization to potassium citrate in hypocitraturia/aciduria patients |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | Active, not recruiting | 48 | Oral potassium citrate raises urinary pH to reduce ureteral stent encrustation post-ureteroscopy |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | Recruiting | 312 | Potassium citrate sustained-release tablets evaluated for urate-lowering and urinary calculi prevention in gout |
| [NCT06003348](https://clinicaltrials.gov/study/NCT06003348) | Phase 4 | Recruiting | 25 | Hydroxycitrate (citrate analog) tested to reduce calcium phosphate stone recurrence |
| [NCT05389995](https://clinicaltrials.gov/study/NCT05389995) | N/A | Active, not recruiting | 10 | Assesses potassium citrate's effect on urinary stone risk factors vs. a lemonade beverage |
| [NCT06944223](https://clinicaltrials.gov/study/NCT06944223) | N/A | Recruiting | 24 | Examines urinary oxalate/citrate response after potassium citrate consumption |
| [NCT01754779](https://clinicaltrials.gov/study/NCT01754779) | Phase 2 | Completed | 13 | Citric acid/potassium citrate reduces calcium phosphate saturation in urine of calcium phosphate stone formers |

---

## Literature Evidence

Currently no related literature available for the nephrolithiasis indication in this evidence pack (the underlying literature search returned 0 results; strong support instead comes from the 36 registered clinical trials above).

---

## Safety Considerations

**Drug Interactions**: 181 total interactions identified. Sample of Major-level interactions requiring caution (hyperkalemia risk / additive electrolyte effects): potassium-sparing agents (Amiloride), ACE inhibitors/ARBs (Benazepril, Olmesartan, Valsartan), anticholinergics (Atropine, Hyoscyamine, Homatropine, Methscopolamine), antihistamines (Chlorpheniramine, Acrivastine, Phenyltoloxamine), and Amitriptyline. Moderate-level interactions include NSAIDs (Ibuprofen, Ketorolac, Acetylsalicylic acid), Doxycycline, Aliskiren, Pseudoephedrine, and amphetamine-class stimulants (Dextroamphetamine, Amphetamine).

Key warnings and contraindications have not yet been obtained (blocking data gap DG001) — refer to the official package insert once available before clinical use.

---

## Other TxGNN-Predicted Indications (Lower Confidence, Not Actionable)

| Disease | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|
| Familial visceral myopathy | 99.95% | L5 | Hold |
| Mitochondrial oxidative phosphorylation disorder (nuclear DNA) | 99.92% | L5 | Hold |
| Pendred syndrome | 99.88% | L5 | Hold |
| Cystinosis | 99.73% | L4 | Research Question |
| Hypermanganesemia with dystonia | 99.72% | L5 | Hold |
| Nephrolithiasis susceptibility (SLC26A1) | 99.68% | L4 | Research Question |
| Autosomal recessive nonsyndromic deafness | 99.67% | L5 | Hold |
| Exocrine pancreatic insufficiency | 99.66% | L3 | Research Question |
| Leukocyte adhesion deficiency | 99.62% | L5 | Hold |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (specific to the Nephrolithiasis indication)

**Rationale:**
- Nephrolithiasis is supported by 36 registered clinical trials, including a completed Phase 3 RCT and multiple completed Phase 2/4 studies, and the mechanism (urinary alkalinization, citrate-mediated crystallization inhibition) is well established and consistent with existing standard-of-care use.
- All other 9 TxGNN-predicted indications lack meaningful clinical or literature support and should remain on **Hold** or treated as **Research Questions** only.

**To proceed, the following is needed:**
- Obtain TFDA/India package insert data to close the blocking data gap (DG001) before any safety sign-off (S1)
- Obtain formal DrugBank/manufacturer MOA documentation (DG002)
- Clarify why `original_indications` is empty — confirm whether potassium citrate already carries an approved nephrolithiasis-related indication in the target market, since this materially changes the regulatory pathway (label extension vs. de novo repurposing)
- Establish an electrolyte/hyperkalemia monitoring plan given the Major-level DDI profile (ACE inhibitors/ARBs, potassium-sparing diuretics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

