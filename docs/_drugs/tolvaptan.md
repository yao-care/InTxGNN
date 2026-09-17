---
layout: default
title: Tolvaptan
parent: High Evidence (L1-L2)
nav_order: 840
evidence_level: L1
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using content synthesis (no applicable coding/debugging skill) to produce the report directly from the evidence pack per the fixed template.

# Tolvaptan: From Hyponatremia to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

> Tolvaptan is a vasopressin V2-receptor antagonist historically used for hyponatremia and fluid overload in heart failure.
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (ADPKD)**,
> with **0 registered clinical trials in this evidence pack** but **20 supporting publications**, including two completed Phase 3 RCTs (TEMPO 3:4, REPRISE) that already established this use elsewhere.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India regulatory data; per literature (PMID 26508187), tolvaptan is used for hyponatremia/fluid congestion in heart failure |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (ADPKD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record is currently unavailable for this drug (data gap DG002). However, evidence embedded in this pack's own literature and rationale fields fills the gap: tolvaptan is a selective vasopressin V2-receptor antagonist. By blocking V2 receptors in the renal collecting duct, it suppresses cyclic AMP (cAMP) generation in tubular epithelial cells.

cAMP is the central driver of cystogenesis in autosomal dominant polycystic kidney disease (ADPKD) — it stimulates both epithelial cell proliferation and fluid secretion into cysts. Because tolvaptan directly interrupts this cAMP pathway, its mechanistic link to ADPKD is not a distant analogy but a proven, on-target effect. This is why tolvaptan is already the only FDA-approved disease-modifying therapy for ADPKD (confirmed in PMID 40726372), and why the two pivotal Phase 3 RCTs in this evidence pack (TEMPO 3:4, PMID 23121377; REPRISE, PMID 29105594) demonstrated slowed total kidney volume growth and eGFR decline.

In short, this is less a speculative "new indication" and more a mechanistically direct, clinically validated use that has simply not yet been registered in the India market — which is reflected in the "Proceed with Guardrails" recommendation rather than a purely exploratory "Hold."

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack for this indication. (Note: the pivotal trials TEMPO 3:4 and REPRISE are captured as journal publications below, not as clinicaltrials.gov registry entries in this pack.)

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | The New England Journal of Medicine | TEMPO 3:4: tolvaptan slowed total kidney volume growth and eGFR decline in early-stage ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | The New England Journal of Medicine | REPRISE: tolvaptan preserved kidney function in later-stage ADPKD (eGFR 25–65 mL/min) |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (pediatric) | Pediatric Nephrology | Randomized trial (NCT02964273) of tolvaptan safety/pharmacodynamics in children (5–17y) with ADPKD |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrología | Confirms tolvaptan efficacy in delaying ADPKD progression to ESRD, with pooled safety data |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Review/Consensus | Nephrology, Dialysis, Transplantation | ERA/PKD International consensus statement on patient selection and monitoring for tolvaptan in ADPKD |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Confirms tolvaptan remains the only FDA-approved disease-modifying ADPKD therapy |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive ADPKD review covering epidemiology, genetics, and tolvaptan-based management |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Cochrane review of disease-modifying interventions (including tolvaptan) for ADPKD progression |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | Journal of Hepatology | EASL guideline on cystic liver disease; notes tolvaptan's role in slowing hepatic cyst growth |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | ADPKD/PLD review: tolvaptan slows renal function deterioration and cyst growth |

## India Market Information

Tolvaptan is currently **not marketed in India** — this evidence pack contains zero registered licenses (`total_licenses: 0`, `market_status: Not marketed`). There is no local approved-indication text to extract.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (blocking data gap DG001 — TFDA-equivalent package insert warnings/contraindications have not yet been sourced). Note that both pivotal RCTs (TEMPO 3:4, REPRISE) reported elevated aminotransferase and bilirubin levels with tolvaptan, indicating hepatotoxicity monitoring is clinically important even though formal labeling data is not yet in this pack.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (TEMPO 3:4, REPRISE) plus a consensus guideline (ERA/PKD International) and a Cochrane systematic review provide strong, mechanistically direct evidence (L1) that tolvaptan slows ADPKD progression. However, the drug has zero registrations in India and this pack is missing formal safety labeling data, so guardrails around safety monitoring and local regulatory filing are required before proceeding.

**To proceed, the following is needed:**
- TFDA/India-equivalent package insert with formal warnings and contraindications (blocking gap DG001)
- Confirmed DrugBank mechanism-of-action record (gap DG002)
- Liver function monitoring protocol (aminotransferase/bilirubin), given hepatotoxicity signals in both pivotal RCTs
- India market entry/registration pathway assessment, since the drug currently has no local license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

