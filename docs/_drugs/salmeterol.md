---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 7
---

# Salmeterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using no additional skills — this is a direct content-generation task per the supplied template, not a coding/debugging task.

---

# Salmeterol: From Asthma/COPD Maintenance Therapy to Chronic Bronchitis

## One-Sentence Summary

> Salmeterol is a long-acting β2-adrenergic agonist (LABA) bronchodilator, established for maintenance therapy of asthma and chronic obstructive pulmonary disease (COPD).
> The TxGNN model predicts it may be effective for **Chronic Bronchitis**,
> with **17 clinical trials** and **20 publications** currently supporting this direction — though this largely confirms an already-recognized indication rather than a truly novel use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (Data Gap — original_indications and label MOA pending retrieval); pharmacological class (LABA bronchodilator) is used for asthma/COPD maintenance |
| Predicted New Indication | Chronic Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (flagged as a data gap, DG002). Based on the supporting clinical evidence and the model's own repurposing rationale, salmeterol belongs to the long-acting β2-adrenoceptor agonist (LABA) bronchodilator class. It relaxes bronchial smooth muscle via the Gs–cAMP–PKA pathway and has also been shown to improve mucociliary and cough clearance — a mechanism directly relevant to the pathophysiology of chronic bronchitis.

Chronic bronchitis is one of the two classic clinical phenotypes within the COPD disease spectrum (alongside emphysema). Salmeterol, particularly in combination with inhaled corticosteroids (e.g., fluticasone/salmeterol, "Advair/Seretide"), is already internationally approved and widely used for "COPD associated with chronic bronchitis" — this is explicitly reflected in several of the retrieved trial titles and abstracts below. The TxGNN prediction is therefore mechanistically sound, but it should be interpreted as **validation of an established indication** rather than discovery of a genuinely new therapeutic application.

It is worth noting that several other TxGNN-predicted indications for this drug in the same evidence pack (e.g., "respiratory malformation," "Rienhoff syndrome," "asthma-related traits, susceptibility to") were independently assessed as mechanistically implausible or unsupported by any evidence (Evidence Level L5, recommendation: Hold), reflecting known limitations of graph-based link prediction near densely connected "respiratory system" nodes. Chronic bronchitis, asthma, and obstructive lung disease — the top three ranked candidates — are the ones with genuine mechanistic and clinical support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | Completed | 130 | Salmeterol/fluticasone propionate 50/500mcg BID vs placebo on airway inflammation in COPD |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | Completed | 584 | 6-month comparison of tiotropium, salmeterol, and placebo bronchodilator efficacy/safety in COPD |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | Multicenter active-controlled study of long-acting bronchodilator maintenance therapy in COPD |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month chronic safety study of long-acting bronchodilator therapy in COPD |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A (PMS) | Completed | 2000 | Special drug use investigation of salmeterol/fluticasone in COPD (chronic bronchitis/emphysema), focused on pneumonia risk |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | Completed | 122 | Long-term (56-week) safety study of salmeterol/fluticasone (GW815SF) in COPD (chronic bronchitis, emphysema) |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | Completed | 247 | Fluticasone/salmeterol HFA MDI vs Diskus in COPD associated with chronic bronchitis (US label dose) |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | Completed | 639 | Fluticasone/salmeterol vs salmeterol alone on COPD exacerbation rate post-hospitalization |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Phase 4 | Completed | 249 | Fluticasone/salmeterol Diskus vs placebo effect on arterial stiffness in COPD |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | Completed | 457 | Dose-finding trial of fluticasone/formoterol benchmarked against fluticasone/salmeterol (Advair) in COPD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | RCT | Pulmonary Pharmacology & Therapeutics | Salmeterol's acute effect on mucociliary and cough clearance in chronic bronchitis patients |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | Efficacy and safety of fluticasone propionate/salmeterol Diskus combination for COPD treatment |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohort | Current Medical Research and Opinion | Healthcare utilization/costs in chronic bronchitis patients initiating fluticasone/salmeterol vs other maintenance therapies |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review/Guideline | Basic & Clinical Pharmacology & Toxicology | Finnish national COPD guideline covering diagnosis and pharmacotherapy of stable COPD |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | Review of salmeterol/fluticasone DPI use in COPD associated with chronic bronchitis |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Patient Experience Trial | MedGenMed | Management of COPD associated with chronic bronchitis using fluticasone/salmeterol 250/50 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Meta-analysis | Respiratory Research | Pooled analysis showing improved outcomes with salmeterol vs placebo/usual therapy in COPD |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | Open-label Study | Clinical Therapeutics | Efficacy, tolerability, and QOL of inhaled salmeterol vs oral theophylline in mild-to-moderate COPD |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Safety Study | Therapeutic Advances in Respiratory Disease | One-year safety/tolerance evaluation of arformoterol and salmeterol in COPD |
| [10832348](https://pubmed.ncbi.nlm.nih.gov/10832348/) | 2000 | Review | MMW Fortschritte der Medizin | Full pharmacological treatment spectrum (including bronchodilators) for smokers with chronic bronchitis/emphysema |

---

## Safety Considerations

**Drug Interactions** (598 total interactions on record; representative examples):

- **Clarithromycin** — Major interaction (CYP3A4-mediated increase in salmeterol exposure; cardiovascular risk)
- **Epinephrine** — Moderate interaction (additive cardiovascular/sympathomimetic effects)
- **Antidiabetic agents** (Acarbose, Alogliptin, Albiglutide, Canagliflozin, Dapagliflozin, Empagliflozin, Chlorpropamide, Dulaglutide) — Moderate interactions (β2-agonists may attenuate glycemic control)
- **Corticosteroids** (Hydrocortisone, Triamcinolone, Dexamethasone, Beclomethasone dipropionate, Betamethasone, Budesonide) — Minor interactions (commonly co-administered as ICS/LABA combination therapy)

Formal key warnings and contraindications are not available in this evidence pack; refer to the package insert once retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2–4 trials (some large-scale, n>500) directly support salmeterol's bronchodilator efficacy in COPD/chronic bronchitis, meeting L1 evidence criteria — but this is confirmatory of an existing indication class, not a novel signal, and two blocking/high-severity data gaps (label warnings/contraindications, formal MOA) prevent a full safety sign-off.

**To proceed, the following is needed:**
- Retrieve official label (warnings, contraindications) — currently blocking (DG001)
- Retrieve formal MOA documentation from DrugBank (DG002)
- Confirm original approved indication and registration pathway, since the drug is currently unregistered/not marketed in this jurisdiction
- Clarify positioning relative to existing salmeterol combination products already approved for COPD/chronic bronchitis elsewhere, to determine whether this represents a true label-extension opportunity or a market-entry decision only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

