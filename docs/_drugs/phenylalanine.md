---
layout: default
title: Phenylalanine
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenylalanine: From Amino Acid Supplement to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine (DB00120) is an essential amino acid with no approved therapeutic indication on record and is currently **not marketed in Taiwan**. TxGNN assigns a high embedding score (99.43%) linking it to **Sclerosing Cholangitis**, but none of the 4 supporting publications actually studies phenylalanine's effect on this disease — the strongest matches concern a different substance (the bacterial peptide fMLP, whose name happens to contain "phenylalanine"). This candidate should be treated as an unverified model artifact, not a validated repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — Phenylalanine is an essential amino acid/nutritional component with no recorded disease indication (`original_moa`: Data Gap) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only) |
| Taiwan Market Status | ✗ Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Mechanism-of-action data for phenylalanine is not available (`[Data Gap]`), and unlike typical repurposing candidates, there is no established original indication to anchor a mechanistic bridge to sclerosing cholangitis.

More importantly, the supporting literature does not actually corroborate the link. Of the 4 publications returned, one (PMID 15790420) studies **tyrosine**, not phenylalanine, in relation to fatigue in PBC/PSC; one (PMID 32025163) is an unrelated cholangiocarcinoma metabolomics study; and two (PMID 8000512, PMID 2103382) study **N-formyl-methionyl-leucyl-phenylalanine (fMLP)**, a bacterial chemotactic peptide used as an immunology reagent — a distinct pharmacological entity that merely shares the substring "phenylalanine" in its name with DB00120.

Taken together, this strongly suggests the TxGNN score reflects a knowledge-graph embedding artifact (likely driven by textual/entity overlap) rather than a genuine pharmacological relationship. No mechanistic rationale currently supports this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examines plasma **tyrosine** (not phenylalanine) and fatigue in PBC/PSC — does not study phenylalanine treatment |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | J Clin Exp Hepatol | Serum metabolomic profiling in cholangiocarcinoma; unrelated to phenylalanine as an intervention |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal study | J Gastroenterol | Rectal **fMLP** (a bacterial peptide, distinct from the amino acid) induced small duct cholangitis in rats with colitis |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Basic research | J Gastroenterol Hepatol | Characterizes enterohepatic circulation of bacterial **F-met chemotactic peptides**, not free phenylalanine |

*Note: none of the above studies evaluates phenylalanine itself as a therapeutic agent for sclerosing cholangitis; matches appear driven by name/text overlap with the unrelated peptide fMLP.*

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are marked as a **Blocking** data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only), with no clinical trials and no literature that genuinely supports phenylalanine's activity in sclerosing cholangitis. The available publications appear to reflect a name-collision artifact with the unrelated peptide fMLP rather than a real pharmacological signal, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA label warnings/contraindications) before any safety pre-assessment
- Obtain verified mechanism-of-action data (DG002) for phenylalanine
- Independent literature/database re-query specifically excluding fMLP and other name-collision entities, to confirm whether any genuine phenylalanine–cholangitis evidence exists
- Note: the secondary candidate (congenital prothrombin deficiency, score 99.26%) was also assessed and is equally unsupported — its only associated trial (NCT06227429, studying Nitisinone, not phenylalanine) was withdrawn with zero enrollment; it carries the same Hold recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

