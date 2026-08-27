---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Epilepsy to Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

> Clobazam is a 1,5-benzodiazepine anticonvulsant, established as an adjunctive antiseizure medication (ASM) in refractory epilepsy syndromes.
> The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
> but currently no clinical trials and only **2 indirect case-series publications** (studying related benzodiazepines/ASMs, not Clobazam itself) support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (adjunctive antiseizure therapy) — no India (CDSCO) regulatory record available; drug is unmarketed locally |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Clobazam in this Evidence Pack. Based on known pharmacological information (and corroborated by the literature retrieved for related, higher-evidence indications in this same pack — see PMID 11129898, 3527689), Clobazam is a 1,5-benzodiazepine that acts as a broad-spectrum positive allosteric modulator of the GABA-A receptor. Its efficacy as adjunctive antiseizure therapy in refractory epilepsy syndromes (e.g., Lennox-Gastaut syndrome, focal epilepsy) is clinically well established, and mechanistically this GABAergic action may extend to other refractory seizure states.

FIRES is a form of new-onset refractory status epilepticus (NORSE) that occurs after a febrile illness in previously healthy children. Acute management of FIRES relies heavily on GABAergic agents — benzodiazepines (e.g., midazolam, lorazepam) and barbiturates — for seizure control, with oral benzodiazepines such as Clobazam commonly considered during the weaning/maintenance phase in clinical practice once the acute anesthetic-coma phase resolves. This shared GABA-A-mediated mechanism is the basis of the TxGNN prediction.

However, the two literature items retrieved for this specific pairing (PMID 35770765 on enteral lorazepam weaning, and PMID 39958143 on perampanel reducing barbiturate dependency) do not study Clobazam directly — they provide only indirect, drug-class-level support. This is reinforced by stronger, Clobazam-specific evidence found elsewhere in this Evidence Pack for closely related epileptic-encephalopathy indications (e.g., benign occipital epilepsy and childhood-onset epileptic encephalopathy/Lennox-Gastaut syndrome, both rated L2 with Cochrane systematic-review-level support), which lends plausibility to the drug class but does not substitute for direct FIRES data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Cohort/Case Series | Epileptic Disorders | Enteral lorazepam (a related benzodiazepine, not Clobazam) used as an effective weaning substitute in midazolam-dependent FIRES patients |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Series | Cureus | Perampanel (AMPA antagonist, not GABAergic) reduced barbiturate dependency in a FIRES case; illustrates the broader refractory-seizure management context in which benzodiazepines like Clobazam are also used |

---

## India Market Information

No India (CDSCO) marketing authorizations on record — Clobazam is currently not marketed in India (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data were not retrievable during this evaluation — the DDI database query failed due to a missing local data file, and no local package-insert data exists since the product is unmarketed in India. This is flagged as a Blocking data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on plausible drug-class mechanism (GABA-A modulation) rather than Clobazam-specific evidence — there are zero clinical trials and only two indirect case-series publications studying other benzodiazepines/ASMs in FIRES, not Clobazam itself (Evidence Level L4, decision stage S1 — "Research Question"). Combined with the absence of any India market presence or safety documentation, this candidate is not yet ready to advance past the research-question stage.

**To proceed, the following is needed:**
- Clobazam-specific case series, cohort studies, or trials in FIRES/NORSE patients (current literature only covers related agents)
- CDSCO/package-insert warnings and contraindications data for Clobazam (currently a **Blocking** data gap — DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (**High** priority gap — DG002)
- Re-run of the drug-drug interaction (DDI) query once the local DDInter reference file is restored (query previously failed with a file-not-found error)
- Consider reprioritizing near-term evaluation toward candidates in this same predicted-indication set with materially stronger, Clobazam-specific evidence — notably **benign occipital epilepsy** and **childhood-onset epileptic encephalopathy/Lennox-Gastaut syndrome** (both Evidence Level L2, decision stage S2, "Proceed with Guardrails," supported by Cochrane systematic reviews)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

