---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with over five decades of clinical use in hematologic malignancies, most notably chronic lymphocytic leukemia (CLL).
The TxGNN model predicts it may be effective for **CLL/SLL with IGHV somatic hypermutation** — a molecularly defined, favorable-risk subtype of CLL — with a prediction score of **99.72%**, though no clinical trials or publications are currently indexed specifically for this molecular subtype.
The prediction reflects a biological refinement of an already-established indication rather than a novel repurposing target, and broader CLL trial data provides the mechanistic underpinning.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia and hematologic malignancies (not registered in India; globally established use) |
| Predicted New Indication | CLL/SLL with IGHV heavy chain variable-region gene somatic hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 (extrapolated from broader CLL evidence base; no subtype-specific studies) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, Chlorambucil is a bifunctional alkylating agent belonging to the nitrogen mustard class. It forms interstrand and intrastrand DNA crosslinks, disrupting replication and transcription in proliferating lymphocytes, ultimately triggering programmed cell death (apoptosis). Its slow oral bioavailability and relatively mild acute toxicity profile made it the dominant first-line CLL therapy for several decades.

The predicted indication — **CLL/SLL with IGHV somatic hypermutation** — is not a distinct new disease but a molecularly defined subgroup of CLL. Patients carrying mutated IGHV genes represent the **favorable-risk molecular stratum** of CLL: their B cells have undergone germinal center maturation, resulting in a less aggressive disease course with better response to conventional chemotherapy, including alkylating agents. In contrast to unmutated IGHV (pregerminal center CLL, which carries a worse prognosis), mutated IGHV patients historically achieved longer progression-free survival on Chlorambucil-based regimens.

This biological alignment is supported by landmark clinical evidence: the CLL11 trial (Goede et al., *NEJM* 2014) enrolled a mixed IGHV population and established obinutuzumab + chlorambucil as the first-line standard for elderly/unfit CLL patients. The mutated IGHV subgroup within such trials consistently showed superior responses to Chlorambucil-based combinations — making the TxGNN prediction a clinically coherent molecular refinement rather than speculative repositioning.

---

## Clinical Trial Evidence

Currently no clinical trials are registered specifically for Chlorambucil in CLL/SLL with IGHV somatic hypermutation.

> **Context:** Broad CLL trials such as CLL11 (obinutuzumab + chlorambucil) and RESONATE-2 (ibrutinib vs. chlorambucil) enrolled patients across IGHV mutation strata, but molecular subgroup stratification is typically available only in secondary analyses — not as the primary registration criterion. Dedicated subtype-specific prospective trials would be required for a formal indication filing.

---

## Literature Evidence

Currently no publications are directly indexed for Chlorambucil in CLL/SLL with IGHV somatic hypermutation.

> **Context:** IGHV mutation status became a standard CLL stratification tool after the mid-2000s. Most legacy Chlorambucil studies predate routine IGHV testing. Retrospective subgroup analyses from CLL11, CLL8, and related trials would be the most productive literature search targets for supplementing this gap.

---

## India Market Information

Chlorambucil is **not currently marketed in India**. No regulatory authorizations are on record in this Evidence Pack.

---

## Cytotoxicity

Chlorambucil meets the criteria for this section: it is a conventional cytotoxic drug whose primary indication involves hematologic malignancy, and it belongs to the nitrogen mustard alkylating agent class — a prototypical cytotoxic chemotherapy category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard / Bifunctional alkylating agent |
| Myelosuppression Risk | **High** — Dose-dependent; neutropenia and thrombocytopenia are primary and cumulative toxicities; marrow suppression may be delayed (onset up to 3–4 weeks after dosing) |
| Emetogenicity Classification | Low to moderate — Oral administration with lower emetogenic potential compared to IV alkylating agents; nausea is dose-dependent |
| Monitoring Items | CBC with differential (weekly during active treatment, then every 2–4 weeks); liver function tests; renal function; uric acid (tumor lysis risk); long-term monitoring for secondary malignancy (AML, MDS) |
| Handling Protection | Must follow cytotoxic drug handling regulations — NIOSH hazardous drug Group 1 classification; requires closed system transfer devices, PPE, and appropriate waste disposal |

---

## Safety Considerations

**Drug Interactions (167 total interactions identified; key interactions listed below):**

| Interacting Drug | Level | Notes |
|-----------------|-------|-------|
| Deferiprone | **Major** | Risk of severe agranulocytosis with concurrent myelosuppressive agents; combination should be avoided |
| Samarium (153Sm) lexidronam | **Major** | Additive myelosuppression; bone marrow reserve must be assessed before combined use |
| Amphotericin B (all formulations) | Moderate | Concurrent antifungal may enhance hematologic toxicity; monitor CBC closely |
| Mercaptopurine | Moderate | Potential additive immunosuppression and myelosuppression |
| Chloramphenicol / Chloramphenicol ophthalmic | Moderate | Additive bone marrow suppression risk |
| Palifermin | Moderate | Not recommended within 24 hours of cytotoxic chemotherapy administration |
| Strontium chloride Sr-89 | Moderate | Additive myelosuppression with radiopharmaceuticals |
| Roflumilast | Moderate | Immunosuppressive interaction; potential increased infection risk |
| Levofloxacin | Minor | Possible minor interaction; monitor for CNS or QT-related effects |
| Warfarin, Prednisone, Prednisolone, Omeprazole, Simvastatin, Levothyroxine | Unknown | Effect direction unclear; monitor therapeutic levels and clinical response during co-administration |

Specific key warnings and contraindications from the CDSCO package insert are not available in this Evidence Pack. Please refer to the approved product monograph for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorambucil has well-established efficacy in CLL broadly, and the **IGHV-mutated subtype** represents precisely the CLL population historically most responsive to Chlorambucil-based regimens. The TxGNN prediction score of 99.72% reflects a mechanistically grounded molecular refinement of an established oncology indication — not a speculative leap. However, the drug carries no regulatory authorization in India, the evidence base for this specific molecular subtype is indirect (extrapolated from broader CLL trials), and modern BTK inhibitors have substantially shifted the treatment landscape.

**To proceed, the following is needed:**

- **Regulatory pathway**: Assess requirements for market authorization in India; Chlorambucil is not currently registered and would require an NDA/import license
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB00291) and CDSCO/originator package insert
- **Subgroup data extraction**: Obtain IGHV-stratified subgroup analyses from published CLL11, RESONATE-2, and CLL8 trial data to quantify Chlorambucil's benefit specifically in mutated-IGHV patients
- **Competitive landscape assessment**: Evaluate positioning relative to BTK inhibitors (ibrutinib, acalabrutinib) and BCL-2 inhibitors (venetoclax), which have largely displaced Chlorambucil monotherapy in fit patients with mutated IGHV in high-income markets
- **Safety monitoring plan**: Formalize CBC monitoring schedule, cumulative dose tracking (secondary malignancy risk), and DDI screening protocol — particularly for the Major-level interactions with deferiprone and samarium-153
- **Patient population definition**: Clarify target population (elderly/unfit patients vs. fit patients; treatment-naïve vs. relapsed) to identify where Chlorambucil retains a clinically defensible niche
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

