---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibacterial conventionally used against anaerobic and gram-positive bacterial infections; no locally registered original-indication text is available in this evidence pack. The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-derived (L5) signal with no direct biological or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local registration data (drug not marketed in India). Internationally, Clindamycin is used for anaerobic and gram-positive bacterial infections. |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Clindamycin is not available in this evidence pack. Based on general pharmacological knowledge, Clindamycin inhibits bacterial protein synthesis by binding the 50S ribosomal subunit and is effective against anaerobic and gram-positive organisms; its established uses span intra-abdominal, skin/soft-tissue, and bacterial vaginosis-type infections.

Punctate epithelial keratoconjunctivitis, however, is predominantly a viral (e.g., adenoviral), dry-eye, or immune-mediated condition rather than a typical bacterial infection. Clindamycin has no antiviral activity, so there is no straightforward mechanistic bridge between its known pharmacology and this predicted indication.

The evidence pack's own rationale for this candidate explicitly flags the link as weak: it describes the association as a statistical artifact of the knowledge-graph embedding ("KG embedding 之統計關聯") rather than a biologically grounded hypothesis. Given the absence of any supporting clinical trials or literature (evidence level L5), this prediction should be treated as exploratory only and not acted upon without independent mechanistic or preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Clindamycin currently holds no registrations in the India market (market status: Not Marketed; total registrations: 0). No product, dosage form, or approved-indication data is available for local reference.

---

## Safety Considerations

Drug-specific labeled warnings and contraindications are not yet available in this evidence pack; please refer to the official package insert for that information.

**Drug Interactions** (from DDI database, 320 total interactions on file for Clindamycin; key Moderate-level interactions shown below):

| Interacting Drug | Level | Source |
|------|------|--------|
| Balsalazide | Moderate | ddinter |
| Clarithromycin | Moderate | ddinter |
| Picosulfuric acid | Moderate | ddinter |
| Attapulgite | Moderate | ddinter |
| Kaolin | Moderate | ddinter |

An additional large set of interactions (e.g., Amphotericin B, Acetylsalicylic acid, Amoxicillin, Bupropion, Pantoprazole, Glimepiride, Doxycycline, Clotrimazole, Morphine, Metformin, Omeprazole, Sucralfate, Rosiglitazone, Lansoprazole, Vancomycin) is on file but classified with "Unknown" severity level by the source database — these should be reviewed individually before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Punctate Epithelial Keratoconjunctivitis) has no clinical trial or literature support and is explicitly noted in the underlying rationale as a weak, mechanistically unsupported statistical association (evidence level L5). Additionally, a Blocking-severity data gap (missing local label warnings/contraindications, DG001) prevents this candidate from entering safety pre-screening (S1) at all.

**To proceed, the following is needed:**
- Local label warnings and contraindications (DG001 — Blocking; required before any S1 safety review)
- Mechanism-of-action data for Clindamycin (DG002 — High priority; needed to properly assess mechanistic plausibility)
- Direct preclinical or clinical efficacy data for Clindamycin specifically in punctate epithelial keratoconjunctivitis (none currently exists)
- Consider re-evaluating other ranked candidates in this evidence pack with stronger indirect support — e.g., **exposure keratitis** (rank 2, evidence level L4, 4 supporting publications on causative pathogens including MRSA) — as a potentially more tractable repurposing direction than the top-ranked candidate
- Note: rank 3 ("non-human animal disease") appears to be a data-quality issue (a generic KG disease-category label, not a valid human indication) and should be excluded from further candidate consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

