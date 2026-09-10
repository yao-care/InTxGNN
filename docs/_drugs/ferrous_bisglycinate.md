---
layout: default
title: Ferrous Bisglycinate
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Ferrous Bisglycinate
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

# Ferrous bisglycinate: From Iron Deficiency to Bronchitis

## One-Sentence Summary

Ferrous bisglycinate is an oral iron supplement (a glycine-chelated form of ferrous iron) commonly used for iron deficiency and iron deficiency anemia. The TxGNN model predicts a possible association with **Bronchitis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the connection as likely indirect/noise rather than a causal mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency / iron deficiency anemia (general pharmacological knowledge; no India license record exists to cite, as the product is not marketed) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, ferrous bisglycinate is an oral iron salt in which ferrous iron is chelated to glycine to improve gastrointestinal absorption and bioavailability; its established role is correcting iron deficiency and supporting erythropoiesis (red blood cell production).

There is no known direct physiological pathway connecting iron repletion to bronchial inflammation. The evidence pack's own mechanistic assessment for this candidate states explicitly: *"no known mechanism: Ferrous bisglycinate acts on intestinal absorption and hematopoiesis, with no direct physiological pathway to bronchial inflammation,"* and suggests the high TxGNN score (0.974) more likely reflects an indirect knowledge-graph association — such as the known comorbidity between iron-deficiency anemia and chronic respiratory disease (anemia of chronic disease) — rather than a causal repurposing signal.

This interpretation is reinforced by the broader prediction list for this drug: several other top-ranked candidates (gastroduodenitis, peptic ulcer disease) represent **known adverse-effect directions** of oral iron (GI mucosal irritation), and a cluster of unrelated coagulation-factor disorders (heparin cofactor 2 deficiency, antithrombin deficiency, factor V excess, thrombophilia) appear consecutively in the ranking, suggesting a knowledge-graph clustering artifact rather than independent pharmacological signals. Taken together, the bronchitis prediction should be treated as **hypothesis-generating only**, not as a mechanistically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

This product currently has no drug registration/license records in India (market status: **Not Marketed**, total registrations: 0). No approved indication text is available for reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/local labeling warnings and contraindications are recorded as a Blocking data gap — DG001 — meaning a formal safety assessment (S1 stage) cannot proceed until this information is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is based solely on a TxGNN model score (L5, no supporting clinical trials or literature), and the model's own rationale identifies no plausible mechanistic link — with some corroborating context (adjacent predictions) suggesting the signal cluster may be graph-embedding noise rather than a genuine pharmacological association. The drug is also not currently marketed in India, and mechanism-of-action and labeling/safety data are both missing (one at Blocking severity).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product labeling (warnings, contraindications) before any safety evaluation can begin
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank or another authoritative source
- Preclinical or mechanistic studies specifically linking iron repletion/chelation to airway inflammation, to establish biological plausibility beyond the KG association
- Continued monitoring of ClinicalTrials.gov, ICTRP, and PubMed for any emerging trials or publications on this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

