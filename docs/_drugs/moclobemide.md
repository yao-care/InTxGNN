---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 2
---

# Moclobemide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible inhibitor of monoamine oxidase A (RIMA), originally used for the treatment of depression and social anxiety disorder.
The TxGNN model predicts it may be effective for **Agoraphobia**,
with **0 registered clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Depression and social anxiety disorder |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Moclobemide is a reversible and selective inhibitor of monoamine oxidase A (RIMA). By selectively blocking MAO-A, it prevents the enzymatic breakdown of serotonin (5-HT) and norepinephrine (NE), leading to elevated synaptic concentrations of these monoamines. Its pharmacological profile is confirmed by its known binding targets, MAOA (gene ID 4128) and MAOB (gene ID 4129), which are central to monoaminergic neurotransmission. Compared to classical irreversible MAOIs, moclobemide carries a substantially lower risk of tyramine-related hypertensive reactions due to its reversibility.

Agoraphobia is closely intertwined with panic disorder: the core pathology involves conditioned avoidance behaviours learned after recurrent panic attacks, driven by hyperactivation of the amygdala and dysregulation of the 5-HT/NE systems. By elevating synaptic 5-HT and NE, moclobemide can suppress amygdala overactivation and weaken fear-conditioned learning circuits — the precise mechanism underlying agoraphobic avoidance. This is not merely theoretical: the classical irreversible MAOI phenelzine has established efficacy in agoraphobia and panic disorder, and moclobemide, as a RIMA, represents a safer successor along the same mechanistic pathway.

The overlap between moclobemide's approved indications (depression, social anxiety) and agoraphobia is substantial. All three conditions share dysregulation of the serotonergic and noradrenergic systems, and treatment guidelines for anxiety spectrum disorders (including panic disorder/agoraphobia) already recommend both SSRIs and MAOIs as pharmacological options. The TxGNN prediction score of 99.43% reflects this high degree of mechanistic and nosological adjacency.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | British Journal of Psychiatry | Randomised placebo-controlled trial of moclobemide, CBT, and their combination in panic disorder with agoraphobia; assessed relative efficacy of pharmacological vs. psychological treatments |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | Active-controlled RCT | European Archives of Psychiatry and Clinical Neuroscience | Multicentre double-blind RCT comparing moclobemide 450 mg/day vs. clomipramine 150 mg/day in 135 patients with DSM-III-R panic disorder with/without agoraphobia; established non-inferiority |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Narrative Review | Dialogues in Clinical Neuroscience | Guideline-based treatment recommendations for anxiety disorders including panic disorder/agoraphobia; reviews evidence for pharmacotherapy including MAOIs |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Narrative Review | Advances in Experimental Medicine and Biology | Comprehensive psychopharmacological treatment review for panic disorder/agoraphobia, GAD, and SAD based on meta-analyses of RCTs; includes RIMA as treatment option |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Clinical Trial | Clinical Neuropharmacology | Randomised double-blind 8-week trial comparing brofaromine vs. clomipramine in panic disorder; discusses class efficacy of reversible MAO-A inhibitors including moclobemide |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Neuroimaging Study | Metabolic Brain Disease | SPECT neuroimaging study comparing moclobemide vs. citalopram effects on resting brain perfusion in social anxiety disorder; provides mechanistic insight into RIMA brain activity |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatrica Scandinavica (Suppl) | Meta-analysis and review of RIMA class (brofaromine, moclobemide, toloxatone); demonstrated consistent antidepressant and anxiolytic activity of moclobemide vs. multiple comparators |
| [1498904](https://pubmed.ncbi.nlm.nih.gov/1498904/) | 1992 | Early Phase Trial | Clinical Neuropharmacology | Early clinical evidence supporting reversible MAO-A inhibitors in panic disorder |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatrica Scandinavica (Suppl) | Review of MAOI efficacy in panic disorder with agoraphobia, social phobia, PTSD, and related disorders based on controlled studies |
| [7892341](https://pubmed.ncbi.nlm.nih.gov/7892341/) | 1995 | Case Report | Psychiatrische Praxis | Treatment-refractory panic disorder with agoraphobia resolved with combined imipramine + moclobemide + behaviour therapy; demonstrates utility in complex, refractory cases |

---

## India Market Information

Moclobemide currently has **no registered products** in the Indian market. No license data is available.

---

## Safety Considerations

**Pharmacological Targets (from interaction database):**
- Moclobemide acts on **Monoamine Oxidase A** (MAOA, ENSG00000189221) and shows secondary activity at **Monoamine Oxidase B** (MAOB, ENSG00000069535), both in human tissue.
- These interactions reflect the drug's primary mechanism; no drug-drug interaction alerts were flagged beyond these pharmacological targets (total DDI count = 2).

Please refer to the package insert for complete warnings, contraindications, and clinical safety information, as full label data was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two RCTs (1999) directly examined moclobemide in panic disorder with agoraphobia and demonstrated efficacy, and the mechanistic basis — reversible MAO-A inhibition elevating synaptic 5-HT/NE with resultant suppression of amygdala-driven fear conditioning — is well-established. However, moclobemide is not currently marketed in India, and full safety label data is unavailable, requiring additional regulatory and clinical review before any application.

**To proceed, the following is needed:**

- **MOA documentation**: Obtain full mechanism of action data from DrugBank API or published pharmacology references to complete the mechanistic analysis
- **Safety label review**: Download and parse the official package insert (SmPC or equivalent) to extract contraindications, key warnings (including tyramine interaction thresholds), and special population guidance
- **Regulatory pathway assessment**: Evaluate the pathway for market authorisation or compassionate use in India (CDSCO), given zero existing registrations
- **Updated clinical trial search**: Broaden the search to include panic disorder (with agoraphobia as a subtype) on ClinicalTrials.gov and ICTRP to identify any more recent trials that may have been missed
- **Head-to-head comparison with current standard of care**: Compare moclobemide's evidence profile against first-line agents (SSRIs/SNRIs) currently available in India for contextualising the clinical value proposition
- **Drug interaction profile expansion**: Conduct a full DDI screen beyond pharmacological targets, particularly for serotonergic combinations and adrenergic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

