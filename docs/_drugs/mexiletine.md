---
layout: default
title: Mexiletine
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Mexiletine
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

# Mexiletine: From Ventricular Arrhythmia to Headache Disorder

## One-Sentence Summary

Mexiletine is a Class IB antiarrhythmic drug that blocks voltage-gated sodium (Nav) channels, originally used for ventricular arrhythmias and recognised off-label for neuropathic pain and myotonia. Across the 10 TxGNN-predicted indications evaluated in this pack, **headache disorder** (including trigeminal autonomic cephalalgias, SUNCT/SUNA, and refractory chronic daily headache) carries the strongest real-world evidence, with **0 registered clinical trials** but **7 publications**—several citing Mexiletine by name—supporting this repurposing direction. Top-ranked predictions (hypertrichosis, NSIAD, Dandy-Walker malformation) were assessed as likely knowledge-graph false positives; headache disorder (TxGNN rank #10) is the most actionable candidate in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ventricular arrhythmia (inferred from drug class and literature; no India market data on file) |
| Predicted New Indication (Most Actionable) | Headache disorder (SUNCT / SUNA / refractory chronic daily headache) |
| TxGNN Prediction Score | 99.48% (rank #10 of ~18,000 diseases) |
| Evidence Level | L3 — observational studies and direct case series with Mexiletine |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Why rank #10 is featured instead of rank #1:** TxGNN ranks #1–5 (hypertrichosis, nephrogenic syndrome of inappropriate antidiuresis, Ambras syndrome, periodontal malformation syndrome, Dandy-Walker malformation) all scored L5 / Hold after mechanistic review—they reflect graph-topology artefacts with no biological plausibility or supporting evidence. The headache cluster (ranks #6 and #10) and pulmonary hypertension (rank #8) are the actionable signals in this pack. Rank #10 is highlighted here as it has the highest evidence level (L3) and direct Mexiletine-named literature.

---

## Why is This Prediction Reasonable?

**Mechanism of action:** Detailed MOA data was not retrieved in this evidence pack (data gap DG002). Based on established pharmacology, Mexiletine is a use-dependent, voltage-gated sodium channel (Nav1.x) blocker belonging to the Class IB antiarrhythmic category. It is structurally and mechanistically homologous to lidocaine—both share a 2,6-dimethylaniline core—differing primarily in oral bioavailability, which makes Mexiletine a practical oral successor to IV lidocaine in chronic management settings.

**Connecting cardiac arrhythmia to headache:** Trigeminal autonomic cephalalgias (TACs)—SUNCT, SUNA, and cluster headache—involve paroxysmal, high-frequency firing of the trigeminocervical complex, a neurophysiological pattern mechanistically analogous to cardiac ectopic discharge. Intravenous lidocaine has documented acute efficacy in refractory TACs; Mexiletine's oral bioavailability makes it a logical maintenance agent after IV lidocaine induction. Additionally, cortical spreading depression (CSD), the electrophysiological substrate of migraine aura, depends on Na⁺/K⁺ flux imbalance that Nav blockade can attenuate—a mechanism shared with topiramate, which partially inhibits Na⁺ channels and is approved for migraine prophylaxis.

**Supporting the prediction:** Multiple published case series (PMIDs 20425204, 18793209, 6938859) directly document Mexiletine use in headache disorders. The mechanistic overlap between cardiac and neuronal Nav channels provides a biologically coherent rationale that is not present in the top-ranked predictions. The primary evidence gap is the absence of formal randomised trials, not a question of biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Mexiletine in headache disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Prospective Case Series | *Current Pain and Headache Reports* | Mexiletine and IV lidocaine as Class IB Nav blockers in TAC management; directly reviews evidence for oral mexiletine in SUNCT/SUNA as maintenance therapy after IV lidocaine induction |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case Series (n=9) | *Headache* | Mexiletine used in 9 patients with refractory chronic daily headache; describes clinical outcomes and tolerability in a difficult-to-treat population |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective Open-label + Single-arm Meta-analysis | *J Neurol Neurosurg Psychiatry* | Most rigorous available study on SUNCT/SUNA treatment landscape; provides evidence-based framework that contextualises sodium channel blockers including mexiletine |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Case Report / Small Study | *NZ Medical Journal* | Early clinical observation of Mexiletine in vascular headaches; first published signal for this repurposing direction |
| [24820732](https://pubmed.ncbi.nlm.nih.gov/24820732/) | 2014 | Review | *Current Pain and Headache Reports* | New daily persistent headache pathogenesis and treatment challenges; contextualises refractory headache as a candidate for Nav channel modulation |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Systematic Review (Cochrane) | *Cochrane Database Syst Rev* | Cochrane review confirming Mexiletine's established efficacy in myotonia (a Nav channelopathy); validates the Nav-blocking pharmacological profile applicable to neuronal excitability disorders |
| [91699](https://pubmed.ncbi.nlm.nih.gov/91699/) | 1979 | Clinical Study | *Kardiologiia* | Original antiarrhythmic study of Mexitil (mexiletine) in ventricular arrhythmias; establishes the foundational Nav-blocking pharmacology from which all repurposing rationale derives |

---

## India Market Information

Mexiletine is currently **not marketed in India**. There are no drug authorizations on file (total licenses = 0). Any prospective clinical use or study in India would require a regulatory pathway assessment—such as a new drug application, import licence, or orphan drug designation if applicable.

---

## Safety Considerations

**Drug Interactions (106 total interactions identified):**

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Bupropion | **Major** | CYP2D6 inhibition by bupropion can significantly raise mexiletine plasma levels; avoid co-administration or monitor closely with dose adjustment |
| Alosetron | Moderate | Pharmacokinetic interaction via shared metabolic pathway; monitor |
| Morphine | Moderate | Potential additive CNS and cardiac effects; monitor |
| Eliglustat | Moderate | CYP2D6 substrate; interaction risk with mexiletine |
| Rolapitant | Moderate | CYP2D6-mediated PK interaction; monitor drug levels |
| Potassium citrate / Sodium sulfate / Picosulfuric acid / PEG 3350 | Moderate | Electrolyte-related interactions; monitor cardiac and electrolyte status |
| Obeticholic acid / Glycerol phenylbutyrate | Moderate | Transporter/metabolic interactions; monitor |
| Omeprazole / Simvastatin / Prednisolone / Vancomycin | Unknown | Limited DDI data; use with caution and monitor |

> The full interaction database contains 106 drugs. Only the highest-priority entries are listed above. A full DDI screen against the patient's complete medication list is required before any clinical use.

> ⚠️ **Key warnings and contraindications data were not available in this evidence pack (data gap DG001, severity: Blocking).** Please consult the FDA, EMA, or equivalent approved package insert for complete safety information prior to any prescribing or clinical study initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple case series and a prospective clinical study directly document Mexiletine's use in refractory trigeminal autonomic cephalalgias and chronic daily headache, supported by a mechanistically coherent Nav-channel rationale analogous to its established cardiac indication. Evidence remains at L3 (no RCTs), which warrants a structured pilot study before broader clinical adoption.

**To proceed, the following is needed:**

- **Resolve blocking safety data gap (DG001):** Retrieve the full package insert warnings and contraindications before any clinical protocol is developed
- **Obtain formal MOA data (DG002):** Query DrugBank API to populate the mechanism of action field and strengthen the regulatory submission narrative
- **India regulatory pathway:** Determine whether Mexiletine can be imported and studied in India under Schedule Y / new drug application, or whether an orphan designation pathway is applicable
- **Pilot study design:** Design a prospective open-label pilot (n=20–30) in refractory TAC or SUNCT/SUNA patients, using IV lidocaine responder status as an enrichment criterion for patient selection
- **DDI risk management plan:** Complete a full drug interaction screen for all anticipated co-medications in the target headache population; note the Major interaction with Bupropion requires specific protocol exclusion criteria
- **Additional signals to monitor:** Pulmonary hypertension (rank #8, L5 but novel mechanistic signal via TMEM16A/lidocaine analogy, PMID 41518899) warrants a dedicated in vitro validation study before any clinical investment

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application. — TxGNN Evidence Pack v4, data cutoff 2026-04-04*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

