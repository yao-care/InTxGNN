---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 3
---

# Phenylephrine
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

# Phenylephrine: From Decongestant/Vasopressor Use to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is a selective α1-adrenergic receptor agonist already established in clinical practice as a nasal/ocular decongestant and vasopressor; formal original-indication and MOA records are not available in this evidence pack. The TxGNN model ranks **Nasal Cavity Disease** as its top predicted indication, and the supporting evidence largely confirms an already-routine clinical use rather than a novel hypothesis, with **8 clinical trials** and **8 publications** currently identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug is unlicensed in Taiwan); generally known as an α1-adrenergic decongestant/vasopressor |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action documentation is not available for this candidate (data gap DG002). Based on the mechanistic rationale captured in this evidence pack, phenylephrine is a selective α1-adrenergic receptor agonist that acts on nasal mucosal vascular smooth muscle to produce vasoconstriction, reducing mucosal congestion and swelling — the standard pharmacology underlying nasal decongestants used for nasal blockage and to improve the surgical field during nasal procedures.

Because this mechanism is already the textbook basis for phenylephrine's clinical use as a nasal decongestant, the TxGNN prediction of "nasal cavity disease" largely reconfirms an existing, well-established use rather than proposing a genuinely novel indication. This is corroborated by the clinical trial and literature evidence below, much of which studies phenylephrine-containing nasal formulations (e.g., co-phenylcaine, Polydexa with phenylephrine) directly in nasal/sinus conditions.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomized double-blind, double-dummy crossover trial of an H3-receptor antagonist against nasal allergen challenge, using acoustic rhinometry to measure congestion (Relevance: A — rigorous design directly targeting nasal congestion, though the study drug is not phenylephrine). |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Compared co-phenylcaine (contains phenylephrine) nasal spray vs. nebulization for decongestion and local anesthesia before rigid nasoendoscopy (Relevance: B). |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Triple-crossover comparison of cocaine, lidocaine/xylometazoline, and saline for intranasal analgesia before awake nasotracheal intubation; no confirmed phenylephrine arm (Relevance: C). |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Unknown | 120 | Compared endonasal-endoscopic vs. external dacryocystorhinostomy for nasolacrimal duct obstruction; phenylephrine, if used, is only an intraoperative hemostatic adjunct (Relevance: C). |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compared topical oxymetazoline vs. epinephrine for blood loss and surgical-field visualization before endoscopic sinus surgery — mechanistically related vasoconstrictor comparison (Relevance: B). |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Compared Kovanaze (tetracaine/oxymetazoline) nasal mist vs. articaine injection for maxillary dental pulpal anesthesia; terminated early, not a nasal-disease indication (Relevance: C). |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Evaluated perioperative esmolol vs. lidocaine infusion on recovery quality after functional endoscopic sinus surgery; indirect relevance (Relevance: C). |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Same Kovanaze vs. articaine dental-anesthesia comparison as NCT03962634; withdrawn with zero enrollment (Relevance: C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | Triple-blind RCT: topical tranexamic acid reduced bleeding and improved surgical-field quality during FESS in chronic rhinosinusitis (vasoconstrictor-comparator context). |
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind RCT of cophenylcaine spray (contains phenylephrine) vs. placebo before flexible nasendoscopy; no significant difference in pain/discomfort between arms. |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental/Clinical | Vestnik otorinolaringologii | Safety and efficacy evaluation of Polydexa nasal spray with phenylephrine in acute rhinosinusitis; no toxic effects identified in available data. |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | Acoustic rhinometry of nasal cavity/nasopharynx geometry before and after adenotonsillectomy in patients with hypertrophied turbinates. |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik otorinolaringologii | Endoscopic assessment of nasal mucosa after topical therapy, including Polydexa with phenylephrine, for granulomatosis with polyangiitis. |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Reviews pathogenetic treatment approaches for inflammatory nasal/paranasal sinus disease, emphasizing decongestants that reduce mucosal hyperemia and swelling. |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case Report | Arch Ophthalmol | Case report of toxicity during cocaine-assisted dacryocystorhinostomy, including a reaction to intranasal phenylephrine. |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In vitro/Preliminary | Clin Otolaryngol Allied Sci | In vitro study of dose-dependent drug effects on nasal ciliary beat frequency. |

## Safety Considerations

- **Drug Interactions**: DDI screening identified **180 total interactions** (source: DDInter). Representative entries are predominantly Moderate-severity interactions with antidiabetic agents — insulin (human, aspart), sulfonylureas (Glimepiride, Glipizide, Glyburide, Chlorpropamide, Acetohexamide), GLP-1 receptor agonists (Dulaglutide, Exenatide, Albiglutide), a DPP-4 inhibitor (Alogliptin), SGLT2 inhibitors (Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin), and Acarbose, consistent with phenylephrine's sympathomimetic potential to interfere with glycemic control. Moderate interactions were also noted with anticholinergic agents (Atropine ophthalmic, Clidinium, Hyoscyamine) and Diethylpropion.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The lead candidate (Nasal Cavity Disease) has L2 evidence — one completed Phase 2 RCT plus several supportive trials and publications involving phenylephrine-containing formulations — and a mechanistically sound, already-routine clinical rationale (α1-agonist nasal vasoconstriction), so this largely confirms existing use rather than a novel hypothesis. However, the drug is currently unlicensed in Taiwan (0 registrations) and a **Blocking** data gap on label warnings/contraindications (DG001) prevents a full safety review, so a full "Go" is not yet warranted.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings and contraindications (Blocking gap DG001 — required before S1 safety review)
- Confirmed official mechanism-of-action documentation (DG002)
- Route/dosage-form compatibility assessment for an intranasal indication
- Note: the two lower-ranked candidates — Acute Laryngopharyngitis (L5, Hold, no supporting trials/literature) and Trigeminal Autonomic Cephalalgia (L4, Hold, phenylephrine used only as a diagnostic pupillometry probe, not therapeutically) — are not recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

