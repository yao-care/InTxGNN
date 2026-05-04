---
layout: default
title: Amineptine
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Amineptine
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

# Amineptine: From Depression to Agoraphobia

## One-Sentence Summary

Amineptine is a tricyclic antidepressant with a unique dopaminergic mechanism (dopamine-norepinephrine reuptake inhibitor, NDRI), historically used across multiple countries for depressive disorders before being withdrawn from most markets due to documented abuse potential.
The TxGNN model predicts it may be effective for **Agoraphobia** as the highest-ranked new indication (score 99.97%),
with **0 clinical trials** and **1 indirectly related publication** supporting this specific direction. Notably, stronger mechanistic and clinical evidence exists for **neurotic depression** (rank 4) and **melancholia** (rank 6), each supported by multiple RCTs at evidence level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration; historically used for depression (per pharmacological literature) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No formal mechanism of action data is available in this evidence pack. Based on pharmacological literature (PMID 9347388), Amineptine is a tricyclic-derived compound that **selectively inhibits dopamine reuptake** at the dopamine transporter (DAT), with secondary norepinephrine reuptake inhibition. This NDRI profile distinguishes it sharply from serotonin-dominant antidepressants (SSRIs, clomipramine) and classical tricyclics with broad receptor blockade. Its active metabolite, 7-OH amineptine, contributes additional pharmacological activity. Importantly, Amineptine lacks the significant anticholinergic and cardiotoxic effects typical of older tricyclics — a profile confirmed in multiple clinical comparator trials.

The predicted link to agoraphobia rests on a theoretical connection: dopaminergic modulation of the mesolimbic system and prefrontal cortex may influence avoidance behavior, motivational deficits, and the behavioral inhibition that characterizes agoraphobia. However, agoraphobia is primarily driven by serotonergic and GABAergic fear circuitry centered on the amygdala, and first-line pharmacological treatments are SSRIs and benzodiazepines — not dopaminergic agents. The mechanistic pathway from dopamine reuptake inhibition to agoraphobia relief is speculative and indirect.

The sole literature citation retrieved for this indication (PMID 7717094) examines **reversible MAO-A inhibitors** (moclobemide, brofaromine, toloxatone) — drugs with a fundamentally different mechanism — for panic disorder and agoraphobia. Amineptine appears only as a comparator in the depression treatment context. The TxGNN score for agoraphobia most likely reflects knowledge graph proximity between anxiety-spectrum disorders and depressive disorders, rather than a direct pharmacological signal. In contrast, neurotic depression (rank 4) and melancholia (rank 6) are supported by direct RCT evidence at L2, suggesting a meaningful divergence between the model's ranking and the clinical evidence hierarchy.

---

## Clinical Trial Evidence

No clinical trials evaluating Amineptine for agoraphobia are currently registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Narrative Review | *Acta Psychiatrica Scandinavica* (Supplement) | Reviews reversible MAO-A inhibitors (moclobemide, brofaromine, toloxatone) for depression and panic/agoraphobia; Amineptine is mentioned only as a comparator for antidepressant efficacy, not as a treatment candidate for agoraphobia — evidence is indirect |

> **Interpretation note**: This single publication does not evaluate Amineptine specifically for agoraphobia. It is classified as indirect (Tier 3) evidence. The study type and mechanism covered are unrelated to Amineptine's dopaminergic MOA.

---

## India Market Information

Amineptine holds no regulatory approvals or marketing authorizations in India (CDSCO). There are no registered products, no approved indications on record, and no active licenses. The drug is classified as **not marketed** in India.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Critical safety signals identified from literature evidence in this evidence pack:**

- **Abuse and dependence liability**: Case series document an amineptine dependence syndrome, including in patients with psychiatric comorbidities such as schizophrenia (PMID [7986891](https://pubmed.ncbi.nlm.nih.gov/7986891/)). A history of amineptine misuse has also been associated with subsequent substance dependence (PMID [18636997](https://pubmed.ncbi.nlm.nih.gov/18636997/)). Amineptine was formally **withdrawn from the French market** and several others specifically due to its abuse potential — a direct consequence of its dopamine-releasing/reuptake-blocking mechanism acting on reward circuitry.
- **Dermatological toxicity**: Dose-related acneiform skin eruptions (retentional lesions) have been documented and described as dose-dependent (PMID [11730047](https://pubmed.ncbi.nlm.nih.gov/11730047/)).
- **Psychiatric risk in vulnerable populations**: Dopamine-enhancing effects may theoretically exacerbate psychotic symptoms or agitation in patients with schizophrenia-spectrum disorders — a concern directly reflected in PMID 7986891. This is especially relevant given several of the TxGNN top-10 predictions involve personality disorders on the schizophrenia spectrum (ranks 8–10).
- **Hepatotoxicity (historical reports)**: Although not captured in the structured safety fields of this pack, Amineptine has historical case reports of hepatotoxic reactions; liver function monitoring was emphasized in clinical trials (PMID [2698271](https://pubmed.ncbi.nlm.nih.gov/2698271/)).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Amineptine in agoraphobia is limited to Level 4 (indirect mechanistic inference), with no registered clinical trials and no directly relevant literature. More critically, Amineptine carries well-documented abuse/dependence liability that led to market withdrawal in multiple countries, representing a regulatory and ethical barrier that takes precedence over any repurposing potential at this stage.

**To proceed, the following is needed:**

- **Safety dossier**: Comprehensive review of Amineptine's controlled substance and abuse-potential status across major regulatory jurisdictions (EMA, US FDA, CDSCO) before any repurposing pathway can be evaluated
- **Regulatory feasibility assessment**: Clarify whether Amineptine is legally obtainable and developable for new indications in India given its withdrawal history
- **Formal MOA documentation**: Retrieve full DrugBank entry to confirm mechanism, targets, and known pharmacodynamic interactions
- **TFDA/CDSCO prescribing information**: Download and parse package insert PDFs to extract formal warnings, contraindications, and interaction profiles (currently blocking data gap DG001)
- **Re-evaluation of indication priority**: If regulatory and safety barriers can be addressed, neurotic depression (rank 4, L2 evidence, multiple RCTs) and melancholia (rank 6, L2 evidence) present a far stronger mechanistic and clinical rationale for repurposing compared to agoraphobia (rank 1, L4 evidence) — a reordering of priorities is recommended
- **Preclinical anxiety models**: If agoraphobia is to be pursued at all, in vivo dopaminergic modulation data in anxiety models would be required to advance beyond L4 evidence

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

