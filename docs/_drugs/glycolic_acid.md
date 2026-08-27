---
layout: default
title: Glycolic Acid
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Glycolic Acid
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

Using the drug-repurposing evaluation report format supplied above (no additional skill applies — this is a direct content-generation task per explicit instructions in the prompt).

I reviewed the Evidence Pack closely before writing. Two things shape this report: (1) `predicted_indications[0]` (the top-ranked candidate, "atypical coarctation of aorta") has **zero** clinical trial or literature support and an explicitly negative mechanistic assessment in the pack itself; (2) the drug has no recorded original indication, no MOA, and is unmarketed in India, with a **Blocking**-severity data gap on label warnings/contraindications. I've followed the template literally for the required tables (which pull from `predicted_indications[0]`), and added a short supplementary table summarizing the other 9 candidates, since this pack is explicitly multi-candidate (`TW-DB03085-multi`) and omitting that context would misrepresent the evidence.

---

# Glycolic Acid: From No Established Indication to Atypical Coarctation of Aorta (Prediction Unsupported by Evidence)

## One-Sentence Summary

Glycolic acid (DrugBank ID DB03085) has no recorded original indication or mechanism-of-action data in this evidence pack, and it is not currently marketed in India. The TxGNN model's top-ranked prediction — **Atypical Coarctation of Aorta** — carries a 99.72% model score but is supported by **zero clinical trials and zero literature citations**, and independent review of all ten ranked candidates found no indication with genuine, mechanistically coherent supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established (no license or indication data on record) |
| Predicted New Indication | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glycolic acid is currently a data gap (DG002, High severity), so a mechanism-based plausibility assessment cannot be performed with confidence. Similarly, no original approved indication or India license history exists for this compound (0 registrations), so there is no established therapeutic baseline to compare the new prediction against.

For the top-ranked candidate itself, the pack's own mechanistic review concludes there is **no known biological link**: atypical coarctation of the aorta is a structural congenital cardiovascular malformation, whereas glycolic acid's known chemistry is limited to its properties as an alpha-hydroxy acid (keratolytic activity, pH modulation). No plausible pathway connects the two, and the prediction rests purely on TxGNN graph-embedding similarity with no clinical or literature corroboration.

It is also worth noting that the candidate with the largest apparent literature base — "esophageal disease" (rank 3, 9 papers, L4) — does not hold up on closer reading. Nearly all of those papers concern **polyglycolic acid (PGA) or PLGA polymer biomaterials** (surgical sheets, stents, nanoparticle drug carriers) rather than the small-molecule glycolic acid itself; this is a name-collision false positive. The one paper that does concern glycolic acid as a molecule (PMID 24996905) describes **glycolic aciduria as a disease-causing metabolic abnormality**, which points in the opposite direction from a therapeutic use case. No candidate in this pack, including the top-ranked one, is currently supported by coherent mechanistic or empirical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available (for the top-ranked candidate, "Atypical Coarctation of Aorta").

**Note on other predicted indications:** While the top-ranked candidate has no literature, three lower-ranked candidates returned PubMed hits that were reviewed and found not to constitute genuine supporting evidence:

| Rank | Disease | Score | Evidence Level | Literature Hits | Reviewer Finding |
|------|---------|-------|-----------------|------------------|-------------------|
| 3 | Esophageal disease | 99.69% | L4 | 9 | Mostly PGA/PLGA biomaterial studies (name-collision false positives); one paper on glycolic acid points to pathology, not treatment |
| 5 | Aortic malformation | 99.58% | L5 | 1 | PLGA vascular wrap material study, unrelated to glycolic acid pharmacology |
| 7 | Disorder of carbohydrate absorption/transport | 99.52% | L5 | 2 | PLGA nanoparticle drug-delivery studies, unrelated to the proposed indication's mechanism |

All other ranked candidates (atypical coarctation of aorta, non-syndromic esophageal malformation, potassium deficiency disease, sclerosing cholangitis, and the four hyperinsulinism/hypoglycemia variants) returned no clinical trial or literature evidence at all. All ten candidates are scored L4–L5 and flagged **Hold** in the source data.

## India Market Information

Glycolic acid is not currently marketed in India — 0 registrations/licenses on record. No authorization, product, or approved-indication data is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently data gaps; the drug-interaction database query additionally failed due to a missing local data file, so DDI screening could not be completed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no clinical, literature, or mechanistic support, and review of the pack's other nine candidates found no genuine repurposing signal — the best-looking literature base (esophageal disease) turns out to reflect an unrelated polymer material (PGA/PLGA), not the glycolic acid molecule. Combined with the absence of any established original indication, MOA, or India market presence, and a **Blocking**-severity gap in label safety data, this candidate does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- India/TFDA package insert warnings and contraindications (DG001 — Blocking; required before any S1 safety screening can occur)
- Verified mechanism of action for glycolic acid (DG002 — High)
- Confirmation of glycolic acid's actual approved indication(s) and regulatory status, if any, in relevant markets
- If the esophageal-disease signal is to be pursued further, a re-run literature search restricted explicitly to small-molecule glycolic acid (excluding PGA/PLGA polymer and biomaterial studies) to determine whether any genuine supporting evidence exists
- Repair of the local DDI dataset (ddinter files missing) so a proper interaction screen can be run
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

