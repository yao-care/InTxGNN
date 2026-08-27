---
layout: default
title: Glycerin
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Glycerin
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

# Glycerin: From No Registered Indication in Taiwan to Irritable Bowel Syndrome (Hypothesis-Stage)

> ⚠️ **Editorial Note on Candidate Selection**: TxGNN's single highest-scoring prediction (rank 1, *cauda equina syndrome*, score 99.60%) is explicitly flagged in the evidence pack's own mechanistic-review as having **"no mechanistic relevance whatsoever... a false-positive association in the TxGNN latent space, with no clinical significance."** Four other top-10 predictions (*primary hereditary glaucoma*, *congenital hypotrichosis milia*, *hypotrichosis simplex of the scalp*, *diffuse alopecia areata*) carry the same "Hold / L5 / no evidence" verdict, and the *migraine* candidates (rank 9–10) are flagged as likely **data-confusion artifacts** between Glycerin (glycerol) and the pharmacologically distinct drug Glycerol Trinitrate (nitroglycerin). Presenting rank 1 as "the" predicted indication would therefore be misleading. This report instead evaluates **Irritable Bowel Syndrome (rank 6)** — the candidate with the strongest independent mechanistic rationale — as the primary hypothesis, and summarizes the other screened candidates separately below.

---

## One-Sentence Summary

> Glycerin (Glycerol, DB09462) has no approved product registration in Taiwan and no documented original indication in this evidence pack; internationally it is best known as an osmotic laxative and osmotic agent for acute pressure reduction (glaucoma/cerebral edema).
> Among ten TxGNN-predicted candidates, **Irritable Bowel Syndrome** is the most mechanistically defensible — Glycerin's established osmotic-laxative action is directly relevant to constipation-predominant symptoms — but it is currently supported by **0 disease-specific publications** and only **1 tangentially related, non-drug clinical trial**.
> Six of the ten candidates are internally flagged as likely false positives with no supporting evidence, and a **Blocking-severity data gap** (missing TFDA label/warning data) prevents any candidate from proceeding to formal safety evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented for Taiwan (0 registered licenses); internationally recognized use: osmotic laxative (rectal/oral) and osmotic agent for acute intraocular/intracranial pressure reduction |
| Predicted New Indication | Irritable Bowel Syndrome (constipation-predominant) — selected as the most mechanistically plausible candidate; see note above |
| TxGNN Prediction Score | 99.49% (rank 6 of 10; overall top-ranked candidate was 99.60% but assessed as a false positive) |
| Evidence Level | L4 (mechanism-based hypothesis; no disease-specific clinical trial or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for Glycerin is currently a data gap in this evidence pack (DG002, High severity). Based on widely established pharmacological knowledge, Glycerin is a small triol that acts as an osmotic agent: taken orally or administered rectally, it draws water into the bowel lumen, softening stool and stimulating peristalsis — this is the basis of its classic use as a laxative (rectal suppository/enema, and diluted oral solution). The same osmotic principle underlies its historical use to acutely reduce intraocular pressure (angle-closure glaucoma emergencies) and intracranial pressure (cerebral edema).

Irritable Bowel Syndrome, particularly the constipation-predominant subtype (IBS-C), shares a core symptom domain — infrequent, hard stool and reduced motility — with the classic constipation indication that Glycerin already addresses through an osmotic mechanism. This makes IBS-C a biologically coherent extension of Glycerin's known pharmacology, even though the disease label "IBS" differs from "constipation" in etiology (visceral hypersensitivity and gut-brain axis dysregulation are also implicated in IBS, which Glycerin's osmotic action does not address).

No clinical trial or published study in this evidence pack directly tests Glycerin in an IBS population. The single retrieved trial (NCT05723731) evaluates transcutaneous auricular vagal nerve stimulation for chronic constipation — a non-pharmacological intervention with no connection to Glycerin — and was terminated. This candidate therefore remains a **mechanism-driven hypothesis**, not an evidence-supported indication, and should be treated as a research question rather than a near-term repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05723731](https://clinicaltrials.gov/study/NCT05723731) | N/A | Terminated | 106 | Evaluated transcutaneous auricular vagal nerve stimulation (taVNS) for chronic constipation / IBS-C; non-pharmacological intervention, no Glycerin arm — relevance is limited to disease-name overlap only |

---

## Literature Evidence

Currently no related literature available specific to Glycerin and Irritable Bowel Syndrome.

---

## Taiwan Market Information

Glycerin currently has **no registered pharmaceutical product licenses in Taiwan** (`market_status: 未上市`, `total_licenses: 0`). No brand names, dosage forms, or approved indication text are available from TFDA records in this evidence pack.

---

## Safety Considerations

**Drug Interactions**: The DDI database (DDInter) returns **220 documented interactions** for Glycerin, predominantly of Moderate severity. A representative sample from the query results:

| Interacting Drug | Severity Level | Source |
|---|---|---|
| Abiraterone | Moderate | DDInter |
| Tramadol | Moderate | DDInter |
| Acetazolamide | Moderate | DDInter |
| Doxycycline | Minor | DDInter |
| Hydrocortisone | Moderate | DDInter |
| Salbutamol | Moderate | DDInter |
| Alfuzosin | Moderate | DDInter |
| Hydrochlorothiazide | Moderate | DDInter |
| Amiloride | Moderate | DDInter |
| Amiodarone | Moderate | DDInter |
| Amisulpride | Moderate | DDInter |
| Apalutamide | Moderate | DDInter |

This is a partial list (12 of 220 total interactions); a full interaction screen against any candidate concomitant regimen should be run before clinical use. **Key warnings and contraindications are not available in this evidence pack** (flagged as a Blocking data gap — see Conclusion).

---

## Other Predicted Indications Considered

For completeness, given this evidence pack covers ten TxGNN candidates, the remaining nine are summarized here rather than in separate full sections, since none reached a stronger evidence tier than IBS:

| Rank | Disease | Score | Evidence Level | Verdict |
|---|---|---|---|---|
| 1 | Cauda equina syndrome | 99.60% | L5 | **False positive** — no mechanistic link; surgical emergency, unrelated to Glycerin's pharmacology |
| 2 | Open-angle glaucoma | 99.59% | L4 | Weak — Glycerin's real, established use is *acute angle-closure* glaucoma emergencies, not chronic open-angle disease; the one retrieved trial (withdrawn, n=0) is about an unrelated macular-pigment supplement |
| 3 | Primary hereditary glaucoma | 99.56% | L5 | **False positive** — structural/genetic outflow defect, not addressable by an osmotic agent |
| 4 | Alopecia | 99.55% | L4 | Weak-to-moderate — 1 ambiguous trial (drug identity unconfirmed) + 13 publications, mostly indirect (Glycerin as a formulation excipient, or basic skin-barrier science), not direct efficacy evidence |
| 5 | Congenital hypotrichosis milia | 99.50% | L5 | **False positive** — rare structural/developmental hair-follicle disorder |
| 7 | Hypotrichosis simplex of the scalp | 99.47% | L5 | **False positive** — genetic follicle-development defect |
| 8 | Diffuse alopecia areata | 99.45% | L5 | **False positive** — autoimmune mechanism, unrelated to osmotic/humectant action |
| 9 | Migraine disorder | 99.27% | L5 | **Likely data-confusion artifact** — core literature actually studies Glycerol Trinitrate (nitroglycerin), a different drug used to *induce* migraine models, not treat migraine |
| 10 | Migraine with brainstem aura | 99.18% | L5 | Same artifact as above, with thinner evidence (2 papers) |

None of these candidates should be prioritized ahead of, or instead of, the IBS hypothesis without new primary evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking-severity data gap** (DG001: missing TFDA label warnings/contraindications) means no candidate — including IBS — can proceed to a formal S1 safety evaluation regardless of indication-level promise.
- Glycerin has **zero market presence in Taiwan** (0 registered licenses), so there is no existing local regulatory or clinical-use foundation to build on.
- The TxGNN prediction set for this drug is unusually noisy: 6 of 10 top candidates are internally assessed as mechanistically implausible false positives, and the highest-scoring prediction (cauda equina syndrome) has no clinical meaning.
- Even the best remaining candidate (IBS) has **no disease-specific clinical trial or published literature** — it is a mechanism-only hypothesis (L4), not an evidence-backed repurposing opportunity.

**To proceed, the following is needed:**
- Remediate DG001: obtain TFDA (or equivalent) label warnings and contraindication data before any safety evaluation can begin
- Remediate DG002: confirm formal mechanism-of-action documentation via DrugBank or primary pharmacology sources
- Design or identify a clinical trial specifically evaluating Glycerin (oral/rectal) in an IBS-C population, since current trial evidence is non-pharmacological and unrelated
- Clarify Taiwan registration/market-entry pathway given the drug is currently unmarketed
- Verify literature attribution for the migraine candidates to rule out confusion between Glycerin and Glycerol Trinitrate before any further action on those candidates
- Treat cauda equina syndrome, hereditary glaucoma, and the hypotrichosis/alopecia-areata candidates as deprioritized/closed unless new supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

