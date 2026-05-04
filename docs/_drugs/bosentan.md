---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 9
---

# Bosentan
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan (Tracleer®) is a dual endothelin receptor antagonist (ERA) originally approved for pulmonary arterial hypertension (PAH) and, in Europe, for prevention of digital ulcers in systemic sclerosis.
The TxGNN model ranks **Rheumatoid Arthritis (RA)** as its top repurposing candidate with a prediction score of **99.80%**, supported by biologically plausible mechanistic evidence from animal models.
However, current clinical evidence consists of **no completed human trials in RA** and **16 publications** that are primarily preclinical studies and indirect reviews — making this a research hypothesis rather than a near-term development opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bosentan is a dual antagonist of endothelin receptors type A (ET-A) and type B (ET-B). In its approved indication — pulmonary arterial hypertension — elevated endothelin-1 (ET-1) drives pathological vasoconstriction and vascular remodelling in the pulmonary circulation. Bosentan blocks both receptor subtypes to reduce pulmonary vascular resistance, improve exercise capacity, and delay disease progression. Detailed mechanistic data (MOA) were not available in this evidence pack; the mechanism described above is derived from established pharmacological literature.

In rheumatoid arthritis, ET-1 is overexpressed in synovial tissue and synovial fluid, where it acts via ET-A receptors to promote TNF-α release, drive synovial angiogenesis, and accelerate joint destruction. This provides a direct mechanistic bridge between Bosentan's known pharmacology and RA pathophysiology. The most compelling preclinical evidence comes from PMID 22249931, in which Bosentan significantly reduced joint inflammation and cartilage damage in a collagen-induced arthritis (CIA) mouse model, and TNF-α was shown to upregulate ET system gene expression in synovial tissue — creating a pro-inflammatory feed-forward loop that Bosentan may interrupt. Additionally, ET signalling participates in the IL-15/IFN-γ axis and IL-17 cascade that drive articular pain hypernociception (PMIDs 16766656, 19969421).

Despite this mechanistic logic, the clinical translation remains entirely unproven. The sole registered clinical trial retrieved (NCT06957002) targets Giant Cell Arteritis — a related but mechanistically distinct inflammatory vasculitis — rather than RA. No Phase 1 or Phase 2 human studies have evaluated Bosentan in RA patients. The cross-indication inference from PAH to RA therefore carries high uncertainty, and the candidate should be treated as a research question warranting dedicated biomarker-driven investigation before any clinical development commitment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Bosentan + glucocorticoids vs. glucocorticoids alone in Giant Cell Arteritis; primary endpoint is 12-month failure-free survival. **Note: Indication is GCA, not RA — evidence relevance to RA is indirect (Grade C).** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Animal Model | Inflammation Research | Bosentan ameliorated CIA mouse arthritis; TNF-α shown to upregulate ET system genes in synovial tissue — direct mechanistic link to RA |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Animal Model | Journal of Leukocyte Biology | ET-A/ET-B receptors mediate neutrophil accumulation and oedema in zymosan-induced arthritis via LTB4, TNF-α, and CXCL-1 pathways |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Animal Model | PNAS | IL-15-induced articular hypernociception blocked by dual ET receptor antagonism; establishes ET system's role in RA-associated pain |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Animal Model | Pain | IL-17 drives hypernociception in antigen-induced arthritis; ET system is part of the downstream signalling cascade |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia Polska | Child with Eisenmenger syndrome + juvenile RA; bosentan used for cardiac indication with clinical improvement — RA co-managed with naproxen |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | PAH associated with CTDs including RA; bosentan cited as treatment option for CTD-associated PAH with significant prognostic impact |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | ET-1 implicated in vascular PAH complicating multiple CTDs; RA listed among affected diseases |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in CTDs; bosentan management context across rheumatic diseases |
| [18238768](https://pubmed.ncbi.nlm.nih.gov/18238768/) | 2008 | Review | AJHP | Drug therapy options for systemic sclerosis complications; bosentan for PAH and digital ulcers — indirect relevance via shared CTD mechanisms |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | Rheumatic skin disease pathophysiology and therapies; broader rheumatology context |

---

## India Market Information

Bosentan is currently **not marketed in India**. No approved product licences, registrations, or authorised dosage forms are on record. Any clinical development or compassionate use pathway would require de novo regulatory filing with CDSCO.

---

## Safety Considerations

Package insert warnings and contraindications were not available in this evidence pack. Please refer to the Tracleer® Summary of Product Characteristics (EMA) or FDA prescribing information for complete safety data including hepatotoxicity monitoring requirements and reproductive toxicity warnings.

**Drug Interactions** — 244 total interactions identified (all listed interactions are Moderate severity):

| Interacting Drug | Severity | Clinical Note |
|---|---|---|
| Clarithromycin | Moderate | CYP3A4 inhibition → may increase bosentan plasma exposure |
| Dexamethasone / Hydrocortisone / Betamethasone / Triamcinolone | Moderate | Mutual CYP3A4 induction; may reduce corticosteroid and bosentan levels — clinically significant given corticosteroids are first-line in RA |
| Pioglitazone | Moderate | CYP2C8/3A4 interaction; bosentan induction may reduce pioglitazone efficacy |
| Canagliflozin / Dapagliflozin / Empagliflozin / Ertugliflozin | Moderate | Bosentan CYP induction may reduce SGLT2 inhibitor exposure |
| Metronidazole | Moderate | CYP2C9 interaction |
| Cimetidine | Moderate | CYP inhibition may alter bosentan metabolism |
| Cisapride | Moderate | QT prolongation risk combined with CYP3A4 interaction |
| Aprepitant | Moderate | CYP3A4 substrate/inhibitor; bidirectional interaction potential |
| Eliglustat | Moderate | Narrow therapeutic index drug; CYP2D6/3A4 interaction |

> Bosentan is a well-established inducer of CYP3A4 and CYP2C9, underpinning many of these 244 interactions. The interaction with corticosteroids is particularly relevant for RA patients, where glucocorticoids are frequently co-administered. A full DDI review against any planned concomitant RA therapy (e.g., methotrexate, biologics, JAK inhibitors) is essential.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Preclinical animal model data (CIA, zymosan, antigen-induced arthritis) provide biologically coherent mechanistic support for ET-1 involvement in RA synovial inflammation and pain, and Bosentan's dual ERA mechanism is theoretically applicable. However, there are no completed or active human clinical trials specifically evaluating Bosentan in RA, and the one retrieved trial (NCT06957002) addresses a different disease (GCA) and has not yet enrolled its first patient. With an evidence level of L4 and zero India market presence, the risk-benefit profile does not support clinical development at this stage.

**To proceed, the following is needed:**
- Complete MOA documentation from DrugBank or primary pharmacological sources
- Full review of Tracleer® package insert for contraindications, hepatotoxicity monitoring requirements, and reproductive warnings (known class concern for ERAs)
- Assessment of DDI profile against RA standard-of-care drugs (methotrexate, TNF inhibitors, JAK inhibitors) — not yet captured in this evidence pack
- A dedicated biomarker study to identify RA patient subpopulations with elevated synovial ET-1 levels as potential responders
- A Phase 1/2 proof-of-concept clinical trial in RA with pre-specified synovial histology and imaging endpoints
- India regulatory pre-submission consultation with CDSCO given current zero-registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

