---
layout: default
title: Tenoxicam
parent: Moderate Evidence (L3-L4)
nav_order: 819
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenoxicam: predicted new indication Rheumatoid arthritis (evidence level L3). Approved use: Arthritic joint disease"
monitor_inn: "Tenoxicam"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
---

# Tenoxicam
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tenoxicam: From Arthritic Joint Disease to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Tenoxicam is an oxicam-class nonsteroidal anti-inflammatory drug (NSAID), originally used for arthritic joint disease and arthropathy.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, supported by **20 publications** (no registered clinical trials for this indication). Because rheumatoid arthritis is closely related to the original indications, this is effectively an on-label or near-label use rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arthritic joint disease; arthropathy (from the knowledge graph, as no approved indication text is available for the Indian licence) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tenoxicam belongs to the oxicam class of NSAIDs. These drugs inhibit COX-1 and COX-2 enzymes, which reduces prostaglandin-mediated inflammation and pain. This mechanism is inferred from the drug class rather than taken from a recorded mechanism entry.

This mechanism is directly relevant to the symptomatic management of rheumatoid arthritis. Rheumatoid arthritis is a form of inflammatory joint disease, so it sits very close to the original indications (arthritic joint disease and arthropathy). The prediction therefore largely confirms existing use rather than opening a new therapeutic area.

Note that the benefit is symptomatic (pain and inflammation relief). Nothing in the data compiled for this report suggests tenoxicam modifies the course of the disease. The supporting clinical studies are also mostly from the 1980s to 1990s.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | Double-blind trial in 292 rheumatoid arthritis patients comparing aceclofenac and tenoxicam over 3 months; both groups improved clinically |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | Comparative study | J Rheumatol | Tenoxicam 20 mg vs piroxicam 20 mg in 102 rheumatoid arthritis patients; no difference in efficacy, similar adverse event rates |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Effective analgesic and anti-inflammatory agent for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and other rheumatic conditions; efficacy at least equivalent to other NSAIDs |
| [3315620](https://pubmed.ncbi.nlm.nih.gov/3315620/) | 1987 | Review | Drugs | Once-daily 20 mg appears as effective as piroxicam 20 mg in rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and gout |
| [3329109](https://pubmed.ncbi.nlm.nih.gov/3329109/) | 1987 | Review | Eur J Rheumatol Inflamm | Overview of 133 clinical studies; efficacy shown in double-blind comparisons, with 20 mg as the optimal dose |
| [3317799](https://pubmed.ncbi.nlm.nih.gov/3317799/) | 1987 | Review | Scand J Rheumatol Suppl | Nine clinical studies; efficacious in rheumatoid arthritis and osteoarthrosis, with less gastrointestinal blood loss than aspirin |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | Cohort | J Int Med Res | General practice study of 2,963 patients with osteoarthritis or rheumatoid arthritis treated with 20 mg/day for 12 weeks or longer |
| [2692947](https://pubmed.ncbi.nlm.nih.gov/2692947/) | 1989 | Cohort | Clin Rheumatol | 12-week open study in 58 patients with impaired renal function; renal function was monitored during treatment |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Double-blind trials | Eur J Rheumatol Inflamm | Tenoxicam at least as effective as piroxicam in osteoarthrosis, rheumatoid arthritis and ankylosing spondylitis |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics: completely absorbed orally, about 99% protein bound |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217961 | Tobitil 20mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not specified |

## Safety Considerations

- **Adverse effect signal:** A case report (PMID 9303679, 1997) describes alopecia secondary to tenoxicam.
- **Renal function:** A 12-week open study in patients with impaired renal function (PMID 2692947) included renal monitoring, so kidney function deserves attention in this population.
- **Gastrointestinal tolerability:** In one comparative study, six patients discontinued treatment because of gastrointestinal intolerance (PMID 1593574).

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rheumatoid arthritis is closely related to the original indications, and multiple clinical studies (including a double-blind RCT of 292 patients and comparisons with piroxicam) support symptomatic efficacy. The evidence is mostly old, has no registered trials, and does not show disease-modifying benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian licence holder, and the approved indication text
- Mechanism of action data from DrugBank
- A safety monitoring plan, particularly for gastrointestinal and renal risk
- Confirmation of the approved indication scope under the Indian licence

### Other Predicted Indications (Brief Note)

- **Headache disorder (migraine):** An active Phase 4 trial ([NCT06786650](https://clinicaltrials.gov/study/NCT06786650), n=100) compares intravenous tenoxicam with ibuprofen in acute migraine. There are no results yet and no placebo arm. This is worth treating as a research question.
- **Alopecia and hair-related predictions:** The only literature describes alopecia as an adverse effect of tenoxicam, so these high scores likely reflect a spurious association rather than benefit. **Hold.**
- **Other predictions** (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, osteoarthritis susceptibility, trigeminal autonomic cephalalgia): model prediction only, with no clinical or literature support and no plausible mechanistic link. **Hold.**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

