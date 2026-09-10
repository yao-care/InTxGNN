---
layout: default
title: Riociguat
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease

## One-Sentence Summary

> Riociguat is a soluble guanylate cyclase (sGC) stimulator already established for pulmonary arterial hypertension (PAH), as confirmed by the PATENT‑1/2 pivotal trial literature in this evidence pack.
> TxGNN's single highest-scoring prediction (*Ambras type hypertrichosis*, 94.9%) has zero supporting evidence and is flagged in the rationale itself as model noise, so it is not a usable candidate.
> Among the candidates that do have evidence, the model repeatedly surfaces specific **PAH etiological subtypes** — most notably **PAH associated with connective tissue disease (CTD-PAH)** — supported by **12 publications**, including a dedicated riociguat-specific PATENT‑1/2 subgroup RCT analysis, but **no dedicated clinical trials** for this subgroup are currently registered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — inferred from PATENT‑1/2 trial literature in this pack; no formal license/label data available |
| Predicted New Indication | PAH associated with Connective Tissue Disease (CTD-PAH) |
| TxGNN Prediction Score | 91.55% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

⚠️ **Note on ranking**: TxGNN's raw #1–#5, #7, #8 candidates (scores 91.5%–94.9%) — including hair-shaft disorders, Dandy-Walker syndrome, and periodontal malformation — have **zero clinical trial or literature support**, and the pack's own rationale explicitly labels them prediction noise. This report focuses on the highest-evidence, mechanistically coherent candidate (CTD-PAH) rather than the raw top score.

---

## Why is This Prediction Reasonable?

Formal MOA documentation (DrugBank) is currently a data gap (DG002). However, the literature within this pack consistently characterizes riociguat as a **soluble guanylate cyclase (sGC) stimulator** that amplifies the NO–sGC–cGMP signaling pathway, producing pulmonary vasodilation as well as anti-proliferative and anti-fibrotic effects on remodeled pulmonary vasculature.

CTD-PAH is not a separate disease but a recognized **etiological subgroup within WHO Group 1 PAH** — the same broad category riociguat is already indicated for. Connective tissue disease, particularly systemic sclerosis, is one of the largest non-idiopathic contributors to the global PAH population, and the pivotal PATENT‑1/PATENT‑2 phase III program that established riociguat's efficacy in PAH included a **prospectively planned CTD-PAH subgroup** (PMID 27457511).

Mechanistically, CTD-PAH shares the same core vasculopathy as idiopathic PAH — medial hypertrophy, intimal fibrosis, and endothelial NO/cGMP deficiency — so riociguat's sGC-stimulating action is expected to translate similarly. A clinical case series (PMID 28671485) further reports benefit when CTD-PAH patients were switched from PDE5 inhibitors to riociguat, reinforcing the biological plausibility beyond the trial subgroup data alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(A related trial exists for a different PAH-CHD subgroup — NCT07356778 — but it evaluates sotatercept add-on therapy, not riociguat, so it is not included here.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27457511](https://pubmed.ncbi.nlm.nih.gov/27457511/) | 2017 | RCT subgroup analysis | Annals of the Rheumatic Diseases | Riociguat improved outcomes in the PAH-CTD subgroup of the PATENT‑1/PATENT‑2 phase III program |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review/meta-analysis | Internal and Emergency Medicine | Meta-analysis of RCT subgroup/post-hoc data on CTD-PAH treatment outcomes |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Overview of PAH-CTD pathophysiology and treatment advances, including riociguat |
| [28671485](https://pubmed.ncbi.nlm.nih.gov/28671485/) | 2017 | Cohort (case series) | Pulmonary Circulation | Switching from PDE5 inhibitor to riociguat improved outcomes in 3 PAH-CTD patients |
| [33131480](https://pubmed.ncbi.nlm.nih.gov/33131480/) | 2020 | Review/commentary | Kardiologiia | Discusses riociguat's role in PAH associated with systemic connective tissue disease |
| [27941129](https://pubmed.ncbi.nlm.nih.gov/27941129/) | 2017 | Guideline (EULAR) | Annals of the Rheumatic Diseases | EULAR recommendations include PAH-targeted therapy for systemic sclerosis |
| [40331647](https://pubmed.ncbi.nlm.nih.gov/40331647/) | 2025 | Cohort (prospective) | Kardiologiia | Long-term survival analysis in PAH associated with autoimmune rheumatic disease |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis and treatment overview |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort (registry) | Terapevticheskii Arkhiv | Six-year national PAH registry observation |
| [40592721](https://pubmed.ncbi.nlm.nih.gov/40592721/) | 2025 | Review (narrative) | RMD Open | 2025 update on the systemic sclerosis treatment landscape |

---

## India Market Information

Riociguat currently has **no registrations** and is **not marketed** in this jurisdiction (0 licenses on file), so no product/dosage-form table is available.

---

## Safety Considerations

- **Drug Interactions**: 75 documented interactions identified (all Moderate severity in the available data), notably with:
  - Proton pump inhibitors (rabeprazole, omeprazole, pantoprazole, lansoprazole, dexlansoprazole, esomeprazole)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Antacids/mineral agents (magnesium oxide/carbonate/hydroxide, calcium carbonate, aluminum hydroxide, magaldrate, mannitol)
  - Dexamethasone, clarithromycin, papaverine

Formal label warnings and contraindications are a blocking data gap (DG001) and are not yet available in this pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CTD-PAH is a pre-specified subgroup of riociguat's pivotal PATENT‑1/2 phase III program (tier‑1 RCT subgroup evidence), reinforced by cohort/case-series data — sufficient to advance under guardrails, but not to a full "Go" given the absence of a dedicated trial in this specific subgroup and outstanding blocking safety data gaps.

**To proceed, the following is needed:**
- Official label warnings/contraindications (DG001 — blocking; required for S1 safety screen)
- Formal DrugBank/regulatory MOA documentation (DG002)
- Market entry/registration assessment, since the drug currently has zero registrations in this jurisdiction
- A dedicated prospective trial or registry analysis in the CTD-PAH population if a formal label extension is sought
- Review of the TxGNN ranking pipeline: six of the ten returned candidates (including the #1-ranked prediction) have no supporting evidence and should be filtered as noise before future evidence packs are generated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

