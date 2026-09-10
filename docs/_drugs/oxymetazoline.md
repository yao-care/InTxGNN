---
layout: default
title: Oxymetazoline
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxymetazoline: From Nasal Decongestion to Nasal Cavity Disease

## One-Sentence Summary

Oxymetazoline is a topical alpha-adrenergic agonist globally known as an over-the-counter nasal (and ophthalmic) decongestant, but it currently holds **no marketing authorization** in the local registry reviewed here. The TxGNN model's top-ranked prediction is **Nasal Cavity Disease**, a target that is largely consistent with the drug's already-established pharmacology rather than a truly novel disease area, supported by **17 clinical trials** and **5 publications**, most of which are indirect or comparator studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the local registry (drug not marketed); globally recognized as an OTC nasal/ophthalmic decongestant per DrugBank pharmacology data |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation is currently a data gap (DG002). However, DrugBank pharmacology profiling shows oxymetazoline is a synthetic imidazoline derivative acting as an agonist at α1A/α1B/α1D and α2A/α2B/α2C adrenoceptors, with additional affinity at 5-HT1B, 5-HT1D and 5-HT2C receptors. Its dominant clinical action — local vasoconstriction of nasal mucosal blood vessels leading to reduced congestion and swelling — is already well established and is the basis of its worldwide OTC use (and its 2020 FDA approval as an ophthalmic solution, Upneeq®, for acquired blepharoptosis).

Because of this, the "predicted" indication of **Nasal Cavity Disease** largely overlaps with oxymetazoline's existing, long-standing clinical use as a topical decongestant, rather than representing a genuinely novel repurposing hypothesis. The value of this signal is therefore less about discovering a new mechanism and more about confirming a well-known pharmacological effect that has simply never been formally licensed in this jurisdiction.

Mechanistically, α-adrenergic-mediated vasoconstriction directly reduces mucosal blood flow and edema, which underlies symptomatic relief in nasal cavity conditions such as rhinitis-related congestion and pre-surgical decongestion (e.g., NCT03228914, comparing oxymetazoline to epinephrine before endoscopic sinus surgery). This gives the prediction high biological plausibility even though the supporting trial base is mostly indirect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Direct comparison of topical 0.05% oxymetazoline vs. 1:1000 epinephrine on blood loss and surgical field visualization before endoscopic sinus surgery. |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | N/A | Completed | 16 | Acoustic rhinometry study using 0.05% oxymetazoline as the decongestion agent to characterize nasal cavity notches. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, double-dummy, 4-way crossover design typical of nasal decongestant pharmacodynamic trials; tests an H3 antagonist's effect on allergen-induced congestion. |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Evaluates topical anesthesia and/or decongestant pretreatment for reducing discomfort during fiberoptic nasal pharyngoscopy/laryngoscopy. |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Compares co-phenylcaine nasal spray vs. nebulization for decongestion and local anesthesia prior to nasoendoscopy. |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Triple-crossover comparison of cocaine, lidocaine/xylometazoline (same imidazoline class as oxymetazoline), and saline for intranasal analgesia. |
| [NCT00147940](https://clinicaltrials.gov/study/NCT00147940) | Phase 4 | Terminated | 20 | Correlates nasal volume/cross-sectional area with nasalance scores via acoustic rhinometry; no direct drug intervention. |
| [NCT00015795](https://clinicaltrials.gov/study/NCT00015795) | Phase 1 | Completed | 30 | Investigates airflow/laryngeal resistance in abductor spasmodic dysphonia; limited direct relevance to nasal cavity disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal/Preclinical | Ann Otol Rhinol Laryngol | Topical oxymetazoline nose drops evaluated for effect on early local tissue defense in an experimental bacterial maxillary sinusitis model in rabbits. |
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Cohort | Ann NY Acad Sci | Assesses olfactory function and nasal volume (via acoustic rhinometry) changes during acute rhinitis. |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohort | J Plast Surg Hand Surg | Evaluates nasal patency by acoustic rhinometry in children after repair of unilateral cleft lip/palate. |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case Report | Global Pediatric Health | Case of rhinoscleroma (a rare granulomatous nasal cavity disease) in a 9-year-old boy. |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case Report/Series | Am J Rhinol Allergy | Describes endoscopic coblation treatment technique for nasal telangiectasias in hereditary hemorrhagic telangiectasia. |

---

## Market Information

No marketing authorization is currently registered for this product in the reviewed jurisdiction (market status: 未上市 / not marketed; total registrations: 0).

---

## Safety Considerations

- **Drug Interactions**: No formal clinical drug-drug interaction records are available. Pharmacology profiling (DrugBank, 9 targets) shows oxymetazoline binds α1A/α1B/α1D- and α2A/α2B/α2C-adrenoceptors as well as 5-HT1B/1D/2C receptors. This sympathomimetic activity is consistent with the general caution — discussed in a broader review of MAOI drug interactions (PMID 36425231) — that adrenergic agents may interact with monoamine oxidase inhibitors, though no oxymetazoline-specific interaction level is documented here.

Formal warnings and contraindication data (from the package insert) are not yet available (see DG001, blocking severity). Please refer to the package insert for complete safety information once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The predicted indication (Nasal Cavity Disease) is mechanistically strong but largely reconfirms oxymetazoline's already well-known decongestant activity rather than revealing a novel therapeutic direction; evidence level is L3 (mostly indirect/comparator trials and preclinical/observational literature, no direct confirmatory RCT for this specific indication framing).
- The product is not currently marketed locally, so no safety dossier or approved indication text exists to build on.
- Two additional lower-ranked candidates were also evaluated: *acute laryngopharyngitis* (L5, no supporting trials or literature — **Hold**) and *headache disorder* (L3, plausible sphenopalatine-ganglion mechanism but only indirect/comparator evidence — **Research Question**). Neither is ready to advance ahead of the nasal cavity disease candidate.

**To proceed, the following is needed:**
- TFDA package insert data — key warnings and contraindications (DG001, blocking)
- Confirmed mechanism-of-action documentation (DG002)
- Direct oxymetazoline trials specifically designed for nasal cavity disease endpoints (current trials are mostly comparator/diagnostic studies)
- A formal local regulatory pathway assessment, given the product currently has zero registrations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

