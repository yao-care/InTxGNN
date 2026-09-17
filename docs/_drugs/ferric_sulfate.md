---
layout: default
title: Ferric Sulfate
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Ferric Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ferric Sulfate: From No Recorded Indication to Bronchitis (Low-Confidence Prediction)

## One-Sentence Summary

Ferric sulfate (DB11171) has no recorded original indication and is not currently marketed in India. TxGNN's top prediction is **bronchitis** (score 97.65%), but the only two retrieved clinical trials are unrelated Ferrlecit-vs-oral-iron studies in CKD-related anemia, graded "C" (index mismatch) — not real supporting evidence. No literature and no mechanistic link were found; this candidate should be treated as a **model-only signal**, not an actionable repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record — drug is not marketed in India and no original indications are listed |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.65% |
| Evidence Level | L5 (see note below) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on Evidence Level:** the evidence pack auto-tagged this candidate as L4, but the two clinical trials retrieved were both graded relevance "C" (trial-disease mismatch — they study Ferrlecit/IV iron vs. oral ferrous sulfate for anemia in chronic kidney disease, not bronchitis). With zero disease-relevant trials and zero literature, this candidate is more accurately **L5 — model prediction only, no actual supporting studies**.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ferric sulfate (`[Data Gap]`), and no original indication is on file — the drug is not marketed in India and carries zero registrations. This makes it impossible to build a rationale from "proven efficacy in indication A → mechanistic extension to indication B," because indication A does not exist in this dataset.

The evidence pack's own rationale is explicitly skeptical: there is no known pathophysiological connection between iron salts and bronchitis. The TxGNN score likely reflects an indirect graph co-occurrence between iron-metabolism/anemia nodes and respiratory-inflammation nodes in the knowledge graph, rather than a genuine pharmacological or causal relationship.

It is also worth noting that several lower-ranked predictions in this pack (gastroduodenitis, peptic ulcer disease) actually correspond to **known adverse effects of oral iron salts** (GI mucosal irritation), not therapeutic opportunities — a useful sanity check that the model's high-ranking outputs here should not be read as validated mechanistic signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00224055](https://clinicaltrials.gov/study/NCT00224055) | Phase 4 | Completed | 89 | Compares Ferrlecit® (IV iron) vs. oral ferrous sulfate for anemia/iron deficiency in CKD patients not on erythropoietic therapy. **Relevance: Grade C — disease mismatch, unrelated to bronchitis.** |
| [NCT00224042](https://clinicaltrials.gov/study/NCT00224042) | Phase 4 | Completed | 52 | Compares Ferrlecit® vs. oral ferrous sulfate for anemia/iron deficiency in CKD patients on erythropoietic therapy. **Relevance: Grade C — disease mismatch, unrelated to bronchitis.** |

Both trials were retrieved via drug-name matching, not disease relevance, and provide no support for a bronchitis indication.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Ferric sulfate is currently not marketed in India — no registration/license records exist (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this evidence pack; a DDI database query also failed due to a missing local reference file.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (bronchitis) has no relevant clinical trial or literature support — the only retrieved trials are index mismatches for an unrelated CKD/anemia indication — and no mechanistic rationale exists linking iron salts to bronchitis. Combined with the drug having no recorded original indication and zero market presence in India, there is no basis to advance this candidate beyond model prediction.

**To proceed, the following is needed:**
- Ferric sulfate mechanism of action (MOA) data (currently a blocking data gap)
- Original/reference indication data to establish any baseline pharmacological rationale
- TFDA/CDSCO label warnings and contraindications (currently a blocking data gap, per `DG001`)
- Disease-relevant (bronchitis-specific) clinical trial or literature search, since current retrieval only surfaced unrelated CKD-anemia trials
- DDI database reference file repair, so drug interaction queries can actually execute
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

