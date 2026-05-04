---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 8
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a broad-spectrum aminopenicillin antibiotic widely used for the treatment of bacterial infections including respiratory, urinary tract, ear, and skin infections.
The TxGNN model's top-ranked prediction is **Polyclonal Hyperviscosity Syndrome**, with **0 clinical trials** and **0 publications** directly supporting this indication (Evidence Level: L5).
Across all 8 predicted indications in this Evidence Pack, the most clinically actionable signal is **Rank #6 — Monoclonal Gammopathy (IPSID subtype)**, which carries an L3 evidence rating, 1 terminated clinical trial, and 11 supporting publications with a plausible mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum; gram-positive and gram-negative coverage) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | Not marketed (0 registrations on file) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

> **Data Note:** The regulatory dataset shows 0 registrations for Amoxicillin in India. This is almost certainly a data collection gap — Amoxicillin is one of the most widely dispensed antibiotics globally and in India. Verification against the live CDSCO database is strongly recommended before drawing any regulatory conclusions.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacology, Amoxicillin is an aminopenicillin antibiotic that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and triggering bacterial cell lysis. It has a broad spectrum of activity against gram-positive organisms (e.g., *Streptococcus*, *Staphylococcus*) and selected gram-negative organisms (e.g., *H. pylori*, *E. coli*, *H. influenzae*).

The theoretical connection to polyclonal hyperviscosity syndrome rests on the following chain: chronic bacterial infections (notably *H. pylori*, but also HIV and HCV) can drive polyclonal B-cell activation, leading to excessive immunoglobulin production, which in turn raises serum viscosity. Treating the underlying infection with Amoxicillin could theoretically reduce the antigenic stimulus and indirectly lower immunoglobulin levels. This mechanistic pathway is highly indirect and depends on multiple unverified intermediate steps.

In practice, no clinical study, case report, or preclinical model has specifically investigated Amoxicillin for polyclonal hyperviscosity syndrome. The TxGNN model's high score most likely reflects broad "infection node → haematological disease node" connectivity within the knowledge graph rather than genuine biological plausibility for this specific condition. This prediction is best interpreted as a graph-level noise signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amoxicillin in Polyclonal Hyperviscosity Syndrome.

---

## Literature Evidence

Currently no related literature available for Amoxicillin in Polyclonal Hyperviscosity Syndrome.

---

## India Market Information

No marketing authorizations are on file in the current regulatory dataset (0 licenses retrieved).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No records found |

> As noted above, this likely reflects an incomplete regulatory data pull. Amoxicillin (oral and injectable formulations) is widely approved and marketed in India. CDSCO database manual verification is recommended.

---

## Safety Considerations

**Drug Interactions** — 271 total interactions identified (DDInter database). Key interactions are listed below:

| Severity | Interacting Drug | Clinical Relevance |
|----------|-----------------|-------------------|
| **Major** | Vibrio cholerae CVD 103-HgR strain live antigen (live oral cholera vaccine) | Amoxicillin may kill the live vaccine organism, reducing vaccine immunogenicity; schedule vaccination at least 14 days before or after antibiotic course |
| **Major** | Methotrexate | Amoxicillin reduces renal tubular secretion of methotrexate, increasing methotrexate plasma levels and risk of serious toxicity (myelosuppression, mucositis) |
| Moderate | Doxycycline / Minocycline / Demeclocycline | Pharmacodynamic antagonism: bactericidal (amoxicillin) vs. bacteriostatic (tetracyclines); concurrent use may reduce efficacy of both agents |
| Moderate | Ethinylestradiol / Estradiol | Disruption of gut flora may reduce enterohepatic recirculation of oestrogens, potentially decreasing hormonal contraceptive efficacy |
| Moderate | Mycophenolate mofetil | Gut flora disruption may reduce enterohepatic recycling of mycophenolic acid, lowering immunosuppressant exposure in transplant patients |
| Moderate | Anisindione / Dicoumarol | Enhanced anticoagulant effect; monitor INR closely |
| Moderate | Balsalazide | Amoxicillin may reduce conversion of balsalazide to active 5-aminosalicylic acid by colonic bacteria |
| Moderate | Entecavir | Potential for increased entecavir exposure via renal transporter competition |
| Moderate | Lactobacillus acidophilus / Bifidobacterium longum infantis | Antibiotic activity may reduce viability of probiotic organisms |
| Minor | Allopurinol | Concomitant use increases incidence of amoxicillin-associated skin rash (mechanism unclear) |
| Minor | Azithromycin / Clarithromycin / Erythromycin | Overlapping spectrum; clinical benefit of combination is usually marginal |

Please refer to the package insert for complete warnings, contraindications, and special population guidance (Data Gap DG001 is currently unresolved).

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rank #1 — Polyclonal Hyperviscosity Syndrome)*

**Rationale:**
No clinical trials, observational studies, or published literature support the use of Amoxicillin in polyclonal hyperviscosity syndrome. The mechanistic connection is speculative and multi-step, and the TxGNN score reflects graph topology rather than direct biological evidence. There is no basis to initiate a repurposing programme for this specific indication.

---

### Clinically Noteworthy Signal — Rank #6: Monoclonal Gammopathy (IPSID Subtype)

Although the primary ranked prediction warrants a "Hold," this Evidence Pack contains one signal that merits genuine scientific attention:

**Rank #6 — Monoclonal Gammopathy / Immunoproliferative Small Intestinal Disease (IPSID)**
- **Evidence Level:** L3 (case series, observational studies, historical cohort data)
- **Recommendation:** Research Question
- **Mechanistic basis:** Amoxicillin is a cornerstone of *H. pylori* triple eradication therapy. IPSID (alpha heavy-chain disease), a subtype of monoclonal gammopathy affecting the proximal small bowel, is driven by chronic antigenic stimulation — principally by *H. pylori* and *Campylobacter jejuni*. Published case series demonstrate that antibiotic-based eradication can lead to histological tumour regression in early-stage disease, directly analogous to the *H. pylori* → gastric MALT lymphoma eradication model.
- **Supporting literature:** [PMID 8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) (Lancet, 1997 — regression of IPSID after H. pylori eradication), [PMID 20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) (J Gastrointest Cancer, 2010 — IPSID regression after H. pylori eradication), [PMID 9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) (Intern Med, 1996 — Mediterranean lymphoma treated with antibiotics)
- **Important caveat:** This mechanistic link applies specifically to IPSID/alpha-HCD and early antibiotic-responsive MALT-type lesions. It does **not** extend to MGUS, multiple myeloma, or non-IPSID monoclonal gammopathies.

**To proceed with the Rank #6 signal, the following steps are needed:**

1. **Systematic literature review** of antibiotic regimens for IPSID specifically — comparing amoxicillin-based vs. tetracycline-based eradication protocols
2. **Pathogen confirmation** — establish whether the target patient population has demonstrated *H. pylori* or *Campylobacter jejuni* as the driving antigen
3. **Prospective study design** — design a clinical protocol for antibiotic treatment of early-stage IPSID (Stage A/B per WHO classification), with histological response as primary endpoint
4. **Regulatory verification** — manually query CDSCO database to confirm Amoxicillin market status and approved formulations in India (resolves the regulatory data gap)
5. **Safety documentation** — obtain and parse the package insert PDF from TFDA/CDSCO to resolve Data Gap DG001 (warnings and contraindications)
6. **MOA documentation** — query DrugBank API for complete mechanism-of-action data to resolve Data Gap DG002, supporting mechanistic link analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

