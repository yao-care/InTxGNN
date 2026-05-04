---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin type A (ETA) receptor antagonist, approved internationally for pulmonary arterial hypertension (PAH) but not yet registered in India.
The TxGNN model predicts it may be effective for **Pulmonary Arteriovenous Malformation (AVM)**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.
Notably, co-predictions for PAH subtypes — including PAH associated with congenital heart disease (L2), HIV infection (L1), and connective tissue disease (L2) — carry substantially stronger evidence and represent more immediately actionable repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — approved globally (US/EU); not registered in India |
| Predicted New Indication | Pulmonary Arteriovenous Malformation (disease) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action (MOA) data is not documented in this Evidence Pack. Based on established pharmacology, Ambrisentan is a highly selective endothelin type A (ETA) receptor antagonist. It competitively blocks ET-1 binding to ETA receptors on pulmonary arterial smooth muscle and endothelial cells, reducing pulmonary vasoconstriction and vascular remodeling — the core pathophysiology of PAH. Its selectivity for ETA over ETB is clinically relevant because preserved ETB receptor activity maintains endogenous NO production and vascular clearance of ET-1.

Pulmonary arteriovenous malformations (PAVMs) are predominantly structural vascular anomalies, most commonly arising in patients with Hereditary Hemorrhagic Telangiectasia (HHT), a rare autosomal dominant disorder caused by mutations in the *ACVRL1* or *ENG* genes — both encoding components of the TGF-β/BMP signaling pathway. A subset of HHT patients (estimated 5–15%) concurrently develop PAH. It is in this specific HHT-PAH overlap population that an endothelin receptor antagonist like Ambrisentan could theoretically provide benefit. The mechanistic link is therefore indirect: Ambrisentan would target the PAH complication co-occurring with HHT, not the PAVM structural lesion itself.

The sole supporting publication (PMID 33969094) precisely describes this overlap scenario — an HHT patient who developed PAH and underwent PAH-targeted therapy, with family gene analysis revealing ACVRL1/ENG mutation implicating the endothelin signaling axis. The TxGNN model likely captured this biological connection through shared knowledge-graph nodes (*ACVRL1/ENG* ↔ endothelin pathway ↔ PAH), but this does not imply Ambrisentan can structurally reverse or ablate PAVM lesions. The prediction reflects a comorbidity-driven opportunity rather than a primary PAVM mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Pulmonary Arteriovenous Malformation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World Journal of Clinical Cases | HHT patient with concurrent PAH treated with PAH-targeted therapy; family gene analysis identified ACVRL1/ENG mutation, illustrating the HHT-PAH co-morbidity where endothelin-axis therapies may be relevant |

---

## Safety Considerations

**Drug Interactions**: Ambrisentan has 112 documented interactions. The most clinically significant are listed below:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Canagliflozin | Moderate | Monitor when co-administered |
| Dapagliflozin | Moderate | Monitor when co-administered |
| Empagliflozin | Moderate | Monitor when co-administered |
| Ertugliflozin | Moderate | Monitor when co-administered |
| Eliglustat | Moderate | Monitor when co-administered |
| Naltrexone | Moderate | Monitor when co-administered |
| Clarithromycin | Minor | Routine monitoring sufficient |
| Miconazole | Minor | Routine monitoring sufficient |
| Omeprazole | Minor | Routine monitoring sufficient |

Please refer to the package insert for complete warnings and contraindications (formal India package insert data not available in this Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns Pulmonary AVM the highest prediction score (99.41%), the mechanistic link is indirect — Ambrisentan targets PAH co-occurring in HHT patients rather than the AVM lesion itself — and clinical evidence is limited to a single case report, placing it at L4. This is insufficient to support clinical advancement for this specific indication. The more compelling repurposing story lies in the co-predicted PAH subtypes (ranks 2–4), all of which share the same ETA-antagonism mechanism and are supported by Phase 2/3 level evidence.

**To proceed, the following is needed:**

- **MOA documentation**: Obtain formal DrugBank MOA and DrugBank categories to complete the mechanism-of-action analysis and confirm non-antineoplastic classification
- **Package insert review**: Retrieve India or international package insert (Letairis/Volibris) for warnings, contraindications, and hepatotoxicity monitoring requirements
- **Redirect primary evaluation**: Prioritize higher-evidence co-predictions:
  - PAH-CHD (L2): NCT01808313, Phase 3b, completed in Chinese population — directly actionable for India market
  - PAH-HIV (L1): NCT00709956, Phase 3 double-blind RCT — meets highest evidence threshold
  - PAH-CTD (L2): Multiple completed trials including AMBITION post-hoc CTD-PAH subgroup (PMID 28039187, 32161055)
- **For PAVM specifically**: Conduct a systematic review to determine whether HHT/PAVM patients were included in any existing Ambrisentan PAH registrational trials; assess whether PAVM+PAH co-morbidity constitutes a viable labeling sub-indication
- **DDI safety audit**: Review all 112 documented interactions with focus on antiretroviral drugs (for PAH-HIV subgroup, given potential CYP3A4/P-gp interplay) and immunosuppressants (for PAH-CTD subgroup)
- **India regulatory pathway**: Assess feasibility of new drug application or importation approval for Ambrisentan in India, given zero existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

