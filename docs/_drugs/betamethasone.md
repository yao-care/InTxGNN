---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid corticosteroid widely used in clinical practice for a broad range of inflammatory, allergic, and autoimmune conditions; no India (CDSCO) regulatory registration records were found in this dataset.
The TxGNN model predicts it may be effective for **Alopecia Areata**, with **7 clinical trials** and **20 publications** currently supporting this direction.
Evidence includes a 2023 Cochrane systematic review and multiple completed randomised controlled trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India (CDSCO) registry record available; betamethasone is a glucocorticoid corticosteroid broadly used for inflammatory and autoimmune conditions |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (1 completed Phase 2 RCT + multiple completed Phase 4 RCTs + Cochrane review) |
| India Market Status | Not Marketed (no CDSCO registrations found) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betamethasone is a synthetic glucocorticoid with potent anti-inflammatory and immunosuppressive activity. Although detailed MOA data is unavailable in this Evidence Pack, it is well-established that betamethasone binds to intracellular glucocorticoid receptors, suppresses the transcription of pro-inflammatory cytokines (including IL-1, IL-6, TNF-α), and inhibits T-lymphocyte activation and proliferation.

Alopecia areata (AA) is a tissue-specific autoimmune disorder in which autoreactive CD8⁺ T cells breach the immune privilege of hair follicles and trigger non-scarring hair loss. This immune-mediated mechanism is precisely the pathological pathway that corticosteroids are designed to suppress. The mechanistic match between betamethasone's immunosuppressive action and the T-cell-driven pathology of AA is therefore direct and biologically coherent.

In clinical practice, corticosteroids — administered topically, intralesionally, or systemically as pulse/mini-pulse regimens — are already regarded as first- or second-line agents for AA. The TxGNN prediction is therefore consistent with existing clinical knowledge, and the strength of the supporting evidence (including a Cochrane review and multiple RCTs comparing betamethasone formulations head-to-head with other agents) strongly reinforces its plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Compared weekly azathioprine pulse vs. betamethasone oral mini-pulse (BOMP) in moderate-to-severe AA; directly evaluates betamethasone as primary intervention |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | Combined topical 5% minoxidil + potent topical corticosteroid vs. intralesional triamcinolone in AA; RCT assessing topical corticosteroid combination efficacy |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | Head-to-head comparison of topical betamethasone vs. topical latanoprost for localised AA; provides direct comparative evidence |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Topical cetirizine 1% vs. topical betamethasone valerate 0.1% in localised AA; efficacy and safety comparison |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Topical pentoxifylline 2% gel and topical metformin 10% gel vs. topical betamethasone valerate 0.1% cream in patchy AA; novel comparator study |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicentre prospective study of treatment outcomes in Central Centrifugal Cicatricial Alopecia (related scarring alopecia subtype); corticosteroid arm included |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Unknown | 30 | Safety and efficacy of clobetasol propionate 0.05% foam in Central Centrifugal Cicatricial Alopecia; related corticosteroid comparator |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Network meta-analysis of all AA treatments; establishes comparative evidence base for corticosteroids including betamethasone |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iranian Journal of Pharmaceutical Research | Double-blind, placebo-controlled RCT (n=36) comparing oral betamethasone pulse, methotrexate, and combination in severe AA; betamethasone arm showed significant hair regrowth |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | Randomised controlled trial (n=60) comparing oral cyclosporine vs. betamethasone mini-pulse in AA; provides head-to-head comparative efficacy data |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatologic Therapy | Blinded multi-group RCT evaluating latanoprost vs. minoxidil, betamethasone, and combinations in AA (6 groups, n=18 each); comprehensive comparative design |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | Journal of the American Academy of Dermatology | Randomised controlled trial of microneedle transdermal delivery of compound betamethasone in AA; demonstrates novel delivery approach reduces injection pain while maintaining efficacy |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | RCT | Cureus | Comparison of topical betamethasone dipropionate vs. topical minoxidil in AA patients; direct head-to-head RCT |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Observational Study | Cureus | Prospective study assessing efficacy, safety, and outcomes of oral betamethasone mini-pulses in moderate-to-severe AA |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Comprehensive review of corticosteroid pulse therapy in AA: efficacy, relapse rates, side effects, and prognostic factors |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Review of pulse dose corticosteroid therapy dosing and administration specifically in paediatric AA; summarises available dosing regimens |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | Journal of Dermatological Treatment | Within-patient randomised controlled trial comparing intralesional betamethasone vs. triamcinolone acetonide in localised AA; directly evaluates betamethasone intralesional efficacy |

---

## Safety Considerations

**Drug Interactions (451 total interactions identified):**

| Severity | Interacting Drug | Clinical Relevance |
|----------|----------------|--------------------|
| **Major** | Adalimumab | Concurrent use significantly increases infection risk due to compounded immunosuppression |
| Moderate | Ibuprofen, Ketorolac | Increased risk of gastrointestinal ulceration and bleeding with concomitant NSAIDs |
| Moderate | Acarbose, Albiglutide | Glucocorticoids antagonise hypoglycaemic effects; blood glucose monitoring required |
| Moderate | Acetazolamide | Risk of hypokalaemia may be increased |
| Moderate | Nifedipine | Possible pharmacokinetic interaction; blood pressure monitoring warranted |
| Moderate | Ethinylestradiol | Oestrogens may increase corticosteroid plasma levels |
| Moderate | Fluvoxamine | CYP3A4 inhibition may increase betamethasone exposure |
| Moderate | Fosamprenavir | CYP3A4-mediated interaction; monitor for increased corticosteroid effects |
| Moderate | Isotretinoin | Concurrent use increases risk of raised intracranial pressure |
| Moderate | Immunologicals (Adalimumab, Alefacept, Alemtuzumab, Aldesleukin, Tetanus toxoid) | Betamethasone may reduce immune response to vaccines and biologics |
| Minor | Formoterol, Salbutamol | Hypokalaemia risk may be mildly increased |

> **Note:** Detailed key warnings and contraindications from the package insert are not available in this Evidence Pack. Please refer to the full prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betamethasone is a mechanistically well-justified treatment for alopecia areata — an autoimmune disease driven by T-cell activity that is directly suppressed by glucocorticoids — and is already used in clinical practice for this indication globally, supported by a 2023 Cochrane systematic review, multiple completed RCTs, and ongoing comparative trials. However, no India (CDSCO) regulatory registration was found in this dataset, formal large-scale Phase 3 RCT data is absent, and safety details (key warnings, contraindications) are not available in this pack.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm actual CDSCO registration status in India, as betamethasone products are widely sold; the current dataset result (0 registrations) may reflect a data gap rather than true market absence
- **Package insert review:** Obtain and review the full India package insert for key warnings and contraindications (DG001 — currently blocking S1 safety assessment)
- **MOA documentation:** Retrieve mechanism of action data from DrugBank (DG002) to complete the mechanistic evidence dossier
- **Route-specific assessment:** Determine which administration route (topical, intralesional, oral mini-pulse) is most appropriate for the India clinical context and patient population
- **Paediatric vs. adult dosing plan:** Given existing evidence for both adult and paediatric AA, a dose-stratified safety monitoring plan should be developed
- **DDI screening:** For AA patients commonly co-prescribed immunosuppressants or biologics (e.g., adalimumab — a **major** interaction), prospective DDI screening protocols should be established before clinical deployment

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

