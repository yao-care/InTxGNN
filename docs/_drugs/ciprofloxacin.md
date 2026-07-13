---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic widely used in clinical practice for the treatment of bacterial infections, including urinary tract, respiratory, gastrointestinal, and systemic infections.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma**, with **0 clinical trials** and **2 publications** currently supporting this direction.
The evidence base remains early-stage, warranting further mechanistic and clinical investigation before advancing this hypothesis beyond a research question.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum fluoroquinolone antibiotic; no India registration data available) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Ciprofloxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase (topoisomerase II) and topoisomerase IV, blocking DNA replication and repair to achieve bactericidal activity. It has broad-spectrum coverage against gram-negative and many gram-positive organisms, with high oral bioavailability (>70%) and excellent tissue penetration.

Two plausible — though as yet unproven — mechanistic pathways connect ciprofloxacin to diffuse scleroderma. The first is a direct antifibrotic effect: preclinical and early clinical observations suggest that ciprofloxacin may inhibit fibroblast activation and collagen synthesis, directly targeting the excessive fibrosis that defines scleroderma pathology. The second is an indirect route via gut microbiome modulation: systemic sclerosis patients frequently develop small intestinal bacterial overgrowth (SIBO) secondary to gut dysmotility, and ciprofloxacin's antibiotic activity could reduce microbial dysbiosis and the resulting systemic inflammatory burden.

These hypotheses are supported by a 2010 double-blind randomized pilot study specifically evaluating ciprofloxacin as an antifibrotic agent in scleroderma skin (PMID 20507401), and by a 1995 observational study documenting SIBO in systemic sclerosis patients treated with antibiotics including ciprofloxacin (PMID 7728404). Both studies are small and early-phase, placing the overall evidence at L4. Importantly, the topoisomerase II inhibition mechanism shared by fluoroquinolones and certain chemotherapeutic agents may also confer indirect immunomodulatory effects relevant to autoimmune fibrosis — though this remains speculative without dedicated studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ciprofloxacin in diffuse scleroderma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Clinical Observation / Small Study | The Journal of Dermatology | Controlled, double-blind randomized pilot study evaluating oral ciprofloxacin as an antifibrotic agent in the skin of scleroderma patients; tested whether ciprofloxacin reduces fibrosis severity — the first published RCT framework for this indication |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational Study | British Journal of Rheumatology | 24 systemic sclerosis patients (including 6 with diffuse disease) investigated for SIBO via jejunal aspiration; antibiotic treatment outcomes documented, supporting the gut dysbiosis pathway as a secondary therapeutic rationale |

---

## India Market Information

Ciprofloxacin currently has **0 approved product registrations** in India per this dataset. No authorization records are available. The drug's regulatory status in India cannot be evaluated for repurposing purposes based on available data.

---

## Safety Considerations

**Drug Interactions**: Ciprofloxacin carries a substantial interaction burden with **417 documented drug-drug interactions**. The following Major-level interactions are clinically relevant, particularly in the context of scleroderma management where corticosteroids are frequently co-prescribed:

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|--------------------|
| Hydrocortisone | Major | Fluoroquinolone + corticosteroid combination significantly increases risk of tendon rupture and tendinopathy |
| Dexamethasone | Major | Same mechanism as above; often used in scleroderma-related inflammatory flares |
| Betamethasone | Major | Heightened tendinopathy risk; monitor musculoskeletal symptoms closely |
| Triamcinolone | Major | Risk of tendon damage; avoid periarticular injections during ciprofloxacin therapy |
| Bupropion | Major | CYP1A2 inhibition by ciprofloxacin may elevate bupropion plasma levels, increasing seizure risk |

> ⚠️ **Note for Scleroderma Context**: The five Major interactions with corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide as Moderate) are particularly significant because corticosteroids are standard components of scleroderma management. Any clinical trial or compassionate use protocol must explicitly address tendinopathy monitoring and risk mitigation.

Additional Moderate interactions were identified with commonly co-prescribed agents including Metformin, Acetylsalicylic acid, Famotidine, and Loperamide — all relevant in a scleroderma population with gastrointestinal involvement.

Please refer to the approved package insert for complete warnings and contraindications; these were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis linking ciprofloxacin to diffuse scleroderma is biologically plausible — supported by one small double-blind randomized pilot study and one observational study — but evidence remains at L4 level with no registered clinical trials, no India regulatory foothold, and unresolved safety data gaps. The drug's substantial DDI burden with corticosteroids (Major interactions) presents an additional barrier requiring explicit protocol design before any clinical advancement.

**To proceed, the following is needed:**
- Retrieval and review of the full ciprofloxacin package insert (from any approved jurisdiction: FDA, EMA, or CDSCO) to document formal warnings, contraindications, and black box alerts
- Mechanism of action verification via DrugBank API (DB00537) to confirm antifibrotic and immunomodulatory pharmacology
- Systematic review or meta-analysis of antibiotic use in systemic sclerosis, specifically ciprofloxacin's antifibrotic and SIBO-targeting effects
- Phase 2 proof-of-concept clinical trial with skin fibrosis biomarkers (modified Rodnan Skin Score, TGF-β, collagen type I/III levels) as primary endpoints
- Tendinopathy risk management protocol if corticosteroids are included in the study population's background therapy
- Assessment of India-specific scleroderma epidemiology and patient access pathways before local regulatory strategy is developed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

