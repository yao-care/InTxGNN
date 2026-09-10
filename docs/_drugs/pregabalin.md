---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 690
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pregabalin: From Neuropathic Pain to Migraine Prophylaxis — and Other TxGNN-Predicted Candidates

## Summary

This evidence pack evaluates Pregabalin (DrugBank DB00230) against **five** TxGNN-predicted indications rather than a single candidate. Original indication and mechanism-of-action data were not captured in this pack (both flagged as data gaps), so context below draws on general pharmacological knowledge of Pregabalin as a gabapentinoid. Among the five candidates, **Migraine Disorder** stands out as the only one with a completed randomized trial, a network meta-analysis, and multiple supporting cohort studies (**Evidence Level L2, "Proceed with Guardrails"**), even though it does not carry the single highest TxGNN score. The top-scoring candidate, **Tendinitis** (score 99.71%), is supported only by perioperative pain-control studies unrelated to tendon pathology itself (**L4, "Research Question"**). Three further candidates — myositis fibrosa, idiopathic granulomatous myositis, and inclusion body myositis — have **no clinical trial or literature support at all** and are recommended **Hold**.

## Quick Overview (Lead Candidate: Migraine Disorder)

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (drug is not marketed in Taiwan; no license records on file) |
| Predicted New Indication | Migraine Disorder (migraine prophylaxis) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

### All Candidate Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Tendinitis | 99.71% | L4 | S1 | Research Question |
| 2 | Myositis fibrosa | 99.71% | L5 | S0 | Hold |
| 3 | Idiopathic granulomatous myositis | 99.71% | L5 | S0 | Hold |
| 4 | Inclusion body myositis | 99.52% | L5 | S0 | Hold |
| **5** | **Migraine disorder** | **99.47%** | **L2** | **S2** | **Proceed with Guardrails** |
| 6 | Migraine with brainstem aura | 99.43% | L4 | S1 | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on general pharmacological knowledge, Pregabalin is a gabapentinoid that binds the α2δ subunit of voltage-gated calcium channels, reducing excitatory neurotransmitter release and central neuronal excitability; it is best known for neuropathic pain and adjunctive epilepsy treatment. This same mechanism — dampening cortical hyperexcitability — has a documented, biologically plausible extension to migraine: preclinical imaging studies (PMID 28223480, 37924146) show Pregabalin raises the threshold for and inhibits propagation of cortical spreading depolarization/depression, the phenomenon underlying migraine aura, via P/Q-type calcium channel inhibition. This places Pregabalin mechanistically alongside already-approved migraine-preventive antiepileptics such as topiramate and valproate.

By contrast, the three myositis-type candidates (fibrosing, granulomatous, inclusion body) require anti-inflammatory, immunomodulatory, or anti-fibrotic activity that Pregabalin does not possess — its calcium-channel modulation has no known effect on muscle inflammation or fibrosis, which is consistent with the complete absence of trial or literature evidence for these three candidates. Tendinitis sits in between: existing literature supports Pregabalin only as a perioperative analgesic/opioid-sparing agent after tendon surgery (e.g., rotator cuff repair), not as a treatment for the tendon pathology itself.

## Clinical Trial Evidence — Migraine Disorder

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) | Phase 3 | Withdrawn | 70 | Only trial designed specifically to compare Pregabalin vs. sodium valproate for migraine prevention; withdrawn before enrollment, no data generated |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Phase 4 | Completed | 200 | Neuroimaging study of chronic migraine/fibromyalgia "brain signatures" for chronic pain; not a direct efficacy trial |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3300 | EMR-based pragmatic registry across 10 neurological disorders; not a targeted Pregabalin-migraine intervention trial |

## Literature Evidence — Migraine Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | Compares preventive medications, including Pregabalin, for pediatric migraine prophylaxis |
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iranian J Child Neurology | Pregabalin vs. sodium valproate in pediatric migraine prophylaxis |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Medica Iranica | Pregabalin vs. propranolol for childhood migraine prophylaxis |
| [23797675](https://pubmed.ncbi.nlm.nih.gov/23797675/) | 2013 | Cochrane Systematic Review | Cochrane Database Syst Rev | Reviews gabapentin/Pregabalin specifically for episodic migraine prophylaxis in adults |
| [21479703](https://pubmed.ncbi.nlm.nih.gov/21479703/) | 2011 | Cohort (open-label) | J Headache Pain | 3-month follow-up on efficacy/tolerability of Pregabalin as migraine preventive |
| [25669613](https://pubmed.ncbi.nlm.nih.gov/25669613/) | 2015 | Cohort | Int J Clin Pharmacol Ther | Pregabalin reduces central sensitization/allodynia in migraine patients |
| [19935409](https://pubmed.ncbi.nlm.nih.gov/19935409/) | 2010 | Open-label study | Clinical Neuropharmacology | Pregabalin in chronic migraine prevention |
| [20464594](https://pubmed.ncbi.nlm.nih.gov/20464594/) | 2010 | Review | Neurological Sciences | Migraine preventive strategy in patients with comorbid mood/anxiety disorders |
| [30880369](https://pubmed.ncbi.nlm.nih.gov/30880369/) | 2019 | Review | Curr Treat Options Neurol | Status of antiepileptic drugs, including Pregabalin, as migraine preventive therapy |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | Mechanistic (animal imaging) | PNAS | Pregabalin inhibits cortical spreading depression, the proposed mechanistic basis for migraine aura |

## Clinical Trial & Literature Evidence — Other Candidates

**Tendinitis** (rank 1, L4): No registered clinical trials. 6 publications, dominated by case reports and perioperative pain-control RCTs (e.g., [PMID 32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/), [PMID 34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) — Pregabalin for post-rotator-cuff-surgery analgesia), none targeting tendinitis as a disease.

**Myositis fibrosa / Idiopathic granulomatous myositis / Inclusion body myositis** (ranks 2–4, L5): Currently no related clinical trials registered. Currently no related literature available.

**Migraine with brainstem aura** (rank 6, L4): No registered clinical trials. 3 publications, all mechanistic/animal or general migraine reviews — no subtype-specific clinical data.

## Taiwan Market Information

Pregabalin is currently **not marketed in Taiwan** — 0 licenses are on file in this evidence pack, so no product/dosage-form table can be produced.

## Safety Considerations

- **Drug Interactions**: 183 total interactions on file. Notable **Major**-level interactions: **Morphine** and **Morphine (liposomal)** — combined CNS/respiratory depression risk. Multiple **Moderate**-level interactions with other CNS depressants and opioid-class agents (Difenoxin, Diphenoxylate, Dronabinol, Nabilone, Opium), the antiemetic Metoclopramide, the appetite suppressant Sibutramine, and thiazolidinediones (Pioglitazone, Rosiglitazone, Troglitazone).

Detailed key warnings and contraindications are not available in this evidence pack — please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Migraine Disorder — the lead candidate); **Hold** on the three myositis-type candidates; **Research Question** stage for Tendinitis and Migraine with Brainstem Aura.

**Rationale:**
- Migraine disorder is backed by a completed RCT-supported evidence base, a network meta-analysis, and a mechanistically plausible link (cortical spreading depression inhibition) consistent with already-approved antiepileptic migraine preventives — sufficient to proceed cautiously.
- The three myositis-type candidates have zero clinical or literature support and no plausible mechanistic basis; further investment is not warranted at this time.
- Tendinitis, despite the highest raw TxGNN score, is supported only by perioperative analgesia studies rather than disease-modifying evidence, so it remains a research question rather than an actionable candidate.

**To proceed, the following is needed:**
- Pregabalin's confirmed original indication and MOA (both flagged as data gaps in this pack)
- TFDA/package-insert warnings, contraindications, and full DDI clinical significance review (currently unavailable)
- A dedicated Phase 2/3 RCT for Pregabalin in adult migraine prophylaxis (NCT00447369 was withdrawn without generating data)
- Regulatory pathway assessment given Pregabalin is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

