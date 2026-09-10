---
layout: default
title: Roxatidine Acetate
parent: 僅模型預測 (L5)
nav_order: 749
evidence_level: L5
indication_count: 6
---

# Roxatidine Acetate
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

# Roxatidine Acetate: From Unregistered H2-Receptor Antagonist to Active Peptic Ulcer Disease

## One-Sentence Summary

Roxatidine acetate is a histamine H2-receptor antagonist with no recorded original indication in the current regulatory dataset (drug is not marketed in India/Taiwan). The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, and this direction is strongly corroborated by **2 randomized controlled trials** and **13 additional publications**, largely because this is in fact the drug's well-established historical use as an antisecretory agent rather than a novel mechanistic leap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in dataset (no Taiwan/India license on file) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not currently available for this candidate. However, the accompanying literature evidence fills this gap: roxatidine acetate is rapidly converted by esterases to its active metabolite roxatidine, a potent H2-receptor antagonist that inhibits basal and histamine-stimulated gastric acid secretion in parietal cells. Unlike cimetidine, it does not exhibit anti-androgenic effects or interfere with hepatic (CYP-mediated) drug metabolism (PMID 1717223, 2906472). Preclinical work additionally demonstrates a cytoprotective action independent of pure acid suppression, involving endogenous prostaglandin pathways (PMID 2906796, 9379358).

This mechanism is the textbook, non-inferential basis for treating peptic ulcer disease — acid suppression combined with mucosal protection directly addresses the pathophysiology of gastric and duodenal ulcers. Notably, this is not a true "repurposing" scenario in the conventional sense: the predicted indication (active peptic ulcer disease) is the class-defining, historically established use of H2-receptor antagonists like roxatidine, dating to clinical development in the late 1980s–1990s. The TxGNN model has effectively rediscovered the drug's original therapeutic niche rather than identifying a novel disease association.

Given that this drug currently has zero regulatory registrations in India/Taiwan and no recorded "original indication" in the local dataset, the practical value of this prediction lies in supporting a **first-time market entry submission** for peptic ulcer disease, using decades of existing global clinical evidence, rather than validating a genuinely new therapeutic direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries found in `clinical_trials` or `ictrp_trials`).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1674231](https://pubmed.ncbi.nlm.nih.gov/1674231/) | 1991 | RCT | Clinical Therapeutics | Two 12-month, double-blind, placebo-controlled multicenter maintenance studies (n=725); 75mg nightly roxatidine reduced duodenal and gastric ulcer relapse vs. placebo |
| [1352083](https://pubmed.ncbi.nlm.nih.gov/1352083/) | 1992 | RCT | Am J Gastroenterol | 4-week double-blind RCT in active duodenal ulcer; roxatidine healing rate 33.9% vs. placebo 21.9% at week 2 (p=0.018), sustained advantage through week 4 |
| [8527619](https://pubmed.ncbi.nlm.nih.gov/8527619/) | 1995 | RCT | Aliment Pharmacol Ther | Double-blind RCT comparing early-evening vs. bedtime roxatidine 150mg dosing in short-term duodenal ulcer treatment; comparable efficacy and tolerability between regimens |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Review | Drugs | Comprehensive PK/PD review: >95% oral absorption, potent basal/stimulated acid suppression, no anti-androgenic effects, no hepatic enzyme interference |
| [2906456](https://pubmed.ncbi.nlm.nih.gov/2906456/) | 1988 | Review | Scand J Gastroenterol Suppl | 150mg identified as optimal dose for acid suppression; modified-release capsule sustains nocturnal acid control; confirmed ulcer-healing efficacy in trials |
| [2906472](https://pubmed.ncbi.nlm.nih.gov/2906472/) | 1988 | Review (DDI focus) | Scand J Gastroenterol Suppl | Contrasts roxatidine's minimal hepatic microsomal enzyme interaction with cimetidine/ranitidine, suggesting lower drug-interaction risk profile |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of PUD medical therapy; roxatidine and nizatidine noted as safe, effective new H2 blockers without added clinical advantage over existing agents |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Bailliere's Clin Gastroenterol | Mechanistic review of gastric acid regulation (ACh/gastrin/histamine pathways), providing pharmacological basis for H2RA antisecretory action |
| [2906796](https://pubmed.ncbi.nlm.nih.gov/2906796/) | 1988 | Preclinical | Arch Int Pharmacodyn Ther | Demonstrates cytoprotective action against ethanol-induced gastric mucosal lesions, partly prostaglandin-mediated, distinct from acid suppression |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Preclinical | J Pharm Pharmacol | Rat stress-ulcer model: MX1 (roxatidine-bismuth-citrate complex) showed enhanced gastroprotection vs. equimolar roxatidine alone |

---

## India Market Information

Roxatidine acetate is currently **not marketed** in India (0 registrations on file); no authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are currently unavailable — flagged as a **Blocking** data gap, see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The efficacy evidence for roxatidine acetate in active peptic ulcer disease is strong (L1 — multiple completed RCTs plus a substantial supporting literature base spanning three decades), and the mechanism is well-established rather than speculative. However, this drug is unregistered in India/Taiwan and **safety labeling data (warnings, contraindications) is entirely missing (DG001, Blocking severity)** — this must be resolved before any S1 safety evaluation or market submission can proceed. Lower-ranked predicted indications (gastrojejunal ulcer, peptic ulcer perforation, gastroduodenitis, duodenogastric reflux, duodenal obstruction) are all L5 (model-prediction only, no supporting evidence) and are recommended for **Hold** — several (e.g., perforation, structural obstruction) are mechanistically inappropriate for an antisecretory agent and should be deprioritized or excluded from further evaluation.

**To proceed, the following is needed:**
- Official product label / package insert (warnings, contraindications, DDI) — source: regulatory agency label database (Blocking, per DG001)
- Formal DrugBank MOA record to replace literature-derived mechanism summary (DG002)
- Confirmation of dosage form and route availability for the local market
- If pursuing India market entry: full CDSCO registration dossier referencing the existing global RCT evidence base for peptic ulcer disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

