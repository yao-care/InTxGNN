---
layout: default
title: Framycetin
parent: Moderate Evidence (L3-L4)
nav_order: 379
evidence_level: L4
indication_count: 7
---

# Framycetin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Framycetin: From Topical Antibacterial Use to Urinary Tract Infection

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic conventionally used as a topical antibacterial (skin, eye, ear); no original indication record exists for this compound in the India regulatory dataset, and the drug is currently unmarketed there. Among seven TxGNN-predicted indications, **Urinary Tract Infection (UTI)** is the only one that reached the research-question stage, supported by a plausible antibacterial mechanism and one historical clinical report — the higher-scoring top prediction (sclerosing cholangitis) and four others are explicitly flagged in the evidence pack's own rationale as lacking any biological plausibility and are treated as likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in India regulatory data; known clinically as a topical antibacterial agent (skin/eye/ear) |
| Predicted New Indication | Urinary Tract Infection (UTI) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question stage) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable for framycetin (flagged as a High-severity data gap, DG002). Based on known pharmacology, framycetin is an aminoglycoside antibiotic that inhibits bacterial protein synthesis via binding to the 30S ribosomal subunit, and it is active against common gram-negative uropathogens such as *E. coli*, *Proteus mirabilis*, and *Pseudomonas aeruginosa*. This provides a mechanistically coherent link to urinary tract infection, one of the most common indications for aminoglycoside-class antibacterial activity.

However, framycetin's established clinical use is almost exclusively topical (dermatological, ophthalmic, otic), and systemic administration is constrained by the class-wide risks of nephrotoxicity and ototoxicity. This means the mechanistic plausibility is reasonable, but practical route-of-administration feasibility (e.g., local bladder instillation vs. systemic dosing) remains unresolved and would need to be established before further development.

It is also worth noting that this evidence pack surfaced six other predicted indications with comparable or higher TxGNN scores (e.g., sclerosing cholangitis at 99.66%, congenital prothrombin deficiency at 99.41%). The pack's own mechanistic review explicitly identifies these as biologically implausible for an antibacterial drug — autoimmune/fibrotic biliary disease and a hereditary coagulation factor defect have no known relationship to aminoglycoside pharmacology — and treats them as likely model noise (all scored L5/Hold). UTI is therefore selected here as the only candidate with both a plausible mechanism and independent supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [816047](https://pubmed.ncbi.nlm.nih.gov/816047/) | 1976 | Case series/Older clinical report | Der Urologe. Ausg. A | In an experimental infected-bladder model, concurrent framycetin sulfate (or kanamycin) irrigation completely suppressed growth of *Proteus mirabilis* and *Pseudomonas aeruginosa*, and reduced *E. coli* growth, during continuous bladder irrigation therapy |

## India Market Information

This drug is not currently marketed in India — 0 registrations are on file, so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction data was found for framycetin (DDI query: not found). Note that TFDA/India label warnings and contraindications are an outstanding Blocking data gap (DG001); as a general aminoglycoside class caution, nephrotoxicity and ototoxicity risk with systemic use should be assumed pending confirmation.

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
Only one 1976 experimental/case-level report supports antibacterial activity relevant to UTI, with no completed clinical trials, no India market presence, and unresolved route-of-administration feasibility for systemic or bladder-targeted use. This does not yet meet the bar for further investment absent additional validation.

**To proceed, the following is needed:**
- TFDA/India label warnings and contraindications (Blocking gap, DG001) — required before any S1 safety screening
- Detailed mechanism of action data from DrugBank (High-priority gap, DG002)
- Contemporary evidence (post-1976) on aminoglycoside efficacy/safety for UTI, ideally via local (intravesical) rather than systemic delivery
- Route-of-administration and nephrotoxicity/ototoxicity risk assessment before considering clinical development
- Re-validation of the other six TxGNN-predicted indications' mechanistic plausibility before any further evidence collection is invested in them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

