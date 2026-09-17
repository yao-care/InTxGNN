---
layout: default
title: Phenindione
parent: Moderate Evidence (L3-L4)
nav_order: 654
evidence_level: L3
indication_count: 1
---

# Phenindione
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

# Phenindione: From Anticoagulant Therapy (Discontinued) to Thrombotic Disease

## One-Sentence Summary

Phenindione is an indanedione-class vitamin K antagonist historically used as an oral anticoagulant, but it has been discontinued in most markets due to a higher incidence of severe adverse effects than warfarin. The TxGNN model predicts renewed relevance for **Thrombotic Disease**, but this is essentially the drug's own historical indication rather than a novel signal, and the current evidence base is **1 loosely related clinical trial** and **20 publications**, most of which concern the vitamin K antagonist (VKA) class in general rather than phenindione specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulant / thromboembolism prophylaxis (VKA) — historical use, discontinued in most markets due to safety concerns; no India/Taiwan license record found |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `original_moa` field is not populated in this evidence pack, but the pharmacology data captured under drug-target interactions clarifies the mechanism: phenindione targets **VKORC1 (vitamin K epoxide reductase complex subunit 1)**, the same target as warfarin, acenocoumarol, and fluindione. Inhibiting VKORC1 blocks the recycling of vitamin K, which in turn suppresses hepatic synthesis of clotting factors II, VII, IX, and X — the classic vitamin K antagonist anticoagulant mechanism.

Because thrombotic disease is precisely the therapeutic area VKAs were designed for, the mechanistic link to the "predicted" indication is strong — arguably too strong to be a genuine repurposing discovery. Phenindione already has a documented anticoagulant clinical history; the pharmacology record notes it is an "anticoagulant — discontinued due to higher incidence of severe adverse effects than warfarin," with no current FDA or EMA marketing approval and uncertain status elsewhere. In other words, this candidate is a rediscovery of a known-but-withdrawn indication rather than a novel mechanistic hypothesis, which changes the framing from "efficacy validation" to "risk-benefit re-evaluation."

The literature reinforces this: the available publications are overwhelmingly about the VKA class as a whole (warfarin, fluindione, acenocoumarol) rather than phenindione-specific trials, and several directly describe serious phenindione-related hypersensitivity reactions from historical case series.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05646394](https://clinicaltrials.gov/study/NCT05646394) | N/A (Registry) | Recruiting | 150 | Registry study on antithrombotic regimens (VKA ± aspirin vs. dual antiplatelet) in antiphospholipid syndrome patients with a recent arterial event. Not a phenindione-specific interventional trial — relevance graded "C" (observational, same drug class only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13162792](https://pubmed.ncbi.nlm.nih.gov/13162792/) | 1954 | Case Report | JAMA | Severe drug sensitivity reaction directly attributed to phenindione (phenylindandione) — earliest direct safety signal for this drug. |
| [13307153](https://pubmed.ncbi.nlm.nih.gov/13307153/) | 1956 | Clinical Report | J Med Assoc Georgia | Early clinical description of phenylindanedione as an anticoagulant. |
| [8037888](https://pubmed.ncbi.nlm.nih.gov/8037888/) | 1994 | Review | Drug Safety | Review of clinically significant drug interactions with oral anticoagulants, including indanedione derivatives. |
| [41177211](https://pubmed.ncbi.nlm.nih.gov/41177211/) | 2025 | Review (systematic) | Contraception | Updated systematic review on safety of contraception in women using anticoagulant therapy (bleeding/thrombosis risk). |
| [24889788](https://pubmed.ncbi.nlm.nih.gov/24889788/) | 2014 | Cohort | J Mal Vasc | Case-control analysis of risk factors for thrombotic or bleeding events in VKA-treated patients. |
| [12503504](https://pubmed.ncbi.nlm.nih.gov/12503504/) | 2002 | Cohort | Arch Pediatr | Acenocoumarol and fluindione use in 150 children after cardiac surgery. |
| [17176918](https://pubmed.ncbi.nlm.nih.gov/17176918/) | 2006 | Case Report | Clin Nephrol | Acute immuno-allergic interstitial nephritis caused by fluindione (VKA-class hypersensitivity reaction, analogous to phenindione's known AE profile). |
| [21978501](https://pubmed.ncbi.nlm.nih.gov/21978501/) | 2011 | Case Report | Ann Dermatol Venereol | Five cases of necrotic leg ulcers induced by vitamin K antagonists. |
| [14714343](https://pubmed.ncbi.nlm.nih.gov/14714343/) | 2003 | Cohort | Ann Cardiol Angeiol | Evaluation of a patient education program for oral anticoagulation therapy. |
| [21531328](https://pubmed.ncbi.nlm.nih.gov/21531328/) | 2011 | Review | Adv Chronic Kidney Dis | Review of nephrotoxins, including thrombotic microangiopathy as a drug-induced vascular injury pattern. |

---

## India Market Information

Phenindione has **0 registrations** and is currently **not marketed** in the available regulatory dataset — no license records were returned.

---

## Safety Considerations

- **Known Safety Signal (pharmacology database):** Phenindione has been discontinued in multiple markets due to a higher incidence of severe adverse effects than warfarin; no current FDA or EMA marketing approval is on record, though individual national agencies may still authorize it.
- **Historical Case Evidence:** A severe drug sensitivity reaction to phenindione was documented as early as 1954 (PMID 13162792).
- **Class-Related Adverse Events (from VKA analogs):** Hypersensitivity-mediated interstitial nephritis (fluindione, PMID 17176918) and necrotic skin ulcers (VKA class, PMID 21978501) have been reported for structurally related vitamin K antagonists.
- **Official warnings and contraindications are not available in this evidence pack** (TFDA label data collection is flagged as a blocking gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is not a novel mechanistic prediction but a resurfacing of phenindione's own original — and clinically discontinued — anticoagulant indication. Evidence is L3 (observational/class-level literature, no phenindione-specific RCTs), and the drug's documented history of severe hypersensitivity reactions relative to warfarin outweighs the mechanistic plausibility of the "prediction" until safety data is reviewed.

**To proceed, the following is needed:**
- TFDA/CDSCO label data (warnings, contraindications) — currently a blocking data gap preventing S1 safety screening
- Confirmed original mechanism-of-action documentation (beyond the inferred VKORC1 target from pharmacology data)
- Phenindione-specific (not VKA-class) clinical evidence for thrombotic disease, ideally contemporary Phase 2/3 data
- A formal comparative safety assessment against warfarin/DOACs before any "Go" consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

