---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 5
---

# Propofol
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a widely used intravenous general anesthetic and sedative-hypnotic agent, originally developed for induction and maintenance of general anesthesia and procedural sedation. The TxGNN model predicts it may be effective for **Migraine Disorder** (specifically as an abortive treatment for acute migraine attacks), with **5 clinical trials** and **20 publications** currently supporting this direction, including two completed RCTs and one systematic review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia / procedural sedation (well-established clinical use; not captured in the registration data provided) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on well-established pharmacological knowledge, Propofol is a GABA-A receptor agonist used clinically as an intravenous general anesthetic and sedative-hypnotic agent for induction and maintenance of anesthesia and procedural sedation. Its efficacy in this original use is well proven and extensively documented.

Anesthesia/sedation and migraine disorder appear unrelated at first glance, but they are mechanistically connected: cortical spreading depression (CSD) is believed to be the neural correlate of migraine aura and a trigger of migraine pain. Propofol's GABA-ergic sedative properties have been shown in basic-science work to suppress CSD, providing a plausible biological rationale for its use as an acute abortive agent — a use already explored clinically at subanesthetic doses in emergency department settings, particularly in pediatric and refractory adult migraine.

This mechanistic plausibility is reinforced by real-world use: propofol has been administered off-label in EDs for over two decades for refractory migraine, and several prospective and randomized trials (below) have specifically tested low-dose propofol as an abortive migraine therapy. This gives the TxGNN prediction meaningfully more support than a purely computational association — the mechanism (CSD suppression) and the clinical use pattern (subanesthetic ED dosing) point in the same direction. Note, however, that this rationale applies only to **acute abortive treatment of migraine attacks**, not to chronic migraine prevention, which has no supporting mechanism or evidence here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Tested low-dose (subanesthetic) propofol as abortive therapy for pediatric migraine in the ED; prior retrospective experience suggested it is safe and may be more effective than standard ED treatments. |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Evaluated low-dose propofol for severe refractory migraine in adults presenting to the ED; trial was terminated early, limiting the strength of the signal. |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Assessed low-dose propofol infusion as an abortive agent for pediatric migraine, including effective/safe dosing limits and duration of effect. |

*Two additional registered trials (NCT02443220, NCT03789370) were identified in the search but excluded as low-relevance — they evaluate propofol only as an incidental anesthesia agent (electroacupuncture-combined cardiac surgery; general anesthesia maintenance vs. sevoflurane) rather than as a migraine treatment.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | The Journal of Emergency Medicine | Prospective RCT suggesting efficacy of sub-anesthetic propofol doses for pediatric migraine with a favorable side-effect profile and potentially shorter ED length of stay. |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management in the ED. |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT comparing sumatriptan+placebo vs. sumatriptan+propofol combination for acute migraine management. |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Academic Emergency Medicine | Systematic review concluding that, based on limited but consistent evidence from outpatient and inpatient settings, propofol is a reasonable option for acute migraine treatment in the ED. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Review/Guideline | Headache | 2025 American Headache Society guideline update on parenteral pharmacotherapies for acute migraine treatment in the ED. |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Current Pain and Headache Reports | Review of intravenous migraine treatment options in children and adolescents in the ED setting. |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Current Neurology and Neuroscience Reports | Review of ED and inpatient abortive headache management in children and adolescents. |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Review | Headache | Review of rescue therapies for acute migraine, including neuroleptics, antihistamines, and propofol among other agents. |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Cohort/Case Series | Expert Review of Neurotherapeutics | Describes the drug profile and clinical experience of sub-anesthetic propofol dosing for refractory/intractable migraine. |
| [32705803](https://pubmed.ncbi.nlm.nih.gov/32705803/) | 2020 | Commentary/Opinion | Emergency Medicine Australasia | Editorial questioning whether propofol should be used for migraine given the current strength of evidence, despite feasibility. |

---

## India Market Information

Currently no India market registrations were found — Propofol is recorded as **not marketed** in the reviewed jurisdiction, with 0 registered licenses.

---

## Safety Considerations

- **Drug Interactions**: 228 documented interactions on record. Notable moderate-level interactions include opioids/opium derivatives (Morphine, Morphine [liposomal], Opium), 5-HT3 antiemetics (Ondansetron, Granisetron, Dolasetron), macrolide antibiotic Clarithromycin, fluoroquinolone Levofloxacin, prokinetic agent Cisapride, H2-blocker Famotidine, and various laxatives/bowel-prep agents (Bisacodyl, Castor oil, Glycerin, Lactitol, Lactulose, Magnesium citrate, Magnesium hydroxide, Mineral oil, Loperamide). One minor-level interaction was noted with Metronidazole.

*Key warnings and contraindications are not available in this evidence pack (Blocking data gap DG001 — TFDA/label warnings and contraindications must be sourced from the official package insert before proceeding to safety screening).*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for propofol as an acute abortive migraine treatment is meaningfully stronger than a pure model prediction — it includes a completed Phase 2/3 RCT, additional pediatric RCTs, and a systematic review, supporting an L2 evidence level. However, a **Blocking-severity data gap** exists: official package insert warnings/contraindications (DG001) have not yet been obtained, which per protocol prevents this candidate from formally entering the S1 safety screening stage. The recommendation therefore reflects genuine efficacy signal tempered by an unresolved safety-data blocker.

**To proceed, the following is needed:**
- Official TFDA/label package insert warnings and contraindications (resolves Blocking gap DG001)
- Confirmed mechanism-of-action data from DrugBank (resolves High-severity gap DG002)
- Assessment of subanesthetic dosing/monitoring feasibility outside anesthesia-controlled settings (given propofol's respiratory depression and sedation risk profile), since current evidence is ED-based and pediatric-heavy
- Evaluation of local market/import pathway, given the drug is currently not registered in the reviewed jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

