---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mefenamic Acid: From Pain and Dysmenorrhoea to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class non-steroidal anti-inflammatory drug (NSAID) established globally for mild-to-moderate pain, dysmenorrhoea, and menorrhagia, though it currently holds no marketing authorisation in India.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (rank 1 of 8 predicted indications),
with **0 registered clinical trials** and **20 publications** — including multiple randomised controlled trials — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, dysmenorrhoea, and inflammation (no India regulatory approval on record) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrievable at the time of this report. Based on available pharmacological information, mefenamic acid belongs to the fenamate subclass of NSAIDs and exerts its effects primarily through inhibition of both COX-1 and COX-2 enzymes, reducing synovial production of prostaglandin E2 (PGE2) and prostacyclin (PGI2). What distinguishes mefenamic acid from most other NSAIDs is its additional fenamate-structure-mediated antagonism of prostaglandin receptors — providing a dual anti-inflammatory benefit that goes beyond simple COX inhibition.

Rheumatoid arthritis is a chronic, systemic autoimmune disease in which persistent synovial inflammation, mediated substantially by prostaglandins, drives progressive joint destruction and pain sensitisation. This pathological profile directly overlaps with mefenamic acid's pharmacodynamic targets, making the TxGNN prediction mechanistically coherent. Unlike conditions driven by structural or genetic factors, RA's inflammatory core can plausibly be modulated by prostaglandin pathway suppression at multiple levels.

Importantly, this is not a purely theoretical prediction. Multiple head-to-head randomised controlled trials conducted between the mid-1960s and late 1970s directly evaluated mefenamic acid in RA patients, consistently demonstrating analgesic and anti-inflammatory efficacy comparable to ibuprofen, flurbiprofen, sulindac, aspirin, and phenylbutazone. A 1992 clinical study additionally reported a 75% response rate using mefenamic acid electrophoresis in 125 RA patients. The body of older but clinically relevant evidence, combined with the strong mechanistic rationale and a near-maximum TxGNN score, collectively support advancing this candidate to a guarded next stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (double-blind crossover) | Current Medical Research and Opinion | Mefenamic acid 1,500 mg/day vs flurbiprofen, sulindac, and placebo in 24 RA patients over 2-week periods; all active drugs significantly superior to placebo on pain score, articular index, and morning stiffness severity |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT (double-blind within-patient) | J Int Medical Research | Mefenamic acid vs ibuprofen in 40 RA patients; analgesic and anti-inflammatory effects statistically equivalent; side-effect profiles similar except slightly more drowsiness with ibuprofen |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | Comparative trial | Medical Journal of Australia | Double-blind crossover of mefenamic acid 1,500 mg/day vs ibuprofen 1,200 mg/day with background salicylates; mefenamic acid performed comparably with predominantly mild GI side-effects |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Clinical trial | British Medical Journal | Mefenamic acid and flufenamic acid compared head-to-head with aspirin and phenylbutazone in RA; one of the earliest formal efficacy comparisons |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Clinical trial | Annals of the Rheumatic Diseases | Methodological evaluation and drug comparison in RA outpatients; mefenamic acid and flufenamic acid benchmarked against phenylbutazone and aspirin |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Early clinical trial | Annals of the Rheumatic Diseases | Early controlled clinical evaluation of mefenamic acid specifically in rheumatoid arthritis |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Clinical evaluation | Journal of Rheumatology | Single-blind non-crossover study assessing analgesic action of 10 antirheumatic drugs (including mefenamic acid) in 684 RA patients using daily pain charts and patient satisfaction ratings |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Comprehensive narrative review consolidating evidence on mefenamic acid's clinical position in RA management |
| [1455792](https://pubmed.ncbi.nlm.nih.gov/1455792/) | 1992 | Clinical study | Voprosy Kurortologii | Novel electrophoresis delivery of mefenamic acid from dimexide solution in 125 RA patients; complete or partial responses in 75%; improvements in pain, immunity markers, and inflammation indices |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Epidemiological (case-crossover) | American Journal of Cardiology | Case-crossover study of 5,921 RA patients with stroke or AMI; evaluates transient cardiovascular risk associated with nonselective NSAID use (including mefenamic acid) — important safety reference for RA use |

---

## India Market Information

Mefenamic acid currently has **no registered products** in India. There are zero active marketing authorisations on record (CDSCO total registrations: 0). This means there is no locally approved prescribing information or dosage form available through Indian regulatory channels.

---

## Safety Considerations

**Drug Interactions (195 total interactions identified; key examples listed below):**

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Acetylsalicylic acid | Moderate | Concurrent NSAID use compounds GI bleeding and ulceration risk |
| Hydrocortisone / Dexamethasone / Betamethasone / Budesonide / Triamcinolone | Moderate | NSAID + corticosteroid combination substantially increases risk of GI ulceration and haemorrhage |
| Metformin | Moderate | NSAIDs may impair renal function, reducing metformin clearance and raising risk of lactic acidosis |
| Mesalazine / Balsalazide | Moderate | Pharmacodynamic interaction at GI mucosal level; monitor GI tolerability |
| Potassium citrate / Potassium bicarbonate | Moderate | NSAID-induced renal effects may alter potassium handling; electrolyte monitoring advised |
| Chlorpropamide | Moderate | NSAIDs can potentiate hypoglycaemic effects of sulphonylureas; blood glucose monitoring required |
| Aprepitant | Moderate | Potential pharmacokinetic interaction via CYP3A4 pathway |
| Famotidine / Ranitidine / Cimetidine | Minor | H2-blockers often co-prescribed for GI protection; minor pharmacokinetic interaction |
| Dapagliflozin | Minor | NSAIDs may reduce renal SGLT2 inhibitor efficacy; monitor renal function |

> **Note:** CDSCO prescribing information (detailed warnings and contraindications for India) was not available at the time of this report. Please consult the current package insert and CDSCO guidelines for a full list of contraindications and special precautions before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomised controlled trials — primarily from the 1960s to 1970s — directly evaluated mefenamic acid in RA patients and demonstrated efficacy comparable to established NSAIDs of that era; the mechanistically coherent dual COX inhibition and prostaglandin receptor antagonism, combined with the near-maximal TxGNN prediction score of 99.73%, provide sufficient scientific justification to advance this candidate — provided key safety and regulatory gaps are resolved first.

**To proceed, the following is needed:**

- **Retrieve CDSCO/package insert safety data** — warnings and contraindications are currently a Blocking data gap (DG001); a formal safety assessment cannot be completed without this
- **Confirm MOA data from DrugBank** — needed to complete the mechanistic link analysis and drug-disease compatibility assessment (DG002)
- **India regulatory pathway analysis** — mefenamic acid is not currently marketed in India; a new drug application or import licence pathway must be mapped with CDSCO
- **Cardiovascular and GI risk stratification** — given 195 identified DDIs and the RA population's inherent cardiovascular co-morbidities (see PMID 29548675), a dedicated safety monitoring protocol is required
- **Modern clinical validation** — existing RA evidence dates predominantly from the 1960s–1970s and does not meet contemporary ICH or CDSCO trial standards; a Phase 2 proof-of-concept study in an Indian RA cohort would substantially strengthen the regulatory dossier
- **Formulation and dosing optimisation** — India-specific dosage form registration and dose-finding studies should be included in the development plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

