---
layout: default
title: Tenoxicam
parent: High Evidence (L1-L2)
nav_order: 812
evidence_level: L1
indication_count: 10
---

# Tenoxicam
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

Using no additional skill — this is a straightforward document-generation task following the given report template with the supplied Evidence Pack (no code changes, no debugging, no build/brainstorm activity applicable).

---

# Tenoxicam: From NSAID Musculoskeletal Pain Management to Rheumatoid Arthritis

## One-Sentence Summary

> Tenoxicam is an oxicam-class NSAID whose classic indications include osteoarthritis, ankylosing spondylitis, and other rheumatic pain conditions — Taiwan registry data on its specific original indication text is unavailable because the drug currently holds **zero active licenses** in this jurisdiction.
> The TxGNN model's top prediction, **Rheumatoid Arthritis**, is supported by **1 registered clinical trial** and **20 publications**, but this is largely a re-confirmation of an already well-established NSAID use rather than a genuinely novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from Taiwan registry (0 licenses on file). Internationally, tenoxicam (oxicam-class NSAID) is indicated for osteoarthritis, ankylosing spondylitis, and acute musculoskeletal/rheumatic pain |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this candidate (flagged as data gap DG002). Based on well-established pharmacology, however, tenoxicam is an oxicam-class NSAID that non-selectively inhibits COX-1 and COX-2, reducing prostaglandin synthesis and thereby producing anti-inflammatory, analgesic, and antipyretic effects.

This mechanism maps directly onto the joint-inflammation pathology of rheumatoid arthritis, which is why oxicams (including piroxicam, tenoxicam's closest analog) have long been used as symptomatic RA therapy. In this specific case, the repurposing rationale in the evidence pack explicitly notes that RA is a **classic, pre-existing indication for the oxicam class**, not a novel association discovered by the TxGNN graph model. The prediction should therefore be read as validation of known pharmacology rather than a new hypothesis — useful for confirming model calibration, but with limited "new science" value for a repurposing pipeline.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | N/A | Completed | 80 | Compared tenoxicam, paracetamol, and tenoxicam-paracetamol combination for postoperative pain in double-jaw surgery patients. Note: this trial studies postoperative surgical pain, not an RA patient population — its relevance to the RA indication is indirect (shared NSAID analgesic mechanism only) |

No RA-specific registered clinical trial (e.g., a dedicated RA efficacy RCT on ClinicalTrials.gov) was found in the evidence pack; the historical RA evidence base below comes from older published literature rather than current trial registries.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | Multicentre double-blind RCT, n=292: aceclofenac vs. tenoxicam in RA, both showed comparable efficacy improvement |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | J Rheumatol | n=102: tenoxicam 20mg OD vs. piroxicam 20mg OD in RA, no efficacy difference, similar adverse event rates |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | RCT | Eur J Rheumatol Inflamm | Double-blind parallel trials in OA, RA, and ankylosing spondylitis; tenoxicam at least as effective as piroxicam |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | RCT (multicentre) | J Int Med Res | n=2,963 general-practice patients with OA/RA; 20mg/day tenoxicam for 12 weeks, long-term tolerability data to 52 weeks |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | RCT (double-blind parallel) | Br J Clin Pract | n=1,328 OA/RA patients comparing tenoxicam and piroxicam; tenoxicam showed slightly greater effect on global assessment |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | Open, non-comparative study | Eur J Rheumatol Inflamm | n=79 (39 RA, 40 arthrosis); rectal tenoxicam suppository 20mg/day showed clinical improvement over 6 weeks |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Comprehensive review: tenoxicam efficacy in RA, OA, ankylosing spondylitis at least equivalent to other NSAIDs, tolerability better than diclofenac/indomethacin |
| [2512637](https://pubmed.ncbi.nlm.nih.gov/2512637/) | 1989 | Long-term trial | Scand J Rheumatol Suppl | 4-year trial in 20 RA patients; sustained analgesic/anti-inflammatory benefit with tenoxicam + basis therapy |
| [3329109](https://pubmed.ncbi.nlm.nih.gov/3329109/) | 1987 | Overview | Eur J Rheumatol Inflamm | Summary of 133 clinical studies of tenoxicam across RA, OA, ankylosing spondylitis, and gout; optimal dose established at 20mg |
| [7983661](https://pubmed.ncbi.nlm.nih.gov/7983661/) | 1994 | Compliance study | J Rheumatol | 6-month compliance comparison in RA: tenoxicam vs. naproxen |

## Taiwan Market Information

No license records are available — `taiwan_regulatory.licenses` is empty and `total_licenses = 0`. Tenoxicam does not currently hold any active drug registration in this jurisdiction, so no approved-indication text can be cited locally.

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and drug-interaction data are all flagged as data gaps in this evidence pack; DDI query returned no results.)

**Note:** Data gap DG001 (TFDA label warnings/contraindications) is classified as **Blocking severity** — it prevents this candidate from entering the S1 safety pre-screen stage and must be resolved before any further clinical decision-making.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical double-blind RCTs (1985–1996) consistently demonstrate tenoxicam's efficacy in RA, comparable to piroxicam and aceclofenac, giving the indication a robust literature base (L1). However, this "prediction" largely reconfirms an already-known NSAID use rather than identifying a novel repurposing opportunity, and the drug is currently unregistered in Taiwan with no accessible label safety data — both of which limit near-term actionability.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before S1 safety pre-screen
- Confirmed MOA data from DrugBank (DG002, High) — currently assumed from oxicam-class pharmacology only
- Clarification of whether RA should be treated as a "known-use confirmation" rather than a true repurposing candidate, to properly prioritize pipeline resources
- Market-entry/registration assessment, since Taiwan currently has zero active licenses for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

