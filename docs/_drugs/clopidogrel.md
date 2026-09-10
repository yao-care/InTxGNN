---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a P2Y12 receptor antagonist antiplatelet drug used for the prevention of atherothrombotic cardiovascular events. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, with **0 dedicated clinical trials** and **16 supporting publications**, though the underlying evidence base is drawn mainly from a related, broader population (PFO/atrial-septal-defect–associated migraine) rather than basilar-type migraine specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local market license data (drug not marketed). Pharmacologically, clopidogrel is an antiplatelet agent for prevention of atherothrombotic events (per mechanism described in evidence pack) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack ([Data Gap] flagged for MOA, DG002). Based on known information referenced in the evidence rationale, clopidogrel is a P2Y12 receptor antagonist antiplatelet drug, and its efficacy in preventing atherothrombotic events is well established.

The proposed link to migraine rests on a mechanistic hypothesis shared with the closely related prediction "migraine disorder" (rank 2): migraine with aura is strongly associated with patent foramen ovale (PFO)/right-to-left shunting, and microembolism through this shunt is thought to trigger cortical spreading depression that provokes migraine attacks. Antiplatelet therapy such as clopidogrel may reduce this embolic risk. Separately, mechanistic studies suggest P2Y12 receptors are involved in microglial activation in the trigeminal nucleus caudalis (PMID 31722730), hinting at a possible direct neural pathway in addition to the antiplatelet effect.

Importantly, the evidence pack itself flags a caveat: most supporting literature addresses "migraine with aura" broadly (often in the specific context of post-PFO/ASD-closure migraine), not the narrower, formally defined "migraine with brainstem aura" (basilar-type migraine). This suggests possible over-generalization from ontology mapping, and the strength of evidence for this specific subtype should be discounted accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

*(Note: For the closely related broader indication "migraine disorder," 8 clinical trials exist, including the completed Phase 4 CANOA trial (NCT00799045, n=220) and the ongoing Phase 3 SPRING trial (NCT04946734, n=440) — see repository notes for that indication.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: randomized trial of percutaneous PFO closure in migraine with aura refractory to medical treatment |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT | Cephalalgia | Pilot randomized controlled study of clopidogrel as prophylactic treatment for migraine |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Review | Headache | Systematic review on the role of antithrombotic drugs in migraine prevention |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Pilot Study | Neurology | TRACTOR pilot study: following observation that clopidogrel/prasugrel reduced migraine in PFO patients, tested ticagrelor as alternative |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Cohort | Neurology | Retrospective review of thienopyridine (clopidogrel-class) therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Cohort | Cephalalgia | Retrospective review of clopidogrel as primary therapy for migraineurs with right-to-left shunt lesions |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case Series | Journal of Interventional Cardiology | Intense migraines after percutaneous ASD closure; dramatic relief with 300mg clopidogrel in 5/13 patients |
| [17459082](https://pubmed.ncbi.nlm.nih.gov/17459082/) | 2007 | Case Series / Review | Cephalalgia | Migraine symptoms after percutaneous ASD closure in four pediatric cases, with literature review |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Case Series | Heart (British Cardiac Society) | Clopidogrel reduces migraine with aura after transcatheter closure of PFO/ASD |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Case Series | J Investig Med | Clopidogrel as effective complementary prophylactic for drug-refractory migraine with PFO |

---

## India Market Information

This drug currently has **0 registrations** on file and is **not marketed** locally per the available regulatory data — no license records to display.

---

## Safety Considerations

**Drug Interactions**: The evidence pack records **614 total interactions** on file for clopidogrel. Notable Major-severity interactions include:

| Interacting Drug | Level |
|------|------|
| Rabeprazole | Major |
| Omeprazole | Major |
| Esomeprazole | Major |
| Pioglitazone | Major |
| Repaglinide | Major |
| Loperamide | Major |

Moderate-severity interactions on file include Bupropion, Morphine, Acetylsalicylic acid, Cimetidine, Clarithromycin, Dexfenfluramine, Eluxadoline, Fenfluramine, Lansoprazole, Opium, Pantoprazole, and Sibutramine.

*(Note: Local label warnings and contraindications data are not available in this evidence pack — see Blocking data gap below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to "migraine with brainstem aura" consists only of literature (no dedicated clinical trials), and much of that literature actually studies a broader/different population (PFO- or ASD-closure–associated migraine with aura) rather than the formally defined basilar-type subtype — raising an ontology-mapping concern flagged directly in the evidence rationale. Combined with a Blocking data gap on local safety labeling (DG001), the initial safety screen (S1) cannot be completed, and the drug is not currently marketed locally.

**To proceed, the following is needed:**
- Local (TFDA-equivalent) label warnings and contraindications to clear the Blocking data gap (DG001)
- Detailed mechanism of action data to support the mechanistic rationale (DG002)
- Clarification of whether trial/literature evidence generalizes from broader migraine-with-aura/PFO populations to the specific "migraine with brainstem aura" phenotype
- A trial or registry specifically targeting basilar-type migraine, ideally independent of the ASD/PFO-closure context
- Assessment of local market entry pathway, since the drug currently has no registrations in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

