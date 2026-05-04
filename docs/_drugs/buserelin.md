---
layout: default
title: Buserelin
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 5
---

# Buserelin
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

# Buserelin: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Buserelin is a GnRH (gonadotropin-releasing hormone) agonist used clinically in the treatment of prostate cancer through suppression of sex hormone production via pituitary desensitization.
The TxGNN model predicts it may be effective for **Hypertrichosis**, with **0 clinical trials** and **1 publication** currently supporting this direction — making the evidence base extremely thin.
The single available publication addresses a rare genetic syndrome in which Buserelin plays no direct therapeutic role, and all five predicted indications in this pack are rated **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (sex hormone suppression therapy) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the pharmacology information retrieved, Buserelin is a synthetic GnRH agonist that targets the **GnRH1 receptor** (GNRHR, gene ID 2798). Paradoxically, chronic administration causes pituitary receptor downregulation, ultimately suppressing LH, FSH, and downstream sex hormones (testosterone and estrogen) — a state known as medical castration. This makes it effective in androgen-sensitive prostate cancer.

The theoretical bridge to hypertrichosis is built on the androgen axis: androgen-driven hair growth (as seen in hirsutism) can theoretically be reduced by androgen suppression. However, **hypertrichosis and hirsutism are pathophysiologically distinct**. Hypertrichosis denotes excess hair growth that is fundamentally non-androgenic in origin — its causes include genetic channelopathies (e.g., Cantú syndrome via ABCC9/KCNJ8 mutations), chromosomal rearrangements, and keratin structural defects. In these settings, GnRH axis manipulation has no meaningful biological rationale.

The sole supporting literature (PMID 31743099) documents a Cantú syndrome patient who developed multiple pituitary hormone deficiencies — a case emphasising the need for endocrine monitoring, not Buserelin therapy. The TxGNN high score for this group of indications most likely reflects shared "hair disorder" node proximity in the knowledge graph rather than a true drug–disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Case Report | *Endocrinology, Diabetes & Metabolism Case Reports* | Cantú syndrome (hypertrichotic osteochondrodysplasia) presenting with multiple pituitary hormone deficiencies at age 13; supports endocrine monitoring in this rare genetic condition but contains no data on Buserelin treatment or hypertrichosis management |

---

## India Market Information

Buserelin currently has **no registered products in India** (0 approved licenses). Any clinical development pathway would require a full new drug application with CDSCO.

---

## Cytotoxicity

Buserelin is used in prostate cancer management and is classified as a hormonal anticancer agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal therapy — GnRH agonist (not conventional cytotoxic) |
| Myelosuppression Risk | Low — acts via hormonal suppression, no direct myelotoxic mechanism |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum testosterone/estradiol levels, bone mineral density (risk of osteoporosis with prolonged use), liver function tests |
| Handling Protection | Standard drug handling applies; dedicated cytotoxic handling protocols are not required |

---

## Safety Considerations

**Drug–Target Interaction:**
Buserelin binds the **GnRH1 receptor** (GNRHR; Entrez Gene 2798, Ensembl ENSG00000109163) as a peptide agonist. Known trade names include Suprefact®, Metrelef®, and Receptal. Sustained GnRH receptor stimulation leads to desensitisation and sex hormone suppression — the basis for its clinical use but also a source of class-effect risks (hot flushes, bone loss, metabolic effects).

Detailed warnings, contraindications, and drug interaction data from an Indian or international package insert were not available in the current evidence pack. Please refer to the originator SmPC (Suprefact® or equivalent) for complete prescribing safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for Buserelin are rated L5 (model prediction only, no clinical studies) with a unanimous Hold recommendation. The top-ranked prediction — hypertrichosis — lacks mechanistic plausibility because the predominant forms of this condition are non-androgenic (genetic channelopathies, chromosomal defects, keratin mutations) and therefore fall outside the GnRH–androgen axis that Buserelin modulates. The single supporting publication does not provide any clinical evidence for Buserelin's efficacy in any hair disorder.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Identify whether any clinical subtype of hypertrichosis has a confirmed androgen-dependent component amenable to GnRH agonist suppression
- **Preclinical data**: Animal or ex vivo hair follicle models demonstrating Buserelin's effect on non-androgenic hypertrichosis
- **Targeted literature search**: Systematic search combining GnRH agonists with hypertrichosis, hirsutism, and hair shaft disorders (current evidence pack returned only 1 peripheral case report)
- **Safety package**: Retrieve full package insert (warnings, contraindications, teratogenicity data) from the Suprefact® SmPC or equivalent international label
- **India regulatory pathway assessment**: Determine whether a new drug application, or an extension of indication under an existing global dossier, is feasible given zero current India registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

