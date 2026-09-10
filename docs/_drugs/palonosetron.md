---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 633
evidence_level: L5
indication_count: 5
---

# Palonosetron
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

# Palonosetron: From CINV/PONV to Migraine Disorder

## One-Sentence Summary

Palonosetron is a highly selective 5-HT3 receptor antagonist used for chemotherapy- and postoperative-induced nausea and vomiting (CINV/PONV). TxGNN predicts a possible link to **Migraine Disorder** with a 99.74% score, but this is currently supported by **0 clinical trials** and only **1 case report** — and that single report describes palonosetron *causing* migraine-type headache as an adverse effect, not treating it. This is a low-confidence, mechanistically unsupported signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not in local registry (drug not marketed); per known drug class, used for CINV/PONV |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal mechanism-of-action record is not available for this candidate (data gap DG002). Based on known pharmacology noted in the associated evidence, palonosetron is a highly selective **5-HT3 receptor antagonist**, used to prevent chemotherapy- and surgery-induced nausea/vomiting by blocking serotonin signaling at the chemoreceptor trigger zone and vagal afferents.

Migraine, by contrast, is primarily managed through **5-HT1B/1D receptor agonism** (e.g., triptans), a distinct serotonergic pathway from the 5-HT3 antagonism palonosetron provides. There is no established pharmacological rationale connecting 5-HT3 blockade to migraine prevention or treatment. The high TxGNN score most likely reflects shared "serotonin/neurotransmission" graph neighborhoods rather than a genuine therapeutic mechanism.

Critically, the only literature retrieved for this pairing is a case report titled *"Palonosetron-induced migraine-type headache"* — this documents palonosetron as a **trigger** of migraine-type headache (an adverse event), which is the opposite of therapeutic evidence. This is a negative/contradictory signal, not supportive evidence.

*(For transparency: this same prediction batch also generated four additional candidates for palonosetron — migraine with brainstem aura, migraine susceptibility, atrophoderma vermiculata, and ulerythema ophryogenesis — all rated L5/Hold with no supporting trials or literature. The pattern across this batch suggests TxGNN graph-co-occurrence noise for this drug rather than genuine repurposing signals.)*

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report (Adverse Event) | Canadian Journal of Anaesthesia | Documents palonosetron **inducing** migraine-type headache as an adverse effect — this is a safety signal, not evidence of therapeutic benefit for migraine. |

---

## India Market Information

Palonosetron currently has **0 registrations** and is **not marketed** in this jurisdiction, so no local authorization records are available.

---

## Safety Considerations

- **Drug Interactions**: 398 total interactions identified. Notable **Major**-level interactions include several serotonergic and QT-prolonging agents: Fentanyl, Dextromethorphan, Tramadol, Alfentanil, Amiodarone, Amisulpride, Amitriptyline, Anagrelide, and — notably — the triptans **Almotriptan** and **Sumatriptan**. This last point is directly relevant to the proposed migraine indication: standard first-line migraine therapy (triptans) carries a **Major** interaction risk (serotonin syndrome) with palonosetron, which would complicate any real-world repurposing even if efficacy were later established. Additional **Moderate**-level interactions include Famotidine, Propofol, Loperamide, Adenosine, Salbutamol, and Formoterol.

Detailed key warnings and contraindications are not currently available (data gap DG001, flagged as Blocking) — refer to the package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but all substantive evidence contradicts rather than supports the hypothesis: the single literature hit describes palonosetron *causing* migraine-type headache, there are zero clinical trials, and the underlying mechanism (5-HT3 antagonism) does not align with established migraine pharmacology (5-HT1B/1D agonism). Combined with a Blocking safety data gap (no TFDA warnings/contraindications available) and a Major-level DDI conflict with triptans — the standard migraine therapy — this candidate does not warrant progression past S0.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Preclinical or mechanistic studies establishing a plausible causal link between 5-HT3 antagonism and migraine pathophysiology (none currently exist)
- Re-review of whether this candidate should remain in the pipeline at all, given the sole evidence is an adverse-event report contradicting the hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

