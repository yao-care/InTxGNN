---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 4
---

# Codeine
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

# Codeine: From Analgesic/Antitussive Use to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid historically used as an analgesic and antitussive (cough suppressant); no original indication or approval record is present in this Evidence Pack, and detailed mechanism-of-action data is a confirmed data gap. TxGNN predicts a possible link to **Nasal Cavity Disease** with a very high score, but the only supporting literature (2 case reports) describes intranasal opioid **abuse causing tissue necrosis and rhinolithiasis** — i.e., harm, not therapeutic benefit — and no clinical trials exist for this pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this Evidence Pack (Codeine is generally known as an opioid analgesic/antitussive; DG002 flags MOA as a data gap) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (2 case reports only; no trials, no mechanistic support) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Codeine is not available in this Evidence Pack (DG002, High severity). Based on general pharmacological knowledge, Codeine is a mu-opioid agonist used systemically for pain and centrally to suppress cough — neither mechanism has an established link to primary nasal cavity pathology.

Critically, the literature returned for this pairing does **not** support a therapeutic hypothesis. Both PubMed hits (PMID 22965281, PMID 17315836) describe **intranasal abuse of opioid-containing products causing tissue necrosis, rhinolithiasis, and a foreign-body "opioma"** — these are adverse/toxic events, not evidence of treatment efficacy. One of the two reports concerns hydrocodone-acetaminophen, not Codeine itself, further weakening the direct evidence base.

The TxGNN score of 99.93% most likely reflects a **co-occurrence artifact** (Codeine and nasal-cavity terms appear together in adverse-event literature) rather than a genuine repurposing signal. The same pattern repeats across the other top-ranked predictions in this pack: acute laryngopharyngitis (L5, no evidence at all), trigeminal autonomic cephalalgia (L4, headache-society guidance explicitly discourages opioids), and allergic urticaria (L4, literature shows Codeine **causes** mast-cell degranulation/urticaria rather than treating it). All four were independently scored "Hold" in the source evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case report | The Laryngoscope | Intranasal hydrocodone-acetaminophen abuse caused necrosis of the nasal cavity and pharynx — adverse event, not therapeutic use |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | Rhinolithiasis ("opioma") formed around an impacted mixture of codeine and opium in the nasal cavity — foreign-body/toxicity case, not treatment evidence |

---

## India Market Information

No registration records available — Codeine is currently not marketed in this jurisdiction under this Evidence Pack (0 licenses on file).

---

## Safety Considerations

- **Drug Interactions**: Database query returned 449 total interactions. Notable examples include **Major**-level interactions with Alvimopan and Bupropion, and **Moderate**-level interactions with Atropine, Cimetidine, Dexamethasone, Dronabinol, Eliglustat, Eluxadoline, Glycopyrronium, Granisetron, Hyoscyamine, and Loperamide, among others (source: DDInter).

Key warnings and contraindications from the local product label are not yet available (DG001, Blocking severity) — please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is supported only by two case reports describing opioid-related nasal tissue injury, not therapeutic benefit — the mechanistic direction is inverted relative to what would justify repurposing. This pattern holds across all four top predictions in the pack, none of which have supporting trials or a coherent MOA-to-indication rationale. Codeine is also not currently marketed in this jurisdiction, and label-level safety data (DG001) is a blocking gap.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) — currently blocking
- Confirmed mechanism of action from DrugBank or primary literature
- Re-evaluation of TxGNN candidate list against literature co-occurrence bias (adverse-event mentions should be filtered from training/scoring)
- If any indication is pursued further, dedicated preclinical or observational evidence specific to a therapeutic (not toxic) relationship
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

