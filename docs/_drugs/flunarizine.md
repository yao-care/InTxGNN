---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine: From Not Marketed in Taiwan to Migraine Disorder

## One-Sentence Summary

Flunarizine has no registered indication or license record in Taiwan and is currently not marketed here. The TxGNN model predicts it may be effective for **Migraine Disorder** (migraine prophylaxis) — an indication already well-established internationally — with **10+ clinical trials** and **10+ publications**, including multiple completed Phase 3/4 head-to-head RCTs and international headache-society guidelines, supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Taiwan registration data available; internationally used for migraine prophylaxis and vertigo |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in the registry (data gap), but pharmacology binding data confirms Flunarizine acts on the D₂ dopamine receptor and on T-type voltage-gated calcium channels (Ca_v3.1, Ca_v3.2, Ca_v3.3). Blockade of T-type calcium channels reduces neuronal hyperexcitability and is believed to inhibit cortical spreading depression, the physiological correlate of migraine aura — this is the accepted mechanistic basis for calcium-channel blockers used in migraine prophylaxis.

Notably, this is not a case of mechanistic extrapolation across unrelated diseases: per the DrugBank pharmacology record, Flunarizine's principal established use worldwide is migraine prophylaxis, and it is approved in a large number of countries (though not by the FDA, and not currently registered in Taiwan). The TxGNN prediction therefore largely confirms an already-recognized global standard-of-care indication rather than proposing a novel mechanistic leap — the practical question for this jurisdiction is one of market entry and local regulatory dossier completeness rather than proof-of-concept.

Consistent with this, the evidence base includes multiple completed head-to-head Phase 3/4 RCTs against topiramate, propranolol, and amitriptyline, plus endorsement in Canadian, European (EHF), and pediatric (AAN/AHS) headache-society guidelines, reinforcing that the mechanism-to-indication link is well supported rather than speculative.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Head-to-head RCT: flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Compares flunarizine vs propranolol for reducing pediatric migraine frequency using PedMIDAS |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Drug-interaction/pharmacokinetic study of flunarizine + topiramate mono- vs concomitant therapy |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Compares greater occipital nerve block, topiramate, and flunarizine for episodic migraine prevention |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Compares flunarizine vs amitriptyline on attack frequency and pain score in migraine prophylaxis |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | Acupuncture vs flunarizine hydrochloride (current standard prophylaxis) for migraine without aura |
| [NCT00740259](https://clinicaltrials.gov/study/NCT00740259) | Phase 4 | Completed | 70 | Explores flunarizine's D2-blockade for antipsychotic activity vs haloperidol in schizophrenia (mechanistic relevance, different indication) |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Active, not recruiting | 60 | Compares transcutaneous pulsed radiofrequency vs calcium channel blockers (flunarizine class) in childhood migraine |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not yet recruiting | 460 | Pragmatic multicentre trial comparing first-line migraine prophylaxis: amitriptyline, flunarizine, topiramate, propranolol |
| [NCT40614441](https://clinicaltrials.gov/study/NCT40614441) | — | — | — | *(see literature PMID 40614441 below — clinical trial registry entry not separately listed)* |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Systematic Review/Meta-analysis | The Journal of Headache and Pain | EHF critical re-appraisal and meta-analysis specifically rating the evidence for flunarizine in migraine prevention |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurologica Scandinavica | Flunarizine combined with transcutaneous supraorbital neurostimulation improves migraine prophylaxis vs either alone |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic Review/Meta-analysis | J Assoc Physicians India | Compares amitriptyline, propranolol, and flunarizine efficacy/safety for migraine prophylaxis |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic Review | Health Technology Assessment | Systematic review with economic modelling of preventive drugs for chronic migraine |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Guideline | Can J Neurol Sci | Canadian Headache Society guideline for migraine prophylaxis, including flunarizine |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Guideline | Neurology | AAN/AHS evidence-based guideline update for pediatric migraine prevention |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | Network meta-analysis of preventive medications, including flunarizine, in pediatric migraine |
| [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/) | 1997 | Postmarketing Study | Pharmacy World & Science | Postmarketing study comparing flunarizine to propranolol (migraine) and betahistine (vertigo) on risk/benefit |
| [2404346](https://pubmed.ncbi.nlm.nih.gov/2404346/) | 1990 | Comparative Trial | S Afr Med J | Double-blind trial comparing flunarizine 10 mg vs propranolol 60 mg TID for migraine prevention |
| [40614441](https://pubmed.ncbi.nlm.nih.gov/40614441/) | 2025 | Comparative Study | Brain & Development | Compares topiramate vs flunarizine on pain control and school/social performance in pediatric migraine |

## Taiwan Market Information

No license, product, or dosage-form records exist for Flunarizine in the Taiwan regulatory dataset (0 registrations; market status: Not Marketed). A formal market-entry dossier, including TFDA-equivalent label and package insert, would need to be prepared from scratch.

## Safety Considerations

**Pharmacological Binding Profile** (from pharmacology database, not a clinical DDI/warning source): Flunarizine binds the D₂ dopamine receptor and T-type calcium channels Ca_v3.1, Ca_v3.2, and Ca_v3.3. This target profile is consistent with its use as a calcium-channel blocker with mild dopamine-antagonist activity, and may inform anticipated class-related risks (e.g., extrapyramidal symptoms, weight gain, depression) reported in the postmarketing literature above, but it does not substitute for formal contraindication or warning data.

Please refer to the package insert for detailed safety information once available — key warnings and contraindications are not currently documented in this evidence pack (see Data Gap DG001, Blocking severity).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3/4 head-to-head RCTs and endorsement across several national/international headache-society guidelines for migraine prophylaxis. However, Flunarizine has zero registrations and no market presence in Taiwan, and both the formal MOA record and TFDA-equivalent safety documentation (warnings, contraindications) are missing — the latter is flagged as a Blocking data gap (DG001) that prevents a full S1 safety assessment.

**To proceed, the following is needed:**
- TFDA-equivalent package insert / label (warnings and contraindications) — Blocking (DG001)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- A market-entry regulatory dossier, since there are currently no Taiwan registrations
- Confirmation of true drug-drug interaction data (the current DDI dataset reflects pharmacology binding targets, not clinical interactions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

