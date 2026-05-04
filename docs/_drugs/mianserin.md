---
layout: default
title: Mianserin
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 7
---

# Mianserin
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

# Mianserin: From Major Depressive Disorder to Neurotic Depression

## One-Sentence Summary

Mianserin is a tetracyclic antidepressant used in the treatment of major depressive disorder, operating through presynaptic α2-adrenergic antagonism and multi-serotonin receptor blockade to enhance noradrenaline and serotonin neurotransmission. The TxGNN model identifies **Neurotic Depression** (the highest-evidence prediction among 7 candidates) as the most clinically supported repurposing direction, backed by **0 registered clinical trials** but **20 publications** — including multiple randomized controlled trials directly evaluating Mianserin in depression with anxiety features.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder |
| Predicted New Indication | Neurotic Depression |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## All TxGNN Predicted Indications (Summary)

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Benign Paroxysmal Torticollis of Infancy | 99.49% | L5 | Hold |
| 2 | Dysthymic Disorder | 99.45% | L5 | Hold |
| 3 | Agoraphobia | 99.40% | L4 | Hold |
| 4 | Ohdo Syndrome and Variants | 99.23% | L5 | Hold |
| 5 | Melancholia | 99.17% | L3 | Research Question |
| **6** | **Neurotic Depression** | **99.16%** | **L3** | **Research Question** |
| 7 | Neurotic Disorder | 99.02% | L3 | Research Question |

> **Note on top-ranked prediction:** Benign Paroxysmal Torticollis of Infancy (rank 1) has the highest TxGNN score but zero supporting evidence and no plausible mechanistic connection — the prediction likely reflects knowledge graph topological proximity among neurological disease nodes rather than true pharmacological relevance. Neurotic depression (rank 6) is featured as the primary focus of this report due to its strongest mechanistic rationale and richest evidence base.

---

## Why is This Prediction Reasonable?

Mianserin is a tetracyclic antidepressant that acts primarily by blocking presynaptic α2-adrenergic autoreceptors and heteroreceptors, thereby disinhibiting noradrenaline (NE) and serotonin (5-HT) release from presynaptic terminals. It simultaneously antagonizes postsynaptic 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6, and 5-HT7 receptors, as well as α1A, α1B, and α1D adrenoceptors, and inhibits the norepinephrine transporter (NET). This multi-receptor profile — increasing NE/5-HT availability while blunting potentially adverse serotonin receptor subtypes — is pharmacologically nearly identical to its structural successor, mirtazapine, which is currently in widespread clinical use.

Neurotic depression (corresponding broadly to DSM-5 persistent depressive disorder or mild-to-moderate major depressive disorder with prominent anxiety features) is pathophysiologically characterized by chronic monoamine insufficiency, heightened hypothalamic-pituitary-adrenal (HPA) axis reactivity, and significant autonomic dysregulation — all targets addressable by Mianserin's mechanism. The α2 antagonism-driven NE enhancement addresses the core monoamine deficit; 5-HT2C and histamine H1 blockade provide secondary anxiolytic and sedative effects particularly relevant to the anxiety component; and α1-adrenoceptor blockade may modulate autonomic symptoms such as tension headaches and vegetative crises.

Historically, the clinical trial literature from the 1980s used this exact patient phenotype — outpatient depression with anxiety features — as the primary study population for Mianserin. Multiple double-blind randomized controlled trials (PMID 2864794, PMID 6824555, PMID 1806624) compared Mianserin directly against other antidepressants in this population, establishing a direct evidence base that goes beyond mechanistic inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for neurotic depression.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2864794](https://pubmed.ncbi.nlm.nih.gov/2864794/) | 1985 | Double-blind Multicenter RCT | Acta Psychiatrica Scandinavica Suppl. | Mianserin (60 mg) vs. nomifensine in 61 depressive outpatients with anxiety features; no significant efficacy difference between arms; confirms Mianserin's antidepressant activity in this population |
| [6824555](https://pubmed.ncbi.nlm.nih.gov/6824555/) | 1983 | RCT | British Journal of Clinical Pharmacology | Mianserin vs. doxepin in 60 outpatients with depression and anxiety across two centres; both drugs showed substantial improvement on Hamilton scores; no consistent efficacy difference; Mianserin showed a distinct tolerability profile |
| [1806624](https://pubmed.ncbi.nlm.nih.gov/1806624/) | 1991 | Double-blind RCT | International Clinical Psychopharmacology | Mianserin (60–90 mg/day) vs. maprotiline (100–150 mg/day) in 317 DSM-III major depressive outpatients; significant improvement in both arms; direct large-sample Mianserin evidence |
| [2530770](https://pubmed.ncbi.nlm.nih.gov/2530770/) | 1989 | Double-blind Multicenter RCT | Acta Psychiatrica Scandinavica Suppl. | Paroxetine vs. Mianserin in depression; direct head-to-head comparison providing insight into Mianserin's efficacy profile |
| [7048075](https://pubmed.ncbi.nlm.nih.gov/7048075/) | 1982 | Review | Modern Problems of Pharmacopsychiatry | Comprehensive early review of Mianserin pharmacology and clinical evidence across multiple depression types; foundational reference for the drug's therapeutic use |
| [40616802](https://pubmed.ncbi.nlm.nih.gov/40616802/) | 2025 | Review | Prilozi (Macedonian Academy of Sciences) | Treatment-resistant depression: highlights combining SSRIs with α2-autoreceptor antagonists such as Mianserin and Mirtazapine as an evidence-based strategy; reaffirms Mianserin's continued mechanistic relevance |
| [6686702](https://pubmed.ncbi.nlm.nih.gov/6686702/) | 1983 | Single-blind Study | Progress in Neuro-Psychopharmacology & Biological Psychiatry | Single-blind open study of Mianserin in inpatients with DSM-III major depression; significant Hamilton score reduction (p < 0.001); explored plasma-level/response relationship |
| [1454971](https://pubmed.ncbi.nlm.nih.gov/1454971/) | 1992 | Double-blind Placebo-controlled Trial | Psychotherapy and Psychosomatics | Mianserin vs. placebo in chronic idiopathic pain as "masked depression"; tests the hypothesis that chronic pain may represent a depressive equivalent; direct Mianserin placebo-controlled evidence |
| [3863468](https://pubmed.ncbi.nlm.nih.gov/3863468/) | 1985 | Open Pilot Study | Acta Psychiatrica Scandinavica Suppl. | Open study of Mianserin (1 mg/kg/day) in 110 depressed children and adolescents aged 8–19; improvement apparent from end of week 1; only study evaluating Mianserin in pediatric depression |
| [9090572](https://pubmed.ncbi.nlm.nih.gov/9090572/) | 1997 | Review | Journal of Clinical Psychopharmacology | Mechanistic review of NE-5-HT interactions in depression; provides theoretical grounding for α2-antagonist antidepressants including Mianserin and mirtazapine |

---

## India Market Information

Mianserin is currently **not marketed in India**. There are no CDSCO-registered product licenses on record. The drug is marketed in certain European countries (e.g., UK as Norval/Bolvidon, Netherlands as Tolvon) and may require import authorization or new drug application procedures for India use.

---

## Safety Considerations

**Pharmacological Target Interactions (from receptor binding data):**

Mianserin has documented activity at 11 receptor/transporter targets with clinical relevance to its safety profile:

| Target | Gene | Species | Clinical Implication |
|--------|------|---------|----------------------|
| 5-HT2A receptor | HTR2A | Human | Antagonism reduces adverse serotonin effects; may contribute to antipsychotic-like properties |
| 5-HT2B receptor | HTR2B | Human | 5-HT2B blockade; relevant to cardiovascular monitoring |
| 5-HT2C receptor | HTR2C | Human | Blockade contributes to anxiolytic and appetite-stimulating effects (weight gain risk) |
| 5-HT6 receptor | HTR6 | Human | Cognitive modulation |
| 5-HT7 receptor | HTR7 | Human | Mood and circadian rhythm modulation; sleep effects |
| α1A-adrenoceptor | ADRA1A | Human | Postural hypotension risk; dizziness on standing |
| α1B-adrenoceptor | ADRA1B | Human | Cardiovascular effects |
| α1D-adrenoceptor | ADRA1D | Human | Peripheral vascular effects |
| LPA1 receptor | LPAR1 | Human | Lysophosphatidic acid signaling; emerging relevance |
| NET (Norepinephrine Transporter) | Slc6a2 | Rat | NE reuptake inhibition; NE enhancement mechanism |
| 5-HT1B receptor | Htr1b | Mouse | Serotonin autoreceptor modulation |

For complete warnings, contraindications, and drug-drug interaction details, please refer to the package insert from a country where Mianserin is currently marketed (e.g., UK Summary of Product Characteristics). Formal CDSCO prescribing information is not available as the drug is not marketed in India.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Mianserin has a well-established antidepressant mechanism and historical RCT evidence base in neurotic/anxiety-type depression, making it biologically plausible for further investigation in neurotic depression subtypes. However, with no registered clinical trials in the target indication and a not-marketed status in India, the path to clinical application requires regulatory and strategic groundwork before commitment.

**To proceed, the following is needed:**

- **MOA documentation:** Obtain full pharmacological profile from DrugBank API (DG002) and recent literature to characterize the α2/5-HT mechanism in detail for regulatory submissions
- **Package insert safety data:** Download the UK or EU Summary of Product Characteristics (SPC) to extract formal contraindications and warnings (DG001 critical gap — Blocking severity)
- **India regulatory pathway:** Assess CDSCO requirements for new drug approval or import license for a drug not currently marketed in India
- **Systematic literature review:** Commission a formal meta-analysis specifically on Mianserin (not mirtazapine) in neurotic depression subtypes to quantify effect size vs. current standard of care
- **Differentiation analysis:** Evaluate whether Mianserin offers advantages over its successor mirtazapine (already widely available), particularly in populations requiring specific receptor profiles or different tolerability characteristics
- **Evidence gap for aligned predictions:** Melancholia (rank 5) and Neurotic Disorder (rank 7) share overlapping evidence and should be co-evaluated as secondary research questions in the same protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

