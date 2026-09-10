---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 795
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tacrolimus: From Organ Transplant Rejection Prophylaxis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor originally developed as a systemic immunosuppressant to prevent organ transplant rejection, with a topical ointment formulation (Protopic) also long used for atopic dermatitis. The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**, with **2 clinical trials** and **21 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap). Literature within the pack confirms tacrolimus is used systemically as an immunosuppressant for organ transplant rejection prophylaxis, and topically (Protopic) for atopic dermatitis |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is currently a flagged data gap (DG002). Based on the pharmacology referenced across the collected literature, tacrolimus is a calcineurin inhibitor that blocks T-cell activation and downregulates inflammatory cytokine release. This mechanism underlies its established use as a topical immunomodulator (Protopic) for T-cell-mediated skin inflammation, most notably atopic dermatitis.

Seborrheic dermatitis is likewise a chronic, relapsing inflammatory dermatological condition, with the face and scalp as primary sites, driven by cytokine-mediated inflammation and modulated by Malassezia yeast colonization. Because calcineurin inhibition suppresses this inflammatory cascade without the skin-atrophy risk associated with long-term corticosteroid use, tacrolimus ointment is mechanistically well suited to facial areas requiring long-term maintenance therapy — which is exactly the population studied in the supporting trials below.

One data-quality note: the evidence pack lists "dermatitis" (atopic dermatitis) as a separate, lower-ranked predicted indication, but this is in fact an already-established, marketed indication for topical tacrolimus rather than a novel repurposing candidate. This, combined with the empty `original_indications` field and "Not marketed" status recorded here, suggests the source regulatory record for this drug is incomplete and should be manually reconciled before this candidate proceeds further.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic) as maintenance treatment for severe facial seborrheic dermatitis, aiming to prolong remission and reduce reliance on topical steroids |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed whether proactive, once/twice-weekly application of 0.1% tacrolimus ointment maintains remission and reduces exacerbation in adult facial seborrheic dermatitis |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT comparing tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | RCT | Ann Dermatol | Evaluated 0.1% tacrolimus ointment as maintenance therapy for facial seborrheic dermatitis, extending the intermittent-use strategy proven in atopic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT/Cohort | Ann Parasitol | Comparative trial of sertaconazole 2% cream vs. tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Compared oral itraconazole plus topical tacrolimus vs. topical tacrolimus alone for maintenance treatment of seborrheic dermatitis in Vietnam |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors as a corticosteroid-sparing option for seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Cochrane Systematic Review/NMA | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments across eczema/inflammatory dermatoses, including calcineurin inhibitors |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open pilot study | J Am Acad Dermatol | Early open-label pilot in 18 patients; 61% achieved complete clearance of seborrheic dermatitis with 0.1% tacrolimus over 28 days |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis pathophysiology and emerging therapeutic options, including topical calcineurin inhibitors |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Reviews tacrolimus ointment's efficacy and safety across atopic dermatitis and other inflammatory cutaneous diseases |

## India Market Information

Tacrolimus currently has no marketing authorization on record in India (total registrations: 0; market status: not marketed). No product-level licensing data is available to summarize dosage forms or approved indications.

## Safety Considerations

- **Drug Interactions**: The evidence pack records 868 total known interactions. Notable **Major**-level interactions include Amphotericin B, Amphotericin B (lipid complex), Loperamide, Mesalazine, Omeprazole, and Balsalazide. **Moderate**-level interactions include Acarbose, Famotidine, Rabeprazole, Hydrocortisone, Metformin, Pioglitazone, Dexamethasone, Betamethasone, Metronidazole, and Budesonide (among others).

Detailed key warnings and contraindications are not available in this evidence pack (flagged as a Blocking data gap, DG001) — please refer to the package insert for this information once obtained.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed trials (one Phase 3, one Phase 4) plus a substantial literature base — including a multicenter double-blind RCT — directly support tacrolimus ointment for facial seborrheic dermatitis maintenance therapy, justifying an L1 evidence rating. However, the drug is not currently marketed in India and key regulatory safety data is missing, so progression must be gated on closing those gaps.

**To proceed, the following is needed:**
- TFDA/CDSCO-equivalent label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action documentation (DG002)
- Reconciliation of the drug's actual original/marketed indications (current record shows empty `original_indications` despite topical tacrolimus being a known marketed product elsewhere)
- India-specific regulatory filing and registration pathway assessment, since the product is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

