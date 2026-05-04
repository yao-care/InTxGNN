---
layout: default
title: Amifostine
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Amifostine
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

# Amifostine: From Cancer Chemo/Radioprotection to Hypertensive Disorder

## One-Sentence Summary

Amifostine (WR-2721) is a cytoprotective prodrug approved for reducing normal tissue damage from cisplatin chemotherapy and head and neck radiotherapy.
The TxGNN model predicts it may be relevant to **Hypertensive Disorder** (score: 99.995%), but a **⚠️ critical reverse warning applies**: amifostine's most common serious clinical side effect is **transient hypotension**, creating a direct mechanistic contradiction against its use for treating hypertension.
Currently **0 clinical trials** and **11 publications** exist for this pairing, and none directly support amifostine as a treatment for hypertension.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cancer cytoprotection (cisplatin-induced nephrotoxicity prevention; radiation-induced xerostomia reduction) |
| Predicted New Indication | Hypertensive Disorder |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 (model prediction only — no directly supporting studies) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why This Prediction Was Made — and Why It Has Limitations

Amifostine is a phosphorylated aminothiol prodrug converted to its active metabolite **WR-1065** by alkaline phosphatase, an enzyme more highly expressed in normal tissues than in tumors. WR-1065 is a potent free radical scavenger that selectively shields normal cells from oxidative DNA damage caused by radiation and alkylating chemotherapy. It is approved for (1) prevention of cumulative cisplatin-induced renal toxicity and (2) reduction of moderate-to-severe xerostomia in post-operative head and neck cancer radiotherapy.

Critically, **transient hypotension is amifostine's most common clinically significant side effect**, occurring in up to 60% of patients and requiring pre-hydration, supine positioning, and temporary treatment suspension protocols. This well-established pharmacological property — blood pressure reduction — creates a **direct mechanistic contradiction** against using amifostine to treat hypertension.

The TxGNN prediction most likely reflects knowledge graph topology rather than a genuine therapeutic opportunity. One literature study (PMID 40479584) links the Fanconi anemia complementation group L (FANCL) pathway to pulmonary arterial hypertension via endothelial DNA damage — and amifostine's mechanism involves DNA damage prevention — creating an indirect graph node connection. However, this chain of inference is highly speculative and does not translate into a clinically actionable hypothesis. The 99.995% score reflects graph connectivity, not biological plausibility for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for amifostine in hypertensive disorder.

---

## Literature Evidence

The 11 retrieved publications describe amifostine in oncology cytoprotection contexts; none directly investigate amifostine as a treatment for hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10755322](https://pubmed.ncbi.nlm.nih.gov/10755322/) | 2000 | RCT (cytoprotection) | Cancer Chemother Pharmacol | Compared amifostine vs. dexrazoxane for doxorubicin-induced cardiotoxicity using spontaneously hypertensive rats as an animal model — these are **not hypertension treatment studies** but cardiotoxicity protection studies |
| [11335791](https://pubmed.ncbi.nlm.nih.gov/11335791/) | 2001 | Cohort Study | Anti-Cancer Drugs | Tolerability of amifostine in elderly vs. younger cancer patients (268 IV administrations); **transient hypotension confirmed as the most common side effect** |
| [15560691](https://pubmed.ncbi.nlm.nih.gov/15560691/) | 2004 | Phase II Trial | J Med Assoc Thailand | Cisplatin-vinblastine + amifostine in advanced NSCLC; assessed whether amifostine reduces cisplatin toxicity without compromising antitumor efficacy |
| [6286554](https://pubmed.ncbi.nlm.nih.gov/6286554/) | 1982 | Early Phase Trial | Int J Radiat Oncol Biol Phys | Phase I trials of WR-2721 with radiation therapy in 65 patients; established 740 mg/m² as well-tolerated single dose |
| [6274534](https://pubmed.ncbi.nlm.nih.gov/6274534/) | 1981 | Phase I Trial | Cancer Clin Trials | Three Phase I trials of WR-2721 with radiation and alkylating agents (cyclophosphamide, cisplatin); maximum tolerated dose determination |
| [19395196](https://pubmed.ncbi.nlm.nih.gov/19395196/) | 2009 | Cohort Study | Int J Radiat Oncol Biol Phys | Evaluated moderate wine consumption as a natural alternative to amifostine for radioprotection in breast cancer; amifostine noted for high cost and significant side effects |
| [27855533](https://pubmed.ncbi.nlm.nih.gov/27855533/) | 2016 | Preclinical | Drug Delivery | Sustained-release microsphere formulation of amifostine to reduce injection frequency and blood-concentration-dependent side effects including hypotension |
| [19915842](https://pubmed.ncbi.nlm.nih.gov/19915842/) | 2010 | Review | Eur J Nucl Med Mol Imaging | Review of kidney protection strategies during peptide receptor radionuclide therapy; amifostine mentioned as one nephroprotective option |
| [40479584](https://pubmed.ncbi.nlm.nih.gov/40479584/) | 2025 | Mechanistic Study | Am J Respir Crit Care Med | FANCL pathway deficiency linked to pulmonary arterial hypertension via endothelial DNA damage — likely the knowledge graph source for TxGNN's prediction; amifostine is not studied as a therapeutic agent in this paper |
| [26130118](https://pubmed.ncbi.nlm.nih.gov/26130118/) | 2015 | Case Series/Review | Circulation | Mitomycin C-induced pulmonary veno-occlusive disease; chemotherapy identified as a risk factor for PH — peripherally related to hypertension by drug-induced pathway, not amifostine treatment |

---

## India Market Information

Amifostine is currently **not marketed in India** and has no registered product licenses on file.

---

## Safety Considerations

**Drug Interactions (134 total identified; key interactions listed below):**

A particularly important pattern in the interaction data is that amifostine carries moderate-level interactions with **multiple antihypertensive drug classes**. Concurrent use would risk additive hypotension — further reinforcing that this drug is unsuitable for use in hypertensive patients rather than offering therapeutic benefit.

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Acebutolol (beta-blocker) | Moderate | Additive hypotension risk |
| Nifedipine (calcium channel blocker) | Moderate | Additive hypotension risk |
| Fosinopril (ACE inhibitor) | Moderate | Additive hypotension risk |
| Furosemide (loop diuretic) | Moderate | Additive hypotension/fluid depletion risk |
| Alfuzosin (alpha-blocker) | Moderate | Additive hypotension risk |
| Aliskiren (direct renin inhibitor) | Moderate | Additive hypotension risk |
| Hydrochlorothiazide (thiazide diuretic) | Moderate | Additive hypotension risk |
| Amiloride (potassium-sparing diuretic) | Moderate | Additive hypotension risk |
| Mannitol | Moderate | Additive hypotension/fluid balance alteration |
| Papaverine | Moderate | Additive vasodilatory / hypotensive effects |
| Foscarnet | Moderate | Renal and electrolyte monitoring required |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Amifostine's established clinical pharmacology directly contradicts its use in hypertension: transient hypotension is its most common serious side effect, evidence is L5 (model prediction only) with zero clinical trials for this indication, and its interaction profile with standard antihypertensive drug classes creates compounding hypotensive risk rather than therapeutic synergy. The TxGNN high score likely reflects knowledge graph connectivity artifacts rather than a genuine repurposing signal.

**To revisit this prediction, the following would first be required:**
- A clearly articulated mechanistic hypothesis that resolves the fundamental contradiction between amifostine's blood-pressure-lowering side effect and its proposed antihypertensive use
- Exploratory preclinical studies specifically examining amifostine in hypertension models (currently absent in the literature)
- Confirmation that the TxGNN graph node connection via FANCL/PAH represents a true mechanistic pathway rather than a graph traversal artifact
- Assessment of whether a structurally modified derivative of amifostine (without the hypotensive pharmacology) might retain any potential hypertension-relevant activity

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

