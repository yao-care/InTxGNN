---
layout: default
title: Stanozolol
parent: 僅模型預測 (L5)
nav_order: 782
evidence_level: L5
indication_count: 10
---

# Stanozolol
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

# Stanozolol: From Anabolic-Androgenic Steroid Therapy to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

> Stanozolol is an anabolic-androgenic steroid; no specific original indication is recorded in the available regulatory dataset for this market.
> The TxGNN model predicts it may be effective for **C1 Inhibitor Deficiency (Hereditary Angioedema)**,
> a use already echoed in the older medical literature, with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug class: anabolic-androgenic steroid) |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema) |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Stanozolol in this evidence pack. Based on known pharmacology, Stanozolol belongs to the class of **attenuated (anabolic-androgenic) androgens**, a group of agents historically shown to increase hepatic synthesis of several plasma proteins, including C1 esterase inhibitor (C1-INH) and other serpin-family proteins.

This mechanistic link is not purely theoretical — several papers in the evidence set explicitly describe Stanozolol being used clinically as **prophylactic therapy for hereditary angioedema due to C1-INH deficiency**, predating the availability of modern C1-INH concentrates and bradykinin-pathway antagonists (e.g., Greaves & Lawlor 1991: *"Prophylactic therapy is possible with danazol or stanozolol"*; Bhivgade et al. 2012 and Guilarte et al. 2008 describe individual patients maintained on stanozolol). This suggests the TxGNN prediction is re-surfacing a **known but currently under-utilized therapeutic role**, rather than an entirely novel mechanistic hypothesis.

The absence of registered clinical trials reflects that this use pattern predates modern trial registries and has largely been documented through case series, case reports, and narrative/systematic reviews rather than randomized controlled trials — consistent with how attenuated androgens were adopted into HAE management practice historically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25707325](https://pubmed.ncbi.nlm.nih.gov/25707325/) | 2015 | Systematic Review | Ann Allergy Asthma Immunol | Risk-benefit appraisal of long-term androgen (incl. attenuated androgens) use in HAE |
| [31826031](https://pubmed.ncbi.nlm.nih.gov/31826031/) | 2018 | Review | Allergologie select | Update on acute and prophylactic treatment options for HAE due to C1-INH deficiency |
| [22729959](https://pubmed.ncbi.nlm.nih.gov/22729959/) | 2012 | Review | Curr Allergy Asthma Rep | Overview of current HAE management options, including androgen prophylaxis |
| [18220148](https://pubmed.ncbi.nlm.nih.gov/18220148/) | 2008 | Review | Ann Allergy Asthma Immunol | 40-50 year literature review on attenuated androgens for HAE treatment |
| [1518394](https://pubmed.ncbi.nlm.nih.gov/1518394/) | 1992 | Case Series (n=235) | Medicine | Biological and clinical characteristics of hereditary/acquired C1-INH deficiency |
| [8356982](https://pubmed.ncbi.nlm.nih.gov/8356982/) | 1993 | Case Series (n=8) | Am J Med | Autoimmune C1 inhibitor deficiency, clinical and treatment response features |
| [26727765](https://pubmed.ncbi.nlm.nih.gov/26727765/) | 2015 | Observational Study | J Investig Allergol Clin Immunol | Clinical pattern and acute/long-term management of HAE due to C1-INH deficiency |
| [1869690](https://pubmed.ncbi.nlm.nih.gov/1869690/) | 1991 | Review | J Am Acad Dermatol | Angioedema classification and management, notes danazol/stanozolol prophylaxis |
| [23248378](https://pubmed.ncbi.nlm.nih.gov/23248378/) | 2012 | Case Report | Indian J Dermatol | Type 1 HAE patient started on stanozolol 2 mg TID |
| [18447143](https://pubmed.ncbi.nlm.nih.gov/18447143/) | 2008 | Case Report | J Investig Allergol Clin Immunol | HAE patient remained clinically stable on stanozolol therapy |

---

## India Market Information

Stanozolol currently holds **no marketing authorization** in this market — the regulatory dataset lists zero registered licenses ("Not Marketed"). No product/dosage-form records are available for review.

---

## Safety Considerations

- **Drug Interactions**: DDI screening identified **69 total interactions**. Notable entries include:
  - **Major**: Carfilzomib
  - **Moderate**: Corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide), asparaginase products (Asparaginase E. coli/Erwinia, Calaspargase pegol), Cyclosporine, Clofarabine, Brentuximab vedotin, Chlorpropamide, Cannabidiol
  - Notably, moderate interactions are also flagged with agents used in current HAE treatment (**Human C1-esterase inhibitor**, **Conestat alfa**) — relevant if Stanozolol is considered alongside modern C1-INH replacement therapy.
- Detailed product-label warnings and contraindications are **not yet available** for this drug in the evidence pack (pending label retrieval — see data gap remediation below); no clinical safety claims should be made until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists — the drug label warnings/contraindications required for initial safety screening (S1) have not yet been retrieved, and Stanozolol is currently unregistered in this market. While decades of case-series/review literature support a mechanistically plausible and historically practiced role for attenuated androgens in HAE prophylaxis, the evidence level (L3) rests on observational data and reviews rather than controlled trials.

**To proceed, the following is needed:**
- Retrieve and parse the official product label (warnings/contraindications) — Blocking gap (DG001)
- Confirm mechanism of action via DrugBank API — High priority gap (DG002)
- Comparative positioning analysis against modern first-line HAE therapies (C1-INH concentrates, bradykinin B2 antagonists, kallikrein inhibitors), given attenuated androgens are now largely a second-line/legacy option
- Long-term androgen safety monitoring protocol (liver function, lipid profile, virilization risk) if local registration is pursued
- Review potential interaction management when co-administered with modern C1-INH replacement products (Human C1-esterase inhibitor, Conestat alfa)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

