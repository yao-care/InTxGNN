---
layout: default
title: Galantamine
parent: Model Prediction Only (L5)
nav_order: 386
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Galantamine: predicted new indication Psychogenic movement disorders (evidence level L5). Approved use: Alzheimer disease"
monitor_inn: "Galantamine"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Galantamine: From Alzheimer Disease to Psychogenic Movement Disorders
{: .text-alpha }

## One-Sentence Summary

Galantamine is an acetylcholinesterase inhibitor originally used to treat Alzheimer disease.
The TxGNN model's top-ranked prediction is **psychogenic movement disorders**, which has **no clinical trials and no publications** behind it. The best-supported item among the nine predictions is the lower-ranked **lingual-facial-buccal dyskinesia** (tardive dyskinesia), which has **21 publications** (mostly indirect) but no registered trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer disease (the licence records list no approved indication text) |
| Predicted New Indication | Psychogenic movement disorders (rank 1) |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

Eight other predictions, all mainly movement disorders, scored 0.9971 to 0.9989. Only two have any literature: extrapyramidal and movement disease (L4, 4 publications) and lingual-facial-buccal dyskinesia (L4, 21 publications).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Galantamine is a known acetylcholinesterase inhibitor and a positive allosteric modulator of nicotinic receptors. Its efficacy in Alzheimer disease comes from boosting cholinergic signalling.

For **psychogenic movement disorders**, there is no established link between cholinergic mechanisms and the pathophysiology of functional movement disorders. The score is a TxGNN model (deep learning) prediction only.

The more plausible link is to **tardive dyskinesia and extrapyramidal disorders**. The striatum depends on a balance between cholinergic and dopaminergic signalling. Some researchers propose that tardive dyskinesia involves a cholinergic deficiency caused by antipsychotic damage to striatal cholinergic neurons. The evidence is mixed, though. A 2025 systematic review reports movement disorders as *adverse effects* of cholinesterase inhibitors in Alzheimer dementia, so the drug may carry a risk signal rather than a benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

## Literature Evidence

No literature was retrieved for the top-ranked prediction, psychogenic movement disorders. The tables below cover the two predictions that have literature, with the most relevant items selected.

**Lingual-facial-buccal dyskinesia (tardive dyskinesia)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17388711](https://pubmed.ncbi.nlm.nih.gov/17388711/) | 2007 | RCT (crossover) | J Clin Psychiatry | 30-week randomized, double-blind, placebo-controlled crossover trial of galantamine in tardive dyskinesia; the abstract provided does not state the results |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis | Prog Neuropsychopharmacol Biol Psychiatry | Meta-analysis of RCTs of cholinergic drugs, galantamine among them, for neuroleptic-induced tardive dyskinesia |
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane systematic review | Cochrane Database Syst Rev | Cholinergic medication for antipsychotic-induced tardive dyskinesia (class-level, not galantamine-specific) |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier version of the Cochrane review on cholinergic drugs for tardive dyskinesia |
| [23897874](https://pubmed.ncbi.nlm.nih.gov/23897874/) | 2013 | Guideline | Neurology | American Academy of Neurology evidence-based guideline on treating tardive syndromes |
| [25734590](https://pubmed.ncbi.nlm.nih.gov/25734590/) | 2015 | Cochrane review | Cochrane Database Syst Rev | Cholinesterase inhibitors for rarer dementias (e.g. Huntington's disease, progressive supranuclear palsy) |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | Pharmacovigilance study | Pharmacotherapy | Reports on cholinesterase inhibitors and Pisa syndrome (a dystonia), a safety signal |
| [25850380](https://pubmed.ncbi.nlm.nih.gov/25850380/) | 2015 | Preclinical (mouse) | J Pharmacol Sci | Interaction of donepezil and galantamine with antipsychotics on extrapyramidal side effects |
| [18938211](https://pubmed.ncbi.nlm.nih.gov/18938211/) | 2008 | Preclinical (rat) | Neurosci Lett | Galantamine reduced striatal degeneration in a Huntington's disease model |

**Extrapyramidal and movement disease**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic review | Brain Circ | Reviews movement disorders associated with acetylcholinesterase inhibitors (including galantamine) in Alzheimer dementia, a risk signal rather than a benefit |
| [20701827](https://pubmed.ncbi.nlm.nih.gov/20701827/) | 2011 | Preclinical (animal) | Int J Neuropsychopharmacol | Adjunct galantamine with risperidone or haloperidol in animal models of antipsychotic activity and extrapyramidal side-effect liability |
| [17374745](https://pubmed.ncbi.nlm.nih.gov/17374745/) | 2007 | Preclinical (monkey) | J Pharmacol Exp Ther | Galantamine inhibited amphetamine-induced psychotic-like behaviour in Cebus monkeys |
| [14676467](https://pubmed.ncbi.nlm.nih.gov/14676467/) | 2004 | Review | Dement Geriatr Cogn Disord | Pharmacologic treatment expectations in dementia with Lewy bodies |

Note: the Cochrane reviews cover cholinergic drugs as a class, so whether galantamine was studied and what the conclusions were needs to be checked in the full texts. The one galantamine-specific RCT (17388711) lacks reported results in the data compiled for this report.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 95138 | Galamer 8 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |
| 94579 | Galamer 4 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |
| 96956 | Galamer OD 4mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |

All three registrations are valid single-ingredient oral products.

## Safety Considerations

- **Contraindications and cautions from the knowledge graph (not label text):** familial long QT syndrome, atrioventricular block, liver failure and liver disease, kidney disease, epilepsy, asthma (including intrinsic and allergic), chronic obstructive pulmonary disease, peptic and duodenal ulcer disease, gallbladder disease, bladder neck obstruction and pyoureter.
- **Drug Interactions:** 173 interactions were identified. One is rated Major: **bupropion**. The ones shown below are rated Moderate, and the full list is longer.
  - Acid reducers: famotidine, ranitidine, cimetidine
  - Anticholinergics and antispasmodics: atropine, dicyclomine, hyoscyamine, glycopyrronium, clidinium, trospium
  - Antibiotics: clarithromycin, metronidazole
  - QT-relevant or antiemetic agents: dolasetron, palonosetron, eliglustat
  - Others: loperamide, lorcaserin, picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate
- **Prediction-specific concerns:**
  - Cholinesterase inhibition may aggravate peptic ulcer disease, which matters for the tremor-nystagmus-duodenal ulcer syndrome prediction.
  - Galantamine is metabolized by CYP2D6 and CYP3A4. Porphyrinogenic safety would need review before any use in acute intermittent porphyria.
  - Cholinesterase inhibitors have been linked to movement disorders, including Pisa syndrome.

Please refer to the package insert for label warnings, as none were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, psychogenic movement disorders, rests on the model score alone: there are no trials, no literature and no plausible mechanism. The tardive dyskinesia direction has a more plausible cholinergic rationale and one galantamine RCT, but the evidence is indirect and mixed, and cholinesterase inhibitors may themselves cause movement disorders.

**To proceed, the following is needed:**
- Full-text review of the 2007 galantamine tardive dyskinesia crossover trial (PMID 17388711) and of the Cochrane reviews, to see whether galantamine showed any benefit
- Package insert warnings and contraindications from the India registrations (currently missing, and blocking safety screening)
- Mechanism of action data (currently unavailable)
- An assessment of whether the risk signal for drug-induced movement disorders outweighs any benefit
- Route compatibility checks, which are still pending for all predictions (only oral tablets are currently registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

