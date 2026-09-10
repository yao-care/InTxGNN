---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 664
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus is a topical calcineurin inhibitor originally developed and marketed internationally (as Elidel) for atopic dermatitis, but it currently holds **no marketing registration** in this jurisdiction. The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**, with **1 clinical trial** and **18 publications** currently supporting this direction, largely reflecting well-established off-label use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis *(internationally approved use; see note below — no local registration record exists)* |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on Original Indication**: This candidate's source regulatory dataset shows zero local licenses and no `original_moa` on file — the drug has never been registered in this market. Its internationally recognized indication (atopic dermatitis, marketed as Elidel) is cited here for mechanistic context only, not as a locally verified label claim.

---

## Why is This Prediction Reasonable?

Detailed local mechanism-of-action documentation is not available (data gap), but pharmacological literature consistently describes pimecrolimus as a topical, cell-selective calcineurin inhibitor. It suppresses T-cell activation and blocks release of inflammatory cytokines (IL-2, IL-4, interferon-γ, TNF-α), and also inhibits mast cell degranulation — this is the mechanism underlying its established use in atopic dermatitis.

Seborrheic dermatitis and atopic dermatitis are both chronic, relapsing inflammatory skin conditions with overlapping T-cell-mediated cytokine pathways; seborrheic dermatitis additionally involves *Malassezia* yeast-triggered keratinocyte and T-cell inflammation. Because calcineurin inhibition dampens the shared inflammatory cascade rather than targeting a disease-specific driver, the mechanistic extension from atopic dermatitis to seborrheic dermatitis is biologically plausible.

Critically, this is not a purely theoretical hypothesis: topical pimecrolimus has been used off-label for seborrheic dermatitis in clinical practice since the mid-2000s, and this usage is corroborated by two independent systematic reviews of RCTs showing efficacy comparable to corticosteroids and antifungal agents, with a favorable side-effect profile for long-term/facial use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | Randomized, double-blind, parallel-group, active-comparator-controlled exploratory study of Elidel (pimecrolimus) for seborrheic dermatitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream is a well-tolerated, effective treatment for seborrheic dermatitis with efficacy comparable to corticosteroids/antimycotics. |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT (vs sertaconazole) | Clin Exp Dermatol | Randomized blinded trial comparing pimecrolimus 1% cream vs. sertaconazole 2% cream for facial seborrhoeic dermatitis. |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT (vs sertaconazole) | Ir J Med Sci | Compared efficacy of sertaconazole 2% cream vs. pimecrolimus 1% cream in treatment of seborrheic dermatitis. |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review | Cureus | Critical review of efficacy and safety of pimecrolimus in facial seborrheic dermatitis across RCTs, positioned among calcineurin-inhibitor treatment options. |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Clinical Study/Review | J Clin Aesthet Dermatol | Topical pimecrolimus offers a safe long-term alternative to corticosteroids for seborrheic dermatitis, avoiding steroid-related adverse effects. |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label Study | Am J Clin Dermatol | Pimecrolimus 1% cream effective and well tolerated in resistant facial seborrheic dermatitis. |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Clinical Study | J Cosmet Dermatol | Compared different treatment-duration regimens of pimecrolimus 1% cream for facial seborrheic dermatitis. |
| [19391059](https://pubmed.ncbi.nlm.nih.gov/19391059/) | 2010 | Clinical Study | J Dermatolog Treat | Evaluated safe, effective repetitive/long-term use of pimecrolimus in relapsing seborrheic dermatitis. |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | Clinical Study | J Dermatolog Treat | Close follow-up study reporting mean cure/remission times and side-effect profile of pimecrolimus in seborrheic dermatitis. |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Clinical Study | Drugs Exp Clin Res | Early study assessing efficacy, tolerability and safety of pimecrolimus cream 1% for seborrheic dermatitis of face and trunk. |

---

## Safety Considerations

- **Drug Interactions**: A DDInter query identified **103 total documented interacting drugs**; however, severity levels are marked "Unknown" (unclassified) in the source data for all entries reviewed. Frequently listed interacting agents include: Phentermine, Pantoprazole, Doxycycline, Metformin, Omeprazole, Lansoprazole, Triamcinolone, Prednisone, Simvastatin, Nystatin, Hydrocortisone, Tetracycline, Ranitidine, Ondansetron, Metronidazole, Famotidine, Acetylsalicylic acid, Rabeprazole, Bupropion, and Budesonide. Given the "Unknown" severity classification, clinical significance cannot be determined from this data alone — please cross-check against the product label.

Key warnings and contraindications are not available in the current dataset; please refer to the package insert for this information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The seborrheic dermatitis signal is supported by a completed Phase 2 RCT and a coherent body of literature (2 tier-1 systematic reviews, 2 tier-1 head-to-head RCTs, plus multiple supporting clinical studies spanning 2004–2022), and reflects mechanistically plausible, long-standing off-label practice rather than a purely novel hypothesis. However, this candidate carries a **Blocking-severity data gap (DG001: local product-label warnings/contraindications)**, which per the evaluation framework prevents full entry into the S1 safety review — the "Proceed with Guardrails" status should be treated as conditional until this gap is closed.

**To proceed, the following is needed:**
- Obtain and parse the official product label (warnings, contraindications) — currently blocking (DG001)
- Obtain confirmed mechanism-of-action documentation from DrugBank (DG002)
- Reclassify the 103 DDI entries currently marked "Unknown" severity for clinical significance
- Given zero existing local registrations, confirm the regulatory pathway (new drug application vs. supplemental indication) required to bring pimecrolimus to market locally before pursuing the seborrheic dermatitis indication
- Note: the "dermatitis" (atopic dermatitis) prediction in this pack largely reflects validation of pimecrolimus's *existing* global indication rather than a new repurposing signal, and should not be conflated with the seborrheic dermatitis opportunity above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

