---
layout: default
title: Terfenadine
parent: 僅模型預測 (L5)
nav_order: 815
evidence_level: L5
indication_count: 5
---

# Terfenadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Terfenadine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

> Terfenadine is a second-generation H1-antihistamine historically used for allergic rhinitis and chronic urticaria, though it is not currently marketed in India and was withdrawn in many markets due to cardiac safety concerns.
> The TxGNN model predicts it may be effective for **Allergic Urticaria**,
> with **0 clinical trials** and **19 publications** currently supporting this direction — most of which describe the drug class rather than terfenadine specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the India regulatory dataset (no licenses on file); historically, terfenadine was developed for seasonal allergic rhinitis and chronic idiopathic urticaria before being superseded by its active metabolite, fexofenadine |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, terfenadine is a second-generation H1-histamine receptor antagonist, and H1-antagonism is the standard mechanism underlying treatment of urticaria (histamine-mediated mast cell degranulation drives wheal-and-flare reactions). Its efficacy for urticaria-type conditions has been established for this drug class, and mechanistically the same pathway is plausible for allergic urticaria.

However, this is essentially a **class-effect prediction rather than a drug-specific finding**. Of the 19 supporting publications, the large majority describe fexofenadine, cetirizine, loratadine, or other successor antihistamines rather than terfenadine itself — several explicitly note that fexofenadine ("the active metabolite of terfenadine") was developed specifically to retain the antihistamine efficacy of terfenadine while removing its cardiotoxic liability. Only one identified study (PMID 8828024) directly compares terfenadine against placebo in chronic idiopathic urticaria.

Importantly, terfenadine's own DDI profile (292 recorded interactions, including multiple **Major**-severity interactions with CYP3A4 inhibitors such as clarithromycin, cimetidine, and miconazole) reflects the well-documented risk of QT-interval prolongation and torsades de pointes that led to its withdrawal or restriction in many jurisdictions. This safety history is the direct reason the drug class evolved toward fexofenadine, and it substantially weakens the case for repurposing terfenadine itself, as opposed to a safer successor molecule.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8828024](https://pubmed.ncbi.nlm.nih.gov/8828024/) | 1996 | RCT | Drugs | Double-blind multicentre trial: ebastine vs. terfenadine vs. placebo in chronic idiopathic urticaria over 3 months; both active drugs significantly outperformed placebo |
| [25097491](https://pubmed.ncbi.nlm.nih.gov/25097491/) | 2014 | Review | Postepy Dermatol Alergol | Reviews antihistamine cardiovascular safety; specifically notes terfenadine and astemizole were withdrawn due to QT prolongation and cardiotoxicity |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines (including terfenadine) for allergic conditions |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics/dynamics of desloratadine, fexofenadine, levocetirizine — successors developed from terfenadine's mechanism |
| [39028636](https://pubmed.ncbi.nlm.nih.gov/39028636/) | 2024 | Review | Curr Med Res Opin | Systematic review of fexofenadine (terfenadine's active metabolite) as non-sedating, non-cardiotoxic antihistamine |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | Discusses how to select optimal H1-antihistamine for chronic spontaneous urticaria |
| [18020585](https://pubmed.ncbi.nlm.nih.gov/18020585/) | 1998 | Review | BioDrugs | Reviews mizolastine efficacy vs. other second-generation antihistamines in chronic idiopathic urticaria |
| [8808167](https://pubmed.ncbi.nlm.nih.gov/8808167/) | 1996 | Review | Drugs | Ebastine review; contextualizes efficacy against terfenadine in allergic disorders |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Overview of urticaria pathophysiology; nonsedating antihistamines described as mainstay treatment for chronic idiopathic urticaria |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine review; efficacy in chronic urticaria found similar to terfenadine |

---

## India Market Information

No registrations found. Terfenadine is currently **not marketed** in India (total licenses: 0), so no authorization records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 292 total interactions recorded in the database (20 detailed here). Notable **Major**-severity interactions include: Clarithromycin, Cimetidine, Miconazole, Aprepitant, Dolasetron, Picosulfuric acid, Sodium sulfate, and Polyethylene glycol (3350 with electrolytes) — several of these (clarithromycin, cimetidine, miconazole) are CYP3A4 inhibitors/substrates, consistent with terfenadine's known risk of elevated plasma levels leading to QT prolongation. **Moderate**-severity interactions include Famotidine, Loperamide, Bisacodyl, Eliglustat, Eluxadoline, Levofloxacin, Lactitol, Lactulose, Ondansetron, and Palonosetron.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for terfenadine specifically (as opposed to its successor fexofenadine or the antihistamine class generally) is weak — only one direct RCT (PMID 8828024) and no active clinical trials support this indication. Combined with terfenadine's well-documented cardiotoxicity risk (major CYP3A4-related DDIs) and its absence from the India market, the evidence does not currently support advancing this candidate.

**To proceed, the following is needed:**
- Regulatory safety labeling data (TFDA/CDSCO package insert warnings and contraindications) — flagged as a **Blocking** data gap (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Terfenadine-specific efficacy evidence in urticaria distinguishable from class-effect literature
- A formal cardiac safety (QTc) monitoring plan given the drug's known arrhythmia risk profile
- Assessment of India market entry feasibility, given zero current registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

