---
layout: default
title: Cisapride
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 5
---

# Cisapride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cisapride: From Gastroparesis / GERD to Peptic Ulcer Perforation

## One-Sentence Summary

Cisapride is a gastrointestinal prokinetic agent historically used for gastroesophageal reflux disease (GERD), gastroparesis, functional dyspepsia, and chronic intestinal motility disorders.
The TxGNN model predicts it may have activity against **Peptic Ulcer Perforation** with a score of **99.94%**, yet only **0 clinical trials** and **2 publications** are available to support this direction — and mechanistic analysis indicates this prediction is most likely a knowledge graph artifact rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | GERD, gastroparesis, functional dyspepsia (no India regulatory license on file) |
| Predicted New Indication | Peptic Ulcer Perforation |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on information extracted from the supporting literature (PMID 8527013, 7510617), Cisapride is a substituted benzamide prokinetic agent that enhances gastrointestinal motility by facilitating acetylcholine release from myenteric nerves — primarily via 5-HT₄ receptor agonism. Its proven clinical roles include accelerating gastric emptying, increasing lower esophageal sphincter (LES) pressure, improving antroduodenal coordination, and reducing duodenogastric bile reflux.

Peptic ulcer perforation, however, is a surgical emergency defined by full-thickness disruption of the gastrointestinal wall leading to peritoneal contamination. The pathological mechanism is completely distinct from the motility disorders for which Cisapride provides benefit. Prokinetic agents are widely regarded as relatively contraindicated in the context of an acute perforation: accelerating intestinal propulsion can worsen peritoneal contamination, mask localizing symptoms, and delay definitive surgical intervention.

The TxGNN model's very high score (0.9994) for this indication most likely reflects topological proximity within the gastrointestinal disease cluster of the knowledge graph, not a real therapeutic relationship. The 2 retrieved publications are general GI disease reviews and do not contain data specifically linking Cisapride to peptic ulcer perforation. This prediction is assessed as a **false positive**, and the mechanistic link is explicitly negative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18097282](https://pubmed.ncbi.nlm.nih.gov/18097282/) | 2008 | Review / Case Series | J Clin Gastroenterology | Reviews GI involvement in progressive systemic sclerosis; notes delayed gastric emptying in 10–75% of patients and mentions prokinetic management; no data on peptic ulcer perforation |
| [8931825](https://pubmed.ncbi.nlm.nih.gov/8931825/) | 1996 | Review | Am J Health-Syst Pharm | Describes GERD pathophysiology and cost-effective treatment selection; references Cisapride as prokinetic option; no specific data on perforation |

---

## India Market Information

Cisapride is **not currently registered or marketed in India**. No authorisation records are available in the regulatory database. The drug was withdrawn from most major markets (including the United States in 2000) due to serious cardiac arrhythmia risks (QT prolongation / torsades de pointes) associated with CYP3A4 drug interactions.

---

## Safety Considerations

**Drug Interactions**: Cisapride has **302 documented drug–drug interactions** (source: DDInter). This extensive interaction profile is the primary reason for global market withdrawal and constitutes the most critical safety signal for any repurposing consideration. Key interactions are summarised below:

| Severity | Interacting Drug | Clinical Concern |
|----------|----------------|-----------------|
| **Major** | Amiodarone | Additive QT prolongation; high risk of torsades de pointes |
| **Major** | Amitriptyline | QT prolongation via CYP3A4 inhibition and additive cardiac effects |
| **Major** | Abiraterone | CYP3A4 inhibition raises Cisapride plasma levels; QT risk |
| **Major** | Adenosine | Cardiac conduction abnormality risk |
| **Major** | Alfuzosin | Additive QT prolongation |
| **Major** | Amisulpride | Additive QT prolongation |
| **Major** | Anagrelide | Additive QT prolongation |
| **Major** | Apalutamide | CYP3A4 induction may alter Cisapride levels |
| **Major** | Hydrochlorothiazide | Hypokalaemia-mediated QT prolongation |
| **Major** | Nifedipine | CYP3A4 inhibition significantly elevates Cisapride exposure |
| **Major** | Tramadol | Additive QT prolongation |
| **Major** | Acetazolamide | Electrolyte disruption potentiating QT risk |
| **Moderate** | Abametapir (topical) | CYP3A4 inhibition |
| **Moderate** | Famotidine | Altered GI absorption kinetics |
| **Moderate** | Formoterol | Additive QT effects via beta-agonist pathway |
| **Moderate** | Hyoscyamine | Pharmacodynamic antagonism of prokinetic effect |
| **Moderate** | Loperamide | Opposing GI motility effects |
| **Moderate** | Propofol | Additive cardiac depression risk |
| **Moderate** | Salbutamol | QT risk via beta-agonist |
| **Minor** | Ranitidine | Minor effect on GI transit; generally manageable |

Please refer to the original package insert for complete warnings and contraindications, as detailed CDSCO label data was not available in this Evidence Pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Peptic ulcer perforation is a surgical emergency where prokinetic agents are mechanistically contraindicated, not therapeutic. The TxGNN high-confidence prediction (99.94%) is assessed as a knowledge graph false positive driven by GI node proximity, not clinical evidence. There are no registered trials, and the 2 available publications do not address this indication at all. Simultaneously, Cisapride's QT prolongation safety profile and global market withdrawal status present significant barriers to any repurposing programme without a robust cardiac safety management plan.

**To proceed further, the following is needed:**

- **Mechanistic data**: Obtain full MOA profile via DrugBank API (DB00604) to resolve Data Gap DG002
- **Regulatory label**: Retrieve CDSCO / TFDA package insert PDFs to obtain formal warnings and contraindications (Data Gap DG001)
- **Indication re-prioritisation**: Consider redirecting analysis to the Rank 3 candidate, **Gastric Ulcer Disease** (Evidence Level L2; multiple RCTs including PMID 7732330, 8409300, 1823066), which carries a genuine mechanistic rationale (prokinesis reducing bile reflux and acid contact time) and existing clinical data
- **Cardiac safety strategy**: Any repurposing pathway for Cisapride must include a formal QT risk management plan given 302 documented interactions and historical market withdrawal
- **India market feasibility check**: Confirm whether Cisapride can be imported or re-approved under a named-patient or restricted-access programme in India before committing further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

