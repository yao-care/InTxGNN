---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acetylsalicylic Acid (Aspirin): From Cardiovascular Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (Aspirin, DB00945) is one of the world's most widely used drugs, classically indicated for analgesia, antipyresis, anti-inflammation, and antiplatelet-mediated cardiovascular protection.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, with **0 clinical trials** and **19 publications** currently supporting this direction.
The overall evidence is rated **L3**, based on retrospective studies and reviews; targeted prospective research is needed before any clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, anti-inflammation, and cardiovascular prevention (antiplatelet); no India regulatory record in dataset |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the automated regulatory database query for this candidate. Based on established pharmacological knowledge, Aspirin irreversibly acetylates cyclooxygenase-1 (COX-1) at the Ser529 residue, permanently blocking platelet thromboxane A2 (TXA2) biosynthesis for the entire platelet lifespan (~7–10 days). Aspirin also inhibits COX-2 at higher doses, reducing prostaglandin synthesis and mediating its analgesic and anti-inflammatory effects across tissues.

Migraine with brainstem aura (formerly "basilar-type migraine") is a distinct ICHD-III subtype characterized by neurological symptoms referable to the brainstem — including dysarthria, vertigo, tinnitus, diplopia, and ataxia — before the headache phase. The mechanistic link to Aspirin runs through two complementary pathways: (1) Cortical spreading depression (CSD), the electrophysiological correlate of aura, is associated with platelet activation and TXA2-mediated vasoconstriction particularly in the posterior circulation; Aspirin's antiplatelet action may interrupt this vascular cascade. (2) Neurogenic inflammation in the trigeminovascular system, driven partly by prostaglandins, amplifies pain signaling; Aspirin's COX inhibition may dampen this trigeminal sensitization.

However, brainstem aura is a rare and clinically distinct subtype, and virtually all existing clinical evidence pertains to "migraine with aura" as a broader category. A retrospective study (PMID 25729594) demonstrated prophylactic benefit of low-dose Aspirin in migraine with aura broadly, and a 2025 systematic review (PMID 39989443) specifically assessed antithrombotic drugs in migraine prevention. No RCT has been conducted specifically enrolling brainstem aura patients. The TxGNN high prediction score (99.94%) likely reflects topological proximity in the disease knowledge graph between aura-type migraine and brainstem aura, rather than direct clinical data — warranting cautious interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Aspirin in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | Double-blind RCT | Cephalalgia | 278 acute migraine patients (with or without aura) randomized to IV lysine acetylsalicylate 1.8 g vs subcutaneous sumatriptan 6 mg vs placebo; both active agents were superior to placebo, establishing Aspirin's acute efficacy in migraine |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Study | Current Health Sciences Journal | 203 migraine-with-aura patients (ICHD-II); 46.8% received low-dose ASA for prophylaxis over ≥4 months — demonstrates real-world feasibility and tolerability of Aspirin in aura-type migraine prevention |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | First systematic review specifically examining the role of antithrombotic drugs (including Aspirin) as migraine preventive medication; evaluates mechanistic plausibility and the available clinical evidence base |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment / Guideline | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies; Aspirin and aspirin-combination products receive Level A evidence for mild-to-moderate migraine attacks |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Guideline | FP Essentials | AHA/ASA primary stroke prevention guidelines classify migraine with aura as an independent vascular risk factor; directly relevant context given brainstem aura's posterior circulation involvement and elevated stroke risk |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Comprehensive review of migraine with aura covering CSD mechanism and ICHD-III diagnostic criteria; provides the pathophysiological framework underpinning Aspirin's plausible anti-CSD mechanism |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Systematic comparison of migraine with and without aura: distinct vascular risk profiles, pathophysiology, and management implications — supports a differentiated therapeutic approach for aura-type migraine |
| [2701286](https://pubmed.ncbi.nlm.nih.gov/2701286/) | 1989 | Review | Biomedicine & Pharmacotherapy | Foundational 10-year review of the platelet hypothesis of migraine; presents evidence that primary platelet abnormalities (excess TXA2, abnormal serotonin uptake) contribute to migraine attacks — core mechanistic rationale for Aspirin's antiplatelet approach |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: multicentre RCT of percutaneous PFO closure vs medical management (including antiplatelet agents) in patients with refractory migraine with aura — demonstrates vascular-cardiac pathophysiology in aura-type migraine and the relevance of antiplatelet therapy |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart | Clopidogrel (an antiplatelet agent of a different drug class) reduced migraine-with-aura frequency after transcatheter closure of PFO and ASD — supports a class-level antiplatelet mechanism effect applicable to Aspirin in aura-type migraine |

---

## Safety Considerations

**Drug Interactions (657 interactions identified):**

The most clinically significant interactions are listed below:

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|--------------------|
| Acalabrutinib | Major | Enhanced hemorrhagic risk; concurrent use should be avoided |
| Acetazolamide | Major | Risk of salicylate toxicity due to increased renal reabsorption |
| Ketorolac | Major | Additive GI toxicity and bleeding risk; combination contraindicated |
| Fondaparinux | Major | Additive bleeding risk; monitor closely if combined |
| Trastuzumab emtansine | Major | Significantly enhanced hemorrhagic adverse events |
| Ibuprofen | Major | Ibuprofen competitively antagonizes Aspirin's antiplatelet effect at COX-1; avoid concurrent use in cardiovascular protection settings |
| Abciximab | Moderate | Additive antiplatelet effects; bleeding risk increased |
| Ethanol | Moderate | Increased gastrointestinal bleeding risk |
| Fluvoxamine | Moderate | Enhanced bleeding risk via serotonin-mediated platelet inhibition |
| Hydrocortisone | Moderate | Reduced Aspirin efficacy; additive GI mucosal injury |

A total of **657 drug-drug interactions** have been identified in the DDInter database. Key warnings and contraindications data were not retrievable from this dataset — please refer to the current approved package insert for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Aspirin in migraine with brainstem aura is biologically plausible — antiplatelet suppression of TXA2-mediated posterior circulation vasospasm and anti-neuroinflammatory effects on the trigeminovascular system both provide a credible rationale. However, no clinical trials exist for this specific ICHD-III subtype, and available evidence (L3) derives entirely from broader aura-type migraine populations or indirect mechanistic studies. The clinical distinction between general migraine with aura and the brainstem aura subtype is important and not bridged by current evidence.

**To proceed, the following is needed:**
- Design a prospective pilot cohort or crossover study specifically enrolling patients with confirmed migraine with brainstem aura (ICHD-III criterion 1.2.2), with Aspirin as prophylactic intervention
- Retrieve complete MOA data from the DrugBank API (DB00945) and regulatory package inserts to address current data gaps before mechanism-based claims are formalized
- Obtain full safety profile (key warnings, contraindications) from the package insert; this is a Blocking data gap that must be resolved before any S1 safety pre-assessment
- Evaluate bleeding risk in the target population — particularly in women of reproductive age, where Aspirin use during pregnancy requires careful monitoring
- Assess whether evidence from the 2025 antithrombotic systematic review (PMID 39989443) and the retrospective aura study (PMID 25729594) can support a formal research protocol for the brainstem aura subtype, potentially through collaboration with neurology headache centers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

