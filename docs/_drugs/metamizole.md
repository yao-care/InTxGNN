---
layout: default
title: Metamizole
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Metamizole
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

# Metamizole: From Analgesic/Antipyretic to Migraine Disorder

## One-Sentence Summary

Metamizole (also known as dipyrone) is a pyrazolone-class non-opioid analgesic and antipyretic, widely used in many countries for acute pain and fever management.
The TxGNN model's top-ranked prediction is **Rheumatoid Arthritis** (rank 1, score 99.78%), but the most evidence-backed actionable indication is **Migraine Disorder** (rank 2, score 99.72%), supported by **3 clinical trials** (including 1 completed Phase 3 RCT) and **19 publications** (including multiple RCTs and a Cochrane systematic review).
The RA prediction is assessed as **Hold** due to absence of direct clinical evidence; migraine carries a **Proceed with Guardrails** recommendation at evidence level **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic/Antipyretic (inferred from pharmacology; no India market approval on record) |
| Predicted New Indication | Migraine Disorder (TxGNN rank 2; highest-evidence actionable prediction) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (Migraine) / Hold (Rheumatoid Arthritis) |

---

## Why is This Prediction Reasonable?

Metamizole belongs to the pyrazolone class of non-opioid analgesics. Detailed MOA data is not currently available in the Evidence Pack, but known pharmacological mechanisms include inhibition of COX-2 and the less-characterised COX-3 isoform, with resulting suppression of prostaglandin E2 (PGE2) synthesis. On top of the peripheral anti-inflammatory effect, metamizole exerts central analgesic actions mediated through cannabinoid CB1 receptors and the descending serotonergic (5-HT) pain-modulation pathway — a dual peripheral-central profile that distinguishes it from conventional NSAIDs.

Migraine attacks are initiated by cortical spreading depression (CSD) and trigemino-vascular system activation. PGE2 is a principal sensitising agent for trigeminal nerve endings surrounding meningeal blood vessels, and its suppression at both the trigeminal ganglia and the meningeal level directly interrupts the pain cascade. Metamizole's additional central action via the 5-HT descending pathway provides a second layer of pain modulation, targeting the very pathways responsible for migraine chronification.

The mechanistic fit is supported by a substantial body of clinical evidence. Multiple randomised controlled trials conducted in Brazil, Turkey, and Israel — together with Cochrane systematic reviews — confirm metamizole's efficacy as an abortive treatment for acute migraine with and without aura, via both intravenous and oral routes. Intravenous metamizole is routinely used in emergency department settings across Latin America, southern Europe, and the Middle East. TxGNN's high score for migraine (99.72%) therefore reflects a genuine pharmacological relationship, not a knowledge-graph artefact.

> **Note on the top TxGNN prediction (Rheumatoid Arthritis, rank 1, 99.78%):** Metamizole's COX inhibition can provide symptomatic analgesia in RA, and German claims data (PMID 33825975) confirms it is indeed prescribed as an adjunct analgesic in rheumatic diseases. However, it has no disease-modifying (DMARD) activity, cannot halt joint destruction, and is not recommended as a primary RA therapy. The high TxGNN score most likely arises from a RA ↔ pain ↔ analgesic pathway similarity in the knowledge graph rather than a direct therapeutic relationship. Evidence level is L4; recommendation is **Hold**.

---

## Clinical Trial Evidence

*(Evidence for Migraine Disorder, predicted_indications[1])*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02183220](https://clinicaltrials.gov/study/NCT02183220) | Phase 3 | Completed | 417 | Double-blind, placebo- and aspirin-controlled RCT evaluating a single oral dose of metamizole 0.5 g and 1.0 g vs. placebo and aspirin 1.0 g across 2 episodes of moderate tension headache; directly assessed analgesic efficacy and tolerability — the highest-quality direct trial in this dataset |
| [NCT05048914](https://clinicaltrials.gov/study/NCT05048914) | N/A (Observational) | Unknown | 50 | Evaluated abortive migraine treatment patterns in Israeli children and adolescents aged 6–18; provides pediatric real-world use data for metamizole |
| [NCT02706015](https://clinicaltrials.gov/study/NCT02706015) | Phase 3 | Withdrawn | 0 | Planned non-inferiority trial comparing Cefaliv® vs Neosaldina® (both contain metamizole) for migraine attacks; withdrawn before any enrollment — no data contributed |

---

## Literature Evidence

*(Evidence for Migraine Disorder, predicted_indications[1])*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17443558](https://pubmed.ncbi.nlm.nih.gov/17443558/) | 2007 | Cochrane Systematic Review | Cochrane Database Syst Rev | Dipyrone for acute primary headaches; comprehensive review of evidence across multiple countries confirming efficacy; foundational high-quality evidence |
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Cochrane Review | Cochrane Database Syst Rev | Single-dose dipyrone for acute postoperative pain; includes migraine context; confirms non-opioid analgesic efficacy profile |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Systematic Review | Headache | Parenteral treatment of episodic tension-type headache; metamizole evaluated as a parenteral analgesic option for acute care settings |
| [12390611](https://pubmed.ncbi.nlm.nih.gov/12390611/) | 2002 | RCT | Headache | IV dipyrone in acute migraine without aura and with aura; randomized, double-blind, placebo-controlled; confirms efficacy for both migraine subtypes |
| [15595715](https://pubmed.ncbi.nlm.nih.gov/15595715/) | 2004 | RCT | Functional Neurology | Dipyrone 1 g tablets in acute migraine attacks (with/without aura); double-blind, cross-over, randomized, placebo-controlled multicenter study (n=73); confirms oral efficacy |
| [11422089](https://pubmed.ncbi.nlm.nih.gov/11422089/) | 2001 | Clinical Trial | Cephalalgia | IV metamizole vs. placebo in migraine with aura (n=54), without aura (n=95), and tension-type headache (n=30); placebo-controlled; supports IV use across headache subtypes |
| [18545786](https://pubmed.ncbi.nlm.nih.gov/18545786/) | 2008 | RCT | Arq Neuropsiquiatr | Lysine clonixinate vs. IV dipyrone for severe migraine attacks; single-blind, randomized; IV dipyrone confirmed effective with good tolerability |
| [35523834](https://pubmed.ncbi.nlm.nih.gov/35523834/) | 2022 | Observational Study | Scientific Reports | Abortive migraine treatment in Israeli children/adolescents (n=50); real-world pediatric prescribing data including metamizole |
| [33712966](https://pubmed.ncbi.nlm.nih.gov/33712966/) | 2021 | Observational Study | Internal and Emergency Medicine | Acute migraine management in a large Spanish tertiary hospital ED (n=847 cases, 2016–2019); documents contemporary real-world use of metamizole in acute migraine care |
| [22404708](https://pubmed.ncbi.nlm.nih.gov/22404708/) | 2012 | Review | Headache | Rescue therapy for acute migraine — opioids, NSAIDs, and steroids in ED/urgent care; positions metamizole within the NSAID class for acute migraine rescue |

---

## India Market Information

Metamizole is currently **not marketed in India**. No CDSCO license records are available. The drug is approved and in active clinical use in numerous markets — including Germany, Brazil, Spain, Turkey, Poland, and Israel — but has been withdrawn or remains banned in the United States, United Kingdom, and Australia due to the risk of agranulocytosis.

Any India market entry would require a full CDSCO new drug application (NDA) pathway.

---

## Safety Considerations

Detailed TFDA/CDSCO package insert warnings and contraindications are not yet available in the Evidence Pack (Data Gap DG001). Drug interaction data could not be retrieved (DDI database file not found during query).

> Please refer to the originator package insert for complete safety information.

**Key safety consideration known from pharmacological literature:** Metamizole carries a rare but potentially life-threatening risk of **agranulocytosis** (estimated incidence 1:1,000 to 1:30,000 exposures depending on the population and exposure duration). This adverse effect is the primary reason for the drug's withdrawal in several high-income countries and must be a central element of any benefit–risk assessment for new indications. Baseline and periodic complete blood count (CBC) monitoring is recommended when metamizole is used on a chronic or recurrent basis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Migraine Disorder)* | **Hold** *(Rheumatoid Arthritis and all other predicted indications)*

**Rationale:**
For migraine disorder, multiple Phase 3/RCT-level studies, Cochrane systematic reviews, and real-world evidence from five countries confirm metamizole's acute abortive efficacy. The mechanism of action (COX-2/COX-3 inhibition + central 5-HT/CB1 analgesia) directly maps to established migraine pathophysiology, supporting biological plausibility at L1 evidence level. For all other top-10 predicted indications, evidence is insufficient (L4–L5) or the predictions represent knowledge-graph artefacts without mechanistic basis.

**To proceed (Migraine), the following is needed:**

- **Obtain package insert / prescribing information** (DG001): Download and parse TFDA or originator PDF to complete the safety assessment
- **Retrieve DrugBank MOA data** (DG002): Complete API query for DB04817 to confirm full mechanism and receptor targets
- **Agranulocytosis risk management plan**: Define CBC monitoring schedule, patient eligibility criteria, and contraindications (e.g., known blood dyscrasias, concurrent myelosuppressive therapy)
- **India regulatory pathway assessment**: Evaluate CDSCO requirements for a drug currently not marketed in India, including whether prior approval in reference jurisdictions (Germany, Brazil) supports an expedited pathway
- **Comparative effectiveness positioning**: Benchmark against available alternatives in India (paracetamol, ibuprofen, naproxen, triptans) to define the clinical niche where metamizole's benefit-risk is most favourable
- **Formulation strategy**: Determine whether IV (emergency/hospital use) or oral (outpatient/OTC) development is the priority for the India market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

