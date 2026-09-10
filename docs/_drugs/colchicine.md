---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Colchicine: From Gout to Familial Mediterranean Fever (Autosomal Dominant)

## One-Sentence Summary

Colchicine is a tubulin-binding anti-inflammatory alkaloid classically used to treat and prevent acute gout flares. The TxGNN model additionally flags **Familial Mediterranean Fever, Autosomal Dominant** as a high-confidence predicted indication (score **99.38%**), backed by **20 publications** — including a 1977 *Lancet* landmark study — documenting colchicine as the long-established standard of care for preventing FMF attacks and amyloidosis, although this evidence pack contains no colchicine-specific RCT and the drug is not currently registered in this market.

*Note: this evidence pack (`TW-DB01394-multi`) contains three TxGNN-predicted indications for colchicine. This report focuses on the one with the strongest evidence and most actionable recommendation (FMF); the other two, lower-confidence candidates are summarized at the end.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no local license/label text available (drug not currently marketed here); classically indicated for acute gout flare treatment and prophylaxis |
| Predicted New Indication | Familial Mediterranean Fever, Autosomal Dominant |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L2 |
| Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this pack (MOA field is a data gap — see DG002). Based on known pharmacology, colchicine binds tubulin and inhibits neutrophil microtubule polymerization, blocking neutrophil chemotaxis and degranulation, and also suppresses pyrin/NLRP3 inflammasome activation. This is directly relevant to FMF, a disease driven by MEFV-gene/pyrin dysregulation that produces recurrent neutrophilic, IL-1β-mediated inflammation.

Gout and FMF are pathophysiologically related: both are neutrophil-driven, inflammasome/IL-1-mediated inflammatory conditions in which colchicine's anti-chemotactic, anti-inflammasome action limits acute attacks. This mechanistic overlap is why colchicine's proven efficacy in gout translates plausibly — and, per decades of clinical literature, has already translated in practice — to FMF.

Importantly, colchicine's role in FMF is not a novel hypothesis but a globally recognized first-line standard of care. The "not marketed" status in this evidence pack should be read as **this specific market lacking a registered license**, not as an absence of clinical evidence — the literature evidence below substantially predates and exceeds typical repurposing-candidate strength.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Recruiting | 25 | Real-world safety/effectiveness study of canakinumab (Ilaris®) in hereditary periodic fever syndromes including colchicine-resistant FMF (crFMF). **Note: tests canakinumab, not colchicine — only the patient population overlaps (relevance grade C), this is not direct colchicine efficacy evidence.** |

No trial in this pack directly evaluates colchicine in FMF; the single registered trial is an indirect population match with a comparator biologic.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [68234](https://pubmed.ncbi.nlm.nih.gov/68234/) | 1977 | Historical report | Lancet | Landmark early report establishing colchicine as effective therapy in FMF |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Review | Semin Arthritis Rheum | Colchicine is the "gold standard" FMF treatment, reducing attack frequency and amyloidosis risk; defines resistance/intolerance and alternatives |
| [25649364](https://pubmed.ncbi.nlm.nih.gov/25649364/) | 2014 | Review | Acta Med (Hradec Kralove) | Colchicine is the only agent shown to reduce amyloidosis development and attack frequency/severity in FMF |
| [35789271](https://pubmed.ncbi.nlm.nih.gov/35789271/) | 2023 | Cohort | Mod Rheumatol | Identifies early clinical predictors of colchicine resistance in FMF patients |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort | Int J Rheum Dis | Compares attack characteristics and renal outcomes in FMF patients on canakinumab with vs. without background colchicine |
| [38354004](https://pubmed.ncbi.nlm.nih.gov/38354004/) | 2023 | Review | La Revue du praticien | Long-term colchicine treatment prevents FMF attack recurrence |
| [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/) | 2010 | Review (toxicology) | Clin Toxicol | Colchicine has a narrow therapeutic index with no clear separation between nontoxic, toxic and lethal doses — key safety caveat |
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Review | Int J Mol Sci | Update on FMF including treatment resistance and compliance considerations |
| [29526329](https://pubmed.ncbi.nlm.nih.gov/29526329/) | 2018 | Review | La Revue de medecine interne | FMF pathophysiology via pyrin/IL-1 pathway, contextualizing colchicine's mechanism |
| [31705200](https://pubmed.ncbi.nlm.nih.gov/31705200/) | 2020 | Cohort/Review | Rheumatol Int | Colchicine treatment has altered the natural course of FMF but subclinical inflammation and atherosclerosis risk may persist |

---

## Safety Considerations

- **Drug Interactions**: 127 total interactions on file. Major-severity interactions include **Aprepitant, Clarithromycin, Eliglustat, Rolapitant, Cobicistat, Deferiprone, Rosuvastatin, Simvastatin** (largely CYP3A4/P-glycoprotein-mediated, raising colchicine toxicity risk). Moderate-severity interactions include Metronidazole, Cimetidine, Miconazole, Eluxadoline, Deferasirox, Fostamatinib, Ticagrelor, Chloroquine, Benznidazole, Disulfiram, Tinidazole, Strontium chloride Sr-89.
- Formal label warnings and contraindications are not yet available for this market (data gap DG001) — refer to the package insert once obtained, and note independently that colchicine has a narrow therapeutic index (see PMID 20586571 above).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Colchicine's role in FMF is supported by a strong, decades-deep literature base (L2) and a clear, disease-specific mechanistic rationale (pyrin/NLRP3 inflammasome suppression), and it is internationally recognized as first-line FMF therapy. However, this pack lacks a colchicine-specific RCT, a formal local drug label, and MOA documentation, so guardrails (safety data completion, DDI monitoring) are needed before a full Go.

**To proceed, the following is needed:**
- Local label/package-insert warnings and contraindications (DG001, Blocking — required before S1 safety review)
- Formal DrugBank/MOA documentation (DG002)
- Confirmation of route/formulation compatibility for chronic FMF maintenance dosing
- A monitoring plan for major CYP3A4/P-gp interactions (e.g., clarithromycin, cobicistat) given colchicine's narrow therapeutic index

---

## Other Predicted Indications (Lower Evidence — Not Recommended at This Time)

| Indication | TxGNN Score | Evidence Level | Recommendation | Why It's Weaker |
|---|---|---|---|---|
| Plasmodium falciparum malaria | 99.60% | L4 | Hold | Only 6 in-vitro mechanistic papers; effect is non-specific tubulin toxicity, and systemic toxicity (myelosuppression, GI, rhabdomyolysis) occurs well below antimalarial-effective concentrations |
| Dermatofibrosarcoma protuberans | 99.37% | L5 | Hold | No clinical trials or literature at all — pure knowledge-graph score; DFSP is driven by COL1A1-PDGFB/PDGFR signaling, mechanistically unrelated to microtubule inhibition |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

