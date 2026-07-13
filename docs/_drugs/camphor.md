---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Traditional Topical Counterirritant to Migraine Disorder

## One-Sentence Summary

Camphor (DB01744) is a naturally occurring bicyclic monoterpenoid historically employed as a topical counterirritant and local analgesic; no formally approved pharmaceutical indication is on record in India or internationally.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a confidence score of **99.85%**,
however the supporting evidence consists of **0 clinical trials** and **5 publications**, several of which document camphor as a headache *trigger* rather than a treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved pharmaceutical indication on record (traditional topical counterirritant use) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for Camphor. Based on established pharmacological knowledge, Camphor is a bicyclic monoterpenoid that acts as a partial agonist of TRPV1 (the capsaicin/heat receptor) and an agonist of TRPM8 (the menthol/cold receptor). Both TRP channels are densely expressed in trigeminal sensory neurons — the very neural pathway responsible for migraine headache pain. In theory, modulating these receptors could attenuate pain signal transmission at the trigeminal nucleus caudalis in the brainstem, which is the primary relay hub for craniofacial pain.

This biological rationale aligns with centuries of folk medicine tradition in which camphor oil applied to the temples was used to relieve headaches — a counter-irritant mechanism whereby localised cutaneous stimulation dampens deeper pain perception. The traditional temple application practice, documented across multiple cultures, is broadly consistent with TRPV1-mediated desensitisation of peripheral trigeminal fibres.

However, this entire mechanistic chain remains indirect extrapolation. There are no prospective or controlled clinical trials testing camphor in migraine patients. More critically, the available case literature contains examples of camphor in essential-oil toothpastes *triggering* cluster headache attacks — a finding that introduces a meaningful safety concern and contradicts any simple anti-nociceptive narrative. The TxGNN model likely captures network proximity between camphor's receptor targets and migraine's pain circuitry, but proximity in a knowledge graph does not translate to therapeutic utility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Camphor in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT (Phase 3) | J Headache Pain | DRAGON study: erenumab vs. placebo for chronic migraine prevention in Asian patients (N=not specified). **Not a camphor study** — retrieved due to migraine keyword overlap; no relevance to camphor efficacy. |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | Five cases of cluster headache secondary to toothpastes containing pro-convulsant essential oils including camphor. **Negative signal** — camphor acted as a headache trigger, not a treatment. |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | Two cases of cluster headache temporally related to use of toothpastes containing camphor and eucalyptus essential oils. **Negative signal** — reinforces trigger risk. |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Z Kinder Jugendpsychiatr Psychother | Historical overview of neuropsychopharmacotherapy in children in the 1940s–50s; camphor mentioned as a historical CNS stimulant agent. Low relevance to modern migraine treatment. |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Case Report / Historical | Minerva Medica | Historical report on therapy for essential hemicrania. No abstract available; significance cannot be assessed. |

> ⚠️ **Evidence quality alert**: Two of the five publications (PMID 35856604, 34373243) document camphor as a cluster headache *trigger*. The only controlled trial (PMID 36404301) studies erenumab, not camphor. No publication demonstrates camphor efficacy in migraine prevention or acute treatment.

---

## India Market Information

Camphor holds no pharmaceutical marketing authorisations in India. Zero registrations are on record across all dosage forms and routes of administration.

---

## Safety Considerations

Formal regulatory warning text (TFDA/CDSCO package insert) was not available in this data package. Based on established general pharmacology:

- **Systemic toxicity**: Camphor is acutely toxic when ingested. Doses above approximately 2 g in adults — and far lower in children — can cause seizures, CNS excitation, and respiratory depression. The margin between a pharmacologically active dose and a toxic dose is narrow.
- **Paediatric risk**: Application to the nasal area or large skin surfaces in infants and young children has caused seizures and deaths; camphor products are contraindicated in children under 2 years in multiple jurisdictions.
- **Topical safety limit**: The US FDA restricts OTC topical camphor products to ≤11% concentration; formulations above this level require prescription status.
- **Skin and mucosa**: Not for application to broken skin, wounds, or mucous membranes.

Please refer to the relevant package insert and regulatory guidance for a complete and jurisdiction-specific safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While camphor has a theoretically plausible mechanistic link to migraine pain pathways via TRPV1/TRPM8 modulation of trigeminal neurons, the clinical evidence base is not only absent — it is actively negative, with published cases documenting camphor-containing products triggering cluster headache attacks. There are zero registered clinical trials, zero approved indications, and the drug is not marketed in India. Proceeding to clinical development without foundational preclinical data would be premature and potentially unsafe.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept**: In vivo studies in established migraine or trigeminal pain animal models (e.g., nitroglycerin-induced trigeminal sensitisation models, dural electrical stimulation) to confirm analgesic — not pro-nociceptive — effects.
- **Formal MOA characterisation**: DrugBank API query to retrieve confirmed receptor binding data, pharmacodynamic profiles, and any known drug interactions.
- **Safety package**: TFDA and CDSCO package insert text for formal contraindication and warning review; DDI database query (current data package returned a file-not-found error).
- **Route of administration decision**: Systemic vs. topical routes carry fundamentally different safety profiles, bioavailability considerations, and regulatory pathways — this must be defined before any clinical design.
- **Cluster headache signal evaluation**: The two case series documenting camphor as a headache trigger require formal risk assessment before any human exposure study is considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

