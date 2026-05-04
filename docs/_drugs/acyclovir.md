---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpes Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is a nucleoside analogue antiviral with well-established efficacy against herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
with **0 clinical trials** and **2 publications** currently supporting this direction — neither of which directly tests Acyclovir as a treatment for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpes simplex virus infections; varicella-zoster virus infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established medical knowledge, Acyclovir is a synthetic nucleoside analogue that, upon entry into virus-infected cells, is selectively converted to its active triphosphate form by viral thymidine kinase (TK). The active metabolite then competitively inhibits the viral DNA polymerase, halting viral replication. This TK-dependent activation is the cornerstone of Acyclovir's selectivity — it acts preferentially in HSV- and VZV-infected cells while sparing healthy host cells.

Punctate epithelial keratoconjunctivitis is typically caused by adenoviruses (serotypes 3, 7, 8, 19, 37) or, in some populations, Microsporidia. Critically, neither adenoviruses nor Microsporidia encode a thymidine kinase. Without this viral enzyme, Acyclovir cannot be phosphorylated into its active form, making the standard antiviral mechanism mechanistically non-functional against these pathogens. This represents a fundamental incompatibility between drug mechanism and disease etiology.

The TxGNN model's high prediction score (99.67%) most likely reflects a broad knowledge graph association between the "ocular infections" node and "antiviral drugs" rather than a specific, direct efficacy signal for PEK. The two retrieved publications concern corneal lipidosis in AIDS patients and microsporidial keratoconjunctivitis epidemiology — neither involves Acyclovir as a therapeutic intervention for punctate epithelial keratoconjunctivitis. This is a cautionary example of a high TxGNN score driven by indirect node relationships in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case Series | American Journal of Ophthalmology | Two AIDS patients treated for opportunistic infections developed bilateral ocular surface changes consistent with drug-induced corneal lipidosis; describes phospholipid accumulation in lysosomal membranes but does not involve Acyclovir as a PEK treatment |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian Journal of Pathology & Microbiology | Case series characterizing microsporidial keratoconjunctivitis in an eastern Indian cohort; describes Microsporidia as intracellular parasites causing MKC; Acyclovir not mentioned as treatment |

> ⚠️ Neither publication supports Acyclovir as an effective or tested treatment for punctate epithelial keratoconjunctivitis.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Punctate epithelial keratoconjunctivitis is caused by adenoviruses and Microsporidia, neither of which encodes the thymidine kinase required for Acyclovir activation. There is no mechanistic rationale for this repurposing candidate, the evidence level is L5 (model prediction only), and the high TxGNN score almost certainly reflects an indirect knowledge graph artifact rather than a genuine therapeutic signal.

**To proceed, the following is needed:**
- Identification of any TK-independent antiviral mechanism that could explain activity against adenovirus or Microsporidia
- In vitro testing of Acyclovir against the clinically relevant adenovirus serotypes (8, 19, 37) to determine minimum inhibitory concentrations
- Mechanistic hypothesis generation distinct from the standard TK-phosphorylation pathway
- Complete safety profile retrieval from the package insert (currently unavailable due to data gap DG001)
- MOA confirmation via DrugBank API query (data gap DG002) before any further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

