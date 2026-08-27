---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Heart Failure to Alopecia

## One-Sentence Summary

Dobutamine is a synthetic catecholamine and β1-adrenergic agonist, used clinically as an inotropic agent for acute decompensated heart failure and cardiogenic shock.
The TxGNN model predicts it may be effective for **Alopecia** with a score of 99.85%, however **no directly relevant clinical trials** exist and the only **2 retrieved publications** are unrelated to this use.
Mechanistic analysis suggests this high-scoring prediction is most likely a **knowledge graph artefact** rather than a genuine repurposing signal — all 10 predicted indications carry an L5 evidence level and a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute heart failure / Cardiogenic shock (short-term inotropic support) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed (CDSCO) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Dobutamine is a selective β1-adrenergic receptor agonist (with minor β2 and α1 activity) that increases cardiac output by enhancing myocardial contractility and heart rate. It is administered exclusively by continuous intravenous infusion in acute care settings. There is no known biological pathway by which β1-adrenergic stimulation would promote hair follicle growth, arrest follicle miniaturisation, or modulate immune-mediated follicle damage.

Alopecia involves pathological hair loss through diverse mechanisms — immune-mediated T-cell attack on follicles (alopecia areata), androgen-driven follicle miniaturisation (androgenetic alopecia), or structural follicle defects. None of these pathways have an established connection to adrenergic signalling, let alone to β1-selective agonism.

The high TxGNN score almost certainly reflects a **knowledge graph artefact**: Minoxidil (a well-known topical hair loss treatment) causes cardiac side effects → cardiac toxicity cases may require Dobutamine for haemodynamic support → this indirect path creates an erroneous graph edge linking Dobutamine to hair loss. Both retrieved literature results (PMID 41046802: cat with minoxidil-induced heart failure; PMID 17505274: colchicine-poisoning with incidental hair loss) confirm this interpretation — neither paper involves Dobutamine in the context of treating alopecia. This KG confound appears to propagate across the top 4 ranked predictions, all of which involve hair-related conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The two retrieved publications for the top-ranked indication (alopecia) are not directly relevant to Dobutamine as a treatment. Both confirm the KG artefact hypothesis described above.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Veterinary) | Journal of Veterinary Cardiology | Cat developed left-sided congestive heart failure from **minoxidil intoxication**; Dobutamine was used for haemodynamic support of hypotension — no connection to alopecia treatment |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report (Pediatric) | Pediatric Emergency Care | Child with acute colchicine poisoning; hair loss appeared in the recovery phase as a known colchicine effect — Dobutamine not involved in alopecia context |

> Neither publication supports Dobutamine as a treatment for alopecia. These results are consistent with the KG artefact pathway (Minoxidil → cardiac toxicity → Dobutamine rescue) rather than a genuine pharmacological signal.

---

## India Market Information

Dobutamine has no products currently registered with CDSCO and is not marketed in India. There are no authorisation records available for review.

---

## Safety Considerations

**Drug Interactions:** A total of 99 drug-drug interactions have been identified (source: DDInter). The 20 documented interactions below are all classified as **Moderate** severity. Notable clustering around antidiabetic agents (GLP-1 agonists, SGLT2 inhibitors, insulins, sulfonylureas) suggests particular vigilance is warranted in patients with concurrent diabetes management.

| Interacting Drug | Level | Clinical Class |
|-----------------|-------|----------------|
| Acarbose | Moderate | Alpha-glucosidase inhibitor |
| Albiglutide | Moderate | GLP-1 receptor agonist |
| Alogliptin | Moderate | DPP-4 inhibitor |
| Metformin | Moderate | Biguanide |
| Pioglitazone | Moderate | Thiazolidinedione |
| Canagliflozin | Moderate | SGLT2 inhibitor |
| Chlorpropamide | Moderate | Sulfonylurea |
| Cimetidine | Moderate | H2 receptor antagonist |
| Dapagliflozin | Moderate | SGLT2 inhibitor |
| Diethylpropion | Moderate | Sympathomimetic / appetite suppressant |
| Dulaglutide | Moderate | GLP-1 receptor agonist |
| Empagliflozin | Moderate | SGLT2 inhibitor |
| Linagliptin | Moderate | DPP-4 inhibitor |
| Phentermine | Moderate | Sympathomimetic / appetite suppressant |
| Repaglinide | Moderate | Meglitinide |
| Semaglutide | Moderate | GLP-1 receptor agonist |
| Vancomycin | Moderate | Glycopeptide antibiotic |
| Insulin aspart | Moderate | Rapid-acting insulin |
| Insulin degludec | Moderate | Long-acting insulin |
| Liraglutide | Moderate | GLP-1 receptor agonist |

> For complete warnings, contraindications, and the full interaction list of 99 agents, please refer to the official package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dobutamine carry an **L5 evidence level** (model prediction only, no direct supporting studies), and the highest-ranked prediction — alopecia — is assessed as a **probable knowledge graph artefact** with no mechanistic basis. The drug's well-established role as an acute intravenous cardiac inotrope is fundamentally incompatible with the dermatological and ophthalmological conditions appearing in the top 10 predictions. Proceeding with any of these indications in their current state would not be scientifically justified.

**To proceed, the following would be needed:**

- **KG audit**: Confirm and correct the suspected Minoxidil → cardiac toxicity → Dobutamine artefact path in the TxGNN knowledge graph before re-running predictions
- **MOA data**: Retrieve complete mechanism of action from DrugBank API to support any future mechanistic plausibility analysis (Data Gap DG002)
- **Safety dossier**: Download and parse CDSCO/package insert PDF to populate warnings and contraindications (Data Gap DG001 — currently Blocking severity)
- **Preclinical evidence**: Any in vitro or in vivo data linking β-adrenergic signalling to the predicted indication would be required before any clinical consideration
- **CDSCO registration pathway**: If a valid repurposing signal were ever identified, a de novo registration strategy for India would be needed given zero existing market presence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

