---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix (Firmagon) is a GnRH receptor antagonist approved internationally for advanced prostate cancer, suppressing testosterone to castrate levels; it has no current registration in India.
The TxGNN model predicts it may be effective for **Hypertrichosis**, with **no clinical trials** and **no supporting publications** currently available for this specific indication.
The evidence base is limited to model prediction alone, warranting a **Hold** decision at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced prostate cancer (international approval; not marketed in India) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacology, Degarelix is a competitive GnRH (gonadotropin-releasing hormone) receptor antagonist. By directly blocking pituitary GnRH receptors — without the initial hormonal surge ("flare") seen with GnRH agonists — it rapidly suppresses LH and FSH secretion, driving testosterone to castrate levels within days. This makes it effective in advanced prostate cancer, where tumour growth is androgen-dependent.

The predicted new indication, **hypertrichosis**, refers to excessive hair growth occurring independently of androgen stimulation. This is a critical distinction from *hirsutism*, which is androgen-driven and would theoretically be more responsive to androgen deprivation. Hypertrichosis is most commonly congenital (e.g., Ambras syndrome), drug-induced, or paraneoplastic in origin — conditions where the HPG axis plays no primary pathogenic role.

While androgens do modulate hair follicle cycling in certain regions, the mechanistic bridge between GnRH receptor antagonism and non-androgenic hypertrichosis is weak and indirect. The high TxGNN score (99.99%) likely reflects network-level associations between this drug class and hair-related phenotypes in the knowledge graph, rather than a direct therapeutic mechanism. At present, this prediction lacks the biological rationale to justify clinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Degarelix in hypertrichosis.

---

## Literature Evidence

Currently no related literature available for Degarelix in hypertrichosis.

---

## Cytotoxicity

Degarelix is used in the treatment of advanced prostate cancer and falls within the oncology drug category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal/Targeted therapy (GnRH receptor antagonist) — not conventional cytotoxic |
| Myelosuppression Risk | Low (mechanism does not involve bone marrow suppression) |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum testosterone, PSA, liver function tests, QTc interval (ECG), bone mineral density (with long-term use) |
| Handling Protection | Standard precautions; does not require cytotoxic drug handling protocols |

---

## Safety Considerations

**Drug Interactions**: Degarelix has 217 documented interactions in the DDI database. A key pattern is **QT interval prolongation risk**, as Degarelix itself can prolong QTc. Co-administration with the following drugs carries the most clinically significant concern:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Cisapride | **Major** | Additive QT prolongation; risk of torsades de pointes |
| Dolasetron | **Major** | Additive QT prolongation; cardiac arrhythmia risk |
| Clarithromycin | Moderate | QT prolongation and CYP3A4 inhibition |
| Levofloxacin | Moderate | Additive QT prolongation |
| Ondansetron | Moderate | Additive QT prolongation |
| Granisetron | Moderate | Additive QT prolongation |
| Palonosetron | Moderate | Additive QT prolongation |
| Famotidine | Moderate | Electrolyte effects may compound QT risk |

> Please refer to the package insert for complete safety information including key warnings and contraindications. Full TFDA/CDSCO prescribing information was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a 99.99% prediction score, this reflects mathematical confidence within the knowledge graph model — not clinical evidence. Hypertrichosis is predominantly a non-androgenic disorder, and no clinical trials, observational studies, or mechanistic publications support the use of GnRH antagonism for this condition. The drug is also not registered in India, adding a further regulatory barrier.

**To proceed, the following is needed:**
- Obtain full package insert (TFDA/EMA Firmagon SmPC) to complete safety profiling (warnings, contraindications)
- Retrieve DrugBank MOA entry to formally characterise mechanism and explore class-level evidence
- Conduct a focused literature review on androgenic vs. non-androgenic hypertrichosis subtypes to determine whether any subgroup could benefit from androgen suppression
- If sub-indication of interest shifts to *hirsutism* (androgenic type) or *central precocious puberty* (Rank 9, L4 evidence), the mechanistic rationale becomes substantially stronger and may warrant a Research Question designation
- Assess feasibility of India regulatory registration as a prerequisite for any clinical programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

