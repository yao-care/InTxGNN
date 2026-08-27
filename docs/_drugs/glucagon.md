---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glucagon: From Hypoglycemia Management to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon (DB00040) is the endogenous pancreatic hormone conventionally used as emergency treatment for severe hypoglycemia and as a GI-motility-suppressing diagnostic aid; it is **not currently marketed in Taiwan**. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, with **11 clinical trials** and **20 publications** retrieved — however, nearly all of this evidence actually tests **GLP-1 receptor agonists** (a related but distinct drug class), not Glucagon itself, so the strength of support for Glucagon specifically is much weaker than the raw counts suggest.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (original_indications and MOA are data gaps). Glucagon's established clinical use — emergency treatment of severe hypoglycemia and suppression of GI motility for diagnostic imaging — is general pharmacology knowledge, not sourced from this dossier |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 (preclinical/mechanism studies; no completed RCT of Glucagon itself in IBS) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Glucagon (DB00040) is currently a **data gap**, and no original indication is recorded in this evidence pack. What can be said from general pharmacology knowledge is that Glucagon is the mature peptide product of the *proglucagon* (GCG) gene, secreted by pancreatic alpha cells, and acts as insulin's physiological counter-regulator to raise blood glucose; it is also used clinically to transiently relax GI smooth muscle for endoscopic/radiologic procedures.

**Important caveat on this prediction's basis**: the TxGNN score (0.992) appears to be driven largely by knowledge-graph proximity — Glucagon and Glucagon-Like Peptide-1 (GLP-1) are both cleavage products of the same *proglucagon* precursor gene, so they sit close together in the graph even though they act on different receptors (glucagon receptor vs. GLP-1 receptor) with largely opposite metabolic effects. Consistent with this, essentially all of the retrieved clinical trials and literature test **GLP-1 receptor agonists** (liraglutide, exendin-4, native GLP-1, and the GLP-1 analog ROSE-010) for their effects on gut motility and visceral pain in IBS — not Glucagon itself. This is flagged explicitly in the underlying analysis as a possible **target confound**: the graph signal may reflect GLP-1 pharmacology rather than any direct action of Glucagon on IBS. Without confirmed MOA data for Glucagon and without any study that actually tests Glucagon (rather than its gene-family relative) in IBS patients, mechanistic applicability to Glucagon specifically cannot be established from the current evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | Tested ROSE-010 (a GLP-1 analog, not Glucagon) on GI motor function in constipation-predominant IBS (IBS-C) women; hypothesized delayed gastric emptying without slowing colonic transit |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Compared native GLP-1 with its analog ROSE-010 on inhibition of prandial upper-GI motility in humans; mechanism study, not a Glucagon trial |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated (n=8) | 8 | Liraglutide (GLP-1 receptor agonist) vs. placebo for chronic high bowel frequency after ileal pouch-anal anastomosis; terminated early |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Mechanistic study of butyrate (a microbial metabolite) in the human colon, linked to IBS via loss of colonic butyrate; no drug intervention |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Prevalence of idiopathic reactive hypoglycemia and effect of fructo-oligosaccharide supplementation on glucose variability; indirect relevance via glycemic regulation only |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Establishes small-intestinal human organoid models to test nutrient antigens/therapeutic agents; basic research tool, not a drug trial |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Gut-microbiota-targeted nutritional intervention (fiber/polyphenol blend) for GI barrier integrity under hypoxia; no drug tested |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Whole-grain rye bread's effect on gut-microbiota-brain axis and gut peptide release in healthy subjects; dietary intervention only |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise intensity's effect on gut dysbiosis and GLP-1 hormone levels in pre-diabetic, obese IBS patients; lifestyle intervention, not a drug trial |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Effect of eating rate of ultra-processed foods on dietary intake and metabolic response; dietary behavior study, unrelated to Glucagon |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Review (systematic review/meta-analysis) | Frontiers in Endocrinology | GLP-1 and its analog ROSE-010 inhibit the migrating motor complex and decrease GI motility in IBS patients; evidence is for GLP-1 receptor agonists, not Glucagon |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Reviews the role of L-cell-derived GLP-1 in IBS pathophysiology (gut neuron sensitization, motility); focused on the GLP-1 axis |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT (cross-analysis) | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1 receptor agonist) reduced pain during IBS attacks; identifies subpopulations most responsive to treatment |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Pending classification | Clinics and Research in Hepatology and Gastroenterology | Decreased serum GLP-1 correlates with abdominal pain in constipation-predominant IBS; colonic GLP-1 receptor expression assessed |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Pending classification | Neurogastroenterology and Motility | Exendin-4 (GLP-1 receptor agonist) improved GI dysfunction in a rat model of IBS; animal mechanism study |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Review | The Journal of Headache and Pain | Reviews GLP-1's broader roles (insulin secretion, glucagon inhibition, gastric emptying) and its emerging relevance to pain/headache disorders |
| [24605036](https://pubmed.ncbi.nlm.nih.gov/24605036/) | 2014 | Pending classification | World Journal of Gastroenterology | Characterizes ileal endocrine cell types (including GLP-1-secreting L-cells) in IBS patients |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Annals of Gastroenterology | Real-world prescription/discontinuation patterns of GLP-1 receptor agonists among IBS patients, noting GI adverse effects |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews novel investigational drugs for constipation-predominant IBS, including GLP-1-pathway agents |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | Reviews IBS treatments beyond fiber/antispasmodics, including 5-HT agents and emerging drug classes |

---

## Taiwan Market Information

Glucagon (DB00040) currently has **no marketing authorization records in Taiwan** (`total_licenses: 0`, `market_status: 未上市`). No product listings, dosage forms, or approved-indication text are available to summarize.

---

## Safety Considerations

**Drug Interactions**: 25 interactions on record, all classified as **Minor** severity (source: DDInter). The interacting drugs are predominantly **beta-blockers** (e.g., Propranolol, Metoprolol, Atenolol, Bisoprolol, Carvedilol, Nadolol, Sotalol, Esmolol, Labetalol, Pindolol, Acebutolol, and several ophthalmic beta-blockers such as Timolol, Betaxolol, Carteolol, Levobunolol, Metipranolol), plus **Warfarin**. These interactions generally relate to blunted counter-regulatory glycemic response and altered anticoagulant effect; all are rated Minor.

Key warnings and contraindications are not available in this evidence pack — please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is confounded — almost every retrieved clinical trial and publication tests GLP-1 receptor agonists (a related but pharmacologically distinct product of the same proglucagon gene), not Glucagon itself. Combined with the missing MOA data, absent original indication, and the drug's unmarketed status in Taiwan, there is currently no direct evidence that Glucagon (as opposed to GLP-1) has efficacy in IBS.

**To proceed, the following is needed:**
- Resolve **DG002 (High severity)**: obtain Glucagon's confirmed mechanism of action from DrugBank to properly assess mechanistic relevance to IBS
- Resolve **DG001 (Blocking severity)**: obtain TFDA label warnings/contraindications before any safety pre-assessment (S1) can proceed
- Clarify whether the TxGNN prediction reflects true Glucagon pharmacology or a graph-proximity artifact from the shared proglucagon/GCG gene node (target confound check)
- Identify or commission preclinical/clinical evidence testing **Glucagon itself** (not GLP-1 analogs) in IBS models
- Confirm Taiwan regulatory pathway, since the drug currently holds no local marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

