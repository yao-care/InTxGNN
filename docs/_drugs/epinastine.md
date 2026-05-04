---
layout: default
title: Epinastine
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 2
---

# Epinastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Epinastine: From Allergic Conjunctivitis to Allergic Urticaria

## One-Sentence Summary

Epinastine (Elestat®/Alesion®) is a second-generation H1 antihistamine and mast cell stabilizer originally approved as an ophthalmic formulation for the treatment of allergic conjunctivitis.
The TxGNN model predicts it may be effective for **Allergic Urticaria** (score 99.28%), supported by **2 completed real-world surveillance studies** and **11 publications**.
A separate top-ranked prediction for **Rosacea Conjunctivitis** (score 99.57%, rank #1) currently has no clinical evidence and is classified as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic conjunctivitis (ocular pruritus) — ophthalmic formulation |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Epinastine is a selective second-generation H1 receptor antagonist (targeting HRH1, Entrez Gene ID: 3269) with documented low central nervous system penetration. Although formal MOA data from DrugBank was not available in this evidence pack, published pharmacological reviews (PMID 12845334) confirm that beyond H1 blockade, epinastine also inhibits leukotriene release, platelet-activating factor (PAF), bradykinin activity, and directly suppresses mast cell degranulation — as well as post-transcriptional inhibition of IL-8 release from eosinophils.

Allergic urticaria is driven by IgE-mediated mast cell activation, triggering histamine release that produces the classic wheal-and-flare response, vasodilation, and pruritus. This is precisely the pathway epinastine targets at multiple levels (H1 blockade + mast cell stabilisation), making the mechanistic rationale direct and well-established — not an indirect inference. The TxGNN score of 99.28% (global rank #11,188) reflects strong phenotypic overlap between the original indication (mast cell-driven ocular allergy) and the predicted indication (systemic mast cell-driven urticaria).

Crucially, this prediction is already validated by regulatory precedent: in Japan, oral Alesion® (epinastine hydrochloride) carries an approved label that explicitly includes urticaria among its indications. Post-marketing surveillance data from over 5,700 Japanese patients further confirms real-world safety and efficacy for this indication class, substantially de-risking the repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02238236](https://clinicaltrials.gov/study/NCT02238236) | N/A (PMS) | Completed | 3,793 | Large real-world post-marketing surveillance of Alesion® Dry Syrup in Japanese paediatric patients; confirmed safety and tolerability for allergic rhinitis, urticaria, eczema/dermatitis, and pruritus in daily clinical practice |
| [NCT02238223](https://clinicaltrials.gov/study/NCT02238223) | N/A (PMS) | Completed | 2,001 | Post-marketing surveillance of Alesion® Tablet across multiple allergic indications including urticaria, prurigo, and psoriasis vulgaris with itching; conducted following revised Japanese treatment guidelines |

> **Important note:** Both studies are non-interventional post-marketing surveillance designs (no control arm, no randomisation). Together they cover 5,794 real-world patients and provide robust safety evidence, but are insufficient to establish superiority over comparators. No randomised controlled trials specifically targeting urticaria were identified for epinastine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/) | 1999 | RCT (double-blind crossover) | Allergy | Head-to-head comparison of 6 H1-antagonists including epinastine vs. placebo; demonstrated 24-hour suppression of histamine-induced wheal-and-flare — the core pharmacodynamic endpoint for urticaria efficacy |
| [19558008](https://pubmed.ncbi.nlm.nih.gov/19558008/) | 2009 | Comparative clinical study | Ann Allergy Asthma Immunol | Compared first- vs. second-generation antihistamines in suppressing histamine- and allergen-induced skin reactions; supports the role of second-generation agents (including epinastine) in urticaria management |
| [12845334](https://pubmed.ncbi.nlm.nih.gov/12845334/) | 2000 | Systematic Review | Drugs of Today | Comprehensive pharmacology review confirming epinastine's multi-target antiallergic profile (H1, anti-leukotriene, anti-PAF, mast cell stabilisation, eosinophil inhibition) — all relevant to urticaria pathophysiology |
| [15510239](https://pubmed.ncbi.nlm.nih.gov/15510239/) | 2004 | Clinical Review | Drugs of Today | Review of epinastine for atopic diseases including skin urticaria; contextualises H1 blockade in controlling itching, tearing, and urticarial skin response |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Clinical pharmacology | An Bras Dermatol | Brazilian comparative study of H1 antihistamines including epinastine for wheal-and-flare suppression in dermatological conditions including urticaria |
| [11829715](https://pubmed.ncbi.nlm.nih.gov/11829715/) | 2002 | Narrative Review | Expert Opin Investig Drugs | Reviews antihistamines in chronic idiopathic urticaria; discusses shared pathological mechanisms across allergic diseases and the profile of late-phase agents including epinastine |
| [18524543](https://pubmed.ncbi.nlm.nih.gov/18524543/) | 2008 | Immunological study | J Dermatol Sci | Demonstrates antihistamine (including epinastine) regulatory effects on monocyte-derived dendritic cells and CD4+ T cells in urticaria and atopic dermatitis; provides mechanistic evidence for immune-modulatory activity beyond H1 blockade |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Large observational study | Methods Find Exp Clin Pharmacol | Large-scale surveillance (n=1,742) quantifying sedation profiles of H1-antihistamines including epinastine via VAS; confirms low sedation risk — a clinically meaningful safety differentiator for urticaria management |
| [34387278](https://pubmed.ncbi.nlm.nih.gov/34387278/) | 2021 | Receptor affinity study | Curr Opin Allergy Clin Immunol | Receptor profiling study for ophthalmic and systemic agents; contextualises epinastine's H1 receptor activity in the landscape of mast cell-driven inflammatory eye and skin diseases |
| [10876807](https://pubmed.ncbi.nlm.nih.gov/10876807/) | 2000 | Narrative Review | Folia Pharmacol Jpn | Benchmarking study citing epinastine among H1 antihistamines; notes pharmacodynamic activity in wheal-response suppression versus cetirizine and other second-generation agents |

---

## India Market Information

Epinastine is currently **not marketed in India**. No product registrations or CDSCO approvals were found in this evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No records found |

> **For reference:** In Japan, Alesion® (epinastine hydrochloride) is approved for allergic rhinitis, eczema/dermatitis, urticaria, pruritus, prurigo, psoriasis vulgaris with itching, and bronchial asthma. In the United States, Elestat® (ophthalmic solution) is approved for ocular pruritus associated with allergic conjunctivitis. Neither product holds an Indian registration at the time of this report.

---

## Safety Considerations

Formal warning and contraindication data from an Indian package insert (CDSCO label) was not available in this evidence pack and represents a blocking data gap for a full S1 safety evaluation.

Based on available pharmacological and surveillance data:

- **Drug Interaction (Pharmacological):** Epinastine acts as a selective H1 receptor ligand (HRH1; Ensembl: ENSG00000196639). Additive sedation with CNS depressants is theoretically possible, though epinastine's low CNS penetration substantially reduces this risk compared to first-generation antihistamines.
- **Sedation Profile:** Large-scale Japanese surveillance (n=1,742; PMID 18597008) confirms epinastine is classified as a non-sedating second-generation antihistamine — a clinically important distinction for patients requiring daytime use.

> Please refer to the full package insert for complete safety information, including contraindications, special population warnings (pregnancy, renal/hepatic impairment), and drug interaction details.

---

## Conclusion and Next Steps

### Primary Recommendation: Allergic Urticaria

**Decision: Proceed with Guardrails**

**Rationale:**
Epinastine's mechanism of action directly and specifically addresses the core pathophysiology of allergic urticaria (H1 blockade + mast cell stabilisation), the drug already holds regulatory approval for urticaria in Japan, and real-world safety is supported by data from over 5,700 patients. The mechanistic case is strong, the evidence base is consistent, and regulatory precedent exists in a comparable market.

**To proceed, the following is needed:**
- Obtain the Indian package insert (CDSCO) to complete the S1 blocking safety gap (DG001)
- Confirm formal MOA documentation from DrugBank (DG002) to strengthen mechanistic dossier
- Identify an Indian partner or generic manufacturer holding oral epinastine formulation rights
- Conduct a competitive landscape assessment against first-line urticaria treatments already approved in India (cetirizine, loratadine, fexofenadine)
- Design a bridging PK/PD or comparative efficacy study in the Indian patient population if a formal indication application is planned

---

### Secondary Prediction: Rosacea Conjunctivitis (TxGNN Rank #1, Score 99.57%)

**Decision: Hold**

**Rationale:**
Despite achieving the highest TxGNN score, rosacea conjunctivitis is primarily driven by neurovascular dysregulation — not histamine-mediated inflammation. The mechanistic link to epinastine's H1/mast cell mechanism is indirect at best. No clinical trials, no ICTRP registrations, and no publications were found to support this specific indication.

**To reactivate this prediction, the following would be needed:**
- Preclinical studies demonstrating H1 antagonism or mast cell stabilisation efficacy in rosacea conjunctivitis models
- Exploratory clinical case series or mechanistic pilot studies
- Biomarker evidence of histamine involvement in rosacea conjunctivitis pathogenesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

