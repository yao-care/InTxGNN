---
layout: default
title: Ambroxol
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 5
---

# Ambroxol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ambroxol: From Expectorant to Nasal Cavity Disease

## One-Sentence Summary

Ambroxol is a mucolytic and expectorant agent used in several jurisdictions for respiratory conditions involving excessive mucus production (not yet FDA/EMA-approved, but approved by individual European agencies and widely used in Asia and Europe).
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.
Evidence remains at the preclinical/mechanistic level, making this a hypothesis-generating rather than decision-ready finding at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant — respiratory conditions with excessive or impaired mucus secretion |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed (0 registered products) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available from the DrugBank source for this report. Based on pharmacological information retrieved from the drug interaction database, Ambroxol is a small-molecule mucolytic with at least two distinct mechanistic properties relevant to nasal cavity physiology. First, it promotes serous mucus secretion and activates mucociliary clearance — the very mechanism by which the nasal mucosa traps and expels pathogens and debris. Second, it blocks sodium channels (Nav1.2/Nav1.4), a property already exploited commercially in European lozenge formulations targeting throat pain and inflammation.

The link between Ambroxol's established respiratory mucosal activity and nasal cavity disease is anatomically straightforward: the nasal cavity is the proximal segment of the same mucosal surface that Ambroxol acts upon in the lower airways. Impaired mucociliary function and mucus stagnation are central to many nasal cavity conditions, including rhinitis, sinusitis, and post-viral nasal inflammation. Ambroxol's additional anti-inflammatory actions — reported NF-κB inhibition and reduced prostaglandin synthesis — provide a secondary mechanistic rationale.

That said, the current literature retrieved by the search pipeline focuses exclusively on "acute cough" in the setting of viral upper respiratory infections, rather than on nasal cavity disease as a discrete target. The mechanistic link is biologically coherent but remains an indirect inference. No direct preclinical or clinical studies targeting nasal cavity disease with Ambroxol were identified in this Evidence Pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ambroxol + Nasal Cavity Disease in ClinicalTrials.gov or ICTRP.

> **Note:** External databases (ClinicalTrials.gov) do contain Ambroxol studies for broader upper respiratory and ENT indications. A targeted search using MeSH terms for rhinitis, sinusitis, and nasal mucosal disease is recommended to confirm whether relevant trials have been missed by the current query scope.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Narrative Review | *Vestnik otorinolaringologii* | Discusses Ambroxol as a treatment option for acute cough in influenza and ARVI. Notes that acute viral cough is typically non-productive and self-limiting (2–3 weeks), but in some patients becomes productive with mucus abnormalities — the scenario where mucolytic agents like Ambroxol are considered. No direct nasal cavity outcome data reported. |

---

## India Market Information

Ambroxol is currently **not marketed** in the India regulatory database reviewed for this report. No product authorizations or registered licenses were found (total registrations: 0). This is consistent with the drug's global regulatory status, where it is approved by several individual European national agencies but not by the FDA or EMA as a centrally authorized product.

---

## Safety Considerations

**Drug Interactions:**

- **Glucosylceramidase beta (GBA1):** Ambroxol displays a context-dependent interaction with GBA1 (the enzyme deficient in Gaucher disease and implicated in GBA-associated Parkinson's disease). At neutral pH (e.g., in cerebrospinal fluid), Ambroxol acts as an *inhibitory* GCase chaperone, temporarily reducing extracellular enzyme activity. Within cells and acidic lysosomes, the same chaperone effect *increases* intracellular GCase activity by improving enzyme trafficking to the lysosome. This pharmacological duality is being actively investigated in clinical trials for Parkinson's disease and ALS/MND (EMA granted orphan designation for ALS in July 2018). Clinically, this interaction is most relevant in patients with GBA1 mutations or lysosomal storage disorders — a population that would require careful monitoring if Ambroxol were prescribed.

Please refer to the package insert (available from EMA SmPC or national agency product monographs) for full warnings and contraindications, which could not be retrieved in this Evidence Pack due to a data gap.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.91% is striking, and there is a biologically coherent mechanistic pathway connecting Ambroxol's mucolytic and anti-inflammatory properties to nasal cavity disease. However, the evidence base currently consists of a single narrative review tangentially related to nasal symptoms, placing this firmly at L4 — mechanistic plausibility without clinical validation. This does not justify immediate development investment, but the hypothesis is worth structured follow-up.

**To proceed, the following is needed:**

- **Expand literature search:** Query PubMed/EMBASE with MeSH terms specifically for Ambroxol + rhinitis, sinusitis, nasal mucosal disease, and upper airway inflammation to confirm whether relevant evidence was missed by the current query scope
- **Retrieve MOA data:** Query DrugBank API (DB06742) to obtain full pharmacological profile, target list, and enzyme interaction data
- **Retrieve safety data:** Download and parse the EMA SmPC or a national-level package insert to complete the key warnings and contraindications assessment (currently a blocking data gap)
- **Evaluate delivery routes:** Determine whether existing formulations (oral syrup, lozenge, inhalation) are compatible with nasal cavity disease — or whether a nasal spray formulation would be required for clinical relevance
- **KG path audit:** Review the TxGNN knowledge graph path connecting Ambroxol to nasal cavity disease to distinguish true biological connectivity from topological proximity artifacts (as observed in lower-ranked predictions such as faucial diphtheria and vulvovaginal candidiasis, where high scores appear driven by mucosal node proximity rather than pharmacological mechanism)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

