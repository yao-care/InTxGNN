---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab (Tysabri) is a monoclonal antibody that blocks α4-integrin, approved internationally for relapsing-remitting multiple sclerosis and Crohn's disease.
The TxGNN model predicts it may be effective for **Bronchitis**, however currently **0 clinical trials** and **0 publications** directly support this specific indication.
With evidence level L5, this prediction is based solely on computational modelling and requires substantial further investigation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Sclerosis (Relapsing-Remitting) / Crohn's Disease |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided dataset. Based on the repurposing rationale embedded in the evidence pack, Natalizumab blocks α4β1 and α4β7 integrins — the same receptors responsible for directing immune cells (eosinophils and lymphocytes) toward mucosal tissues. In theory, blocking this trafficking pathway could reduce inflammatory cell infiltration into the bronchial mucosa, offering an indirect anti-inflammatory effect in eosinophilic subtypes of bronchitis.

However, the mechanistic link is considered biologically weak for this indication. Bronchitis encompasses a highly heterogeneous group of conditions — ranging from infectious (bacterial, viral) to purely inflammatory origins — and α4-integrin is not recognised as a core pathogenic driver in any of these subtypes. The anti-adhesion mechanism that works well in CNS-directed neuroinflammation (MS) and gut-directed inflammation (Crohn's) does not translate clearly to the bronchial epithelium.

As a result, this prediction likely reflects structural or co-occurrence patterns within the TxGNN knowledge graph rather than a validated therapeutic signal. The absence of any supporting clinical trial or published literature reinforces that this remains a computational hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Natalizumab is currently not marketed in India. No product authorizations are on record.

---

## Safety Considerations

**Drug Interactions (273 total interactions on record):**

The following major interactions warrant particular attention in any clinical planning:

| Interacting Drug | Severity |
|-----------------|----------|
| Hydrocortisone | Major |
| Triamcinolone | Major |
| Dexamethasone | Major |
| Betamethasone | Major |
| Budesonide | Major |
| Prednisolone | Major |
| Prednisone | Major |
| Triamcinolone (ophthalmic) | Major |
| Iobenguane (I-131) | Major |
| Ibritumomab tiuxetan | Major |
| Tositumomab (I-131) | Major |
| Tositumomab | Major |
| Levamisole | Major |
| Trimetrexate | Major |
| Mercaptopurine | Major |
| Naltrexone | Moderate |
| Zinc sulfate / acetate / gluconate / chloride | Minor |

> Note: The pattern of major interactions — predominantly corticosteroids and immunosuppressants — is consistent with Natalizumab's known immunomodulatory profile and the heightened risk of opportunistic infections (including PML) when combined with other immunosuppressive agents.

Please refer to the package insert for key warnings and contraindications, as this data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN computational score (99.46%), there is zero clinical, observational, or preclinical evidence linking Natalizumab to bronchitis treatment. The mechanistic hypothesis is speculative and weak, and bronchitis aetiology is too heterogeneous to support a targeted repurposing strategy without foundational data.

**To proceed, the following is needed:**
- Preclinical studies (e.g., murine models of eosinophilic or allergic bronchitis) to test whether α4-integrin blockade produces measurable bronchial anti-inflammatory effects
- Disease subtype clarification: if any benefit is plausible, it would likely be limited to eosinophilic or allergic bronchitis, not infectious bronchitis
- Complete MOA data retrieved from DrugBank (DG002 remediation)
- Full safety package insert from CDSCO/FDA for key warnings and contraindications (DG001 remediation)
- Comparison with existing bronchitis therapies (inhaled corticosteroids, β2-agonists) to assess whether a systemic monoclonal antibody offers any advantage in risk-benefit terms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

