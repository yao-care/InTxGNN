---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nizatidine: From Established H2-Antagonist Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist; detailed original-indication and regulatory data are not available in this evidence pack, and the drug is currently **not marketed in Taiwan**. The TxGNN model's top prediction is **Active Peptic Ulcer Disease**, which — importantly — appears to be the drug's own well-established core indication for this class rather than a genuinely novel target, supported by **0 clinical trials** and **19 publications** (including 4 completed RCTs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no Taiwan license record; DrugBank indication text not retrieved) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in this pack). Based on the information that is available, Nizatidine is a **histamine H2-receptor antagonist** that inhibits basal, nocturnal, and stimulated gastric acid secretion by blocking histamine's action on parietal cells — the standard pharmacological mechanism underlying acid-suppressive therapy for peptic ulcer disease.

The evidence pack's own rationale for this prediction is explicit and important: it states that acid suppression via H2-antagonism is the "core, already-established indication" for this drug class, and that this candidate is "not a repurposing signal in the typical sense." In other words, the model has correctly re-identified the drug's known pharmacology rather than surfaced a genuinely new therapeutic use. This is a useful validation signal for the TxGNN model's accuracy, but it should not be read as a novel repurposing opportunity.

For context, several other lower-ranked candidates in this pack (e.g., gastroduodenitis, L2 evidence; gastrojejunal ulcer, L3 evidence) sit closer to genuine extrapolation — acid-related mucosal injury outside the classic duodenal/gastric ulcer population — and may be more informative if the goal is to find an actual new indication rather than confirm the existing one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled RCT: nizatidine 150mg BID healed active duodenal ulcers over 4–8 weeks |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicenter RCT: nizatidine 150mg BID or 300mg qHS vs placebo healed active benign gastric ulcer |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | 1-year maintenance RCT (n=513): nizatidine 150mg qHS cut duodenal ulcer recurrence to 34% vs 64% with placebo at 12 months |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepato-gastroenterology | 8-week RCT: nizatidine (150mg BID or 300mg qHS) comparable to ranitidine 150mg BID for gastric ulcer healing |
| [9198292](https://pubmed.ncbi.nlm.nih.gov/9198292/) | 1997 | RCT (combination therapy) | Chinese Medical Journal | Clarithromycin-based combination regimen for H. pylori eradication in peptic ulcer disease |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT / Mechanistic | Isr J Med Sci | Placebo-controlled RCT: nizatidine 300mg qHS promoted duodenal ulcer healing and altered mucosal inflammatory mediators |
| [15683433](https://pubmed.ncbi.nlm.nih.gov/15683433/) | 2005 | RCT | J Gastroenterol Hepatol | Multicenter RCT: nizatidine vs famotidine for maintenance therapy of erosive esophagitis |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Pharmacodynamic/pharmacokinetic review establishing nizatidine's role in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy for peptic ulcer disease, situating nizatidine among H2-antagonists |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Bailliere's Clin Gastroenterol | Review of gastric acid secretion pharmacology (histamine/gastrin/acetylcholine pathways) |

---

## India Market Information

Currently no registrations recorded (market status: Not Marketed; total registrations: 0)

---

## Safety Considerations

- **Drug Interactions**: 263 documented interactions on record. Two are rated **Major**: **Atazanavir** and **Dasatinib**. Several are rated **Moderate**, including a cluster of oral cephalosporins that may be affected by acid suppression (Cefditoren, Cefpodoxime, Cefuroxime), plus Acalabrutinib, Bosutinib, Brigatinib, Ceritinib, Chlorpropamide, and Dabrafenib/Dacomitinib. The remainder are rated Minor (e.g., Ketorolac, Ibuprofen, Diclofenac, Alendronic acid, Axitinib, Cyanocobalamin, Magnesium oxide, Oxaprozin).

No TFDA-sourced warnings or contraindications are available in this evidence pack (flagged as a Blocking data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction is backed by strong historical clinical evidence (4 completed RCTs, L1), but it represents the drug's already-established core H2-antagonist indication rather than a novel repurposing candidate — so the "new indication" framing needs to be qualified before any downstream use. Separately, a Blocking data gap (missing TFDA label warnings/contraindications) prevents a full safety assessment, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings, contraindications) to clear the Blocking gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A decision on whether this candidate is being pursued as a genuine repurposing opportunity or a market-entry case (since the predicted indication overlaps with known drug-class use)
- If genuine repurposing is the goal, prioritize review of the lower-confidence but more novel candidates in this pack (e.g., gastroduodenitis, L2; gastrojejunal ulcer, L3) instead of this top-ranked, non-novel result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

