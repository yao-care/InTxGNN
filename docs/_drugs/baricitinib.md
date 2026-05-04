---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baricitinib: From Autoimmune Conditions to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is a selective JAK1/JAK2 inhibitor used in the treatment of autoimmune inflammatory conditions; detailed original indication data is not captured in this dataset.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**,
however **no clinical trials and no publications** currently support this direction — the prediction is model-generated only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed in current regulatory dataset |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Baricitinib is a selective JAK1 and JAK2 inhibitor that blocks cytokine signalling through the JAK-STAT pathway. It suppresses downstream inflammatory mediators including IL-6, IL-12, IL-23, and interferons, making it effective in autoimmune and inflammatory conditions such as rheumatoid arthritis and atopic dermatitis.

Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome is an extremely rare congenital developmental disorder (classified under OMIM developmental gene defects), characterised by ocular developmental defects (iris/choroidal coloboma, microphthalmia) and skeletal abnormalities (proximal limb shortening). Its pathogenic pathways are dominated by transcription factor mutations such as PAX6, SOX2, and OTX2, as well as BMP signalling defects in skeletal morphogenesis — none of which have an established biological link to the JAK-STAT inflammatory axis that Baricitinib targets.

The high TxGNN score (0.9994) in this context is most likely attributable to a **topological artifact** within the knowledge graph — specifically, network proximity artefacts among rare developmental disease nodes — rather than a biologically meaningful mechanistic connection. There is no clinical, translational, or preclinical literature to support this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Baricitinib in Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome.

---

## Literature Evidence

Currently no related literature available for Baricitinib in Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome.

---

## India Market Information

No drug licenses or regulatory registrations for Baricitinib are recorded in the current India market dataset.

---

## Safety Considerations

**Drug Interactions (321 total interactions on record):**

The following key interactions are flagged from the DDInter database:

| Severity | Interacting Drug(s) | Clinical Implication |
|----------|---------------------|----------------------|
| **Major** | Hydrocortisone, Betamethasone, Budesonide, Dexamethasone, Prednisolone, Prednisone, Triamcinolone, Triamcinolone (ophthalmic) | Co-administration with systemic corticosteroids significantly increases immunosuppression risk; heightened susceptibility to serious and opportunistic infections |
| **Major** | Deferiprone | Additive myelosuppression risk; concurrent use may severely impair haematopoiesis |
| **Major** | Ibritumomab tiuxetan, Iobenguane (I-131), Tositumomab (I-131) | Additive immunosuppression and bone marrow suppression with radioimmunotherapy agents |
| **Moderate** | Morphine, Morphine (liposomal), Opium | Potential for additive CNS and respiratory depression; requires monitoring |
| **Moderate** | Acetylsalicylic acid | Possible increased bleeding risk and gastrointestinal effects |
| **Moderate** | Nitisinone | Metabolic interaction requiring monitoring |
| **Minor** | Zinc acetate, Zinc gluconate, Zinc sulfate | Low-level interaction; clinically unlikely to be significant |

> **Note:** Comprehensive warnings and contraindications from the official prescribing information are not available in this dataset. Please refer to the approved package insert and the SmPC/prescribing information for the full safety profile, including black-box warnings (e.g., serious infections, malignancy, thrombosis, and cardiovascular risk class effects common to JAK inhibitors).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.94%), but the predicted indication — Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome — is a rare congenital developmental disorder with no established mechanistic link to JAK-STAT signalling. The evidence level is L5 (model prediction only), and there are zero supporting clinical trials or publications. The repurposing rationale analysis explicitly identifies this as a likely knowledge graph topological artefact rather than a biologically plausible hypothesis.

**To proceed, the following would be needed:**

- Retrieval and analysis of the official Baricitinib prescribing information (SmPC / US label / package insert) to fill critical safety data gaps
- Detailed mechanism of action documentation from DrugBank API query (DG002)
- Identification of any plausible mechanistic hypothesis linking JAK1/JAK2 inhibition to ocular or skeletal developmental pathways (e.g., role of JAK-STAT in embryonic eye development literature review)
- Preclinical model data (animal or in vitro) demonstrating any effect on the disease's core pathology (BMP/FGF/transcription factor signalling)
- Consultation with a rare disease specialist or paediatric ophthalmologist to assess biological plausibility
- If biological rationale can be established: development of a hypothesis-generating preclinical study before considering any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

