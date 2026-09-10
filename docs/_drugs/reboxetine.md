---
layout: default
title: Reboxetine
parent: 僅模型預測 (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
---

# Reboxetine
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

Using the report structure to synthesize this multi-candidate evidence pack. Note: `predicted_indications[0]` (benign paroxysmal torticollis of infancy) is a pure TxGNN topology artifact with zero supporting evidence — I'm leading with the best-evidenced candidate (dysthymic disorder, L2) instead, and flagging the mechanistically implausible top-ranked hits separately, since presenting rank-1 as the headline would be misleading.

---

# Reboxetine: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

> Reboxetine is a selective norepinephrine reuptake inhibitor (NRI) originally developed and approved (e.g., UK, 1997) for major depressive disorder, with off-label use in panic disorder.
> Among 10 TxGNN-predicted indications, **Dysthymic Disorder** has the strongest supporting evidence — **9 publications** including placebo-controlled RCT meta-analyses — while the model's single highest-scoring prediction (benign paroxysmal torticollis of infancy) has **no clinical trials, no literature, and no plausible mechanism**, and should be disregarded.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (per DrugBank pharmacology `clinical_use`: also used for panic disorder, ADHD; not formally in `taiwan_regulatory`) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

### All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Benign paroxysmal torticollis of infancy | 99.92% | L5 | Hold – no mechanistic link |
| 2 | Agoraphobia | 99.91% | L3 | Research Question |
| 3 | **Dysthymic disorder** | 99.87% | **L2** | Research Question |
| 4 | Ohdo syndrome and variants | 99.76% | L5 | Hold – no mechanistic link |
| 5 | Melancholia | 99.74% | L2 | Research Question (efficacy controversial) |
| 6 | Neurotic depression | 99.74% | L2 | Research Question (overlaps with #5) |
| 7 | Blepharophimosis–intellectual disability syndrome, Ohdo type | 99.70% | L5 | Hold – no mechanistic link |
| 8 | Neurotic disorder | 99.66% | L5 | Hold – no evidence |
| 9 | Keppen-Lubinsky syndrome | 99.54% | L5 | Hold – no mechanistic link |
| 10 | Ligneous conjunctivitis | 99.40% | L5 | Hold – no mechanistic link |

Five of the ten predictions (ranks 1, 4, 7, 9, 10) are rare genetic syndromes with no plausible pharmacological connection to a norepinephrine reuptake inhibitor — these are graph-topology artifacts of the TxGNN model and are not clinically actionable.

---

## Why is This Prediction Reasonable?

Reboxetine is a highly selective norepinephrine transporter (NET/SLC6A2) inhibitor with low affinity for serotonin or dopamine transporters and negligible affinity for other CNS receptors (confirmed via DrugBank pharmacology data: target NET, human SLC6A2, CAS 71620-89-8). It was the first selective NRI brought to market, approved in the UK in 1997 as Edronax® for acute and maintenance treatment of major depressive illness.

Dysthymic disorder (persistent depressive disorder) sits on the same depressive spectrum as major depressive disorder and shares the underlying monoamine-deficiency pathophysiology that reboxetine's original indication targets. This is not merely theoretical: reboxetine's original clinical development program directly included dysthymic patients — the pivotal review by Burrows et al. (1998, PMID 9818623) explicitly evaluated reboxetine across "major depressive disorders and dysthymia" using pooled data from 8 placebo/active-controlled and 4 open-label trials (n=690).

The five rare-syndrome predictions (torticollis, Ohdo syndrome, Keppen-Lubinsky syndrome, blepharophimosis–ID syndrome, ligneous conjunctivitis) have no shared pathway with NET inhibition — these are genetic/structural conditions (e.g., KAT6A/KAT6B, KCNJ6, plasminogen deficiency) and the high TxGNN scores reflect graph embedding proximity, not biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dysthymic Disorder specifically (or for any of the 10 predicted indications — the evidence pack contains no `clinicaltrials.gov` or ICTRP entries across all candidates).

---

## Literature Evidence

*(Dysthymic Disorder — highest evidence-level candidate)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis (placebo-controlled RCTs) | J Clin Psychiatry | Antidepressants show significant efficacy vs. placebo in dysthymic disorder, comparable response pattern to MDD |
| [10628889](https://pubmed.ncbi.nlm.nih.gov/10628889/) | 1999 | Double-blind RCT (vs. imipramine) | J Affect Disord | Reboxetine vs. imipramine in elderly depressive patients; comparable efficacy with better tolerability profile |
| [9818623](https://pubmed.ncbi.nlm.nih.gov/9818623/) | 1998 | RCT review (8 controlled + 4 open trials, n=690) | J Clin Psychiatry | Reboxetine effective and well-tolerated for major depressive disorder and dysthymia, short- and long-term |
| [10984724](https://pubmed.ncbi.nlm.nih.gov/10984724/) | 2000 | Open-label long-term study | Int J Geriatr Psychiatry | Reboxetine maintenance therapy in 160 elderly patients with MDD or dysthymia; effective and well-tolerated |
| [10616869](https://pubmed.ncbi.nlm.nih.gov/10616869/) | 1999 | Pilot study | J Geriatr Psychiatry Neurol | Reboxetine titrated to 8mg/day in elderly depressed/dysthymic patients; tolerability assessed |
| [15183602](https://pubmed.ncbi.nlm.nih.gov/15183602/) | 2004 | Open-label adjunct study | J Affect Disord | Reboxetine as add-on therapy for partial/non-responders to prior antidepressants |
| [15358987](https://pubmed.ncbi.nlm.nih.gov/15358987/) | 2004 | Physiological/sleep study | J Psychopharmacol | Reboxetine's effect on sleep architecture and nocturnal cardiac autonomic activity in 12 dysthymic patients |
| [10839469](https://pubmed.ncbi.nlm.nih.gov/10839469/) | 2000 | Pharmacokinetic study | Int J Clin Pharmacol Ther | PK characterization of reboxetine in elderly depressive patients |
| [21057421](https://pubmed.ncbi.nlm.nih.gov/21057421/) | 2010 | Mechanistic/lab study | Psychiatria Danubina | NK cell cytotoxicity differences between major depression and dysthymia |

**Note on secondary candidates (Melancholia / Neurotic Depression, L2):** these share largely overlapping literature with dysthymia but efficacy is more contested — the 2018 Cipriani et al. network meta-analysis (PMID 29477251, Lancet) ranked reboxetine among the less-favorable antidepressants for efficacy, and a dedicated systematic review (Eyding et al. 2010, BMJ, PMID 20940209) raised significant publication-bias concerns specific to reboxetine's depression trial data. Treat these two as the same underlying question as dysthymia rather than independent new indications.

---

## India Market Information

Reboxetine currently has **no registered products** (`market_status`: Not marketed, `total_licenses`: 0). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No usable warnings, contraindications, or drug-drug interaction data are currently available. The single `safety.ddi` entry describes reboxetine's own pharmacological target — NET/SLC6A2 — rather than an interacting drug, and is not a genuine interaction record.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking** data gap (DG001: missing India/local label warnings and contraindications) prevents any S1 safety assessment, regardless of indication.
- Reboxetine has **zero market presence locally** (0 registrations), adding regulatory/access barriers.
- Even the best-evidenced candidate (dysthymic disorder, L2) rests on trials designed for the original MDD indication rather than dysthymia-specific confirmatory studies, and closely related candidates (melancholia, neurotic depression) carry documented efficacy/publication-bias controversy.
- 5 of 10 TxGNN predictions are mechanistically implausible rare-disease matches and should not be pursued.

**To proceed, the following is needed:**
- Resolve DG001: obtain official product label (warnings, contraindications) from the relevant regulatory source before any S1 safety evaluation.
- Resolve DG002: confirm detailed MOA documentation beyond DDI-derived pharmacology data.
- If pursuing dysthymic disorder specifically, commission or identify a dysthymia-specific RCT rather than relying on pooled MDD/dysthymia trial data.
- Reassess reboxetine's controversial efficacy profile (publication bias, Cipriani ranking) before allocating further resources to the depression-spectrum candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

