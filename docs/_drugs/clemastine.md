---
layout: default
title: Clemastine
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 6
---

# Clemastine
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

# Clemastine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Clemastine is a first-generation H1-antihistamine traditionally used to control allergic rhinitis and related allergic symptoms. The TxGNN model's top-ranked prediction reinforces its effectiveness for **Allergic Urticaria**, supported by **0 clinical trials** and **13 publications**, though the underlying mechanism is a well-established antihistamine effect rather than a truly novel repurposing pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack's regulatory dataset (Clemastine is a classical first-generation H1-antihistamine used for allergic rhinitis and related allergic conditions) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Clemastine is not available in the evidence pack (flagged as a High-severity data gap). Based on generally known pharmacology, Clemastine is an ethanolamine-derivative, first-generation H1-receptor antagonist. It blocks histamine-mediated vasodilation, increased vascular permeability, and pruritus caused by mast cell/basophil degranulation — the core pathological mechanism underlying urticaria.

It is important to note that this is not a novel disease-category jump: allergic urticaria has long been one of the classical, standard indications for antihistamines like clemastine (marketed historically as Tavegyl). The TxGNN prediction here largely **reconfirms an existing, well-characterized pharmacological effect** rather than proposing a mechanistically unexpected new use. This is reflected in the supporting literature, which is dominated by comparative reviews of other antihistamines (loratadine, astemizole, acrivastine) using clemastine as a benchmark comparator, plus a small number of clemastine-specific clinical reports.

By contrast, the model's lower-ranked predictions (e.g., cold urticaria at rank 2, evidence level L3) extend into more specific subtypes with thinner direct evidence, and the remaining candidates (nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness) have no supporting trials or literature at all (evidence level L5) and are not recommended for further action at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6119852](https://pubmed.ncbi.nlm.nih.gov/6119852/) | 1981 | Comparative Cohort | Wisconsin Medical Journal | Direct patient evaluation of clemastine fumarate compared with other antihistamines (highest-tier clemastine-specific evidence in this set) |
| [40055203](https://pubmed.ncbi.nlm.nih.gov/40055203/) | 2025 | Review | Naunyn-Schmiedeberg's Arch Pharmacol | Patent-landscape review (2015-2024) confirming clemastine's traditional role in allergic rhinitis/urticaria and noting emerging non-antihistaminergic applications |
| [4152119](https://pubmed.ncbi.nlm.nih.gov/4152119/) | 1971 | Clinical Report | Therapia Hungarica | Early clinical introduction of clemastine (Tavegyl) for allergic diseases including urticaria |
| [6230808](https://pubmed.ncbi.nlm.nih.gov/6230808/) | 1984 | Case Report | Vestnik Dermatologii i Venerologii | Documents an allergic reaction to Tavegyl (clemastine) itself — relevant safety signal |
| [19739446](https://pubmed.ncbi.nlm.nih.gov/19739446/) | 2009 | Commentary | Läkartidningen | Notes that documentation for acute clemastine (Tavegyl) treatment is limited, highlighting an evidence gap |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine review reporting clemastine as similarly effective to comparator antihistamines in chronic urticaria and allergic rhinitis |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort | Asian Pac J Allergy Immunol | Epidemiological study of urticaria in Thai children, providing disease background context |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine review listing clemastine among antihistamines with demonstrated efficacy in urticaria |
| [2523301](https://pubmed.ncbi.nlm.nih.gov/2523301/) | 1989 | Review | Drugs | Loratadine review confirming clemastine's established efficacy in chronic urticaria |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Z Hautkrankheiten | Global astemizole trial review using clemastine as a classical comparator in chronic urticaria |

---

## India Market Information

Clemastine currently has no registered products in India (0 licenses on record; market status: Not Marketed). No authorization data is available to tabulate.

---

## Safety Considerations

**Drug Interactions**: The DDI database records 297 total documented interactions for Clemastine. Representative interactions include:

- **Major**: Potassium citrate, Potassium chloride (anticholinergic slowing of GI transit may increase risk of mucosal irritation from oral potassium salts)
- **Moderate**: Multiple opioids and anticholinergic/antimuscarinic agents — Hyoscyamine, Loperamide, Morphine (including liposomal), Atropine, Glycopyrronium (systemic and topical), Clidinium, Dicyclomine, Dronabinol, Eluxadoline, Mepenzolate, Methscopolamine, Metoclopramide, Nabilone, Opium, Propantheline, Scopolamine — generally reflecting additive anticholinergic effects and/or additive CNS/GI depression

Detailed key warnings and contraindications are not available in the current evidence pack (flagged as a Blocking-severity data gap); please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis is strong and well-precedented — clemastine's H1-antagonism is a textbook mechanism for treating urticaria — but this is confirmatory rather than novel, no dedicated clinical trials exist for this indication, and critical safety documentation (TFDA/CDSCO label warnings and contraindications) is currently a blocking data gap. Combined with the drug's non-marketed status in India, guardrails are warranted before any indication-expansion or market-entry action.

**To proceed, the following is needed:**
- Official India (CDSCO) package insert/label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action documentation from DrugBank or equivalent source (DG002, High)
- Assessment of whether India market entry/registration is planned or feasible, given current "Not Marketed" status
- If pursuing further, a targeted literature/trial search specifically on clemastine efficacy in urticaria (rather than as a comparator in other antihistamines' trials) to strengthen the evidence level beyond L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

