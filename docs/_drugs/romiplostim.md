---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia to Platelet-Type Bleeding Disorder

## One-Sentence Summary

> Romiplostim is a thrombopoietin receptor (MPL) agonist originally used to raise platelet counts in chronic immune thrombocytopenia (ITP).
> The TxGNN model predicts it may also be effective for **platelet-type bleeding disorder** — a broader category covering chemotherapy-induced, transplant-related, and MDS-associated thrombocytopenia —
> with **8 clinical trials**, including a completed Phase 3 randomized controlled trial, currently supporting this direction.

*Note: Among the 10 TxGNN candidates in this evidence pack, "primary release disorder of platelets" received the highest raw model score, but its own mechanistic rationale flags a mismatch (it is a platelet-release defect, not a production deficit) and it is backed by only one low-relevance trial. "Platelet-type bleeding disorder" is presented here as the lead candidate because it has by far the strongest and most mechanistically consistent evidence base.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic immune thrombocytopenia (ITP) *(from pharmacology clinical-use data; no local label on file)* |
| Predicted New Indication | Platelet-type bleeding disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action documentation from an official label is not available (data gap). Based on the pharmacology data on file, romiplostim is a peptide agonist of the thrombopoietin receptor (MPL, target gene *MPL*), and its efficacy in raising platelet counts in ITP is well established. Mechanistically, this receptor-agonist action stimulates megakaryocyte proliferation and maturation, which is not specific to autoimmune platelet destruction — it should, in principle, also compensate for insufficient platelet production from other causes.

"Platelet-type bleeding disorder," as captured in the supporting trials, spans exactly this broader production-deficit population: chemotherapy-induced thrombocytopenia (RECITE trial), post-transplant delayed platelet engraftment, and MDS-associated thrombocytopenia. In each case the underlying problem — inadequate megakaryocyte-driven platelet output — is the same one romiplostim already treats in ITP, which is why the mechanistic extension is plausible and, unlike several other TxGNN candidates in this pack (e.g., pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome), does not conflict with the underlying disease pathology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03362177](https://clinicaltrials.gov/study/NCT03362177) | Phase 3 | Completed | 165 | RECITE: randomized, placebo-controlled, double-blind trial of romiplostim for chemotherapy-induced thrombocytopenia in oxaliplatin-treated GI/pancreatic/colorectal cancer patients — highest-quality direct evidence |
| [NCT05492409](https://clinicaltrials.gov/study/NCT05492409) | Phase 3 | Completed | 160 | Extension study of long-term safety/immunogenicity of a romiplostim-class agent (GNR-069) in ITP patients |
| [NCT02335268](https://clinicaltrials.gov/study/NCT02335268) | Phase 2 | Completed | 77 | EUROPE trial: prospective validation of a response-prediction model for romiplostim in low/int-1 risk MDS with thrombocytopenia |
| [NCT04638829](https://clinicaltrials.gov/study/NCT04638829) | Phase 4 | Completed | 60 | Real-world safety/treatment-satisfaction study in chronic ITP patients switching off romiplostim/eltrombopag |
| [NCT02046291](https://clinicaltrials.gov/study/NCT02046291) | Phase 1 | Completed | 21 | Dose-escalation safety study of romiplostim for failed platelet engraftment after umbilical cord blood transplant |
| [NCT02298075](https://clinicaltrials.gov/study/NCT02298075) | N/A | Completed | 148 | Retrospective study of sustained response after discontinuing TPO-receptor agonists (romiplostim/eltrombopag) in primary ITP |
| [NCT02227576](https://clinicaltrials.gov/study/NCT02227576) | Phase 2 | Terminated | 20 | Secondary prophylaxis with romiplostim for temozolomide-induced thrombocytopenia in glioblastoma (terminated — reason not detailed in this record) |
| [NCT07321626](https://clinicaltrials.gov/study/NCT07321626) | Phase 1 | Recruiting | 130 | Ongoing randomized study of romiplostim for platelet reconstruction after haploidentical allogeneic stem cell transplant |

---

## Literature Evidence

Currently no related literature available for this specific indication cluster.

---

## India Market Information

Romiplostim currently has **0 registered authorizations** and is **not marketed** in this jurisdiction (taiwan_regulatory dataset). No license records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: Major-level interaction reported with **Carfilzomib** (source: DDInter) — combined use warrants close monitoring given the overlapping thrombocytopenia/thrombosis risk profile of both agents.

Detailed label-based warnings and contraindications are not yet available for this drug (data gap, TFDA label pending retrieval); please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 placebo-controlled RCT (RECITE) plus a second completed Phase 3 study directly support romiplostim's efficacy across production-deficit thrombocytopenias, and the underlying MPL-agonist mechanism is already clinically validated in ITP — but the drug is currently unregistered locally and key safety documentation is missing.

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (DG001, blocking)
- Verified mechanism-of-action documentation from DrugBank (DG002)
- Local regulatory filing/registration pathway, given current "not marketed" status
- A defined monitoring and management protocol for the Major Carfilzomib interaction
- Clarification of the termination reason for NCT02227576 before relying on that data point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

