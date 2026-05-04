---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 4
---

# Acitretin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Acitretin: From Psoriasis to Acne (Disease)

## One-Sentence Summary

Acitretin is a second-generation aromatic retinoid, well established for the systemic treatment of severe psoriasis and hyperkeratotic skin disorders.
The TxGNN model predicts it may be effective for **Acne (disease)** — most strongly for the acne inversa/hidradenitis suppurativa spectrum —
with **1 clinical trial** and **18 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis / severe keratinization disorders (not currently registered in India) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data from DrugBank is unavailable for this analysis. Based on published literature, acitretin is a second-generation aromatic retinoid that acts through nuclear retinoic acid receptors (RAR-α/γ), normalizing keratinocyte differentiation and suppressing aberrant epidermal proliferation. It is the active free-acid metabolite of etretinate and is primarily indicated for severe, recalcitrant psoriasis.

The mechanistic link between acitretin and acne lies in the shared role of the RAR pathway in regulating sebaceous gland activity and follicular keratinization — two core pathological drivers of acne. Acitretin's closely related compound, isotretinoin (13-cis-retinoic acid), is the gold standard for severe acne vulgaris, acting through overlapping retinoid receptor pathways to suppress sebum production and normalize follicular epithelium. Preclinical data also demonstrates acitretin's ability to inhibit eosinophil leukotriene (LTC4) release, supporting an anti-inflammatory mechanism relevant to acne pathology.

Critically, the evidence base most strongly supports acitretin for **acne inversa / hidradenitis suppurativa (HS)** rather than common acne vulgaris. Over 25 years of accumulated case observations and retrospective series document meaningful clinical responses to acitretin in HS, and the European S1 guideline formally acknowledges it as a systemic treatment option. The TxGNN score of 99.94% reflects the close mechanistic proximity between retinoid biology and acne-spectrum disease, though dedicated RCT evidence for acitretin specifically in acne remains sparse.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study assessing whether **isotretinoin** (not acitretin) increases COVID-19 risk via retinoid-induced nasal mucosal dryness. Low direct relevance to acitretin repurposing for acne. |

> **Note:** No clinical trials directly evaluating acitretin for acne were identified. The single trial retrieved examines a related retinoid (isotretinoin) for an unrelated safety question.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Retrospective Series | Br J Dermatol | 25-year long-term retrospective of **acitretin in hidradenitis suppurativa (acne inversa)**; scattered case reports showed promising results, the most direct evidence for acitretin in acne-spectrum disease |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case Report | Cutis | Case of severe nodulocystic facial acne + HS treated with **acitretin** after two full courses of isotretinoin; partial but meaningful clinical response reported |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Clinical Guideline | J Eur Acad Dermatol Venereol | European S1 guideline for HS/acne inversa; acitretin is recognized among systemic treatment options for this chronic inflammatory follicular disease |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Der Hautarzt | Drug therapy review for acne inversa; discusses retinoids including acitretin alongside TNF-α inhibitors (adalimumab) and combination antibiotics |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Comprehensive review of retinoids (oral and topical) in dermatology; covers acitretin's established role in psoriasis and keratosis, with discussion of acne-spectrum applications |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Reviews retinoid use across psoriasis, severe acne, keratotic disorders, and chemoprevention; establishes the mechanistic breadth applicable to the acne prediction |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Mechanistic Review | Dermatology | Explores retinoid inhibition of sebaceous gland activity; discusses whether anti-acne effects of oral retinoids including acitretin can be predicted from experimental models |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Review | Clin Pharmacokinet | Pharmacokinetics and therapeutic efficacy of retinoids; clarifies distinct receptor profiles of isotretinoin (acne) vs. etretinate/acitretin (psoriasis), relevant to understanding class differences |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Mechanistic Study | Prostaglandins | Acitretin among 8 retinoids tested for inhibition of eosinophil LTC4 release; provides mechanistic evidence for anti-inflammatory properties relevant to acne pathology |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of drugs for discoid lupus erythematosus; assesses acitretin/retinoids as agents, confirming the immunomodulatory breadth of the drug class across inflammatory skin conditions |

---

## India Market Information

Acitretin is **not currently registered or marketed in India**. No drug authorization records were identified (total licenses: 0). Clinicians requiring this drug would need to explore special import pathways or licensed compassionate use programs under applicable CDSCO regulations.

---

## Safety Considerations

**Drug Interactions** (113 total interactions identified; key interactions listed below):

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Vitamin A | **Major** | Additive retinoid toxicity (hypervitaminosis A); concurrent use contraindicated |
| Doxycycline | **Major** | Risk of pseudotumor cerebri (benign intracranial hypertension) |
| Minocycline | **Major** | Risk of pseudotumor cerebri |
| Tetracycline | **Major** | Risk of pseudotumor cerebri |
| Glipizide | Moderate | Altered glycemic control in diabetic patients |
| Glyburide | Moderate | Altered glycemic control |
| Glimepiride | Moderate | Altered glycemic control |
| Chlorpropamide | Moderate | Altered glycemic control |
| Tolbutamide | Moderate | Altered glycemic control |
| Tolazamide | Moderate | Altered glycemic control |
| Acetohexamide | Moderate | Altered glycemic control |
| Naltrexone | Moderate | Interaction details to be clarified |

> Package insert warnings and contraindications were not available in this evidence pack. Acitretin carries well-documented **teratogenicity (Pregnancy Category X)** — a critical safety concern that requires a strict pregnancy prevention program for any female patient of childbearing potential. Please refer to the full prescribing information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for acitretin in acne (disease) sits at L4 — supported by mechanistic reasoning, case reports, and indirect inference from related retinoid literature — with no dedicated clinical trials and zero market registration in India. The most evidence-supported sub-indication (acne inversa/HS) is clinically distinct from common acne vulgaris, requiring a clearer target definition before advancing.

**To proceed, the following is needed:**

- Retrieve formal MOA documentation from DrugBank API to confirm RAR-α/γ receptor profile
- Obtain package insert from a reference regulatory source (e.g., EMA, US FDA) to complete the safety profile, including teratogenicity warnings and contraindications
- **Clarify target indication**: acne inversa/HS (moderate existing evidence, L3-L4) versus acne vulgaris (very limited direct evidence, L4-L5)
- If focusing on HS: conduct a focused systematic review and consider designing a Phase 2 pilot RCT comparing acitretin to current standard of care
- Evaluate India-specific regulatory pathway for introduction of acitretin (import license, new drug application, or compassionate use), given current zero-registration status
- Mandatory safety protocol: any clinical program must include a strict **pregnancy prevention program** given acitretin's teratogenic potential, particularly relevant for the acne patient population which skews young and female
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

