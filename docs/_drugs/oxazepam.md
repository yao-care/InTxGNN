---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

# Oxazepam: From Benzodiazepine Anxiolytic/Sedative Use to Insomnia

## One-Sentence Summary

Oxazepam is a short/intermediate-acting benzodiazepine; a formal registered original indication was not available in this evidence pack (India/Taiwan market status: not marketed), but its established pharmacological class is anxiolytic/sedative-hypnotic. The TxGNN model predicts it may be effective for **Insomnia**, with **0 registered clinical trials** and **11 supporting publications** (including 2 RCTs) currently identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (no India/Taiwan license on file); pharmacologically classified as a benzodiazepine anxiolytic/sedative-hypnotic |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 (literature-based: RCTs, cohort studies, and reviews; no registered clinical trials) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Oxazepam is a benzodiazepine that acts at the benzodiazepine binding site on the GABA-A receptor chloride channel, potentiating GABAergic inhibitory neurotransmission. This produces sedative, anxiolytic, and muscle-relaxant effects — a well-characterized sedative-hypnotic mechanism.

Detailed original-indication registry data was not available in this evidence pack (the drug is not currently marketed in India/Taiwan, and 0 licenses are on file), so the original-to-new indication relationship cannot be drawn from regulatory label text. However, based on its known drug class, oxazepam's core pharmacological action — GABA-A receptor potentiation — is the direct pharmacological basis for hypnotic/sleep-promoting effects. This is consistent with decades of clinical use of benzodiazepines as sleep aids, including direct comparative data (e.g., a 1984 nighttime/daytime efficacy comparison of oxazepam versus flurazepam in chronic insomnia).

Because GABA-A agonism is the established mechanistic pathway for insomnia treatment (rather than an indirect or inferential link), the TxGNN score of 99.86% aligns well with known pharmacology. What remains incomplete is indication-specific registrational evidence: no clinical trials formally studying oxazepam for an insomnia indication are currently registered, and product label safety data (warnings/contraindications) is a blocking data gap.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | The American Journal of Psychiatry | In 14 chronic insomnia patients, both oxazepam and flurazepam improved polysomnographic sleep measures; flurazepam caused substantial daytime sleepiness while oxazepam did not, though oxazepam produced some rebound effects |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | The Annals of Pharmacotherapy | Randomized comparison of melatonin vs. oxazepam for anxiety/sleep quality in STEMI patients post-PCI; benzodiazepines effective but with adverse-effect and interaction concerns |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Cohort | Archives of Gerontology and Geriatrics | Study of 60 elderly insomnia patients with comorbidities (depression, dementia, behavioral disturbances) evaluating hypnotic drug effectiveness and safety |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Cohort | JAMA | Withdrawal syndrome observed after substituting a short-acting benzodiazepine (oxazepam) for long-term diazepam use, persisting over a month |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Cohort | PeerJ | Analysis of factors (age, sex, depression, comorbidity) associated with long-term benzodiazepine/z-drug use in older populations |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | Journal of Clinical and Experimental Hepatology | Review of alcohol withdrawal syndrome management, where insomnia is a core symptom addressed with sedative-hypnotics in alcoholic liver disease patients |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review | Psychiatrische Praxis | Cross-sectional review of behavioral/psychological symptoms of dementia (BPSD) management practice, including benzodiazepine/sedative use |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Review of anxiolytic drug pharmacokinetics, relevant to benzodiazepine class dosing and sedative effects |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Review of paroxetine pharmacology in panic disorder, contextualizing benzodiazepine alternatives for anxiety-related sleep disturbance |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case Report | American Journal of Translational Research | Case report of a sensory adverse effect with agomelatine, included as related sedative/sleep-agent safety literature |

## India Market Information

Oxazepam is not currently registered or marketed in India (0 authorizations on file).

## Safety Considerations

- **Drug Interactions**: A DDI query returned 163 total interactions (sample of 20 detailed below). Notable interactions include:
  - **Major**: Morphine, Morphine (liposomal) — increased CNS/respiratory depression risk
  - **Moderate**: Bupropion, Dronabinol, Nabilone, Metoclopramide, Opium, Sibutramine, Teduglutide
  - **Minor**: Magnesium oxide, Calcium carbonate, Magnesium carbonate, Magnesium hydroxide, Aluminum hydroxide, Magaldrate (antacids — absorption effects)
  - **Unknown/unclassified**: Calcitriol, Glimepiride, Mesalazine, Doxycycline, Clotrimazole

No product label warnings or contraindications data was available in this evidence pack; please refer to the official package insert once obtained.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link (GABA-A receptor potentiation → sedative-hypnotic effect) is direct and well-established, and literature evidence (including 2 RCTs and multiple cohort studies) supports oxazepam's sleep-promoting effects. However, no registered clinical trials specifically target an insomnia indication, the drug is not currently marketed in India (0 licenses), and official warnings/contraindications data is a blocking gap (DG001) that prevents a complete S1 safety assessment.

**To proceed, the following is needed:**
- Official package insert / label data for warnings and contraindications (blocking gap DG001)
- Confirmed original indication and detailed MOA from an authoritative source such as DrugBank (gap DG002)
- Assessment of whether a dedicated Phase 2/3 RCT for insomnia is warranted, given existing evidence is largely older or indirect
- Monitoring protocol addressing major DDIs (notably opioids — Major-level interaction with Morphine) given likely polypharmacy in the target insomnia population (e.g., elderly patients)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

