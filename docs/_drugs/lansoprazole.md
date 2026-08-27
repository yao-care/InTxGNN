---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

# Lansoprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI) widely used for treating acid-related gastrointestinal disorders, including peptic ulcer disease, gastroesophageal reflux disease (GERD), *Helicobacter pylori* eradication, and Zollinger-Ellison syndrome. The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, with **0 clinical trials** and **2 publications** currently supporting this direction. However, one of these publications is an animal study raising a concerning safety signal — Lansoprazole may actually promote gastric carcinogenesis in the context of duodenogastric reflux, which significantly tempers the initial prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease, GERD, *H. pylori* eradication, Zollinger-Ellison syndrome |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on known pharmacological information, Lansoprazole is a proton pump inhibitor (PPI) that irreversibly blocks the H⁺/K⁺-ATPase enzyme on the gastric parietal cell — the final step in gastric acid secretion. This mechanism is well-established, making it effective for any condition driven by excessive or harmful gastric acid.

Duodenogastric reflux (DGR) involves the retrograde movement of duodenal contents — including bile acids, pancreatic enzymes, and intestinal fluid — back into the stomach. While DGR does expose the gastric mucosa to a mixed, partially acidic refluxate, the primary pathogenic drivers are **bile acids and pancreatic fluid, not gastric acid itself**. Theoretically, Lansoprazole could reduce the acidic component of the refluxate and offer some mucosal protection; however, it cannot address the mechanical or bile-driven pathology that characterises DGR. This makes the mechanistic link indirect and incomplete.

More importantly, the available preclinical evidence raises a red flag. A rat model study (PMID 15052437) found that Lansoprazole may **promote gastric carcinogenesis** in the presence of DGR, potentially through hypergastrinaemia and mucosal hyperproliferation. This reverses the expected benefit and makes this TxGNN prediction particularly difficult to advance without substantial further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lansoprazole in duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Narrative Review | European Journal of Clinical Pharmacology | Comprehensive update on PPI clinical use and pharmacokinetics; confirms Lansoprazole and other PPIs as first-line therapy for peptic ulcer, GERD, *H. pylori*, NSAID-induced GI lesions, and Zollinger-Ellison syndrome — contextualises the drug's established mechanism |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal Study (Rat Model) | Gastric Cancer | Lansoprazole promoted gastric carcinogenesis in rats with surgically induced duodenogastric reflux; suggests that acid suppression in a DGR environment may paradoxically increase cancer risk, possibly via elevated gastrin and mucosal hyperproliferation — a critical safety signal |

---

## India Market Information

Lansoprazole is currently **not registered** in India. No licensed products are available in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | — | — | No registrations on record |

---

## Safety Considerations

**Drug Interactions**: Lansoprazole has **618 documented drug interactions** in the DDInter database. The most clinically significant are listed below:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Acalabrutinib | **Major** | Lansoprazole raises gastric pH, substantially reducing Acalabrutinib oral absorption and efficacy |
| Atazanavir | **Major** | PPI-mediated pH elevation markedly reduces Atazanavir bioavailability; co-administration is generally contraindicated |
| Apalutamide | Moderate | May alter Lansoprazole exposure via CYP induction |
| Aprepitant | Moderate | Possible CYP3A4-mediated interaction |
| Bosutinib | Moderate | Reduced Bosutinib absorption at higher gastric pH |
| Brigatinib | Moderate | Possible pH-dependent absorption reduction |
| Bromocriptine | Moderate | Possible interaction |
| Amphotericin B | Moderate | Possible interaction |
| Hydrochlorothiazide | Moderate | Possible interaction |
| Atorvastatin | Moderate | Possible CYP-mediated interaction |

> Please refer to the full package insert for complete warnings and contraindications, which could not be retrieved in this data collection cycle.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Lansoprazole in duodenogastric reflux is limited to one animal study and a general PPI review — with zero registered clinical trials. More critically, the only directly relevant preclinical study found a harmful signal: Lansoprazole may **increase gastric carcinogenesis risk** in the DGR environment rather than providing benefit. Until this safety concern is resolved with human-level evidence, proceeding with development is not justified.

**To proceed, the following is needed:**

- **Safety data**: Obtain the full package insert (CDSCO/TFDA) to extract approved warnings and contraindications (currently a blocking data gap)
- **MOA clarification**: Retrieve Lansoprazole mechanism of action from DrugBank to better assess mechanistic overlap with DGR pathophysiology
- **Human-level evidence**: Search for any observational studies, systematic reviews, or clinical trial sub-analyses examining Lansoprazole specifically in DGR patients
- **Carcinogenesis risk resolution**: Commission or identify studies that specifically address whether the rat-model carcinogenesis signal (PMID 15052437) translates to humans — this is the primary decision gate
- **Indication scope clarification**: Determine whether the target is DGR as a primary indication or as an adjunct condition managed alongside another pathology (e.g., peptic ulcer, post-surgical reflux)
- **India regulatory pathway**: If evidence becomes favourable, assess the India registration pathway given zero current market presence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

