---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 2
---

# Ethanol
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

# Ethanol: From No Registered Therapeutic Indication to Migraine Disorder

## One-Sentence Summary

Ethanol (ethyl alcohol, DB00898) has no approved therapeutic indication on record in the evaluated regulatory registry, and is widely recognized as a general-purpose chemical compound rather than a targeted pharmaceutical agent.
The TxGNN model assigns it a high prediction score for **Migraine Disorder** (99.29%); however, all available mechanistic and epidemiological evidence consistently identifies ethanol as a **migraine trigger rather than a therapeutic intervention** — strongly suggesting this is a **false-positive prediction driven by knowledge graph co-occurrence bias**.
The full literature corpus of **20 publications** and **0 therapeutically relevant clinical trials** uniformly supports an adverse causal relationship, not a beneficial one.

---

## ⚠️ Critical Interpretation Alert

> **This prediction is a likely algorithmic false positive.** TxGNN's high score most likely reflects the strong co-occurrence link between "ethanol" and "migraine" in the biomedical knowledge graph — a relationship that is pathogenic (ethanol triggers migraine attacks), not therapeutic. No evidence supports ethanol as a treatment for migraine disorder. This report documents the evidence and formally recommends against repurposing development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indication on record |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 (mechanistic/preclinical studies only; no therapeutic trials) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data for ethanol as a therapeutic agent is not available in this evidence pack. Based on the mechanistic literature collected, ethanol is metabolized by alcohol dehydrogenase (ADH) to acetaldehyde, a reactive metabolite with well-characterized pro-nociceptive effects. A 2023 animal study (PMID 37101198) demonstrated that acetaldehyde activates TRPA1 channels on Schwann cells and stimulates release of calcitonin gene-related peptide (CGRP) — the central signaling molecule in migraine pathophysiology — triggering periorbital mechanical allodynia in mice. This is precisely the mechanism responsible for migraine *precipitation*, not relief.

The connection between ethanol and migraine in the biomedical literature is one of the most well-established trigger relationships in headache medicine. Multiple systematic reviews estimate that 30–50% of migraine patients identify alcohol as a migraine trigger, with red wine most frequently implicated. Epidemiological evidence further shows that genetic variants in the ADH2 gene (rs1229984) modulating acetaldehyde clearance efficiency are directly associated with migraine susceptibility (PMID 19486361), reinforcing that the ethanol–migraine link is biological and operates in the direction of harm.

The TxGNN score of 0.993 almost certainly reflects the density and strength of ethanol–migraine co-occurrence edges in the underlying knowledge graph, where a "drug–disease" edge was likely assigned irrespective of directionality. This is a known limitation of graph-based prediction models: they can score highly when a compound and a disease are strongly linked in the literature, even when the relationship is adverse rather than therapeutic. This candidate should be classified as a model artefact rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

No clinical trials testing **ethanol as a therapeutic intervention** for migraine disorder were identified. The 32 trials retrieved by the search engine were evaluated and found to have no direct therapeutic relevance to ethanol treatment of migraine (all rated Grade C). Representative trials are listed below to document the search results.

| Trial Number | Phase | Status | Enrollment | Context |
|-------------|-------|--------|------------|---------|
| [NCT07301008](https://clinicaltrials.gov/study/NCT07301008) | Phase 4 | Recruiting | 60 | Rimegepant for trigger-induced migraine; alcohol listed as one acceptable trigger — alcohol is the *exposure*, not the treatment |
| [NCT05175521](https://clinicaltrials.gov/study/NCT05175521) | N/A | Active, not recruiting | 50 | Inhaled **isopropyl** alcohol vapor vs. eucalyptus for migraine-associated nausea — a different molecule; not ethanol |
| [NCT01764685](https://clinicaltrials.gov/study/NCT01764685) | Phase 2 | Terminated (n=4) | 4 | Topiramate to reduce heavy drinking in HIV+ patients; terminated early, alcohol is the target *behavior*, not the therapy |
| [NCT05351086](https://clinicaltrials.gov/study/NCT05351086) | Phase 1 | Completed | 26 | PUR3100 formulation safety/PK study; not ethanol itself |
| [NCT05454826](https://clinicaltrials.gov/study/NCT05454826) | N/A | Completed | 26 | Cold application + relaxation exercises for migraine; no ethanol involvement |

> **Summary:** Zero clinical trials evaluate ethanol as a pharmacological treatment for migraine. The association in the knowledge graph does not translate to a therapeutic research programme.

---

## Literature Evidence

The literature corpus consistently characterizes ethanol as a **migraine trigger and adverse exposure factor**. Key publications are listed below, prioritized by study type and mechanistic relevance.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41305669](https://pubmed.ncbi.nlm.nih.gov/41305669/) | 2025 | Review | *Nutrients* | Comprehensive review of alcohol and primary headache: epidemiological data confirm association but no therapeutic role; pathophysiological mechanisms remain incompletely understood |
| [37612595](https://pubmed.ncbi.nlm.nih.gov/37612595/) | 2023 | Systematic Review & Meta-analysis | *J Headache Pain* | Meta-analysis of alcohol intake in migraine patients; confirms migraine patients consume less alcohol than controls (avoidance behaviour), reinforcing adverse relationship |
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | *Headache* | Narrative review of the complex alcohol–migraine relationship; concludes alcohol acts predominantly as a trigger, with red wine most implicated |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Mechanistic (Animal) | *J Biomed Sci* | **Key mechanistic study:** Acetaldehyde (ethanol metabolite) activates TRPA1/CGRP pathway in Schwann cells, producing periorbital allodynia — directly relevant to migraine pathogenesis but in an adverse direction |
| [18231712](https://pubmed.ncbi.nlm.nih.gov/18231712/) | 2008 | Review | *J Headache Pain* | MEDLINE review 1988–2007: ~1/3 of migraine patients report alcohol as trigger; proposes serotonin release and prostaglandin-mediated vasodilation as mechanisms |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetic Case-Control | *Headache* | ADH2 (rs1229984) genotype study: slower acetaldehyde metabolizers have significantly higher migraine susceptibility — causal adverse link confirmed |
| [8681169](https://pubmed.ncbi.nlm.nih.gov/8681169/) | 1996 | Review | *Rev Neurol* | Dietary triggers in migraine including alcoholic beverages; identifies physiological mechanisms of food/drink-induced attacks |
| [6352781](https://pubmed.ncbi.nlm.nih.gov/6352781/) | 1983 | Review | *J Am Diet Assoc* | Early systematic review of diet and migraine; alcohol identified as trigger factor in susceptible individuals |
| [6352219](https://pubmed.ncbi.nlm.nih.gov/6352219/) | 1983 | Mechanistic Review | *Drug Alcohol Depend* | Prostaglandin-mediated mechanisms in alcohol intolerance and hangover; relevant to understanding ethanol-induced headache biochemistry |
| [1495822](https://pubmed.ncbi.nlm.nih.gov/1495822/) | 1992 | Commentary | *Pathol Biol* | Critical analysis of migraine trigger methodology; challenges the evidence base for dietary triggers including alcohol, but does not propose therapeutic use |

---

## Safety Considerations

**Drug Interactions:** The DDI database identifies **471 known interactions** for ethanol. Key interactions of clinical concern include:

- **Major:** Eluxadoline — concurrent use is contraindicated; ethanol significantly increases the risk of pancreatitis with this IBS medication
- **Moderate (selected examples):** Acarbose, Acetohexamide, Albiglutide, Alogliptin, Canagliflozin, Chlorpropamide, Dapagliflozin, Dulaglutide, Empagliflozin — ethanol potentiates hypoglycaemic effects of antidiabetic agents and may mask hypoglycaemic symptoms; Acetylsalicylic acid — increased risk of GI bleeding; Atropine, Clidinium, Dicyclomine — additive CNS depression and anticholinergic effects; Bupropion — lowers seizure threshold; Dronabinol — additive CNS depression
- **Minor:** Doxycycline — ethanol accelerates doxycycline elimination; Cimetidine — inhibits alcohol dehydrogenase, increasing ethanol blood levels

For full prescribing warnings and contraindications, please refer to the package insert, as regulatory label data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ethanol is an established migraine **trigger**, not a therapeutic agent — its metabolite acetaldehyde activates the TRPA1/CGRP pathway to precipitate migraine attacks, and no clinical trial programme exists to evaluate it therapeutically. The TxGNN prediction score of 99.29% is almost certainly a false positive arising from the algorithm interpreting a strong adverse co-occurrence relationship as a drug–disease therapeutic link; this is a known limitation of knowledge graph-based models that do not encode relationship directionality.

**To formally close this candidate, the following should be documented:**

- [ ] Confirm the adverse directionality flag in the TxGNN candidate database to prevent re-surfacing in future runs
- [ ] Log this case as a model calibration example: high TxGNN score driven by trigger/adverse co-occurrence rather than therapeutic evidence
- [ ] No further clinical or regulatory investigation is warranted for ethanol as a migraine treatment
- [ ] If the investigative interest is in the ethanol–CGRP/TRPA1 pathway, re-frame as a **target biology study** rather than a repurposing candidate (e.g., acetaldehyde/TRPA1 inhibition as a novel anti-migraine target)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

